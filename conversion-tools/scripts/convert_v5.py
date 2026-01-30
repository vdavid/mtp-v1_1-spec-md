#!/usr/bin/env python3
"""
Improved PDF text to Markdown converter v5.
Hybrid approach: split on spaces for cells, but use positions for continuation merging.
"""

import re
from typing import List, Tuple, Optional
from dataclasses import dataclass

# Page header/footer patterns
PAGE_HEADER_PATTERN = re.compile(r'^Revision\s+1\.1\s+April\s+6.*2011\s+\d+\s*$')
COPYRIGHT_LINES = [
    'USB Media Transfer Protocol Specification',
    'Copyright © 2011, USB Implementers Forum',
    'All Rights Reserved'
]

def is_page_break_line(line: str) -> bool:
    """Check if line is part of page header/footer."""
    stripped = line.strip()
    if PAGE_HEADER_PATTERN.match(stripped):
        return True
    if stripped == 'th':  # Superscript artifact
        return True
    for copyright_line in COPYRIGHT_LINES:
        if copyright_line in stripped:
            return True
    return False

def is_toc_line(line: str) -> bool:
    """Check if line is a TOC entry (has dots leading to page number)."""
    return bool(re.search(r'\.{3,}\s*\d+\s*$', line))

def extract_toc(lines: List[str], start_idx: int) -> Tuple[List[str], int]:
    """Extract TOC from lines starting at start_idx."""
    toc_entries = []
    i = start_idx

    while i < len(lines):
        line = lines[i]

        if is_page_break_line(line):
            i += 1
            continue

        if not line.strip():
            i += 1
            continue

        if is_toc_line(line):
            toc_entries.append(line)
            i += 1
            continue

        stripped = line.strip()
        if re.match(r'^\d+\s+[A-Z]', stripped) and '...' not in stripped:
            break

        if re.match(r'^\s+\d+\.\d+', stripped) or re.match(r'^\s+[A-Z]\.\d+', stripped):
            toc_entries.append(line)
            i += 1
            continue

        i += 1

    return toc_entries, i

def format_toc(toc_lines: List[str]) -> str:
    """Format TOC entries as markdown."""
    result = ["## Table of Contents\n"]

    for line in toc_lines:
        clean = line.rstrip()
        match = re.match(r'^(\s*)(.+?)\.{2,}\s*(\d+)\s*$', clean)
        if match:
            indent = match.group(1)
            text = match.group(2).strip()
            page = match.group(3)
            indent_level = len(indent) // 2
            slug = re.sub(r'[^\w\s-]', '', text.lower())
            slug = re.sub(r'[\s_]+', '-', slug).strip('-')
            result.append('  ' * indent_level + f'- [{text}](#{slug}) (p.{page})')
        else:
            text = clean.strip()
            if text and text != 'Table of Contents':
                indent = len(clean) - len(clean.lstrip())
                indent_level = indent // 2
                result.append('  ' * indent_level + f'- {text}')

    return '\n'.join(result)

@dataclass
class CellInfo:
    text: str
    start_pos: int
    end_pos: int

def split_line_with_positions(line: str) -> List[CellInfo]:
    """
    Split line by 2+ spaces, recording start and end positions of each cell.
    """
    cells = []
    i = 0

    # Skip leading whitespace
    while i < len(line) and line[i] == ' ':
        i += 1

    while i < len(line):
        # Start of cell
        start = i

        # Find end of cell (next 2+ spaces or end of line)
        while i < len(line):
            if line[i] == ' ':
                # Check if this is 2+ spaces
                space_start = i
                while i < len(line) and line[i] == ' ':
                    i += 1
                if i - space_start >= 2:
                    # End of cell
                    cells.append(CellInfo(line[start:space_start].strip(), start, space_start))
                    break
                # Just 1 space, continue with cell
            else:
                i += 1

        # End of line - last cell
        if i >= len(line) and start < len(line):
            text = line[start:].strip()
            if text:
                cells.append(CellInfo(text, start, len(line)))

    return cells

def find_best_matching_column(pos: int, col_starts: List[int]) -> int:
    """
    Find which column a position best matches based on nearest column start.
    Uses a simple nearest-neighbor approach with bias toward later columns
    when position is between two column starts.
    """
    if not col_starts:
        return -1

    # Find the column whose start is closest to pos
    # If pos is exactly between two columns, prefer the earlier one
    best_col = 0
    for i in range(len(col_starts)):
        if col_starts[i] <= pos:
            best_col = i
        else:
            # pos is before this column's start
            # Check if it's closer to this column or the previous one
            if i > 0:
                dist_to_prev = pos - col_starts[i - 1]
                dist_to_curr = col_starts[i] - pos
                if dist_to_curr < dist_to_prev:
                    best_col = i
            break

    return best_col

