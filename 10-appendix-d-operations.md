## Appendix D Operations

### D.1 Operation Summary Table

| Operation Name          | Operation Code |
|-------------------------|----------------|
| GetDeviceInfo           | 0x1001         |
| OpenSession             | 0x1002         |
| CloseSession            | 0x1003         |
| GetStorageIDs           | 0x1004         |
| GetStorageInfo          | 0x1005         |
| GetNumObjects           | 0x1006         |
| GetObjectHandles        | 0x1007         |
| GetObjectInfo           | 0x1008         |
| GetObject               | 0x1009         |
| GetThumb                | 0x100A         |
| DeleteObject            | 0x100B         |
| SendObjectInfo          | 0x100C         |
| SendObject              | 0x100D         |
| InitiateCapture         | 0x100E         |
| FormatStore             | 0x100F         |
| ResetDevice             | 0x1010         |
| SelfTest                | 0x1011         |
| SetObjectProtection     | 0x1012         |
| PowerDown               | 0x1013         |
| GetDevicePropDesc       | 0x1014         |
| GetDevicePropValue      | 0x1015         |
| SetDevicePropValue      | 0x1016         |
| ResetDevicePropValue    | 0x1017         |
| TerminateOpenCapture    | 0x1018         |
| MoveObject              | 0x1019         |
| CopyObject              | 0x101A         |
| GetPartialObject        | 0x101B         |
| InitiateOpenCapture     | 0x101C         |
| GetObjectPropsSupported | 0x9801         |
| GetObjectPropDesc       | 0x9802         |
| GetObjectPropValue      | 0x9803         |
| SetObjectPropValue      | 0x9804         |
| GetObjectReferences     | 0x9810         |
| SetObjectReferences     | 0x9811         |
| Skip                    | 0x9820         |

### D.2 Operation Descriptions

#### D.2.1 GetDeviceInfo

This operation returns the DeviceInfo dataset, as defined in section 5.1.1 "DeviceInfo
Dataset Description." This dataset provides identifying information about the device,
such as model and serial number, as well as describing the capabilities of the device.
This operation is commonly the first operation called by an initiator upon connecting to a
responder for the first time.

| Operation Code        | 0x1001                      |
|-----------------------|-----------------------------|
| Operation Parameter 1 | None                        |
| Operation Parameter 2 | None                        |
| Operation Parameter 3 | None                        |
| Operation Parameter 4 | None                        |
| Operation Parameter 5 | None                        |
| Data                  | DeviceInfo dataset          |
| Data Direction        | R->I                        |
| ResponseCode Options  | OK, Parameter_Not_Supported |
| Response Parameter 1  | None                        |
| Response Parameter 2  | None                        |
| Response Parameter 3  | None                        |
| Response Parameter 4  | None                        |
| Response Parameter 5  | None                        |

This operation may be called outside of a session. When used outside a session, both the
SessionID and TransactionID in the OperationRequest dataset must be 0x00000000.

#### D.2.2 OpenSession

This operation creates a new session for communication between the Initiator and
Responder. Sessions are described in more detail in section 4.4 “Sessions.” All
operations require a session to exist, unless otherwise specified.

| Operation Code        | 0x1002                                                                            |
|-----------------------|-----------------------------------------------------------------------------------|
| Operation Parameter 1 | SessionID                                                                         |
| Operation Parameter 2 | None                                                                              |
| Operation Parameter 3 | None                                                                              |
| Operation Parameter 4 | None                                                                              |
| Operation Parameter 5 | None                                                                              |
| Data                  | None                                                                              |
| Data Direction        | N/A                                                                               |
| ResponseCode Options  | OK, Parameter_Not_Supported, Invalid_Parameter, Session_Already_Open, Device_Busy |
| Response Parameter 1  | None                                                                              |
| Response Parameter 2  | None                                                                              |
| Response Parameter 3  | None                                                                              |
| Response Parameter 4  | None                                                                              |
| Response Parameter 5  | None                                                                              |

If this operation is called and an active session has already been opened, a response of
Session_Already_Open shall be returned, and the first response parameter shall contain
the SessionID of the open session. This response shall also be returned if the session ID
passed in the first parameter is already in use in a different session. If the SessionID
passed in the first parameter is equal to 0x00000000, the operation shall fail and shall
return a response of Invalid_Parameter.

#### D.2.3 CloseSession

This operation closes an active session. All stateful information pertaining to the session
being closed shall be discarded.

| Operation Code        | 0x1003                                                               |
|-----------------------|----------------------------------------------------------------------|
| Operation Parameter 1 | None                                                                 |
| Operation Parameter 2 | None                                                                 |
| Operation Parameter 3 | None                                                                 |
| Operation Parameter 4 | None                                                                 |
| Operation Parameter 5 | None                                                                 |
| Data                  | None                                                                 |
| Data Direction        | N/A                                                                  |
| ResponseCode Options  | OK, Session_Not_Open, Invalid_TransactionID, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                 |
| Response Parameter 2  | None                                                                 |
| Response Parameter 3  | None                                                                 |
| Response Parameter 4  | None                                                                 |
| Response Parameter 5  | None                                                                 |

#### D.2.4 GetStorageIDs

This operation returns a list of StorageIDs of storages on this device. StorageIDs are
defined in more detail in section 5.2.1 “Storage IDs”.

| Operation Code        | 0x1004                                                                                        |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Operation Parameter 1 | None                                                                                          |
| Operation Parameter 2 | None                                                                                          |
| Operation Parameter 3 | None                                                                                          |
| Operation Parameter 4 | None                                                                                          |
| Operation Parameter 5 | None                                                                                          |
| Data                  | StorageID array                                                                               |
| Data Direction        | R->I                                                                                          |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                          |
| Response Parameter 2  | None                                                                                          |
| Response Parameter 3  | None                                                                                          |
| Response Parameter 4  | None                                                                                          |
| Response Parameter 5  | None                                                                                          |

Removable storages with no inserted media shall be returned in the dataset returned by
this operation as well, though they would contain a value of 0x0000 in the lower 16 bits
indicating that they are not present.

#### D.2.5 GetStorageInfo

This operation returns the StorageInfo dataset for the storage identified by the StorageID
in the first parameter. The StorageInfo dataset is defined in section 5.2.2, “Storage Info
Dataset”.

| Operation Code        | 0x1005                                                                                                                      |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | StorageID                                                                                                                   |
| Operation Parameter 2 | None                                                                                                                        |
| Operation Parameter 3 | None                                                                                                                        |
| Operation Parameter 4 | None                                                                                                                        |
| Operation Parameter 5 | None                                                                                                                        |
| Data                  | StorageInfo dataset                                                                                                         |
| Data Direction        | R->I                                                                                                                        |
| ResponseCode Options  | OK, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_StorageID, Store_Not_Available, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                        |
| Response Parameter 2  | None                                                                                                                        |
| Response Parameter 3  | None                                                                                                                        |
| Response Parameter 4  | None                                                                                                                        |
| Response Parameter 5  | None                                                                                                                        |

#### D.2.6 GetNumObjects

This operation returns the number of objects on the device, or the subset defined by the
first three parameters.

