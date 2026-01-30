# MTP specification PDF to Markdown conversion

This directory contains the tools used to convert the MTP (Media Transfer Protocol) v1.1 specification from PDF to Markdown.

## Source document

- **File**: `source/MTPforUSB-IFv1.1.pdf`
- **Title**: USB Media Transfer Protocol Specification
- **Version**: Revision 1.1
- **Date**: April 6, 2011
- **Pages**: 282

## Directory structure

```
conversion-tools/
├── source/
│   ├── MTPforUSB-IFv1.1.pdf    # Original PDF specification
│   └── extracted.txt            # Raw text extracted from PDF
├── scripts/
│   ├── convert_v5.py           # Full-document converter
│   ├── split_document.py       # Splits markdown into section files
│   └── convert_sections.py     # Direct section extraction (recommended)
└── README.md
```

The final Markdown files are in the repository root (`../`).

## Conversion process

### Step 1: Extract text from PDF

Extract text preserving column positions using `pdftotext`:

```bash
pdftotext -layout source/MTPforUSB-IFv1.1.pdf source/extracted.txt
```

The `-layout` flag preserves horizontal positioning, which is needed for accurate table column detection.

### Step 2: Convert to Markdown

Two approaches are available:

#### Option A: Full document conversion (then split)

```bash
python3 scripts/convert_v5.py
python3 scripts/split_document.py
```

#### Option B: Direct section extraction (recommended)

```bash
python3 scripts/convert_sections.py
```

### Step 3: Manual cleanup

The generated files require manual review. Common issues:

1. **Merged table rows**: Multi-value rows may need splitting
2. **Split format names**: Multi-word names split across rows
3. **Datacode columns merged**: Hex values merged with type names
4. **Orphaned header continuations**: Stray partial rows

## Technical details

### Table detection

Tables are detected by looking for lines with:
- Multiple segments separated by 2+ spaces
- Header words like "Field", "Size", "Datatype", "Description"

### Position-based column matching

For multi-line cells, the converter tracks character positions and assigns continuation text to the nearest column based on horizontal position.

### Page break handling

Page headers/footers are detected and stripped:
- "Revision 1.1 April 6 th 2011 [page number]"
- Copyright lines

## Requirements

- Python 3.6+
- `pdftotext` (part of poppler-utils)

**macOS:**
```bash
brew install poppler
```

**Ubuntu/Debian:**
```bash
apt-get install poppler-utils
```

## Re-running the conversion

```bash
cd conversion-tools

# Extract text (only needed if PDF changes)
pdftotext -layout source/MTPforUSB-IFv1.1.pdf source/extracted.txt

# Generate section files
python3 scripts/convert_sections.py

# Copy to root for manual cleanup
cp *.md ../
```

Note: The files in `../` have been manually reviewed and corrected.