def merge_header_continuation(header_cells: List[CellInfo], cont_cells: List[CellInfo]) -> List[str]:
    """
    Merge header continuation line with header based on positions.
    """
    # Build list of column start positions
    col_starts = [c.start_pos for c in header_cells]
    merged = [c.text for c in header_cells]

    for cont in cont_cells:
        # Find which header column this continuation belongs to
        best_col = find_best_matching_column(cont.start_pos, col_starts)
        if best_col >= 0 and best_col < len(merged):
            merged[best_col] = merged[best_col] + ' ' + cont.text

    return merged

def is_data_continuation(line: str) -> bool:
    """Check if line is a data continuation (starts with significant whitespace)."""
    if not line.strip():
        return False

    leading_spaces = len(line) - len(line.lstrip())
    return leading_spaces > 3  # More than 3 spaces = likely continuation

def merge_data_continuation(current_row: List[str], cont_cells: List[CellInfo],
                           col_starts: List[int]) -> List[str]:
    """
    Merge continuation cells into current row based on position matching.
    """
    for cont in cont_cells:
        best_col = find_best_matching_column(cont.start_pos, col_starts)
        if best_col >= 0 and best_col < len(current_row):
            if current_row[best_col]:
                current_row[best_col] += ' ' + cont.text
            else:
                current_row[best_col] = cont.text

    return current_row

def is_likely_table_header(line: str) -> bool:
    """Check if line looks like a table header."""
    if '  ' not in line:  # Must have multi-space gaps
        return False

    stripped = line.strip().lower()
    header_words = ['field', 'size', 'datatype', 'description', 'value', 'code',
                    'name', 'type', 'format', 'bytes', 'bit', 'bits', 'order',
                    'datacode', 'operation', 'response', 'event', 'property']

    word_count = sum(1 for word in header_words if word in stripped)
    return word_count >= 2

def is_header_continuation_pattern(line: str) -> bool:
    """Check if line looks like a header continuation."""
    stripped = line.strip().lower()
    # Common header continuation patterns
    if re.match(r'^[\d\-]+$', stripped):  # Just numbers like "15", "9-0"
        return True
    if stripped in ['order', '(bytes)', '(bits)']:
        return True
    # Multiple numbers/short words separated by spaces
    parts = stripped.split()
    if all(re.match(r'^[\d\-]+$', p) or p in ['order', '(bytes)', '(bits)'] for p in parts):
        return True
    return False

def table_to_markdown(headers: List[str], rows: List[List[str]]) -> str:
    """Convert headers and rows to markdown table."""
    if not headers:
        return ''

    num_cols = len(headers)

    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row[:num_cols]):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(cell))

    col_widths = [max(w, 3) for w in col_widths]

    lines = []

    # Header
    header_cells = [headers[i].ljust(col_widths[i]) for i in range(num_cols)]
    lines.append('| ' + ' | '.join(header_cells) + ' |')

    # Separator
    lines.append('| ' + ' | '.join('-' * w for w in col_widths) + ' |')

    # Data rows
    for row in rows:
        cells = [(row[i] if i < len(row) else '').ljust(col_widths[i]) for i in range(num_cols)]
        lines.append('| ' + ' | '.join(cells) + ' |')

    return '\n'.join(lines)

def extract_table(lines: List[str], start_idx: int) -> Tuple[Optional[str], int]:
    """Extract a table starting at start_idx."""
    header_line = lines[start_idx]
    header_cells = split_line_with_positions(header_line)

    if len(header_cells) < 2:
        return None, start_idx

    i = start_idx + 1

    # Check for header continuation
    if i < len(lines) and is_header_continuation_pattern(lines[i]):
        cont_cells = split_line_with_positions(lines[i])
        headers = merge_header_continuation(header_cells, cont_cells)
        i += 1
    else:
        headers = [c.text for c in header_cells]

    # Build column start positions from header for data matching
    col_starts = [cell.start_pos for cell in header_cells]

    num_cols = len(headers)

    # Read data rows
    rows = []
    current_row = None

    while i < len(lines):
        line = lines[i]

        # Skip page breaks
        if is_page_break_line(line):
            i += 1
            continue

        stripped = line.strip()

        # Empty line - might end table
        if not stripped:
            lookahead = i + 1
            while lookahead < len(lines) and not lines[lookahead].strip():
                lookahead += 1

            if lookahead < len(lines):
                next_line = lines[lookahead]
                # Check if table continues
                if '  ' in next_line and not re.match(r'^\d+\.?\d*\.?\d*\s+[A-Z]', next_line.strip()):
                    i = lookahead
                    continue

            if current_row:
                rows.append(current_row)
            break

        # Check for section header (end of table)
        if re.match(r'^\d+\.?\d*\.?\d*\s+[A-Z]', stripped) and '  ' not in line:
            if current_row:
                rows.append(current_row)
            break

        # Parse the line
        cells = split_line_with_positions(line)

        # Determine if this is a continuation or new row
        # A continuation line has fewer cells than expected columns
        # This indicates it's continuing values from the previous row
        leading_spaces = len(line) - len(line.lstrip()) if line else 0
        is_continuation = (
            current_row is not None and
            len(cells) < num_cols - 1  # Significantly fewer cells
        )

        # Also treat as continuation if it has few cells and starts indented
        if not is_continuation and current_row is not None:
            if leading_spaces > 3 and len(cells) <= num_cols // 2:
                is_continuation = True

        if is_continuation:
            # Merge based on position
            current_row = merge_data_continuation(current_row, cells, col_starts)
        else:
            # New data row
            if current_row:
                rows.append(current_row)

            # Build row from cells
            row_values = [''] * num_cols
            for cell in cells:
                best_col = find_best_matching_column(cell.start_pos, col_starts)
                if 0 <= best_col < num_cols:
                    if row_values[best_col]:
                        row_values[best_col] += ' ' + cell.text
                    else:
                        row_values[best_col] = cell.text

            current_row = row_values

        i += 1

    # Don't forget last row
    if current_row and current_row not in rows:
        rows.append(current_row)

    if not rows:
        return None, start_idx

    md_table = table_to_markdown(headers, rows)
    return md_table, i

