## 5 Device Model

MTP is a protocol designed to represent an abstracted view of a device which can be
loosely defined by the following criteria:

- It has storage.
- It interacts with its own storage.
- It fulfils its primary purpose while not in an MTP session.
- It frequently connects to other devices using MTP in order to exchange and update content.

### 5.1 Device Representation

In MTP, a device has equal prominence within the protocol as its contents.
Understanding the capabilities and properties of a device enables a number of important
scenarios above and beyond simple data transfer.
Examples of enabled scenarios include:

- Rich UI representation of a connected device
- Matching content to device capabilities
- Meta-functionality on objects, such as DRM
- Device state awareness, such as battery level or capture settings
- Device command and control
- Etc.

These scenarios are implemented by a combination of a standard device-describing
dataset (the DeviceInfo dataset) to provide basic device capabilities, which is always
present and implicit in MTP functionality; and flexible and extensible device properties.
Both are discussed in more detail below.

#### 5.1.1 DeviceInfo Dataset

The DeviceInfo dataset is used to provide a description of the device. This dataset can be
obtained using the GetDeviceInfo operation without first initiating a session, and is
mostly static. If any value in this dataset is changed while a session is active, a
DeviceInfoChanged event shall be issued to each connected Initiator, and each Initiator
must re-acquire the DeviceInfo dataset to determine the updated values.

An example of a situation where the DeviceInfo dataset could change within a session is
as a reaction to a change in the Functional Mode of the device. A device may enter a
"sleep" state where it has a limited (but sufficient) set of enabled MTP operations and
functionality. When such a state is entered, a DeviceInfoChanged event is issued to each
active session to alert them to the changed functionality of the device.

| Dataset field               | Field order | Size (bytes) | Datatype                   |
|-----------------------------|-------------|--------------|----------------------------|
| Standard Version            | 1           | 2            | UINT16                     |
| MTP Vendor Extension ID     | 2           | 4            | UINT32                     |
| MTP Version                 | 3           | 2            | UINT16                     |
| MTP Extensions              | 4           | Variable     | String                     |
| Functional Mode             | 5           | 2            | UINT16                     |
| Operations Supported        | 6           | Variable     | Operation Code Array       |
| Events Supported            | 7           | Variable     | Event Code Array           |
| Device Properties Supported | 8           | Variable     | Device Property Code Array |
| Capture Formats             | 9           | Variable     | Object Format Code Array   |
| Playback Formats            | 10          | Variable     | Object Format Code Array   |
| Manufacturer                | 11          | Variable     | String                     |
| Model                       | 12          | Variable     | String                     |
| Device Version              | 13          | Variable     | String                     |
| Serial Number               | 14          | Variable     | String                     |

##### 5.1.1.1 Standard Version

This identifies the PTP version this device can support in hundredths. For MTP devices
implemented under this specification, this shall contain the value 100 (representing 1.00).

##### 5.1.1.2 MTP Vendor ExtensionID

This identifies the PTP vendor-extension version in use by this device. For MTP devices
implemented under this specification, this shall contain the value 0xFFFFFFFF.

##### 5.1.1.3 MTP Version

This identifies the version of the MTP standard this device supports. It is expressed in
hundredths. The final version of this specification will identify the correct value to place
in this field.

##### 5.1.1.4 MTP Extensions

This string is used to identify any extension sets applied to MTP, and is discussed in
length later in this specification.

##### 5.1.1.5 Functional Mode

Modes allow the device to express different states with different capabilities. If the device
supports only one mode, this field shall contain the value 0x00000000.

| Value                                                     | Description             |
|-----------------------------------------------------------|-------------------------|
| 0x0000                                                    | Standard mode           |
| 0x0001                                                    | Sleep state             |
| All other values with bit 15 set to 0                     | Reserved                |
| 0xC001                                                    | Non-responsive playback |
| 0xC002                                                    | Responsive playback     |
| All other values with bit 15 set to 1 and bit 14 set to 0 | MTP vendor extension    |
| All other values with bit 15 set to 1 and bit 14 set to 1 | MTP-defined             |

The current functional mode is also contained in a device property. In order to change the
functional mode of the device, a session must be opened and the appropriate device
property updated (if allowed). More information about device properties is available later
in this document.

##### 5.1.1.6 Operations Supported

This field identifies by datacode all operations that this device supports in the current
functional mode.

##### 5.1.1.7 Events Supported

This field identifies by datacode all events that this device can generate in the current
functional mode.

##### 5.1.1.8 Device Properties Supported

This field identifies by datacode all device properties that this device supports in the
current functional mode.

##### 5.1.1.9 Capture Formats

This field identifies by datacode the object format codes for each format that this device
can generate independently (that is, without the content being placed on the device).

##### 5.1.1.10 Playback Formats

This field identifies by datacode the object format codes for each format that this device
can understand and parse if placed on the device.

If the device can carry unidentified binary objects without understanding them, it shall
indicate this by including the Undefined Object (0x3000) code in its Playback Formats.

##### 5.1.1.11 Manufacturer

This optional string is a human-readable string identifying the manufacturer of this
device.

##### 5.1.1.12 Model

This optional string is a human-readable string identifying the model of this device.

##### 5.1.1.13 Device Version

This optional string identifies the software or firmware version of this device in a vendor-
specific format.

##### 5.1.1.14 Serial Number

This string is required, and contains the MTP function’s serial number. Serial numbers
are required to be unique among all MTP functions sharing identical Model and Device
Version fields (this field was optional in the PTP specification, but is required in MTP).
The serial number should be the device’s unique serial number such as the one typically
printed on the device.

The serial number shall be a 32 character hexadecimal string for legacy compatibility
reasons. This string must be exactly 32 characters, including any leading 0s, and does not
require any prefix to identify it as hexadecimal (such as ‘0x’).

#### 5.1.2 Device Properties

This section describes device properties. Device-property support is a mandatory part of
PTP, and remains unchanged in MTP beyond additional, added device properties.

