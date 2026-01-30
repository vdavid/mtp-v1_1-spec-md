## 1 Introduction

Media Transfer Protocol, or MTP, is a protocol designed for content exchange with and
command and control of transient storage devices. It was been developed as an extension
to PTP, or Picture Transfer Protocol, and is targeted primarily at Digital Still Cameras,
Portable Media Players and Cellular phones.

### 1.1 Purpose

The primary purpose of this protocol is to facilitate communication between media
devices that have transient connectivity and significant storage capacity. This includes the
exchange of binary objects and the enumeration of the contents of that connected device.

The secondary purpose of this protocol is to enable command and control of the
connected device. This includes the remote invocation of device functionality, monitoring
of device-initiated events, and the reading and setting of device properties.

### 1.2 MTP Device Model

MTP devices may be loosely defined as devices with storage that consume or produce
media objects in a binary format, which have intermittent connections with other media
devices, and which fulfill their primary purpose while not connected to another device.

Devices generally act primarily as either media consumers or media producers, although
this line is becoming increasingly blurred. Some examples of common portable media
devices are: digital cameras (both still and video), portable audio players, and cellular
phones.

### 1.3 MTP Object Model

The term "media" in "Media Transfer Protocol" is used to identify any binary data, and is
not restricted to audio/video formats to which it is commonly applied. Some examples of
non-audio/video objects include contacts, programs, scheduled events and text files.

Media objects are required to be represented as atomic binary objects during transfer, but
are not required to be stored in the same format or structure on the device. Objects may
be created on-demand, as long as they are accurately represented during content
enumeration.

MTP objects consist of not only the binary content of the file, but also the descriptive
metadata and references. MTP is designed such that objects can be recognized through
the mechanisms provided in the protocol without requiring an understanding of the binary
format of the file itself.

The combination of the binary file, its descriptive metadata and any intra-object
references together is referred to in MTP as an object.

### 1.4 Scope

This specification is intended to define the USB implementation of MTP in a way that is
agnostic to both device type and OS. Certain operating systems or device classes may
require a particular subset of MTP to enable their minimal scenarios; it is strongly
suggested that implementers investigate the intended usage scenarios to determine if any
such requirements exist.

### 1.5 PTP Compatibility

This protocol is implemented as an extension of the existing Picture Transfer Protocol, as
defined by the ISO 15740 specification
(http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=37445&
ICS1=37&ICS2=40&ICS3=99). MTP is intended to co-exist with and not overlap PTP
functionality, and it is hoped that devices will be developed to comply fully with the PTP
specification where possible to leverage the existing base of PTP-enabled devices and
applications.

MTP has been implemented using the defined vendor extensibility mechanism of PTP
using the MTP Vendor Extension ID. By implementing MTP in this way, compatibility
of devices with PTP is preserved. However, in rare cases, optional modifications to the
core protocol have been included to enhance the functionality of connected devices.
These are clearly identified in this specification, and it is the responsibility of
implementers of this protocol to determine whether PTP-compatibility is desirable, and if
so, to implement this protocol in such a manner as to be compatible with PTP.

The name "Media Transfer Protocol" is used to refer to the combination of the core PTP
specification and the extension set provided by the USB-IF in this specification.