def convert_section_header(line: str) -> Optional[str]:
    """Convert section number + title to markdown header."""
    stripped = line.strip()

    if '...' in stripped:
        return None

    match = re.match(r'^(\d+)\s+([A-Z][A-Za-z].*)$', stripped)
    if match:
        return f'## {match.group(1)} {match.group(2)}'

    match = re.match(r'^(\d+\.\d+)\s+([A-Z][A-Za-z].*)$', stripped)
    if match:
        return f'### {match.group(1)} {match.group(2)}'

    match = re.match(r'^(\d+\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', stripped)
    if match:
        return f'#### {match.group(1)} {match.group(2)}'

    match = re.match(r'^(\d+\.\d+\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', stripped)
    if match:
        return f'##### {match.group(1)} {match.group(2)}'

    match = re.match(r'^(Appendix\s+[A-Z])\s*[–-]\s*(.+)$', stripped)
    if match:
        return f'## {match.group(1)} – {match.group(2)}'

    match = re.match(r'^([A-Z]\.\d+)\s+([A-Z][A-Za-z].*)$', stripped)
    if match:
        return f'### {match.group(1)} {match.group(2)}'

    match = re.match(r'^([A-Z]\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', stripped)
    if match:
        return f'#### {match.group(1)} {match.group(2)}'

    match = re.match(r'^([A-Z]\.\d+\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', stripped)
    if match:
        return f'##### {match.group(1)} {match.group(2)}'

    return None

def process_file(input_path: str, output_path: str):
    """Main processing function."""
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.rstrip('\n\r') for line in lines]

    output = []
    i = 0
    toc_done = False

    # Document header
    output.append('# Media Transfer Protocol')
    output.append('')
    output.append('**Revision 1.1**')
    output.append('')
    output.append('*April 6th, 2011*')
    output.append('')
    output.append('---')
    output.append('')
    output.append('**Copyright © 2011, USB Implementers Forum, Inc. All rights reserved.**')
    output.append('')

    # Skip to TOC
    while i < len(lines) and i < 60:
        if 'Table of Contents' in lines[i]:
            break
        if 'Please send comments' in lines[i]:
            output.append(f'*{lines[i].strip()}*')
            output.append('')
        i += 1

    # Process TOC
    if i < len(lines) and 'Table of Contents' in lines[i]:
        i += 1
        toc_lines, i = extract_toc(lines, i)
        output.append(format_toc(toc_lines))
        output.append('')
        toc_done = True

    # Process rest of document
    while i < len(lines):
        line = lines[i]

        if is_page_break_line(line):
            i += 1
            continue

        if toc_done and is_toc_line(line):
            i += 1
            continue

        stripped = line.strip()

        if not stripped:
            if output and output[-1] != '':
                output.append('')
            i += 1
            continue

        # Section header
        header = convert_section_header(line)
        if header:
            output.append('')
            output.append(header)
            output.append('')
            i += 1
            continue

        # Check for table
        if is_likely_table_header(line):
            md_table, new_i = extract_table(lines, i)
            if md_table:
                output.append('')
                output.append(md_table)
                output.append('')
                i = new_i
                continue

        # Regular text
        output.append(stripped)
        i += 1

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        prev_blank = False
        for line in output:
            if line == '':
                if not prev_blank:
                    f.write('\n')
                prev_blank = True
            else:
                f.write(line + '\n')
                prev_blank = False

if __name__ == '__main__':
    import sys
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.dirname(script_dir)

    default_input = os.path.join(artifacts_dir, 'source', 'extracted.txt')
    default_output = os.path.join(artifacts_dir, 'converted', 'MTPforUSB-IFv1.1.md')

    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_file = sys.argv[2] if len(sys.argv) > 2 else default_output
    process_file(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")