Device properties identify settings or state conditions of the device, and are not linked to
any data objects on the device. Objects on the device are described using Object
Properties, which are discussed further in section 5.3.2 Object Properties.

Device Properties may be read-only or read-write, and serve different functions
depending on the context in which they are used. A single device may have only one set
of device properties, and they must be the same across all sessions and connections.

##### 5.1.2.1 Device Property Describing Dataset

Device properties are defined by their DevicePropDesc dataset, which can be retrieved
with the GetDevicePropDesc operation.

The DevicePropDesc dataset includes the device property value, read/write settings for
the property, a default value and, where relevant, any restrictions on allowed values.

Restrictions on the allowed values of a device property are communicated using
additional fields following the core dataset. The format of the additional forms is
determined by a flag in the sixth field, which enumerates allowed forms.

| Field name            | Field order | Size (bytes) | Datatype | Description                                                                                                                                                                |
|-----------------------|-------------|--------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device Property Code  | 1           | 2            | UINT16   | A specific device property code.                                                                                                                                           |
| Datatype              | 2           | 2            | UINT16   | Identifies the data type code of the property, as defined in section 3.2 Simple Types.                                                                                     |
| Get/Set               | 3           | 1            | UINT8    | Indicates whether the property is read-only (Get), or read-write (Get/Set). 0x00 Get 0x01 Get/Set                                                                          |
| Factory Default Value | 4           | DTS          | DTS      | Identifies the value of the factory default for the property.                                                                                                              |
| Current Value         | 5           | DTS          | DTS      | Identifies the current value of this property.                                                                                                                             |
| Form Flag             | 6           | 1            | UINT8    | Indicates the format of the next field. 0x00 None. This is for properties like DateTime. In this case the FORM field is not present. 0x01 Range-Form 0x02 Enumeration-Form |
| FORM                  | N/A         | Variable     | -        | This dataset depends on the Form Flag, and is absent if Form Flag = 0x00.                                                                                                  |

5.1.2.1.1 Range Form

| Field name    | Field order | Size (bytes) | Datatype | Description                                                                                                                                                                                         |
|---------------|-------------|--------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum Value | 7           | DTS          | DTS      | Minimum value supported by this property.                                                                                                                                                           |
| Maximum Value | 8           | DTS          | DTS      | Maximum value supported by this property.                                                                                                                                                           |
| Step Size     | 9           | DTS          | DTS      | A particular vendor's device shall support all values of a property defined by Minimum Value + N x Step Size, which is less than or equal to Maximum Value where N= 0 to a vendor- defined maximum. |

5.1.2.1.2 Enumeration Form

| Field name        | Field order | Size (bytes) | Datatype | Description                                                                                               |
|-------------------|-------------|--------------|----------|-----------------------------------------------------------------------------------------------------------|
| Number Of Values  | 7           | 2            | UINT16   | This field indicates the number of values of size DTS of the particular property supported by the device. |
| Supported Value 1 | 8           | DTS          | DTS      | A particular vendor's device shall support this value of the property.                                    |
| Supported Value 2 | 9           | DTS          | DTS      | A particular vendor's device shall support this value of the property.                                    |
| Supported Value 3 | 10          | DTS          | DTS      | A particular vendor's device shall support this value of the property.                                    |
| …                 | …           | …            | …        | …                                                                                                         |
| Supported Value M | M+7         | DTS          | DTS      | A particular vendor's device shall support this value of the property.                                    |

##### 5.1.2.2 Retrieving Device Properties

Device Properties may be retrieved by one of two methods: They may be retrieved as a
part of the Device Property Description Dataset returned by the GetDevicePropDesc
operation, or they may be retrieved in a more-streamlined fashion by the
GetDevicePropValue operation.

If both operations are supported by a Responder, the Initiator may use the
GetDevicePropValue whenever the additional information contained in the
DevicePropDesc dataset is not required. If a Responder is to optimize device-property
retrieval, it shall enable and implement the GetDevicePropValue operation. Similarly, if
an Initiator wishes to be performance-conscious when retrieving device properties, it
should use the GetDevicePropValue operation if implemented. The
GetDevicePropDesc/GetDevicePropValue operation should only be called when
information other than the DevicePropDesc dataset is required.

##### 5.1.2.3 Setting Device Properties

Device property values may be set by the SetDevicePropValue operation, or may be
updated as a result of changes to the state of the device. It is also permitted for a device
property to be static, to provide information about the device that is not contained by the
DeviceInfo dataset.

When a device property value is changed by a SetDevicePropValue operation request,
all connected Initiators shall be alerted to the change with a DevicePropChanged event,
except the Initaitor that directly caused the change. If a device property value is updated
by any mechanism except the SetDevicePropValue operation, then all connected
Initiators shall receive the DevicePropChanged event, including any Initiators that may
have indirectly caused the property to be changed.

Device properties shall all be set atomically, and the act of setting one device property
does not imply a change to any other device property. In cases where device property
values are inherently intertwined, this specification combines those values into a single
property where possible. For example, Width and Height are combined into the Image
Size property.

If updating one property changes the indicated allowed values for another property, such
as if increasing the Image Size reduced the allowed Bit Depth settings, this should be
indicated using the DevicePropChanged event.

##### 5.1.2.4 Device Properties as Device Control

Device Properties may be read-only or read-write. In the case where device properties
identify the current functional state of the device, the state may be changed through the
use of a writeable device property.

An example of a Device Property used for functional control of the device is the Digital
Zoom device property, which identifies not only the current Digital Zoom setting, but
also allows the initiator to set a new Digital Zoom setting. Another example is the
Functional Mode device property.

### 5.2 Storage Representation

MTP devices generally include a substantial amount of persistent data storage, either
contained in the device or on a removable storage medium. This section provides
additional information about the required representation of that storage.

#### 5.2.1 Storage IDs