| Operation Code        | 0x1006                                                                                                                                                                                                                                                         |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | StorageID                                                                                                                                                                                                                                                      |
| Operation Parameter 2 | [ObjectFormatCode]                                                                                                                                                                                                                                             |
| Operation Parameter 3 | [ObjectHandle of Association for which number of children is needed]                                                                                                                                                                                           |
| Operation Parameter 4 | None                                                                                                                                                                                                                                                           |
| Operation Parameter 5 | None                                                                                                                                                                                                                                                           |
| Data                  | None                                                                                                                                                                                                                                                           |
| Data Direction        | N/A                                                                                                                                                                                                                                                            |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_StorageID, Store_Not_Available, Specification_By_Format_Unsupported, Invalid_Code_Format, Parameter_Not_Supported, Invalid_ParentObject, Invalid_ObjectHandle, Invalid_Parameter |
| Response Parameter 1  | NumObjects                                                                                                                                                                                                                                                     |
| Response Parameter 2  | None                                                                                                                                                                                                                                                           |
| Response Parameter 3  | None                                                                                                                                                                                                                                                           |
| Response Parameter 4  | None                                                                                                                                                                                                                                                           |
| Response Parameter 5  | None                                                                                                                                                                                                                                                           |

The first parameter contains the StorageID of the storage for which the number of objects
is desired. A value of 0xFFFFFFFF may be used to indicate that an aggregated total
across all storages shall be returned. If a storage is specified and the storage is
unavailable, this operation shall return Store_Not_Available.

The second parameter is optional, and contains an Object Format datacode. Object
Formats are described in section 4, “Object Formats”. If the second parameter contains a
non-0x00000000 value, it specifies that a count of objects of a certain object format is
desired. If the parameter is not used, it shall contain a value of 0x00000000 and objects
shall be counted regardless of their object format. If this parameter is not supported, the
responder shall return a response code of Specification_By_Format_Unsupported.

The third parameter may be used to restrict the count of objects returned by this operation
to objects directly contained in a particular folder (Association). If this parameter
contains a non-0x00000000 value, the responder shall return a count of objects which
have as their ParentObject the folder (Association) identified by this parameter. If the
number of objects contained in the root of a storage is desired, a value of 0xFFFFFFFF
may be passed in this operation, indicating that only those objects with no ParentObject
(i.e., objects in the root of the storage) shall be returned. If the first parameter indicates
that all storages are included in this query, then a value of 0xFFFFFFFF shall return a
count of all objects at the root level of any storage. If this parameter is unused, it shall
contain a value of 0x00000000.

If the third parameter is unsupported and a non-0x00000000 value is sent in this
operation, a response of Parameter_Unsupported shall be returned. If the use of the third
parameter is supported, but the value contained does not reference an actual object on the
device, a response of Invalid_ObjectHandle shall be returned. If the use of the third
parameter is supported and it contains a valid Object Handle, but the object referenced is
not of type Association, then a response of Invalid_ParentObject shall be returned.

#### D.2.7 GetObjectHandles

This operation returns an array of Object Handles referencing the contents of the device.

| Operation Code        | 0x1007                                                                                                                                                                                                                                                                                                         |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | StorageID                                                                                                                                                                                                                                                                                                      |
| Operation Parameter 2 | [ObjectFormatCode]                                                                                                                                                                                                                                                                                             |
| Operation Parameter 3 | [ObjectHandle of Association or hierarchical folder for which a list of children is needed]                                                                                                                                                                                                                    |
| Operation Parameter 4 | None                                                                                                                                                                                                                                                                                                           |
| Operation Parameter 5 | None                                                                                                                                                                                                                                                                                                           |
| Data                  | ObjectHandle array                                                                                                                                                                                                                                                                                             |
| Data Direction        | R->I                                                                                                                                                                                                                                                                                                           |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_StorageID, Store_Not_Available, Invalid_ObjectFormatCode, Specification_By_Format_Unsupported, Invalid_Code_Format, Invalid_ObjectHandle, Invalid_Parameter, Parameter_Not_Supported, Invalid_ParentObject, Invalid_ObjectHandle |
| Response Parameter 1  | None                                                                                                                                                                                                                                                                                                           |
| Response Parameter 2  | None                                                                                                                                                                                                                                                                                                           |
| Response Parameter 3  | None                                                                                                                                                                                                                                                                                                           |
| Response Parameter 4  | None                                                                                                                                                                                                                                                                                                           |
| Response Parameter 5  | None                                                                                                                                                                                                                                                                                                           |

The first parameter contains the StorageID of the storage for which the list of Object
Handles is desired. A value of 0xFFFFFFFF may be used to indicate that a list of Object
Handles of all objects on all storages shall be returned. If a storage is specified and the
storage is unavailable, this operation shall return Store_Not_Available.

The second parameter is optional, and contains an Object Format datacode. Object
Formats are described in Appendix A – Object Formats. If the second parameter contains
a non-0x00000000 value, it specifies that a list of object handles referencing objects of a
certain object format is desired. If the parameter is not used, it shall contain a value of
0x00000000 and objects shall be included in the response dataset regardless of their
object format. If use of this parameter is not supported, and a non-zero value is passed,
the Responder shall return a response code of Specification_By_Format_Unsupported.

The third parameter may be used to restrict the list of objects returned by this operation to
objects directly contained in a particular folder (Association). If this parameter contains a
non-0x00000000 value, the responder shall return a list of objects which have as their
ParentObject the folder (Association) identified by this parameter. If the number of
objects contained in the root of a storage is desired, a value of 0xFFFFFFFF may be
passed in this operation, indicating that only those objects with no ParentObject are to be
returned. If the first parameter indicates that all storages are included in this query, then a
value of 0xFFFFFFFF shall return a list of all objects at the root level of all storages. If
this parameter is unused, it shall contain a value of 0x00000000.

If the third parameter is unsupported and a non-0x00000000 value is sent in this
operation, a response of Parameter_Unsupported shall be returned. If the use of the third
parameter is supported, but the value contained does not reference an actual object on the
device, a response of Invalid_ObjectHandle shall be returned. If the use of the third
parameter is supported and it contains a valid Object Handle, but the object referenced is
not of type Association, then a response of Invalid_ParentObject shall be returned.

#### D.2.8 GetObjectInfo

This operation returns the ObjectInfo dataset for the object identified by the Object
Handle in the first parameter. The ObjectInfo dataset is defined in section 5.3.1, “Object
Info Dataset”.

| Operation Code        | 0x1008                                                                                                                                   |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                             |
| Operation Parameter 2 | None                                                                                                                                     |
| Operation Parameter 3 | None                                                                                                                                     |
| Operation Parameter 4 | None                                                                                                                                     |
| Operation Parameter 5 | None                                                                                                                                     |
| Data                  | ObjectInfo dataset                                                                                                                       |
| Data Direction        | R->I                                                                                                                                     |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_ObjectHandle, Store_Not_Available, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                                     |
| Response Parameter 2  | None                                                                                                                                     |
| Response Parameter 3  | None                                                                                                                                     |
| Response Parameter 4  | None                                                                                                                                     |
| Response Parameter 5  | None                                                                                                                                     |

#### D.2.9 GetObject

This object retrieves the binary data component of an object from the device. This will
generally be preceded by either a GetObjectInfo operation or GetObjectPropList
operation(s) to first identify the object’s type and descriptive information, but this is not
required.

| Operation Code        | 0x1009                                                                                                                                                                                          |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                    |
| Operation Parameter 2 | None                                                                                                                                                                                            |
| Operation Parameter 3 | None                                                                                                                                                                                            |
| Operation Parameter 4 | None                                                                                                                                                                                            |
| Operation Parameter 5 | None                                                                                                                                                                                            |
| Data                  | Object Binary Data                                                                                                                                                                              |
| Data Direction        | R->I                                                                                                                                                                                            |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_ObjectHandle, Invalid_Parameter, Store_Not_Available, Incomplete_Transfer, Access_Denied, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                                                                                            |
| Response Parameter 2  | None                                                                                                                                                                                            |
| Response Parameter 3  | None                                                                                                                                                                                            |
| Response Parameter 4  | None                                                                                                                                                                                            |
| Response Parameter 5  | None                                                                                                                                                                                            |

