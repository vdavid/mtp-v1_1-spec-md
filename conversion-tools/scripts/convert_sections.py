#!/usr/bin/env python3
"""
Convert MTP specification by extracting sections from raw text and converting each individually.
This avoids the table corruption that happens when tables span across section boundaries.
"""

import re
import os
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
    if stripped == 'th':
        return True
    for copyright_line in COPYRIGHT_LINES:
        if copyright_line in stripped:
            return True
    return False

@dataclass
class CellInfo:
    text: str
    start_pos: int
    end_pos: int

def split_line_with_positions(line: str) -> List[CellInfo]:
    """Split line by 2+ spaces, recording positions."""
    cells = []
    i = 0
    while i < len(line) and line[i] == ' ':
        i += 1
    while i < len(line):
        start = i
        while i < len(line):
            if line[i] == ' ':
                space_start = i
                while i < len(line) and line[i] == ' ':
                    i += 1
                if i - space_start >= 2:
                    cells.append(CellInfo(line[start:space_start].strip(), start, space_start))
                    break
            else:
                i += 1
        if i >= len(line) and start < len(line):
            text = line[start:].strip()
            if text:
                cells.append(CellInfo(text, start, len(line)))
    return cells

def find_best_column(pos: int, col_starts: List[int]) -> int:
    """Find which column a position best matches."""
    if not col_starts:
        return -1
    best_col = 0
    for i in range(len(col_starts)):
        if col_starts[i] <= pos:
            best_col = i
        else:
            if i > 0:
                dist_to_prev = pos - col_starts[i - 1]
                dist_to_curr = col_starts[i] - pos
                if dist_to_curr < dist_to_prev:
                    best_col = i
            break
    return best_col

def is_likely_table_header(line: str) -> bool:
    """Check if line looks like a table header."""
    if '  ' not in line:
        return False
    stripped = line.strip().lower()
    header_words = ['field', 'size', 'datatype', 'description', 'value', 'code',
                    'name', 'type', 'format', 'bytes', 'bit', 'bits', 'order',
                    'datacode', 'operation', 'response', 'event', 'property']
    return sum(1 for word in header_words if word in stripped) >= 2

def is_header_continuation(line: str) -> bool:
    """Check if line looks like a header continuation."""
    stripped = line.strip().lower()
    if re.match(r'^[\d\-]+$', stripped):
        return True
    if stripped in ['order', '(bytes)', '(bits)']:
        return True
    parts = stripped.split()
    return all(re.match(r'^[\d\-]+$', p) or p in ['order', '(bytes)', '(bits)'] for p in parts)

def table_to_markdown(headers: List[str], rows: List[List[str]]) -> str:
    """Convert headers and rows to markdown table."""
    if not headers:
        return ''
    num_cols = len(headers)
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row[:num_cols]):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(cell))
    col_widths = [max(w, 3) for w in col_widths]
    lines = []
    header_cells = [headers[i].ljust(col_widths[i]) for i in range(num_cols)]
    lines.append('| ' + ' | '.join(header_cells) + ' |')
    lines.append('| ' + ' | '.join('-' * w for w in col_widths) + ' |')
    for row in rows:
        cells = [(row[i] if i < len(row) else '').ljust(col_widths[i]) for i in range(num_cols)]
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)