Storages are identified in MTP using a 32-bit unsigned integer (UINT32), called a
StorageID. The StorageID is subdivided into two halves, the most-significant 16 bits
and the least-significant 16 bits. The most-significant 16 bits identify a physical storage
location, such as a removable memory card or an internal memory bank. The least-
significant 16 bits identify a logical partition of that physical storage.

Devices may contain zero or more physical storages, and each physical storage may have
zero or more logical storages. Each physical storage is defined by a unique 16-bit code
occupying the most-significant 16 bits of the StorageID. If two StorageIDs contain an
identical, top-most 16 bits, they are assumed to exist on the same physical component of

the device. The upper 16-bits of the StorageID may contain any values except 0x0000
and 0xFFFF, which may have special meaning, depending on the lower 16 bits.

If a physical storage contains no logical storages, it shall be represented using a single
StorageID in which the least-significant 16-bit segment contains the value 0x0000. Any
storage for which the lower 16 bits are 0x0000 is assumed to neither contain any data nor
be able to have data written to it.

If a physical storage contains one or more logical storages, each storage must contain the
same top-most 16-bit segment, to indicate that it is located in the same physical location.

Logical stores are defined by the lower 16-bits of the StorageID. Each logical storage on
a physical storage must be identified by a unique 16-bit segment. The lower 16 bits of the
StorageID may contain any value but 0x0000 (which has special meaning as outlined
previously) and 0xFFFF (which may have special meaning depending on the upper-most
16 bits).

A StorageID of 0x00000000 or 0xFFFFFFFF has special meaning, depending on
context, such as "All Storages" or "default store", and does not refer to an actual storage.
The meaning is explained with the operation/response/event where it is used.

StorageIDs shall not be assumed to persist between sessions.

#### 5.2.2 StorageInfo Dataset Description

This dataset describes a storage contained in a device.

| Dataset field          | Field order | Length (bytes) | Datatype |
|------------------------|-------------|----------------|----------|
| Storage Type           | 1           | 2              | UINT16   |
| Filesystem Type        | 2           | 2              | UINT16   |
| Access Capability      | 3           | 2              | UINT16   |
| Max Capacity           | 4           | 8              | UINT64   |
| Free Space In Bytes    | 5           | 8              | UINT64   |
| *Free Space In Objects | 6           | 4              | UINT32   |
| Storage Description    | 7           | Variable       | String   |
| Volume Identifier      | 8           | Variable       | String   |

##### 5.2.2.1 Storage Type

This field identifies the physical nature of the storage described by this dataset. If the
Storage Type is read-only memory (0x0001 or 0x0002), it supersedes any protection
status indicated by the Access Capability field.

Allowed values are shown in the following table.

| Code value       | Description   |
|------------------|---------------|
| 0x0000           | Undefined     |
| 0x0001           | Fixed ROM     |
| 0x0002           | Removable ROM |
| 0x0003           | Fixed RAM     |
| 0x0004           | Removable RAM |
| All other values | Reserved      |

##### 5.2.2.2 Filesystem Type

This field identifies the logical file system in use on this storage. This field may be used
to define the file-naming conventions or directory structure conventions in use on this
storage, as well as indicate support for a hierarchical file system.

Allowed values are shown in the following table.

| Code Value                                                | Description          |
|-----------------------------------------------------------|----------------------|
| 0x0000                                                    | Undefined            |
| 0x0001                                                    | Generic flat         |
| 0x0002                                                    | Generic hierarchical |
| 0x0003                                                    | DCF                  |
| All other values with bit 15 set to 0                     | Reserved             |
| All other values with bit 15 set to 1 and bit 14 set to 0 | MTP vendor extension |
| All other values with bit 15 set to 1 and bit 14 set to 1 | MTP-defined          |

##### 5.2.2.3 Access Capability

This field identifies any write-protection that globally affects this storage (this supersedes
any protection status on individual objects). If the Storage Type field indicates that this
storage is defined as ROM (0x0001 or 0x0002), this field must contain the value 0x0001
(read-only without object deletion).

Allowed values are shown in the following table.

| Code value       | Description                       |
|------------------|-----------------------------------|
| 0x0000           | Read-write                        |
| 0x0001           | Read-only without object deletion |
| 0x0002           | Read-only with object deletion    |
| All other values | Reserved                          |

##### 5.2.2.4 Max Capacity

This field identifies the maximum capacity in bytes of this storage. If this storage can be
written to, that is, the storage type is not read-only and the access capability is read-write,

then this field must contain an accurate value. If the storage is read-only, this field is
optional.

##### 5.2.2.5 Free Space In Bytes

This field indicates how much space remains to be written to on the drive. If this storage
can be written to, that is, the storage type is not read-only and the access capability is
read-write, then this field must contain an accurate value. If the storage type is read-only,
this field is optional. If Free Space In Bytes does not apply to this device or this storage,
and it can be written to, this field may contain a value of 0xFFFFFFFF, and the Free
Space In Objects field may be used instead.

##### 5.2.2.6 Free Space In Objects

This field indicates how many additional objects may be written to this device. This field
shall only be used if there is a reasonable expectation that the number of objects that
remain to be written can be accurately predicted (for instance, if the device contains only
one object type of fixed size.).
If this field is not used, it shall be set to 0xFFFFFFFF.

##### 5.2.2.7 Storage Description

This optional field contains a human-readable string identifying this storage, such as
"256Mb SD Card" or "20Gb HDD". If unused, it shall contain an empty string.

##### 5.2.2.8 Volume Identifier

This field contains a unique, programmatically relevant volume identifier, such as a serial
number. This field may be up to 255 characters long, however, only the first 128
characters will be used to identify the device, and these first 128 characters must be
unique for all storages. If this field does not contain a string in which the first 128
characters are unique, it must contain an empty string.

#### 5.2.3 Defining Access Restrictions

If the device has restrictions on allowed operations on the content of the device, such as
read-only, or read-deletion only, this shall be indicated in the AccessCapability field of
the StorageInfo dataset. For more information, refer to section 5.2.2 StorageInfo Dataset
Description.

