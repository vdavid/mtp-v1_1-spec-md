## Appendix C Device Properties

### C.1 Device Property Summary Table

| MTP Name                       | MTP Datacode |
|--------------------------------|--------------|
| Undefined                      | 0x5000       |
| Battery Level                  | 0x5001       |
| Functional Mode                | 0x5002       |
| Image Size                     | 0x5003       |
| Compression Setting            | 0x5004       |
| White Balance                  | 0x5005       |
| RGB Gain                       | 0x5006       |
| F-Number                       | 0x5007       |
| Focal Length                   | 0x5008       |
| Focus Distance                 | 0x5009       |
| Focus Mode                     | 0x500A       |
| Exposure Metering Mode         | 0x500B       |
| Flash Mode                     | 0x500C       |
| Exposure Time                  | 0x500D       |
| Exposure Program Mode          | 0x500E       |
| Exposure Index                 | 0x500F       |
| Exposure Bias Compensation     | 0x5010       |
| DateTime                       | 0x5011       |
| Capture Delay                  | 0x5012       |
| Still Capture Mode             | 0x5013       |
| Contrast                       | 0x5014       |
| Sharpness                      | 0x5015       |
| Digital Zoom                   | 0x5016       |
| Effect Mode                    | 0x5017       |
| Burst Number                   | 0x5018       |
| Burst Interval                 | 0x5019       |
| Timelapse Number               | 0x501A       |
| Timelapse Interval             | 0x501B       |
| Focus Metering Mode            | 0x501C       |
| Upload URL                     | 0x501D       |
| Artist                         | 0x501E       |
| Copyright Info                 | 0x501F       |
| Synchronization Partner        | 0xD401       |
| Device Friendly Name           | 0xD402       |
| Volume                         | 0xD403       |
| SupportedFormatsOrdered        | 0xD404       |
| DeviceIcon                     | 0xD405       |
| Playback Rate                  | 0xD410       |
| Playback Object                | 0xD411       |
| Playback Container Index       | 0xD412       |
| Session Initiator Version Info | 0xD406       |
| Perceived Device Type          | 0xD407       |

### C.2 Device Property Descriptions

#### C.2.1 Undefined

This is not used

| Field name   | Field order | Size (bytes) | Datatype | Value              |
|--------------|-------------|--------------|----------|--------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5000             |
| Datatype     | 2           | 2            | UINT16   | 0x0000 (Undefined) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined     |
| DefaultValue | 4           |              |          | Device-Defined     |
| CurrentValue | 5           | 4            | UINT32   | Device-defined     |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined     |

#### C.2.2 Battery Level

The current battery level of a device is represented by the BatteryLevel property.

The battery level is indicated by an unsigned, read-only integer, and constrained by either
an Enumeration or Range of integers. The lowest value in the enumeration or range shall
indicate the state of having no battery power remaining, and the largest value shall
indicate a full battery. The enumeration or range of other allowed values indicate battery
levels at which a DevicePropChanged event shall triggered to indicate to the initiator that
that level has been reached, and must therefore not be chosen at too granular a level. A
value of 0 may used to indicate that the device has an alternate power source.

| Field name   | Field order | Size (bytes) | Datatype | Value          |
|--------------|-------------|--------------|----------|----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5001         |
| Datatype     | 2           | 2            | UINT16   | 0x0002 (UINT8) |
| Get/Set      | 3           | 1            | UINT8    | 0x00 (GET)     |
| DefaultValue | 4           |              |          | Device-Defined |
| CurrentValue | 5           | 4            | UINT32   | Device-defined |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined |

#### C.2.3 Functional Mode

The current functional mode of a device may be retrieved and manipulated using this
property.

All devices must default to a standard mode. Non-standard modes generally indicate
support for a different level of functionality, either a reduced set (such as when in a sleep
state) or an advanced mode (such as when running off an alternative power source). The
definition of non-standard modes is dependent on the device. Any change in capability
caused by a change in the device’s functional mode shall be described in an updated
DeviceInfo dataset, and this change shall be communicated using a DeviceInfoChanged
event (which shall always be sent when device capabilities change.)

This property is described using an Enumeration and is exposed outside of sessions in the
corresponding field in the DeviceInfo dataset.

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5002                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.4 Image Size

This property indicates and controls the height and width of images which are produced
or captured by the device.