def extract_table(lines: List[str], start_idx: int, section_end: int) -> Tuple[Optional[str], int]:
    """Extract a table, respecting section boundary."""
    header_line = lines[start_idx]
    header_cells = split_line_with_positions(header_line)
    if len(header_cells) < 2:
        return None, start_idx

    i = start_idx + 1

    # Check for header continuation
    if i < section_end and i < len(lines) and is_header_continuation(lines[i]):
        cont_cells = split_line_with_positions(lines[i])
        col_starts = [c.start_pos for c in header_cells]
        headers = [c.text for c in header_cells]
        for cont in cont_cells:
            best_col = find_best_column(cont.start_pos, col_starts)
            if best_col >= 0 and best_col < len(headers):
                headers[best_col] = headers[best_col] + ' ' + cont.text
        i += 1
    else:
        headers = [c.text for c in header_cells]

    col_starts = [c.start_pos for c in header_cells]
    num_cols = len(headers)
    rows = []
    current_row = None

    while i < len(lines) and i < section_end:
        line = lines[i]
        if is_page_break_line(line):
            i += 1
            continue
        stripped = line.strip()
        if not stripped:
            lookahead = i + 1
            while lookahead < len(lines) and lookahead < section_end and not lines[lookahead].strip():
                lookahead += 1
            if lookahead < len(lines) and lookahead < section_end:
                next_line = lines[lookahead]
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
        if re.match(r'^[A-Z]\.\d+\.?\d*\.?\d*\s+[A-Z]', stripped) and '  ' not in line:
            if current_row:
                rows.append(current_row)
            break

        cells = split_line_with_positions(line)
        leading_spaces = len(line) - len(line.lstrip()) if line else 0
        is_continuation = current_row is not None and len(cells) < num_cols - 1
        if not is_continuation and current_row is not None:
            if leading_spaces > 3 and len(cells) <= num_cols // 2:
                is_continuation = True

        if is_continuation and current_row:
            for cont in cells:
                best_col = find_best_column(cont.start_pos, col_starts)
                if best_col >= 0 and best_col < len(current_row):
                    if current_row[best_col]:
                        current_row[best_col] += ' ' + cont.text
                    else:
                        current_row[best_col] = cont.text
        else:
            if current_row:
                rows.append(current_row)
            row_values = [''] * num_cols
            for cell in cells:
                best_col = find_best_column(cell.start_pos, col_starts)
                if 0 <= best_col < num_cols:
                    if row_values[best_col]:
                        row_values[best_col] += ' ' + cell.text
                    else:
                        row_values[best_col] = cell.text
            current_row = row_values
        i += 1

    if current_row and current_row not in rows:
        rows.append(current_row)
    if not rows:
        return None, start_idx
    return table_to_markdown(headers, rows), i

def convert_section_header(line: str) -> Optional[str]:
    """Convert section number + title to markdown header."""
    stripped = line.strip()
    if '...' in stripped:
        return None

    patterns = [
        (r'^(\d+)\s+([A-Z][A-Za-z].*)$', '## '),
        (r'^(\d+\.\d+)\s+([A-Z][A-Za-z].*)$', '### '),
        (r'^(\d+\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', '#### '),
        (r'^(\d+\.\d+\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', '##### '),
        (r'^(Appendix\s+[A-Z])\s*[–-]\s*(.+)$', '## '),
        (r'^([A-Z]\.\d+)\s+([A-Z][A-Za-z].*)$', '### '),
        (r'^([A-Z]\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', '#### '),
        (r'^([A-Z]\.\d+\.\d+\.\d+)\s+([A-Z][A-Za-z].*)$', '##### '),
    ]
    for pattern, prefix in patterns:
        match = re.match(pattern, stripped)
        if match:
            return f'{prefix}{match.group(1)} {match.group(2)}'
    return None

def convert_section(lines: List[str], start_idx: int, end_idx: int) -> str:
    """Convert a section of raw text lines to markdown."""
    output = []
    i = start_idx

    while i < end_idx:
        line = lines[i]
        if is_page_break_line(line):
            i += 1
            continue

        stripped = line.strip()
        if not stripped:
            if output and output[-1] != '':
                output.append('')
            i += 1
            continue

        header = convert_section_header(line)
        if header:
            output.append('')
            output.append(header)
            output.append('')
            i += 1
            continue

        if is_likely_table_header(line):
            md_table, new_i = extract_table(lines, i, end_idx)
            if md_table:
                output.append('')
                output.append(md_table)
                output.append('')
                i = new_i
                continue

        output.append(stripped)
        i += 1

    # Clean up multiple blank lines
    result = []
    prev_blank = False
    for line in output:
        if line == '':
            if not prev_blank:
                result.append(line)
            prev_blank = True
        else:
            result.append(line)
            prev_blank = False

    return '\n'.join(result)

def find_section_boundaries(lines: List[str]) -> List[Tuple[int, str, str]]:
    """Find where each main section starts in the raw text."""
    # Section patterns: (regex, filename, title)
    sections = [
        (r'^1\s+Introduction$', '02-introduction', '1 Introduction'),
        (r'^2\s+Transport Requirements$', '03-transport-requirements', '2 Transport Requirements'),
        (r'^3\s+Normative Reference$', '04-normative-reference', '3 Normative Reference'),
        (r'^4\s+Communication Model$', '05-communication-model', '4 Communication Model'),
        (r'^5\s+Device Model$', '06-device-model', '5 Device Model'),
        (r'^Appendix A\s*[–-]', '07-appendix-a-object-formats', 'Appendix A – Object Formats'),
        (r'^Appendix B\s*[–-]', '08-appendix-b-object-properties', 'Appendix B – Object Properties'),
        (r'^Appendix C\s*[–-]', '09-appendix-c-device-properties', 'Appendix C – Device Properties'),
        (r'^Appendix D\s*[–-]', '10-appendix-d-operations', 'Appendix D – Operations'),
        (r'^Appendix E\s*[–-]', '11-appendix-e-enhanced-operations', 'Appendix E – Enhanced Operations'),
        (r'^Appendix F\s*[–-]', '12-appendix-f-responses', 'Appendix F – Responses'),
        (r'^Appendix G\s*[–-]', '13-appendix-g-events', 'Appendix G – Events'),
        (r'^Appendix H\s*[–-]', '14-appendix-h-usb-optimizations', 'Appendix H – USB Optimizations'),
    ]

    boundaries = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        for pattern, filename, title in sections:
            if re.match(pattern, stripped):
                boundaries.append((i, filename, title))
                break

    # Sort by line number
    boundaries.sort(key=lambda x: x[0])
    return boundaries

