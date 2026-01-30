## Appendix F Responses

### F.1 Response Summary Table

| Name                                     | Datacode |
|------------------------------------------|----------|
| Undefined                                | 0x2000   |
| OK                                       | 0x2001   |
| General_Error                            | 0x2002   |
| Session_Not_Open                         | 0x2003   |
| Invalid_TransactionID                    | 0x2004   |
| Operation_Not_Supported                  | 0x2005   |
| Parameter_Not_Supported                  | 0x2006   |
| Incomplete_Transfer                      | 0x2007   |
| Invalid_StorageID                        | 0x2008   |
| Invalid_ObjectHandle                     | 0x2009   |
| DeviceProp_Not_Supported                 | 0x200A   |
| Invalid_ObjectFormatCode                 | 0x200B   |
| Store_Full                               | 0x200C   |
| Object_WriteProtected                    | 0x200D   |
| Store_Read-Only                          | 0x200E   |
| Access_Denied                            | 0x200F   |
| No_Thumbnail_Present                     | 0x2010   |
| SelfTest_Failed                          | 0x2011   |
| Partial_Deletion                         | 0x2012   |
| Store_Not_Available                      | 0x2013   |
| Specification_By_Format_Unsupported      | 0x2014   |
| No_Valid_ObjectInfo                      | 0x2015   |
| Invalid_Code_Format                      | 0x2016   |
| Unknown_Vendor_Code                      | 0x2017   |
| Capture_Already_Terminated               | 0x2018   |
| Device_Busy                              | 0x2019   |
| Invalid_ParentObject                     | 0x201A   |
| Invalid_DeviceProp_Format                | 0x201B   |
| Invalid_DeviceProp_Value                 | 0x201C   |
| Invalid_Parameter                        | 0x201D   |
| Session_Already_Open                     | 0x201E   |
| Transaction_Cancelled                    | 0x201F   |
| Specification_of_Destination_Unsupported | 0x2020   |
| Invalid_ObjectPropCode                   | 0xA801   |
| Invalid_ObjectProp_Format                | 0xA802   |
| Invalid_ObjectProp_Value                 | 0xA803   |
| Invalid_ObjectReference                  | 0xA804   |
| Group_Not_Supported                      | 0xA805   |
| Invalid_Dataset                          | 0xA806   |
| Specification_By_Group_Unsupported       | 0xA807   |
| Specification_By_Depth_Unsupported       | 0xA808   |
| Object_Too_Large                         | 0xA809   |
| ObjectProp_Not_Supported                 | 0xA80A   |

### F.2 Response Descriptions

#### F.2.1 Undefined

Response Code: 0x2000

This response code is not used.

#### F.2.2 OK

Response Code: 0x2001

Operation has completed successfully.

#### F.2.3 General_Error

Response Code: 0x2002

This operation did not complete, and the reason for the failure is not known.

#### F.2.4 Session_Not_Open

Response Code: 0x2003

Indicates that the session handle identified by the operation dataset for this operation is
not a currently open session.

#### F.2.5 Invalid_TransactionID

Response Code: 0x2004

Indicates that the TransactionID of this operation does not identify a valid transaction.

#### F.2.6 Operation_Not_Supported

Response Code: 0x2005

This response indicates that an Operation has been called with what appears to be a valid
code, but the responder does not support the operation identified by that code. The
initiator should only invoke operations contained in the responder’s DeviceInfo dataset,
so this response should not normally be returned.

#### F.2.7 Parameter_Not_Supported

Response Code: 0x2006

Indicates that a parameter of an operation contains a non-zero value, but is not supported.
This response is different from Invalid_Parameter.

#### F.2.8 Incomplete_Transfer

Response Code: 0x2007

This response shall be sent when a transfer did not complete successfully, and indicates
that data transferred is to be discarded. This response shall not be sent if the transfer was
cancelled by the Initiator.

#### F.2.9 Invalid_StorageID

Response Code: 0x2008

Indicates that one or more StorageIDs sent as parameters of an operation do not refer to
actual StorageIDs on the device.

#### F.2.10 Invalid_ObjectHandle

