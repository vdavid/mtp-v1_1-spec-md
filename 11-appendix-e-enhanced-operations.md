## Appendix E Enhanced Operations

### E.1 Enhanced Operation Summary Table

| Operation Name            | Operation Datacode |
|---------------------------|--------------------|
| GetObjectPropList         | 0x9805             |
| SetObjectPropList         | 0x9806             |
| GetInterdependentPropDesc | 0x9807             |
| SendObjectPropList        | 0x9808             |

### E.2 Enhanced Operation Descriptions

#### E.2.1 GetObjectPropList

This operation returns a dataset containing all object properties specified by the query
defined by the five parameters.

The primary purpose of this operation is to provide optimized access to object properties
without needing to individually query each {object,property} pair. However, it also
provides a more flexible querying mechanism for object properties in general, and
supercedes the simpler, object property retrieval methods.

| Operation Code        | 0x9805                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectHandle                                                                                                                                                                                                                                                                                                                                                                      |
| Operation Parameter 2 | [ObjectFormatCode]                                                                                                                                                                                                                                                                                                                                                                |
| Operation Parameter 3 | ObjectPropCode                                                                                                                                                                                                                                                                                                                                                                    |
| Operation Parameter 4 | [ObjectPropGroupCode]                                                                                                                                                                                                                                                                                                                                                             |
| Operation Parameter 5 | [Depth]                                                                                                                                                                                                                                                                                                                                                                           |
| Data                  | ObjectPropList dataset                                                                                                                                                                                                                                                                                                                                                            |
| Data Direction        | R->I                                                                                                                                                                                                                                                                                                                                                                              |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, ObjectProp_Not_Supported, Invalid_ObjectHandle, Group_Not_Supported, Device_Busy, Parameter_Not_Supported, Specification_By_Format_Unsupported, Specification_By_Group_Unsupported, Specification_By_Depth_Unsupported, Invalid_Code_Format, Invalid_ObjectPropCode, Invalid_StorageID, Store_Not_Available |
| Response Parameter 1  | None                                                                                                                                                                                                                                                                                                                                                                              |
| Response Parameter 2  | None                                                                                                                                                                                                                                                                                                                                                                              |
| Response Parameter 3  | None                                                                                                                                                                                                                                                                                                                                                                              |
| Response Parameter 4  | None                                                                                                                                                                                                                                                                                                                                                                              |
| Response Parameter 5  | None                                                                                                                                                                                                                                                                                                                                                                              |

The first parameter is required, and defines the object for which properties are requested.
A value of 0xFFFFFFFF indicates that all objects are requested. A value of 0x00000000
indicates that all objects at the root level are desired, and may be further specified by the
second and/or fifth parameters.

The second parameter is optional, and may be used to request only properties for objects
which possess a format specified by the ObjectFormatCode. A value of 0x00000000
indicates that this parameter is not being used, and properties of all Object Formats are
desired. If the value is not 0x00000000 and the device does not support specification by
ObjectFormatCode, it shall fail the operation by returning a response code with the value
of Specificiation_By_Format_Unsupported. For the second parameter, the value
0xFFFFFFFF is reserved for future use.

The third parameter is required and identifies the ObjectPropCode of the property that is
being requested. A value of 0xFFFFFFFF indicates that all properties are requested
except those with a group code of 0xFFFFFFFF; properties with this group code are
defined as being potentially very slow, and shall be retrieved separately.

A value of 0x00000000 in the third parameter indicates that the fourth parameter shall be
used. If the value is 0x00000000 and the Responder does not support specification by
ObjectPropGroupCode, it shall fail the operation by returning a response code with the
value of Specification_By_Group_Unsupported. If both the third and the fourth
parameters contain the value 0x00000000, then Parameter_Not_Supported shall be
returned.

The final parameter is optional, and allows properties to be queried for all objects at a
certain level (or levels) of a folder hierarchy on the device. In this case, properties (as
defined by the third and/or fourth parameters) shall be returned for all objects, down to a
depth from the top object, including the top object, which is identified in the first
parameter. If the first parameter contains a value of 0x00000000, then the Responder
shall return property values for objects starting from the root (having no parent object) to
the desired depth.