def process_raw_file(input_path: str, output_dir: str):
    """Process raw extracted text file and create section files."""
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = [line.rstrip('\n\r') for line in lines]

    os.makedirs(output_dir, exist_ok=True)

    # Create front matter
    front_matter = """# Media Transfer Protocol

**Revision 1.1**

*April 6th, 2011*

---

**Copyright © 2011, USB Implementers Forum, Inc. All rights reserved.**

*Please send comments via electronic mail to mtp-chair@usb.org*
"""
    with open(os.path.join(output_dir, '00-front-matter.md'), 'w') as f:
        f.write(front_matter)
    print("Created: 00-front-matter.md")

    # Find TOC
    toc_start = None
    toc_end = None
    for i, line in enumerate(lines):
        if 'Table of Contents' in line:
            toc_start = i
        if toc_start and re.match(r'^1\s+Introduction', line.strip()):
            toc_end = i
            break

    # Create TOC file
    if toc_start and toc_end:
        toc_content = convert_toc(lines[toc_start:toc_end])
        with open(os.path.join(output_dir, '01-toc.md'), 'w') as f:
            f.write(toc_content)
        print(f"Created: 01-toc.md ({toc_end - toc_start} lines)")

    # Find and process each section
    boundaries = find_section_boundaries(lines)
    print(f"\nFound {len(boundaries)} sections")

    for idx, (start_line, filename, title) in enumerate(boundaries):
        # Determine end line
        if idx + 1 < len(boundaries):
            end_line = boundaries[idx + 1][0]
        else:
            end_line = len(lines)

        print(f"Processing: {filename} (lines {start_line}-{end_line}, {end_line - start_line} lines)")

        # Convert section
        md_content = convert_section(lines, start_line, end_line)

        # Write file
        output_path = os.path.join(output_dir, f'{filename}.md')
        with open(output_path, 'w') as f:
            f.write(md_content)
            f.write('\n')

    # Create index
    create_index(output_dir)

def convert_toc(lines: List[str]) -> str:
    """Convert TOC lines to markdown."""
    result = ["## Table of Contents\n"]

    for line in lines:
        clean = line.rstrip()
        if is_page_break_line(line):
            continue
        if not clean.strip():
            continue
        if 'Table of Contents' in clean:
            continue

        match = re.match(r'^(\s*)(.+?)\.{2,}\s*(\d+)\s*$', clean)
        if match:
            indent = match.group(1)
            text = match.group(2).strip()
            page = match.group(3)
            indent_level = len(indent) // 2
            slug = re.sub(r'[^\w\s-]', '', text.lower())
            slug = re.sub(r'[\s_]+', '-', slug).strip('-')
            result.append('  ' * indent_level + f'- [{text}](#{slug}) (p.{page})')

    return '\n'.join(result)

def create_index(output_dir: str):
    """Create index file listing all sections."""
    files = sorted([f for f in os.listdir(output_dir) if f.endswith('.md') and f != 'index.md'])

    with open(os.path.join(output_dir, 'index.md'), 'w') as f:
        f.write('# MTP Specification Bundle\n\n')
        f.write('This directory contains the MTP specification split into individual files.\n\n')
        f.write('## Files\n\n')
        for filename in files:
            f.write(f'- [{filename}]({filename})\n')

    print(f"\nCreated: index.md")

if __name__ == '__main__':
    import sys
    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.dirname(script_dir)

    default_input = os.path.join(artifacts_dir, 'source', 'extracted.txt')
    default_output = os.path.join(artifacts_dir, 'bundle-gen')

    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_dir = sys.argv[2] if len(sys.argv) > 2 else default_output
    process_raw_file(input_file, output_dir)
