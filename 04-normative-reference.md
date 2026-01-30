## 3 Normative Reference

Within the context of MTP, certain terms and conventions are used extensively to provide
a basic foundation of functionality in the protocol. These conventions are described here.

MTP does not require that the device employ these conventions or representations in the
internal working of a device, only that they are adhered to in the implementation of the
over-the-wire protocol.

### 3.1 Data Formatting

PTP defines a convention for encoding datatypes and datasets, and as a PTP extension set
the data structures used in MTP are identical to those used in PTP. It is repeated here for
convenience, but the PTP specification shall (as always) be considered the definitive
source.

#### 3.1.1 Multi-byte Data

The standard format for multi-byte data in this specification is big-endian. That is, the
bits within a byte will be read such that the most significant byte is read first. The actual
multi-byte data sent over the transport may not necessarily adhere to this same format,
and the actual multi-byte data used on the devices may also use a different multi-byte
format. The big-endian convention only applies within this document, except where
otherwise stated.

#### 3.1.2 Bit Field Format

When bit fields are defined in this format, the least significant bit is at the zero position.
When the bit field is represented in the specification, this is the right-most position. For
example, the most significant bit of a 32-bit integer (UINT32) will be at the 31st position,
while the least significant bit will be at the 0-th position.

### 3.2 Simple Types

All non-opaque data in MTP consists of either an atomic value of a simple type, or an
array of atomic values of a simple type. The set of simple atomic types used in MTP is
described here as a common foundation for data representation.

Specifically, any time data is passed as a parameter to an operation, response or event, it
must take one of the following forms.

#### 3.2.1 Simple Type Summary

| Data Type code   | Type      | Description                        |
|------------------|-----------|------------------------------------|
| 0x0000           | UNDEF     | Undefined                          |
| 0x0001           | INT8      | Signed 8-bit integer               |
| 0x0002           | UINT8     | Unsigned 8-bit integer             |
| 0x0003           | INT16     | Signed 16-bit integer              |
| 0x0004           | UINT16    | Unsigned 16-bit integer            |
| 0x0005           | INT32     | Signed 32-bit integer              |
| 0x0006           | UINT32    | Unsigned 32-bit integer            |
| 0x0007           | INT64     | Signed 64-bit integer              |
| 0x0008           | UINT64    | Unsigned 64-bit integer            |
| 0x0009           | INT128    | Signed 128-bit integer             |
| 0x000A           | UINT128   | Unsigned 128-bit integer           |
| 0x4001           | AINT8     | Array of signed 8-bit integers     |
| 0x4002           | AUINT8    | Array of unsigned 8-bit integers   |
| 0x4003           | AINT16    | Array of signed 16-bit integers    |
| 0x4004           | AUINT16   | Array of unsigned 16-bit integers  |
| 0x4005           | AINT32    | Array of signed 32-bit integers    |
| 0x4006           | AUINT32   | Array of unsigned 32-bit integers  |
| 0x4007           | AINT64    | Array of signed 64-bit integers    |
| 0x4008           | AUINT64   | Array of unsigned 64-bit integers  |
| 0x4009           | AINT128   | Array of signed 128-bit integers   |
| 0x400A           | AUINT128  | Array of unsigned 128-bit integers |
| 0xFFFF           | STR       | Variable-length Unicode string     |
| All other values | Undefined | Reserved (PTP)                     |

#### 3.2.2 Arrays

Arrays are defined in PTP (and thus MTP) as a concatenation of the same fixed-length
type. MTP does not define an array of strings. The size of each element is identified by
the simple type that is contained in the array (see 3.2.2.1). Arrays in MTP start with an
unsigned 32-bit integer that identifies the number of elements to follow, followed by a
concatenation of repeated instances of the simple type identified by the array’s datatype
code. For the purposes of this specification, arrays are considered to be zero-based.

An empty array is represented by a single 32-bit integer containing a value of
0x00000000.

##### 3.2.2.1 Array Definition

| Field                     | Size (bytes) | Format  |
|---------------------------|--------------|---------|
| NumElements               | 4            | UINT32  |
| ArrayEntry[0]             | Element Size | Special |
| ArrayEntry[1]             | Element Size | Special |
| …                         | …            | …       |
| ArrayEntry[NumElements-1] | Element Size | Special |