Objects with no data component (having a binary size 0), such as associations or abstract
playlists cannot be retrieved with this operation.

If the object handle in the first parameter refers to a folder (Association) object, the
Responder shall respond with an Invalid_ObjectHandle response. If the object handle in
the first parameter does not refer to an object on the device, then the responder shall
respond with an Invalid_ObjectHandle response. If the first parameter references an
object which is not of type Association, but which has a size of 0, then this operation
shall succeed, and an object of size 0 shall be returned.

#### D.2.10 GetThumb

This operation retrieves a thumbnail for an image object on the responder.

The Representative Sample object property may be used as a more flexible alternative for
devices which support object properties, but this operation must be supported for PTP-
compatibiliy.

| Operation Code        | 0x100A                                                                                                                                                                                    |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                              |
| Operation Parameter 2 | None                                                                                                                                                                                      |
| Operation Parameter 3 | None                                                                                                                                                                                      |
| Operation Parameter 4 | None                                                                                                                                                                                      |
| Operation Parameter 5 | None                                                                                                                                                                                      |
| Data                  | ThumbnailData                                                                                                                                                                             |
| Data Direction        | R->I                                                                                                                                                                                      |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_ObjectHandle, Thumbnail_Not_Present, Invalid_ObjectFormatCode, Store_Not_Available, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                                                                                      |
| Response Parameter 2  | None                                                                                                                                                                                      |
| Response Parameter 3  | None                                                                                                                                                                                      |
| Response Parameter 4  | None                                                                                                                                                                                      |
| Response Parameter 5  | None                                                                                                                                                                                      |

#### D.2.11 DeleteObject

This operation deletes a data object from the responder.

| Operation Code        | 0x100B                                                                                                                                                                                                                                                                                   |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                                                                                                             |
| Operation Parameter 2 | [ObjectFormatCode]                                                                                                                                                                                                                                                                       |
| Operation Parameter 3 | None                                                                                                                                                                                                                                                                                     |
| Operation Parameter 4 | None                                                                                                                                                                                                                                                                                     |
| Operation Parameter 5 | None                                                                                                                                                                                                                                                                                     |
| Data                  | None                                                                                                                                                                                                                                                                                     |
| Data Direction        | N/A                                                                                                                                                                                                                                                                                      |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_ObjectHandle, Object_WriteProtected, Store_Read_Only, Partial_Deletion, Store_Not_Available, Specification_By_Format_Unsupported, Invalid_Code_Format, Device_Busy, Parameter_Not_Supported, Access_Denied |
| Response Parameter 1  | None                                                                                                                                                                                                                                                                                     |
| Response Parameter 2  | None                                                                                                                                                                                                                                                                                     |
| Response Parameter 3  | None                                                                                                                                                                                                                                                                                     |
| Response Parameter 4  | None                                                                                                                                                                                                                                                                                     |
| Response Parameter 5  | None                                                                                                                                                                                                                                                                                     |

The first parameter contains an object handle which references the object to be deleted.
Write-protected objects cannot be deleted by this operation. If the first parameter
contains a value of 0xFFFFFFFF, then all objects on the device able to be deleted shall be
deleted. If a value of 0xFFFFFFFF is passed in the first parameter, and some subset of
objects are not deleted (but at least one object is deleted), a response of Partial_Deletion
shall be returned. If the object handle in the first parameter does not reference a valid
object on the device, the responder shall return an Invalid_ObjectHandle response. If the
first parameter identifies an object on the responder, but the object is on a storage which
is read-only and does not allow deletion, then the response Store_Read_Only shall be
returned.

If the first parameter contains an object handle for a folder object (Association), then all
objects in that association shall be deleted. Any folder objects contained in that folder
shall also be deleted. If the first parameter contains a folder (Association) object, and
that folder contains an object which cannot be deleted, the parent folder of the object
which cannot be deleted shall also not be deleted.

The second parameter is optional, and contains an Object Format datacode. Object
Formats are described in section 4, “Object Formats”. If the second parameter contains a
non-0x00000000 value and the first parameter contains a value of 0xFFFFFFFF, it
specifies that all objects on the device of the object format specified in this parameter
shall be deleted. If the responder does not support this parameter and it contains a non-
0x00000000 value, it shall return a response code of
Specification_By_Format_Unsupported.

If all objects identified by the first two parameters are protected and cannot be deleted (as
identified by the ProtectionStatus field of the object’s ObjectInfo dataset or the
ProtectionStatus object poperty), a response code of Object_WriteProtected shall be
returned. If some, but not all, objects are successfully deleted, then a response code of
Partial_Deletion must always be returned.

#### D.2.12 SendObjectInfo

This is the first operation sent when an initiator wishes to send a new object to a
responder. When objects are sent to a responder, the ObjectInfo dataset precedes the data
component to give the responder context for the transfer, allowing resources to be
allocated, and verifying to the initiator that the object should be able to be sent
successfully. This operation is usually followed by a SendObject operation, as described
in Appendix D.2.13 SendObject”. A successful completion of this operation indicates
that the responder is ready and able to receive the object described in the ObjectInfo
dataset.

| Operation Code        | 0x100C                                                                                                                                                                                                                                                                                                         |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | [Destination StorageID on responder]                                                                                                                                                                                                                                                                           |
| Operation Parameter 2 | [Parent ObjectHandle on responder where object shall be placed]                                                                                                                                                                                                                                                |
| Operation Parameter 3 | None                                                                                                                                                                                                                                                                                                           |
| Operation Parameter 4 | None                                                                                                                                                                                                                                                                                                           |
| Operation Parameter 5 | None                                                                                                                                                                                                                                                                                                           |
| Data                  | ObjectInfo dataset                                                                                                                                                                                                                                                                                             |
| Data Direction        | I->R                                                                                                                                                                                                                                                                                                           |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_StorageID, Store_Read_Only, Object_Too_Large, Store_Full, Invalid_ObjectFormatCode, Store_Not_Available, Parameter_Not_Supported, Invalid_ParentObject, Invalid_Dataset, Specification_Of_Destination_Unsupported |
| Response Parameter 1  | Responder StorageID in which the object will be stored                                                                                                                                                                                                                                                         |
| Response Parameter 2  | Responder parent ObjectHandle in which the object will be stored                                                                                                                                                                                                                                               |
| Response Parameter 3  | Responder's reserved ObjectHandle for the incoming object                                                                                                                                                                                                                                                      |
| Response Parameter 4  | None                                                                                                                                                                                                                                                                                                           |
| Response Parameter 5  | None                                                                                                                                                                                                                                                                                                           |

The first parameter is optional, and indicates the store on the responder on which the
following object shall be stored. If this parameter is included and the responder cannot
place the described object in that store, this operation shall fail with a response code of
Store_Not_Available, Store_Read_Only or Store_Full. If the responder does not support
this parameter, a response code of Specification_Of_Destination_Unsupported shall be
returned. If this parameter contains a value of 0x00000000, the responder may choose on
which store it will save the object.

The second parameter is optional, and indicates the folder (Association) into which this
object shall be placed. If the second parameter contains a non-0x00000000 value, the
storage of that parent object must also be specified in the first parameter. If the responder
does not support the use of this parameter, it shall fail this operation with a response code
of Specification_Of_Destination_Unsupported. If an Initiator receives a response of
Specification_Of_Destination_Unsupported when specifying both the first and second
parameter, it may try again while specifying only the first parameter if desired. If the
object handle included in the second parameter does not reference a valid object on the
device, a response of Invalid_ObjectHandle shall be returned. If the object handle
included in the second parameter does not reference a folder (Association) object, the
responder shall return a value of Invalid_ParentObject.

