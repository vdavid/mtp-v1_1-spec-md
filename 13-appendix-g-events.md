## Appendix G Events

### G.1 Event Summary Table

| MTP Name                | Event Datacode |
|-------------------------|----------------|
| Undefined               | 0x4000         |
| CancelTransaction       | 0x4001         |
| ObjectAdded             | 0x4002         |
| ObjectRemoved           | 0x4003         |
| StoreAdded              | 0x4004         |
| StoreRemoved            | 0x4005         |
| DevicePropChanged       | 0x4006         |
| ObjectInfoChanged       | 0x4007         |
| DeviceInfoChanged       | 0x4008         |
| RequestObjectTransfer   | 0x4009         |
| StoreFull               | 0x400A         |
| DeviceReset             | 0x400B         |
| StorageInfoChanged      | 0x400C         |
| CaptureComplete         | 0x400D         |
| UnreportedStatus        | 0x400E         |
| ObjectPropChanged       | 0xC801         |
| ObjectPropDescChanged   | 0xC802         |
| ObjectReferencesChanged | 0xC803         |

### G.2 Event Descriptions

#### G.2.1 Undefined

Event Code: 0x4000
Parameter 1: None
Parameter 2: None
Parameter 3: None

This event code is undefined, and is not used.

#### G.2.2 CancelTransaction

Event Code: 0x4001
Parameter 1: None
Parameter 2: None
Parameter 3: None

This event is used to initiate the cancellation of a transaction.It is strongly recommended
to utilize USB cancelation functionality in preference to this protocol level cancelation.
When an Initiator or Responder receives this event, it shall cancel the transaction
identified by the TransactionID in the event dataset. If the transaction has already
completed, this event shall be ignored.

After receiving a CancelTransaction event from the initiator during an object transfer, the
responder shall send an Transaction_Cancelled response for the transfer which was in
progress.

#### G.2.3 ObjectAdded

Event Code: 0x4002
Parameter 1: ObjectHandle
Parameter 2: None
Parameter 3: None

This event indicates that a new data object has been added to the device. The first
parameter of this event shall contain the ObjectHandle assigned by the device to the new
object. If more than one object has been added, each new object shall generate its own
ObjectAdded event. This event shall not be issued by the appearance of a new store on
the device, which shall instead cause the generation of a StoreAdded event.

#### G.2.4 ObjectRemoved

Event Code: 0x4003
Parameter 1: ObjectHandle
Parameter 2: None
Parameter 3: None

This event indicates that a data object has been removed from the device for reasons
external to the current session. The handle of the removed object shall be contained in the
first parameter of this event. If more than one object is removed, each removed object
shall generate its own ObjectRemoved event. If the data object was removed because of a
previous operation issued in the current session, no event shall be isued. This event shall
not be issued by the removal of a store from the device, which shall instead cause the
generation of one StoreRemoved event with the appropriate PhysicalStorageID.

#### G.2.5 StoreAdded

Event Code: 0x4004
Parameter 1: StorageID
Parameter 2: None
Parameter 3: None

This event indicates that a new store has been added to the device. If this is a new
physical store which contains only one logical store, then the complete StorageID of the
new store shall be contained in the first parameter. If the new store contains more than
one logical store, then the first parameter shall be set to 0x00000000 and the initiator
should retrieve a new list of StorageIDs using the GetStorageIDs operation. Any new
StorageIDs discovered should result in the appropriate invocations of GetStorageInfo
operations.

#### G.2.6 StoreRemoved

Event Code: 0x4005
Parameter 1: StorageID
Parameter 2: None
Parameter 3: None

The indicated stores are no longer available. The opposing device may assume that the
StorageInfo datasets and ObjectHandles associated with those stores are no longer valid.

The first parameter is used to indicate the StorageID of the store that is no longer
available. If the store that has been removed is only a single logical store within a
physical store, the entire StorageID shall be sent, which indicates that any other logical
stores on that physical store are still available. If the physical store and all logical stores
upon it are removed (for example, removal of an ejectable media device that contains
multiple partitions), the first parameter shall contain the PhysicalStorageID in the most
significant sixteen bits, with the least significant sixteen bits set to 0xFFFF.

#### G.2.7 DevicePropChanged