The value of this property shall take the form of a Unicode, null-terminated string which
is structured as: “WxH”, where W represents the width of the image desired, and H
represents the height. Both the width and the height are represented by unsigned integers.
An example would be a value of “640x480” with a null terminator for the string, which
represents a width of 640 and a height of 480 pixels.

The allowed values of this property may be represented by either an Enumeration or a
Range form, depending on the capabilities of the device. Devices which can smoothly
scale image creation may choose to use a range form. A range form for this property
shall have as the minimum of the range a value which is the smallest image it can create,
and a maximum value of the largest image it can create, with a step value for each. An
example of a range implementation would be a Range form with a minimum value of
“1x1” (terminated by a null value), a maximum value of “1024x768” (terminated by a
null value) and a step of “1x1” (terminated by a null value) indicating that the image can
take any intermediate value.

If the device cannot process all possible image capture sizes in a range, it shall implement
this using an enumeration, which shall contain a list of all possible dimensions for
captured images.

Changing this property may cause the the Free Space In Objects field of the StorageInfo
dataset to be updated. When this occurs, the device is required to issue a
StorageInfoChanged event to indicate that this has occurred.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5003          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.5 Compression Setting

Objects captured by a device are generally not stored in their raw form, but are
compressed to save limited storage space. The Compression Setting property shall
indicate the level of compression in use by the device, and the range of values shall be as
close as possible to a linear represention of the perceived quality of the compressed
content. Smaller values indicate low quality and high compression, while large values
indicate high quality and low compression. This specification does not attempt to assign
specific values to this property with any absolute benchmarks, so this value is inherently
device and codec specific.

| Field name   | Field order | Size (bytes) | Datatype | Value          |
|--------------|-------------|--------------|----------|----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5004         |
| Datatype     | 2           | 2            | UINT16   | 0x0002 (UINT8) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined |
| DefaultValue | 4           |              |          | Device-Defined |
| CurrentValue | 5           | 4            | UINT32   | Device-defined |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined |

#### C.2.6 White Balance

This property identifies how the device weights the different colour channels.

Valid values include:

0x0000 Undefined

0x0001 Manual
The white balance is set directly by using the RGB Gain property, described in section
C.2.7 "RGB Gain", and is static until changed.

0x0002 Automatic
The device attempts to set the white balance using some kind of automatic mechanism.

0x0003 One-push automatic
The user must press the capture button while pointing the device at a white field, at which
time the device determines the white balance setting.

0x0004 Daylight
The device attempts to set the white balance to a value that is appropriate for use in
daylight conditions.

0x0005 Florescent
The device attempts to set the white balance to a value that is appropriate for use in
conditions with a florescent light source.

0x0006 Tungsten
The device attempts to set the white balance to a value that is appropriate for use in
conditions with a tungsten light source.

0x0007 Flash
The device attempts to set the white balance to a value that is appropriate for flash
conditions.

All other values with Bit 15 set to zero are reserved for PTP
All other values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor
extensions
All other values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5005                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.7 RGB Gain

This property is a Unicode, null-terminated string which represents the current RGB gain
setting of the device. This property is structured as “R:G:B”, where R represents the red
gain, G represents the green gain and B represents the blue gain. All the gain values are
represented by unsigned integers, up to a maximum of sixteen-bit unsigned integers. An
example value of “4:2:3” (terminated by a null value) indicates a gain value of 4 for red,
2 for green and 4 for blue. An example value of “2000:1000:1500” (terminated by a null
value) indicates a gain value of 2000 for red, 1000 for green and 1500 for blue. These
values are relative to each other, and therefore may take on any integer value less than
2^16.

This property may be constrained by either an Enumeration or a Range form. The
minimum value would represent the smallest numerical value (typically "1:1:1", null-
terminated). Using values of zero for a particular color channel would mean that color
channel would be dropped, so a value of "0:0:0" would result in images with all pixel
values being equal to zero. The maximum value would represent the largest value each
field may be set to (up to "65535:65535:65535", null-terminated), effectively determining
the setting's granularity by an order of magnitude per significant digit. The step value is
typically "1:1:1".

If a particular implementation desires the capability to enforce minimum and/or
maximum ratios, the green channel may be forced to a fixed value. An example of this
would be a minimum field of "1:1000:1", a maximum field of "20000:1000:20000" and a
step field of "1:0:1".

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5006          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.8 F-Number