### 5.3 Content Representation

In MTP, all contents of a device are represented as objects. Objects are abstract
containers for a variety of data, which each represent an atomic element of information.
Examples of objects include:

- Image Files
- Audio/Video Files
- Contacts
- Calendar/Task Items
- Generic Binary Files
- Etc.

Objects are comprised of four parts: the object’s binary data, the ObjectInfo dataset,
Object Properties and Object References. Each component serves a different purpose,
and together they facilitate broad interoperability and a rich enumeration experience.

The ObjectInfo Dataset is a standard fixed dataset available for every object, and
provides basic information about an object. This information includes the object type,
object size, etc, and represents the information required for every object in order to
enable basic object management. The ObjectInfo dataset was originally defined in PTP,
and has been largely replaced in MTP by Object Properties.

Object Properties provide a flexible and extensible way of representing object metadata.
They may be used to describe a device in either (or both) a machine-readable or human-
readable way, and serve to not only describe the actual content of the object but also to
indirectly indicate the various structures a particular object format can take.

Finally, Object References provide an internal referencing feature within MTP, allowing
objects to associate themselves with other objects, a feature which would otherwise be
impossible without a standard persistent addressing mechanism.

#### 5.3.1 ObjectInfo Dataset Description

The ObjectInfo dataset provides an overview of the core properties of an object. These
properties are also retrievable as Object Properties (detailed later in this document), and
must be accessible through both mechanisms.

The contents of the ObjectInfo dataset were originally defined for imaging-centric
devices, and continue to be used for that purpose. For devices to be compatible with
existing PTP implementations, it is very important that this dataset be accurately filled
out in accordance with the PTP specification. For more information, please refer to that
document.

Many fields in the ObjectInfo dataset do not apply to non-imaging objects; these fields
shall be set to zero when not in use.

MTP still requires the use of the ObjectInfo dataset in various operations that require an
encapsulated view of core file attributes, such as when sending a new object to the
device. The fields that are required for the MTP SendObjectInfo operation are
specifically called out in the following table.

Fields marked with a * are supplanted in MTP with new mechanisms, but must be
implemented if PTP-compatibility is desired. Refer to the PTP specification for
implementation details for these fields.

| Dataset field           | Field order | Size (bytes) | Datatype         | Required for SendObjectInfo |
|-------------------------|-------------|--------------|------------------|-----------------------------|
| StorageID               | 1           | 4            | StorageID        | No                          |
| Object Format           | 2           | 2            | ObjectFormatCode | Yes                         |
| Protection Status       | 3           | 2            | UINT16           | No                          |
| Object Compressed Size  | 4           | 4            | UINT32           | Yes                         |
| *Thumb Format           | 5           | 2            | ObjectFormatCode | No                          |
| *Thumb Compressed Size  | 6           | 4            | UINT32           | No                          |
| *Thumb Pix Width        | 7           | 4            | UINT32           | No                          |
| *Thumb Pix Height       | 8           | 4            | UINT32           | No                          |
| Image Pix Width         | 9           | 4            | UINT32           | No                          |
| Image Pix Height        | 10          | 4            | UINT32           | No                          |
| Image Bit Depth         | 11          | 4            | UINT32           | No                          |
| Parent Object           | 12          | 4            | ObjectHandle     | No                          |
| Association Type        | 13          | 2            | Association Code | Yes                         |
| Association Description | 14          | 4            | AssociationDesc  | Yes                         |
| *Sequence Number        | 15          | 4            | UINT32           | No                          |
| Filename                | 16          | Variable     | String           | Yes                         |
| Date Created            | 17          | Variable     | DateTime String  | No                          |
| Date Modified           | 18          | Variable     | DateTime String  | No                          |
| Keywords                | 19          | Variable     | String           | No                          |

##### 5.3.1.1 StorageID

The device storage on which the object defined by this dataset is located. For more
information about StorageIDs, refer to section 5.2.1 "Storage IDs".

##### 5.3.1.2 ObjectFormat

Every object format type is identified by an ObjectFormatCode. Refer to section 3.5
Object Formats for more information about Object Formats.

##### 5.3.1.3 Protection Status

An optional field that identifies the write-protection status of a data object. This field may
be updated using the SetProtection operation.

If the device does not support object protection, this field should always contain 0x0000,
the SetProtection operation should not be supported, and the only allowed value
identified in the ObjectPropDesc field should be 0x0000.

Read-only protection may modified with the SetObjectProtection operation if allowed by
the device. Read-only protection may not be modified by mechanisms used to set Object
Properties.

Allowed values are shown in the following table:

| Value            | Description           |
|------------------|-----------------------|
| 0x0000           | No protection         |
| 0x0001           | Read-only             |
| 0x8002           | Read-only data        |
| 0x8003           | Non-transferable data |
| All other values | Reserved              |

- **No Protection**: This object has no protection; it may be modified or deleted arbitrarily and its properties may be
  modified freely.
- **Read-only**: This object cannot be deleted or modified; none of the properties of this object can be modified by the
  initiator. (However, properties can be modified by the device that contains the object.)
- **Read-only data**: This object's binary component cannot be deleted or modified; however, any object properties may
  be modified if allowed by the object property constraints.
- **Non-transferable data**: This object's properties may be read and modified, and it may be moved or deleted on the
  device, but this object's binary data may not be retrieved from the device using a GetObject operation.

This property identifies the write-protection status of the binary component of the data object. The allowed values for
this property for a device should be enumerated in ObjectPropDesc dataset and are defined as follows:

| Value         | Description                                                                                                                                                                                                              |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0000        | No Protection - This object has no protection, it may be modified or deleted arbitrarily, and its properties may be modified freely.                                                                                     |
| 0x0001        | Read-only - This object cannot be deleted or modified, and none of the properties of this object can be modified by the initiator. (Properties may be modified by the device however.)                                   |
| 0x8002        | Read-only data - This object's binary component cannot be deleted or modified, however any object properties may be modified if allowed by the object property constraints.                                              |
| 0x8003        | Non-transferable data - This object's properties may be read and modified, and it may be moved or deleted on the device, but this object's binary data may not be retrieved from the device using a GetObject operation. |
| 0x0002-0x7FFF | Reserved for PTP                                                                                                                                                                                                         |
| 0x8004-0x8BFF | Reserved for MTP                                                                                                                                                                                                         |
| 0x8C00-0xFFFF | MTP Vendor Extension Range                                                                                                                                                                                               |

This property may be indirectly set using the SetObjectProtection operation.

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0xDC03                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | 0x00 (GET)            |
| DefaultValue | 4           | -            | -        | 0x0000                |
| GroupCode    | 5           | 4            | UINT32   | Device Defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration Form |

##### 5.3.1.4 Object Compressed Size

The size of the data component of the object in bytes. If the object is larger than 2^32
bytes in size (4GB), this field shall contain a value of 0xFFFFFFFF.

5.3.1.5 *Thumb Format, *Thumb Compressed Size, *Thumb Pix Width, *Thumb
Pix Height
These fields provide information about thumbnails of images on the device. In MTP,
thumbnail functionality has been supplanted with the Representative Sample Object
Properties, and in most cases these values shall be duplicated there.

If PTP-compatibility is desired, these fields shall be supported for all image objects, and
the associated operations shall be implemented.

##### 5.3.1.6 Image Pix Width

If the defined object is an image, this field identifies the width in pixels of that image.
This information is also available in MTP through the object property mechanism, but
shall be implemented here to maintain PTP-compatibility if desired.

##### 5.3.1.7 Image Pix Height

If the defined object is an image, this field identifies the height in pixels of that image.
This information is also available in MTP through the object property mechanism, but
shall be implemented here to maintain PTP-compatibility if desired.

##### 5.3.1.8 Image Bit Depth

If the defined object is an image, this field identifies the bit depth of that image. This
information is also available in MTP through the object property mechanism, but shall be
implemented here to maintain PTP-compatibility if desired.

##### 5.3.1.9 Parent Object

If this object exists in a hierarchy, this field contains the Object Handle of the parent of
this object. Only objects of type Association may be identified in this field. If this object
is in the root or the device does not support Associations, this field shall be set to
0x00000000.

More information about Associations is contained in section 3.6 Associations.

##### 5.3.1.10 Association Type

This field is only used for objects of type Association, and indicates what type of
Association it is. In MTP, the Generic Folder Association type is most commonly used,
which has an Association Type code of 0x0001.

More information about Associations is contained in section 3.6 Associations.

##### 5.3.1.11 AssociationDesc

This field is used only for objects of type Association, and provides additional
information about the implementation of this particular type.

More information about Associations is contained in section 3.6 Associations.

##### 5.3.1.12 Sequence Number

This field is used in PTP to further define certain non-folder types of associations. It is
not generally used in MTP, but should be implemented by any Responder that desires the
provided functionality and that wishes to interact with PTP Initiators.

More information about the use of Sequence Numbers in Associations is contained in
section 3.6 Associations.

##### 5.3.1.13 Filename

A string containing the file name of this object, without any directory or file system
information. This string is also accessible and defined via an Object Property, and
restrictions on its format may be identified in the Object Property Description for this
object property.

##### 5.3.1.14 Date Created

This field identifies the creation date of this object, and uses the DateTime string as
described in section 3.2.5 DateTime.

##### 5.3.1.15 Date Modified

This field identifies the date when this object was last modified, and uses the DateTime
string described in section 3.2.5 DateTime.

##### 5.3.1.16 Keywords

This field contains keywords associated with the object. Keywords shall be delimited by
a single space: " ". If a given keyword contains a space, the space shall be replaced with
an underscore character: "_".

#### 5.3.2 Object Properties

Object properties provide a mechanism for exchanging object-describing metadata
separate from the objects themselves. The primary benefit of this functionality is to
permit the rapid enumeration of large storages, regardless of the file-system.

In PTP, there is an existing mechanism for describing an object, the ObjectInfo dataset
(PTP Specification, section 5.5.2). This is a static and non-extensible dataset containing
basic information about the object, and assumes that the object being described is an
image object.

There is also an extensible property system in device properties (PTP Specification,
section 13). These properties are notable, as they define the format their values can take,
which allows for much safer device management. By restricting property values and
formats at the protocol level, the responder has a much simpler time parsing and
understanding that metadata for its own use.

Object properties combine these two concepts. They provide information about objects
on the device, and specify the values they can contain.

##### 5.3.2.1 Requirements for Object Property Support

A device that will implement object properties must support the following operations:

- GetObjectPropsSupported
- GetObjectPropValue
- GetObjectPropDesc

A corollary of this is that all devices that support these minimum requirements are
assumed to support object properties as a primary method of retrieving object metadata.

##### 5.3.2.2 Identifying Object Property Support

Devices that identify their support for the operations listed previously in their DeviceInfo
dataset are considered to support object properties, and will be treated as such by
initiators that understand the USB-IF PTP extension set. Devices that do not support the
minimum requirements listed previously will not be considered to support object
properties.

Object properties are format-specific. That is, for all objects on a device of the same
format, the same set of object properties will be supported. Discovering which object
properties are applied to a given object format is accomplished by the
GetObjectPropsSupported operation, with the format code passed as the argument in
the table in the next section.

The GetObjectPropsSupported operation returns an ObjectPropCode array of
supported object properties for the object format indicated in the first parameter. More
details about the GetObjectPropsSupported operation are available in the appropriate
appendix of this specification.

##### 5.3.2.3 Defining Object Properties

Object properties are defined by an ObjectPropDesc dataset much in the same way that
device properties are defined by their DevicePropDesc dataset (PTP Specification,
section 13.3.3).