If the responder cannot accept an object based upon information in the SendObjectInfo
dataset (where there is not already an appropriate response), such as an invalid filename,
the error code Invalid_Dataset shall be used.

If the initiator wishes to place an object in the root of a given storage, it shall indicate the
desired storage in the first parameter and include a value of 0xFFFFFFFF in the second
parameter.

Upon the successful completion of this operation, the responder shall be prepared to
receive a SendObject operation to receive the binary data for the specified object. If the
ObjectInfo dataset sent in the data phase of this operation indicates that the size in bytes
of the object to be sent is greater than 0, then the next operation called in the same
session is intended to be a SendObject operation. If the next operation sent in the same
session is not a SendObject operation, the responder shall not retain the sent or
ObjectInfo dataset. If the following SendObject operation does not successfully execute,
the ObjectInfo dataset passed in this operation shall be retained until the successful
completion of a SendObject operation.

An object handle issued during a successful SendObjectInfo or SendObjectPropList
operation should be reserved for the duration of the MTP session, even if there is no
successful SendObject operation for that handle.

If the ObjectInfo dataset sent in the data phase of this operation indicates that the object
to be sent has a size of 0, then a response of OK indicates that the object has been sent
successfully, and it is not required that this operation be followed by a SendObject
operation. However, the responder shall not fail if a SendObject operation follows
containing an object of size 0.

Object properties that are get-only (0x00 GET) shall accept values during object creation
from the SendObjectInfo operation.

#### D.2.13 SendObject

This operation is used to send the binary content of an object to the device, and follows a
successful SendObjectInfo operation (as described in Appendix D.2.12 SendObjectInfo).
The data object sent in this operation must correspond to the ObjectInfo dataset
description sent in the preceeding SendObjectInfo.

| Operation Code        | 0x100D                                                                                                                                                                                                                                              |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | None                                                                                                                                                                                                                                                |
| Operation Parameter 2 | None                                                                                                                                                                                                                                                |
| Operation Parameter 3 | None                                                                                                                                                                                                                                                |
| Operation Parameter 4 | None                                                                                                                                                                                                                                                |
| Operation Parameter 5 | None                                                                                                                                                                                                                                                |
| Data                  | Object Binary Data                                                                                                                                                                                                                                  |
| Data Direction        | I->R                                                                                                                                                                                                                                                |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_StorageID, Store_Read_Only, Object_Too_Large, Store_Full, Invalid_ObjectFormatCode, Store_Not_Available, Parameter_Not_Supported, Invalid_ParentObject |
| Response Parameter 1  | None                                                                                                                                                                                                                                                |
| Response Parameter 2  | None                                                                                                                                                                                                                                                |
| Response Parameter 3  | None                                                                                                                                                                                                                                                |
| Response Parameter 4  | None                                                                                                                                                                                                                                                |
| Response Parameter 5  | None                                                                                                                                                                                                                                                |

If this operation does not follow a successful SendObjectInfo operation in the same
session, a response of No_Valid_ObjectInfo shall be returned. If the target destination
does not contain sufficient free space for the object sent in the data phase of this
operation, a response of Store_Full shall be returned. If the object sent in the data phase
of this operation is larger than the size indicated in the ObjectInfo dataset sent in the
SendObjectInfo which precedes this operation, this operation shall fail and a response
code of Store_Full shall be returned.

If this operation completes successfully, any stored ObjectInfo dataset shall be discarded.
If this operation fails for any reason, the ObjectInfo dataset shall be retained and the
responder shall remain ready to receive the object.

If for any reason the data transfer fails during data transfer, the responder shall fail this
operation with a response code of Incomplete_Transfer.

#### D.2.14 InitiateCapture

This operation indicates to the responder that it is to produce a new data object according
to its current device properties using an object capture mechanism enabled by the device.

| Operation Code        | 0x100E                                                                                                                                                                                                                                            |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | [StorageID]                                                                                                                                                                                                                                       |
| Operation Parameter 2 | [ObjectFormatCode]                                                                                                                                                                                                                                |
| Operation Parameter 3 | None                                                                                                                                                                                                                                              |
| Operation Parameter 4 | None                                                                                                                                                                                                                                              |
| Operation Parameter 5 | None                                                                                                                                                                                                                                              |
| Data                  | None                                                                                                                                                                                                                                              |
| Data Direction        | N/A                                                                                                                                                                                                                                               |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_StorageID, Store_Full, Invalid_ObjectFormatCode, Invalid_Parameter, Store_Not_Available, Invalid_Code_Format, Device_Busy, Parameter_Not_Supported, Store_Read-Only |
| Response Parameter 1  | None                                                                                                                                                                                                                                              |
| Response Parameter 2  | None                                                                                                                                                                                                                                              |
| Response Parameter 3  | None                                                                                                                                                                                                                                              |
| Response Parameter 4  | None                                                                                                                                                                                                                                              |
| Response Parameter 5  | None                                                                                                                                                                                                                                              |

The first parameter indicates the storage on which the captured object shall be stored.
The first parameter is optional, and if it is not used shall contain a value of 0x00000000.
If the first parameter does not contain 0x00000000 and the device cannot place the object
on the desired storage, the responder shall fail this operation with the appropriate
response code (Store_Not_Available, Invalid_StorageID, Store_Full).
The second parameter contains an ObjectFormatCode which indicates the format of the
object to be captured. If the second parameter contains a value of 0x00000000 it
indicates that the device shall capture an object in whatever format is the default for the
device.

The act of creating a new object in response to receiving this operation is asynchronous,
and does not occur immediately. An OK response to this operation indicates that the
responder accepts the command and will attempt to create a new object. The completion
of the capture shall be indicated by sending a Capture_Complete event. If the capture of
new object(s) does not fully complete successfully due to insufficient space on the target
storage, a Store_Full event shall be generated and a Capture_Complete event shall not.
An ObjectAdded event shall also be generated for each object which is created in the
execution of the new capture, and that event shall contain the TransactionID of the
InitiateCapture operation which triggered its creation. The device should not send any
other events during the capture session (other than ObjectAdded) until the
Capture_Complete event has been sent.

A separate operation, InitiateOpenCapture, described in section A.2.28, can be used to
support dynamically controlled captures that are terminable by the initiator.

Example Single Object InitiateCapture Sequence:
Initiator -> Responder: InitiateCapture Operation
Responder -> Initiator: InitiateCapture Response
Responder -> Initiator: ObjectAdded Event
Responder -> Initiator: CaptureComplete Event
Initiator -> Responder: GetObjectInfo Operation
Responder -> Initiator: ObjectInfo Dataset/Response

Example Multiple Object InitiateCapture Sequence
Initiator -> Responder: InitiateCapture Operation
Responder -> Initiator: InitiateCapture Response
Responder -> Initiator: ObjectAdded Event(1)
Responder -> Initiator: ObjectAdded Event(2)
...
Responder -> Initiator: ObjectAdded Event(n-1)
Responder -> Initiator: ObjectAdded Event(n)
Responder -> Initiator: CaptureComplete Event
Initiator -> Responder: GetObjectInfo Operation(1)
Responder -> Initiator: ObjectInfo Dataset/Response(1)
Initiator -> Responder: GetObjectInfo Operation(2)
Responder -> Initiator: ObjectInfo Dataset/Response(2)
...
Initiator -> Responder: GetObjectInfo Operation(n-1)
Responder -> Initiator: ObjectInfo Dataset/Response(n-1)
Initiator -> Responder: GetObjectInfo Operation(n)
Responder -> Initiator: ObjectInfo Dataset/Response(n)

#### D.2.15 FormatStore

This operation formats the media contained in the storage identified by the StorageID in
the first parameter.