If the value of the fifth parameter is 0x00000000, it indicates that properties for objects
are desired to a depth of 0, which returns only the head object (as indicated by the first
parameter). If the fifth parameter contains a value of 0x00000000, and the ObjectHandle
in the first parameter also contains a value of 0x00000000, the Responder shall return an
empty set.

If the final parameter contains a value of 0xFFFFFFFF, the Responder shall return all
values for all objects that are contained within the folder hierarchy rooted at the object
identified by the first parameter. It should be noted that a value of 0x00000000 in the first
two parameters, followed by a value of 0xFFFFFFFF in the fifth parameter, is equivalent
to having a value of 0xFFFFFFFF in the first parameter.

If the fifth parameter contains a non-zero value and the property or properties indicated
by the third and fourth parameters are not supported for all objects in the desired hierarcy,
then the Responder shall return an ObjectPropList dataset containing only the properties
which are both requested and supported for each (but not necessarily every) object in the
desired hierarchy. If a property is identified by the third parameter which not
implemented for any object format type on the device, then a response of
ObjectProp_Not_Supported shall be returned.

It is recommended that Responders support specification by depth to at least one level to
support file-browsing scenarios. If the Responder does not support specification by
depth, or the Responder does not support specification to the desired depth, it shall fail
the operation by returning a response code with the value of
Specification_By_Depth_Unsupported.

##### E.2.1.1 ObjectPropList Dataset Table:

| Field name           | Field order | Size (bytes) | Datatype     | Description                                                   |
|----------------------|-------------|--------------|--------------|---------------------------------------------------------------|
| NumberOfElements     | 1           | 4            | UINT32       | Count of property quadruples in this dataset.                 |
| Element1ObjectHandle | 2           | 4            | ObjectHandle | ObjectHandle of the object to which Property1 applies.        |
| Element1PropertyCode | 3           | 2            | Datacode     | Datacode identifying the ObjectPropDesc describing Property1. |
| Element1Datatype     | 4           | 2            | Datacode     | This field identifies the DatatypeCode of Property1.          |
| Element1Value        | 5           | DTS          | DTS          | Value of Property1.                                           |
| Element2ObjectHandle | 6           | 4            | ObjectHandle | ObjectHandle of the object to which Property2 applies.        |
| Element2PropertyCode | 7           | 2            | Datacode     | Datacode identifying the ObjectPropDesc describing Property2. |
| Element2Datatype     | 8           | 2            | Datacode     | This field identifies the DatatypeCode of Property2.          |
| Element2Value        | 9           | DTS          | DTS          | Value of Property2.                                           |
| ...                  |             |              |              |                                                               |
| ElementNObjectHandle | 4*N-2       | 4            | ObjectHandle | ObjectHandle of the object to which PropertyN applies.        |
| ElementNPropertyCode | 4*N-1       | 2            | Datacode     | Datacode identifying the ObjectPropDesc describing PropertyN. |
| ElementNDatatype     | 4*N         | 2            | Datacode     | This field identifies the DatatypeCode of PropertyN.          |
| ElementNValue        | 4*N+1       | DTS          | DTS          | Value of PropertyN.                                           |

#### E.2.2 SetObjectPropList

This operation sets ObjectProperty values contained in the dataset provided.

| Operation Code        | 0x9806                                                                                                                                                                                                                                                           |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | None                                                                                                                                                                                                                                                             |
| Operation Parameter 2 | None                                                                                                                                                                                                                                                             |
| Operation Parameter 3 | None                                                                                                                                                                                                                                                             |
| Operation Parameter 4 | None                                                                                                                                                                                                                                                             |
| Operation Parameter 5 | None                                                                                                                                                                                                                                                             |
| Data                  | ObjectPropList dataset                                                                                                                                                                                                                                           |
| Data Direction        | I->R                                                                                                                                                                                                                                                             |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_denied, ObjectProp_Not_Supported, Invalid_ObjectProp_Format, Invalid_ObjectProp_Value, Invalid_ObjectHandle, Device_Busy, ObjectProp_Not_Supported, Store_Not_Available, Store_Full |
| Response Parameter 1  | None                                                                                                                                                                                                                                                             |
| Response Parameter 2  | None                                                                                                                                                                                                                                                             |
| Response Parameter 3  | None                                                                                                                                                                                                                                                             |
| Response Parameter 4  | None                                                                                                                                                                                                                                                             |
| Response Parameter 5  | None                                                                                                                                                                                                                                                             |