This property identifies the aperture setting of the lens.

This property contains the F-number scaled by 100. When the device is set to capture
using an automatic exposure mode, the setting of this property may cause other properties
(such as Exposure Time and Exposure Index) to change. When that happens, the device
must issue a DevicePropChanged event to indicate the change. This property is typically
only able to be set when the device’s Exposure Program Mode property is set to Manual
or Aperture Priority.

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5007                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.9 Focal Length

This property corresponds to the 35mm equivalent focal length in millimeters multiplied
by 100.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5008          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.10 Focus Distance

This property contains an unsigned integer corresponding to the focus distance in
millimeters. A value of 0xFFFF indicates a setting greater than 655 meters.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5009          |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.11 Focus Mode

This property identifies the current focusing mode in use by the device for image capture.
Only the values in the following table are defined by this standard.

Valid values include:
0x0000 Undefined
0x0001 Manual
0x0002 Automatic
0x0003 Automatic Macro (close-up)
All values with Bit 15 set to zero are reserved for PTP
All values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor extensions
All values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x500A                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.12 Exposure Metering Mode

This property identifies the current exposure metering mode in use by the device for
image capture. Only the values in the following table are defined by this standard.

Valid values include:
0x0000 Undefined
0x0001 Average
0x0002 Center-weighted-average
0x0003 Multi-spot
0x0004 Center-spot
All values with Bit 15 set to zero are reserved for PTP
All values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor extensions
All values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x500B                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.13 Flash Mode

This property identifies the current flash mode in use by the device for image capture.
Only the values in the following table are defined by this standard.

Valid values include:
0x0000 Undefined
0x0001 Auto flash
0x0002 Flash off
0x0003 Fill flash
0x0004 Red-eye auto
0x0005 Red-eye fill
0x0006 External sync
All values with Bit 15 set to zero are reserved for PTP
All values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor extensions
All values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x500C                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.14 Exposure Time

This property identifies the current shutter speed of the device in seconds, scaled by
10,000. If the device is set to an automatic exposure program mode, setting this property
through SetDeviceProp may cause other properties to change. When that happens, the
device must issue a DevicePropChanged event to indicate the change. This property is
typically only able to be set when the device’s Exposure Program Mode property is set to
Manual or Shutter Priority.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x500D          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.15 Exposure Program Mode

This property allows the exposure program mode settings of the device, corresponding to
the "Exposure Program" tag within an EXIF or a TIFF/EP image file, to be constrained
by a list of allowed exposure program mode settings supported by the device.

Valid values include:
0x0000 Undefined
0x0001 Manual
0x0002 Automatic
0x0003 Aperture Priority
0x0004 Shutter Priority
0x0005 Program Creative (greater depth of field)
0x0006 Program Action (faster shutter speed)
0x0007 Portrait
All values with Bit 15 set to zero are reserved for PTP
All values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor extensions
All values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x500E                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.16 Exposure Index

This property can be used by an image capture device to emulate film speed settings on a
digital camera. The settings of this property correspond to the ISO designations
(ASA/DIN). Typically, a device supports discrete enumerated values, but continuous
control over a range is possible. A value of 0xFFFF corresponds to automatic ISO setting.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x500F          |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.17 Exposure Bias Compensation

This property allows the set point of an image capture device’s auto exposure control to
be identified and set.

This is a signed sixteen-bit integer, and represents a scaling factor.
A value of 0 will not change the factory set auto exposure level. The units of this
property represent “stops” scaled by a factor of 1000, which enables fractional stop
values. For example, a setting of 2000 indicates two stops of additional exposure (four
times more energy to the sensor and a brigher image). A setting of -1000 indicates one
stop less exposure (half the energy to the sensor and a darker image). The setting values
are expressed in APEX units (Additive system of Photographic Exposure). This property
may be constrained by an enumeration or a range.

This property is typically only used when the device has an Exposure Program Mode of
Manual.

| Field name   | Field order | Size (bytes) | Datatype | Value          |
|--------------|-------------|--------------|----------|----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5010         |
| Datatype     | 2           | 2            | UINT16   | 0x0003 (INT16) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined |
| DefaultValue | 4           |              |          | Device-Defined |
| CurrentValue | 5           | 4            | UINT32   | Device-defined |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined |

#### C.2.18 DateTime

This property identifies the current date and time settings of the device.

The value of this property follows the ISO standard format as described in ISO 8601
from the most significant number to the least significant number. This shall take the form
of a Unicode string in the format "YYYYMMDDThhmmss.s" where YYYY is the year,
MM is the month (01 to 12), DD is the day of the month (01 to 31), T is a constant
character, hh is the hours since midnight (00 to 23), mm is the minutes past the hour (00
to 59), and ss.s is the seconds past the minute, with the ".s" being optional tenths of a
second past the second.

This string can optionally be appended with Z to indicate UTC, or +/-hhmm to indicate
the time is relative to a time zone. Appending neither indicates the time zone is unknown.
This property shall not be constrained in the DevicePropDesc form fields, as the ISO
8601 specification already describes the allowed values.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5011          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.19 Capture Delay

This value describes the time delay which is to be be inserted between the triggering of
the image capture and the actual data capture.

This value is represented by an unsigned integer, which represents the capture delay in
milliseconds. This property does not describe the time between multiple frames of a burst
capture or capture time of a time-lapse capture, which are described by the Burst Interval
and Timelapse Interval properties respectively. In those cases it would still serve as an
initial delay before the first image in the series was captured, independent of the time
between frames. When no capture delay is desired, this property shall be set to zero.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5012          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.20 Still Capture Mode

This property identifies the type of still capture which will be performed by an image
capture initiation.
Valid values include:
0x0000 Undefined
0x0001 Normal
0x0002 Burst
0x0003 Timelapse
All values with Bit 15 set to zero are reserved for PTP
All values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor extensions
All values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5013                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.21 Contrast

This property identifies the perceived contrast of images captured by the device

This property be constrained by either an enumeration or range, with actual values being
relative. The smallest value allowed by the range or enumeration form represents the least
contrast, while the largest value represents the most contrast. A value in the middle of the
range shall be used to represent the normal (default) contrast.

| Field name   | Field order | Size (bytes) | Datatype | Value          |
|--------------|-------------|--------------|----------|----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5014         |
| Datatype     | 2           | 2            | UINT16   | 0x0002 (UINT8) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined |
| DefaultValue | 4           |              |          | Device-Defined |
| CurrentValue | 5           | 4            | UINT32   | Device-defined |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined |

#### C.2.22 Sharpness

This property identifies the perceived sharpness of images captured by this device.

This property may be constrained by either an enumeration or a range. The minimum
value allowed by the range or enumeration form represents the least amount of sharpness,
while the largest value represents the most sharpness. A value in the middle of the range
shall be used to represent normal (default) sharpness.

| Field name   | Field order | Size (bytes) | Datatype | Value          |
|--------------|-------------|--------------|----------|----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5015         |
| Datatype     | 2           | 2            | UINT16   | 0x0002 (UINT8) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined |
| DefaultValue | 4           |              |          | Device-Defined |
| CurrentValue | 5           | 4            | UINT32   | Device-defined |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined |

#### C.2.23 Digital Zoom

This property identifies the effective digital zoom which will be applied to an image
capture device’s acquired image, scaled by a factor of 10. When no digital zoom is
applied, the value of this property shall be equal to 10. A value of 20 indicates a zoom by
a factor of 2 (2X), where only ¼ of the possible scene is captured by the camera. This
property may be constrained by either an enumeration or a range, with the lowest value
indicating the minimum digital zoom (generally 10) and the largest value indicating the
maximum digital zoom which the device can apply.

| Field name   | Field order | Size (bytes) | Datatype | Value          |
|--------------|-------------|--------------|----------|----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5016         |
| Datatype     | 2           | 2            | UINT16   | 0x0002 (UINT8) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined |
| DefaultValue | 4           |              |          | Device-Defined |
| CurrentValue | 5           | 4            | UINT32   | Device-defined |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined |

#### C.2.24 Effect Mode

This property allows the image capture device to specify special image acquisition
modes.

Valid values include:
0x0000 Undefined
0x0001 Standard (color)
0x0002 Black & White
0x0003 Sepia
All values with Bit 15 set to zero are reserved for PTP
All values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor extensions
All values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5017                |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.25 Burst Number