#### 3.2.3 Strings

Strings in PTP (and thus MTP) consist of standard 2-byte Unicode characters as defined
by ISO 10646. Strings begin with a single, 8-bit unsigned integer that identifies the
number of characters to follow (not bytes). An empty string is represented by a single 8-
bit integer containing a value of 0x00. A non-empty string is represented by the count
byte, a sequence of Unicode characters, and a terminating Unicode L'\0' character
(“null”). Strings are limited to 255 characters, including the terminating null character.

It should be noted that strings with embedded nulls are not permitted.

Examples:
The string L"" is represented as the single byte 0x00.
The string L"A" is represented as the five-byte sequence 0x02 0x41 0x00 0x00 0x00.

##### 3.2.3.1 String Definition

| Dataset field     | Size (bytes) | Datatype                       |
|-------------------|--------------|--------------------------------|
| NumChars          | 1            | UINT8                          |
| String Characters | Variable     | Unicode null-terminated string |

#### 3.2.4 Decimal Types

MTP does not include decimal values as a data type. They may be represented using the
string datatype where required, or the unit of measurement can be subdivided to allow a
particular level of precision (for example, measure in thousandths instead of having
decimals to three places).

#### 3.2.5 DateTime

DateTime strings follow a compatible subset of the definition found in ISO 8601, and
take the form of a Unicode string formatted as: "YYYYMMDDThhmmss.s". In this
representation, YYYY shall be replaced by the year, MM replaced by the month (01-12),
DD replaced by the day (01-31), T is a constant character ‘T’ delimiting time from date,
hh is replaced by the hour (00-23), mm is replaced by the minute (00-59), and ss by the
second (00-59). The ".s" is optional, and represents tenths of a second.

This string can optionally be appended with a constant character “Z” to indicate UTC, or
+/-hhmm to indicate that the time is relative to a time zone. Appending neither indicates
that the time zone is unspecified.

Leap seconds are not used in MTP.

The following regular expression accurately defines DateTime strings:
```
[0-9]{4}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3])([0-5][0-9])([0-5][0-9])(\.[0-9])?(Z|[+-]([01][0-9]|2[0-3])([0-5][0-9]))?
```

### 3.3 Datacodes

In MTP, all protocol traffic is binary and of fixed length. In order to enable this, all
operations, responses, events, object formats, and properties are represented by assigned
16-bit datacodes.

Datacodes are assigned from a range which is partitioned by origin (PTP, MTP or Vendor
Extension) as well as function. Though this assignment is explicitly partitioned, the
location of a datacode in a range in the table below shall not be used to interpret the
datacode; rather, all datacodes shall be individually recognized by their specific value.

As the MTP vendor-extension set occupies the vendor-extension datacode ranges of PTP,
the MTP ranges have been further subdivided to allow vendor extensions to MTP.

#### 3.3.1 Datacode Summary

