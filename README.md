# MTP v1.1 specification (Markdown)

The USB Media Transfer Protocol (MTP) v1.1 specification, converted to Markdown for easy reading and AI/LLM consumption.

## Why this exists

The official MTP specification is only available as
a [282-page PDF](https://www.usb.org/document-library/media-transfer-protocol-v11-spec-and-mtp-v11-adopters-agreement)
from USB.org. PDFs are difficult for AI assistants and LLMs to process effectively. This repository provides a clean
Markdown conversion, enabling:

- AI-assisted MTP implementation development
- Easy searching and navigation
- Copy-paste of tables and code references
- Integration with documentation tools

## Specification contents

| File                                                                         | Content                                            |
|------------------------------------------------------------------------------|----------------------------------------------------|
| [00-front-matter.md](00-front-matter.md)                                     | Title and copyright                                |
| [01-toc.md](01-toc.md)                                                       | Table of contents                                  |
| [02-introduction.md](02-introduction.md)                                     | Section 1: Introduction                            |
| [03-transport-requirements.md](03-transport-requirements.md)                 | Section 2: Transport requirements                  |
| [04-normative-reference.md](04-normative-reference.md)                       | Section 3: Normative reference (data types, codes) |
| [05-communication-model.md](05-communication-model.md)                       | Section 4: Communication model                     |
| [06-device-model.md](06-device-model.md)                                     | Section 5: Device model                            |
| [07-appendix-a-object-formats.md](07-appendix-a-object-formats.md)           | Appendix A: Object formats                         |
| [08-appendix-b-object-properties.md](08-appendix-b-object-properties.md)     | Appendix B: Object properties                      |
| [09-appendix-c-device-properties.md](09-appendix-c-device-properties.md)     | Appendix C: Device properties                      |
| [10-appendix-d-operations.md](10-appendix-d-operations.md)                   | Appendix D: Operations                             |
| [11-appendix-e-enhanced-operations.md](11-appendix-e-enhanced-operations.md) | Appendix E: Enhanced operations                    |
| [12-appendix-f-responses.md](12-appendix-f-responses.md)                     | Appendix F: Response codes                         |
| [13-appendix-g-events.md](13-appendix-g-events.md)                           | Appendix G: Events                                 |
| [14-appendix-h-usb-optimizations.md](14-appendix-h-usb-optimizations.md)     | Appendix H: USB optimizations                      |

## Related projects

- [mtp-rs](https://github.com/vdavid/mtp-rs) - A Rust implementation of MTP, built using this specification

## Official source

The original specification is available from the USB Implementers Forum:

- [MTP v1.1 spec and adopters agreement](https://www.usb.org/document-library/media-transfer-protocol-v11-spec-and-mtp-v11-adopters-agreement)

## Conversion process

This Markdown version was created using Python scripts that extract text from the PDF while preserving table structure.
The conversion tools are available in the [`/conversion-tools`](conversion-tools/) directory. See
the [conversion README](conversion-tools/README.md) for technical details.

## Copyright notice

The MTP specification content is:

> **Copyright © 2011, USB Implementers Forum, Inc. All rights reserved.**

This repository contains an unofficial Markdown conversion for reference purposes. The conversion tooling is licensed
under MIT (see [LICENSE](LICENSE)). For official use, please refer to
the [original PDF](https://www.usb.org/document-library/media-transfer-protocol-v11-spec-and-mtp-v11-adopters-agreement)
and the USB-IF Adopters Agreement.

## Contributing

Found an error in the conversion? Please [open an issue](../../issues) with:

- The file and section containing the error
- What the text currently says
- What it should say (reference the original PDF page number if possible)