| Operation Code        | 0x100F                                                                                                                                                                                 |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | StorageID                                                                                                                                                                              |
| Operation Parameter 2 | [FileSystem Format]                                                                                                                                                                    |
| Operation Parameter 3 | None                                                                                                                                                                                   |
| Operation Parameter 4 | None                                                                                                                                                                                   |
| Operation Parameter 5 | None                                                                                                                                                                                   |
| Data                  | None                                                                                                                                                                                   |
| Data Direction        | N/A                                                                                                                                                                                    |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_StorageID, Store_Not_Available, Device_Busy, Parameter_Not_Supported, Invalid_Parameter, Store_Read_Only |
| Response Parameter 1  | None                                                                                                                                                                                   |
| Response Parameter 2  | None                                                                                                                                                                                   |
| Response Parameter 3  | None                                                                                                                                                                                   |
| Response Parameter 4  | None                                                                                                                                                                                   |
| Response Parameter 5  | None                                                                                                                                                                                   |

If the storage in the first parameter cannot be formatted, the responder shall return the
appropriate response (Store_Read_Only, Invalid_StorageID, Store_Not_Available). If a
specified filesystem format is desired, the second parameter may contain a filesystem
type as defined in the StorageInfo dataset described in Section 5.2.2 “Storage Info
Dataset”.

If the device is unable to format the store due to concurrency issues, or due to a condition
which is known to be temporary, a response of Device_Busy shall be returned.

#### D.2.16 ResetDevice

This operation signals to the device that it is to return to a default state.

| Operation Code        | 0x1010                                                                            |
|-----------------------|-----------------------------------------------------------------------------------|
| Operation Parameter 1 | None                                                                              |
| Operation Parameter 2 | None                                                                              |
| Operation Parameter 3 | None                                                                              |
| Operation Parameter 4 | None                                                                              |
| Operation Parameter 5 | None                                                                              |
| Data                  | None                                                                              |
| Data Direction        | N/A                                                                               |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Device_Busy |
| Response Parameter 1  | None                                                                              |
| Response Parameter 2  | None                                                                              |
| Response Parameter 3  | None                                                                              |
| Response Parameter 4  | None                                                                              |
| Response Parameter 5  | None                                                                              |

This closes all open sessions. This does not affect the state of the device or its contents,
so all device properties and object properties shall remain unchanged following a device
reset.

If multiple sessions are open on the Responder when this operation is received, the
Responder shall send a DeviceReset event to all open sessions except the one in which
the ResetDevice operation was sent. These events must be sent prior to resetting.

#### D.2.17 SelfTest

This operation directs the device to implement a device-specific self-test.

| Operation Code        | 0x1011                                                                                                                      |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | [SelfTest Type]                                                                                                             |
| Operation Parameter 2 | None                                                                                                                        |
| Operation Parameter 3 | None                                                                                                                        |
| Operation Parameter 4 | None                                                                                                                        |
| Operation Parameter 5 | None                                                                                                                        |
| Data                  | None                                                                                                                        |
| Data Direction        | N/A                                                                                                                         |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, SelfTest_Failed, Device_Busy, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                        |
| Response Parameter 2  | None                                                                                                                        |
| Response Parameter 3  | None                                                                                                                        |
| Response Parameter 4  | None                                                                                                                        |
| Response Parameter 5  | None                                                                                                                        |

The first parameter is used to indicate the type of self-test that shall be performed,
according to the following table.

| Value                                               | Description                       |
|-----------------------------------------------------|-----------------------------------|
| 0x0000                                              | Default device-specific self-test |
| All other values with Bit 15 set to 0               | Reserved PTP                      |
| All values with Bit 15 set to 1 and Bit 14 set to 0 | MTP Vendor Extension range        |
| All values with Bit 15 set to 1 and Bit 14 set to 1 | Reserved MTP                      |

#### D.2.18 SetObjectProtection

This operation sets the write-protection status for the data object referred to in the first
parameter to the value indicated in the second parameter.

| Operation Code        | 0x1012                                                                                                                                                                                      |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                |
| Operation Parameter 2 | ProtectionStatus                                                                                                                                                                            |
| Operation Parameter 3 | None                                                                                                                                                                                        |
| Operation Parameter 4 | None                                                                                                                                                                                        |
| Operation Parameter 5 | None                                                                                                                                                                                        |
| Data                  | None                                                                                                                                                                                        |
| Data Direction        | N/A                                                                                                                                                                                         |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_ObjectHandle, Invalid_Parameter, Store_Not_Available, Parameter_Not_Supported, Store_Read_Only |
| Response Parameter 1  | None                                                                                                                                                                                        |
| Response Parameter 2  | None                                                                                                                                                                                        |
| Response Parameter 3  | None                                                                                                                                                                                        |
| Response Parameter 4  | None                                                                                                                                                                                        |
| Response Parameter 5  | None                                                                                                                                                                                        |

For a description of the ProtectionStatus field, refer to the ObjectInfo dataset described in
section 5.3.1 "ObjectInfo Dataset Description". If the ProtectionStatus field does not hold
a valid value, the ResponseCode shall be Invalid_Parameter.

#### D.2.19 PowerDown

This operation instructs the device to close all active sessions and power down.

| Operation Code        | 0x1013                                                                                                     |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | None                                                                                                       |
| Operation Parameter 2 | None                                                                                                       |
| Operation Parameter 3 | None                                                                                                       |
| Operation Parameter 4 | None                                                                                                       |
| Operation Parameter 5 | None                                                                                                       |
| Data                  | None                                                                                                       |
| Data Direction        | N/A                                                                                                        |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Device_Busy, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                       |
| Response Parameter 2  | None                                                                                                       |
| Response Parameter 3  | None                                                                                                       |
| Response Parameter 4  | None                                                                                                       |
| Response Parameter 5  | None                                                                                                       |

#### D.2.20 GetDevicePropDesc

This operation returns the DevicePropDesc dataset identified by the DevicePropCode in
the first parameter.

| Operation Code        | 0x1014                                                                                                                                              |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | DevicePropCode                                                                                                                                      |
| Operation Parameter 2 | None                                                                                                                                                |
| Operation Parameter 3 | None                                                                                                                                                |
| Operation Parameter 4 | None                                                                                                                                                |
| Operation Parameter 5 | None                                                                                                                                                |
| Data                  | DevicePropDesc dataset                                                                                                                              |
| Data Direction        | R->I                                                                                                                                                |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, DeviceProp_Not_Supported, Device_Busy, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                                                |
| Response Parameter 2  | None                                                                                                                                                |
| Response Parameter 3  | None                                                                                                                                                |
| Response Parameter 4  | None                                                                                                                                                |
| Response Parameter 5  | None                                                                                                                                                |

#### D.2.21 GetDevicePropValue

This operation returns the current value of the device property indicated by the
DevicePropCode in the first parameter.

| Operation Code        | 0x1015                                                                                                                               |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | DevicePropCode                                                                                                                       |
| Operation Parameter 2 | None                                                                                                                                 |
| Operation Parameter 3 | None                                                                                                                                 |
| Operation Parameter 4 | None                                                                                                                                 |
| Operation Parameter 5 | None                                                                                                                                 |
| Data                  | DeviceProp Value                                                                                                                     |
| Data Direction        | R->I                                                                                                                                 |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, DeviceProp_Not_Supported, Device_Busy, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                                 |
| Response Parameter 2  | None                                                                                                                                 |
| Response Parameter 3  | None                                                                                                                                 |
| Response Parameter 4  | None                                                                                                                                 |
| Response Parameter 5  | None                                                                                                                                 |

For more information about device properties refer to section 5.1.2 . The
GetDevicePropDesc also returns this value contained in the DevicePropDesc dataset
returned by that operation, and when both are supported by a device either can be used.