| Bit 15 | Bit 14 | Bit 13 | Bit 12 | Bit 11 | Bit 10 | Bits 9-0 | Values          | Datacode type                       |
|--------|--------|--------|--------|--------|--------|----------|-----------------|-------------------------------------|
| 0      | 0      | 0      | 0      | Any    | Any    | Any      | 0..0xFFF        | Undefined                           |
| 0      | 0      | 0      | 1      | Any    | Any    | Any      | 0x1000.. 0x1FFF | PTP Operation Code                  |
| 0      | 0      | 1      | 0      | Any    | Any    | Any      | 0x2000.. 0x2FFF | PTP Response Code                   |
| 0      | 0      | 1      | 1      | Any    | Any    | Any      | 0x3000.. 0x3FFF | PTP Object Format Code              |
| 0      | 1      | 0      | 0      | Any    | Any    | Any      | 0x4000.. 0x4FFF | PTP Event Code                      |
| 0      | 1      | 0      | 1      | Any    | Any    | Any      | 0x5000.. 0x5FFF | PTP Device Prop Code                |
| 0      | 1      | 1      | 0      | Any    | Any    | Any      | 0x6000.. 0x6FFF | Reserved (PTP)                      |
| 0      | 1      | 1      | 1      | Any    | Any    | Any      | 0x7000.. 0x7FFF | Reserved (PTP)                      |
| 1      | 0      | 0      | 0      | Any    | Any    | Any      | 0x8000.. 0x8FFF | Undefined                           |
| 1      | 0      | 0      | 1      | 0      | Any    | Any      | 0x9000.. 0x97FF | Vendor Extension Operation Code     |
| 1      | 0      | 0      | 1      | 1      | Any    | Any      | 0x9800.. 0x9FFF | MTP Operation Code                  |
| 1      | 0      | 1      | 0      | 0      | Any    | Any      | 0xA000.. 0xA7FF | Vendor Extension Response Code      |
| 1      | 0      | 1      | 0      | 1      | Any    | Any      | 0xA800.. 0xAFFF | MTP Response Code                   |
| 1      | 0      | 1      | 1      | 0      | Any    | Any      | 0xB000.. 0xB7FF | Vendor Extension Object Format Code |
| 1      | 0      | 1      | 1      | 1      | Any    | Any      | 0xB800.. 0xBFFF | MTP Object Format Code              |
| 1      | 1      | 0      | 0      | 0      | Any    | Any      | 0xC000..0xC7FF  | Vendor Extension Event Code         |
| 1      | 1      | 0      | 0      | 1      | Any    | Any      | 0xC800..0xC8FF  | MTP Event Code                      |
| 1      | 1      | 0      | 1      | 0      | 0      | Any      | 0xD000..0xD3FF  | Vendor Extension Device Prop Code   |
| 1      | 1      | 0      | 1      | 0      | 1      | Any      | 0xD400..0xD7FF  | MTP Device Prop Code                |
| 1      | 1      | 0      | 1      | 1      | 0      | Any      | 0xD800..0xDBFF  | Vendor Extension Object Prop Code   |
| 1      | 1      | 0      | 1      | 1      | 1      | Any      | 0xDC00..0xDFFF  | MTP Object Prop Code                |
| 1      | 1      | 1      | 0      | Any    | Any    | Any      | 0xE000..0xEFFF  | Reserved (PTP)                      |
| 1      | 1      | 1      | 1      | Any    | Any    | Any      | 0xF000..0xFFFF  | Reserved (PTP)                      |

Individual datacode types are explained in the appropriate sections of this document.

### 3.4 Object Handles

Object handles are 32-bit identifiers that provide a device- and session-unique consistent
reference to a logical object on a device. All handles are represented using the UINT32
simple type. There is no special meaning attached to the value of object handles; they
may be chosen in any manner that facilitates device implementation.

Object handles are used in MTP transactions to reference a logical object on the device,
but do not necessarily reference actual data constructs on the device. As identified in
section 1.3, objects may be exposed through MTP that will be created on-demand. Object
handles are only persistent within an MTP session; once a session has been re-opened, all
previous values shall be assumed to be invalid, and the contents of the Responder must be
re-enumerated if object handles are needed.

The values "0xFFFFFFFF" and "0x00000000" have special meaning and shall not be
assigned to objects. The meanings of those values are context-specific.

#### 3.4.1 Assigning Object Handles

Object Handles are assigned by the responder. They must be globally unique across all
storages on the device.

Object Handles are only defined within an open session. If the Initiator has not yet
opened a session, object handles do not have any meaning and cannot be used. When a

session is closed, either intentionally by the initiator or as a result of an error or USB
interruption, all Object Handles are invalidated and must be re-acquired by the Initiator.
Object Handles do not persist between sessions.

If an object is deleted in a session, the Responder shall not re-use the deleted object’s
Object Handle in the same session.

### 3.5 Object Formats

As MTP is file-system-agnostic, the usual method of overloading file extensions to
determine file type is not a reliable method of identifying device contents. In many
cases, objects on a device may have no qualified filename, or may not even exist until
requested for transfer by the Initiator.

Instead, object formats are identified using predefined ObjectFormat datacodes.

#### 3.5.1 Object Format Versions

The version information for a particular object format shall be contained in the object
itself in a format-specific way, and declaring support for an object format type implies
that the Responder is able to parse the data object to determine the appropriate version,
and able to decode the data contained within.