Response Code: 0x2009

Indicates that one or more ObjectHandles sent as parameters of an operation do not refer
to actual Objects on the device. The list of valid ObjectHandles should be requested
again, along with any appropriate ObjectInfo datasets.

#### F.2.11 DeviceProp_Not_Supported

Response Code: 0x200A

Indicates that a DevicePropCode sent as a parameter of an operation appears to be a valid
code, but is not supported by the device. The initiator should only attempt to work with
Device Properties identified in the DevicePropertiesSupported field of the DeviceInfo
Dataset, so this response should not normally be returned.

#### F.2.12 Invalid_ObjectFormatCode

Response Code: 0x200B

Indicates that the device does not support an ObjectFormatCode supplied in the given
context.

#### F.2.13 Store_Full

Response Code: 0x200C

Indicates that a store identified in this operation is full, and this is preventing the
successful completion of that operation.

#### F.2.14 Object_WriteProtected

Response Code: 0x200D

Indicates that an object referred to by the operation is write-protected.

#### F.2.15 Store_Read-Only

Response Code: 0x200E

Indicates that a store referred to by the operation is read-only.

#### F.2.16 Access_Denied

Response Code: 0x200F

This response shall be sent when access to data required by the operation is denied. This
shall not be used when the device is busy, but to indicate that if the current state of the
device does not change access will continue to be denied.

#### F.2.17 No_Thumbnail_Present

Response Code: 0x2010

Indicates that a data object exists with the specified ObjectHandle, but a thumbnail
cannot be provided for that object.

#### F.2.18 SelfTest_Failed

Response Code: 0x2011

This shall be sent when the device fails a device-specific self test.

#### F.2.19 Partial_Deletion

Response Code: 0x2012

Indicates that only a subset of the objects indicated for deletion were actually deleted.
This could be caused by some of those objects being write-protected or on read-only
stores.

#### F.2.20 Store_Not_Available

Response Code: 0x2013

Indicates that the store indicated (or the store that contains the indicated object) is not
physically available. This can be caused by media ejection. This response shall not be
used to indicate that the store is busy.

#### F.2.21 Specification_By_Format_Unsupported

Response Code: 0x2014

This response shall be sent when an operation attempts to specify an action only on
objects which have a particular format code, but the responder does not support that
capability. The operation should be attempted again without specifying by format. When
this response is sent, it shall indicate that any future attempts to call the same operation
specifying by format will also result in this response.

#### F.2.22 No_Valid_ObjectInfo

Response Code: 0x2015

This shall be sent when a SendObject operation has been called without the initiator
having previously sent a corresponding SendObjectInfo successfully. The initiator must
successfully complete a SendObjectInfo operation before attempting another SendObject
operation.

#### F.2.23 Invalid_Code_Format

Response Code: 0x2016

Indicates that a datacode used in this operation does not have the correct format, and is
therefore known to be invalid. This response shall be used when the most-significant bits
of a datacode does not have the format required for that type of code, and not when the
data appears to have the correct type but is invalid for other reasons.

#### F.2.24 Unknown_Vendor_Code

Response Code: 0x2017

Indicates that the indicated data code has the correct format, but is in a vendor extension
range not recognized by the device. This response will typically not occur, because the
Initiator can identify the supported vendor extensions by examination of the DeviceInfo
dataset.

#### F.2.25 Capture_Already_Terminated

Response Code: 0x2018

This shall be sent when an operation attempts to terminate a capture session, but that the
capture session has already terminated. This response is only used for the
TerminateOpenCapture operation, which is only used to terminate open-ended captures.

#### F.2.26 Device_Busy

Response Code: 0x2019

This response shall be sent when the device is not currently able to process a request
because it, or the specified store, is busy. This response implies that the operation may be
successful at a later time, but is not possible right now. This response shall not be used to
indicate that a store is physically unavailable.

#### F.2.27 Invalid_ParentObject

Response Code: 0x201A

This response shall be sent when an indicated object is not of type Association, but is
required to be of type Association in the context in which it is used, and therefore is not a
valid ParentObject. This response is not intended to be used for specified ObjectHandles
that do not refer to valid objects, but only for ObjectHandles which refer to actual objects
which are not of type Association.

