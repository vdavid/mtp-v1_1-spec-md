## 2 Transport Requirements

MTP is intended to be transport-agnostic, that is, it is intended to function over multiple
underlying transports. However, this specification deals specifically with the USB
implementation of MTP – which assumes certain qualities in the USB transport in order
to function effectively.

### 2.1 Disconnection Events

An underlying transport should notify the application or service that is implementing
MTP initiator or responder functionality when a connected MTP device is disconnected
or otherwise rendered inaccessible at the transport level.

### 2.2 Error-Free Data Transmission

An underlying transport should guarantee error-free data transmission. This may be
provided by the transport itself, using error-correction codes or packet validation, or may
be ensured artificially on an inconsistent transport by the transport-specific
implementation definition.

### 2.3 Asynchronous Events

MTP devices are required to notify any connected devices immediately about any
changes in device status, device properties, object addition/deletion/modification or
storage status modifications, and so on. In order to provide that support, the underlying
transport must enable events to be communicated asynchronously with operations,
responses or data transfers.

### 2.4 Device Discovery and Enumeration

MTP does not attempt to define how devices are discovered or identified as supporting
MTP. This should be defined in a manner consistent with the underlying transport, and
may be performed in more than one way for a given transport.

### 2.5 Security and Authentication

MTP does not include any functionality for user authentication or data security. Any sort
of device validation or protection of data while in transit should be implemented in a
transport-specific manner.

### 2.6 Transport Independence

MTP was fundamentally defined as a transport independent protocol, while this
specification serves to define a standard USB implementation only. As a result, while this
specification shall be considered the definitive protocol reference, nothing in this
specification shall preclude the core protocol from operating over other transports. These
may include, but are not limited to, TCP/IP, Bluetooth, serial, or any other yet to be
defined transport mechanism.

### 2.7 MTP Device Enumeration

MTP device enumeration over USB requires no specific or proprietary USB string
descriptors. Some implementations prior to the publication of this specification may
require proprietary enumeration techniques; those are not specifically covered in this
document.

