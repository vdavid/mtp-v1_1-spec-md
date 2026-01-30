## Appendix A Object Formats

### A.1 Object Format Summary Table

| Name                                     | Datacode Description                                                                                                                                                                     |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Undefined                                | 0x3000 Undefined object                                                                                                                                                                  |
| Association                              | 0x3001 Association (for example, a folder)                                                                                                                                               |
| Script                                   | 0x3002 Device model-specific script                                                                                                                                                      |
| Executable                               | 0x3003 Device model-specific binary executable                                                                                                                                           |
| Text                                     | 0x3004 Text file                                                                                                                                                                         |
| HTML                                     | 0x3005 Hypertext Markup Language file (text)                                                                                                                                             |
| DPOF                                     | 0x3006 Digital Print Order Format file (text)                                                                                                                                            |
| AIFF                                     | 0x3007 Audio clip                                                                                                                                                                        |
| WAV                                      | 0x3008 Audio clip                                                                                                                                                                        |
| MP3                                      | 0x3009 MPEG-1 Layer III audio (ISO/IEC 13818-3)                                                                                                                                          |
| AVI                                      | 0x300A Video clip                                                                                                                                                                        |
| MPEG                                     | 0x300B Video clip                                                                                                                                                                        |
| ASF                                      | 0x300C Microsoft Advanced Streaming Format (video)                                                                                                                                       |
| Undefined Image                          | 0x3800 Undefined image object                                                                                                                                                            |
| EXIF/JPEG                                | 0x3801 Exchangeable File Format, JEIDA standard                                                                                                                                          |
| TIFF/EP                                  | 0x3802 Tag Image File Format for Electronic Photography                                                                                                                                  |
| FlashPix                                 | 0x3803 Structured Storage Image Format                                                                                                                                                   |
| BMP                                      | 0x3804 Microsoft Windows Bitmap file                                                                                                                                                     |
| CIFF                                     | 0x3805 Canon Camera Image File Format                                                                                                                                                    |
| Undefined                                | 0x3806 Reserved                                                                                                                                                                          |
| GIF                                      | 0x3807 Graphics Interchange Format                                                                                                                                                       |
| JFIF                                     | 0x3808 JPEG File Interchange Format                                                                                                                                                      |
| CD                                       | 0x3809 PhotoCD Image Pac                                                                                                                                                                 |
| PICT                                     | 0x380A Quickdraw Image Format                                                                                                                                                            |
| PNG                                      | 0x380B Portable Network Graphics                                                                                                                                                         |
| Undefined                                | 0x380C Reserved                                                                                                                                                                          |
| TIFF                                     | 0x380D Tag Image File Format                                                                                                                                                             |
| TIFF/IT                                  | 0x380E Tag Image File Format for Information Technology (graphic arts)                                                                                                                   |
| JP2                                      | 0x380F JPEG2000 Baseline File Format                                                                                                                                                     |
| JPX                                      | 0x3810 JPEG2000 Extended File Format                                                                                                                                                     |
| Undefined Firmware                       | 0xB802                                                                                                                                                                                   |
| Windows Image Format                     | 0xB881                                                                                                                                                                                   |
| WBMP                                     | 0xB803 Wireless Application Protocol Bitmap Format (.wbmp). image/vnd.wap.wbmp http://www.wapforum.org/what/technical/SPEC-WAESpec-19990524.pdf                                          |
| JPEG XR                                  | 0xB804 JPEG XR, also known as HD Photo (.hdp, jxr, .wpd). image/vnd.ms-photo. ISO/IEC 29199-2:2009 http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=51609 |
| Undefined Audio                          | 0xB900 Undefined audio object                                                                                                                                                            |
| WMA                                      | 0xB901 Windows Media Audio                                                                                                                                                               |
| OGG                                      | 0xB902                                                                                                                                                                                   |
| AAC                                      | 0xB903 Advanced Audio Coding (.aac). audio/aac. MPEG-4 AAC.                                                                                                                              |
| Audible                                  | 0xB904                                                                                                                                                                                   |
| FLAC                                     | 0xB906 Free Lossless Audio Codec                                                                                                                                                         |
| QCELP                                    | 0xB907 Qualcomm Code Excited Linear Prediction (.qcp). audio/qcelp                                                                                                                       |
| AMR                                      | 0xB908 Adaptive Multi-Rate audio codec (.amr). audio/amr                                                                                                                                 |
| Undefined Video                          | 0xB980 Undefined video object                                                                                                                                                            |
| WMV                                      | 0xB981 Windows Media Video                                                                                                                                                               |
| MP4 Container                            | 0xB982 ISO 14496-1                                                                                                                                                                       |
| MP2                                      | 0xB983 MPEG-1 Layer II audio (ISO/IEC 13818-3)                                                                                                                                           |
| 3GP Container                            | 0xB984 3GPP file format. Details: http://www.3gpp.org/ftp/Specs/html-info/26244.htm (page title - "Transparent end-to-end packet switched streaming service, 3GPP file format").         |
| 3G2                                      | 0xB985 3GPP2 format (.3g2). video/3gpp2, audio/3gpp2 http://www.3gpp2.org/Public_html/specs/C.S0050-B_v1.0_070521.pdf                                                                    |
| AVCHD                                    | 0xB986 MPEG-4 AVC video and Dolby Digital audio within an MPEG-2 Transport Stream as constrained by the AVCHD format specification http://www.avchd-info.org/                            |
| ATSC-TS                                  | 0xB987 MPEG-2 video and AC-3 audio within an ATSC-compliant MPEG-2 Transport Stream                                                                                                      |
| DVB-TS                                   | 0xB988 MPEG-2 video and MPEG-1 Layer II or AC-3 audio within a DVB-compliant MPEG-2 Transport Stream                                                                                     |
| Undefined Collection                     | 0xBA00                                                                                                                                                                                   |
| Abstract Multimedia Album                | 0xBA01                                                                                                                                                                                   |
| Abstract Image Album                     | 0xBA02                                                                                                                                                                                   |
| Abstract Audio Album                     | 0xBA03                                                                                                                                                                                   |
| Abstract Video Album                     | 0xBA04                                                                                                                                                                                   |
| Abstract Audio & Video Playlist          | 0xBA05                                                                                                                                                                                   |
| Abstract Contact Group                   | 0xBA06                                                                                                                                                                                   |
| Abstract Message Folder                  | 0xBA07                                                                                                                                                                                   |
| Abstract Chaptered Production            | 0xBA08                                                                                                                                                                                   |
| Abstract Audio Playlist                  | 0xBA09                                                                                                                                                                                   |
| Abstract Video Playlist                  | 0xBA0A                                                                                                                                                                                   |
| Abstract Mediacast                       | 0xBA0B For use with mediacasts; references multimedia enclosures of RSS feeds or episodic content                                                                                        |
| WPL Playlist                             | 0xBA10                                                                                                                                                                                   |
| M3U Playlist                             | 0xBA11                                                                                                                                                                                   |
| MPL Playlist                             | 0xBA12                                                                                                                                                                                   |
| ASX Playlist                             | 0xBA13                                                                                                                                                                                   |
| PLS Playlist                             | 0xBA14                                                                                                                                                                                   |
| Undefined Document                       | 0xBA80                                                                                                                                                                                   |
| Abstract Document                        | 0xBA81                                                                                                                                                                                   |
| XML Document                             | 0xBA82                                                                                                                                                                                   |
| Microsoft Word Document                  | 0xBA83                                                                                                                                                                                   |
| MHT Compiled HTML Document               | 0xBA84                                                                                                                                                                                   |
| Microsoft Excel Spreadsheet (.xls)       | 0xBA85                                                                                                                                                                                   |
| Microsoft Powerpoint Presentation (.ppt) | 0xBA86                                                                                                                                                                                   |
| Undefined Message                        | 0xBB00                                                                                                                                                                                   |
| Abstract Message                         | 0xBB01                                                                                                                                                                                   |
| Undefined Bookmark                       | 0xBB10                                                                                                                                                                                   |
| Abstract Bookmark                        | 0xBB11                                                                                                                                                                                   |
| Undefined Appointment                    | 0xBB20                                                                                                                                                                                   |
| Abstract Appointment                     | 0xBB21                                                                                                                                                                                   |
| vCalendar 1.0                            | 0xBB22                                                                                                                                                                                   |
| Undefined Task                           | 0xBB40                                                                                                                                                                                   |
| Abstract Task                            | 0xBB41                                                                                                                                                                                   |
| iCalendar                                | 0xBB42                                                                                                                                                                                   |
| Undefined Note                           | 0xBB60                                                                                                                                                                                   |
| Abstract Note                            | 0xBB61                                                                                                                                                                                   |
| Undefined Contact                        | 0xBB80                                                                                                                                                                                   |
| Abstract Contact                         | 0xBB81                                                                                                                                                                                   |
| vCard 2                                  | 0xBB82                                                                                                                                                                                   |
| vCard 3                                  | 0xBB83                                                                                                                                                                                   |

Notes:
M4A – unambiguous definition for MP4 files containing MPEG-4 Audio (as used by
iTunes, cellphone music services etc.)

M4V – unambiguous definition for MP4 files containing MPEG-4 AVC video together
with MPEG-4 audio (as used by iTunes, cellphone music services etc.)

M4V_EAC3 – definition for MP4 files containing MPEG-4 AVC video together with
Enhanced AC-3 audio, an emerging format for online content distribution (supported by
DECE, DVB, emerging CE, PC and mobile media players)

AVCHD – definition to support the AVCHD format found on an increasing number of
consumer camcorders and digital cameras

ATSC-TS – definition to support MPEG-2 Transport streams from ATSC OTA services
as used in the US, Korea and other territories, and supported by many CE and PC media
players

DVB-TS - definition to support MPEG-2 Transport streams from DVB services as used
in Europe, Australia and other territories, and supported by many CE and PC media
players

DVB-TS-AVC - definition to support MPEG-2 Transport streams containing MPEG-4
AVC video and Enhanced AC-3 audio from DVB services as used in emerging HD
services in Europe (e.g. mandatory HD broadcast format in France, UK, Spain,. Italy)