Before an object property is queried for the first time, its ObjectPropDesc should be
retrieved from the device by using the GetObjectPropDesc operation. The
ObjectPropDesc dataset is defined in Table 5-1.

The GetObjectPropDesc operation returns the appropriate Property Describing Dataset,
indicated in the first parameter as defined for the Object Format indicated in the second
parameter. More details about the GetObjectPropDesc operation are available in
Appendix D.2.30 GetObjectPropDesc.

A base set of object properties are defined in the MTP specification, but many aspects of
an object property need to be defined by the device for its particular implementation,
particularly properties that the device will use for its own operations.

The ObjectPropDesc dataset is formatted as shown in the following table:
Table 5-1. ObjectPropDesc dataset

| Field name    | Field order | Size (bytes) | Datatype | Description                                                                                                                                                                                                                                     |
|---------------|-------------|--------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property Code | 1           | 2            | UINT16   | A specific ObjectPropCode identifying this property.                                                                                                                                                                                            |
| Datatype      | 2           | 2            | UINT16   | This field identifies the datatype code of the property.                                                                                                                                                                                        |
| Get/Set       | 3           | 1            | UINT8    | This field indicates whether the property is read-only (Get), or read-write (Get/Set). 0x00 = Get, 0x01 = Get/Set                                                                                                                               |
| Default Value | 4           | DTS          | DTS      | This field identifies the value of the factory default for the property.                                                                                                                                                                        |
| Group Code    | 5           | 4            | UINT32   | This field identifies the retrieval group this property belongs to.                                                                                                                                                                             |
| Form Flag     | 6           | 1            | UINT8    | This field indicates the format of the next field. 0x00 = None, 0x01 = Range form, 0x02 = Enumeration form, 0x03 = DateTime form, 0x04 = Fixed-length Array form, 0x05 = Regular Expression form, 0x06 = ByteArray form, 0xFF = LongString form |
| FORM          | N/A         | Variable     | -        | This dataset depends on the Form Flag, and is absent if Form Flag = 0x00.                                                                                                                                                                       |

5.3.2.3.1 Range Form

| Field name   | Field order | Size (bytes) | Datatype | Description                                                                                                            |
|--------------|-------------|--------------|----------|------------------------------------------------------------------------------------------------------------------------|
| MinimumValue | 7           | DTS          | DTS      | Minimum value supported by this property.                                                                              |
| MaximumValue | 8           | DTS          | DTS      | Maximum value supported by this property.                                                                              |
| Step Size    | 9           | DTS          | DTS      | The property shall support all values defined by MinimumValue+N*StepSize, which is less than or equal to MaximumValue. |

5.3.2.3.2 Enumeration Form

| Field name      | Field order | Size (bytes) | Datatype | Description                                                                                                               |
|-----------------|-------------|--------------|----------|---------------------------------------------------------------------------------------------------------------------------|
| NumberOfValues  | 7           | 2            | UINT16   | The number of values, of size DTS, supported by the property. These shall be listed in order of preference if applicable. |
| SupportedValue1 | 8           | DTS          | -        | The property shall support this value.                                                                                    |
| SupportedValue2 | 9           | DTS          | -        | The property shall support this value.                                                                                    |
| ...             | ...         | ...          | ...      | ...                                                                                                                       |
| SupportedValueM | 7+M         | DTS          | -        | The property shall support this value.                                                                                    |

5.3.2.3.3 DateTime Form
Properties that have the DateTime form have no additional fields. Date and time are
represented in ISO standard format as described in ISO 8601, from the most significant
number to the least significant number. This shall take the form of a Unicode string in the
format “YYYYMMDDThhmmss.s” where YYYY is the year, MM is the month (01 to 12),
DD is the day of the month (01 to 31), T is a constant character, hh is the hours since
midnight (00 to 23), mm is the minutes past the hour (00 to 59), and ss.s is the seconds
past the minute, with the “.s” being optional tenths of a second past the second.

This string can optionally be appended with Z to indicate UTC, or +/-hhmm to indicate
that the time is relative to a time zone. Appending neither indicates that the time zone is
unknown.

5.3.2.3.4 Fixed-length Array Form

| Field name | Field order | Size (bytes) | Datatype | Description                                                                                                                                                                        |
|------------|-------------|--------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Length     | 7           | 4            | UINT32   | A 32-bit unsigned integer giving the number of elements which must be included in the array contained by this property. All properties which have this form must contain an array. |

5.3.2.3.5 Regular Expression Form

| Field name | Field order | Size (bytes) | Datatype | Description                                                                                                                                                                                                                                                                     |
|------------|-------------|--------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RegEx      | 7           | Variable     | String   | A regular expression that must exactly generate the value of this property. A standardized syntax for regular expressions as they are used in MTP is available at: http://msdn2.microsoft.com/en-us/library/1400241x.aspx (page title: "Regular Expression Syntax (Scripting)") |

5.3.2.3.6 ByteArray Form

| Field name | Field order | Size (bytes) | Datatype | Description                                                                                                                                                                                                                                                                                      |
|------------|-------------|--------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MaxLength  | 7           | 4            | UINT32   | The maximum length of the ByteArray that may be contained by this property. The device shall accept any property values that have a NumElements value equal to or less than this field. Properties that have a ByteArray form must contain an AUINT8 datatype, which contains an array of bytes. |

5.3.2.3.7 LongString Form

| Field name | Field order | Size (bytes) | Datatype | Description                                                                                                                                                                                                                                                                                                                                                 |
|------------|-------------|--------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MaxLength  | 7           | 4            | UINT32   | The maximum length of the LongString that may be contained by this property. The device shall accept any property values that have a NumElements value equal to or less than this field. Properties that have a LongString form must contain an AUINT16 datatype, which contains characters encoded in 2-byte Unicode characters, as described in ISO10646. |

##### 5.3.2.4 Retrieving Object Properties

When information about an object is required, the properties can be retrieved one at a
time using the GetObjectPropValue operation, which returns the current value of an
object property. A complete description of the GetObjectPropValue operation can be
found in the appropriate appendix of this specification.

