# MTP v1.1 specification (Markdown)

![MTP v1.1](https://img.shields.io/badge/MTP-v1.1-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

The USB Media Transfer Protocol (MTP) v1.1 specification, converted to Markdown for easy reading and AI/LLM consumption.

## Why this exists

The official MTP specification is only available as
a [282-page PDF](https://www.usb.org/document-library/media-transfer-protocol-v11-spec-and-mtp-v11-adopters-agreement)
from USB.org. PDFs are rather hard for LLMs to process. This repository is a clean Markdown conversion, enabling:

- MTP implementation development for AI agents
- Easy searching and navigation
- Copy-pasting tables and code references
- Easier integration with documentation tools

## Getting started

New to MTP? Here's a recommended reading order:

1. **[02-introduction.md](02-introduction.md)**: Start here. Covers the device model, object model, and core concepts.
2. **[05-communication-model.md](05-communication-model.md)**: How initiators and responders communicate (transactions,
   sessions, operations).
3. **[04-normative-reference.md](04-normative-reference.md)**: Data types and codes you'll need to understand the rest.
4. **[10-appendix-d-operations.md](10-appendix-d-operations.md)**: The core operations (GetDeviceInfo, OpenSession,
   GetObject, SendObject, etc.).
5. **[12-appendix-f-responses.md](12-appendix-f-responses.md)**: Response codes your implementation needs to handle.

Then reference the remaining appendices (object formats, properties, events) as-needed during implementation.

## Quick reference

These might come handy.

### Common operations

| Operation        | Code     | Description                                       |
|------------------|----------|---------------------------------------------------|
| GetDeviceInfo    | `0x1001` | Get device capabilities and info (call first)     |
| OpenSession      | `0x1002` | Start a session (required before most operations) |
| CloseSession     | `0x1003` | End the current session                           |
| GetStorageIDs    | `0x1004` | List available storage areas                      |
| GetObjectHandles | `0x1007` | List objects in storage                           |
| GetObjectInfo    | `0x1008` | Get metadata for an object                        |
| GetObject        | `0x1009` | Download an object's data                         |
| SendObjectInfo   | `0x100C` | Prepare to upload (send metadata first)           |
| SendObject       | `0x100D` | Upload an object's data                           |
| DeleteObject     | `0x100B` | Delete an object                                  |

### Common responses

| Response             | Code     | Meaning                        |
|----------------------|----------|--------------------------------|
| OK                   | `0x2001` | Success                        |
| General_Error        | `0x2002` | Unknown failure                |
| Session_Not_Open     | `0x2003` | Need to call OpenSession first |
| Invalid_ObjectHandle | `0x2009` | Object doesn't exist           |
| Store_Full           | `0x200C` | No space left                  |
| Access_Denied        | `0x200F` | Permission denied              |
| Device_Busy          | `0x2019` | Try again later                |

See [Appendix D](10-appendix-d-operations.md) and [Appendix F](12-appendix-f-responses.md) for complete lists.

## Index

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

## Implementations

These projects were built using this Markdown specification, proving it's complete and usable:

| Project                                    | Language | Description                                          |
|--------------------------------------------|----------|------------------------------------------------------|
| [mtp-rs](https://github.com/vdavid/mtp-rs) | Rust     | MTP implementation built with Claude using this spec |

Built something with this spec? [Open a PR](../../pulls) to add it!

## Related specifications

MTP builds on other standards. These may be helpful for deeper understanding:

| Spec                                                                               | Description                                                    |
|------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [PTP (ISO 15740)](https://www.iso.org/standard/45346.html)                         | Picture Transfer Protocol — MTP extends this                   |
| [USB Device Class Definition](https://www.usb.org/documents?search=still+image)    | USB Still Image Capture Device Class (MTP uses this transport) |
| [USB 2.0 Specification](https://www.usb.org/document-library/usb-20-specification) | USB fundamentals                                               |

## Official source

The original specification is available from the USB Implementers Forum:

- [MTP v1.1 spec and adopters agreement](https://www.usb.org/document-library/media-transfer-protocol-v11-spec-and-mtp-v11-adopters-agreement)

## Conversion process

I created this Markdown using Python scripts that extract text from the PDF while preserving table structure.
The conversion tools are available in the [`/conversion-tools`](conversion-tools/) directory, if you want to tweak/reuse
it. Although, note that manual review (95% AI, 5% human) was used after the script conversion. See the
[conversion README](conversion-tools/README.md) for technical details.

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