#### D.2.22 SetDevicePropValue

This operation sets the value of the device property identified by the DevicePropCode in
the first parameter.

| Operation Code        | 0x1016                                                                                                                                                                                                    |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | DevicePropCode                                                                                                                                                                                            |
| Operation Parameter 2 | None                                                                                                                                                                                                      |
| Operation Parameter 3 | None                                                                                                                                                                                                      |
| Operation Parameter 4 | None                                                                                                                                                                                                      |
| Operation Parameter 5 | None                                                                                                                                                                                                      |
| Data                  | DeviceProp Value                                                                                                                                                                                          |
| Data Direction        | I->R                                                                                                                                                                                                      |
| ResponseCode Options  | OK, Session_Not_Open, Invalid_TransactionID, Access_Denied, DeviceProp_Not_Supported, ObjectProp_Not_Supported, Invalid_DeviceProp_Format, Invalid_DeviceProp_Value, Device_Busy, Parameter_Not_Supported |
| Response Parameter 1  | None                                                                                                                                                                                                      |
| Response Parameter 2  | None                                                                                                                                                                                                      |
| Response Parameter 3  | None                                                                                                                                                                                                      |
| Response Parameter 4  | None                                                                                                                                                                                                      |
| Response Parameter 5  | None                                                                                                                                                                                                      |

The property value must conform to the restrictions placed upon it by the device property
description dataset. Device property description datasets are defined in detail in section
5.1.2.1.

If the property cannot be set, the responder shall return a value of Access_Denied. If the
value is not in a range allowed by the device and described by the DevicePropDesc
dataset, the responder shall respond with Invalid_DeviceProp_Value. If the format or
simple type of the new device property value does not correspond with the types
specified in the DevicePropDesc dataset for this device property, a response of
Invalid_DeviceProp_Format shall be returned.

#### D.2.23 ResetDevicePropValue

This operation sets the value of the device property identified by the DevicePropCode in
the first parameter to the default value.

| Operation Code        | 0x1017                                                                                                                                              |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | DevicePropCode                                                                                                                                      |
| Operation Parameter 2 | None                                                                                                                                                |
| Operation Parameter 3 | None                                                                                                                                                |
| Operation Parameter 4 | None                                                                                                                                                |
| Operation Parameter 5 | None                                                                                                                                                |
| Data                  | None                                                                                                                                                |
| Data Direction        | N/A                                                                                                                                                 |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, DeviceProp_Not_Supported, Device_Busy, Parameter_Not_Supported, Access_Denied |
| Response Parameter 1  | None                                                                                                                                                |
| Response Parameter 2  | None                                                                                                                                                |
| Response Parameter 3  | None                                                                                                                                                |
| Response Parameter 4  | None                                                                                                                                                |
| Response Parameter 5  | None                                                                                                                                                |

The default value for a device property is defined in the DevicePropDesc dataset for that
device property. DevicePropDesc datasets are described in section 5.1.2.1.

Attempting to Reset a Get-only device property results in the Access_Denied response.

If the first parameter contains a value of 0xFFFFFFFF, all settable device properties,
except DateTime (0x5011), shall be reset to their default value.

#### D.2.24 TerminateOpenCapture

This operation is used in conjunction with the InitiateOpenCapture operation to capture
new objects in an open-ended way.

| Operation Code        | 0x1018                                                                                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | TransactionID                                                                                                                                |
| Operation Parameter 2 | None                                                                                                                                         |
| Operation Parameter 3 | None                                                                                                                                         |
| Operation Parameter 4 | None                                                                                                                                         |
| Operation Parameter 5 | None                                                                                                                                         |
| Data                  | None                                                                                                                                         |
| Data Direction        | N/A                                                                                                                                          |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Parameter_Not_Supported, Invalid_Parameter, Capture_Already_Terminated |
| Response Parameter 1  | None                                                                                                                                         |
| Response Parameter 2  | None                                                                                                                                         |
| Response Parameter 3  | None                                                                                                                                         |
| Response Parameter 4  | None                                                                                                                                         |
| Response Parameter 5  | None                                                                                                                                         |

The first parameter identifies the TransactionID of the InitiateOpenCapture operation
which initiated the capture sequence which the initiator wishes to terminate. If the
capture has already completed, this operation shall respond with a
Capture_Already_Terminated response code. If the first parameter does not contain a
valid TransactionID, or does not refer to a transaction which contained
InitiateOpenCapture operation, the responder shall return a Invalid_TransactionID
response.

#### D.2.25 MoveObject

This operation changes the location of an object on the device, either by changing the
storage on which it is stored, or changing the location in which it is located, or both.

| Operation Code        | 0x1019                                                                                                                                                                                                                                            |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                                                                      |
| Operation Parameter 2 | StorageID of store to move object to                                                                                                                                                                                                              |
| Operation Parameter 3 | ObjectHandle of the new ParentObject                                                                                                                                                                                                              |
| Operation Parameter 4 | None                                                                                                                                                                                                                                              |
| Operation Parameter 5 | None                                                                                                                                                                                                                                              |
| Data                  | None                                                                                                                                                                                                                                              |
| Data Direction        | N/A                                                                                                                                                                                                                                               |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Store_Read_Only, Store_Not_Available, Invalid_ObjectHandle, Invalid_ParentObject, Device_Busy, Parameter_Not_Supported, Invalid_StorageHandle, Store_Full, Partial_Deletion |
| Response Parameter 1  | None                                                                                                                                                                                                                                              |
| Response Parameter 2  | None                                                                                                                                                                                                                                              |
| Response Parameter 3  | None                                                                                                                                                                                                                                              |
| Response Parameter 4  | None                                                                                                                                                                                                                                              |
| Response Parameter 5  | None                                                                                                                                                                                                                                              |

The first parameter identifies the object which is to be moved. If the first parameter does
not refer to an object on the device, the responder shall return an Invalid_ObjectHandle
response.

The second parameter is required, and identifies the storage to which the object indicated
in the first parameter is to be moved. If the target storage cannot be written to, this
operation shall fail with an appropriate response code (Store_Not_Available,
Store_Read_Only, Invalid_StorageHandle, Store_Full).

The third parameter is optional, and identifies the location on the file hierarchy of the
device to which this object is to be moved. If this parameter is unused, it shall contain a
value of 0x00000000, and the object shall be moved to the root of the storage indicated
by the second parameter.

If some subset of objects are not moved (but at least one object is moved), the response
Partial_Deletion shall be returned.

This object does not change the ObjectHandle of the object which is moved.

#### D.2.26 CopyObject

This operation causes the device to create a copy of the target object and place that copy
in a storage and location indicated by the parameters of this operation.

| Operation Code        | 0x101A                                                                                                                                                                                                 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                           |
| Operation Parameter 2 | StorageID that the newly copied object shall be placed into                                                                                                                                            |
| Operation Parameter 3 | ObjectHandle of newly copied object’s parent                                                                                                                                                           |
| Operation Parameter 4 | None                                                                                                                                                                                                   |
| Operation Parameter 5 | None                                                                                                                                                                                                   |
| Data                  | None                                                                                                                                                                                                   |
| Data Direction        | N/A                                                                                                                                                                                                    |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Store_Read_Only, Invalid_ObjectHandle, Invalid_ParentObject, Device_Busy, Store_Full, Parameter_Not_Supported, Invalid_StorageID |
| Response Parameter 1  | ObjectHandle of new copy of object                                                                                                                                                                     |
| Response Parameter 2  | None                                                                                                                                                                                                   |
| Response Parameter 3  | None                                                                                                                                                                                                   |
| Response Parameter 4  | None                                                                                                                                                                                                   |
| Response Parameter 5  | None                                                                                                                                                                                                   |