##### 5.3.2.5 Setting Object Properties

If a device supports the setting of object properties, which it indicates by supporting the
SetObjectPropValue operation, then properties can be identified as settable by setting
the Get/Set field in the ObjectPropDesc dataset. Those properties can be updated to any
value that satisfies the constraints defined in its ObjectPropDesc dataset.

The SetObjectPropValue operation sets the current value of the object property
indicated by parameter 2 for the object indicated by parameter 1 to the value indicated in
the data phase of the operation. The format of the property value object sent in the data
phase can be determined by the DatatypeCode field of the property's ObjectPropDesc
dataset. If the property is not settable, the response Access_Denied shall be returned. If
the value is not allowed by the device, Invalid_ObjectProp_Value shall be returned. If the
format or size of the property value is incorrect, Invalid_ObjectProp_Format shall be
returned.

The SetObjectPropValue operation is fully defined in the appropriate appendix of this
specification.

##### 5.3.2.6 Required Object Properties

Devices which implement Object Properties must implement as Object Properties the
properties which map to the required fields of the ObjectInfo dataset, as well as certain
properties which are required for effective functioning of the protocol. Required
properties for all object formats include:

- StorageID
- ObjectFormat
- ObjectCompressedSize
- Persistent Unique Object Identifier
- Name

Devices which support file systems through the use of associations must support the
following object properties:

- ParentObject

##### 5.3.2.7 Optimizing Object Properties

The development of object properties allows considerable improvements in functionality
over the static descriptive set of metadata exposed in the ObjectInfo dataset, however, it
comes at the cost of a dramatically increased number of queries to the device. This has
been mitigated in the Basic MTP specification by defining object-property retrieval
groups.

5.3.2.7.1 Object Property Groups

Many devices currently maintain an accelerator file or database containing a subset of
available metadata used by the device for its own UI. These metadata items, when
defined as object properties, are much more easily and efficiently retrieved than metadata
stored within the content on the device.

Devices are encouraged to identify the relative retrieval qualities of different properties
by assigning them a group value in the ObjectPropDesc dataset, and allowing them to be
retrieved based on that group value. Group codes shall be assigned in ascending order,
based upon the relative retrieval speed of the property.

The expected behavior of an initiator that is taking advantage of object property groups is
that it will retrieve properties in ascending order.

5.3.2.7.2 Special Values for Object Property Groups

Properties of essentially unbounded size shall be marked with a group code of
0xFFFFFFFF. This includes any property defined by a LongString or ByteArray form. It
is the responsibility of the device to accurately identify these groups.

##### 5.3.2.8 Representative Samples

It is often desirable to sample an object without acquiring the entire object, or to provide
a visual representation of the object. Examples of this include adding album art to an
album, representative audio clips to music files, or thumbnails to image files. These
representative samples are enabled by embedding them in a property value.

There are six properties related to representative samples. The first five properties are
descriptive of the representative sample, and cannot be set by the initiator. Rather, the
ObjectPropDesc fields of those properties are provided to define the allowable values of
the representative sample, and the values of the properties must be inferred from the
representative sample itself.

Example:
A portable media player needs to attach representative clips of audio files to full-length
songs in order to facilitate audio-only navigation of the contents of a device. To do so, the
media player would identify the format(s) in which the clips are desired in the
ObjectPropDesc dataset for the RepresentativeSampleFormat property on the audio clip
formats. Further, the range of desired durations for the sample is provided in the
RepresentativeSampleDuration ObjectPropDesc dataset, and the maximum file size of the
sample in the RepresentativeSampleSize ObjectPropDesc dataset. This information
would be sufficient for an initiator to send an appropriate clip to the device.

When an initiator is browsing that device later, it can identify the file size, duration, and
format of the representative sample by retrieving those properties. The values for those
properties must be populated by the responder automatically when the sample is sent to
(or created on) the device.

##### 5.3.2.9 Example of Object Properties in Use

The following table shows an overview of the object property exchange process,
presented as a step-through of the dialog between an MTP Initiator and Responder.

| Step | Initiator action                                     | Parameter1       | Parameter2       | Parameter3 | Responder action                                  |
|------|------------------------------------------------------|------------------|------------------|------------|---------------------------------------------------|
| 1    | GetDeviceInfo                                        | 0x00000000       | 0x00000000       | 0x00000000 | Send DeviceInfo dataset.                          |
| 2    | OpenSession                                          | SessionID        | 0x00000000       | 0x00000000 | Create ObjectHandles and StorageIDs if necessary. |
| 3    | GetObjectHandles                                     | 0xFFFFFFFF       | 0xFFFFFFFF       | 0x00000000 | Send ObjectHandle array.                          |
| 4    | GetObjectPropsSupported                              | ObjectFormatCode | 0x00000000       | 0x00000000 | Send ObjectPropCode array.                        |
| 5    | GetObjectPropDesc                                    | ObjectProp 1     | Object Format 1  | 0x00000000 | Send ObjectPropDesc dataset.                      |
| 6    | Repeat step 5 for each ObjectProperty                | ObjectProp n     | 0x00000000       | 0x00000000 | Send ObjectPropDesc dataset.                      |
| 7    | GetObjectPropValue                                   | ObjectHandle 1   | ObjectPropCode 1 | 0x00000000 | Send value of ObjectProp 1 for ObjectHandle 1.    |
| 8    | Repeat step 7 for each ObjectHandle x ObjectPropCode | ObjectHandle m   | ObjectPropCode n | 0x00000000 | Send value of ObjectProp n for ObjectHandle n.    |
| 9    | CloseSession                                         | 0x00000000       | 0x00000000       | 0x00000000 | Close session.                                    |

##### 5.3.2.10 Summary

Object properties provide a more extensible, more flexible, and higher performance
method for object metadata exchange and enumeration. They allow devices to describe
content separate from the binary data itself, which provides value to devices or
applications which do not understand the underlying format, and allows much faster and
more flexible content enumeration.

