## Appendix H USB Optimizations

### H.1 Sending >4GB Binary Objects

As outlined in section 4.3 MTP Transactions, transactions in MTP take place in three
phases: Operation, Data and Response. The USB implementation defined by ISO 15740
requires that the data communicated in a given phase be contained in a container
structure, outlined in Appendix D of the ISO 15740. This generic container contains an
entire transfer phase; multiple containers cannot be combined. In PTP, any short packet
indicates the end of a particular phase (a NULL packet if ContainerLength divides the
USB Packet Size.)

#### USB Generic Container Dataset

| Byte Offset | Length (Bytes)     | Field Name      | Description                                                                                                                |
|-------------|--------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| 0           | 4                  | ContainerLength | Total amount of data to be sent (including this header)                                                                    |
| 4           | 2                  | ContainerType   | Defines the type of this container: 0x0000 = Undefined, 0x0001 = Command, 0x0002 = Data, 0x0003 = Response, 0x0004 = Event |
| 6           | 2                  | Code            | Operation, Response or Event Code as defined in the MTP specification                                                      |
| 8           | 4                  | TransactionID   | See section 4.3.3 Transaction IDs                                                                                          |
| 12          | ContainerLength-12 | Payload         | The data which is to be sent in this phase                                                                                 |

This container structure restricts the total size of the data transmitted in a phase to a size
able to be defined by a 4-byte field (approx 4GB). In order to send a larger data object
during a data phase, a value of 0xFFFFFFFF shall be contained in the ContainerLength
field. This may only be performed during a data phase; the restriction that the Command,
Response and Event phases cannot contain more than (232-1) bytes remains.

### H.2 Sending a >4GB Object with a SendObject Operation

In the likely scenario where the generic container represents the data phase of a
SendObject operation, the following additional restrictions apply:

It is the responsibility of the initiator to ensure that there is sufficient space on the
responder to contain the sent data object on the target storage; failure to do so will result
in the data transfer failing when the incoming object has overflowed the allocated storage
on the device.

It is the responsibility of the responder to first ensure that it has space for at least a 4GB
data object. If not, it shall respond appropriately. If the initiator specified a target storage
for the object being sent, the responder shall attempt to place it on that storage, and fail if
there is insufficient space on that storage with the appropriate response code. Then,
assuming that a file of at least 4Gb may be sent, it shall accept the object.

### H.3 Retrieving a >4GB Object with a GetObject Operation

The other likely scenario for large data transfer is retrieving an object from a responder.

When retrieving an object, the size of the object to be retrieved shall be identified using
the ObjectCompressedSize Object Property, which is not limited to 32 bits. That size
shall be used to identify the size of the incoming data transfer, not including the size of
the generic container header. (Add 12 bytes to the value in the ObjectCompressedSize
object property to determine the value that would be placed in the ContainerLength field
if it were not limited to 32 bits.)

### H.4 Splitting the Header and Data during the Data Phase

As outlined in section 4.3 MTP Transactions, transactions in MTP take place in three
phases: Operation, Data and Response. The USB implementation defined by ISO 15740
requires that the data communicated in a given phase be contained in a container
structure, outlined in Appendix D of the ISO 15740, and also reproduced in the previous
section. This generic container contains an entire transfer phase; multiple containers
cannot be combined. In PTP, any short packet indicates the end of a particular phase (a
NULL packet if ContainerLength divides the USB Packet Size).

This artificial header presents a difficulty for devices that wish to write an incoming
datastream directly to the device, or that wish to pipe data directly to an outgoing
datastream.

An MTP responder may overcome this by separating the header from the payload and
sending/receiving it in a short packet preceding the payload. Devices that choose to do
this must always manage these packets consistently. That is, all data phases (all USB data
transfers where the ContainerType = 0x0002) must have a single packet containing 12
bytes, which has only the header which is followed by the payload beginning with a new
packet. This applies both to data sent to the device and retrieved from the device.

Operations, Responses and Events remain unchanged, and shall never have their generic
container header split from the payload.

If an MTP responder implementation chooses to take advantage of this option, it does not
need to indicate this directly in any way. Rather, it is the responsibility of the MTP
initiator to determine whether the MTP device is separating the header from the payload,
based upon observed behavior. The suggested method is to use a known required
operation (such as GetDeviceInfo) which has a data phase containing known data, and
based upon the format of the structure returned in the data phase, determine how to
handle future data phases.

If the data payload transferred in a data phase of an operation is empty, that is, there is no
data but a data phase is defined, then the data phase consists of a single generic container
header (which identifies the total amount of data to be 12 bytes: the size of the generic
container header), and it shall not be followed by a Zero-Length Packet packet (unless the
container itself is a multiple of wMaxPacketSize for the endpoint).