Event Code: 0x4006
Parameter 1: DevicePropCode
Parameter 2: None
Parameter 3: None

A property changed on the device due to something external to this session. The
appropriate property dataset should be requested from the opposing Responder.

#### G.2.8 ObjectInfoChanged

Event Code: 0x4007
Parameter 1: ObjectHandle
Parameter 2: None
Parameter 3: None

This event indicates that the ObjectInfo dataset for a particular object has changed, and
that it should be requested again.

#### G.2.9 DeviceInfoChanged

Event Code: 0x4008
Parameter 1: None
Parameter 2: None
Parameter 3: None

This event indicates that the capabilities of the Responder have changed, and that the
DeviceInfo should be requested again. This may be caused by the Responder going into
or out of a sleep state, or by the Responder losing or gaining some functionality.

#### G.2.10 RequestObjectTransfer

Event Code: 0x4009
Parameter 1: ObjectHandle
Parameter 2: None
Parameter 3: None

This event can be used by a responder to ask the initiator to initiate a GetObject operation
on the handle specified in the first parameter. This allows for push-mode to be enabled on
devices that intrinsically use pull mode.

#### G.2.11 StoreFull

Event Code: 0x400A
Parameter 1: StorageID
Parameter 2: None
Parameter 3: None

This event shall be sent when a store becomes full. Any multi-object capture that may be
occurring shall retain the objects that were written to a store before the store became full.

#### G.2.12 DeviceReset

Event Code: 0x400B
Parameter 1: None
Parameter 2: None
Parameter 3: None

This event only needs to be supported for devices that support multiple sessions or if the
device is capable of resetting itself automatically or manually through user intervention
while connected. This event shall be sent to all open sessions other than the session that
initiated the operation. This event shall be interpreted as indicating that the sessions are
about to be closed.

#### G.2.13 StorageInfoChanged

Event Code: 0x400C
Parameter 1: StorageID
Parameter 2: None
Parameter 3: None

This event is used when information in the StorageInfo dataset for a store changes. This
can occur due to device properties changing, such as ImageSize, which can cause
changes in fields such as FreeSpaceInImages. This event is typically not needed if the
change is caused by an in-session operation that affects whole objects in a deterministic
manner. This includes changes in FreeSpaceInImages or FreeSpaceInBytes caused by
operations such as InitiateCapture or CopyObject, where the initiator can recognize the
changes due to the successful response code of the operation, and/or related, required
events.

#### G.2.14 CaptureComplete

Event Code: 0x400D
Parameter 1: TransactionID
Parameter 2: None
Parameter 3: None

This event is used to indicate that a capture session, previously initiated by the
InitiateCapture operation, is complete, and that no more ObjectAdded events will occur
as the result of this asynchronous operation. This operation is not used for
InitiateOpenCapture operations.

#### G.2.15 UnreportedStatus

Event Code: 0x400E
Parameter 1: None
Parameter 2: None
Parameter 3: None

When an initiator receives this event, it is responsible for doing whatever is necessary to
ensure that its knowledge of the responder is current. This may include re-obtaining
information such as individual datasets or ObjectHandle lists, or may even result in the
session being closed and re-opened.

#### G.2.16 ObjectPropChanged

Event Code: 0xC801
Parameter 1: ObjectHandle
Parameter 2: ObjectPropCode
Parameter 3: None

This event is used to indicate that an object property value on the Responder has changed,
without that change being performed by the initiator. The parameters passed indicate
which property on which object has been updated.

#### G.2.17 ObjectPropDescChanged

Event Code: 0xC802
Parameter 1: ObjectPropCode
Parameter 2: ObjectFormatCode
Parameter 3: None

This event indicates that an object property description dataset has been updated,
indicating some change on the device. The parameters passed with this event identify the
ObjectPropDesc dataset which has changed.

#### G.2.18 ObjectReferencesChanged

Event Code: 0xC803
Parameter 1: ObjectHandle
Parameter 2: None
Parameter 3: None

This event is used to indicate that the references on an object have been updated. The
object handle in the first parameter identifies the object whose references have changed.
When objects are deleted by the Initiator and the Responder cleans up any references to
the now-deleted object, the Responder does not need to send this event for the resulting
reference updates.