If this operation fails, and all property values sent in the ObjectPropList are not applied
successfully, the operation must return a ResponseCode identifying the reason for failing
to update the property, and a response parameter indicating the (0-based) index of the
property which failed to be applied. The responder must not process any of the object
property values that follow the property that failed to update. If none of the properties
were able to be set, the response parameter shall contain a value of 0x00000000.

If the operation succeeds, the first response parameter shall contain 0x00000000.

#### E.2.3 GetInterdependentPropDesc

An Initiator can query for interdependent properties using the
GetInterdependentPropDesc operation.

| Operation Code        | 0x9807                                                                                                 |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | ObjectFormatCode                                                                                       |
| Operation Parameter 2 | None                                                                                                   |
| Operation Parameter 3 | None                                                                                                   |
| Operation Parameter 4 | None                                                                                                   |
| Operation Parameter 5 | None                                                                                                   |
| Data                  | InterdependentPropDesc dataset                                                                         |
| Data Direction        | R->I                                                                                                   |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Device_Busy, Invalid_Code_Format |
| Response Parameter 1  | None                                                                                                   |
| Response Parameter 2  | None                                                                                                   |
| Response Parameter 3  | None                                                                                                   |
| Response Parameter 4  | None                                                                                                   |
| Response Parameter 5  | None                                                                                                   |

An Initiator can query for interdependent properties using the
GetInterdependentPropDesc operation, which returns an array of ObjectPropertyDesc
arrays, each describing an allowed collection of ranges. Each array of
ObjectPropertyDesc datasets returned gives one possible definition for the interdependent
properties contained in that array; properties not found in that array are constrained only
by the usual ObjectPropDesc datasets.

The first parameter is required, and defines the object format for which interdependent
property codes are desired. A value of 0xFFFFFFFF or 0x00000000 shall not be used.

The operation returns the dataset shown in the following table.

##### E.2.3.1 InterDependentPropList Dataset Table

| Field name                 | Field order | Size (bytes) | Datatype                              | Description                                                                  |
|----------------------------|-------------|--------------|---------------------------------------|------------------------------------------------------------------------------|
| NumberOfInterdependencies  | 1           | 4            | UINT32                                | Count of arrays of interdependencies to follow                               |
| NumberOfPropDescs 1        | 2           | 2            | UINT16                                | Count of object property description datasets in this interdependency array  |
| ObjectPropDesc Dataset 1,1 | 3           | DTS          | See ObjectPropDesc dataset definition | An ObjectPropDesc dataset defining allowed values in this interdependent set |
| ...                        | ...         | ...          |                                       |                                                                              |
| ObjectPropDesc Dataset 1,n | n+2         | DTS          | See ObjectPropDesc dataset definition | An ObjectPropDesc dataset defining allowed values in this interdependent set |
| NumberOfPropDescs 2        | n+3         | 2            | UINT16                                | Count of object property description datasets in this interdependency array  |
| ObjectPropDesc Dataset 2,1 | n+4         | DTS          | See ObjectPropDesc dataset definition | An ObjectPropDesc dataset defining allowed values in this interdependent set |
| ...                        | ...         | ...          |                                       |                                                                              |
| ObjectPropDesc Dataset 2,m | m+n+3       | DTS          | See ObjectPropDesc dataset definition | An ObjectPropDesc dataset defining allowed values in this interdependent set |
| ...                        | ...         | ...          |                                       |                                                                              |

This dataset begins with an entry which counts the number of interdependencies which
follow.