Object properties are an ongoing effort, and will continue to evolve for the lifespan of
MTP. Any changes to the default set of Object Properties in MTP are strictly additive
following version 1.0 of the MTP specification.

#### 5.3.3 Object References

MTP is a file system-independent protocol, which allows more flexibility in device
design. As a consequence of not being able to rely on a common and consistent
addressing mechanism, MTP lacks the ability to form complex linkages between objects
by embedding file names. An abstract referencing mechanism has been defined to allow
arbitrary object referencing.

##### 5.3.3.1 Object Reference Structure

The Object Reference Dataset consists of a single AUINT32, an array of 32-bit unsigned
integers, which contains the Object Handle of each object which is referenced by the
object to which the Object Reference Dataset in question is attached.

More specifically the dataset looks like:

| Field                     | Size (bytes) | Format       |
|---------------------------|--------------|--------------|
| NumElements               | 4            | UINT32       |
| ArrayEntry[0]             | 4            | ObjectHandle |
| ArrayEntry[1]             | 4            | ObjectHandle |
| …                         | …            | …            |
| ArrayEntry[NumElements-1] | 4            | ObjectHandle |

##### 5.3.3.2 Setting Object References

Devices that support object-reference retrieval and are write-capable (that is, they can
have objects sent to them as well as retrieved) shall also support the setting of object
references.

Object references are set by passing the whole array of references for that object in the
SetObjectReference operation, and is defined in the appropriate appendix of this
specification.

This operation replaces the object references on a device with the array of object handles
passed in the data phase. The object handles passed in the data phase must be maintained
indefinitely, and returned as valid ObjectHandles referencing the same object in later
sessions. If any of the object handles in the array passed in the data phase are invalid, the
responder shall fail the operation by returning a response code of Invalid_ObjectHandle.

An object handle may be present multiple times in a single array of references. An
example of this is a song that appears multiple times in a single playlist.

##### 5.3.3.3 Retrieving Object References

If a device indicates support for object references, it must allow those object references to
be retrieved by using the GetObjectReferences operation.

The GetObjectReferences operation returns an array of currently valid ObjectHandles.,
and is defined in the appropriate appendix of this specification.

##### 5.3.3.4 Identifying Support for Object References

For a device to be queried for object references, it must identify support for the
GetObjectReferences operation in the OperationsSupported field of its DeviceInfo
dataset.

Once support for that operation has been declared, the initiator may query for and expose
any and all object references.

##### 5.3.3.5 References are Unidirectional

References are unidirectional, and one cannot determine which objects reference a given
object without examining all the references on all the objects on the device. This does not
prevent the device from containing this information in its internal representation of
references.

##### 5.3.3.6 The Meaning of Object References Is Contextual

Object references do not include any inherent meaning. An object either references
another object, or it does not, and no additional information is contained within that
definition.

In practice, the meaning will be defined by context. For example, when a media object
references a DRM certificate, the DRM certification may be interpreted as being a license
defining the allowed usage of that media object. If a photograph references an audio clip,
that may indicate an audio annotation.

In many cases, the meaning will be unclear to the device, but the device shall maintain
consistent references between objects anyway, to preserve information between
connectivity sessions.

##### 5.3.3.7 Reference Maintenance

The object handles returned must be consistent between sessions. That is, the actual
values may change, but the objects they reference and the order in which those objects
are listed cannot change. It is the responsibility of the device to manage those references
between sessions such that they remain consistent, and to manage the removal of invalid
Object References (caused by an object being deleted from a device.)

If a referenced object is deleted on the device between sessions, the device must remove
all instances of that object in all other objects’ references. This removal may be done
lazily, when the references for an object are requested.

The unidirectional and context-dependent design of references is designed to facilitate
reference maintenance on the device.

#### 5.3.4 Basic Object Transfer

##### 5.3.4.1 Sent Object Placement

When a new object is sent using the SendObject operation, the Initiator may attempt to
specify the location where the new object will be placed on the device. It does this by
first calling the SendObjectInfo operation. The parameters of the SendObjectInfo
operation may contain the StorageID of the storage on the device on which the Initiator
wishes to place the object and the Object Handle of the desired parent of this object (that
is, the folder into which the object shall be placed).

Following the successful execution of the SendObjectInfo operation, the SendObject
operation shall be the next operation to be sent to the receiving device, which will initiate
the transfer of the data portion of the object. The intent is that the SendObjectInfo
operation will provide all the required information to determine whether the object will
be able to be successfully stored by the receiving device, so when the SendObject
operation begins, it will have a high probability of success, and the receiver will know in
advance how to handle the incoming object.

If the sending device provides a StorageID in the SendObjectInfo operation, the
receiving device shall determine whether the specified storage and parent object can be
used to locate the object on the device once it is received.

This requires that the receiving device test the following conditions in this order:

1. If the receiving device does not permit the target destination to be specified at all,
   it shall alert the sending device by sending a
   Specification_of_Destination_Unsupported failure response.
2. The StorageID passed shall refer to an actual storage currently present in the
   device.
3. The storage referred to shall have an access capability that allows write-access.
4. The storage referred to must have sufficient free space to contain the object to be
   sent. The size (in bytes) of the object to be sent is given in the ObjectInfo dataset
   passed in the data phase of the SendObjectInfo operation.
5. The parent object passed in the second parameter shall identify a valid object
   handle of an Association on the device.

6. Any other conditions required for the successful execution of the SendObject
   operation shall then be tested, and an appropriate response sent in the case of an
   expected failure.

The receiving device may choose to not support the specification of a target destination
on the device for a variety of reasons. When this is indicated by the appropriate failure
code, sent as a response to a SendObjectInfo operation that specifies a particular
StorageID/Parent Object, the Initiator shall then attempt the process again without
specifying a desired destination on the device, allowing the receiving device to specify
the location of the object.