#### F.2.28 Invalid_DeviceProp_Format

Response Code: 0x201B

This response shall be sent when an attempt is made to set a DeviceProperty, but the
DevicePropDesc dataset sent is not the correct size or format.

#### F.2.29 Invalid_DeviceProp_Value

Response Code: 0x201C

This response shall be sent when an attempt is made to set a DeviceProperty to a
particular value, but that value is not allowed by the device.

#### F.2.30 Invalid_Parameter

Response Code: 0x201D

This response indicates that a parameter of the operation is not a valid value. This
response is different from Parameter_Not_Supported, which indicates that no value was
expected in this parameter.

#### F.2.31 Session_Already_Open

Response Code: 0x201E

This response may be sent in resonse to an OpenSession operation. If multiple sessions
are supported by the device, this response indicates that a session with the specified
SessionID is already open. If multiple sessions are not supported by the device, this
response indicates that a session is open and must be closed before another session can be
opened.

#### F.2.32 Transaction_Cancelled

Response Code: 0x201F

This response indicates that the operation was interrupted due to manual cancellation by
the initiator.

#### F.2.33 Specification_of_Destination_Unsupported

Response Code: 0x2020

This response may be sent as a response to a SendObjectInfo operation to indicate that
the responder does not support the specification of destination. This response implies that
any future attempts to specify the object destination will also fail with the same response.

#### F.2.34 Invalid_ObjectPropCode

Response Code: 0xA801

Indicates that the device does not support the sent Object Property Code in this context.

#### F.2.35 Invalid_ObjectProp_Format

Response Code: 0xA802

Indicates that an object property sent to the device is in an unsupported size or type.

#### F.2.36 Invalid_ObjectProp_Value

Response Code: 0xA803

Indicates that an object property sent to the device is the correct type, but contains a value
which is not supported. The supported values shall be identified by the ObjectPropDesc
dataset.

#### F.2.37 Invalid_ObjectReference

Response Code: 0xA804

Indicates that a sent Object Reference is invalid. Either the reference contains an object
handle not present on the device, or the reference attempting to be set is unsupported in
context.

#### F.2.38 Invalid_Dataset

Response Code: 0xA806

Indicates that the dataset sent in the data phase of this operation is invalid. While the PTP
specification (refer to “USB Still Image Capture Device Definition – July 2000” and the
specifications referred to by that document) refers to “Invalid_Dataset”, at no time does it
specify a response code. Thus the definition of Invalid_Dataset in this MTP specification
does not conflict with the PTP specification.

#### F.2.39 Specification_By_Group_Unsupported

Response Code: 0xA807

May be used as the response to indicate that the responder does not support the
specification of groups by the initiator. This response implies that the initiator should not
attempt to specify the group code in any future operations, as they will also fail with the
same response.

#### F.2.40 Specification_By_Depth_Unsupported

Response Code: 0xA808

May be used as the response to indicate that the responder does not support the
specification of depth by the initiator. This response implies that the initiator should not
attempt to specify depth in any future call of the operation which resulted in this
response, as they will also fail with the same response.

#### F.2.41 Object_Too_Large

Response Code: 0xA809

Indicates that the object desired to be sent cannot be stored in the filesystem of the
device. This should not be used when there is insufficient space on the storage. For
example, a FAT32 system can only support a 4GB object. A 6GB object would receive
Object_Too_Large.

#### F.2.42 ObjectProp_Not_Supported

Response Code: 0xA80A

Indicates that an ObjectPropCode sent as a parameter of an operation appears to be a
valid code, but is not supported by the device. The initiator should only attempt to work
with Object Properties identified as supported by the responder, so this response should
not normally be returned.

#### F.2.43 Group_Not_Supported

Response Code: 0xA805

Indicates that an Object Property group code sent as a parameter of an operation appears
to be a valid code, but is not supported by the device. The initiator should only attempt to
work with Object Property group codes identified as supported by the responder, so this
response should not normally be returned.