Each interdependency which follows consists of a set of concatenated ObjectPropDesc
datasets whose constraints (as identified in their FORM fields) apply as a group. This set
is preceded by a count of the number of ObjectPropDesc datasets which follow in that
interdependent set of object properties.

#### E.2.4 SendObjectPropList

| Operation Code        | 0x9808                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Parameter 1 | [Destination StorageID on responder]                                                                                                                                                                                                                                                                                                                                                                                            |
| Operation Parameter 2 | [Parent ObjectHandle on responder where object shall be placed]                                                                                                                                                                                                                                                                                                                                                                 |
| Operation Parameter 3 | ObjectFormatCode                                                                                                                                                                                                                                                                                                                                                                                                                |
| Operation Parameter 4 | ObjectSize [most significant 4 bytes]                                                                                                                                                                                                                                                                                                                                                                                           |
| Operation Parameter 5 | ObjectSize [least significant 4 bytes]                                                                                                                                                                                                                                                                                                                                                                                          |
| Data                  | ObjectPropList dataset                                                                                                                                                                                                                                                                                                                                                                                                          |
| Data Direction        | I->R                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ResponseCode Options  | OK, Operation_Not_Supported, Session_Not_Open, Invalid_TransactionID, Access_Denied, Invalid_StorageID, Store_Read_Only, Store_Full, Invalid_ObjectFormatCode, Store_Not_Available, Parameter_Not_Supported, Invalid_ParentObject, Invalid_Dataset, ObjectProp_Not_Supported, Invalid_ObjectProp_Format, Invalid_ObjectProp_Value, Invalid_ObjectHandle, Object_Too_Large, Store_Full, Specification_Of_Destination_Unsupported |
| Response Parameter 1  | Responder StorageID in which the object will be stored                                                                                                                                                                                                                                                                                                                                                                          |
| Response Parameter 2  | Responder parent ObjectHandle in which the object will be stored                                                                                                                                                                                                                                                                                                                                                                |
| Response Parameter 3  | Responder’s reserved ObjectHandle for the incoming object                                                                                                                                                                                                                                                                                                                                                                       |
| Response Parameter 4  | [Index of failed property]                                                                                                                                                                                                                                                                                                                                                                                                      |
| Response Parameter 5  | None                                                                                                                                                                                                                                                                                                                                                                                                                            |

This is used as an alternative first operation when the initiator wants to send an object to
the responder. This operation sends a modified ObjectPropList dataset from the initiator
to the responder.

This operation is sent prior to the SendObject operation, in order to inform the responder
about the properties of the object that it intends to send later, and to ask whether the
object can be sent to the responder. A response of "OK" implies that the receiver can
accept the object, and serves to inform the sender that it may now issue a SendObject
operation for the object.

The first parameter is optionally used to indicate the store on the responder into which the
object shall be stored. If this parameter is specified, and the responder will not be able to
store the object in the indicated store, the operation shall fail, and the appropriate
response, such as Specification_Of_Destination_Unsupported, Store_Not_Available,
Store_Read_Only, or Store_Full shall be used. If this parameter is unused, it shall be set
to 0x00000000, and the responder shall decide in which store to place the object, whether
that is a responder-determined default location, or the location with the most free space
(or possibly the only location with enough free space).

The second parameter is optionally used to indicate where on the indicated store the
object is to be placed (the association/folder that the object is to become a child of). If
this parameter is used, the first parameter must also be used. If the receiver is unable to
place the object as a child of the indicated second parameter, the operation shall fail.

The third parameter identifies the ObjectFormat datacode of the object, which may be
required to validate the properties sent in the data phase. If the ObjectFormat code
indicated in the third parameter is not supported by the responder (as indicated in the
DeviceInfo dataset), the responder shall fail and return an Invalid_ObjectHandle
response.

The fourth and fifth parameters together indicate the size of the data object to be sent. If
the indicated size is larger than the available space on the device, it shall fail this
operation and return a response of Store_Full.

