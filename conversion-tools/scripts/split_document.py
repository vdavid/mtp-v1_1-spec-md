#!/usr/bin/env python3
"""
Split MTP specification markdown into individual section files.
"""

import re
import os

def slugify(text: str) -> str:
    """Create a URL-safe slug from text."""
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[\s_]+', '-', slug)
    return slug.strip('-')

def split_document(input_path: str, output_dir: str):
    """Split the document into separate files by main section."""

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    # Define section patterns and their output filenames
    # Format: (pattern, filename_prefix, title)
    sections = [
        (r'^# Media Transfer Protocol', '00-front-matter', 'Front Matter'),
        (r'^## Table of Contents', '01-toc', 'Table of Contents'),
        (r'^## 1 Introduction', '02-introduction', 'Introduction'),
        (r'^## 2 Transport Requirements', '03-transport-requirements', 'Transport Requirements'),
        (r'^## 3 Normative Reference', '04-normative-reference', 'Normative Reference'),
        (r'^## 4 Communication Model', '05-communication-model', 'Communication Model'),
        (r'^## 5 Device Model', '06-device-model', 'Device Model'),
        (r'^## Appendix A', '07-appendix-a-object-formats', 'Appendix A – Object Formats'),
        (r'^## Appendix B', '08-appendix-b-object-properties', 'Appendix B – Object Properties'),
        (r'^## Appendix C', '09-appendix-c-device-properties', 'Appendix C – Device Properties'),
        (r'^## Appendix D', '10-appendix-d-operations', 'Appendix D – Operations'),
        (r'^## Appendix E', '11-appendix-e-enhanced-operations', 'Appendix E – Enhanced Operations'),
        (r'^## Appendix F', '12-appendix-f-responses', 'Appendix F – Responses'),
        (r'^## Appendix G', '13-appendix-g-events', 'Appendix G – Events'),
        (r'^## Appendix H', '14-appendix-h-usb-optimizations', 'Appendix H – USB Optimizations'),
    ]

    # Find where each section starts
    section_starts = []
    for i, line in enumerate(lines):
        for pattern, filename, title in sections:
            if re.match(pattern, line):
                section_starts.append((i, filename, title, pattern))
                break

    # Sort by line number
    section_starts.sort(key=lambda x: x[0])

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Extract and write each section
    files_created = []
    for idx, (start_line, filename, title, pattern) in enumerate(section_starts):
        # Determine end line
        if idx + 1 < len(section_starts):
            end_line = section_starts[idx + 1][0]
        else:
            end_line = len(lines)

        # Extract section content
        section_lines = lines[start_line:end_line]

        # Remove trailing blank lines
        while section_lines and not section_lines[-1].strip():
            section_lines.pop()

        # Write to file
        output_path = os.path.join(output_dir, f'{filename}.md')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(section_lines))
            f.write('\n')

        files_created.append((output_path, title, len(section_lines)))
        print(f"Created: {filename}.md ({len(section_lines)} lines) - {title}")

    # Create an index file
    index_path = os.path.join(output_dir, 'index.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('# MTP Specification Bundle\n\n')
        f.write('This directory contains the MTP specification split into individual files.\n\n')
        f.write('## Files\n\n')
        for path, title, line_count in files_created:
            filename = os.path.basename(path)
            f.write(f'- [{filename}]({filename}) - {title} ({line_count} lines)\n')

    print(f"\nCreated index: index.md")
    print(f"\nTotal: {len(files_created)} section files created in {output_dir}")

    return files_created

if __name__ == '__main__':
    import sys

    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.dirname(script_dir)

    default_input = os.path.join(artifacts_dir, 'converted', 'MTPforUSB-IFv1.1.md')
    default_output = os.path.join(artifacts_dir, 'bundle-gen')

    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_dir = sys.argv[2] if len(sys.argv) > 2 else default_output

    split_document(input_file, output_dir)