This property identifies the number of images which the device will capture upon the
initiation of a burst capture operation.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5018          |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.26 Burst Interval

This property identifies the time delay in milliseconds between subsequent image capture
operations in a burst capture operation.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x5019          |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.27 Timelapse Number

This property indicates the number of images which will be captured when a time-lapse
capture is begun.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x501A          |
| Datatype     | 2           | 2            | UINT16   | 0x0004 (UINT16) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.28 Timelapse Interval

This property indicates the time delay in milliseconds between captures of a time-lapse
capture operation.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x501B          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | Device-Defined  |

#### C.2.29 Focus Metering Mode

This property identifies the automatic-focus mechanism currently in use by the device.

All allowed values of this property shall be identified in an enumeration form of the
DevicePropDesc dataset.

Valid values include:
0x0000 Undefined
0x0001 Center-spot
0x0002 Multi-spot
All values with Bit 15 set to zero are reserved for PTP
All values with Bit 15 set to 1 and Bit 14 set to 0 are open for MTP vendor extensions
All values with Bit 15 set to 1 and Bit 14 set to 1 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0x501C                |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32)       |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.30 Upload URL

This property describes an Internet URL (Universal Resource Locator) which the initiator
may use to upload objects after they have been acquired from the device.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x501D          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.31 Artist

This property contains the name of the owner/operator of this device, and shall be used
by the device to populate the “Artist” property in any objects created on this device.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x501E          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.32 Copyright Info

This property contains the copyright notification which shall be used to populate the
“Copyright” property on any objects created by this device.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0x501F          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.33 Synchronization Partner

This property gives a human-readable description of a synchronization partner for a
device. A synchronization partner can be either another device, a software application on
a device, or a server over the network. Typically, for a device to PC connection, this is
the name of the PC.

This property may also be used by a synchronization process to recognize that it is the
partner for this device, so that it may modify its behavior appropriately, but in doing so,
should assume that the property will need to be human-readable. This is because this
property may be exposed in UI in an operating system.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD401          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.34 Device Friendly Name

This property gives a human-readable description of the device, for use in an initiating
device’s user interface.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD402          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.35 Volume

This identifies (and is used to set) the current volume of the device, and is an unsigned
32-bit integer. The allowed values of this property device shall be identified by a range
form defined in the DevicePropDesc dataset defining this property. Values for this
property are always based at 0, and a value of 0 indicates that the device is muted.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD403          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x01 Range form |

#### C.2.36 SupportedFormatsOrdered

This property identifies whether a device is indicating its supported production &
consumption object formats in order of preference.

Valid values include:
0x00 Unordered
0x01 Ordered
All values with Bit 7 set to 1 are open for MTP vendor extensions
All values with Bit 7 set to 0 are reserved for MTP

| Field name   | Field order | Size (bytes) | Datatype | Value          |
|--------------|-------------|--------------|----------|----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD404         |
| Datatype     | 2           | 2            | UINT16   | 0x0002 (UINT8) |
| Get/Set      | 3           | 1            | UINT8    | 0x00 (GET)     |
| DefaultValue | 4           |              |          | Device-Defined |
| CurrentValue | 5           | 4            | UINT32   | Device-defined |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None      |

#### C.2.37 DeviceIcon

This property identifies a .ICO icon object that represents the device to an initiator. The
specification for a .ICO is located here: http://msdn2.microsoft.com/en-
us/library/ms997538.aspx (page title: “Icons in Win32”).

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD405          |
| Datatype     | 2           | 2            | UINT16   | 0x4002 (AUINT8) |
| Get/Set      | 3           | 1            | UINT8    | Device-Defined  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.38 Playback Rate

This identifies the current speed of playback, identified linearly. It is a signed 32-bit
integer, which identifies the speed in thousandths. Thus, a value of 1000 indicates that
the playback shall proceed at full speed. A value of 500 indicates that playback shall be
at half-speed. A value of -1000 indicates that playback shall be in reverse at full speed.
A value of 0 indicates that the device is paused.

A complete list of allowed playback rates for an object shall be contained in an
enumeration of allowed values defined in the DevicePropDesc dataset defining this
property. This list shall always include the values 1000 and 0.