If the problem with the attempted specification is the general inability of the receiving
device to allow the specification of destination, the response
Specification_of_Destination_Unsupported shall be sent. This response implies that the
initiator should not try to specify a destination location in future invocations of
SendObjectInfo, as all attempts at such specification will fail. If the problem is only with
the particular destination specified, the Invalid_ObjectHandle or Invalid_ParentObject
response shall be used, depending on whether the ObjectHandle did not refer to a valid
object or the indicated object is a valid object, but is not an association.

If the root directory of the indicated store is needed, the second parameter shall be set to
0xFFFFFFFF. If this parameter is unused, it shall be set to 0x00000000, and the
responder shall decide where in the indicated store the object is to be placed. If neither
the first nor the second parameter is used, the responder shall decide which store to place
the object in, and where to place it within that store.

An object handle issued during a successful SendObjectInfo or SendObjectPropList
operation should be reserved for the duration of the MTP session, even if there is no
successful SendObject operation for that handle.

Object properties that are get-only (0x00 GET) shall accept values during object creation
via the SendObjectPropList command.
If the responder agrees that the object may be sent, it is required to retain this
ObjectPropList dataset until the next SendObject, SendObjectPropList or SendObjectInfo
operation is performed within the session. If the SendObjectPropList operation succeeds,
and the next occurring SendObject operation does not return a successful response, the
sent ObjectPropList dataset shall be retained by the responder in case the initiator wants
to re-attempt the SendObject operation for that previously successful SendObjectPropList
operation. If the initiator wants to resend the ObjectPropList dataset before attempting to
resend the object, it may do so. Successful completion of the SendObjectPropList
operation conveys that the responder possesses a copy of all sent properties, and that the
responder has allocated space for the incoming data object. Any response code other than
OK indicates that the responder has not retained the ObjectPropList dataset, and the
object shall not be sent.

For a particular session, the receiving device shall only retain one ObjectPropList or
ObjectInfo dataset that is the result of a SendObjectInfo or SendObjectPropList operation
in memory at a time. If another SendObjectInfo or SendObjectPropList operation occurs
before a SendObject operation, the new ObjectInfo or ObjectPropList shall replace the
previously held one. If this occurs, any storage or memory space reserved for the object
described in the overwritten ObjectInfo or ObjectPropList dataset shall be freed before
overwriting and allocating the resources for the new data. Upon the successful execution
of this operation, the next operation called in the same session shall be a SendObject
operation. If the next operation sent in the same session is not a SendObject operation,
the responder shall not retain the sent ObjectPropList or ObjectInfo dataset.
The first response parameter of this operation shall be set to the StorageID that the
responder will store the object into if it is sent. The second response parameter of this
operation shall be set to the parent ObjectHandle of the association that the object
becomes a child of. If the object is stored in the root of the store, this parameter shall be
set to 0xFFFFFFFF.

If the initiator wants to retain an association hierarchy on the responder for the objects it
is sending, then the objects must be sent top down, starting with the highest level of the
hierarchy, and proceeding in either a depth-first or breadth-first fashion down the
hierarchy tree. The initiator shall use the responder’s newly assigned ObjectHandle in the
third response parameter for the ParentObject that is returned in the SendObjectPropList
response as the second operation parameter for a child’s SendObjectPropList operation.

The dataset sent in this operation is similar to the ObjectPropValueList dataset sent and
received in the SetObjectPropList and GetObjectPropList operations respectively, but has
additional restrictions on the values of the contained fields. All ObjectHandle fields must
contain the value 0x00000000, and all properties defined in this operation will be applied
to the object, which is sent in a subsequent SendObject operation. If any properties are
inconsistent, that is, the property is either not supported or the value is inconsistent for
the sent ObjectFormat, then this operation shall fail with the appropriate response code,
and indicate the (0-based) index of the first failed property in the fourth return parameter.
If the object size indicated in the data phase of this operation indicates that the object to
be sent has a size of 0, then a response of OK indicates that the object has been sent
successfully, and it is not required that this operation be followed by a SendObject
operation. However, the responder shall not fail the request if a SendObject operation
follows containing an object of size 0.

Properties which are contained in the operation parameters (StorageID, ParentObject,
ObjectFormat, ObjectSize) shall not be included in the sent dataset.