If an object format has multiple versions all identified by the same ObjectFormat
datacode, then any device that indicates support for that ObjectFormat shall be able to
interpret and consume any version of that format. If an object format defined by this
specification is not self versioning, different ObjectFormat types are assigned for each
version. Vendor-defined ObjectFormat types shall follow this convention.

### 3.6 Associations

Associations are used in MTP to describe hierarchical file systems on devices.
Responders and Initiators that are based on the PTP standard also use Associations to
provide a limited method of associating related image and data objects.

The use of Associations has been superseded in MTP by the concept of object references.
Refer to section 5.3.3 for more information about object references.

Associations other than type 0x1 (hierarchical) aren’t used in MTP, and should not be
unless a PTP device is being developed. In that case, the associations rules should be
followed from the PTP specification and the object references references from this
specification.

#### 3.6.1 Association Types

Associations represent various collections of objects. The kind of collection is conveyed
by the Association Type field in the ObjectInfo dataset, and is also exposed in the
Association Type object property.

The Association Description field, also contained in the ObjectInfo dataset, provides
additional information to further qualify the Association type. The meaning of the
Association Description field varies depending on the Association Type.

#### 3.6.2 Association Type Summary

| Association code                                          | Association type     | AssociationDesc interpretation                        |
|-----------------------------------------------------------|----------------------|-------------------------------------------------------|
| 0x0000                                                    | Undefined            | Undefined                                             |
| 0x0001                                                    | Generic Folder       | Unused by PTP; used by MTP to indicate type of folder |
| 0x0002                                                    | Album                | Reserved                                              |
| 0x0003                                                    | Time Sequence        | Default Playback Delta                                |
| 0x0004                                                    | Horizontal Panoramic | Unused                                                |
| 0x0005                                                    | Vertical Panoramic   | Unused                                                |
| 0x0006                                                    | 2D Panoramic         | Images per row                                        |
| 0x0007                                                    | Ancillary Data       | Undefined                                             |
| All other values with bit 15 set to 0                     | Reserved             | Unused                                                |
| All other values with bit 15 set to 1 and bit 14 set to 0 | Vendor-defined       | Undefined                                             |
| All other values with bit 15 set to 1 and bit 14 set to 1 | MTP                  | Undefined                                             |

##### 3.6.2.1 Generic Folder

Association objects with this Association Type represent hierarchical folders rooted on a
particular storage. This provides a mechanism of exposing a file hierarchy on the device
without relying on any path or naming conventions specific to a particular file system.

The AssociationDesc field of a Generic Folder Association may contain either
0x00000000 or 0x00000001. If it contains a value of 0x00000001, this indicates that it is
a bi-directionally linked folder, and must have Object References to each object
"contained" by this association (each object which contains this Association’s
ObjectHandle in the ParentID field of its ObjectInfo dataset).

Note that a PTP Initiator or Responder only has a defined response if a value of
0x00000000 is used in the AssociationDesc field.

##### 3.6.2.2 Album

This Association Type is PTP-specific. For more information, please refer to the
documents referenced in “USB Still Image Capture Device Definition – July 2000”.

##### 3.6.2.3 Time Sequence

This Association Type is PTP-specific. For more information, please refer to the
documents referenced in “USB Still Image Capture Device Definition – July 2000”.

##### 3.6.2.4 Horizontal Panoramic

This Association Type is PTP-specific. For more information, please refer to the
documents referenced in “USB Still Image Capture Device Definition – July 2000”.

##### 3.6.2.5 Vertical Panoramic

This Association Type is PTP-specific. For more information, please refer to the
documents referenced in “USB Still Image Capture Device Definition – July 2000”.

3.6.2.6 2D Panoramic
This Association Type is PTP-specific. For more information, please refer the documents
referenced in “USB Still Image Capture Device Definition – July 2000”.

##### 3.6.2.7 Ancillary Data

This Association Type is PTP-specific. For more information, please refer the documents
referenced in “USB Still Image Capture Device Definition – July 2000”.

#### 3.6.3 Associations as File System Folders

The primary usage of Associations in MTP is to expose a hierarchical file system present
on the device. By making use of Associations in the communications protocol,
hierarchies may be represented without requiring any particular file name or path name
conventions, or any understanding of the device file system.