The first parameter identifies the object which is to be copied. If the first parameter does
not refer to an object on the device, the responder shall return an Invalid_ObjectHandle
response.

The second parameter is required, and identifies the storage on which the copy of the
object indicated in the first parameter is to be placed. If the target storage cannot be
written to, this operation shall fail with an appropriate response code.
(Store_Not_Available, Store_Read_Only, Invalid_StorageHandle, Store_Full)

The third parameter is optional, and identifies the location on the file hierarchy of the
device to which the copy of the object indicated in the first parameter is to be placed. If
this parameter is unused, it shall contain a value of 0x00000000, and the object shall be
placed in the root of the storage indicated by the second parameter.
Following the successful completion of this operation, the ObjectHandle of the new
object created is returned in the first response parameter.

#### D.2.27 GetPartialObject

This operation retrieves a partial object from the device, and may be used in place of the
GetObject operation.

| Operation Code        | 0x101B                                                                                                                                                                                             |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                       |
| Operation Parameter 2 | Offset in bytes                                                                                                                                                                                    |
| Operation Parameter 3 | Maximum number of bytes to obtain                                                                                                                                                                  |
| Operation Parameter 4 | None                                                                                                                                                                                               |
| Operation Parameter 5 | None                                                                                                                                                                                               |
| Data                  | Object Binary Data                                                                                                                                                                                 |
| Data Direction        | R->I                                                                                                                                                                                               |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_ObjectHandle, Invalid_ObjectFormatCode, Invalid_Parameter, Store_Not_Available, Device_Busy, Parameter_Not_Supported |
| Response Parameter 1  | Actual number of bytes sent                                                                                                                                                                        |
| Response Parameter 2  | None                                                                                                                                                                                               |
| Response Parameter 3  | None                                                                                                                                                                                               |
| Response Parameter 4  | None                                                                                                                                                                                               |
| Response Parameter 5  | None                                                                                                                                                                                               |

This operation applies to all data object types on a device. In the context of this operation,
the size fields in the ObjectInfo and Size Object Property represent the maximum size, as
opposed to the actual size. This operation is not necessary for objects which do not have a
binary component, such as folders or hierarchies.

The operation is identical to GetObject, except that the second and third parameters
contain the offset in bytes and the number of bytes to obtain starting from the offset. If
the entire object is desired, starting from the offset in the second parameter, the third
parameter may be set to 0xFFFFFFFF. The first response parameter shall contain the
actual number of bytes of the object sent, not including any wrappers or overhead
structures.

#### D.2.28 InitiateOpenCapture

This operation causes the device to initiate the capture of multiple new data objects as
specified by the current device properties.

| Operation Code        | 0x101C                                                                                                                                                                                                                                            |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | [StorageID]                                                                                                                                                                                                                                       |
| Operation Parameter 2 | [ObjectFormatCode]                                                                                                                                                                                                                                |
| Operation Parameter 3 | None                                                                                                                                                                                                                                              |
| Operation Parameter 4 | None                                                                                                                                                                                                                                              |
| Operation Parameter 5 | None                                                                                                                                                                                                                                              |
| Data                  | None                                                                                                                                                                                                                                              |
| Data Direction        | N/A                                                                                                                                                                                                                                               |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_StorageID, Store_Full, Invalid_ObjectFormatCode, Invalid_Parameter, Store_Not_Available, Invalid_Code_Format, Device_Busy, Parameter_Not_Supported, Store_Read-Only |
| Response Parameter 1  | None                                                                                                                                                                                                                                              |
| Response Parameter 2  | None                                                                                                                                                                                                                                              |
| Response Parameter 3  | None                                                                                                                                                                                                                                              |
| Response Parameter 4  | None                                                                                                                                                                                                                                              |
| Response Parameter 5  | None                                                                                                                                                                                                                                              |

The captured objects shall be saved to the store indicated by the StorageID in the first
parameter. If the StorageID is 0x00000000, the location where the objects will be saved
is determined by the responder. If the store specified is unavailable or the first parameter
contains 0x00000000 and there are no stores available, this operation shall return
Store_Not_Available.

Capturing new data objects is an asynchronous operation. If the ObjectFormatCode in the
second operation parameter is unspecified (and contains a value of 0x00000000), then the
device shall capture an object in a format chosen by the device.

A successful response to the InitiateOpenCapture operation means that the responder has
begun to capture one or more objects. When the initiator wishes to terminate the
capturing of new objects, it shall send a TerminateOpenCapture operation. The
CaptureComplete event shall not be sent at the end of this capture period if it is
terminated by the initiator. As new objects are created on the responder, the responder is
required to send an ObjectAdded event to the initiator for each object. The ObjectAdded
event shall contain the TransactionID of the InitiateOpenCapture operation which
initiated the capture of the device.

If the store becomes full while completing this operation, the device shall send a
Store_Full event containing the TransactionID of the InitiateOpenCapture operation in
progress. In the case of multiple objects being captured, each object shall be treated
separately, so any object captured before the store becomes full shall be retained.

Whether an object that was partially captured can be retained and used is a function of the
device’s behavior and object format. For example, if the device runs out of room while
capturing a video clip, it may be able to save the portion that it had room to store. A
Store_Full event completes the capture.

Single Object InitiateOpenCapture Sequence
Initiator -> Responder: InitiateOpenCapture Operation
Responder -> Initiator: InitiateOpenCapture Response
Initiator -> Responder: TerminateOpenCapture Operation
Responder -> Initiator: TerminateOpenCapture Response
Responder -> Initiator: ObjectAdded Event
Initiator -> Responder: GetObjectInfo Operation
Responder -> Initiator: ObjectInfo Dataset/Response

Multiple Object InitiateOpenCapture Sequence
Initiator -> Responder: InitiateOpenCapture Operation
Responder -> Initiator: InitiateOpenCapture Response
Responder -> Initiator: ObjectAdded Event(1)*
Responder -> Initiator: ObjectAdded Event(2)
Responder -> Initiator: ObjectAdded Event(n-1)
Responder -> Initiator: ObjectAdded Event(n)
Initiator -> Responder: TerminateOpenCapture Operation
Responder -> Initiator: TerminateOpenCapture Response
Initiator -> Responder: GetObjectInfo Operation(1)
Responder -> Initiator: ObjectInfo Dataset/Response(1)
Initiator -> Responder: GetObjectInfo Operation(2)
Responder -> Initiator: ObjectInfo Dataset/Response(2)
Initiator -> Responder: GetObjectInfo Operation(n-1)
Responder -> Initiator: ObjectInfo Dataset/Response(n-1)
Initiator -> Responder: GetObjectInfo Operation(n)
Responder -> Initiator: ObjectInfo Dataset/Response(n)

#### D.2.29 GetObjectPropsSupported

This operation returns an ObjectPropCode array of supported object properties for the
object format indicated in the first parameter.

| Operation Code        | 0x9801                                                                                    |
|-----------------------|-------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectFormatCode                                                                          |
| Operation Parameter 2 | None                                                                                      |
| Operation Parameter 3 | None                                                                                      |
| Operation Parameter 4 | None                                                                                      |
| Operation Parameter 5 | None                                                                                      |
| Data                  | ObjectPropCode Array                                                                      |
| Data Direction        | R->I                                                                                      |
| ResponseCode Options  | OK, Operation_Not_Supported, Device_Busy, Invalid_TransactionID, Invalid_ObjectFormatCode |
| Response Parameter 1  | None                                                                                      |
| Response Parameter 2  | None                                                                                      |
| Response Parameter 3  | None                                                                                      |
| Response Parameter 4  | None                                                                                      |
| Response Parameter 5  | None                                                                                      |