| Field name   | Field order | Size (bytes) | Datatype | Value                 |
|--------------|-------------|--------------|----------|-----------------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD410                |
| Datatype     | 2           | 2            | UINT16   | 0x0005 (INT32)        |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)        |
| DefaultValue | 4           |              |          | Device-Defined        |
| CurrentValue | 5           | 4            | UINT32   | Device-defined        |
| FormFlag     | 6           | 1            | UINT8    | 0x02 Enumeration form |

#### C.2.39 Playback Object

This identifies the object currently being played back on the device, identified by Object
Handle. This property has two special values. A value of 0x00000000 indicates that the
device is currently stopped, and no media file is being consumed.

Devices which support playlist or album objects shall allow this property to contain a
reference to an album or playlist. If a device supports these object types, as well as
playback control, it must also support the Playback Container Index Device Property. If
this property contains an album or playlist object, it indicates that the device is currently
playing back the contents of that album or playlist.

Whenever the object being played back is updated on the device (due to the previous
object finishing playback, user input on the device, or active control on another active
session) the device shall indicate this by initiating a DevicePropChanged event for this
property.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD411          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.40 Playback Container Index

When playing content, the Playback Object device property may contain a container
object (album, playlist, etc.) rather than the actual object being consumed. In this case, it
is important to expose the specific object in that playback container which is being
consumed. The object being played is identified by its index within Object References
array of that playback container, and that index is contained in this property. Recall that
arrays in MTP are zero-based (so a value of 0x00000000 in this property indicates that
the first ObjectHandle in the Object References array is being consumed).
If the Playback Object does not represent a container object, this property shall always
contain a value of 0x00000000.

When the playback container index changes, such as during a song change, a
DevicePropChanged event shall be sent to notify the initiator.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD412          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.41 Playback Position

This identifies the current time offset of the object currently being played back in
milliseconds. During playback, this property will change frequently, and those changes
shall not result in DevicePropChanged events unless they are caused by actions external
to both the current session and the regular playback of the object.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD413          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)  |
| DefaultValue | 4           |              |          | Device-Defined  |
| CurrentValue | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

#### C.2.42 Session Initiator Version Info

This property describes the version information of the session initiator. The value of this
property shall take the form of a Unicode, null-terminated string that is formatted as the
User Agent string in HTTP 1.1 spec (RFC 2068). The initiator shall set this device
property directly after GetDeviceInfo is called. This will give the device a chance to
adjust behavior before additional operations occur within the session. GetDeviceInfo is
called to determine if this property is supported by the device.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD406          |
| Datatype     | 2           | 2            | UINT16   | 0xFFFF (STRING) |
| Get/Set      | 3           | 1            | UINT8    | 0x01 (Get/Set)  |
| DefaultValue | 4           |              |          | Device-Defined  |
| GroupCode    | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

The following example shows a Windows OS version and a class driver version.

Example: “Windows/6.0.5330.0 MTPClassDriver/6.0.5330.0”

#### C.2.43 Perceived Device Type

This property allows an Initiator to determine the device type of the Responder, as
perceived by the user. This property is intended to be used by the Initiator to graphically
represent the Responder; a Device Icon (0xD405) is intended to be preferred over
Perceived Device Type. Perceived Device Type may also be used to represent device
capabilities or functionality.

| Value      | Perceived Device Type                                     |
|------------|-----------------------------------------------------------|
| 0x00000000 | Generic                                                   |
| 0x00000001 | Still Image/Video Camera                                  |
| 0x00000002 | Media (Audio/Video) Player                                |
| 0x00000003 | Mobile Handset                                            |
| 0x00000004 | Video Player                                              |
| 0x00000005 | Personal Information Manager / Personal Digital Assistant |
| 0x00000006 | Audio Recorder                                            |

All values with Bit 15 set to zero are reserved for MTP.
All values with Bit 15 set to 1 are open for MTP vendor extensions.

| Field name   | Field order | Size (bytes) | Datatype | Value           |
|--------------|-------------|--------------|----------|-----------------|
| PropertyCode | 1           | 2            | UINT16   | 0xD407          |
| Datatype     | 2           | 2            | UINT16   | 0x0006 (UINT32) |
| Get/Set      | 3           | 1            | UINT8    | 0x00 (GET)      |
| DefaultValue | 4           |              |          | Device-Defined  |
| GroupCode    | 5           | 4            | UINT32   | Device-defined  |
| FormFlag     | 6           | 1            | UINT8    | 0x00 None       |