Folder hierarchies are storage-specific, and are exposed in a bottom-up fashion using the
Parent Object field in the ObjectInfo dataset. This field contains the Object Handle of
the Association that “contains” the object. The Parent Object field is also identified by
the appropriate object property (for more information, see the section on Object
Properties).

Only objects of type Association may be referenced in the Parent Object field/property.
By representing object hierarchies in a bottom-up way, associations are stateless with
regard to which objects are their children, as only children identify their parents. In this
way, object deletion does not result in having to re-establish the object hierarchy already
communicated.

Objects that exist in the root of the storage shall contain a value of 0x00000000 in the
Parent Object field/property.

A full path name may be reconstructed by traversing the parentage of a particular object,
concatenating each Filename with an appropriate delimiter, in a file-system-specific way.

#### 3.6.4 Associations and Object References

MTP enhances Associations using object references, which make generic folder
Association objects more efficient. This feature can be used when an Association object
represents a generic folder (Association Type = 0x0001), if the value of the
AssociationDesc field is 0x00000001.

For such Associations, GetObjectReferences must return references to all of the objects
contained in the folder. When objects are added to or deleted from such a folder
(whether by the Initiator or Responder), the reference list shall be updated automatically.

### 3.7 MTP Extensibility

The vendor-extension mechanism described in the following section addresses two major
scenarios. The first scenario is allowing a vendor to access the functionality of the USB-
IF PTP extensions while still providing their own extensions, either pre-existing or
created at a later date. The second scenario is enabling vendors that do not have an
assigned VendorExtensionID to extend the protocol as they require.

This extension scheme allows multiple vendor-extension sets to be implemented
concurrently, as long as their assigned datacodes do not overlap. It is the responsibility of
the device vendor to avoid such conflicts.

#### 3.7.1 Identifying Vendor Extension Support

Devices identify their support for vendor extensions using the VendorExtensionDesc
field of the DeviceInfo dataset. The VendorExtensionDesc field is of datatype string,
and provides a human-readable description of the supported extensions. Each supported
extension is represented in the string value, with both the name of the extension set and
the version number of the extension set. The name and version number of the extension
set must follow a specific format:

 The name must be a valid internet domain name, owned and operated by the
organization defining the extension set.
 The version number must have the traditional format of a Dewey decimal number.
 The name of the extension set is terminated with the colon character, and the version
number is terminated with the semicolon character. A single space is required after
each terminator character (':' and ';').

Example: "abc.com: 1.0; "

If several extension sets are implemented by the device, the series of names and version
numbers of the extension sets are joined in the string value. The order of the extension
sets within the value is not meaningful; the extension sets can be re-ordered within the
value with no effect on the device implementation.

Example: "company1.com: 1.2; company2.com: 2.1.4; "

#### 3.7.2 Linking to Extension Documentation and Specification

Extension set names and version numbers can be used to find human-readable
documentation and machine-readable definitions on the Internet. The extension-set name
and version number are placed into a template URL and used to reference both types of
information. The following URL template is used to build the target URL:

“http://www.[name]/standards/protocols/mtp/[version]/

Where the extension set name replaces the [name] parameter, and the extension set
version number replaces the [version] parameter. For example, the extension set for
"abc.com: 1.1;" has an extension set name of "abc.com" and an extension set version
number of "1.1". Replacing the [name] and [version] parameters in the URL template
would produce the target URL:

"http://www.abc.com/standards/protocols/mtp/1.1/"

The type of the HTTP request determines which type of information is returned,
assuming that the information is available on a public server. A request for HTML will
return the human-readable documentation describing the extension set, and a request for
XML will return the machine-readable XML schema describing the extension set.

It is not required that all extensions be documented in this way, but it is very strongly
recommended.

#### 3.7.3 Allowed Datacode Ranges

Datacodes for vendor extensions to this extension set must fall within the ranges
identified within each datacode definition as being reserved for vendor extensions to
MTP. This is a subdivision of the standard vendor-extension ranges of PTP. If no vendor-
extension range exists for the datacode that a vendor wants to extend, the vendor must
attempt to determine an alternate implementation of the desired functionality or request a
revision to this specification.