#### D.2.30 GetObjectPropDesc

This operation returns the appropriate property describing dataset indicated in the first
parameter as defined for the object format indicated in the second parameter.

| Operation Code        | 0x9802                                                                                                                                             |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectPropCode                                                                                                                                     |
| Operation Parameter 2 | Object Format Code                                                                                                                                 |
| Operation Parameter 3 | None                                                                                                                                               |
| Operation Parameter 4 | None                                                                                                                                               |
| Operation Parameter 5 | None                                                                                                                                               |
| Data                  | ObjectPropDesc dataset                                                                                                                             |
| Data Direction        | R->I                                                                                                                                               |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_ObjectPropCode, Invalid_ObjectFormatCode, Device_Busy |
| Response Parameter 1  | None                                                                                                                                               |
| Response Parameter 2  | None                                                                                                                                               |
| Response Parameter 3  | None                                                                                                                                               |
| Response Parameter 4  | None                                                                                                                                               |
| Response Parameter 5  | None                                                                                                                                               |

#### D.2.31 GetObjectPropValue

This operation returns the current value of an object property.

| Operation Code        | 0x9803                                                                                                                           |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                     |
| Operation Parameter 2 | ObjectPropCode                                                                                                                   |
| Operation Parameter 3 | None                                                                                                                             |
| Operation Parameter 4 | None                                                                                                                             |
| Operation Parameter 5 | None                                                                                                                             |
| Data                  | ObjectProp Value                                                                                                                 |
| Data Direction        | R->I                                                                                                                             |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_ObjectPropCode, Device_Busy, Invalid_Object_Handle |
| Response Parameter 1  | None                                                                                                                             |
| Response Parameter 2  | None                                                                                                                             |
| Response Parameter 3  | None                                                                                                                             |
| Response Parameter 4  | None                                                                                                                             |
| Response Parameter 5  | None                                                                                                                             |

The first parameter is required and identifies the object for which the property is
requested.

The second parameter is required and identifies the property that is requested for the
object identified in the first parameter.

The size and format of the data returned from this operation shall be determined from the
corresponding ObjectPropDesc dataset returned from the GetObjectPropDesc operation.

#### D.2.32 SetObjectPropValue

This operation sets the current value of the object property.

| Operation Code        | 0x9804                                                                                                                                                                     |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                               |
| Operation Parameter 2 | ObjectPropCode                                                                                                                                                             |
| Operation Parameter 3 | None                                                                                                                                                                       |
| Operation Parameter 4 | None                                                                                                                                                                       |
| Operation Parameter 5 | None                                                                                                                                                                       |
| Data                  | ObjectProp Value                                                                                                                                                           |
| Data Direction        | I->R                                                                                                                                                                       |
| ResponseCode Options  | OK, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_ObjectPropCode, Invalid_ObjectHandle, Device_Busy, Invalid_ObjectProp_Format, Invalid_ObjectProp_Value |
| Response Parameter 1  | None                                                                                                                                                                       |
| Response Parameter 2  | None                                                                                                                                                                       |
| Response Parameter 3  | None                                                                                                                                                                       |
| Response Parameter 4  | None                                                                                                                                                                       |
| Response Parameter 5  | None                                                                                                                                                                       |

This operation sets the current value of the object property indicated by parameter 2 for
the object indicated by parameter 1 to the value indicated in the data phase of the
operation. The format of the property value object sent in the data phase can be
determined by the DatatypeCode field of the property's ObjectPropDesc dataset. If the
property is not settable, the response Access_Denied shall be returned. If the value is not
allowed by the device, Invalid_ObjectProp_Value shall be returned. If the format or size
of the property value is incorrect, Invalid_ObjectProp_Format shall be returned.

#### D.2.33 GetObjectReferences

This operation returns an array of currently valid ObjectHandles.

| Operation Code        | 0x9810                                                                                                          |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                    |
| Operation Parameter 2 | None                                                                                                            |
| Operation Parameter 3 | None                                                                                                            |
| Operation Parameter 4 | None                                                                                                            |
| Operation Parameter 5 | None                                                                                                            |
| Data                  | ObjectHandle array                                                                                              |
| Data Direction        | R->I                                                                                                            |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Invalid_ObjectHandle, Store_Not_Available |
| Response Parameter 1  | None                                                                                                            |
| Response Parameter 2  | None                                                                                                            |
| Response Parameter 3  | None                                                                                                            |
| Response Parameter 4  | None                                                                                                            |
| Response Parameter 5  | None                                                                                                            |

If the object handle passed in the first parameter does not refer to a valid object, a
response code of Invalid_ObjectHandle shall be returned.

#### D.2.34 SetObjectReferences

This operation replaces the object references on an object.

| Operation Code        | 0x9811                                                                                                                                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                            |
| Operation Parameter 2 | None                                                                                                                                                                                                    |
| Operation Parameter 3 | None                                                                                                                                                                                                    |
| Operation Parameter 4 | None                                                                                                                                                                                                    |
| Operation Parameter 5 | None                                                                                                                                                                                                    |
| Data                  | ObjectHandle array                                                                                                                                                                                      |
| Data Direction        | I->R                                                                                                                                                                                                    |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_StorageID, Store_Read_Only, Store_Full, Store_Not_Available, Invalid_ObjectHandle, Invalid_ObjectReference |
| Response Parameter 1  | None                                                                                                                                                                                                    |
| Response Parameter 2  | None                                                                                                                                                                                                    |
| Response Parameter 3  | None                                                                                                                                                                                                    |
| Response Parameter 4  | None                                                                                                                                                                                                    |
| Response Parameter 5  | None                                                                                                                                                                                                    |

This operation replaces the object references on a device with the array of object handles
passed in the data phase. The object handles passed in the data phase must be maintained
indefinitely, and returned as valid object handles referencing the same object in later
sessions. If any of the object handles in the array passed in the data phase are invalid, the
responder shall fail the operation by returning a response code of
Invalid_ObjectReference.

If the object handle passed in the first parameter does not refer to a valid object a
response code of Invalid_ObjectHandle shall be returned.

If SetObjectReferences is called on an association object with an Association Type of 1
and an Association Description of 1, the device shall fail the operation with the response
Access_Denied.

#### D.2.35 Skip

This operation updates the current object being played back.

| Operation Code        | 0x9820                                                                                                                      |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | Skip Index                                                                                                                  |
| Operation Parameter 2 | None                                                                                                                        |
| Operation Parameter 3 | None                                                                                                                        |
| Operation Parameter 4 | None                                                                                                                        |
| Operation Parameter 5 | None                                                                                                                        |
| Data                  | None                                                                                                                        |
| Data Direction        | N/A                                                                                                                         |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, Store_Not_Available, Invalid_Parameter |
| Response Parameter 1  | None                                                                                                                        |
| Response Parameter 2  | None                                                                                                                        |
| Response Parameter 3  | None                                                                                                                        |
| Response Parameter 4  | None                                                                                                                        |
| Response Parameter 5  | None                                                                                                                        |

This operation updates the current object being played back by skipping either ahead or
behind in a device-specific playback queue. This operation requires one parameter,
containing a signed INT32 value, which indicates the depth and direction into the
playback queue to which the current playback object should skip.

A value of 1 indicates that the device shall skip ahead one media object to the object
immediately following the object currently identified in the Playback Object device
property. A value of -1 indicates that the previous object in the device playback queue
shall be loaded as the current playback object. If a device supports this operation, it must
support values of [-1,1]. If a value outside of this range is passed in this parameter, and
the device is incapable of interpreting it, a response code of Invalid_Parameter shall be
returned. If a value of 0 is passed in this parameter, the responder shall fail this operation
with a response code of Invalid_Parameter.

