# Cover
===== page_number= i, page_type= toc ==___

<!-- Embeded_Image 1, coordinate:(312,320,685,410) -->

**NVM Express®**  
**Base Specification**

**Revision 2.3**  
**July 31th, 2025**

*Please send comments to* [info@nvmexpress.org](mailto:info@nvmexpress.org)

---

i


![Embeded_Image 1](restored_images/Embeded_Image_1.png)
**Embeded_Image 1**


---

# 1 Introduction



---

## 1.1 Overview

The NVM Express® (NVMe®) interface allows a host to communicate with a non-volatile memory subsystem (NVM subsystem). This interface is optimized for all storage solutions, attached using a variety of transports including PCI Express®, Ethernet, InfiniBand™, and Fibre Channel. The mapping of extensions defined in this document to a specific NVMe Transport are defined in an NVMe Transport binding specification. The NVMe Transport binding specification for Fibre Channel is defined in INCITS 556 Fibre Channel – Non-Volatile Memory Express - 2 (FC-NVMe-2).

For an overview of changes from revision 2.2 to revision 2.3 and the description of the new features, including mandatory requirements for a controller to comply with revision 2.3, refer to https://nvmexpress.org/specification/nvm-express-revision-changes.



---

## 1.1.1 NVM Express® Specification Family

Figure 1 shows the relationship of the NVM Express specifications to each other within the NVMe® family of specifications.

<!-- Figure 1, coordinate:(115,392,900,645) -->

The NVM Express specification family structure shown in Figure 1 is intended to show the applicability of NVM Express specifications to each other, not a hierarchy, protocol stack, or system architecture.

The NVM Express Base Specification (i.e., this specification) defines a protocol for a host to communicate with an NVM subsystem over a variety of memory-based transports and message-based transports.

The NVM Express Management Interface (NVMe-MI) Specification defines an optional management interface for all NVM Express Subsystems.

NVM Express I/O Command Set specifications define data structures, features, log pages, commands, and status values that extend the NVM Express Base Specification.

NVM Express Transport specifications define the binding of the NVMe protocol including controller properties to a specific transport.

The NVM Express Boot Specification defines constructs and guidelines for booting from NVM Express interfaces.
NVM Express® Base Specification, Revision 2.3



![Figure 1](restored_images/Figure_1.png)
**Figure 1**


---

## 1.2 Scope

This specification defines a set of properties and commands that comprise the interface required for communication with a controller in an NVM subsystem. These properties are to be implemented by an instance of a controller using a specific NVMe Transport. This specification also defines common aspects of the NVMe I/O Command Sets that may be supported by a controller.

There are three types of controllers with different capabilities (refer to section 3.1.3):

a) I/O controllers;

b) Discovery controllers; and

c) Administrative controllers.

In this document the generic term controller is often used instead of enumerating specific controller types when applicable controller types may be determined from the context.



---

## 1.3 Outside of Scope

The property interface and command set are specified apart from any usage model for the NVM, but rather only specifies the communication interface to the NVM subsystem. Thus, this specification does not specify whether the NVM subsystem is used as a solid-state drive, a main memory, a cache memory, a backup memory, a redundant memory, etc. Specific usage models are outside the scope, optional, and not licensed.

This specification defines requirements and behaviors that are implementation agnostic. The implementation of these requirements and behaviors are outside the scope of this specification. For example, an NVM subsystem that follows this specification may be implemented by an SSD that attaches directly to a fabric, a device that translates between a fabric and a PCIe NVMe SSD, or software running on a general-purpose server.

This interface is specified above any non-volatile media management, like wear leveling. Erases and other management tasks for NVM technologies like NAND are abstracted.

This specification does not contain any information on caching algorithms or techniques.

The implementation or use of other published specifications referred to in this specification, even if required for compliance with the specification, are outside the scope of this specification (e.g., PCI, PCI Express, and PCI-X). This includes published specifications for fabrics and other technologies referred to by this document or any NVMe Transport binding specification.



---

## 1.4 Conventions



---

### 1.4.1 Keywords

Several keywords are used to differentiate between different levels of requirements.

#### 1.4.1.1 mandatory

A keyword indicating items to be implemented as defined by this specification.

#### 1.4.1.2 may

A keyword that indicates flexibility of choice with no implied preference.

#### 1.4.1.3 obsolete

A keyword indicating functionality that was defined in a previous version of the NVM Express specification and that has been removed from this specification.

2
===== page_number= 3, page_type= body ====

## 1.4.1.4 optional

A keyword that describes features that are not required by this specification. However, if any optional feature defined by the specification is implemented, the feature shall be implemented in the way defined by the specification.



---

## 1.4.1.5 R

“R” is used as an abbreviation for “reserved” when the figure or table does not provide sufficient space for the full word “reserved”.

## 1.4.1.6 reserved

A keyword referring to bits, bytes, words, fields, and opcode values that are set-aside for future standardization. Their use and interpretation may be specified by future extensions to this or other specifications. A reserved bit, byte, word, field, property, or register shall be cleared to 0h, or in accordance with a future extension to this specification. The recipient of a command or a controller property write is not required to check reserved bits, bytes, words, or fields. Receipt of reserved coded values in defined fields in commands shall be reported as an error. Writing a reserved coded value into a controller property field produces undefined results.

## 1.4.1.7 shall

A keyword indicating a mandatory requirement. Designers are required to implement all such mandatory requirements to ensure interoperability with other products that conform to the specification.

## 1.4.1.8 should

A keyword indicating flexibility of choice with a strongly preferred alternative. Equivalent to the phrase “it is recommended”.



---

## 1.4.2 Numerical Descriptions

A 0’s based value is a numbering scheme in which the number 0h represents a value of 1h, 1h represents 2h, 2h represents 3h, etc. In this numbering scheme, there is no method to represent the value of 0h. Values in this specification are 1-based (i.e., the number 1h represents a value of 1h, 2h represents 2h, etc.) unless otherwise specified.

Size values are shown in binary units or decimal units. The symbols used to represent these values are as shown in Figure 2.

<!-- Figure 2, coordinate:(255,625,745,825) -->

**Figure 2: Decimal and Binary Units**

| Decimal | Binary |
|---------|--------|
| **Symbol** | **Power (base-10)** | **Symbol** | **Power (base-2)** |
| kilo / k | 10³ | kibi / Ki | 2¹⁰ |
| mega / M | 10⁶ | mebi / Mi | 2²⁰ |
| giga / G | 10⁹ | gibi / Gi | 2³⁰ |
| tera / T | 10¹² | tebi / Ti | 2⁴⁰ |
| peta / P | 10¹⁵ | pebi / Pi | 2⁵⁰ |
| exa / E | 10¹⁸ | exbi / Ei | 2⁶⁰ |
| zetta / Z | 10²¹ | zebi / Zi | 2⁷⁰ |
| yotta / Y | 10²⁴ | yobi / Yi | 2⁸⁰ |

The ^ operator is used to denote the power to which that number, symbol, or expression is to be raised.

Some parameters are defined as an ASCII string. ASCII strings shall contain only code values (i.e., byte values or octet values) 20h through 7Eh. For the string “Copyright”, the character “C” is the first byte, the character “o” is the second byte, etc. ASCII strings are left justified. If padding is necessary, then the string
===== page_number= 4, page_type= body ====

shall be padded with spaces (i.e., ASCII character 20h) to the right unless the string is specified as null-terminated.

Some parameters are defined as a UTF-8 string. UTF-8 strings shall contain only byte values (i.e., octet values) 20h through 7Eh, 80h through BFh, and C2h through F4h (refer to sections 1 to 3 of RFC 3629). For the string “Copyright”, the character “C” is the first byte, the character “o” is the second byte, etc. UTF-8 strings are left justified. If padding is necessary, then the string shall be padded with spaces (i.e., ASCII character 20h, Unicode character U+0020) to the right unless the string is specified as null-terminated.

If padding is necessary for a field that contains a null-terminated string then the field should be padded with nulls (i.e., ASCII character 00h, Unicode character U+0000) to the right of the string.

A hexadecimal ASCII string is an ASCII string that uses a subset of the code values: “0” to “9”, “A” to “F” uppercase, and “a” to “f” lowercase.

Hexadecimal (i.e., base 16) numbers are written with a lower case “h” suffix (e.g., 0FFFh, 80h). Hexadecimal numbers larger than eight digits are represented with an underscore character dividing each group of eight digits (e.g., 1E_DEADBEEFh).

Binary (i.e., base 2) numbers are written with a lower case “b” suffix (e.g., 1001b, 10b). Binary numbers larger than four digits are written with an underscore character dividing each group of four digits (e.g., 1000_0101_0010b).

All other numbers are decimal (i.e., base 10). A decimal number is represented in this specification by any sequence of digits consisting of only the Western-Arabic numerals 0 to 9 not immediately followed by a lower-case b or a lower-case h (e.g., 175). This specification uses the following conventions for representing decimal numbers:

a) the decimal separator (i.e., separating the integer and fractional portions of the number) is a period;  
b) the thousands separator (i.e., separating groups of three decimal digits in a portion of the number) is a comma;  
c) the thousands separator is used in only the integer portion of a number and not the fractional portion of a number; and  
d) the decimal representation for a year does not include a comma (e.g., 2019 instead of 2,019).
===== page_number= 5, page_type= body ====

# NVM Express® Base Specification, Revision 2.3



| Decimal | Binary |
|---------|--------|
| **Symbol** | **Power (base-10)** | **Symbol** | **Power (base-2)** |
| kilo / k | 10³ | kibi / Ki | 2¹⁰ |
| mega / M | 10⁶ | mebi / Mi | 2²⁰ |
| giga / G | 10⁹ | gibi / Gi | 2³⁰ |
| tera / T | 10¹² | tebi / Ti | 2⁴⁰ |
| peta / P | 10¹⁵ | pebi / Pi | 2⁵⁰ |
| exa / E | 10¹⁸ | exbi / Ei | 2⁶⁰ |
| zetta / Z | 10²¹ | zebi / Zi | 2⁷⁰ |
| yotta / Y | 10²⁴ | yobi / Yi | 2⁸⁰ |


---

## 1.4.3 Byte, Word, and Dword Relationships

Figure 3 illustrates the relationship between bytes, words and dwords. A qword (quadruple word) is a unit of data that is four times the size of a word; it is not illustrated due to space constraints. Unless otherwise specified, this specification specifies data in a little endian format.

### Figure 3: Byte, Word, and Dword Relationships

<!-- Figure 3, coordinate:(110,210,840,740) -->

The figure shows:

- **Byte**: 8 bits, labeled 7 to 0 (bit 7 is MSB, bit 0 is LSB).
- **Word**: 16 bits, labeled 15 to 0. Shown as two bytes: byte 1 (bits 15-8) and byte 0 (bits 7-0). The bit labels above the boxes are: 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 (for bits 15-0) and below: 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0.
- **Dword**: 32 bits, labeled 31 to 0. Shown as two words: word 1 (bits 31-16) and word 0 (bits 15-0). Also shown as four bytes: byte 3 (bits 31-24), byte 2 (bits 23-16), byte 1 (bits 15-8), byte 0 (bits 7-0). The bit labels above the boxes are: 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 (for bits 31-0) and below: 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0.



![Figure 3](restored_images/Figure_3.png)
**Figure 3**


---

## 1.5 Definitions

### 1.5.1 admin label

An admin label is an administratively configured ASCII or UTF-8 string (refer to section 1.4.2) that may be used to help identify specific NVMe entities (i.e., Hosts, NVM subsystems and namespaces). An admin label is capable of describing the entity’s physical location, DNS name or other information.

### 1.5.2 admin label ASCII

An ASCII string. Refer to section 1.4.2 for ASCII string requirements. Refer to section 1.5.1 for admin label usage.
===== page_number= 6, page_type= body ====

### 1.5.3 admin label UTF-8
A UTF-8 string. Refer to section 1.4.2 for UTF-8 string requirements. Refer to section 1.5.1 for admin label usage.



---

### 1.5.4 Admin Queue
The Admin Queue is the Submission Queue and Completion Queue with identifier 0. The Admin Submission Queue and corresponding Admin Completion Queue are used to submit administrative commands and receive completions for those administrative commands, respectively.  
The Admin Submission Queue is uniquely associated with the Admin Completion Queue.



---

### 1.5.5 Administrative controller
A controller that exposes capabilities that allow a host to manage an NVM subsystem. An Administrative controller does not implement I/O Queues, provide access to data or metadata associated with user data on a non-volatile storage medium, or support namespaces attached to the Administrative controller (i.e., there are never any active NSIDs).

### 1.5.6 allocated namespace
A namespace that is associated with an allocated NSID.



---

### 1.5.7 Allowed Host List
A list of hosts (identified by Host NQN and Host Identifier) present in each Exported NVM Subsystem that are granted access to the Exported NVM Subsystem via an Exported Port.

### 1.5.8 arbitration burst
The maximum number of commands that may be fetched by an arbitration mechanism at one time from a Submission Queue.

### 1.5.9 arbitration mechanism
The method used to determine which Submission Queue is selected next to fetch commands for execution by the controller. Refer to section 3.4.4.

### 1.5.10 association
An exclusive communication relationship between a particular controller and a particular host that encompasses the Admin Queue and all I/O Queues of that controller.

### 1.5.11 audit
The process of accessing media to determine correct operation of a sanitize operation. Refer to section 8.1.26 and to ISO/IEC 27040.

### 1.5.12 authentication commands
Used to refer to Fabrics Authentication Send or Authentication Receive commands.

### 1.5.13 cache
A data storage area used by the NVM subsystem, that is not accessible to a host, and that may contain a subset of user data stored in the non-volatile storage media or may contain user data that is not committed to non-volatile storage media.

### 1.5.14 candidate command
A candidate command is a submitted command which has been transferred into the controller and the controller deems ready for processing.
===== page_number= 7, page_type= body ====

NVM Express® Base Specification, Revision 2.3

### 1.5.15 capsule
An NVMe unit of information exchange used in NVMe over Fabrics. A capsule contains a command or response and may optionally contain command/response data and SGLs.



---

### 1.5.16 Centralized Discovery controller (CDC)
A Discovery controller that reports discovery information registered by Direct Discovery controllers and hosts.



---

### 1.5.17 Channel
A Channel represents a communication path between the controller and one or more Media Units in an NVM subsystem.

### 1.5.18 command completion
A command is completed when the controller has completed processing the command, has updated status information in the completion queue entry, and has posted the completion queue entry to the associated Completion Queue.

### 1.5.19 command submission
For memory-based transport model (e.g., PCIe) implementations, a command is submitted when a Submission Queue Tail Doorbell write has completed that moves the Submission Queue Tail Pointer value past the Submission Queue slot in which the command was placed.

For message-based transport model (e.g., NVMe over Fabrics) implementations, a command is submitted when a host adds a capsule to a Submission Queue.



---

### 1.5.20 Configurable Device Personality (CDP)
The mechanism for a host to change an NVM subsystem configuration using personalities. Refer to section 8.1.6.

### 1.5.21 controller
A controller is the interface between a host and an NVM subsystem. There are three types of controllers:
a) I/O controllers;
b) Discovery controllers; and
c) Administrative controllers.

A controller executes commands submitted by a host on a Submission Queue and posts a completion on a Completion Queue. All controllers implement one Admin Submission Queue and one Admin Completion Queue. Depending on the controller type, a controller may also implement one or more I/O Submission Queues and I/O Completion Queues. When PCI Express is used as the transport, then a controller is a PCI Express function.



---

### 1.5.22 Controller Reset
Host modification of the CC property that clears CC.EN from ‘1’ to ‘0’ (refer to section 3.7.2.1).



---

### 1.5.23 Directive
A method of information exchange between a host and either an NVM subsystem or a controller. Information may be transmitted using the Directive Send and Directive Receive commands. A subset of I/O commands may include a Directive Type field and a Directive Specific field to communicate more information that is specific to the associated I/O command. Refer to section 8.1.9.
===== page_number= 8, page_type= body ====



---

### 1.5.24 Direct Discovery controller (DDC)
A Discovery controller that is capable of registering discovery information with a Centralized Discovery controller.



---

### 1.5.25 Discovery controller
A controller that exposes capabilities that allow a host to retrieve a Discovery Log Page. A Discovery controller does not implement I/O Queues or provide access to a non-volatile storage medium. Refer to section 3.1.3.3.

### 1.5.26 discovery information
Information about a host or NVM subsystem that is used for discovery (e.g., NVMe Transport address, NQN, etc.).



---

### 1.5.27 Discovery Service
An NVM subsystem that supports Discovery controllers only. A Discovery Service shall not support a controller that exposes namespaces.

### 1.5.28 dispersed namespace
A shared namespace that may be concurrently accessed by controllers in two or more NVM subsystems (refer to section 8.1.10).

### 1.5.29 dynamic controller
The controller is allocated on demand with no state (e.g., Feature settings) preserved from prior associations.



---

### 1.5.30 Domain
A domain is the smallest indivisible unit that shares state (e.g., power state, capacity information).

### 1.5.31 embedded management controller
An embedded management controller is a Management Controller (refer to the NVM Express Management Interface Specification) that provides an external management interface (e.g., Redfish®), typically implemented via commands to the Management Endpoint.

### 1.5.32 emulated controller
An NVM Express controller that is defined in software. An emulated controller may or may not have an underlying physical NVMe controller (e.g., physical PCIe function).



---

### 1.5.33 Endurance Group
A portion of non-volatile storage in the NVM subsystem whose endurance is managed as a group. Refer to section 3.2.3.



---

### 1.5.34 Entry Key
A set of discovery information entry fields that allow for the unique identification of each discovery information entry registered with the CDC or DDC. Refer to the Entry Key Type (EKTYPE) field.



---

### 1.5.35 Exported Namespace
A namespace in an Exported NVM Subsystem.



---

### 1.5.36 Exported NVM Resources
NVM resources created to enable remote access to physical NVM resources that includes:
===== page_number= 9, page_type= body ====

NVM Express® Base Specification, Revision 2.3

a) Exported NVM Subsystems;  
b) Exported Namespaces; and  
c) Exported Ports.



---

### 1.5.37 Exported NVM Subsystem  
A logical NVM subsystem that exports underlying NVM resources and that:  
a) contains zero or more Exported Namespaces;  
b) contains zero or more controllers;  
c) contains zero or more Exported Ports; and  
d) may contain an Allowed Host List.



---

### 1.5.38 Exported Port  
A port used to export an NVMe subsystem over a specific fabrics transport and represented by an Exported Port ID.



---

### 1.5.39 Exported Port ID  
A port identifier used to specify an Exported Port.

### 1.5.40 fabric (network fabric)  
A network topology in which nodes pass data to each other.



---

### 1.5.41 Fabric Zoning  
A technique to specify access control configurations between hosts and NVM subsystems.

### 1.5.42 firmware/boot partition image update command sequence  
The sequence of one or more Firmware Image Download commands that download a firmware image or a boot partition image followed by a Firmware Commit command that commits that downloaded image to a firmware slot or a boot partition.

### 1.5.43 firmware slot  
A firmware slot is a location in a domain used to store a firmware image. The domain stores from one to seven firmware images. Controllers in the same domain share the same firmware slots.

### 1.5.44 host  
An entity that interfaces to an NVM subsystem through one or more controllers and submits commands to Submission Queues and retrieves command completions from Completion Queues.

### 1.5.45 host-accessible memory  
Memory that the host is able to access (e.g., host memory, Controller Memory Buffer (CMB), Persistent Memory Region (PMR)).

### 1.5.46 host management agent  
A host management agent is a part of the host that provides an external management interface (e.g., Redfish) to external managers, typically via Admin commands to the controller (refer to the NVM Express Management Interface Specification).

### 1.5.47 host memory  
Memory that may be read and written by both a host and a controller and that is not exposed by a controller (i.e., Controller Memory Buffer or Persistent Memory Region). Host memory may be implemented inside or outside a host (e.g., a memory region exposed by a device that is neither the host nor controller).
===== page_number= 10, page_type= body ====

### 1.5.48 idempotent command
A command that produces the same end state in the NVM subsystem and returns the same results if that command is resubmitted one or more times with no intervening commands. Refer to section 9.6.3.1.



---

### 1.5.49 Identify Controller data structures
All controller data structures that are able to be retrieved via the Identify command:
- Identify Controller data structure (i.e., CNS 01h); and
- each of the I/O Command Set specific Identify Controller data structure (i.e., CNS 06h).



---

### 1.5.50 Identify Namespace data structures
All namespace data structures that are able to be retrieved via the Identify command:
- Identify Namespace data structures (i.e., CNS 00h, CNS 09h, and CNS 11h);
- I/O Command Set Independent Identify Namespace data structures (i.e., CNS 08h and CNS 1Fh); and
- I/O Command Set specific Identify Namespace data structures (i.e., CNS 05h, CNS 0Ah, and CNS 1Bh).



---

### 1.5.51 I/O command
An I/O command is a command submitted to an I/O Submission Queue.



---

### 1.5.52 I/O Completion Queue
An I/O Completion Queue is a Completion Queue that is used to indicate command completions and is associated with one or more I/O Submission Queues.



---

### 1.5.53 I/O controller
A controller that implements I/O queues and is intended to be used to access a non-volatile storage medium.



---

### 1.5.54 I/O Submission Queue
An I/O Submission Queue is a Submission Queue that is used to submit I/O commands for execution by the controller (e.g., Read command and Write command for the NVM Command Set).



---

### 1.5.55 Media Unit
A Media Unit represents a component of the underlying media in an NVM subsystem. Endurance Groups are composed of Media Units.

### 1.5.56 memory-based controller
A controller that supports a memory-based transport model (e.g., a PCIe implementation).

### 1.5.57 message-based controller
A controller that supports a message-based transport model (e.g., a Fabrics implementation).

### 1.5.58 metadata
Metadata is contextual information related to formatted user data (e.g., a particular LBA of data as defined in the NVM Express NVM Command Set Specification). The host may include metadata to be stored by the NVM subsystem if storage space is provided by the controller. Refer to the applicable NVM Express I/O Command Set specification for details.



---

### 1.5.59 MMC
A Migration Management Controller. Refer to section 8.1.13.
===== page_number= 11, page_type= body ====

NVM Express® Base Specification, Revision 2.3



---

### 1.5.60 MMH
A Migration Management Host. Refer to section 8.1.13.



---

### 1.5.61 MMHD
A Migration Management Host associated with a Migration Management Controller in a Destination NVM Subsystem. Refer to section 8.1.13.



---

### 1.5.62 MMHS
A Migration Management Host associated with a Migration Management Controller in a Source NVM Subsystem. Refer to section 8.1.13.

### 1.5.63 namespace
A set of resources that may be directly accessed by a host (e.g., formatted non-volatile storage).

### 1.5.64 namespace ID (NSID)
An identifier used by a controller to provide access to a namespace or the name of the field in the SQE that contains the namespace identifier (refer to Figure 92). Refer to section 3.2.1 for the definitions of valid NSID, invalid NSID, active NSID, inactive NSID, allocated NSID, and unallocated NSID.

### 1.5.65 namespace sanitize operation
A sanitize operation with a sanitization target of a namespace.



---

### 1.5.66 NVM
NVM is an acronym for non-volatile memory.



---

### 1.5.67 NVM Set
A portion of NVM from an Endurance Group. Refer to section 3.2.2.



---

### 1.5.68 NVM subsystem
An NVM subsystem includes one or more domains, one or more controllers, zero or more namespaces, and one or more ports. An NVM subsystem may include a non-volatile storage medium and an interface between the controller(s) in the NVM subsystem and non-volatile storage medium.



---

### 1.5.69 NVM subsystem port
An NVMe over Fabrics protocol interface between an NVM subsystem and a fabric. An NVM subsystem port is a collection of one or more physical fabric interfaces that together act as a single interface.



---

### 1.5.70 NVM subsystem sanitize operation
A sanitize operation with a sanitization target of the NVM subsystem.



---

### 1.5.71 NVMe over Fabrics
An implementation of the NVM Express interface that complies with either the message-only transport model or the message/memory transport model (refer to Figure 4 and section 2.2).



---

### 1.5.72 NVMe Transport
A protocol layer that provides reliable delivery of data, commands, and responses between a host and an NVM subsystem. The NVMe Transport layer is layered on top of the fabric. It is independent of the fabric physical interconnect and low-level fabric protocol layers.

<!-- Figure 92, coordinate:(0,0,0,0) -->  
<!-- Figure 4, coordinate:(0,0,0,0) -->
===== page_number= 12, page_type= body ====



---

### 1.5.73 NVMe Transport binding specification
A specification of reliable delivery of data, commands, and responses between a host and an NVM subsystem for an NVMe Transport. The binding may exclude or restrict functionality based on the NVMe Transport's capabilities.

### 1.5.74 participating NVM subsystem
An NVM subsystem that participates in (i.e., contains controllers that provide access to) a dispersed namespace.



---

### 1.5.75 Personality
A personality consists of settings that contribute to the configuration of the NVM subsystem (refer to section 5.2.26.1.24).

### 1.5.76 physical fabric interface (physical ports)
A physical connection between an NVM subsystem and a fabric.



---

### 1.5.77 Physical Presence Indicator (PPI)
A vendor-defined physical credential readable only by someone with physical possession of the device. Refer to section 5.2.26.1.24.1.1.



---

### 1.5.78 Placement Handle
A namespace scoped handle that maps to an Endurance Group scoped Reclaim Unit Handle which references a Reclaim Unit in each Reclaim Group.



---

### 1.5.79 Placement Identifier
A data structure that specifies a Reclaim Group Identifier and a Placement Handle that references a Reclaim Unit. Refer to Figure 289 and Figure 290.



---

### 1.5.80 Port ID
An identifier that is associated with an NVM subsystem port. Refer to section 2.2.2.



---

### 1.5.81 Ports List
A list of ports that may be used to export an NVM subsystem. Entries in the Ports List are in the format specified by Underlying Fabrics Transport Entry data structure (refer to Figure 352).



---

### 1.5.82 Power Loss Acknowledge (PLA)
The transport-specific variable that is used by the controller to inform the host of the controller’s current Power Loss Signaling processing (refer to section 8.2.5).



---

### 1.5.83 Power Loss Notification (PLN)
The transport-specific variable that is used to inform the controller that a main power loss event is expected to occur (refer to section 8.2.5).

### 1.5.84 primary controller
An NVM Express controller that supports the Virtualization Management command. An NVM subsystem may contain multiple primary controllers. Secondary controller(s) in an NVM subsystem depend on a primary controller for dynamic resource management (refer to section 8.2.6).

A PCI Express SR-IOV Physical Function that supports the NVM Express interface and the Virtualization Enhancements capability is an example of a primary controller (refer to section 8.2.6.4).
===== page_number= 13, page_type= body ====

### 1.5.85 private namespace
A namespace that is only able to be attached to one controller at a time. Refer to the Namespace Multi-path I/O and Namespace Sharing Capabilities (NMIC) field in Figure 335.

### 1.5.86 property
The generalization of memory mapped controller registers defined for NVMe over PCIe. Properties are used to configure low level controller attributes and obtain low level controller status. Refer to section 3.1.4.



---

### 1.5.87 Reclaim Group (RG)
An entity that contains one or more Reclaim Units. Refer to section 3.2.4.



---

### 1.5.88 Reclaim Unit (RU)
A logical representation of non-volatile storage within a Reclaim Group that is able to be physically erased by the controller without disturbing any other Reclaim Units. Refer to section 3.2.4.



---

### 1.5.89 Reclaim Unit Handle (RUH)
A controller resource that references a Reclaim Unit in each Reclaim Group. Refer to section 3.2.4.

### 1.5.90 rotational media
Media that stores data on rotating platters (refer to section 8.1.25).



---

### 1.5.91 Runtime D3 (Power Removed)
In Runtime D3 (RTD3) main power is removed from the controller. Auxiliary power may or may not be provided. For PCI Express, RTD3 is the D3cold power state (refer to section 8.1.18.4).

### 1.5.92 sanitize operation
Process by which all user data in the sanitization target is altered as described in section 8.1.26 such that recovery of the previous user data is infeasible for a given level of effort (refer to IEEE Std 2883).

### 1.5.93 sanitization target
The scope of a sanitize operation (i.e., an NVM subsystem, or a namespace).

### 1.5.94 secondary controller
An NVM Express controller that depends on a primary controller in an NVM subsystem for management of some controller resources (refer to section 8.2.6).

A PCI Express SR-IOV Virtual Function that supports the NVM Express interface and receives resources from a primary controller is an example of a secondary controller (refer to section 8.2.6.4).

### 1.5.95 shared namespace
A namespace that may be attached to two or more controllers in an NVM subsystem concurrently. Refer to the Namespace Multi-path I/O and Namespace Sharing Capabilities (NMIC) field in Figure 335.

### 1.5.96 specified namespace
The namespace that is associated with the value specified by the Namespace Identifier (NSID) field in a command as defined by the Common Command Format (refer to Figure 92).

### 1.5.97 spindown
The process of changing a spindle from an operational power state to a non-operational power state, for an Endurance Group that stores data on rotational media (refer to section 8.1.25).
===== page_number= 14, page_type= body ====

### 1.5.98 spinup
The process of changing a spindle from a non-operational power state to an operational power state, for an Endurance Group associated with rotational media (refer to section 8.1.25).

### 1.5.99 static controller
The controller is pre-existing with a specific Controller ID and its state (e.g., Feature settings) is preserved from prior associations.



---

### 1.5.100 Underlying Namespace
A namespace (defined in section 1.5.63) accessible through physical or virtual functions in an Underlying NVM Subsystem that may be used to associate with an Exported NVM Subsystem. Underlying Namespaces are identified by the Underlying Namespace Entry data structure (refer to Figure 350).



---

### 1.5.101 Underlying Namespace List
A list of namespaces (refer to section 5.2.13.4.1) in all underlying NVM subsystems that may be used to create an Exported Namespace.



---

### 1.5.102 Underlying NVM Subsystem
Defined as NVM subsystem.



---

### 1.5.103 Underlying Port
A port through which an NVMe subsystem is attached to a transport (e.g., Ethernet, InfiniBand, Fibre Channel) (refer to section 1.5.76).

### 1.5.104 user data
Data stored in a namespace that is composed of data that the host may store and later retrieve including metadata if supported.



---

### 1.6 I/O Command Set specific definitions used in this specification
The following terms used in this specification are defined in each NVM Express I/O Command Set specification.



---

#### 1.6.1 Endurance Group Host Read Command
An I/O Command Set specific command that results in the controller reading user data, but may or may not return the data to the host.



---

#### 1.6.2 Format Index
A value used to index into the I/O Command Set Specific Format table (i.e., the User Data Format number).



---

#### 1.6.3 SMART Data Units Read Command
An I/O Command Set specific command that results in the controller reading user data, but may or may not return the data to the host.



---

#### 1.6.4 SMART Host Read Command
An I/O Command Set specific command that results in the controller reading user data, but may or may not return the data to the host.



---

#### 1.6.5 User Data Format
An I/O Command Set specific format that describes the layout of the data on the NVM media.
===== page_number= 15, page_type= body ====

# NVM Express® Base Specification, Revision 2.3



---

## 1.6.6 User Data Out Command

An I/O Command Set specific command that results in the controller writing user data, but may or may not transfer user data from the host to the controller.



---

## 1.7 NVM Command Set specific definitions used in this specification

The following terms used in this specification are defined in the NVM Express NVM Command Set Specification. These terms are used throughout the document as examples for a specific I/O Command Set.

### 1.7.1 logical block

The smallest addressable data unit for Read and Write commands.

### 1.7.2 logical block address (LBA)

The address of a logical block, referred to commonly as LBA.



---

## 1.8 References

- CNSA 1.0, “USE OF PUBLIC STANDARDS FOR SECURE INFORMATION SHARING”, CNSSP 15 ANNEX B “NSA-APPROVED COMMERCIAL NATIONAL SECURITY ALGORITHM (CNSA) SUITE”, 20 October 2016. Available from [https://www.cnss.gov/CNSS/issuances/Policies.cfm](https://www.cnss.gov/CNSS/issuances/Policies.cfm).

- IEEE Std 2883™-2022, IEEE Standard for Sanitizing Storage. Available from [https://standards.ieee.org](https://standards.ieee.org).

- INCITS 502-2019, Information Technology – SCSI Primary Commands - 5 (SPC-5). Available from [https://webstore.ansi.org](https://webstore.ansi.org).

- INCITS 556-2020, Information Technology – Non-Volatile Memory Express - 2 (FC-NVMe-2). Available from [https://webstore.ansi.org](https://webstore.ansi.org).

- ISO 8601, Data elements and interchange formats – Information interchange – Representations of dates and times. Available from [https://www.iso.org](https://www.iso.org).

- ISO/IEC 27040:2024 Information technology – Security techniques – Storage security. Available from [https://www.iso.org](https://www.iso.org).

- JEDEC JESD218B-02: Solid State Drive (SSD) Requirements and Endurance Test Method standard. Available from [https://www.jedec.org](https://www.jedec.org).

- NVM Express Boot Specification, Revision 1.3. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- NVM Express Management Interface Specification, Revision 2.1. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- NVM Express NVM Command Set Specification, Revision 1.2. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- NVM Express Zoned Namespace Command Set Specification, Revision 1.4. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- NVM Express Key Value Command Set Specification, Revision 1.3. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- NVM Express NVMe over PCIe Transport Specification, Revision 1.3. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- NVM Express NVMe over RDMA Transport Specification, Revision 1.2. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- NVM Express NVMe over TCP Transport Specification, Revision 1.2. Available from [https://www.nvmexpress.org](https://www.nvmexpress.org).

- PCI-SIG PCI Express® Base Specification, Revision 6.2. Available from [https://www.pcisig.com](https://www.pcisig.com).

<!-- Embeded_Image 1, coordinate:(112,47,888,900) -->
===== page_number= 16, page_type= body ====

RFC 1952, P. Deutsch, “GZIP file format specification version 4.3”, May 1996. Available from https://www.rfc-editor.org/info/rfc1952.

RFC 1994, W. Simpson, “PPP Challenge Handshake Authentication Protocol (CHAP)”, August 1996. Available from https://www.rfc-editor.org/info/rfc1994.

RFC 2104, H. Krawczyk, M. Bellare, R. Canetti, “HMAC: Keyed-Hashing for Message Authentication”, February 1997. Available from https://www.rfc-editor.org/info/rfc2104.

RFC 2631, E. Rescorla, “Diffie-Hellman Key Agreement Method”, June 1999. Available from https://www.rfc-editor.org/info/rfc2631.

RFC 3629, F. Yergeau, “UTF-8, a transformation format of ISO 10646”, November 2003. Available from https://www.rfc-editor.org/info/rfc3629.

RFC 3986, T. Berners-Lee, R. Fielding, L. Masinter, “Uniform Resource Identifier (URI): Generic Syntax”, January 2005. Available from https://www.rfc-editor.org/info/rfc3986.

RFC 4086, D. Eastlake 3rd, J. Schiller, S. Crocker, “Randomness Requirements for Security”, June 2005. Available from https://www.rfc-editor.org/info/rfc4086.

RFC 4088, D. Black, K. McCloghrie, J. Schoenwaelder, “Uniform Resource Identifier (URI) Scheme for the Simple Network Management Protocol (SNMP)”, June 2005. Available from https://www.rfc-editor.org/info/rfc4088.

RFC 4301, S. Kent, K. Seo, “Security Architecture for the Internet Protocol”, December 2005. Available from https://www.rfc-editor.org/info/rfc4301.

RFC 4648, S. Josefsson, “The Base16, Base32, and Base64 Data Encodings”, October 2006. Available from https://www.rfc-editor.org/info/rfc4648.

RFC 5869, H. Krawczyk, P. Eronen, “HMAC-based Extract-and-Expand Key Derivation Function (HKDF)”, May 2010. Available from https://www.rfc-editor.org/info/rfc5869.

RFC 6234, D. Eastlake 3rd, and T. Hansen, “US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)”, May 2011. Available from https://www.rfc-editor.org/info/rfc6234.

RFC 6520, R. Seggelmann, M. Tuexen, M. Williams, “Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS) Heartbeat Extension”, February 2012. Available from https://www.rfc-editor.org/info/rfc6520.

RFC 7296, C. Kaufman, P. Hoffman, Y. Nir, P. Eronen, T. Kivinen, “Internet Key Exchange Protocol Version 2 (IKEv2)”, October 2014. Available from https://www.rfc-editor.org/info/rfc7296.

RFC 7919, D. Gillmor, “Negotiated Finite Field Diffie-Hellman Ephemeral Parameters for Transport Layer Security (TLS)”, August 2016. Available from https://www.rfc-editor.org/info/rfc7919.

RFC 8446, E. Rescorla, “The Transport Layer Security (TLS) Protocol Version 1.3”, August 2018. Available from https://www.rfc-editor.org/info/rfc8446.

RFC 9562, K. Davis, B. Peabody, and P. Leach, “Universally Unique Identifiers, May 2024”. Available from https://www.rfc-editor.org/info/rfc9562.

UEFI Specification Version 2.10, August 2022. Available from https://uefi.org.

Advanced Configuration and Power Interface (ACPI) Specification, Version 6.5, August 2022. Available from https://www.uefi.org.

TCG Storage Architecture Core Specification, Version 2.01 Revision 1.00. Available from https://www.trustedcomputinggroup.org.

TCG Storage Interface Interactions Specification (SIIS), Version 1.11 Revision 1.18. Available from https://www.trustedcomputinggroup.org.

TCG Storage Security Subsystem Class: Key Per I/O Version 1.00 Revision 1.41. Available from https://trustedcomputinggroup.org.

<!-- Embeded_Image 1, coordinate:(0,0,1000,999) -->
===== page_number= 17, page_type= body ====

NVM Express® Base Specification, Revision 2.3

TCG Storage Opal SSC Feature Set: PSID Specification, Version 1.00 Revision 1.00. Available from [https://www.trustedcomputinggroup.org](https://www.trustedcomputinggroup.org).

TCG Storage Security Subsystem Class: Opal Specification, Version 2.02 Revision 1.0. Available from [https://www.trustedcomputinggroup.org](https://www.trustedcomputinggroup.org).

NIST Special Publication 800-57 Part 1 Revision 5. Available from [https://csrc.nist.gov](https://csrc.nist.gov).

NIST FIPS Publication 180-4. Available from [https://csrc.nist.gov](https://csrc.nist.gov).



![Embeded_Image 1](restored_images/Embeded_Image_1.png)
**Embeded_Image 1**


---

### 1.9 References Under Development

None.
===== page_number= 18, page_type= body ====



---

# 2 Theory of Operation

The NVM Express scalable interface is designed to address the needs of storage systems that utilize PCI Express based solid state drives or fabric connected devices. The interface provides optimized command submission and completion paths. It includes support for parallel operation by supporting up to 65,535 I/O Queues with up to 65,535 outstanding commands per I/O Queue. Additionally, support has been added for many Enterprise capabilities like end-to-end data protection (compatible with SCSI Protection Information, commonly known as T10 DIF, and SNIA DIX standards), enhanced error reporting, and virtualization.

The interface has the following key attributes:

- Does not require uncacheable / MMIO register reads in the command submission or completion path;
- A maximum of one MMIO register write or one 64B message is necessary in the command submission path;
- Support for up to 65,535 I/O Queues, with each I/O Queue supporting up to 65,535 outstanding commands;
- Priority associated with each I/O Queue with well-defined arbitration mechanism;
- All information to complete a 4 KiB read request is included in the 64B command itself, ensuring efficient small I/O operation;
- Efficient and streamlined command set;
- Support for MSI/MSI-X and interrupt aggregation;
- Support for multiple namespaces;
- Efficient support for I/O virtualization architectures like SR-IOV;
- Robust error reporting and management capabilities; and
- Support for multi-path I/O and namespace sharing.

This specification defines a streamlined set of properties that are used to configure low level controller attributes and obtain low level controller status. These properties have a transport specific mechanism for defining access (e.g., memory-based transports use registers, whereas message-based transports use the Property Get and Property Set commands). The following are examples of functionality defined in properties:

- Indication of controller capabilities;
- Status for controller failures (command status is provided in a CQE);
- Admin Queue configuration (I/O Queue configuration processed via Admin commands); and
- Doorbell registers (refer to the NVMe over PCIe Transport Specification) for a scalable number of Submission and Completion Queues.

There are two defined models for communication between the host and the NVM subsystem, a memory-based transport model and a message-based transport model. All NVM subsystems require the underlying NVMe Transport to provide reliable NVMe command and data delivery. An NVMe Transport is an abstract protocol layer independent of any physical interconnect properties. A taxonomy of NVMe Transports, along with examples, is shown in Figure 4. An NVMe Transport may expose a memory-based transport model or a message-based transport model. The message-based transport model has two subtypes: the message-only transport model and the message/memory transport model.

A memory-based transport model is one in which commands, responses, and data are transferred between a host and an NVM subsystem by performing explicit memory read and write operations (e.g., over PCIe).

A message-based transport model is one in which messages containing command capsules and response capsules are sent between a host and an NVM subsystem (e.g., over a fabric). The two subtypes of message-based transport models are differentiated by how data is sent between a host and an NVM subsystem. In the message-only transport model data is only sent between a host and an NVM subsystem using capsules or messages. The message/memory transport model uses a combination of messages and explicit memory read and write operations to transfer command capsules, response capsules and data between a host and an NVM subsystem. Data may optionally be included in command capsules and response capsules. Both the message-only transport model and the message/memory transport model are

<!-- Figure 4, coordinate:(115,880,885,920) -->
===== page_number= 19, page_type= body ==___

referenced as message-based transport models throughout this specification when the description is applicable to both subtypes.

An NVM subsystem is made up of a single domain or multiple domains as described in section 3.2.5. An NVM subsystem may optionally include a non-volatile storage medium, and an interface between the controller(s) of the NVM subsystem and the non-volatile storage medium. Controllers expose this non-volatile storage medium to hosts through namespaces. An NVM subsystem is not required to have the same namespaces attached to all controllers. An NVM subsystem that supports a Discovery controller does not support any other controller type. A Discovery Service is an NVM subsystem that supports Discovery controllers only (refer to section 3.1).

**Figure 4: Taxonomy of Transport Models**

<!-- Figure 4, coordinate:(120,245,880,485) -->

The capabilities and settings that apply to an NVM Express controller are indicated in the Controller Capabilities (CAP) property and the Identify Controller data structure (refer to Figure 328).

A namespace is a set of resources (e.g., formatted non-volatile storage) that may be accessed by a host. A namespace has an associated namespace identifier that a host uses to access that namespace. The set of resources may consist of non-volatile storage and/or other resources.

Associated with each namespace is an I/O Command Set that operates on that namespace. An NVM Express controller may support multiple namespaces. Namespaces may be created and deleted using the Namespace Management command and Capacity Management command. The Identify Namespace data structures (refer to section 1.5.50) indicate capabilities and settings that are specific to a particular namespace.

The NVM Express interface is based on a paired Submission and Completion Queue mechanism. Commands are placed by a host into a Submission Queue. Completions are placed into the associated Completion Queue by the controller.

There are three types of commands that are defined in NVM Express: Admin commands, I/O commands, and Fabrics commands. Figure 5 shows these different command types.
===== page_number= 20, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 5: Types of NVMe Command Sets, coordinate:(208,90,798,275) -->

**Figure 5: Types of NVMe Command Sets**

An Admin Submission Queue and associated Completion Queue exist for the purpose of controller management and control (e.g., creation and deletion of I/O Submission and Completion Queues, aborting commands, etc.). Only commands that are part of the Admin Command Set or the Fabrics Command Set may be submitted to the Admin Submission Queue.

An I/O Command Set is used with an I/O queue pair. This specification defines common I/O commands. I/O Command Sets are defined in the NVM Express I/O Command Set specifications. The example I/O Command Sets shown in Figure 5 are the NVM Command Set, the Key Value Command Set, and the Zoned Namespace Command Set. Other I/O Command Sets include the Computational Programs Command Set and the SLM Command Set.

The Fabrics Command Set is NVMe over Fabrics specific. Fabrics Command Set commands are used for operations specific to NVMe over Fabrics including establishing a connection, NVMe in-band authentication, and to get or set a property. All Fabrics commands may be submitted on the Admin Submission Queue and some Fabrics commands may also be submitted on an I/O Submission Queue. Unlike Admin and I/O commands, Fabrics commands are processed by a controller regardless of whether the controller is enabled (i.e., regardless of the state of CC.EN).



![Figure 4](restored_images/Figure_4.png)
**Figure 4**
![Figure 5](restored_images/Figure_5.png)
**Figure 5**


---

## 2.1 Memory-Based Transport Model (PCIe)

In the memory-based model, Submission and Completion Queues are allocated in memory.

A host creates queues, up to the maximum supported by the controller. Typically, the number of command queues created is based on the system configuration and anticipated workload. For example, on a four core processor based system, there may be a queue pair per core to avoid locking and ensure data structures are created in the appropriate processor core’s cache. Figure 6 provides a graphical representation of the queue pair mechanism, showing a 1:1 mapping between Submission Queues and Completion Queues. Figure 7 shows an example where multiple I/O Submission Queues utilize the same I/O Completion Queue on Core B. Figure 6 and Figure 7 show that there is always a 1:1 mapping between the Admin Submission Queue and Admin Completion Queue.
===== page_number= 21, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 6: Queue Pair Example, 1:1 Mapping, coordinate:(115,115,880,335) -->
**Figure 6: Queue Pair Example, 1:1 Mapping**

The diagram shows a Host with multiple cores (Core 0, Core 1, ..., Core N-1) and a Controller. Each core has an I/O Submission Queue and an I/O Completion Queue. Additionally, there is a Controller Mgmt section with an Admin Submission Queue and an Admin Completion Queue. All queues are connected to the Controller via yellow arrows, indicating communication paths.

<!-- Figure 7: Queue Pair Example, n:1 Mapping, coordinate:(115,385,880,605) -->
**Figure 7: Queue Pair Example, n:1 Mapping**

The diagram shows a Host with Controller Mgmt, Core A, and Core B, each containing various Submission and Completion Queues (e.g., I/O Submission Queue M, I/O Completion Queue N, etc.). All queues are connected to the Controller via yellow arrows, indicating communication paths.

A Submission Queue (SQ) is a circular buffer with a fixed slot size that the host uses to submit commands for execution by the controller. The host updates the appropriate SQ Tail doorbell register when there are one to n new commands to execute. The previous SQ Tail value is overwritten in the controller when there is a new doorbell register write. The controller fetches SQ entries in order from the Submission Queue and may execute those commands in any order.

Each submission queue entry is a command. Commands are 64 bytes in size. The physical memory locations in memory to use for data transfers are specified using Physical Region Page (PRP) entries or Scatter Gather Lists (SGL). Each command may include two PRP entries or one Scatter Gather List segment. If more than two PRP entries are necessary to describe the data buffer, then a pointer to a PRP List that describes a list of PRP entries is provided. If more than one SGL segment is necessary to describe the data buffer, then the SGL segment provides a pointer to the next SGL segment.

A Completion Queue (CQ) is a circular buffer with a fixed slot size used to post status for completed commands. A completed command is uniquely identified by a combination of the associated SQ identifier and command identifier that is assigned by a host. In the memory-based transport model multiple Submission Queues may be associated with a single Completion Queue. A configuration with a single Completion Queue may be used where a single worker thread processes all command completions via one Completion Queue even when those commands originated from multiple Submission Queues. The CQ Head pointer is updated by a host after processing completion queue entries indicating the last free CQ

---
===== page_number= 22, page_type= body ====

slot. A Phase Tag (P) bit is defined in the completion queue entry to indicate whether an entry has been newly posted without the host consulting a register (refer to section 4.2.4). The Phase Tag bit enables the host to determine whether entries are new or not.



![Figure 6](restored_images/Figure_6.png)
**Figure 6**
![Figure 7](restored_images/Figure_7.png)
**Figure 7**


---

## 2.2 Message-Based Transport Model (Fabrics)

The message-based transport model used for NVMe over Fabrics has the following differences from the memory-based transport model:

- There is a one-to-one mapping between I/O Submission Queues and I/O Completion Queues. NVMe over Fabrics does not support multiple I/O Submission Queues being mapped to a single I/O Completion Queue;
- NVMe over Fabrics does not define an interrupt mechanism that allows a controller to generate a host interrupt. It is the responsibility of the host fabric interface (e.g., Host Bus Adapter) to generate host interrupts;
- NVMe over Fabrics uses different mechanisms for I/O Submission Queue and I/O Completion Queue creation and deletion (refer to section 3.5);
- NVMe over Fabrics does not support transferring metadata from a separate buffer (e.g., does not support the Metadata Pointer field, refer to Figure 92);
- NVMe over Fabrics does not support PRPs but requires use of SGLs for Admin, I/O, and Fabrics commands. This differs from the memory-based transport model where SGLs are not supported for Admin commands and are optional for I/O commands;
- NVMe over Fabrics does not support Completion Queue flow control (refer to section 3.3.1.2.1). This requires that the host ensures there are available Completion Queue slots before submitting new commands; and
- NVMe over Fabrics allows Submission Queue flow control to be disabled if the host and controller agree to disable Submission Queue flow control. If Submission Queue flow control is disabled, the host is required to ensure that there are available Submission Queue slots before submitting new commands.



---

## 2.2.1 Fabrics and Transports

NVMe over Fabrics utilizes the protocol layering shown in Figure 8. This specification defines core aspects of the architecture that are independent of the NVMe Transport. An NVMe Transport binding specification is used to describe any NVMe Transport specific specialization as well as how the services required by the NVMe interface are mapped onto the corresponding NVMe Transport. The native fabric communication services and other functionality used by the NVMe interface and NVMe Transports (e.g., the Fabric Protocol and Fabric Physical layers in Figure 8) are outside the scope of the NVMe family of specifications.

<!-- Figure 8, coordinate:(0,0,0,0) -->
===== page_number= 23, page_type= body ====

<!-- Figure 8: NVMe over Fabrics Layering, coordinate:(220,88,795,585) -->
**Figure 8: NVMe over Fabrics Layering**

| Layer | Description |
|-------|-------------|
| **NVMe over Fabrics (Message-based Model)** | NVMe Architecture, Queuing Interface, Admin Command & I/O Command Sets, Properties |
| **NVMe Transport Specification** | Fabric Specific Properties, Transport Specific Features/Specialization |
| | NVMe Transport Binding Services |
| **NVMe Transport** | NVMe Transport |
| | Fabric Protocol (may include multiple fabric protocol layers) |
| **Fabric** | Fabric Physical (e.g., Ethernet, InfiniBand, Fibre Channel) |

---



| Layer | Description |
|-------|-------------|
| **NVMe over Fabrics (Message-based Model)** | NVMe Architecture, Queuing Interface, Admin Command & I/O Command Sets, Properties |
| **NVMe Transport Specification** | Fabric Specific Properties, Transport Specific Features/Specialization |
| | NVMe Transport Binding Services |
| **NVMe Transport** | NVMe Transport |
| | Fabric Protocol (may include multiple fabric protocol layers) |
| **Fabric** | Fabric Physical (e.g., Ethernet, InfiniBand, Fibre Channel) |


---

### 2.2.2 NVM Subsystem Ports for Fabrics

An NVM subsystem presents a collection of one to (64Ki - 16) controllers which are used to access namespaces. The controllers may be associated with hosts through one to 64Ki NVM subsystem ports.

An NVM subsystem port is a protocol interface between an NVM subsystem and a fabric. An NVM subsystem port is a collection of one or more physical fabric interfaces that together act as a single protocol interface. When link aggregation (e.g., Ethernet) is used, the physical ports for the group of aggregated links constitute a single NVM subsystem port.

An NVM subsystem contains one or more NVM subsystem ports.

Each NVM subsystem port has a 16-bit port identifier (Port ID). An NVM subsystem port is identified by the NVM Subsystem NVMe Qualified Name (NQN) and Port ID. The NVM subsystem ports of an NVM subsystem may support different NVMe Transports. An NVM subsystem port may support multiple NVMe Transports if more than one NVMe Transport binding specifications exist for the underlying fabric (e.g., an NVM subsystem port identified by a Port ID may support both iWARP and RoCE). An NVM subsystem implementation may bind specific controllers to specific NVM subsystem ports or allow the flexible allocation of controllers between NVM subsystem ports; however, once connected, each specific controller is bound to a single NVM subsystem port.
===== page_number= 24, page_type= body ==___

A controller is associated with exactly one host at a time. NVMe over Fabrics allows multiple hosts to connect to different controllers in the NVM subsystem through the same NVM subsystem port. All other aspects of NVMe over Fabrics multi-path I/O and namespace sharing (refer to section 2.4.1) are equivalent to that of the memory-based transport model.



---

## 2.2.3 Discovery Service

NVMe over Fabrics defines a discovery mechanism that a host uses to determine the NVM subsystems that expose namespaces that the host may access. The Discovery Service provides a host with the following capabilities:

- The ability to discover a list of NVM subsystems with namespaces that are accessible to the host;
- The ability to discover multiple paths to an NVM subsystem;
- The ability to discover controllers that are statically configured;
- The optional ability to establish explicit persistent connections to the Discovery controller; and
- The optional ability to receive Asynchronous Event Notifications from the Discovery controller.

A Discovery Service is an NVM subsystem that supports only Discovery controllers (refer to section 3.1.3.3), and shall not support any other controller type.

The method that a host uses to obtain the information necessary to connect to the initial Discovery Service is implementation specific. This information may be determined using a host configuration file, a hypervisor or OS property, or some other mechanism.



---

## 2.2.4 Capsules and Data Transfer

A capsule is an NVMe unit of information exchange used in NVMe over Fabrics. A capsule may be classified as a command capsule or a response capsule. A command capsule contains a command (formatted as a submission queue entry) and may optionally include SGLs or data. A response capsule contains a response (formatted as a completion queue entry) and may optionally include data. Data refers to any data transferred at an NVMe layer between a host and an NVM subsystem (e.g., logical block data or a data structure associated with a command). A capsule is independent of any underlying NVMe Transport unit (e.g., packet, message, or frame and associated headers and footers) and may consist of multiple such units.

Command capsules are transferred from a host to an NVM subsystem. The SQE contains an Admin command, an I/O command, or a Fabrics command. The minimum size of a command capsule is NVMe Transport binding specific, but shall be at least 64B in size. The maximum size of a command capsule is NVMe Transport binding specific. The format of a command capsule is shown in Figure 9.

**Figure 9: Command Capsule Format**

<!-- Figure 9, coordinate:(148,630,850,755) -->

Response capsules are transferred from an NVM subsystem to a host. The CQE is associated with a previously issued Admin command, I/O command, or Fabrics command. The size of a response capsule is NVMe Transport binding specific, but shall be at least 16B in size. The maximum size of a response capsule is NVMe Transport binding specific. The format of a response capsule is shown in Figure 10.
===== page_number= 25, page_type= body ==___

NVMe Express® Base Specification, Revision 2.3

<!-- Figure 10, coordinate:(148,88,840,228) -->
**Figure 10: Response Capsule Format**

```
Byte 0           15 16                   (N-1)
+----------------+------------------------+
| Completion Queue Entry | Data (if present) |
+----------------+------------------------+
                Response Capsule of Size N Bytes
```

NVMe Transports using the message-only transport model and message/memory transport model require all SGLs sent from the host to the controller be transferred within the command. NVMe Transports may optionally support the transfer of a portion or all data within the command and response capsules.

NVMe over Fabrics requires SGLs for all commands (Fabrics, Admin, and I/O). An SGL may specify the placement of data within a capsule or the information required to transfer data using an NVMe Transport specific data transfer mechanism (e.g., via memory transfers as in RDMA). Each NVMe Transport binding specification defines the SGLs used by a particular NVMe Transport and any capsule SGL and data placement restrictions.



| Completion Queue Entry | Data (if present) |


![Figure 9](restored_images/Figure_9.png)
**Figure 9**


---

## 2.2.5 Authentication

NVMe over Fabrics supports both fabric secure channel that includes authentication (refer to section 8.3.5.1) and NVMe in-band authentication. An NVM subsystem may require a host to use fabric secure channel, NVMe in-band authentication, or both. The Discovery Service indicates if fabric secure channel shall be used for an NVM subsystem. The Connect response indicates if NVMe in-band authentication shall be used with that controller.

A controller associated with an NVM subsystem that requires a fabric secure channel shall not accept any commands (i.e., Fabrics commands, Admin commands, or I/O commands) on an NVMe Transport until a secure channel is established. Following a Connect command, a controller that requires NVMe in-band authentication shall not accept any commands on the queue created by that Connect command other than authentication commands until NVMe in-band authentication has completed. Refer to section 8.3.5.



---

## 2.3 NVM Storage Model



---

### 2.3.1 Storage Entities

The NVM storage model includes the following entities:

- NVM subsystems (refer to section 1.5.68);
- Domains (refer to section 3.2.5);
- Endurance Groups (refer to section 3.2.3);
- Reclaim Groups and Reclaim Units (refer to section 3.2.4);
- NVM Sets (refer to section 3.2.2); and
- Namespaces (refer to section 3.2.1).

As illustrated in this section:

- each domain is contained in a single NVM subsystem;
- each Endurance Group is contained in a single domain and may contain either:
  - one or more NVM Sets; or
  - one or more Reclaim Groups;
- each NVM Set is contained in a single Endurance Group and each namespace is contained in a single NVM Set. Each Media Unit is contained in a single Endurance Group; and
- each Reclaim Group is contained in a single Endurance Group, each Reclaim Unit is contained in a Reclaim Group, and each namespace is contained in an Endurance Group within one or more Reclaim Units of the Reclaim Groups in that Endurance Group.
===== page_number= 26, page_type= body ==___

Each Endurance Group is composed of storage media, which are termed Media Units (refer to section 8.1.4.2) or Reclaim Units (refer to section 3.2.4). Reclaim Unit Handles reference a Reclaim Unit in each Reclaim group for writing user data. For clarity, Media Units, Reclaim Unit Handles, and Reclaim Units are not shown in the examples in this section that follow.

Figure 11 shows the hierarchical relationships of these entities within a simple NVM subsystem, which has:
- one domain;
- one Endurance Group;
- one NVM Set; and
- one namespace.

**Figure 11: Simple NVM Storage Hierarchy with NVM Sets**

<!-- Figure 11, coordinate:(342,279,655,587) -->

Figure 12 shows the hierarchical relationships in a simple NVM subsystem, which has:
- one domain;
- one Endurance Group;
- one Reclaim Group; and
- one namespace with user data written to the single Reclaim Group.

The placement (i.e., which Reclaim Group) of user data for a namespace is directed by each host write command to that namespace (refer to section 8.1.11).
===== page_number= 27, page_type= body ====

NVM Express® Base Specification, Revision 2.3

**Figure 12: Simple NVM Storage Hierarchy with One Reclaim Group**

<!-- Figure 12, coordinate:(327,115,655,435) -->

Figure 13 shows the hierarchical relationships in a simple NVM subsystem, which has:
- one domain;
- one Endurance Group;
- four Reclaim Groups; and
- one namespace with user data written to each Reclaim Group.

The placement (i.e., which Reclaim Group) of user data for a namespace is directed by each host write command to that namespace (refer to section 8.1.11).
===== page_number= 28, page_type= body ====

NVM Express® Base Specification, Revision 2.3

**Figure 13: Simple NVM Storage Hierarchy with Multiple Reclaim Groups**

<!-- Figure 13, coordinate:(158,122,808,440) -->

The diagram shows a hierarchical structure:

- **Outermost layer**: `NVM Subsystem`
- **Next layer**: `Domain 0` (light green background)
- **Next layer**: `Endurance Group 1` (light orange background)
- **Innermost layer**: Four `Reclaim Group` blocks (Reclaim Group 0, 1, 2, 3) in light blue
- **Overlaying across reclaim groups**: `Namespace 1` (white rectangle spanning all four reclaim groups)

Figure 14 shows the relationships of these entities in a complex NVM subsystem, which has:
- multiple domains;
- multiple Endurance Groups per domain;
- multiple NVM Sets per Endurance Group; and
- multiple namespaces per NVM Set.
===== page_number= 29, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 14, coordinate:(185,93,810,468) -->
**Figure 14: Complex NVM Storage Hierarchy with NVM Sets**

Entity naming key (Abc):
- A: Domain (capital letter)
- b: Endurance Group (digit)
- c: NVM Set (lower case letter)

Figure 15 shows the relationships in a complex NVM subsystem, which has:
- multiple domains;
- multiple Endurance Groups per domain;
- multiple Reclaim Groups per Endurance Group; and
- multiple namespaces per Endurance Group.

The placement (i.e., which Reclaim Group) of user data for a namespace is directed by each host write command to that namespace (refer to section 8.1.11).
===== page_number= 30, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 15, coordinate:(117,115,872,648) -->
**Figure 15: Complex NVM Storage Hierarchy with Multiple Reclaim Groups**

The diagram illustrates a hierarchical structure of NVM storage entities:

- **NVM Subsystem** (outermost container)
  - Contains multiple **Domains** (e.g., Domain A, Domain D)
    - Each Domain contains multiple **Endurance Groups** (e.g., Endurance Group A1, A3, D1, D5)
      - Each Endurance Group contains multiple **Reclaim Groups** (e.g., Reclaim Group A10, A11, ..., A1f; Reclaim Group D10, D11, ..., D1h)
        - Each Reclaim Group may contain one or more **Namespaces**

Entity naming key (Abc):
- A: Domain (capital letter)
- b: Endurance Group (digit)
- c: Reclaim Group (digit or lower-case letter for maximum number)

The support of Endurance Groups, Reclaim Groups within an Endurance Group, or NVM Sets within an Endurance Group is optional, but the storage model supports these concepts. An NVM subsystem may be shipped by the vendor with storage entities configured, or an NVM subsystem may be configured or reconfigured by the customer. Typical changes to the configuration are creation and deletion of namespaces.

An NVM subsystem that does not support multiple NVM Sets does not require reporting of NVM Sets. An NVM subsystem that does not support multiple Endurance Groups does not require reporting of Endurance Groups.
===== page_number= 31, page_type= body ====



![Figure 11](restored_images/Figure_11.png)
**Figure 11**
![Figure 12](restored_images/Figure_12.png)
**Figure 12**
![Figure 13](restored_images/Figure_13.png)
**Figure 13**
![Figure 14](restored_images/Figure_14.png)
**Figure 14**
![Figure 15](restored_images/Figure_15.png)
**Figure 15**


---

## 2.3.2 I/O Command Sets

I/O commands perform operations on namespaces, and each namespace is associated with exactly one I/O command set. For example, commands in the NVM Command Set access data represented in a namespace as logical blocks, and commands in the Key Value Command Set access data represented in a namespace as key-value pairs.

The association of a namespace to an I/O command set is specified when the namespace is created and is fixed for the lifetime of that namespace.

A controller may support one or more I/O command sets. Namespaces that are associated with the I/O command sets that are supported and enabled on a controller may be attached to that controller. A host issues commands to a namespace and those commands are interpreted based on the I/O command set associated with that namespace.



---

## 2.3.3 NVM Subsystem Examples

Figure 16 illustrates a simple NVM subsystem that has a single instance of each storage entity.

### Figure 16: Single-Namespace NVM Subsystem
<!-- Figure 16, coordinate:(340,350,658,735) -->

- The NVM subsystem consists of a single port and a single domain.
- The domain contains a controller and storage media.
- All of the storage media are contained in one Endurance Group.
- All of the storage media in that Endurance Group are organized into one NVM Set.
- That NVM Set contains a single namespace.

Figure 17 shows an NVM subsystem with two namespaces.
===== page_number= 32, page_type= body ====

NVM Express® Base Specification, Revision 2.3

**Figure 17: Two-Namespace NVM Subsystem**

<!-- Figure 17, coordinate:(270,114,728,483) -->

An NVM subsystem may have multiple domains, multiple namespaces, multiple controllers, and multiple ports, as shown in Figure 18.
===== page_number= 33, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 18: Complex NVM Subsystem, coordinate:(144,100,850,525) -->

**Figure 18: Complex NVM Subsystem**

The diagram shows a complex NVM subsystem with three domains (Domain 1, Domain 2, and an implied Domain 3 via ellipsis). Each domain contains a Controller connected to a Port. Each Controller manages one or more NVM Sets, which contain Namespaces. These NVM Sets are grouped into Endurance Groups. Specifically:

- **Domain 1**: Controller → NVM Set 1 → Namespace 1 → Endurance Group 1
- **Domain 2**: Controller → NVM Set 2 → Namespace 2 → Endurance Group 2
- **Domain 3 (implied)**: Controller → NVM Set 3 → Namespace 3 and Namespace 4 → Endurance Group 3

The entire structure is labeled as "NVM Subsystem".

---



![Figure 16](restored_images/Figure_16.png)
**Figure 16**
![Figure 17](restored_images/Figure_17.png)
**Figure 17**
![Figure 18](restored_images/Figure_18.png)
**Figure 18**


---

## 2.4 Extended Capabilities Theory



---

### 2.4.1 Multi-Path I/O and Namespace Sharing

This section provides an overview of multi-path I/O and namespace sharing. Multi-path I/O refers to two or more completely independent paths between a single host and a namespace while namespace sharing refers to the ability for two or more hosts to access a common shared namespace using different NVM Express controllers. Both multi-path I/O and namespace sharing require that the NVM subsystem contain two or more controllers. NVM subsystems that support Multi-Path I/O and Namespace Sharing may also support asymmetric controller behavior (refer to section 2.4.2). Concurrent access to a shared namespace by two or more hosts requires some form of coordination between hosts. The procedure used to coordinate these hosts is outside the scope of this specification.

Figure 19 shows an NVM subsystem that contains a single NVM Express controller implemented over PCI Express and a single PCI Express port. Since this is a single Function PCI Express device, the NVM Express controller shall be associated with PCI Function 0. A controller may support multiple namespaces. The controller in Figure 19 supports two namespaces labeled NS A and NS B. Associated with each controller namespace is a namespace ID, labeled as NSID 1 and NSID 2, that is used by the controller to reference a specific namespace. The namespace ID is distinct from the namespace itself and is the handle a host and controller use to specify a particular namespace in a command. The selection of a controller’s namespace IDs is outside the scope of this specification. In this example, NSID 1 is associated with namespace A and NSID 2 is associated with namespace B. Both namespaces are private to the controller and this configuration supports neither multi-path I/O nor namespace sharing.

---
===== page_number= 34, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

**Figure 19: NVM Express Controller with Two Namespaces**

<!-- Figure 19, coordinate:(400,118,590,308) -->

PCIe Port

PCI Function 0  
NVM Express Controller  

NSID 1     NSID 2  
NS A       NS B  

Figure 20 shows a multi-Function NVM subsystem with a single PCI Express port containing two controllers implementing NVMe over PCIe. One controller is associated with PCI Function 0 and the other controller is associated with PCI Function 1. Each controller supports a single private namespace and access to shared namespace B. The namespace ID shall be the same in all controllers that have access to a particular shared namespace. In this example, both controllers use NSID 2 to access shared namespace B.

**Figure 20: NVM Subsystem with Two Controllers and One Port**

<!-- Figure 20, coordinate:(320,430,670,700) -->

PCIe Port

PCI Function 0         PCI Function 1  
NVMe Controller       NVMe Controller  

NSID 1   NSID 2       NSID 3   NSID 2  
NS A     NS B         NS C     NS B  

There is one or more Identify Controller data structures for each controller and one or more Identify Namespace data structures (refer to section 1.5.50) for each namespace (refer to Figure 326). Controllers with access to a shared namespace return the Identify Namespace data structure associated with that shared namespace (i.e., the same data structure contents are returned by all controllers with access to the same shared namespace). There is a globally unique identifier (refer to section 4.7.1) associated with the namespace itself and may be used to determine when there are multiple paths to the same shared namespace.

Controllers associated with a shared namespace may operate on the namespace concurrently. Operations performed by individual controllers are atomic to the shared namespace at the write atomicity level of the controller to which the command was submitted (refer to section 3.4.3). The write atomicity level is not required to be the same across controllers that share a namespace. If there are any ordering requirements

---
===== page_number= 35, page_type= body ==___

between commands issued to different controllers that access a shared namespace, then a host (e.g., host software or an associated application) is required to enforce these ordering requirements.

Figure 21 illustrates an NVM subsystem with two PCI Express ports, each with an associated controller implementing NVMe over PCIe. Both controllers map to PCI Function 0 of the corresponding port. Each PCI Express port in this example is completely independent and has its own PCI Express Fundamental Reset and reference clock input. A reset of a port only affects the controller associated with that port and has no impact on the other controller, shared namespace, or operations performed by the other controller on the shared namespace. Refer to section 4.4 for Feature behavior on reset. The functional behavior of this example is otherwise the same as that illustrated in Figure 20.

**Figure 21: NVM Subsystem with Two Controllers and Two Ports**

<!-- Figure 21, coordinate:(320,268,675,532) -->

The two ports shown in Figure 21 may be associated with the same Root Complex or with different Root Complexes and may be used to implement both multi-path I/O and I/O sharing architectures. System-level architectural aspects and use of multiple ports in a PCI Express fabric are beyond the scope of this specification.

Figure 22 illustrates an NVM subsystem that supports Single Root I/O Virtualization (SR-IOV) and has one Physical Function and four Virtual Functions. An NVM Express controller implementing NVMe over PCIe is associated with each Function with each controller having a private namespace and access to a namespace shared by all controllers, labeled NS F. The behavior of the controllers in this example parallels that of the other examples in this section. Refer to section 8.2.6.4 for more information on SR-IOV.
===== page_number= 36, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

**Figure 22: PCI Express Device Supporting Single Root I/O Virtualization (SR-IOV)**

<!-- Figure 22, coordinate:(118,118,878,380) -->

Examples provided in this section are meant to illustrate concepts and are not intended to enumerate all possible configurations. For example, an NVM subsystem may contain multiple PCI Express ports with each port supporting SR-IOV.



![Figure 19](restored_images/Figure_19.png)
**Figure 19**
![Figure 20](restored_images/Figure_20.png)
**Figure 20**
![Figure 21](restored_images/Figure_21.png)
**Figure 21**
![Figure 22](restored_images/Figure_22.png)
**Figure 22**


---

### 2.4.2 Asymmetric Controller Behavior

Asymmetric controller behavior occurs in NVM subsystems where namespace access characteristics (e.g., performance) may vary based on:

- the internal configuration of the NVM subsystem; or
- which controller is used to access a namespace (e.g., Fabrics).

NVM subsystems that provide asymmetric controller behavior may support Asymmetric Namespace Access Reporting as described in section 8.1.1.
===== page_number= 37, page_type= body ====



---

# 3 NVM Express Architecture



---

## 3.1 NVM Controller Architecture

A controller is the interface between a host and an NVM subsystem. This specification defines two controller models, the static controller model and the dynamic controller model. All controllers in an NVM subsystem shall support the same controller model.

In an NVM subsystem that supports the static controller model, state (e.g., controller ID, saved Feature settings) is preserved:

- across a Controller Level Reset for memory-based controllers and message-based controllers; and
- from prior associations for message-based controllers.

In an NVM subsystem that supports the dynamic controller model, the NVM subsystem allocates controllers on demand with no state preserved from prior associations.



---

### 3.1.1 Memory-Based Controller Architecture (PCIe)

Memory-based controllers shall support only the static controller model.



---

### 3.1.2 Message-Based Controller Architecture (Fabrics)

Message-based controllers, other than Discovery controllers, may support either the dynamic controller model or the static controller model. A Discovery controller shall support only the dynamic controller model.

In an NVM subsystem that supports the static controller model, each controller that is allocated to a particular host may have different state at the time the association is established (e.g., each controller may have state that is preserved from a prior association). The controllers within such an NVM subsystem are distinguished by their controller identifier. The host may request a particular controller based on the Controller ID (refer to the CNTLID field in Figure 580).

In an NVM subsystem that supports the dynamic controller model, each controller is allocated by the NVM subsystem on demand with no state (e.g., Controller ID, Feature settings) preserved from prior associations. In this model, all controllers allocated to a specific host have the same state at the time the association is established, including Feature settings. The initial set of attached namespaces should be the same for all controllers that are allocated to a specific host and accessed via the same NVM subsystem port. The initial set of attached namespaces may differ among controllers that are each accessed via a different NVM subsystem port. Changes to a dynamic controller (e.g., attached namespaces, Feature settings) after the association is established do not impact other dynamic controllers in that NVM subsystem.

An association is established between a host and a controller when the host connects to a controller’s Admin Queue using the Fabrics Connect command (refer to section 6.3). Within the Connect command, the host specifies the Host NQN, NVM Subsystem NQN, Host Identifier, and may request a specific Controller ID (e.g., the static controller model is being used) or may request a connection to any available controller (e.g., the dynamic controller model is being used). A controller has only one association at a time.

While an association exists between a host and a controller, only that host may establish connections with I/O Queues of that controller. To establish a new connection with I/O Queues of that controller, the host sends subsequent Connect commands using the same NVM subsystem port, NVMe Transport type, and NVMe Transport address and specifies the:

- same Host NQN;
- same NVM Subsystem NQN;
- same Controller ID; and
- either the:
  - same Host Identifier; or
  - a Host Identifier value of 0h, if supported (refer to section 5.2.12.3.3).

<!-- Figure 580, coordinate:(0,0,0,0) -->
===== page_number= 38, page_type= body ====

An association between a host and controller is terminated if:
- the controller is shutdown as described in section 3.6.2;
- a Controller Level Reset occurs;
- the NVMe Transport connection is lost between the host and controller for the Admin Queue; or
- an NVMe Transport connection is lost between the host and controller for any I/O Queue and the host or controller does not support individual I/O Queue deletion (refer to section 3.3.2.4).

There is no explicit NVMe command that breaks the NVMe Transport association between a host and controller. The Disconnect command (refer to section 6.4) provides a method to delete an I/O Queue (refer to section 3.3.2.4). While a controller is associated with a host, that controller is busy, and no other associations may be made with that controller.

To use the dynamic controller model, the host specifies a controller identifier of FFFFh when using the Fabrics Connect command (refer to section 6.3) to establish an association with an NVM subsystem.

When using the static controller model with a fabric connected controller, the state that persists across associations is any state that persists across a Controller Level Reset. Additionally, different controllers may present different Feature settings or namespace attachments to the same host. The NVM subsystem may allocate particular controllers to specific hosts.

While allocation of static controllers to hosts are expected to be durable (so that hosts can expect to form associations to the same controllers repeatedly (e.g., after each host reboot)), the NVM subsystem may remove the host allocation of a controller that is not in use at any time for implementation specific reasons (e.g., controller resource reclamation, subsystem reconfiguration).



---

### 3.1.3 Controller Types

As shown in Figure 23, there are three types of controllers. An I/O controller (refer to section 3.1.3.1) is a controller that supports commands that provide access to user data stored on an NVM subsystem’s non-volatile storage medium and may support commands that provide management capabilities. An Administrative controller (refer to section 3.1.3.2) is a controller that supports commands that provide management capabilities, but does not support I/O commands that access to user data stored on an NVM subsystem’s non-volatile storage medium. A Discovery controller (refer to section 3.1.3.3) is a controller used in NVMe over Fabrics to provide access to a Discovery log page.

<!-- Figure 23: Controller Types, coordinate:(240,580,790,715) -->

The Controller Type (CNTRLTYPE) field in the Identify Controller data structure indicates a controller’s type. Regardless of controller type, all controllers implement one Admin Submission Queue and one Admin Completion Queue. Depending on the controller type, a controller may also support one or more I/O Submission Queues and I/O Completion Queues.

When using a memory-based transport implementation (e.g., PCIe), a host submits commands to a controller through pre-allocated Submission Queues. A controller is alerted to newly submitted commands through SQ Tail Doorbell register (refer to the NVMe over PCIe Transport Specification) writes. The difference between the previous doorbell register value and the current register write indicates the number of commands that were submitted.

A controller fetches commands from the Submission Queue(s) and processes them. Except for fused operations, there are no ordering restrictions for processing of commands within or across Submission
===== page_number= 39, page_type= body ====

Queues (i.e., a controller may arbitrarily order the processing of commands that have been fetched). Data associated with the processing of a command may or may not be committed to the NVM subsystem non-volatile storage medium in the order that commands are submitted. If a host has ordering requirements for the processing of commands, then that host is responsible for enforcing the ordering requirements.

A host submits commands of higher priorities to the appropriate Submission Queues. Priority is associated with the Submission Queue itself, thus the priority of the command is based on the Submission Queue to which that command was submitted. The controller arbitrates across the Submission Queues based on fairness and priority according to the arbitration scheme specified in section 3.4.4.

Upon completion of the command execution by the NVM subsystem, the controller presents completion queue entries to the host through the appropriate Completion Queues. Transport specific methods (e.g., PCIe interrupts) are used to notify the host of completion queue entries to process (refer to the applicable NVM Express Transport specification).

There are no ordering restrictions for completions to the host. Each completion queue entry identifies the Submission Queue Identifier and Command Identifier of the associated command. A host uses this information to correlate the completions with the commands submitted to the Submission Queue(s).

A host is responsible for creating I/O Submission Queues and I/O Completion Queues prior to using those queue pairs to submit commands to the controller. I/O Submission Queues and I/O Completion Queues are created using the Create I/O Submission Queue command (refer to section 5.3.2) and the Create I/O Completion Queue command (refer to section 5.3.1).



![Figure 23](restored_images/Figure_23.png)
**Figure 23**


---

### 3.1.3.1 I/O Controller

An I/O controller is a controller that supports commands that provide access to user data stored on an NVM subsystem’s non-volatile storage medium using an I/O command set and may support commands that provide management capabilities.

An I/O controller may simultaneously support multiple I/O Command Sets. The I/O Command Sets that the controller supports and which of these I/O Command Sets the controller simultaneously supports is reported in the Identify I/O Command Set data structure (refer to section 5.2.13.2.19). The contents of the Identify I/O Command Set data structure are not required to be the same for all controllers in an NVM subsystem.

Figure 24 shows an NVM subsystem with three I/O controllers. I/O controller one has two attached namespaces, private namespace A and shared namespace B. I/O controller two also has two attached namespaces, private namespace C and shared namespace B. I/O controller three has no attached namespaces. At some later point in time shared namespace B may be attached to I/O controller three.

<!-- Figure 24, coordinate:(0,0,0,0) -->
===== page_number= 40, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 24, coordinate:(209,115,790,408) -->
**Figure 24: NVM Subsystem with Three I/O Controllers**

**3.1.3.2 Administrative Controller**

An Administrative controller is a controller whose intended purpose is to provide NVM subsystem management capabilities. While an I/O controller may support these same management capabilities, an Administrative controller has fewer mandatory capabilities. Unlike an I/O controller, an Administrative controller does not support I/O commands. NVMe Transports may support a transport specific mechanism to allow an Administrative controller to load a dedicated NVMe management driver instead of a generic NVMe driver (refer to the applicable NVMe Transport binding specification for details).

Examples of management capabilities that may be supported by an Administrative controller include the following.

- Ability to efficiently poll NVM subsystem health status via NVMe-MI using the NVMe-MI Send command and the NVMe-MI Receive command (refer to the NVM Subsystem Health Status Poll section in the NVM Express Management Interface Specification);
- Ability to manage an NVMe enclosure via NVMe-MI using the NVMe-MI Send command and the NVMe-MI Receive command;
- Ability to manage NVM subsystem namespaces using the Namespace Attachment command and the Namespace Management command;
- Ability to perform virtualization management using the Virtualization Management command;
- Ability to reset an entire NVM subsystem using the NVM Subsystem Reset (NSSR) property if supported; and
- Ability to shutdown an entire NVM subsystem using the NVM Subsystem Shutdown (NSSD) property, if supported.

An Administrative controller shall not support I/O Queues. Namespaces shall not be attached to an Administrative controller.

An Administrative controller is required to support the mandatory Admin commands listed in Figure 28. An Administrative controller may support one or more I/O Command Sets. If an Administrative controller supports an I/O Command Set, then the I/O Command Set specific Admin commands associated with that I/O Command Set may also be supported. I/O commands shall not be supported since an Administrative controller only has an Admin Queue and no I/O Queues.

Figure 25 shows an NVM subsystem with one Administrative controller and two I/O controllers within an NVM subsystem that contains a non-volatile storage medium and namespaces. I/O controller one has two
===== page_number= 41, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

attached namespaces, private namespace A and shared namespace B. I/O controller two also has two attached namespaces, private namespace C and shared namespace B. An Administrative controller has no attached namespaces. The Administrative controller in this example may be used for tasks such as NVM subsystem namespace management and efficiently polling NVM subsystem health status via NVMe-MI. While this example shows a single Administrative controller, an NVM subsystem may support zero or more Administrative controllers.

**Figure 25: NVM Subsystem with One Administrative and Two I/O Controllers**

<!-- Figure 25, coordinate:(248,218,748,470) -->

Figure 26 shows an NVM subsystem with one Administrative controller within an NVM subsystem that contains no non-volatile storage medium or namespaces. The Administrative controller in this example may be used to manage an NVMe enclosure using NVMe-MI. Since the Administrative controller is used for a very specific dedicated purpose, the implementer of such an Administrative controller may choose to implement only the mandatory capabilities along with the NVMe-MI Send and NVMe-MI Receive commands.

**Figure 26: NVM Subsystem with One Administrative Controller**

<!-- Figure 26, coordinate:(408,610,588,762) -->



![Figure 24](restored_images/Figure_24.png)
**Figure 24**
![Figure 25](restored_images/Figure_25.png)
**Figure 25**
![Figure 26](restored_images/Figure_26.png)
**Figure 26**


---

### 3.1.3.3 Discovery Controller

A Discovery controller is a controller used in NVMe over Fabrics. A Discovery controller enables a host to discover other NVM subsystems or other Discovery subsystems. A Discovery controller only implements features related to Discovering other subsystems and does not implement I/O Queues, I/O commands, or expose namespaces. The features supported by the Discovery controller are defined in section 3.1.3.6.

If the Discovery subsystem provides a unique Discovery Service NQN (i.e., the NVM Subsystem NVMe Qualified Name (SUBNQN) field in that Discovery subsystem’s Identify Controller data structure contains a unique Discovery Service NQN value), then that Discovery subsystem shall support both the unique
===== page_number= 42, page_type= body ====

Discovery Service NQN and the well-known Discovery Service NQN (i.e., nqn.2014-08.org.nvmexpress.discovery) being specified in the Connect command (refer to section 6.3) from the host. If the Discovery subsystem does not provide a unique Discovery Service NQN (i.e., the SUBNQN field in that Discovery subsystem’s Identify Controller data structure contains the well-known Discovery Service NQN), then that Discovery subsystem shall support the well-known Discovery Service NQN being specified in the Connect command from the host.

In the Connect command to a Discovery subsystem that provides a unique Discovery Service NQN, the host may use either of the following:
- the well-known Discovery Service NQN; or
- the unique Discovery Service NQN of that Discovery subsystem.

In the Connect command to a Discovery subsystem that does not provide a unique Discovery Service NQN, the host uses the well-known Discovery Service NQN.

The method that a host uses to obtain the fabric information necessary to connect to a Discovery controller using the well-known Discovery Service NQN or the unique NQN via the NVMe Transport may be:
a) implementation specific;
b) fabric specific;
c) known in advance (e.g., a well-known address);
d) administratively configured; or
e) for IP-based fabrics, Automated Discovery of Discovery Controllers for IP-based Fabrics (refer to section 8.3.1) may be used.

The Discovery log page provided by a Discovery controller contains one or more entries. Each entry specifies information necessary for the host to connect to an NVM subsystem. An entry may be associated with an NVM subsystem that exposes namespaces or a referral to another Discovery Service. There are no ordering requirements for log page entries within the Discovery log page.

Discovery controller(s) may provide different log page contents depending on the Host NQN provided (e.g., different NVM subsystems may be accessible to different hosts). The set of Discovery Log Page Entries should include all applicable addresses on the same fabric as the Discovery Service and may include addresses on other fabrics.

Discovery controllers that support explicit persistent connections shall support both the Asynchronous Event Request command and the Keep Alive command (refer to sections 5.2.2 and 5.2.14 respectively). A host requests an explicit persistent connection to a Discovery controller and Asynchronous Event Notifications from the Discovery controller on that persistent connection by specifying a non-zero Keep Alive Timer value in the Connect command. If the Connect command specifies a non-zero Keep Alive Timer value and the Discovery controller does not support Asynchronous Events, then the Discovery controller shall return a status value of Connect Invalid Parameters (refer to Figure 582) for the Connect command. Discovery controllers shall indicate support for Discovery Log Change Notifications in the Identify Controller data structure (refer to Figure 328).

Discovery controllers that do not support explicit persistent connections shall not support Keep Alive commands and may use a fixed Discovery controller activity timeout value (e.g., 2 minutes). If no commands are received by such a Discovery controller within that time period, the controller may perform the actions for Keep Alive Timer expiration defined in section 3.9.5.

A Discovery controller shall not support the Disconnect command.

A Discovery log page with multiple Discovery Log Page Entries for the same NVM subsystem indicates that there are multiple fabric paths to the NVM subsystem, and/or that multiple static controllers may share a fabric path. The host may use this information to form multiple associations to controllers within an NVM subsystem.

Multiple Discovery Log Page Entries for the same NVM subsystem with different Port ID values indicates that the resulting NVMe Transport connections are independent with respect to NVM subsystem port
===== page_number= 43, page_type= body ==___

hardware failures. A host that uses a single association should pick a record to attach to an NVM subsystem. A host that uses multiple associations should choose different ports.

A transport specific method may exist to indicate changes to a Discovery controller.

Controller IDs in the range FFF0h to FFFFh are not allocated as valid Controller IDs on completion of a Connect command, as described in section 6.3. Figure 27 defines these Controller IDs.

**Figure 27: Controller IDs FFF0h to FFFFh**

<!-- Figure 27, coordinate:(114,215,880,380) -->

| Controller ID | Definition |
|---------------|------------|
| FFF0h to FFFCh | Reserved. Use of this value in a Connect command results in a status code of Connect Invalid Parameters being returned, as described in section 6.3. |
| FFFDh | This value in the Controller ID (CNTLID) field of the Registered Controller data structure or Registered Controller Extended data structure for a dispersed namespace indicates that the controller is not contained in the same participating NVM subsystem as the controller processing the command (refer to section 8.1.10.6). Use of this value in a Connect command results in a status code of Connect Invalid Parameters being returned, as described in section 6.3. |
| FFFEh | This value is sent in a Connect command to specify that any available static controller is allowed to be allocated. |
| FFFFh | This value is sent in a Connect command to specify that any available dynamic controller is allowed to be allocated. |

The Controller ID values returned in the Discovery Log Page Entries indicate whether an NVM subsystem supports the dynamic or static controller model. The controller ID value of FFFFh is used for NVM subsystems that support the dynamic controller model indicating that any available controller may be returned. The Controller ID value of FFFEh is used for NVM subsystems that support the static controller model indicating that any available controller may be returned. An NVM subsystem supports the dynamic controller model if Discovery Log Page Entries use the Controller ID value of FFFFh. An NVM subsystem supports the static controller model if Discovery Log Page Entries use a Controller ID value that is less than FFFFh. The Identify Controller data structure also indicates whether an NVM subsystem is dynamic or static.

If an NVM subsystem implements the dynamic controller model, then multiple Discovery Log Page Entries (refer to Figure 310) with the Controller ID set to FFFFh may be returned for that NVM subsystem (e.g., to indicate multiple NVM subsystem ports) in the Discovery log page. If an NVM subsystem implements the static controller model, then multiple Discovery Log Page Entries that indicate different Controller ID values may be returned for that NVM subsystem in the Discovery log page. If an NVM subsystem that implements the static controller model includes any Discovery Log Page Entries that indicate a Controller ID of FFFEh, then the host should remember the Controller ID returned from the Fabrics Connect command and re-use the allocated Controller ID for future associations to that particular controller.



| Controller ID | Definition |
|---------------|------------|
| FFF0h to FFFCh | Reserved. Use of this value in a Connect command results in a status code of Connect Invalid Parameters being returned, as described in section 6.3. |
| FFFDh | This value in the Controller ID (CNTLID) field of the Registered Controller data structure or Registered Controller Extended data structure for a dispersed namespace indicates that the controller is not contained in the same participating NVM subsystem as the controller processing the command (refer to section 8.1.10.6). Use of this value in a Connect command results in a status code of Connect Invalid Parameters being returned, as described in section 6.3. |
| FFFEh | This value is sent in a Connect command to specify that any available static controller is allowed to be allocated. |
| FFFFh | This value is sent in a Connect command to specify that any available dynamic controller is allowed to be allocated. |


---

### 3.1.3.3.1 Discovery Controller Asynchronous Event Configuration

Discovery controllers that support Asynchronous Event Notifications shall implement the Get Features and Set Features commands. A Discovery controller shall enable Asynchronous Discovery Log Event Notifications, if a non-zero Keep Alive Timeout (KATO) value is received in the Connect command (refer to section 6.3) sent to that controller.

Figure 409 defines Discovery controller Asynchronous Event Notifications.



---

### 3.1.3.3.2 Discovery Controller Asynchronous Event Information – Requests and Notifications

If a Discovery controller detects an event that changes the information reported by the Discovery log page or the Host Discovery log page about which a host has requested notification, then the Discovery controller shall send an Asynchronous Event with the:

- Asynchronous Event Type field set to Notice (i.e., 2h);
- Log Page Identifier field set to either Discovery (i.e., 70h) or Host Discovery (i.e., 71h) depending on which log page has changed; and

---
===== page_number= 44, page_type= body ====

- Asynchronous Event Information field set as defined in Figure 154.

As a result of a Discovery controller updating Discovery log page(s), that Discovery controller shall send a Discovery Log Page Change Asynchronous Event notification (i.e., the Asynchronous Event Information field set to F0h) to each entity that has requested asynchronous event notifications of this type (refer to Figure 154).

As a result of a Discovery controller updating Host Discovery log page(s), that Discovery controller shall send a Host Discovery Log Page Change Asynchronous Event notification (i.e., the Asynchronous Event Information field set to F1h) to each entity that has requested asynchronous event notifications of this type (refer to Figure 154).



---

### 3.1.3.3.3 Discovery Controller Initialization

The initialization process for Discovery controllers is described in section 3.5.2.1.



---

### 3.1.3.4 Command Support Requirements

Figure 28, Figure 29, and Figure 30 define commands that are mandatory, optional, and prohibited for an I/O controller, Administrative controller, and Discovery controller. I/O Command Set specific command support requirements are described within NVM Express I/O Command Set specifications. Since an Administrative controller does not support I/O queues, I/O Command Set specific commands that are not Admin commands are not supported by an Administrative controller.

A host may utilize the Commands Supported and Effects log page to determine optional commands that are supported by a controller.

<!-- Figure 28: Admin Command Support Requirements, coordinate:(114,445,885,890) -->
**Figure 28: Admin Command Support Requirements**

| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Delete I/O Submission Queue | 00h | M⁹ | P | P | 5.3.4 |
| Create I/O Submission Queue | 01h | M⁹ | P | P | 5.3.2 |
| Get Log Page | 02h | M | M | M | 5.2.12 |
| Delete I/O Completion Queue | 04h | M⁹ | P | P | 5.3.3 |
| Create I/O Completion Queue | 05h | M⁹ | P | P | 5.3.1 |
| Identify | 06h | M | M | M | 5.2.13 |
| Abort | 08h | M | O | O | 5.2.1 |
| Set Features | 09h | M | O⁴ | Note 6 | 5.2.26 |
| Get Features | 0Ah | M | O⁴ | Note 6 | 5.2.11 |
| Asynchronous Event Request | 0Ch | M | O⁵ | Note 6 | 5.2.2 |
| Namespace Management | 0Dh | O | O | P | 5.2.21 |
| Firmware Commit | 10h | O | O | P | 5.2.8 |
| Firmware Image Download | 11h | O | O | P | 5.2.9 |
| Device Self-test | 14h | O | O | P | 5.2.5 |
| Namespace Attachment | 15h | O | O | P | 5.2.20 |
| Keep Alive | 18h | M² | M² | Note 6 | 5.2.14 |
| Directive Send | 19h | O | O | P | 5.2.7 |
| Directive Receive | 1Ah | O | O | P | 5.2.6 |
| Virtualization Management | 1Ch | O | O | P | 5.3.6 |
| NVMe-MI Send | 1Dh | O | O | P | 5.2.19 |
| NVMe-MI Receive | 1Eh | O | O | P | 5.2.18 |
| Capacity Management | 20h | O | O | P | 5.2.3 |
| Discovery Information Management | 21h | P | P | M⁷ | 5.4.4 |

¹ Controller Support Requirements: M = Mandatory, O = Optional, P = Prohibited  
² Applies to I/O and Administrative controllers only  
⁴ Applies to Administrative controller only  
⁵ Applies to Administrative controller only  
⁶ See Note 6 in specification  
⁷ Applies to Discovery controller only  
⁹ Applies to I/O controller only  

Note: The table includes footnotes and references as specified in the document. The actual coordinate values for the figure are estimated based on typical layout and may vary slightly.
===== page_number= 45, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 28, coordinate:(114,105,880,599) -->
Figure 28: Admin Command Support Requirements

| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Fabric Zoning Receive | 22h | P | P | M⁷ | 5.4.6 |
| Lockdown | 24h | O | O | P | 5.2.15 |
| Fabric Zoning Lookup | 25h | P | P | M⁷ | 5.4.5 |
| Clear Exported NVM Resource Configuration | 28h | P | O | P | 5.4.1 |
| Fabric Zoning Send | 29h | P | P | M⁷ | 5.4.7 |
| Create Exported NVM Subsystem | 2Ah | P | O | P | 5.4.2 |
| Manage Exported NVM Subsystem | 2Dh | P | O | P | 5.4.9 |
| Manage Exported Namespace | 31h | P | O | P | 5.4.8 |
| Manage Exported Port | 35h | P | O | P | 5.4.10 |
| Cross-Controller Reset | 38h | O¹⁰ | O¹⁰ | O¹¹ | 5.4.3 |
| Send Discovery Log Page | 39h | P | P | M⁷ | 5.4.11 |
| Track Send | 3Dh | O | O | P | 5.2.28 |
| Track Receive | 3Eh | O | O | P | 5.2.27 |
| Migration Send | 41h | O | O | P | 5.2.17 |
| Migration Receive | 42h | O | O | P | 5.2.16 |
| Controller Data Queue | 45h | O | O | P | 5.2.4 |
| Doorbell Buffer Config | 7Ch | O | O | P | 5.3.5 |
| **I/O Command Set specific Admin commands** | | | | | |
| Format NVM | 80h | O | O | P | 5.2.10 |
| Security Send | 81h | O | O | P | 5.2.25 |
| Security Receive | 82h | O | O | P | 5.2.23 |
| Sanitize | 84h | O³ | O³ | P | 5.2.22 |
| Sanitize Namespace | 8Ch | O | O | P | 5.2.23 |
| I/O Command Set specific Admin command | 85h | Note 8 | P | P | Note 8 |
| | 86h | | | | |
| | 88h | | | | |
| | 89h | | | | |

¹ Controller Support Requirements: P = Required, O = Optional, M = Mandatory for Discovery (see Note 7)

Note 7: Mandatory for Discovery controllers only.

Note 8: These commands are specific to the I/O Command Set and are defined in the respective I/O Command Set specification.

Note 10: Optional for Cross-Controller Reset in I/O and Administrative contexts.

Note 11: Optional for Cross-Controller Reset in Discovery context.

Note 3: Optional for Sanitize command in I/O and Administrative contexts.

The table lists admin commands with their combined opcode values, support requirements (I/O, Administrative, Discovery), and references to relevant sections in the specification. Commands are categorized into general admin commands and I/O Command Set specific admin commands. Support requirements are marked as P (Required), O (Optional), or M (Mandatory for Discovery). Some entries include footnotes (e.g., ⁷, ¹⁰, ¹¹, ³) that provide additional context or conditions for support.
===== page_number= 46, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 28, coordinate:(114,104,882,382) -->
**Figure 28: Admin Command Support Requirements**

| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Vendor Specific | | O | O | O | |

**Notes:**
1. O/M/P definition: O = Optional, M = Mandatory, P = Prohibited
2. Prohibited if the Keep Alive Timer feature is not supported (refer to section 3.9).
3. Prohibited for an Exported NVM Subsystem (refer to section 8.3.4).
4. Mandatory if any of the features in Figure 32 are implemented.
5. Mandatory if Telemetry Log, Firmware Commit, or SMART / Health Critical Warnings are supported.
6. For Discovery controllers that support explicit persistent connections, this command is mandatory. For Discovery controllers that do not support explicit persistent connections, this command is prohibited.
7. Mandatory for CDCs and optional for Discovery controllers that are not a CDC.
8. Refer to the applicable NVM Express I/O Command Set specification.
9. Mandatory for NVMe over PCIe. This command is not supported for NVMe over Fabrics.
10. Optional for message-based controllers. Prohibited for memory-based controllers.
11. Optional for Discovery controllers that support explicit persistent connections. Prohibited for Discovery controllers that do not support explicit persistent connections.

<!-- Figure 29, coordinate:(114,418,882,649) -->
**Figure 29: Fabrics Command Support Requirements**

| Command | Opcode Value | Fabrics Command Type | Controller Support Requirements¹,² | Reference |
|---------|--------------|----------------------|------------------------------------|-----------|
|         |              |                      | I/O | Administrative | Discovery |           |
| Property Set | | 00h | M | M | M | 6.6 |
| Connect | | 01h | M | M | M | 6.3 |
| Property Get | | 04h | M | M | M | 6.5 |
| Authentication Send | | 05h | O | O | O | 6.2 |
| Authentication Receive | | 06h | O | O | O | 6.1 |
| Disconnect | | 08h | O | P | P | 6.4 |
| Vendor Specific | 7Fh | C0h to FFh | O | O | O | |

**Notes:**
1. O/M/P definition: O = Optional, M = Mandatory, P = Prohibited
2. For NVMe over PCIe implementations, all Fabrics commands are prohibited. For NVMe over Fabrics implementations, the commands are as noted in the table.

<!-- Figure 30, coordinate:(114,670,882,892) -->
**Figure 30: Common I/O Command Support Requirements**

| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Flush | 00h | M | P | P | 7.2 |
| Reservation Register | 0Dh | O² | P | P | 7.6 |
| Reservation Report | 0Eh | O² | P | P | 7.8 |
| Reservation Acquire | 11h | O² | P | P | 7.5 |
| I/O Management Receive | 12h | O³ | P | P | 7.3 |
| Reservation Release | 15h | O² | P | P | 7.7 |
| Cancel | 18h | O | P | P | 7.1 |
| I/O Management Send | 1Dh | O³ | P | P | 7.4 |

46
===== page_number= 47, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 30, coordinate:(114,104,880,262) -->
**Figure 30: Common I/O Command Support Requirements**

| Command | Combined Opcode Value | Controller Support Requirements<sup>1</sup> | Reference |
|---------|------------------------|---------------------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Vendor Specific | | O | O | O |           |

**Notes:**
1. O/M/P definition: O = Optional, M = Mandatory, P = Prohibited
2. Mandatory if reservations are supported as indicated in the Identify Controller data structure.
3. Mandatory for controllers that support the Flexible Data Placement capability (refer to section 8.1.11). Refer to the FDPS bit in Figure 328.

---



| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Delete I/O Submission Queue | 00h | M⁹ | P | P | 5.3.4 |
| Create I/O Submission Queue | 01h | M⁹ | P | P | 5.3.2 |
| Get Log Page | 02h | M | M | M | 5.2.12 |
| Delete I/O Completion Queue | 04h | M⁹ | P | P | 5.3.3 |
| Create I/O Completion Queue | 05h | M⁹ | P | P | 5.3.1 |
| Identify | 06h | M | M | M | 5.2.13 |
| Abort | 08h | M | O | O | 5.2.1 |
| Set Features | 09h | M | O⁴ | Note 6 | 5.2.26 |
| Get Features | 0Ah | M | O⁴ | Note 6 | 5.2.11 |
| Asynchronous Event Request | 0Ch | M | O⁵ | Note 6 | 5.2.2 |
| Namespace Management | 0Dh | O | O | P | 5.2.21 |
| Firmware Commit | 10h | O | O | P | 5.2.8 |
| Firmware Image Download | 11h | O | O | P | 5.2.9 |
| Device Self-test | 14h | O | O | P | 5.2.5 |
| Namespace Attachment | 15h | O | O | P | 5.2.20 |
| Keep Alive | 18h | M² | M² | Note 6 | 5.2.14 |
| Directive Send | 19h | O | O | P | 5.2.7 |
| Directive Receive | 1Ah | O | O | P | 5.2.6 |
| Virtualization Management | 1Ch | O | O | P | 5.3.6 |
| NVMe-MI Send | 1Dh | O | O | P | 5.2.19 |
| NVMe-MI Receive | 1Eh | O | O | P | 5.2.18 |
| Capacity Management | 20h | O | O | P | 5.2.3 |
| Discovery Information Management | 21h | P | P | M⁷ | 5.4.4 |

| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Fabric Zoning Receive | 22h | P | P | M⁷ | 5.4.6 |
| Lockdown | 24h | O | O | P | 5.2.15 |
| Fabric Zoning Lookup | 25h | P | P | M⁷ | 5.4.5 |
| Clear Exported NVM Resource Configuration | 28h | P | O | P | 5.4.1 |
| Fabric Zoning Send | 29h | P | P | M⁷ | 5.4.7 |
| Create Exported NVM Subsystem | 2Ah | P | O | P | 5.4.2 |
| Manage Exported NVM Subsystem | 2Dh | P | O | P | 5.4.9 |
| Manage Exported Namespace | 31h | P | O | P | 5.4.8 |
| Manage Exported Port | 35h | P | O | P | 5.4.10 |
| Cross-Controller Reset | 38h | O¹⁰ | O¹⁰ | O¹¹ | 5.4.3 |
| Send Discovery Log Page | 39h | P | P | M⁷ | 5.4.11 |
| Track Send | 3Dh | O | O | P | 5.2.28 |
| Track Receive | 3Eh | O | O | P | 5.2.27 |
| Migration Send | 41h | O | O | P | 5.2.17 |
| Migration Receive | 42h | O | O | P | 5.2.16 |
| Controller Data Queue | 45h | O | O | P | 5.2.4 |
| Doorbell Buffer Config | 7Ch | O | O | P | 5.3.5 |
| **I/O Command Set specific Admin commands** | | | | | |
| Format NVM | 80h | O | O | P | 5.2.10 |
| Security Send | 81h | O | O | P | 5.2.25 |
| Security Receive | 82h | O | O | P | 5.2.23 |
| Sanitize | 84h | O³ | O³ | P | 5.2.22 |
| Sanitize Namespace | 8Ch | O | O | P | 5.2.23 |
| I/O Command Set specific Admin command | 85h | Note 8 | P | P | Note 8 |
| | 86h | | | | |
| | 88h | | | | |
| | 89h | | | | |

| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Vendor Specific | | O | O | O | |

| Command | Opcode Value | Fabrics Command Type | Controller Support Requirements¹,² | Reference |
|---------|--------------|----------------------|------------------------------------|-----------|
|         |              |                      | I/O | Administrative | Discovery |           |
| Property Set | | 00h | M | M | M | 6.6 |
| Connect | | 01h | M | M | M | 6.3 |
| Property Get | | 04h | M | M | M | 6.5 |
| Authentication Send | | 05h | O | O | O | 6.2 |
| Authentication Receive | | 06h | O | O | O | 6.1 |
| Disconnect | | 08h | O | P | P | 6.4 |
| Vendor Specific | 7Fh | C0h to FFh | O | O | O | |

| Command | Combined Opcode Value | Controller Support Requirements¹ | Reference |
|---------|------------------------|----------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Flush | 00h | M | P | P | 7.2 |
| Reservation Register | 0Dh | O² | P | P | 7.6 |
| Reservation Report | 0Eh | O² | P | P | 7.8 |
| Reservation Acquire | 11h | O² | P | P | 7.5 |
| I/O Management Receive | 12h | O³ | P | P | 7.3 |
| Reservation Release | 15h | O² | P | P | 7.7 |
| Cancel | 18h | O | P | P | 7.1 |
| I/O Management Send | 1Dh | O³ | P | P | 7.4 |

| Command | Combined Opcode Value | Controller Support Requirements<sup>1</sup> | Reference |
|---------|------------------------|---------------------------------------------|-----------|
|         |                        | I/O | Administrative | Discovery |           |
| Vendor Specific | | O | O | O |           |


---

### 3.1.3.5 Log Page Support Requirements

Figure 31 defines log pages that are mandatory, optional, and prohibited for an I/O controller, Administrative controller, and Discovery controller. I/O Command Set specific log page support requirements are described within NVM Express I/O Command Set specifications.

<!-- Figure 31, coordinate:(114,377,880,898) -->
**Figure 31: Log Page Support Requirements**

| Log Page Name | Log Page Identifier | Controller Support Requirements<sup>1</sup> | Reference |
|---------------|---------------------|---------------------------------------------|-----------|
|               |                     | I/O | Administrative | Discovery |           |
| Supported Log Pages | 00h | M<sup>3</sup> | M<sup>3</sup> | M | 5.2.12.1.1 |
| Error Information | 01h | M | M | O | 5.2.12.1.2 |
| SMART / Health Information (Controller scope) | 02h | M | O | P | 5.2.12.1.3 |
| SMART / Health Information (Namespace scope) | 02h | O | O | P |           |
| Firmware Slot Information | 03h | M | O | P | 5.2.12.1.4 |
| Changed Attached Namespace List | 04h | O | O | P | 5.2.12.1.5 |
| Commands Supported and Effects | 05h | M<sup>3</sup> | M | M | 5.2.12.1.6 |
| Device Self-test | 06h | O | O | P | 5.2.12.1.7 |
| Telemetry Host-Initiated | 07h | O | O | P | 5.2.12.1.8 |
| Telemetry Controller-Initiated | 08h | O | O<sup>8</sup> | P | 5.2.12.1.9 |
| Endurance Group Information | 09h | O | O | P | 5.2.12.1.10 |
| Predictable Latency Per NVM Set | 0Ah | O | O<sup>8</sup> | P | 5.2.12.1.11 |
| Predictable Latency Event Aggregate | 0Bh | O | O<sup>8</sup> | P | 5.2.12.1.12 |
| Asymmetric Namespace Access | 0Ch | O | P | P | 5.2.12.1.13 |
| Persistent Event | 0Dh | O | O | P | 5.2.12.1.14 |
| LBA Status Information | 0Eh | Refer to the NVM Express NVM Command Set Specification | | | |
| Endurance Group Event Aggregate | 0Fh | O | O | P | 5.2.12.1.15 |
| Media Unit Status | 10h | O<sup>2</sup> | P | P | 5.2.12.1.16 |
| Supported Capacity Configuration List | 11h | O<sup>2</sup> | P | P | 5.2.12.1.17 |
| Feature Identifiers Supported and Effects | 12h | M<sup>3</sup> | M<sup>3,9</sup> | M<sup>9</sup> | 5.2.12.1.18 |
| NVMe-MI Commands Supported and Effects | 13h | M<sup>3,7</sup> | M<sup>3,7</sup> | O | 5.2.12.1.19 |
| Command and Feature Lockdown | 14h | O | O | P | 5.2.12.1.20 |

---
===== page_number= 48, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 31, coordinate:(113,103,883,557) -->
Figure 31: Log Page Support Requirements

| Log Page Name | Log Page Identifier | Controller Support Requirements<sup>1</sup> | Reference |
|---------------|---------------------|---------------------------------------------|-----------|
|               |                     | I/O | Administrative | Discovery |           |
| Boot Partition | 15h | O | O | P | 5.2.12.1.21 |
| Rotational Media Information | 16h | O | P | P | 5.2.12.1.22 |
| Dispersed Namespace Participating NVM Subsystems | 17h | O | O | P | 5.2.12.1.23 |
| Management Address List | 18h | O | O | O | 5.2.12.1.24 |
| Physical Interface Receiver Eye Opening Measurement | 19h | O<sup>4</sup> | O<sup>4</sup> | P | Note 11 |
| Reachability Groups | 1Ah | O<sup>6</sup> | P | P | 5.2.12.1.25 |
| Reachability Associations | 1Bh | O<sup>6</sup> | P | P | 5.2.12.1.26 |
| Changed Allocated Namespace List | 1Ch | O | O | P | 5.2.12.1.27 |
| Device Personalities | 1Dh | O | O | P | 5.2.12.1.28 |
| Cross-Controller Reset | 1Eh | O<sup>12</sup> | O<sup>12</sup> | O<sup>13</sup> | 5.2.12.3.1 |
| Lost Host Communication | 1Fh | O<sup>12</sup> | O<sup>12</sup> | O<sup>13</sup> | 5.2.12.3.2 |
| FDP Configurations | 20h | O<sup>5</sup> | P | P | 5.2.12.1.29 |
| Reclaim Unit Handle Usage | 21h | O<sup>5</sup> | P | P | 5.2.12.1.30 |
| FDP Statistics | 22h | O<sup>5</sup> | P | P | 5.2.12.1.31 |
| FDP Events | 23h | O<sup>5</sup> | P | P | 5.2.12.1.32 |
| Power Measurement | 25h | O | O | P | 5.2.12.1.33 |
| Discovery | 70h | P | P | M | 5.2.12.3.3 |
| Host Discovery | 71h | P | P | O | 5.2.12.3.4 |
| AVE Discovery | 72h | P | P | O | 5.2.12.3.5 |
| Pull Model DDC Request | 73h | P | P | M<sup>10</sup> | 5.2.12.3.6 |
| Sanitize Namespace Status List | 7Fh | O | O | P | 5.2.12.1.34 |

48
===== page_number= 49, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 31, coordinate:(114,105,881,568) -->
**Figure 31: Log Page Support Requirements**

| Log Page Name | Log Page Identifier | Controller Support Requirements¹ | Reference |
|---------------|---------------------|----------------------------------|-----------|
| Reservation Notification | 80h | I/O: O | Administrative: P | Discovery: P | 5.2.12.1.34 |
| Sanitize Status | 81h | I/O: O | Administrative: O⁸ | Discovery: P | 5.2.12.1.36 |
| Program List | 82h | | | | |
| Downloadable Program Types List | 83h | | | | Refer to the NVM Express Computational Programs Command Set Specification |
| Memory Range Set List | 84h | | | | |
| | 85h to B5h | | | | Refer to the applicable NVM Express I/O Command Set specification |
| Changed Zone List | B6h | | | | Refer to the NVM Express Zoned Namespace Command Set Specification |
| Vendor Specific | C0h to FFh | | | | |

**Notes:**
1. O/M/P definition: O = Optional, M = Mandatory, P = Prohibited
2. Mandatory for controllers that support Fixed Capacity Management (refer to section 8.1.4.2).
3. Optional for NVM Express revision 1.4 and earlier.
4. If this log page is not described for a specific physical interface (refer to the applicable NVM Express Transport specification), then this log page is prohibited for that transport.
5. Mandatory for controllers that support the Flexible Data Placement capability (refer to section 8.1.11). Refer to the FDPS bit in Figure 328.
6. Mandatory for controllers that support Reachability Reporting (refer to section 8.1.21).
7. Optional if the NVMe-MI Send command and the NVMe-MI Receive command are not supported (refer to Figure 28).
8. Prohibited for an Exported NVM subsystem (refer to section 8.3.4).
9. Optional if the Set Features command is not supported (refer to Figure 28).
10. Mandatory for CDCs and prohibited for Discovery controllers that are not a CDC.
11. Refer to the applicable NVM Express Transport specification.
12. Optional for message-based controllers. Prohibited for memory-based controllers.
13. Optional for Discovery controllers that support explicit persistent connections. Prohibited for Discovery controllers that do not support explicit persistent connections.

---

**3.1.3.6 Feature Support Requirements**

Figure 32 defines features that are mandatory, optional, and prohibited for an I/O controller, Administrative controller, and Discovery controller. If any feature is supported, then the Set Features command and the Get Features command shall be supported. I/O Command Set specific feature support requirements are described within NVM Express I/O Command Set specifications.

<!-- Figure 32, coordinate:(114,681,881,897) -->
**Figure 32: Feature Support Requirements**

| Feature Name | Feature Identifier | Controller Support Requirements¹ | Reference |
|--------------|--------------------|----------------------------------|-----------|
| Arbitration | 01h | I/O: M | Administrative: P | Discovery: P | 5.2.26.1.1 |
| Power Management | 02h | I/O: M | Administrative: O | Discovery: P | 5.2.26.1.2 |
| LBA Range Type | 03h | | | | Refer to the NVM Express NVM Command Set Specification |
| Temperature Threshold | 04h | I/O: M | Administrative: O | Discovery: P | 5.2.26.1.3 |
| Error Recovery | 05h | | | | Refer to the NVM Express NVM Command Set Specification |
| Volatile Write Cached | 06h | I/O: O | Administrative: P | Discovery: P | 5.2.26.1.4 |
| Number of Queues | 07h | I/O: M | Administrative: P | Discovery: P | 5.2.26.2.1 |
| Interrupt Coalescing | 08h | I/O: Note 2 | Administrative: Note 2 | Discovery: P | 5.2.26.2.2 |
| Interrupt Vector Configuration | 09h | I/O: Note 2 | Administrative: Note 2 | Discovery: P | 5.2.26.2.3 |

---

49
===== page_number= 50, page_type= body ====

<!-- Figure 32, coordinate:(114,106,881,844) -->
NVM Express® Base Specification, Revision 2.3

**Figure 32: Feature Support Requirements**

| Feature Name | Feature Identifier | Controller Support Requirements<sup>1</sup> | Reference |
|--------------|--------------------|---------------------------------------------|-----------|
|              |                    | **I/O** | **Administrative** | **Discovery** |           |
| Write Atomicity Normal | 0Ah | Refer to the NVM Express NVM Command Set Specification |           |
| Asynchronous Event Configuration | 0Bh | M | O<sup>8</sup> | M<sup>10</sup> | 5.2.26.1.5 |
| Autonomous Power State Transition | 0Ch | O | O | P | 5.2.26.1.6 |
| Host Memory Buffer | 0Dh | O | O | P | 5.2.26.2.4 |
| Timestamp | 0Eh | O | O | P | 5.2.26.1.7 |
| Keep Alive Timer | 0Fh | M<sup>7</sup> | M<sup>7</sup> | M<sup>10</sup> | 5.2.26.1.8 |
| Host Controlled Thermal Management | 10h | O | O | P | 5.2.26.1.9 |
| Non-Operational Power State Config | 11h | O | O | P | 5.2.26.1.10 |
| Read Recovery Level Config | 12h | O | O | P | 5.2.26.1.11 |
| Predictable Latency Mode Config | 13h | O | O<sup>9</sup> | P | 5.2.26.1.12 |
| Predictable Latency Mode Window | 14h | O | O<sup>9</sup> | P | 5.2.26.1.13 |
| LBA Status Information Report Interval | 15h | Refer to the NVM Express NVM Command Set Specification |           |
| Host Behavior Support | 16h | O | O | P | 5.2.26.1.14 |
| Sanitize Config | 17h | O | O<sup>9</sup> | P | 5.2.26.1.15 |
| Endurance Group Event Configuration | 18h | O | O<sup>9</sup> | P | 5.2.26.1.16 |
| I/O Command Set Profile | 19h | O | P | P | 5.2.26.1.17 |
| Spinup Control | 1Ah | O | P | P | 5.2.26.1.18 |
| Power Loss Signaling Config | 1Bh | O | O | P | 5.2.26.1.19 |
| Performance Characteristics | 1Ch | Refer to the NVM Express NVM Command Set Specification |           |
| Flexible Data Placement | 1Dh | O<sup>6</sup> | P | P | 5.2.26.1.20 |
| Flexible Data Placement Events | 1Eh | O<sup>6</sup> | P | P | 5.2.26.1.21 |
| Namespace Admin Label | 1Fh | O | O | P | 5.2.26.1.22 |
| Key Value Configuration | 20h | Refer to the NVM Express Key Value Command Set Specification |           |
| Controller Data Queue | 21h | O | O | P | 5.2.26.1.23 |
| Configurable Device Personality | 22h | O | O | P | 5.2.26.1.24 |
| Power Limit | 23h | O | O | P | 5.2.26.1.25 |
| Power Threshold | 24h | O | O | P | 5.2.26.1.26 |
| Power Measurement | 25h | O | O | P | 5.2.26.1.27 |
| Embedded Management Controller Address | 78h | O | O | O | 5.2.26.1.28 |
| Host Management Agent Address | 79h | O | O | O | 5.2.26.1.29 |
| Enhanced Controller Metadata | 7Dh | O<sup>5</sup> | O<sup>5</sup> | O | 5.2.26.1.30.1 |
| Controller Metadata | 7Eh | O<sup>5</sup> | O<sup>5</sup> | O | 5.2.26.1.30.2 |
| Namespace Metadata | 7Fh | O<sup>5</sup> | O<sup>5</sup> | O | 5.2.26.1.30.3 |
| Software Progress Marker | 80h | O | O | P | 5.2.26.1.31 |
| Host Identifier | 81h | O<sup>3</sup> | O | P | 5.2.26.1.32 |
| Reservation Notification Mask | 82h | O<sup>4</sup> | P | P | 5.2.26.1.33 |
| Reservation Persistence | 83h | O<sup>4</sup> | P | P | 5.2.26.1.34 |

50
===== page_number= 51, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 32, coordinate:(114,104,880,395) -->
**Figure 32: Feature Support Requirements**

| Feature Name                     | Feature Identifier | Controller Support Requirements¹ | Reference       |
|----------------------------------|--------------------|----------------------------------|-----------------|
|                                  |                    | I/O              | Administrative | Discovery     |                 |
| Namespace Write Protection Config | 84h                | O                | O              | P             | 5.2.26.1.35     |
| Boot Partition Write Protection Config | 85h              | O                | O              | P             | 5.2.26.1.36     |

**Notes:**
1. O/M/P definition: O = Optional, M = Mandatory, P = Prohibited
2. Mandatory for NVMe over PCIe. This feature is not supported for NVMe over Fabrics.
3. Mandatory if reservations are supported as indicated in the Identify Controller data structure.
4. Mandatory if reservations are supported by the namespace as indicated by a non-zero value in the Reservation Capabilities (RESCAP) field in the Identify Namespace data structure.
5. Optional for NVM subsystems that do not implement a Management Endpoint. For NVM subsystems that implement any Management Endpoint refer to the NVM Express Management Interface Specification.
6. Mandatory for controllers that support the Flexible Data Placement capability (refer to section 8.1.11). Refer to the FDPS bit in Figure 328.
7. Optional if not required by the NVMe Transport (refer to section 3.9).
8. Mandatory if Telemetry Log, Firmware Commit or SMART / Health Critical Warnings are supported.
9. Prohibited for an Exported NVM Subsystem (refer to section 8.3.4).
10. For Discovery controllers that support explicit persistent connections, this feature is mandatory. For Discovery controllers that do not support explicit persistent connections, this feature is prohibited.

---



| Log Page Name | Log Page Identifier | Controller Support Requirements<sup>1</sup> | Reference |
|---------------|---------------------|---------------------------------------------|-----------|
|               |                     | I/O | Administrative | Discovery |           |
| Supported Log Pages | 00h | M<sup>3</sup> | M<sup>3</sup> | M | 5.2.12.1.1 |
| Error Information | 01h | M | M | O | 5.2.12.1.2 |
| SMART / Health Information (Controller scope) | 02h | M | O | P | 5.2.12.1.3 |
| SMART / Health Information (Namespace scope) | 02h | O | O | P |           |
| Firmware Slot Information | 03h | M | O | P | 5.2.12.1.4 |
| Changed Attached Namespace List | 04h | O | O | P | 5.2.12.1.5 |
| Commands Supported and Effects | 05h | M<sup>3</sup> | M | M | 5.2.12.1.6 |
| Device Self-test | 06h | O | O | P | 5.2.12.1.7 |
| Telemetry Host-Initiated | 07h | O | O | P | 5.2.12.1.8 |
| Telemetry Controller-Initiated | 08h | O | O<sup>8</sup> | P | 5.2.12.1.9 |
| Endurance Group Information | 09h | O | O | P | 5.2.12.1.10 |
| Predictable Latency Per NVM Set | 0Ah | O | O<sup>8</sup> | P | 5.2.12.1.11 |
| Predictable Latency Event Aggregate | 0Bh | O | O<sup>8</sup> | P | 5.2.12.1.12 |
| Asymmetric Namespace Access | 0Ch | O | P | P | 5.2.12.1.13 |
| Persistent Event | 0Dh | O | O | P | 5.2.12.1.14 |
| LBA Status Information | 0Eh | Refer to the NVM Express NVM Command Set Specification | | | |
| Endurance Group Event Aggregate | 0Fh | O | O | P | 5.2.12.1.15 |
| Media Unit Status | 10h | O<sup>2</sup> | P | P | 5.2.12.1.16 |
| Supported Capacity Configuration List | 11h | O<sup>2</sup> | P | P | 5.2.12.1.17 |
| Feature Identifiers Supported and Effects | 12h | M<sup>3</sup> | M<sup>3,9</sup> | M<sup>9</sup> | 5.2.12.1.18 |
| NVMe-MI Commands Supported and Effects | 13h | M<sup>3,7</sup> | M<sup>3,7</sup> | O | 5.2.12.1.19 |
| Command and Feature Lockdown | 14h | O | O | P | 5.2.12.1.20 |

| Log Page Name | Log Page Identifier | Controller Support Requirements<sup>1</sup> | Reference |
|---------------|---------------------|---------------------------------------------|-----------|
|               |                     | I/O | Administrative | Discovery |           |
| Boot Partition | 15h | O | O | P | 5.2.12.1.21 |
| Rotational Media Information | 16h | O | P | P | 5.2.12.1.22 |
| Dispersed Namespace Participating NVM Subsystems | 17h | O | O | P | 5.2.12.1.23 |
| Management Address List | 18h | O | O | O | 5.2.12.1.24 |
| Physical Interface Receiver Eye Opening Measurement | 19h | O<sup>4</sup> | O<sup>4</sup> | P | Note 11 |
| Reachability Groups | 1Ah | O<sup>6</sup> | P | P | 5.2.12.1.25 |
| Reachability Associations | 1Bh | O<sup>6</sup> | P | P | 5.2.12.1.26 |
| Changed Allocated Namespace List | 1Ch | O | O | P | 5.2.12.1.27 |
| Device Personalities | 1Dh | O | O | P | 5.2.12.1.28 |
| Cross-Controller Reset | 1Eh | O<sup>12</sup> | O<sup>12</sup> | O<sup>13</sup> | 5.2.12.3.1 |
| Lost Host Communication | 1Fh | O<sup>12</sup> | O<sup>12</sup> | O<sup>13</sup> | 5.2.12.3.2 |
| FDP Configurations | 20h | O<sup>5</sup> | P | P | 5.2.12.1.29 |
| Reclaim Unit Handle Usage | 21h | O<sup>5</sup> | P | P | 5.2.12.1.30 |
| FDP Statistics | 22h | O<sup>5</sup> | P | P | 5.2.12.1.31 |
| FDP Events | 23h | O<sup>5</sup> | P | P | 5.2.12.1.32 |
| Power Measurement | 25h | O | O | P | 5.2.12.1.33 |
| Discovery | 70h | P | P | M | 5.2.12.3.3 |
| Host Discovery | 71h | P | P | O | 5.2.12.3.4 |
| AVE Discovery | 72h | P | P | O | 5.2.12.3.5 |
| Pull Model DDC Request | 73h | P | P | M<sup>10</sup> | 5.2.12.3.6 |
| Sanitize Namespace Status List | 7Fh | O | O | P | 5.2.12.1.34 |

| Log Page Name | Log Page Identifier | Controller Support Requirements¹ | Reference |
|---------------|---------------------|----------------------------------|-----------|
| Reservation Notification | 80h | I/O: O | Administrative: P | Discovery: P | 5.2.12.1.34 |
| Sanitize Status | 81h | I/O: O | Administrative: O⁸ | Discovery: P | 5.2.12.1.36 |
| Program List | 82h | | | | |
| Downloadable Program Types List | 83h | | | | Refer to the NVM Express Computational Programs Command Set Specification |
| Memory Range Set List | 84h | | | | |
| | 85h to B5h | | | | Refer to the applicable NVM Express I/O Command Set specification |
| Changed Zone List | B6h | | | | Refer to the NVM Express Zoned Namespace Command Set Specification |
| Vendor Specific | C0h to FFh | | | | |

| Feature Name | Feature Identifier | Controller Support Requirements¹ | Reference |
|--------------|--------------------|----------------------------------|-----------|
| Arbitration | 01h | I/O: M | Administrative: P | Discovery: P | 5.2.26.1.1 |
| Power Management | 02h | I/O: M | Administrative: O | Discovery: P | 5.2.26.1.2 |
| LBA Range Type | 03h | | | | Refer to the NVM Express NVM Command Set Specification |
| Temperature Threshold | 04h | I/O: M | Administrative: O | Discovery: P | 5.2.26.1.3 |
| Error Recovery | 05h | | | | Refer to the NVM Express NVM Command Set Specification |
| Volatile Write Cached | 06h | I/O: O | Administrative: P | Discovery: P | 5.2.26.1.4 |
| Number of Queues | 07h | I/O: M | Administrative: P | Discovery: P | 5.2.26.2.1 |
| Interrupt Coalescing | 08h | I/O: Note 2 | Administrative: Note 2 | Discovery: P | 5.2.26.2.2 |
| Interrupt Vector Configuration | 09h | I/O: Note 2 | Administrative: Note 2 | Discovery: P | 5.2.26.2.3 |

| Feature Name | Feature Identifier | Controller Support Requirements<sup>1</sup> | Reference |
|--------------|--------------------|---------------------------------------------|-----------|
|              |                    | **I/O** | **Administrative** | **Discovery** |           |
| Write Atomicity Normal | 0Ah | Refer to the NVM Express NVM Command Set Specification |           |
| Asynchronous Event Configuration | 0Bh | M | O<sup>8</sup> | M<sup>10</sup> | 5.2.26.1.5 |
| Autonomous Power State Transition | 0Ch | O | O | P | 5.2.26.1.6 |
| Host Memory Buffer | 0Dh | O | O | P | 5.2.26.2.4 |
| Timestamp | 0Eh | O | O | P | 5.2.26.1.7 |
| Keep Alive Timer | 0Fh | M<sup>7</sup> | M<sup>7</sup> | M<sup>10</sup> | 5.2.26.1.8 |
| Host Controlled Thermal Management | 10h | O | O | P | 5.2.26.1.9 |
| Non-Operational Power State Config | 11h | O | O | P | 5.2.26.1.10 |
| Read Recovery Level Config | 12h | O | O | P | 5.2.26.1.11 |
| Predictable Latency Mode Config | 13h | O | O<sup>9</sup> | P | 5.2.26.1.12 |
| Predictable Latency Mode Window | 14h | O | O<sup>9</sup> | P | 5.2.26.1.13 |
| LBA Status Information Report Interval | 15h | Refer to the NVM Express NVM Command Set Specification |           |
| Host Behavior Support | 16h | O | O | P | 5.2.26.1.14 |
| Sanitize Config | 17h | O | O<sup>9</sup> | P | 5.2.26.1.15 |
| Endurance Group Event Configuration | 18h | O | O<sup>9</sup> | P | 5.2.26.1.16 |
| I/O Command Set Profile | 19h | O | P | P | 5.2.26.1.17 |
| Spinup Control | 1Ah | O | P | P | 5.2.26.1.18 |
| Power Loss Signaling Config | 1Bh | O | O | P | 5.2.26.1.19 |
| Performance Characteristics | 1Ch | Refer to the NVM Express NVM Command Set Specification |           |
| Flexible Data Placement | 1Dh | O<sup>6</sup> | P | P | 5.2.26.1.20 |
| Flexible Data Placement Events | 1Eh | O<sup>6</sup> | P | P | 5.2.26.1.21 |
| Namespace Admin Label | 1Fh | O | O | P | 5.2.26.1.22 |
| Key Value Configuration | 20h | Refer to the NVM Express Key Value Command Set Specification |           |
| Controller Data Queue | 21h | O | O | P | 5.2.26.1.23 |
| Configurable Device Personality | 22h | O | O | P | 5.2.26.1.24 |
| Power Limit | 23h | O | O | P | 5.2.26.1.25 |
| Power Threshold | 24h | O | O | P | 5.2.26.1.26 |
| Power Measurement | 25h | O | O | P | 5.2.26.1.27 |
| Embedded Management Controller Address | 78h | O | O | O | 5.2.26.1.28 |
| Host Management Agent Address | 79h | O | O | O | 5.2.26.1.29 |
| Enhanced Controller Metadata | 7Dh | O<sup>5</sup> | O<sup>5</sup> | O | 5.2.26.1.30.1 |
| Controller Metadata | 7Eh | O<sup>5</sup> | O<sup>5</sup> | O | 5.2.26.1.30.2 |
| Namespace Metadata | 7Fh | O<sup>5</sup> | O<sup>5</sup> | O | 5.2.26.1.30.3 |
| Software Progress Marker | 80h | O | O | P | 5.2.26.1.31 |
| Host Identifier | 81h | O<sup>3</sup> | O | P | 5.2.26.1.32 |
| Reservation Notification Mask | 82h | O<sup>4</sup> | P | P | 5.2.26.1.33 |
| Reservation Persistence | 83h | O<sup>4</sup> | P | P | 5.2.26.1.34 |

| Feature Name                     | Feature Identifier | Controller Support Requirements¹ | Reference       |
|----------------------------------|--------------------|----------------------------------|-----------------|
|                                  |                    | I/O              | Administrative | Discovery     |                 |
| Namespace Write Protection Config | 84h                | O                | O              | P             | 5.2.26.1.35     |
| Boot Partition Write Protection Config | 85h              | O                | O              | P             | 5.2.26.1.36     |


---

### 3.1.4 Controller Properties

A property is a dword, or qword attribute of a controller. The attribute may have read, write, or read/write access. The host shall access a property using the width specified for that property with an offset that is at the beginning of the property unless otherwise noted in a transport specific specification. All reserved properties and all reserved bits within properties are read-only and return 0h when read.

For message-based controllers, properties may be read with the Property Get command and may be written with the Property Set command.

For memory-based controllers, refer to the applicable NVMe Transport binding specification for access methods and rules (e.g., NVMe over PCIe Transport Specification).

Figure 33 and Figure 34 describe the property map for a memory-based controller. Figure 33 and Figure 35 describe the property map for a message-based controller.

Accesses that target any portion of two or more properties are not supported.

Software should not rely on 0h being returned.

<!-- Figure 33, coordinate:(114,650,880,892) -->
**Figure 33: Property Definition**

| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Administrative Controller¹ | Discovery Controller¹ | Name                     |
|---------------|-----------------|------------------|----------------------------|------------------------|--------------------------|
| 0h            | 8               | M                | M                          | M                      | CAP: Controller Capabilities |
| 8h            | 4               | M                | M                          | M                      | VS: Version              |
| Ch            | 4               | M²               | M²                         | R                      | INTMS: Interrupt Mask Set |
| 10h           | 4               | M²               | M²                         | R                      | INTMC: Interrupt Mask Clear |
| 14h           | 4               | M                | M                          | M                      | CC: Controller Configuration |
| 18h           | 4               | R                | R                          | R                      | Reserved                 |
| 1Ch           | 4               | M                | M                          | M                      | CSTS: Controller Status  |
| 20h           | 4               | O                | O                          | R                      | NSSR: NVM Subsystem Reset |
| 24h           | 4               | M²               | M²                         | R                      | AQA: Admin Queue Attributes |
| 28h           | 8               | M²               | M²                         | R                      | ASQ: Admin Submission Queue Base Address |

---
===== page_number= 52, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 33, coordinate:(114,104,880,792) -->
Figure 33: Property Definition

| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Administrative Controller¹ | Discovery Controller¹ | Name |
|---------------|------------------|------------------|-----------------------------|------------------------|------|
| 30h           | 8                | M²               | M²                          | R                      | ACQ: Admin Completion Queue Base Address |
| 38h           | 4                | O³               | O³                          | R                      | CMBLOC: Controller Memory Buffer Location |
| 3Ch           | 4                | O³               | O³                          | R                      | CMBSZ: Controller Memory Buffer Size |
| 40h           | 4                | O³               | O³                          | R                      | BPINFO: Boot Partition Information |
| 44h           | 4                | O³               | O³                          | R                      | BPRSEL: Boot Partition Read Select |
| 48h           | 8                | O³               | O³                          | R                      | PBMEL: Boot Partition Memory Buffer Location |
| 50h           | 8                | O³               | O³                          | R                      | CMBMSC: Controller Memory Buffer Memory Space Control |
| 58h           | 4                | O³               | O³                          | R                      | CMBSTS: Controller Memory Buffer Status |
| 5Ch           | 4                | O³               | O³                          | R                      | CMBEBS: Controller Memory Buffer Elasticity Buffer Size |
| 60h           | 4                | O³               | O³                          | R                      | CMBSWTP: Controller Memory Buffer Sustained Write Throughput |
| 64h           | 4                | O                | O                           | R                      | NSSD: NVM Subsystem Shutdown |
| 68h           | 4                | M                | M                           | R                      | CRTO: Controller Ready Timeouts |
| 6Ch           | R                | R                | R                           | R                      | Reserved |
| E00h          | 4                | O³               | O³                          | R                      | PMRCAP: Persistent Memory Capabilities |
| E04h          | 4                | O³               | O³                          | R                      | PMRCTL: Persistent Memory Region Control |
| E08h          | 4                | O³               | O³                          | R                      | PMRSTS: Persistent Memory Region Status |
| E0Ch          | 4                | O³               | O³                          | R                      | PMREBS: Persistent Memory Region Elasticity Buffer Size |
| E10h          | 4                | O³               | O³                          | R                      | PMRSWTP: Persistent Memory Region Sustained Write Throughput |
| E14h          | 4                | O³               | O³                          | R                      | PMRMSCL: Persistent Memory Region Controller Memory Space Control Lower |
| E18h          | 4                | O³               | O³                          | R                      | PMRMSCU: Persistent Memory Region Controller Memory Space Control Upper |
| E1Ch          | R                | R                | R                           | R                      | Reserved |
| 1000h         |                  | Transport Specific: <br> • Refer to Figure 34 for Memory-Based transport implementations. <br> • Refer to Figure 35 for Message-Based transport implementations. | | | |

**Notes:**
1. O/M/R definition: O = Optional, M = Mandatory, R = Reserved
2. Mandatory for memory-based controllers. For message-based controllers this property is reserved.
3. Optional for memory-based controllers. For message-based controllers this property is reserved.
4. Determined by the transport (e.g., the offset calculation formula Offset (1000h + ((2y) * (4 << CAP.DSTRD))) for the memory-based PCIe transport).
===== page_number= 53, page_type= body ====

<!-- Figure 34: Memory-Based Property Definition, coordinate:(112,105,882,300) -->
## Figure 34: Memory-Based Property Definition

| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Admin. Controller¹ | Discovery Controller¹ | Name |
|---------------|------------------|------------------|---------------------|------------------------|------|
| 1000h         | Variable²        | T                | T                   | T                      | Transport Specific (e.g., PCIe doorbell registers as specified in the NVMe over PCIe Transport Specification) |
| 1000h + Variable² |              | O                | O                   | O                      | Vendor Specific |

**Notes:**
1. O/T definition: O = Optional, T = Transport Specific
2. Determined by the transport (e.g., the offset calculation formula Offset (1000h + ((2y) * (4 << CAP.DSTRD))) for the PCIe transport).

<!-- Figure 35: Message-Based Property Definition, coordinate:(112,330,882,452) -->
## Figure 35: Message-Based Property Definition

| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Admin. Controller¹ | Discovery Controller¹ | Name |
|---------------|------------------|------------------|---------------------|------------------------|------|
| 1000h         | 300h             | R                | R                   | R                      | Reserved for Fabrics |
| 1300h         |                  | O                | O                   | O                      | Vendor Specific |

**Notes:**
1. O/R definition: O = Optional, R = Reserved

The following conventions are used to describe controller properties for all transport models. Hardware shall return '0' for all bits that are marked as reserved, and a host shall write all reserved bits and properties with the value of 0h.

The following terms and abbreviations are used:

- **RO** – Read Only
- **RW** – Read Write
- **RWC** – Read/Write '1' to clear
- **RWS** – Read/Write '1' to set
- **Impl Spec** – Implementation Specific – the controller has the freedom to choose its implementation.
- **HwInit** – The default state is dependent on NVM Express controller and system configuration.
- **Reset** – This column indicates the value of the field after a Controller Level Reset as defined in section 3.7.2.

For some fields, it is implementation specific as to whether the field is RW, RWC, or RO; this is typically shown as RW/RO or RWC/RO to indicate that if the functionality is not supported that the field is read only.

When a field is referred to in the document, the convention used is “Property Symbol.Field Symbol”. For example, the PCI command register Parity Error Response Enable bit is referred to by the name CMD.PEE. If the field is an array of bits, the field is referred to as “Property Symbol.Field Symbol (array offset to element)”. When a sub-field is referred to in the document, the convention used is “Property Symbol.Field Symbol.Sub Field Symbol”. For example, when the Controller Ready With Media Support sub-field of the Controller Ready Modes Supported field within the Controller Capability property, the sub-field is referred to by the name CAP.CRMS.CRWMs.



| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Administrative Controller¹ | Discovery Controller¹ | Name                     |
|---------------|-----------------|------------------|----------------------------|------------------------|--------------------------|
| 0h            | 8               | M                | M                          | M                      | CAP: Controller Capabilities |
| 8h            | 4               | M                | M                          | M                      | VS: Version              |
| Ch            | 4               | M²               | M²                         | R                      | INTMS: Interrupt Mask Set |
| 10h           | 4               | M²               | M²                         | R                      | INTMC: Interrupt Mask Clear |
| 14h           | 4               | M                | M                          | M                      | CC: Controller Configuration |
| 18h           | 4               | R                | R                          | R                      | Reserved                 |
| 1Ch           | 4               | M                | M                          | M                      | CSTS: Controller Status  |
| 20h           | 4               | O                | O                          | R                      | NSSR: NVM Subsystem Reset |
| 24h           | 4               | M²               | M²                         | R                      | AQA: Admin Queue Attributes |
| 28h           | 8               | M²               | M²                         | R                      | ASQ: Admin Submission Queue Base Address |

| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Administrative Controller¹ | Discovery Controller¹ | Name |
|---------------|------------------|------------------|-----------------------------|------------------------|------|
| 30h           | 8                | M²               | M²                          | R                      | ACQ: Admin Completion Queue Base Address |
| 38h           | 4                | O³               | O³                          | R                      | CMBLOC: Controller Memory Buffer Location |
| 3Ch           | 4                | O³               | O³                          | R                      | CMBSZ: Controller Memory Buffer Size |
| 40h           | 4                | O³               | O³                          | R                      | BPINFO: Boot Partition Information |
| 44h           | 4                | O³               | O³                          | R                      | BPRSEL: Boot Partition Read Select |
| 48h           | 8                | O³               | O³                          | R                      | PBMEL: Boot Partition Memory Buffer Location |
| 50h           | 8                | O³               | O³                          | R                      | CMBMSC: Controller Memory Buffer Memory Space Control |
| 58h           | 4                | O³               | O³                          | R                      | CMBSTS: Controller Memory Buffer Status |
| 5Ch           | 4                | O³               | O³                          | R                      | CMBEBS: Controller Memory Buffer Elasticity Buffer Size |
| 60h           | 4                | O³               | O³                          | R                      | CMBSWTP: Controller Memory Buffer Sustained Write Throughput |
| 64h           | 4                | O                | O                           | R                      | NSSD: NVM Subsystem Shutdown |
| 68h           | 4                | M                | M                           | R                      | CRTO: Controller Ready Timeouts |
| 6Ch           | R                | R                | R                           | R                      | Reserved |
| E00h          | 4                | O³               | O³                          | R                      | PMRCAP: Persistent Memory Capabilities |
| E04h          | 4                | O³               | O³                          | R                      | PMRCTL: Persistent Memory Region Control |
| E08h          | 4                | O³               | O³                          | R                      | PMRSTS: Persistent Memory Region Status |
| E0Ch          | 4                | O³               | O³                          | R                      | PMREBS: Persistent Memory Region Elasticity Buffer Size |
| E10h          | 4                | O³               | O³                          | R                      | PMRSWTP: Persistent Memory Region Sustained Write Throughput |
| E14h          | 4                | O³               | O³                          | R                      | PMRMSCL: Persistent Memory Region Controller Memory Space Control Lower |
| E18h          | 4                | O³               | O³                          | R                      | PMRMSCU: Persistent Memory Region Controller Memory Space Control Upper |
| E1Ch          | R                | R                | R                           | R                      | Reserved |
| 1000h         |                  | Transport Specific: <br> • Refer to Figure 34 for Memory-Based transport implementations. <br> • Refer to Figure 35 for Message-Based transport implementations. | | | |

| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Admin. Controller¹ | Discovery Controller¹ | Name |
|---------------|------------------|------------------|---------------------|------------------------|------|
| 1000h         | Variable²        | T                | T                   | T                      | Transport Specific (e.g., PCIe doorbell registers as specified in the NVMe over PCIe Transport Specification) |
| 1000h + Variable² |              | O                | O                   | O                      | Vendor Specific |

| Offset (OFST) | Size (in bytes) | I/O Controller¹ | Admin. Controller¹ | Discovery Controller¹ | Name |
|---------------|------------------|------------------|---------------------|------------------------|------|
| 1000h         | 300h             | R                | R                   | R                      | Reserved for Fabrics |
| 1300h         |                  | O                | O                   | O                      | Vendor Specific |


---

### 3.1.4.1 Offset 0h: CAP – Controller Capabilities

This property indicates basic capabilities of the controller to a host.
===== page_number= 54, page_type= body ====

<!-- Figure 36, coordinate:(112,104,880,848) -->

NVM Express® Base Specification, Revision 2.3

**Figure 36: Offset 0h: CAP – Controller Capabilities**

| Bits     | Type | Reset   | Description
===== page_number= 55, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 36, coordinate:(114,104,882,907) -->
**Figure 36: Offset 0h: CAP – Controller Capabilities**

| Bits     | Type | Reset   | Description
===== page_number= 56, page_type= body ==___

<!-- Figure 36, coordinate:(114,104,880,815) -->

**Figure 36: Offset 0h: CAP – Controller Capabilities**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:24 | RO | Impl Spec | **Timeout (TO):** This is the worst-case time that a host should wait for the CSTS.RDY bit to transition from:<br> a) ‘0’ to ‘1’ after the CC.EN bit transitions from ‘0’ to ‘1’; or<br> b) ‘1’ to ‘0’ after the CC.EN bit transitions from ‘1’ to ‘0’.<br><br>This worst-case time may be experienced after events such as an abrupt shutdown, loss of main power without shutting down the controller, or activation of a new firmware image; typical times are expected to be much shorter.<br><br>This field is in 500 millisecond units. The maximum value of this field is FFh, which indicates a 127.5 second timeout.<br><br>If the Controller Ready Independent of Media Enable (CC.CRIME) bit is cleared to ‘0’ and the worst-case time for the CSTS.RDY bit to change state is due to enabling the controller after the CC.EN bit transitions from ‘0’ to ‘1’, then this field shall be set to:<br> a) the value in the Controller Ready With Media Timeout (CRTO.CRWMТ) field; or<br> b) FFh if the value in the CRTO.CRWMТ field is greater than FFh.<br><br>If the Controller Ready Independent of Media Enable (CC.CRIME) bit is set to ‘1’ and the worst-case time for the CSTS.RDY bit to change state is due to enabling the controller after the CC.EN bit transitions from ‘0’ to ‘1’, then this field shall be set to:<br> a) the value in the Controller Ready Independent of Media Timeout (CRTO.CRIMT); or<br> b) FFh if the value in the CRTO.CRIMT field is greater than FFh.<br><br>Controllers that support the CRTO property (refer to Figure 57) are able to indicate larger timeouts for enabling the controller. A host should use the value in the CRTO.CRWMТ field or the CRTO.CRIMT field depending on the controller ready mode indicated by the CC.CRIME bit to determine the worst-case timeout for the CSTS.RDY bit to transition from ‘0’ to ‘1’ after the CC.EN bit transitions from ‘0’ to ‘1’. A host that is based on revisions earlier than NVM Express Base Specification, Revision 2.0 is not required to wait for more than 127.5 seconds for the CSTS.RDY bit to transition.<br><br>Refer to sections 3.5.3 and 3.5.4 for more information. |
| 23:19 | RO | 0h | Reserved |
| 18:17 | RO | Impl Spec | **Arbitration Mechanism Supported (AMS):** This field is bit significant and indicates the optional arbitration mechanisms supported by the controller. If a bit is set to ‘1’, then the corresponding arbitration mechanism is supported by the controller. Refer to section 3.4.4 for arbitration details.<br><br><table><tr><th>Bits</th><th>Description</th></tr><tr><td>1</td><td><strong>Vendor Specific (VS):</strong> Vendor Specific arbitration mechanism.</td></tr><tr><td>0</td><td><strong>Weighted Round Robin with Urgent Priority Class (WRRUPC):</strong> Weighted Round Robin with Urgent Priority Class arbitration mechanism.</td></tr></table><br>The round robin arbitration mechanism is not listed since all controllers shall support this arbitration mechanism.<br><br>For Discovery controllers, this property shall be cleared to 0h. |

NVM Express® Base Specification, Revision 2.3

56
===== page_number= 57, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 36, coordinate:(114,104,880,350) -->
**Figure 36: Offset 0h: CAP – Controller Capabilities**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 16 | RO | Impl Spec | **Contiguous Queues Required (CQR):** This bit is set to '1' if the controller requires that I/O Submission Queues and I/O Completion Queues are required to be physically contiguous. This bit is cleared to '0' if the controller supports I/O Submission Queues and I/O Completion Queues that are not physically contiguous. If this bit is set to '1', then the Physically Contiguous bit (CDW11.PC) in the Create I/O Submission Queue and Create I/O Completion Queue commands shall be set to '1'.<br><br>For controllers using a message-based transport, this property shall be set to a value of 1. |
| 15:00 | RO | Impl Spec | **Maximum Queue Entries Supported (MQES):** This field indicates the maximum individual queue size that the controller supports. For NVMe over PCIe implementations, this value applies to the I/O Submission Queues and I/O Completion Queues that the host creates. For NVMe over Fabrics implementations, this value applies to only the I/O Submission Queues that the host creates. This is a 0’s based value. The minimum value is 1h, indicating two entries. |



| Bits     | Type | Reset   | Description

| Bits     | Type | Reset   | Description

| Bits     | Type | Reset   | Description

| Bits     | Type | Reset   | Description

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:24 | RO | Impl Spec | **Timeout (TO):** This is the worst-case time that a host should wait for the CSTS.RDY bit to transition from:<br> a) ‘0’ to ‘1’ after the CC.EN bit transitions from ‘0’ to ‘1’; or<br> b) ‘1’ to ‘0’ after the CC.EN bit transitions from ‘1’ to ‘0’.<br><br>This worst-case time may be experienced after events such as an abrupt shutdown, loss of main power without shutting down the controller, or activation of a new firmware image; typical times are expected to be much shorter.<br><br>This field is in 500 millisecond units. The maximum value of this field is FFh, which indicates a 127.5 second timeout.<br><br>If the Controller Ready Independent of Media Enable (CC.CRIME) bit is cleared to ‘0’ and the worst-case time for the CSTS.RDY bit to change state is due to enabling the controller after the CC.EN bit transitions from ‘0’ to ‘1’, then this field shall be set to:<br> a) the value in the Controller Ready With Media Timeout (CRTO.CRWMТ) field; or<br> b) FFh if the value in the CRTO.CRWMТ field is greater than FFh.<br><br>If the Controller Ready Independent of Media Enable (CC.CRIME) bit is set to ‘1’ and the worst-case time for the CSTS.RDY bit to change state is due to enabling the controller after the CC.EN bit transitions from ‘0’ to ‘1’, then this field shall be set to:<br> a) the value in the Controller Ready Independent of Media Timeout (CRTO.CRIMT); or<br> b) FFh if the value in the CRTO.CRIMT field is greater than FFh.<br><br>Controllers that support the CRTO property (refer to Figure 57) are able to indicate larger timeouts for enabling the controller. A host should use the value in the CRTO.CRWMТ field or the CRTO.CRIMT field depending on the controller ready mode indicated by the CC.CRIME bit to determine the worst-case timeout for the CSTS.RDY bit to transition from ‘0’ to ‘1’ after the CC.EN bit transitions from ‘0’ to ‘1’. A host that is based on revisions earlier than NVM Express Base Specification, Revision 2.0 is not required to wait for more than 127.5 seconds for the CSTS.RDY bit to transition.<br><br>Refer to sections 3.5.3 and 3.5.4 for more information. |
| 23:19 | RO | 0h | Reserved |
| 18:17 | RO | Impl Spec | **Arbitration Mechanism Supported (AMS):** This field is bit significant and indicates the optional arbitration mechanisms supported by the controller. If a bit is set to ‘1’, then the corresponding arbitration mechanism is supported by the controller. Refer to section 3.4.4 for arbitration details.<br><br><table><tr><th>Bits</th><th>Description</th></tr><tr><td>1</td><td><strong>Vendor Specific (VS):</strong> Vendor Specific arbitration mechanism.</td></tr><tr><td>0</td><td><strong>Weighted Round Robin with Urgent Priority Class (WRRUPC):</strong> Weighted Round Robin with Urgent Priority Class arbitration mechanism.</td></tr></table><br>The round robin arbitration mechanism is not listed since all controllers shall support this arbitration mechanism.<br><br>For Discovery controllers, this property shall be cleared to 0h. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 16 | RO | Impl Spec | **Contiguous Queues Required (CQR):** This bit is set to '1' if the controller requires that I/O Submission Queues and I/O Completion Queues are required to be physically contiguous. This bit is cleared to '0' if the controller supports I/O Submission Queues and I/O Completion Queues that are not physically contiguous. If this bit is set to '1', then the Physically Contiguous bit (CDW11.PC) in the Create I/O Submission Queue and Create I/O Completion Queue commands shall be set to '1'.<br><br>For controllers using a message-based transport, this property shall be set to a value of 1. |
| 15:00 | RO | Impl Spec | **Maximum Queue Entries Supported (MQES):** This field indicates the maximum individual queue size that the controller supports. For NVMe over PCIe implementations, this value applies to the I/O Submission Queues and I/O Completion Queues that the host creates. For NVMe over Fabrics implementations, this value applies to only the I/O Submission Queues that the host creates. This is a 0’s based value. The minimum value is 1h, indicating two entries. |


---

### 3.1.4.2 Offset 8h: VS – Version

This property is Read Only (RO) and indicates the version of this specification that the controller supports, as defined in Figure 37.

<!-- Figure 37, coordinate:(114,434,880,568) -->
**Figure 37: Specification Version Descriptor**

| Bits | Description |
|------|-------------|
| 31:16 | **Major Version (MJR):** An integer value indicating the major version number of this specification which is supported by the controller. |
| 15:08 | **Minor Version (MNR):** An integer value indicating the minor version number of this specification which is supported by the controller. |
| 07:00 | **Tertiary Version (TER):** An integer value indicating the tertiary version number of this specification which is supported by the controller. If this field is cleared to 0h, then this specification does not have a tertiary version number. |

The reset value for each field is described in Figure 38:

<!-- Figure 38, coordinate:(180,618,814,842) -->
**Figure 38: NVM Express Base Specification Version Property Reset Values**

| Specification Version¹ | MJR Field | MNR Field | TER Field |
|------------------------|-----------|-----------|-----------|
| 1.0                    | 1h        | 0h        | 0h        |
| 1.1                    | 1h        | 1h        | 0h        |
| 1.2                    | 1h        | 2h        | 0h        |
| 1.2.1                  | 1h        | 2h        | 1h        |
| 1.3                    | 1h        | 3h        | 0h        |
| 1.4                    | 1h        | 4h        | 0h        |
| 2.0                    | 2h        | 0h        | 0h        |
| 2.1                    | 2h        | 1h        | 0h        |
| 2.2                    | 2h        | 2h        | 0h        |
| 2.3                    | 2h        | 3h        | 0h        |

**Notes:**
1. The specification version listed includes lettered versions (e.g., 1.4 includes 1.4, 1.4a through 1.4c, etc.).



| Bits | Description |
|------|-------------|
| 31:16 | **Major Version (MJR):** An integer value indicating the major version number of this specification which is supported by the controller. |
| 15:08 | **Minor Version (MNR):** An integer value indicating the minor version number of this specification which is supported by the controller. |
| 07:00 | **Tertiary Version (TER):** An integer value indicating the tertiary version number of this specification which is supported by the controller. If this field is cleared to 0h, then this specification does not have a tertiary version number. |

| Specification Version¹ | MJR Field | MNR Field | TER Field |
|------------------------|-----------|-----------|-----------|
| 1.0                    | 1h        | 0h        | 0h        |
| 1.1                    | 1h        | 1h        | 0h        |
| 1.2                    | 1h        | 2h        | 0h        |
| 1.2.1                  | 1h        | 2h        | 1h        |
| 1.3                    | 1h        | 3h        | 0h        |
| 1.4                    | 1h        | 4h        | 0h        |
| 2.0                    | 2h        | 0h        | 0h        |
| 2.1                    | 2h        | 1h        | 0h        |
| 2.2                    | 2h        | 2h        | 0h        |
| 2.3                    | 2h        | 3h        | 0h        |


---

### 3.1.4.3 Offset Ch: INTMS – Interrupt Mask Set

This property is used to mask interrupts when using pin-based interrupts, single message MSI, or multiple message MSI. When using MSI-X, the interrupt mask table defined as part of MSI-X should be used to
===== page_number= 58, page_type= body ==___

mask interrupts. A host shall not access this property when configured for MSI-X; any accesses when configured for MSI-X is undefined. For interrupt behavior requirements, refer to the Interrupts section of the NVMe over PCIe Transport Specification.

<!-- Figure 39: Offset Ch: INTMS – Interrupt Mask Set, coordinate:(114,155,885,288) -->
**Figure 39: Offset Ch: INTMS – Interrupt Mask Set**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RWS | 0h | **Interrupt Vector Mask Set (IVMS):** This field is bit significant. If a '1' is written to a bit, then the corresponding interrupt vector is masked from generating an interrupt or reporting a pending interrupt in the MSI Capability Structure. Writing a '0' to a bit has no effect. When read, this field returns the current interrupt mask value within the controller (not the value of this property). If a bit has a value of a '1', then the corresponding interrupt vector is masked. If a bit has a value of '0', then the corresponding interrupt vector is not masked. |

**3.1.4.4 Offset 10h: INTMC – Interrupt Mask Clear**

This property is used to unmask interrupts when using pin-based interrupts, single message MSI, or multiple message MSI. When using MSI-X, the interrupt mask table defined as part of MSI-X should be used to unmask interrupts. A host shall not access this property when configured for MSI-X; any accesses when configured for MSI-X is undefined. For interrupt behavior requirements, refer to the Interrupts section of the NVMe over PCIe Transport Specification.

<!-- Figure 40: Offset 10h: INTMC – Interrupt Mask Clear, coordinate:(114,438,885,535) -->
**Figure 40: Offset 10h: INTMC – Interrupt Mask Clear**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RWC | 0h | **Interrupt Vector Mask Clear (IVMC):** This field is bit significant. If a '1' is written to a bit, then the corresponding interrupt vector is unmasked. Writing a '0' to a bit has no effect. When read, this field returns the current interrupt mask value within the controller (not the value of this property). If a bit has a value of a '1', then the corresponding interrupt vector is masked. If a bit has a value of '0', then the corresponding interrupt vector is not masked. |

**3.1.4.5 Offset 14h: CC – Controller Configuration**

This property modifies settings for the controller. A host shall set the Arbitration Mechanism Selected (CC.AMS), the Memory Page Size (CC.MPS), and the I/O Command Set Selected (CC.CSS) to valid values prior to enabling the controller by setting CC.EN to '1'. Attempting to create an I/O queue before initializing the I/O Completion Queue Entry Size (CC.IOCQES) and the I/O Submission Queue Entry Size (CC.IOSQES) shall cause a controller to abort a Create I/O Completion Queue command or a Create I/O Submission Queue command with a status code of Invalid Queue Size.

<!-- Figure 41: Offset 14h: CC – Controller Configuration, coordinate:(114,686,885,723) -->
**Figure 41: Offset 14h: CC – Controller Configuration**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:25 | RO | 0h | Reserved |
===== page_number= 59, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 41, coordinate:(114,104,882,687) -->

**Figure 41: Offset 14h: CC – Controller Configuration**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 24 | RW/RO | 0b | **Controller Ready Independent of Media Enable (CRIME):** This bit controls the controller ready mode. The controller ready mode is determined by the state of this bit at the time the controller is enabled by transitioning the CC.EN bit from '0' to '1'.<br><br>If the CAP.CRMS field is set to 11b, then this bit is RW. If the CAP.CRMS field is not set to 11b, then this bit is RO and shall be cleared to '0'. Refer to sections 3.5.3 and 3.5.4 for more detail.<br><br>Changing the value of this field may cause a change in the time reported in the CAP.TO field. Refer to the definition of CAP.TO for more details.<br><br><table><tr><th>Value</th><th>Definition</th></tr><tr><td>0b</td><td><strong>Controller Ready With Media Mode:</strong> Enabling the controller (i.e., CC.EN transitions from '0' to '1') when this bit is cleared to '0' enables Controller Ready With Media mode.</td></tr><tr><td>1b</td><td><strong>Controller Ready Independent Of Media Mode:</strong> Enabling the controller when this bit is set to '1' enables Controller Ready Independent of Media mode.</td></tr></table> |
| 23:20 | RW/RO | 0h | **I/O Completion Queue Entry Size (IOCQES):** This field defines the I/O completion queue entry size that is used for the selected I/O Command Set(s). The required and maximum values for this field are specified in the CQES field in the Identify Controller data structure in Figure 328 for each I/O Command Set. The value is in bytes and is specified as a power of two (2^n).<br><br>If any I/O Completion Queues exist, then write operations that change the value in this field produce undefined results.<br><br>If the controller does not support I/O queues, then this field shall be read-only with a value of 0h.<br><br>For Discovery controllers, this field is reserved. |
| 19:16 | RW/RO | 0h | **I/O Submission Queue Entry Size (IOSQES):** This field defines the I/O submission queue entry size that is used for the selected I/O Command Set(s). The required and maximum values for this field are specified in the SQES field in the Identify Controller data structure in Figure 328 for each I/O Command Set. The value is in bytes and is specified as a power of two (2^n).<br><br>If any I/O Submission Queues exist, then write operations that change the value in this field produce undefined results.<br><br>If the controller does not support I/O queues, then this field shall be read-only with a value of 0h.<br><br>For Discovery controllers, this field is reserved. |

59
===== page_number= 60, page_type= body ====

<!-- Figure 41, coordinate:(114,107,878,840) -->

**Figure 41: Offset 14h: CC – Controller Configuration**

| Bits     | Type | Reset | Description
===== page_number= 61, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 41, coordinate:(114,104,880,630) -->
Figure 41: Offset 14h: CC – Controller Configuration

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 06:04 | RW | 000b | **I/O Command Set Selected (CSS):** This field specifies the I/O Command Set or Sets that are selected. This field shall only be changed when the controller is disabled (i.e., CC.EN is cleared to '0'). The I/O Command Set or Sets that are selected shall be used for all I/O Submission Queues. <br><br> **Value** | **Definition** <br> **CAP.CSS.NCSS Bit** | **Definition** <br> 000b | 1b | NVM Command Set <br> 0b | Reserved <br> 001b to 101b | Reserved <br> 110b | CAP.CSS.IOCSS Bit | Definition <br> 1b | All Supported I/O Command Sets <br> The I/O Command Sets that are supported are reported in the identity I/O Command Set data structure (refer to section 5.2.13.2.19). <br> 0b | Reserved <br> 111b | CAP.CSS.NOIOCSS Bit | Definition <br> 1b | Admin Command Set only <br> I/O Command Set and I/O Command Set specific Admin commands are not supported. Any I/O Command Set specific Admin command submitted on the Admin Submission Queue is aborted with a status code of Invalid Command Opcode. <br> 0b | Reserved <br> For Discovery controllers, this property shall be cleared to 000b. |
| 03:01 | RO | 000b | Reserved |

61
===== page_number= 62, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 41, coordinate:(115,104,878,640) -->
**Figure 41: Offset 14h: CC – Controller Configuration**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 00   | RW   | 0b    | **Enable (EN):** While set to '1', then the controller shall process commands. While cleared to '0', then the controller shall not process commands nor post completion queue entries to Completion Queues. If the host writes this property to clear this bit from '1' to '0', the controller is reset (i.e., a Controller Reset, refer to section 3.7.2.1). That Controller Reset results in a Controller Level Reset (refer to section 3.7.2) that deletes all I/O Submission Queues and I/O Completion Queues, resets the Admin Submission Queue and the Admin Completion Queue, and brings the hardware to an idle state. That Controller Level Reset does not affect transport specific state (e.g., PCI Express registers including MMIO MSI-X registers), nor the Admin Queue properties (AQA, ASQ, or ACQ). Refer to section 3.7.2 for the effects of that Controller Level Reset on all controller properties. Internal controller state (e.g., Feature values defined in section 5.2.26 that are not persistent across power states) are reset to their default values. The controller shall ensure that there is no impact (e.g., data loss) caused by that Controller Level Reset to the results of commands that have had corresponding completion queue entries posted to an I/O Completion Queue prior to that Controller Level Reset.<br><br>When this bit is cleared to '0', the CSTS.RDY bit is cleared to '0' by the controller once the controller is ready to be enabled. When this bit is set to '1', the controller sets the CSTS.RDY bit to '1' when the controller is ready to process commands. The CSTS.RDY bit may be set to '1' before namespace(s) are ready to be accessed.<br><br>Setting this bit from a '0' to a '1' when the CSTS.RDY bit is a '1' or clearing this bit from a '1' to a '0' when the CSTS.RDY bit is cleared to '0' has undefined results. The Admin Queue properties (AQA, ASQ, and ACQ) are only allowed to be modified when this bit is cleared to '0'.<br><br>If an NVM Subsystem Shutdown is reported as in progress or is reported as completed (i.e., the CSTS.ST bit is set to '1', and the CSTS.SHST field is set to 01b or 10b), then:<br>• setting this bit from '0' to '1' modifies the field value but has no effect (e.g., the controller does not respond by setting the CSTS.RDY bit to '1'); and<br>• clearing this bit from '1' to '0' resets the controller as defined by this field.<br><br>Refer to section 3.6.3 for details on NVM Subsystem Shutdown functionality. |

**3.1.4.6 Offset 1Ch: CSTS – Controller Status**

<!-- Figure 42, coordinate:(115,688,878,900) -->
**Figure 42: Offset 1Ch: CSTS – Controller Status**

| Bits   | Type | Reset¹ | Description |
|--------|------|--------|-------------|
| 31:07  | RO   | 0h     | Reserved |
| 06     | RO   | HwInit | **Shutdown Type (ST):** If CSTS.SHST is set to a non-zero value, then this bit indicates the type of shutdown reported by CSTS.SHST.<br><br>If this bit is set to '1', then CSTS.SHST is reporting the state of an NVM Subsystem Shutdown and this bit remains set to '1' until an NVM Subsystem Reset occurs.<br><br>If this bit is cleared to '0', then CSTS.SHST is reporting the state of a controller shutdown.<br><br>An NVM Subsystem Reset shall clear this bit to '0'. All other Controller Level Resets shall not change the value of this bit.<br><br>If CSTS.SHST is cleared to 00b, then this bit should be ignored by the host. |

---

*Note: The image contains two figures (Figure 41 and Figure 42) with structured tables. The coordinate ranges are estimated based on visual layout and may vary slightly depending on exact rendering.*
===== page_number= 63, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 42, coordinate:(114,107,880,832) -->

**Figure 42: Offset 1Ch: CSTS – Controller Status**

| Bits | Type | Reset¹ | Description |
|------|------|--------|-------------|
| 05   | RO   | 0b     | **Processing Paused (PP):** This bit indicates whether the controller is processing commands. If this bit is cleared to '0', then the controller is processing commands normally. If this bit is set to '1', then the controller has temporarily stopped processing commands in order to handle an event (e.g., firmware activation). This bit is only valid when CC.EN is set to '1' and CSTS.RDY is set to '1'. |
| 04   | RWC  | HwInit | **NVM Subsystem Reset Occurred (NSSRO):** The initial value of this bit is set to '1' if the last occurrence of an NVM Subsystem Reset (refer to section 3.7.1) occurred while power was applied to the domain. The initial value of this bit is cleared to '0' following an NVM Subsystem Reset due to application of power to the domain. This bit is only valid if the controller supports the NVM Subsystem Reset feature defined in section 3.7.1 as indicated by CAP.NSSRS set to '1'.<br><br>The reset value of this bit is cleared to '0' if an NVM Subsystem Reset causes activation of a new firmware image in the domain. |
| 03:02 | RO   | 00b    | **Shutdown Status (SHST):** This field indicates the status of shutdown processing that is initiated by the host setting the CC.SHN field, the host setting the NSSD.NSSC field, or a Management Endpoint processing an NVMe-MI Shutdown command (refer to the NVM Express Management Interface Specification). Shutdown processing is able to occur on this controller as a consequence of a host setting the NSSD.NSSC field on another controller to initiate an NVM Subsystem Shutdown that affects this controller.<br><br>The shutdown status values are defined as:<br><br><table><tr><th>Value</th><th>Definition</th></tr><tr><td>00b</td><td>Normal operation (no shutdown has been requested)</td></tr><tr><td>01b</td><td>Shutdown processing in progress</td></tr><tr><td>10b</td><td>Shutdown processing complete</td></tr><tr><td>11b</td><td>Reserved</td></tr></table><br><br>If this field is set to 01b (i.e., shutdown processing in progress), then:<br>• an NVM Subsystem Reset aborts both a controller shutdown and an NVM Subsystem Shutdown; and<br>• any other type of Controller Level Reset (CLR):<br>  ○ may or may not abort a controller shutdown; and<br>  ○ shall not abort an NVM Subsystem Shutdown.<br><br>If this field is cleared to 00b (i.e., normal operation) when a CLR is initiated, then that CLR shall not change the value of this field.<br><br>If this field is set to 01b when a CLR is initiated, and shutdown processing is not aborted by that CLR, then that CLR shall not change the value of this field.<br><br>If this field is set to 01b when a CLR is initiated and shutdown processing is aborted by that CLR, then that CLR shall clear this field to 00b.<br><br>If this field is set to 10b (i.e., shutdown processing complete) when a CLR is initiated by NVM Subsystem Reset, then that CLR shall clear this field to 00b.<br><br>If this field is set to 10b when a CLR is initiated by a method other than NVM Subsystem Reset and:<br>• the CSTS.ST bit is set to '1', then that CLR shall not change the value of this field; and<br>• the CSTS.ST bit is cleared to '0', then that CLR shall clear this field to 00b. |

63
===== page_number= 64, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 42, coordinate:(114,104,880,764) -->
**Figure 42: Offset 1Ch: CSTS – Controller Status**

| Bits | Type | Reset¹ | Description |
|------|------|--------|-------------|
|      |      |        | If the CSTS.ST bit is cleared to '0' and this field is set to 10b (i.e., controller shutdown processing is reported as complete), then to start executing commands on the controller: <ul><li>if the CC.EN bit is set to '1', then a CLR initiated by any method (e.g., a Controller Reset) followed by enabling the controller (i.e., host sets the CC.EN bit from '0' to '1') is required (refer to section 3.6.1). If a host submits commands to the controller without a prior CLR, then the behavior is undefined; and</li><li>if the CC.EN is cleared to '0', then: <ul><li>a CLR followed by enabling the controller is required (refer to sections 3.6.1 and 3.6.2); or</li><li>the CC.EN bit is required to be set to '1' and the CC.SHN field is required to be cleared to 00b with the same write to the CC property (refer to sections 3.6.1 and 3.6.2).</li></ul></li></ul> If the CSTS.ST bit is set to '1' and this field is set to 10b (i.e., NVM Subsystem Shutdown processing is reported as complete), then an NVM Subsystem Reset followed by enabling the controller is required to start executing commands (refer to section 3.6.3). If a host submits commands to the controller without a prior NVM Subsystem Reset, then the behavior is undefined. |
| 01   | RO   | HwInit | **Controller Fatal Status (CFS):** This bit is set to '1' when a fatal controller error occurred that could not be communicated in the appropriate Completion Queue. This bit is cleared to '0' when a fatal controller error has not occurred. Refer to section 9.5. The reset value of this bit is set to '1' when a fatal controller error is detected during controller initialization. |
| 00   | RO   | 0b     | **Ready (RDY):** This bit is set to '1' when the controller is ready to process submission queue entries after the CC.EN bit is set to '1'. This bit shall be cleared to '0' when the CC.EN bit is cleared to '0' once the controller is ready to be re-enabled. Commands should not be submitted to the controller until this bit is set to '1' after the CC.EN bit is set to '1'. Failure to follow this recommendation produces undefined results. Refer to the definition of the CAP.TO field, section 3.5.3, and section 3.5.4 for timing information related to this field. If an NVM Subsystem Shutdown that affects this controller is reported as in progress or is reported as complete (i.e., the CSTS.ST bit is set to '1' and the CSTS.SHST field is set to 01b or is set to 10b), then an NVM Subsystem Reset is required before this bit is allowed to be set to '1' from '0'. Refer to section 3.6.3. If a controller shutdown is reported as in progress or is reported as complete (i.e., the CSTS.ST bit is cleared to '0' and the CSTS.SHST field is set to 01b or is set to 10b), then before this bit is allowed to be set to '1' from '0', controller shutdown processing shall stop (e.g., complete or be terminated) and the CSTS.SHST field shall be cleared to 00b. |

**Notes:**
1. During a Controller Level Reset, the field and bit values may transition to values other than the reset value prior to indicating the reset value.

---

**3.1.4.7 Offset 20h: NSSR – NVM Subsystem Reset**

This optional property provides a host with the capability to initiate an NVM Subsystem Reset. Support for this property is indicated by the state of the NVM Subsystem Reset Supported (CAP.NSSRS) field. If this property is not supported, then the address range occupied by this property is reserved. Refer to section 3.7.1.
===== page_number= 65, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 43, coordinate:(114,105,880,198) -->
**Figure 43: Offset 20h: NSSR – NVM Subsystem Reset**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RW | 0h | **NVM Subsystem Reset Control (NSSRC):** A write of the value 4E564D65h ("NVMe") to this field initiates an NVM Subsystem Reset. A write of any other value has no functional effect on the operation of the NVM subsystem. This field shall return the value 0h when read. |



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RWS | 0h | **Interrupt Vector Mask Set (IVMS):** This field is bit significant. If a '1' is written to a bit, then the corresponding interrupt vector is masked from generating an interrupt or reporting a pending interrupt in the MSI Capability Structure. Writing a '0' to a bit has no effect. When read, this field returns the current interrupt mask value within the controller (not the value of this property). If a bit has a value of a '1', then the corresponding interrupt vector is masked. If a bit has a value of '0', then the corresponding interrupt vector is not masked. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RWC | 0h | **Interrupt Vector Mask Clear (IVMC):** This field is bit significant. If a '1' is written to a bit, then the corresponding interrupt vector is unmasked. Writing a '0' to a bit has no effect. When read, this field returns the current interrupt mask value within the controller (not the value of this property). If a bit has a value of a '1', then the corresponding interrupt vector is masked. If a bit has a value of '0', then the corresponding interrupt vector is not masked. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:25 | RO | 0h | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:25 | RO | 0h | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 24 | RW/RO | 0b | **Controller Ready Independent of Media Enable (CRIME):** This bit controls the controller ready mode. The controller ready mode is determined by the state of this bit at the time the controller is enabled by transitioning the CC.EN bit from '0' to '1'.<br><br>If the CAP.CRMS field is set to 11b, then this bit is RW. If the CAP.CRMS field is not set to 11b, then this bit is RO and shall be cleared to '0'. Refer to sections 3.5.3 and 3.5.4 for more detail.<br><br>Changing the value of this field may cause a change in the time reported in the CAP.TO field. Refer to the definition of CAP.TO for more details.<br><br><table><tr><th>Value</th><th>Definition</th></tr><tr><td>0b</td><td><strong>Controller Ready With Media Mode:</strong> Enabling the controller (i.e., CC.EN transitions from '0' to '1') when this bit is cleared to '0' enables Controller Ready With Media mode.</td></tr><tr><td>1b</td><td><strong>Controller Ready Independent Of Media Mode:</strong> Enabling the controller when this bit is set to '1' enables Controller Ready Independent of Media mode.</td></tr></table> |
| 23:20 | RW/RO | 0h | **I/O Completion Queue Entry Size (IOCQES):** This field defines the I/O completion queue entry size that is used for the selected I/O Command Set(s). The required and maximum values for this field are specified in the CQES field in the Identify Controller data structure in Figure 328 for each I/O Command Set. The value is in bytes and is specified as a power of two (2^n).<br><br>If any I/O Completion Queues exist, then write operations that change the value in this field produce undefined results.<br><br>If the controller does not support I/O queues, then this field shall be read-only with a value of 0h.<br><br>For Discovery controllers, this field is reserved. |
| 19:16 | RW/RO | 0h | **I/O Submission Queue Entry Size (IOSQES):** This field defines the I/O submission queue entry size that is used for the selected I/O Command Set(s). The required and maximum values for this field are specified in the SQES field in the Identify Controller data structure in Figure 328 for each I/O Command Set. The value is in bytes and is specified as a power of two (2^n).<br><br>If any I/O Submission Queues exist, then write operations that change the value in this field produce undefined results.<br><br>If the controller does not support I/O queues, then this field shall be read-only with a value of 0h.<br><br>For Discovery controllers, this field is reserved. |

| Bits     | Type | Reset | Description

| Bits     | Type | Reset | Description

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 06:04 | RW | 000b | **I/O Command Set Selected (CSS):** This field specifies the I/O Command Set or Sets that are selected. This field shall only be changed when the controller is disabled (i.e., CC.EN is cleared to '0'). The I/O Command Set or Sets that are selected shall be used for all I/O Submission Queues. <br><br> **Value** | **Definition** <br> **CAP.CSS.NCSS Bit** | **Definition** <br> 000b | 1b | NVM Command Set <br> 0b | Reserved <br> 001b to 101b | Reserved <br> 110b | CAP.CSS.IOCSS Bit | Definition <br> 1b | All Supported I/O Command Sets <br> The I/O Command Sets that are supported are reported in the identity I/O Command Set data structure (refer to section 5.2.13.2.19). <br> 0b | Reserved <br> 111b | CAP.CSS.NOIOCSS Bit | Definition <br> 1b | Admin Command Set only <br> I/O Command Set and I/O Command Set specific Admin commands are not supported. Any I/O Command Set specific Admin command submitted on the Admin Submission Queue is aborted with a status code of Invalid Command Opcode. <br> 0b | Reserved <br> For Discovery controllers, this property shall be cleared to 000b. |
| 03:01 | RO | 000b | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 00   | RW   | 0b    | **Enable (EN):** While set to '1', then the controller shall process commands. While cleared to '0', then the controller shall not process commands nor post completion queue entries to Completion Queues. If the host writes this property to clear this bit from '1' to '0', the controller is reset (i.e., a Controller Reset, refer to section 3.7.2.1). That Controller Reset results in a Controller Level Reset (refer to section 3.7.2) that deletes all I/O Submission Queues and I/O Completion Queues, resets the Admin Submission Queue and the Admin Completion Queue, and brings the hardware to an idle state. That Controller Level Reset does not affect transport specific state (e.g., PCI Express registers including MMIO MSI-X registers), nor the Admin Queue properties (AQA, ASQ, or ACQ). Refer to section 3.7.2 for the effects of that Controller Level Reset on all controller properties. Internal controller state (e.g., Feature values defined in section 5.2.26 that are not persistent across power states) are reset to their default values. The controller shall ensure that there is no impact (e.g., data loss) caused by that Controller Level Reset to the results of commands that have had corresponding completion queue entries posted to an I/O Completion Queue prior to that Controller Level Reset.<br><br>When this bit is cleared to '0', the CSTS.RDY bit is cleared to '0' by the controller once the controller is ready to be enabled. When this bit is set to '1', the controller sets the CSTS.RDY bit to '1' when the controller is ready to process commands. The CSTS.RDY bit may be set to '1' before namespace(s) are ready to be accessed.<br><br>Setting this bit from a '0' to a '1' when the CSTS.RDY bit is a '1' or clearing this bit from a '1' to a '0' when the CSTS.RDY bit is cleared to '0' has undefined results. The Admin Queue properties (AQA, ASQ, and ACQ) are only allowed to be modified when this bit is cleared to '0'.<br><br>If an NVM Subsystem Shutdown is reported as in progress or is reported as completed (i.e., the CSTS.ST bit is set to '1', and the CSTS.SHST field is set to 01b or 10b), then:<br>• setting this bit from '0' to '1' modifies the field value but has no effect (e.g., the controller does not respond by setting the CSTS.RDY bit to '1'); and<br>• clearing this bit from '1' to '0' resets the controller as defined by this field.<br><br>Refer to section 3.6.3 for details on NVM Subsystem Shutdown functionality. |

| Bits   | Type | Reset¹ | Description |
|--------|------|--------|-------------|
| 31:07  | RO   | 0h     | Reserved |
| 06     | RO   | HwInit | **Shutdown Type (ST):** If CSTS.SHST is set to a non-zero value, then this bit indicates the type of shutdown reported by CSTS.SHST.<br><br>If this bit is set to '1', then CSTS.SHST is reporting the state of an NVM Subsystem Shutdown and this bit remains set to '1' until an NVM Subsystem Reset occurs.<br><br>If this bit is cleared to '0', then CSTS.SHST is reporting the state of a controller shutdown.<br><br>An NVM Subsystem Reset shall clear this bit to '0'. All other Controller Level Resets shall not change the value of this bit.<br><br>If CSTS.SHST is cleared to 00b, then this bit should be ignored by the host. |

| Bits | Type | Reset¹ | Description |
|------|------|--------|-------------|
| 05   | RO   | 0b     | **Processing Paused (PP):** This bit indicates whether the controller is processing commands. If this bit is cleared to '0', then the controller is processing commands normally. If this bit is set to '1', then the controller has temporarily stopped processing commands in order to handle an event (e.g., firmware activation). This bit is only valid when CC.EN is set to '1' and CSTS.RDY is set to '1'. |
| 04   | RWC  | HwInit | **NVM Subsystem Reset Occurred (NSSRO):** The initial value of this bit is set to '1' if the last occurrence of an NVM Subsystem Reset (refer to section 3.7.1) occurred while power was applied to the domain. The initial value of this bit is cleared to '0' following an NVM Subsystem Reset due to application of power to the domain. This bit is only valid if the controller supports the NVM Subsystem Reset feature defined in section 3.7.1 as indicated by CAP.NSSRS set to '1'.<br><br>The reset value of this bit is cleared to '0' if an NVM Subsystem Reset causes activation of a new firmware image in the domain. |
| 03:02 | RO   | 00b    | **Shutdown Status (SHST):** This field indicates the status of shutdown processing that is initiated by the host setting the CC.SHN field, the host setting the NSSD.NSSC field, or a Management Endpoint processing an NVMe-MI Shutdown command (refer to the NVM Express Management Interface Specification). Shutdown processing is able to occur on this controller as a consequence of a host setting the NSSD.NSSC field on another controller to initiate an NVM Subsystem Shutdown that affects this controller.<br><br>The shutdown status values are defined as:<br><br><table><tr><th>Value</th><th>Definition</th></tr><tr><td>00b</td><td>Normal operation (no shutdown has been requested)</td></tr><tr><td>01b</td><td>Shutdown processing in progress</td></tr><tr><td>10b</td><td>Shutdown processing complete</td></tr><tr><td>11b</td><td>Reserved</td></tr></table><br><br>If this field is set to 01b (i.e., shutdown processing in progress), then:<br>• an NVM Subsystem Reset aborts both a controller shutdown and an NVM Subsystem Shutdown; and<br>• any other type of Controller Level Reset (CLR):<br>  ○ may or may not abort a controller shutdown; and<br>  ○ shall not abort an NVM Subsystem Shutdown.<br><br>If this field is cleared to 00b (i.e., normal operation) when a CLR is initiated, then that CLR shall not change the value of this field.<br><br>If this field is set to 01b when a CLR is initiated, and shutdown processing is not aborted by that CLR, then that CLR shall not change the value of this field.<br><br>If this field is set to 01b when a CLR is initiated and shutdown processing is aborted by that CLR, then that CLR shall clear this field to 00b.<br><br>If this field is set to 10b (i.e., shutdown processing complete) when a CLR is initiated by NVM Subsystem Reset, then that CLR shall clear this field to 00b.<br><br>If this field is set to 10b when a CLR is initiated by a method other than NVM Subsystem Reset and:<br>• the CSTS.ST bit is set to '1', then that CLR shall not change the value of this field; and<br>• the CSTS.ST bit is cleared to '0', then that CLR shall clear this field to 00b. |

| Bits | Type | Reset¹ | Description |
|------|------|--------|-------------|
|      |      |        | If the CSTS.ST bit is cleared to '0' and this field is set to 10b (i.e., controller shutdown processing is reported as complete), then to start executing commands on the controller: <ul><li>if the CC.EN bit is set to '1', then a CLR initiated by any method (e.g., a Controller Reset) followed by enabling the controller (i.e., host sets the CC.EN bit from '0' to '1') is required (refer to section 3.6.1). If a host submits commands to the controller without a prior CLR, then the behavior is undefined; and</li><li>if the CC.EN is cleared to '0', then: <ul><li>a CLR followed by enabling the controller is required (refer to sections 3.6.1 and 3.6.2); or</li><li>the CC.EN bit is required to be set to '1' and the CC.SHN field is required to be cleared to 00b with the same write to the CC property (refer to sections 3.6.1 and 3.6.2).</li></ul></li></ul> If the CSTS.ST bit is set to '1' and this field is set to 10b (i.e., NVM Subsystem Shutdown processing is reported as complete), then an NVM Subsystem Reset followed by enabling the controller is required to start executing commands (refer to section 3.6.3). If a host submits commands to the controller without a prior NVM Subsystem Reset, then the behavior is undefined. |
| 01   | RO   | HwInit | **Controller Fatal Status (CFS):** This bit is set to '1' when a fatal controller error occurred that could not be communicated in the appropriate Completion Queue. This bit is cleared to '0' when a fatal controller error has not occurred. Refer to section 9.5. The reset value of this bit is set to '1' when a fatal controller error is detected during controller initialization. |
| 00   | RO   | 0b     | **Ready (RDY):** This bit is set to '1' when the controller is ready to process submission queue entries after the CC.EN bit is set to '1'. This bit shall be cleared to '0' when the CC.EN bit is cleared to '0' once the controller is ready to be re-enabled. Commands should not be submitted to the controller until this bit is set to '1' after the CC.EN bit is set to '1'. Failure to follow this recommendation produces undefined results. Refer to the definition of the CAP.TO field, section 3.5.3, and section 3.5.4 for timing information related to this field. If an NVM Subsystem Shutdown that affects this controller is reported as in progress or is reported as complete (i.e., the CSTS.ST bit is set to '1' and the CSTS.SHST field is set to 01b or is set to 10b), then an NVM Subsystem Reset is required before this bit is allowed to be set to '1' from '0'. Refer to section 3.6.3. If a controller shutdown is reported as in progress or is reported as complete (i.e., the CSTS.ST bit is cleared to '0' and the CSTS.SHST field is set to 01b or is set to 10b), then before this bit is allowed to be set to '1' from '0', controller shutdown processing shall stop (e.g., complete or be terminated) and the CSTS.SHST field shall be cleared to 00b. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RW | 0h | **NVM Subsystem Reset Control (NSSRC):** A write of the value 4E564D65h ("NVMe") to this field initiates an NVM Subsystem Reset. A write of any other value has no functional effect on the operation of the NVM subsystem. This field shall return the value 0h when read. |


---

### 3.1.4.8 Offset 24h: AQA – Admin Queue Attributes

This property defines the attributes for the Admin Submission Queue and Admin Completion Queue. The Queue Identifier for the Admin Submission Queue and Admin Completion Queue is 0h. The Admin Submission Queue’s priority is determined by the arbitration mechanism selected, refer to section 3.4.4. The Admin Submission Queue and Admin Completion Queue are required to be in physically contiguous memory.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

**Note:** It is recommended that the host use UEFI during boot operations. In low memory environments (e.g., Option ROMs in legacy BIOS environments) there may not be sufficient available memory to allocate the necessary Submission and Completion Queues. In these types of conditions, low memory operation of the controller is vendor specific.

<!-- Figure 44, coordinate:(114,414,880,613) -->
**Figure 44: Offset 24h: AQA – Admin Queue Attributes**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:28 | RO | 0h | Reserved |
| 27:16 | RW | 0h | **Admin Completion Queue Size (ACQS):** Defines the size of the Admin Completion Queue in entries. Refer to section 3.3.3.1. Enabling a controller while this field is cleared to 0h produces undefined results. The minimum size of the Admin Completion Queue is two entries. The maximum size of the Admin Completion Queue is 4,096 entries. This is a 0’s based value. |
| 15:12 | RO | 0h | Reserved |
| 11:00 | RW | 0h | **Admin Submission Queue Size (ASQS):** Defines the size of the Admin Submission Queue in entries. Refer to section 3.3.3.1. Enabling a controller while this field is cleared to 0h produces undefined results. The minimum size of the Admin Submission Queue is two entries. The maximum size of the Admin Submission Queue is 4,096 entries. This is a 0’s based value. |



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:28 | RO | 0h | Reserved |
| 27:16 | RW | 0h | **Admin Completion Queue Size (ACQS):** Defines the size of the Admin Completion Queue in entries. Refer to section 3.3.3.1. Enabling a controller while this field is cleared to 0h produces undefined results. The minimum size of the Admin Completion Queue is two entries. The maximum size of the Admin Completion Queue is 4,096 entries. This is a 0’s based value. |
| 15:12 | RO | 0h | Reserved |
| 11:00 | RW | 0h | **Admin Submission Queue Size (ASQS):** Defines the size of the Admin Submission Queue in entries. Refer to section 3.3.3.1. Enabling a controller while this field is cleared to 0h produces undefined results. The minimum size of the Admin Submission Queue is two entries. The maximum size of the Admin Submission Queue is 4,096 entries. This is a 0’s based value. |


---

### 3.1.4.9 Offset 28h: ASQ – Admin Submission Queue Base Address

This property defines the base memory address of the Admin Submission Queue.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

<!-- Figure 45, coordinate:(114,715,880,825) -->
**Figure 45: Offset 28h: ASQ – Admin Submission Queue Base Address**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | Impl Spec | **Admin Submission Queue Base (ASQB):** This field specifies the 52 most significant bits of the 64-bit physical address for the Admin Submission Queue. This address shall be memory page aligned (based on the value in CC.MPS). All Admin commands, including creation of I/O Submission Queues and I/O Completions Queues shall be submitted to this queue. For the definition of Submission Queues, refer to section 4.1. |
| 11:00 | RO | 0h | Reserved |



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | Impl Spec | **Admin Submission Queue Base (ASQB):** This field specifies the 52 most significant bits of the 64-bit physical address for the Admin Submission Queue. This address shall be memory page aligned (based on the value in CC.MPS). All Admin commands, including creation of I/O Submission Queues and I/O Completions Queues shall be submitted to this queue. For the definition of Submission Queues, refer to section 4.1. |
| 11:00 | RO | 0h | Reserved |


---

### 3.1.4.10 Offset 30h: ACQ – Admin Completion Queue Base Address

This property defines the base memory address of the Admin Completion Queue.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

---

65
===== page_number= 66, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 46, coordinate:(114,104,880,238) -->
**Figure 46: Offset 30h: ACQ – Admin Completion Queue Base Address**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | Impl Spec | **Admin Completion Queue Base (ACQB):** This field specifies the 52 most significant bits of the 64-bit physical address for the Admin Completion Queue. This address shall be memory page aligned (based on the value in CC.MPS). All completion queue entries for the commands submitted to the Admin Submission Queue shall be posted to this Completion Queue. This queue is always associated with interrupt vector 0. For the definition of Completion Queues, refer to section 4.1. |
| 11:00 | RO | 0h | Reserved |

**3.1.4.11 Offset 38h: CMBLOC – Controller Memory Buffer Location**

This optional property defines the location of the Controller Memory Buffer (refer to section 8.2.1). If the controller does not support the Controller Memory Buffer (CAP.CMBS), this property is reserved. If the controller supports the Controller Memory Buffer and CMBMSC.CRE is set to '0', this property shall be cleared to 0h.

<!-- Figure 47, coordinate:(114,352,880,900) -->
**Figure 47: Offset 38h: CMBLOC – Controller Memory Buffer Location**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:12 | RO | Impl Spec | **Offset (OFST):** Indicates the offset of the Controller Memory Buffer in multiples of the Size Unit specified in CMBSZ. |
| 11:09 | RO | 000b | Reserved |
| 08 | RO | Impl Spec | **CMB Queue Dword Alignment (CQDA):** If this bit is set to '1', CDW11.PC is set to '1'; and the address pointer specifies Controller Memory Buffer, then the address pointer in a Create I/O Submission Queue command (refer to Figure 506) or a Create I/O Completion Queue command (refer to Figure 502) shall be Dword aligned. <br><br> If this bit is cleared to '0', then the I/O Submission Queues and I/O Completion Queues contained in the Controller Memory Buffer are aligned as defined by the PRP1 field of a Create I/O Submission Queue command (refer to Figure 506) or a Create I/O Completion Queue command (refer to Figure 502). |
| 07 | RO | Impl Spec | **CMB Data Metadata Mixed Memory Support (CDMMMS):** If this bit is set to '1', then the restriction on data and metadata use of Controller Memory Buffer by a command as defined in section 8.2.1 is not enforced. If this bit is cleared to '0', then the restriction on data and metadata use of Controller Memory Buffer by a command as defined in section 8.2.1 is enforced. |
| 06 | RO | Impl Spec | **CMB Data Pointer and Command Independent Locations Support (CDPCILS):** If this bit is set to '1', then the restriction that the PRP Lists and SGLs shall not be located in the Controller Memory Buffer if the command that they are associated with is not located in the Controller Memory Buffer is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that restriction is enforced. |
| 05 | RO | Impl Spec | **CMB Data Pointer Mixed Locations Support (CDPMLS):** If this bit is set to '1', then the restriction that for a particular PRP List or SGL associated with a single command, all memory that contains that particular PRP List or SGL shall reside in either the Controller Memory Buffer or outside the Controller Memory Buffer, is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that restriction is enforced. |
| 04 | RO | Impl Spec | **CMB Queue Physically Discontiguous Support (CQPDs):** If this bit is set to '1', then the restriction that for all queues in the Controller Memory Buffer, the queue shall be physically contiguous, is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that restriction is enforced. |
| 03 | RO | Impl Spec | **CMB Queue Mixed Memory Support (CQMMS):** If this bit is set to '1', then for a particular queue placed in the Controller Memory Buffer, the restriction that all memory associated with that queue shall reside in the Controller Memory Buffer is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that requirement is enforced. |
| 02:00 | RO | Impl Spec | **Base Indicator Register (BIR):** Indicates the Base Address Register (BAR) that contains the Controller Memory Buffer. For a 64-bit BAR, the BAR for the least significant 32-bits of the address is specified. Values 000b, 010b, 011b, 100b, and 101b are valid. The address specified by the BAR shall be 4 KiB aligned. |

66
===== page_number= 67, page_type= body ====

# NVM Express® Base Specification, Revision 2.3



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | Impl Spec | **Admin Completion Queue Base (ACQB):** This field specifies the 52 most significant bits of the 64-bit physical address for the Admin Completion Queue. This address shall be memory page aligned (based on the value in CC.MPS). All completion queue entries for the commands submitted to the Admin Submission Queue shall be posted to this Completion Queue. This queue is always associated with interrupt vector 0. For the definition of Completion Queues, refer to section 4.1. |
| 11:00 | RO | 0h | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:12 | RO | Impl Spec | **Offset (OFST):** Indicates the offset of the Controller Memory Buffer in multiples of the Size Unit specified in CMBSZ. |
| 11:09 | RO | 000b | Reserved |
| 08 | RO | Impl Spec | **CMB Queue Dword Alignment (CQDA):** If this bit is set to '1', CDW11.PC is set to '1'; and the address pointer specifies Controller Memory Buffer, then the address pointer in a Create I/O Submission Queue command (refer to Figure 506) or a Create I/O Completion Queue command (refer to Figure 502) shall be Dword aligned. <br><br> If this bit is cleared to '0', then the I/O Submission Queues and I/O Completion Queues contained in the Controller Memory Buffer are aligned as defined by the PRP1 field of a Create I/O Submission Queue command (refer to Figure 506) or a Create I/O Completion Queue command (refer to Figure 502). |
| 07 | RO | Impl Spec | **CMB Data Metadata Mixed Memory Support (CDMMMS):** If this bit is set to '1', then the restriction on data and metadata use of Controller Memory Buffer by a command as defined in section 8.2.1 is not enforced. If this bit is cleared to '0', then the restriction on data and metadata use of Controller Memory Buffer by a command as defined in section 8.2.1 is enforced. |
| 06 | RO | Impl Spec | **CMB Data Pointer and Command Independent Locations Support (CDPCILS):** If this bit is set to '1', then the restriction that the PRP Lists and SGLs shall not be located in the Controller Memory Buffer if the command that they are associated with is not located in the Controller Memory Buffer is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that restriction is enforced. |
| 05 | RO | Impl Spec | **CMB Data Pointer Mixed Locations Support (CDPMLS):** If this bit is set to '1', then the restriction that for a particular PRP List or SGL associated with a single command, all memory that contains that particular PRP List or SGL shall reside in either the Controller Memory Buffer or outside the Controller Memory Buffer, is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that restriction is enforced. |
| 04 | RO | Impl Spec | **CMB Queue Physically Discontiguous Support (CQPDs):** If this bit is set to '1', then the restriction that for all queues in the Controller Memory Buffer, the queue shall be physically contiguous, is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that restriction is enforced. |
| 03 | RO | Impl Spec | **CMB Queue Mixed Memory Support (CQMMS):** If this bit is set to '1', then for a particular queue placed in the Controller Memory Buffer, the restriction that all memory associated with that queue shall reside in the Controller Memory Buffer is not enforced (refer to section 8.2.1). If this bit is cleared to '0', then that requirement is enforced. |
| 02:00 | RO | Impl Spec | **Base Indicator Register (BIR):** Indicates the Base Address Register (BAR) that contains the Controller Memory Buffer. For a 64-bit BAR, the BAR for the least significant 32-bits of the address is specified. Values 000b, 010b, 011b, 100b, and 101b are valid. The address specified by the BAR shall be 4 KiB aligned. |


---

## 3.1.4.12 Offset 3Ch: CMBSZ – Controller Memory Buffer Size

This optional property defines the size of the Controller Memory Buffer (refer to section 8.2.1). If the controller does not support the Controller Memory Buffer feature or if the controller supports the Controller Memory Buffer (CAP.CMBS) and CMBMSC.CRE is cleared to '0', then this property shall be cleared to 0h.

### Figure 48: Offset 3Ch: CMBSZ – Controller Memory Buffer Size

<!-- Figure 48, coordinate:(114,202,880,785) -->

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:12 | RO | Impl Spec | **Size (SZ):** Indicates the size of the Controller Memory Buffer available for use by the host. The size is in multiples of the Size Unit. If the Offset + Size exceeds the length of the indicated BAR, the size available to the host is limited by the length of the BAR. |
| 11:08 | RO | Impl Spec | **Size Units (SZU):** Indicates the granularity of the Size field. <br> <table><tr><th>Value</th><th>Granularity</th></tr><tr><td>0h</td><td>4 KiB</td></tr><tr><td>1h</td><td>64 KiB</td></tr><tr><td>2h</td><td>1 MiB</td></tr><tr><td>3h</td><td>16 MiB</td></tr><tr><td>4h</td><td>256 MiB</td></tr><tr><td>5h</td><td>4 GiB</td></tr><tr><td>6h</td><td>64 GiB</td></tr><tr><td>7h to Fh</td><td>Reserved</td></tr></table> |
| 07:05 | RO | 000b | Reserved |
| 04 | RO | Impl Spec | **Write Data Support (WDS):** If this bit is set to '1', then the controller supports data and metadata in the Controller Memory Buffer for commands that transfer data from the host to the controller (e.g., Write). If this bit is cleared to '0', then data and metadata for commands that transfer data from the host to the controller shall not be transferred to the Controller Memory Buffer. |
| 03 | RO | Impl Spec | **Read Data Support (RDS):** If this bit is set to '1', then the controller supports data and metadata in the Controller Memory Buffer for commands that transfer data from the controller to the host (e.g., Read). If this bit is cleared to '0', then data and metadata for commands that transfer data from the controller to the host shall not be transferred from the Controller Memory Buffer. |
| 02 | RO | Impl Spec | **PRP SGL List Support (LISTS):** If this bit is set to '1', then: <ul><li>the controller supports PRP Lists in the Controller Memory Buffer;</li><li>if SGLs are supported by the controller, then the controller supports Scatter Gather Lists in the Controller Memory Buffer; and</li><li>the Submission Queue Support bit shall be set to '1'.</li></ul> If this bit is cleared to '0', then the host shall not place PRP Lists and SGLs in the Controller Memory Buffer. If the host places PRP Lists or SGLs in the Controller Memory Buffer, then controller behavior is undefined. |
| 01 | RO | Impl Spec | **Completion Queue Support (CQS):** If this bit is set to '1', then the controller supports Admin and I/O Completion Queues in the Controller Memory Buffer. If this bit is cleared to '0', then Completion Queues shall not be placed in the Controller Memory Buffer. |
| 00 | RO | Impl Spec | **Submission Queue Support (SQS):** If this bit is set to '1', then the controller supports Admin and I/O Submission Queues in the Controller Memory Buffer. If this bit is cleared to '0', then the host shall not place Submission Queues in the Controller Memory Buffer. If the host places Submission Queues in the Controller Memory Buffer, then controller behavior is undefined. |



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:12 | RO | Impl Spec | **Size (SZ):** Indicates the size of the Controller Memory Buffer available for use by the host. The size is in multiples of the Size Unit. If the Offset + Size exceeds the length of the indicated BAR, the size available to the host is limited by the length of the BAR. |
| 11:08 | RO | Impl Spec | **Size Units (SZU):** Indicates the granularity of the Size field. <br> <table><tr><th>Value</th><th>Granularity</th></tr><tr><td>0h</td><td>4 KiB</td></tr><tr><td>1h</td><td>64 KiB</td></tr><tr><td>2h</td><td>1 MiB</td></tr><tr><td>3h</td><td>16 MiB</td></tr><tr><td>4h</td><td>256 MiB</td></tr><tr><td>5h</td><td>4 GiB</td></tr><tr><td>6h</td><td>64 GiB</td></tr><tr><td>7h to Fh</td><td>Reserved</td></tr></table> |
| 07:05 | RO | 000b | Reserved |
| 04 | RO | Impl Spec | **Write Data Support (WDS):** If this bit is set to '1', then the controller supports data and metadata in the Controller Memory Buffer for commands that transfer data from the host to the controller (e.g., Write). If this bit is cleared to '0', then data and metadata for commands that transfer data from the host to the controller shall not be transferred to the Controller Memory Buffer. |
| 03 | RO | Impl Spec | **Read Data Support (RDS):** If this bit is set to '1', then the controller supports data and metadata in the Controller Memory Buffer for commands that transfer data from the controller to the host (e.g., Read). If this bit is cleared to '0', then data and metadata for commands that transfer data from the controller to the host shall not be transferred from the Controller Memory Buffer. |
| 02 | RO | Impl Spec | **PRP SGL List Support (LISTS):** If this bit is set to '1', then: <ul><li>the controller supports PRP Lists in the Controller Memory Buffer;</li><li>if SGLs are supported by the controller, then the controller supports Scatter Gather Lists in the Controller Memory Buffer; and</li><li>the Submission Queue Support bit shall be set to '1'.</li></ul> If this bit is cleared to '0', then the host shall not place PRP Lists and SGLs in the Controller Memory Buffer. If the host places PRP Lists or SGLs in the Controller Memory Buffer, then controller behavior is undefined. |
| 01 | RO | Impl Spec | **Completion Queue Support (CQS):** If this bit is set to '1', then the controller supports Admin and I/O Completion Queues in the Controller Memory Buffer. If this bit is cleared to '0', then Completion Queues shall not be placed in the Controller Memory Buffer. |
| 00 | RO | Impl Spec | **Submission Queue Support (SQS):** If this bit is set to '1', then the controller supports Admin and I/O Submission Queues in the Controller Memory Buffer. If this bit is cleared to '0', then the host shall not place Submission Queues in the Controller Memory Buffer. If the host places Submission Queues in the Controller Memory Buffer, then controller behavior is undefined. |


---

## 3.1.4.13 Offset 40h: BPINFO – Boot Partition Information

This optional property defines the characteristics of Boot Partitions (refer to section 8.1.3). If the controller does not support the Boot Partitions feature, then this property shall be cleared to 0h.
===== page_number= 68, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 49, coordinate:(115,104,880,437) -->
**Figure 49: Offset 40h: BPINFO – Boot Partition Information**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31 | RO | Impl Spec | **Active Boot Partition ID (ABPID):** This bit indicates the identifier of the active Boot Partition. |
| 30:26 | RO | 0h | Reserved |
| 25:24 | RO | 00b | **Boot Read Status (BRS):** This field indicates the status of Boot Partition read operations initiated by the host writing to the BPRSEL.BPID field. Refer to section 8.1.3. <br><br> The boot read status values are defined as: <br><br> <table><tr><th>Value</th><th>Definition</th></tr><tr><td>00b</td><td>No Boot Partition read operation requested</td></tr><tr><td>01b</td><td>Boot Partition read in progress</td></tr><tr><td>10b</td><td>Boot Partition read completed successfully</td></tr><tr><td>11b</td><td>Error completing Boot Partition read</td></tr></table> <br><br> If a host writes the BPRSEL.BPID field, this field transitions to 01b. After successfully completing a Boot Partition read operation (i.e., transferring the contents to the boot memory buffer), the controller sets this field to 10b. If there is an error completing a Boot Partition read operation, this field is set to 11b, and the contents of the boot memory buffer are undefined. |
| 23:15 | RO | 0h | Reserved |
| 14:00 | RO | Impl Spec | **Boot Partition Size (BPSZ):** This field defines the size of each Boot Partition in multiples of 128 KiB. Both Boot Partitions are the same size. |

**3.1.4.14 Offset 44h: BPRSEL – Boot Partition Read Select**

This optional property is used to initiate the transfer of a data in the Boot Partition (refer to section 8.1.3) from the controller to the host. If the controller does not support the Boot Partitions feature, then this property shall be cleared to 0h.

If the host attempts to read beyond the end of a Boot Partition (i.e., the Boot Partition Read Offset plus Boot Partition Read Size, is greater than the Boot Partition Size in bytes), the controller shall not transfer data and report an error in the BPINFO.BRS field.

<!-- Figure 50, coordinate:(115,580,880,725) -->
**Figure 50: Offset 44h: BPRSEL – Boot Partition Read Select**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31 | RW | 0b | **Boot Partition Identifier (BPID):** This bit specifies the Boot Partition identifier for the Boot Partition read operation. |
| 30 | RO | 0b | Reserved |
| 29:10 | RW | 0h | **Boot Partition Read Offset (BPROF):** This field selects the offset into the Boot Partition, in 4 KiB units, that the controller copies into the Boot Partition Memory Buffer. |
| 09:00 | RW | 0h | **Boot Partition Read Size (BPRSZ):** This field selects the read size in multiples of 4 KiB to copy into the Boot Partition Memory Buffer. |

**3.1.4.15 Offset 48h: BPMBL – Boot Partition Memory Buffer Location**

This optional property specifies the memory buffer that is used as the destination for data when a Boot Partition is read (refer to section 8.1.3). If the controller does not support the Boot Partitions feature, then this property shall be cleared to 0h.

<!-- Figure 51, coordinate:(115,820,880,908) -->
**Figure 51: Offset 48h: BPMBL – Boot Partition Memory Buffer Location**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | 0h | **Boot Partition Memory Buffer Base Address (BMBBA):** This field specifies the 52 most significant bits of the 64-bit physical address for the Boot Partition Memory Buffer. |
| 11:00 | RO | 0h | Reserved |

68
===== page_number= 69, page_type= body ==___

# NVM Express® Base Specification, Revision 2.3



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31 | RO | Impl Spec | **Active Boot Partition ID (ABPID):** This bit indicates the identifier of the active Boot Partition. |
| 30:26 | RO | 0h | Reserved |
| 25:24 | RO | 00b | **Boot Read Status (BRS):** This field indicates the status of Boot Partition read operations initiated by the host writing to the BPRSEL.BPID field. Refer to section 8.1.3. <br><br> The boot read status values are defined as: <br><br> <table><tr><th>Value</th><th>Definition</th></tr><tr><td>00b</td><td>No Boot Partition read operation requested</td></tr><tr><td>01b</td><td>Boot Partition read in progress</td></tr><tr><td>10b</td><td>Boot Partition read completed successfully</td></tr><tr><td>11b</td><td>Error completing Boot Partition read</td></tr></table> <br><br> If a host writes the BPRSEL.BPID field, this field transitions to 01b. After successfully completing a Boot Partition read operation (i.e., transferring the contents to the boot memory buffer), the controller sets this field to 10b. If there is an error completing a Boot Partition read operation, this field is set to 11b, and the contents of the boot memory buffer are undefined. |
| 23:15 | RO | 0h | Reserved |
| 14:00 | RO | Impl Spec | **Boot Partition Size (BPSZ):** This field defines the size of each Boot Partition in multiples of 128 KiB. Both Boot Partitions are the same size. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31 | RW | 0b | **Boot Partition Identifier (BPID):** This bit specifies the Boot Partition identifier for the Boot Partition read operation. |
| 30 | RO | 0b | Reserved |
| 29:10 | RW | 0h | **Boot Partition Read Offset (BPROF):** This field selects the offset into the Boot Partition, in 4 KiB units, that the controller copies into the Boot Partition Memory Buffer. |
| 09:00 | RW | 0h | **Boot Partition Read Size (BPRSZ):** This field selects the read size in multiples of 4 KiB to copy into the Boot Partition Memory Buffer. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | 0h | **Boot Partition Memory Buffer Base Address (BMBBA):** This field specifies the 52 most significant bits of the 64-bit physical address for the Boot Partition Memory Buffer. |
| 11:00 | RO | 0h | Reserved |


---

## 3.1.4.16 Offset 50h: CMBMSC – Controller Memory Buffer Memory Space Control

This optional property specifies how the controller references the Controller Memory Buffer with host-supplied addresses. If the controller supports the Controller Memory Buffer (CAP.CMBS), this property is mandatory. Otherwise, this property is reserved.

This property shall not be reset by a Controller Level Reset initiated by:
- a Controller Reset; and
- a Function Level Reset (refer to the NVMe over PCIe Transport Specification).

### Figure 52: Offset 50h: CMBMSC – Controller Memory Buffer Memory Space Control

<!-- Figure 52, coordinate:(115,255,880,685) -->

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | 0h | **Controller Base Address (CBA):** This field specifies the 52 most significant bits of the 64-bit base address for the Controller Memory Buffer’s controller address range. The Controller Memory Buffer’s controller base address and its size determine its controller address range.<br><br>The specified address shall be valid only under the following conditions:<br>a) no part of the Controller Memory Buffer’s controller address range is greater than 2<sup>64</sup> – 1; and<br>b) if the Persistent Memory Region’s controller memory space is enabled, then the Controller Memory Buffer’s controller address range does not overlap the Persistent Memory Region’s controller address range. |
| 11:02 | RO | 0h | Reserved |
| 01 | RW | 0b | **Controller Memory Space Enable (CMSE):** This bit specifies whether addresses supplied by the host are permitted to reference the Controller Memory Buffer.<br><br>If CMBMSC.CRE is cleared to ‘0’ this bit has no effect, and the Controller Memory Buffer’s controller memory space is not enabled.<br><br>If this bit is set to ‘1’ and the controller base address is valid, then the Controller Memory Buffer’s controller memory space is enabled. Otherwise, the controller memory space is not enabled.<br><br>If the Controller Memory Buffer’s controller memory space is enabled, then addresses supplied by the host that fall within the Controller Memory Buffer’s controller address range shall reference the Controller Memory Buffer.<br><br>If the Controller Memory Buffer’s controller memory space is not enabled, then no address supplied by the host shall reference the Controller Memory Buffer. Instead, such addresses shall reference memory spaces other than the Controller Memory Buffer. |
| 00 | RW | 0b | **Capabilities Registers Enabled (CRE):** This bit specifies whether the CMBLOC and CMBSZ properties are enabled. If this bit is set to ‘1’, then CMBLOC is defined as shown in Figure 47 and CMBSZ is defined as shown in Figure 48. If this bit is cleared to ‘0’, then CMBSZ and CMBLOC are cleared to 0h. |



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 63:12 | RW | 0h | **Controller Base Address (CBA):** This field specifies the 52 most significant bits of the 64-bit base address for the Controller Memory Buffer’s controller address range. The Controller Memory Buffer’s controller base address and its size determine its controller address range.<br><br>The specified address shall be valid only under the following conditions:<br>a) no part of the Controller Memory Buffer’s controller address range is greater than 2<sup>64</sup> – 1; and<br>b) if the Persistent Memory Region’s controller memory space is enabled, then the Controller Memory Buffer’s controller address range does not overlap the Persistent Memory Region’s controller address range. |
| 11:02 | RO | 0h | Reserved |
| 01 | RW | 0b | **Controller Memory Space Enable (CMSE):** This bit specifies whether addresses supplied by the host are permitted to reference the Controller Memory Buffer.<br><br>If CMBMSC.CRE is cleared to ‘0’ this bit has no effect, and the Controller Memory Buffer’s controller memory space is not enabled.<br><br>If this bit is set to ‘1’ and the controller base address is valid, then the Controller Memory Buffer’s controller memory space is enabled. Otherwise, the controller memory space is not enabled.<br><br>If the Controller Memory Buffer’s controller memory space is enabled, then addresses supplied by the host that fall within the Controller Memory Buffer’s controller address range shall reference the Controller Memory Buffer.<br><br>If the Controller Memory Buffer’s controller memory space is not enabled, then no address supplied by the host shall reference the Controller Memory Buffer. Instead, such addresses shall reference memory spaces other than the Controller Memory Buffer. |
| 00 | RW | 0b | **Capabilities Registers Enabled (CRE):** This bit specifies whether the CMBLOC and CMBSZ properties are enabled. If this bit is set to ‘1’, then CMBLOC is defined as shown in Figure 47 and CMBSZ is defined as shown in Figure 48. If this bit is cleared to ‘0’, then CMBSZ and CMBLOC are cleared to 0h. |


---

## 3.1.4.17 Offset 58h: CMBSTS – Controller Memory Buffer Status

This optional property indicates the status of the Controller Memory Buffer. If the controller supports the Controller Memory Buffer (CAP.CMBS), this property is mandatory. Otherwise, this property is reserved.

### Figure 53: Offset 58h: CMBSTS – Controller Memory Buffer Status

<!-- Figure 53, coordinate:(115,785,880,880) -->

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:01 | RO | 0h | Reserved |
| 00 | RO | 0b | **Controller Base Address Invalid (CBAI):** This bit indicates whether the controller has failed to enable the Controller Memory Buffer’s controller memory space because CMBMSC.CBA is invalid. If CMBMSC.CRE and CMBMSC.CMSE are set to ‘1’, and CMBMSC.CBA is invalid, this bit shall be set to ‘1’. Otherwise, this bit shall be cleared to ‘0’. |

---
===== page_number= 70, page_type= body ====

NVM Express® Base Specification, Revision 2.3



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:01 | RO | 0h | Reserved |
| 00 | RO | 0b | **Controller Base Address Invalid (CBAI):** This bit indicates whether the controller has failed to enable the Controller Memory Buffer’s controller memory space because CMBMSC.CBA is invalid. If CMBMSC.CRE and CMBMSC.CMSE are set to ‘1’, and CMBMSC.CBA is invalid, this bit shall be set to ‘1’. Otherwise, this bit shall be cleared to ‘0’. |


---

### 3.1.4.18 Offset 5Ch: CMBEBS – Controller Memory Buffer Elasticity Buffer Size

This optional property identifies to the host the size of the CMB elasticity buffer. A value of 0h in this property indicates to the host that no information regarding the presence or size of a CMB elasticity buffer is available.

#### Figure 54: Offset 5Ch: CMBEBS – Controller Memory Buffer Elasticity Buffer Size

<!-- Figure 54, coordinate:(114,203,878,503) -->

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **CMB Elasticity Buffer Size Base (CMBWBZ)**: Indicates the size of the CMB elasticity buffer. The size of the CMB elasticity buffer is equal to the value in this field multiplied by the value specified by the CMB Elasticity Buffer Size Units field. |
| 7:5 | RO | 0h | Reserved |
| 4 | RO | Impl Spec | **CMB Read Bypass Behavior (CMBRBB)**: If a memory read does not conflict with any memory write in the CMB Elasticity Buffer (i.e., if the set of memory addresses specified by a read is disjoint from the set of memory addresses specified by all writes in the CMB Elasticity Buffer), and this bit is:<br>a) set to '1', then memory reads not conflicting with memory writes in the CMB Elasticity Buffer shall bypass those memory writes; and<br>b) cleared to '0', then memory reads not conflicting with memory writes in the CMB Elasticity Buffer may bypass those memory writes. |
| 3:0 | RO | Impl Spec | **CMB Elasticity Buffer Size Units (CMBSZU)**: Indicates the granularity of the CMB Elasticity Buffer Size Base field.<br><br><table><tr><th>Value</th><th>Granularity</th></tr><tr><td>0h</td><td>Bytes</td></tr><tr><td>1h</td><td>1 KiB</td></tr><tr><td>2h</td><td>1 MiB</td></tr><tr><td>3h</td><td>1 GiB</td></tr><tr><td>4h – Fh</td><td>Reserved</td></tr></table> |



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **CMB Elasticity Buffer Size Base (CMBWBZ)**: Indicates the size of the CMB elasticity buffer. The size of the CMB elasticity buffer is equal to the value in this field multiplied by the value specified by the CMB Elasticity Buffer Size Units field. |
| 7:5 | RO | 0h | Reserved |
| 4 | RO | Impl Spec | **CMB Read Bypass Behavior (CMBRBB)**: If a memory read does not conflict with any memory write in the CMB Elasticity Buffer (i.e., if the set of memory addresses specified by a read is disjoint from the set of memory addresses specified by all writes in the CMB Elasticity Buffer), and this bit is:<br>a) set to '1', then memory reads not conflicting with memory writes in the CMB Elasticity Buffer shall bypass those memory writes; and<br>b) cleared to '0', then memory reads not conflicting with memory writes in the CMB Elasticity Buffer may bypass those memory writes. |
| 3:0 | RO | Impl Spec | **CMB Elasticity Buffer Size Units (CMBSZU)**: Indicates the granularity of the CMB Elasticity Buffer Size Base field.<br><br><table><tr><th>Value</th><th>Granularity</th></tr><tr><td>0h</td><td>Bytes</td></tr><tr><td>1h</td><td>1 KiB</td></tr><tr><td>2h</td><td>1 MiB</td></tr><tr><td>3h</td><td>1 GiB</td></tr><tr><td>4h – Fh</td><td>Reserved</td></tr></table> |


---

### 3.1.4.19 Offset 60h: CMBSWTP – Controller Memory Buffer Sustained Write Throughput

This optional property identifies to the host the maximum CMB sustained write throughput. A value of 0h in this property indicates to the host that no information regarding the CMB sustained write throughput is available.

#### Figure 55: Offset 60h: CMBSWTP – Controller Memory Buffer Sustained Write Throughput

<!-- Figure 55, coordinate:(114,622,878,853) -->

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **CMB Sustained Write Throughput (CMBSWTV)**: Indicates the sustained write throughput of the CMB at the maximum payload size specified by the applicable NVMe Transport binding specification (e.g., the PCIe TLP payload size, as specified in the Max_Payload_Size (MPS) field of the PCIe Express Device Control (PXDC) register). The sustained write throughput of the CMB is equal to the value in this field multiplied by the units specified by the CMB Sustained Write Throughput Units field. |
| 7:4 | RO | 0h | Reserved |
| 3:0 | RO | Impl Spec | **CMB Sustained Write Throughput Units (CMBSWTU)**: Indicates the granularity of the CMB Sustained Write Throughput field.<br><br><table><tr><th>Value</th><th>Granularity</th></tr><tr><td>0h</td><td>Bytes/second</td></tr><tr><td>1h</td><td>1 KiB/second</td></tr><tr><td>2h</td><td>1 MiB/second</td></tr><tr><td>3h</td><td>1 GiB/second</td></tr><tr><td>4h – Fh</td><td>Reserved</td></tr></table> |

70
===== page_number= 71, page_type= body ====

NVM Express® Base Specification, Revision 2.3



| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **CMB Sustained Write Throughput (CMBSWTV)**: Indicates the sustained write throughput of the CMB at the maximum payload size specified by the applicable NVMe Transport binding specification (e.g., the PCIe TLP payload size, as specified in the Max_Payload_Size (MPS) field of the PCIe Express Device Control (PXDC) register). The sustained write throughput of the CMB is equal to the value in this field multiplied by the units specified by the CMB Sustained Write Throughput Units field. |
| 7:4 | RO | 0h | Reserved |
| 3:0 | RO | Impl Spec | **CMB Sustained Write Throughput Units (CMBSWTU)**: Indicates the granularity of the CMB Sustained Write Throughput field.<br><br><table><tr><th>Value</th><th>Granularity</th></tr><tr><td>0h</td><td>Bytes/second</td></tr><tr><td>1h</td><td>1 KiB/second</td></tr><tr><td>2h</td><td>1 MiB/second</td></tr><tr><td>3h</td><td>1 GiB/second</td></tr><tr><td>4h – Fh</td><td>Reserved</td></tr></table> |


---

### 3.1.4.20 Offset 64h: NSSD – NVM Subsystem Shutdown

This optional property provides a host with the capability to initiate a normal or an abrupt NVM Subsystem Shutdown.

Support for this property is indicated by the state of the NVM Subsystem Shutdown Supported (CAP.NSSS) field. If this property is not supported, then the address range occupied by this property is reserved.

The NVM Subsystem Shutdown Enhancements Supported (CAP.NSES) bit affects the functionality invoked by host modification of this property (refer to section 3.6.3).

#### Figure 56: Offset 64h: NSSD – NVM Subsystem Shutdown

<!-- Figure 56, coordinate:(115,253,878,488) -->

| Bits  | Type | Reset | Description |
|-------|------|-------|-------------|
| 31:00 | RW   | 0h    | **NVM Subsystem Shutdown Control (NSSC):** A write of the value 4E726D6Ch ("Nrm!") to this field initiates a normal NVM Subsystem Shutdown on every controller: <ul><li>in the domain associated with the controller when CAP.CPS is set to 10b (i.e., domain scope) as specified in section 3.6.3.2 or</li><li>in the NVM subsystem when CAP.CPS is set to 11b (i.e., NVM subsystem scope) in the NVM subsystem as specified in section 3.6.3.1.</li></ul> A write of the value 41627074h ("Abpt") to this field initiates an abrupt NVM subsystem shutdown on every controller: <ul><li>in the domain associated with the controller when CAP.CPS is set to 10b as specified in section 3.6.3.2; or</li><li>in the NVM subsystem when CAP.CPS is set to 11b in the NVM subsystem as specified in section 3.6.3.1.</li></ul> A write of any other value to this field has no functional effect on the operation of the NVM subsystem. This field shall return the value 0h when read. |



| Bits  | Type | Reset | Description |
|-------|------|-------|-------------|
| 31:00 | RW   | 0h    | **NVM Subsystem Shutdown Control (NSSC):** A write of the value 4E726D6Ch ("Nrm!") to this field initiates a normal NVM Subsystem Shutdown on every controller: <ul><li>in the domain associated with the controller when CAP.CPS is set to 10b (i.e., domain scope) as specified in section 3.6.3.2 or</li><li>in the NVM subsystem when CAP.CPS is set to 11b (i.e., NVM subsystem scope) in the NVM subsystem as specified in section 3.6.3.1.</li></ul> A write of the value 41627074h ("Abpt") to this field initiates an abrupt NVM subsystem shutdown on every controller: <ul><li>in the domain associated with the controller when CAP.CPS is set to 10b as specified in section 3.6.3.2; or</li><li>in the NVM subsystem when CAP.CPS is set to 11b in the NVM subsystem as specified in section 3.6.3.1.</li></ul> A write of any other value to this field has no functional effect on the operation of the NVM subsystem. This field shall return the value 0h when read. |


---

### 3.1.4.21 Offset 68h: CRTO – Controller Ready Timeouts

This property indicates the controller ready timeout values. This property is mandatory for controllers compliant with NVM Express Base Specification revision 2.0 and later.

#### Figure 57: Offset 68h: CRTO – Controller Ready Timeouts

<!-- Figure 57, coordinate:(115,588,878,832) -->

| Bits  | Type | Reset     | Description |
|-------|------|-----------|-------------|
| 31:16 | RO   | Impl Spec | **Controller Ready Independent of Media Timeout (CRIMT):** If the CAP.CRMS.CRIMS bit is cleared to '0', then the controller shall clear this field to 0h and the host should ignore this field. <br><br> If the CAP.CRMS.CRIMS bit is set to '1', then this field contains the worst-case time that a host should wait after CC.EN transitions from '0' to '1' for the controller to become ready and be able to successfully process all commands that do not access attached namespaces and Admin commands that do not require access to media when the controller is in Controller Ready Independent of Media mode (i.e., the CC.CRIME bit is set to '1'). Attached namespaces and media required to process Admin commands may or may not be ready within this time period (refer to section 3.5.3, section 3.5.4, and Figure 84). <br><br> This worst-case time may be experienced after events such as an abrupt shutdown or activation of a new firmware image; typical times are expected to be much shorter. This field is in 500 millisecond units. <br><br> The value of this field should not exceed FFh (i.e., 127.5 seconds). |

---
===== page_number= 72, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 57, coordinate:(120,104,870,358) -->
**Figure 57: Offset 68h: CRTO – Controller Ready Timeouts**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 15:0 | RO | Impl Spec | **Controller Ready With Media Timeout (CRWMT):** This field contains the worst-case time that a host should wait after CC.EN transitions from '0' to '1' for:<br>a) the controller to become ready and be able to successfully process all commands; and<br>b) all attached namespaces and media required to process Admin commands to become ready,<br>independent of which ready mode (refer to CC.CRIME) the controller is in (refer to section 3.5.3 and section 3.5.4).<br><br>This worst-case time may be experienced after events such as an abrupt shutdown or activation of a new firmware image; typical times are expected to be much shorter. This field is in 500 millisecond units.<br><br>The value of this field shall be greater than or equal to the value of the CRTO.CRIMT field and may be significantly larger than the value of the CRTO.CRIMT field. |

---

**3.1.4.22 Offset E00h: PMRCAP – Persistent Memory Region Capabilities**

This property indicates capabilities of the Persistent Memory Region. If the controller does not support the Persistent Memory Region feature, then this property shall be cleared to 0h.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

<!-- Figure 58, coordinate:(115,465,875,870) -->
**Figure 58: Offset E00h: PMRCAP – Persistent Memory Region Capabilities**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:25 | RO | 0h | Reserved |
| 24 | RO | Impl Spec | **Controller Memory Space Supported (CMSS):** If this bit is set to '1', then the addresses supplied by the host are permitted to reference the Persistent Memory Region only if the host has enabled the Persistent Memory Region's controller memory space.<br><br>If the controller supports referencing the Persistent Memory Region with host-supplied addresses, then this bit shall be set to '1'. Otherwise, this bit shall be cleared to '0'. |
| 23:16 | RO | Impl Spec | **Persistent Memory Region Timeout (PMRTO):** This field contains the minimum amount of time that a host should wait for the Persistent Memory Region to become ready or not ready after PMRCTLEN is modified. The time in this field is expressed in Persistent Memory Region time units (refer to PMRCAP.PMRTU). |
| 15:14 | RO | 00b | Reserved |
| 13:10 | RO | Impl Spec | **Persistent Memory Region Write Barrier Mechanisms (PMRWBM):** This field lists mechanisms that may be used to ensure that previous writes to the Persistent Memory Region have completed and are persistent when the Persistent Memory Region is ready and operating normally. A bit in this field is set to '1' if the corresponding mechanism to ensure persistence is supported. A bit in this field is cleared to '0' if the corresponding mechanism to ensure persistence is not supported.<br><br>At least one bit in this field shall be set to '1'.<br><br><table><tr><th>Bits</th><th>Description</th></tr><tr><td>3:2</td><td>Reserved</td></tr><tr><td>1</td><td>**Completion of PMRSTS Read (CPMTSTSR):** The completion of a read to the PMRSTS property shall ensure that all prior writes to the Persistent Memory Region have completed and are persistent.</td></tr><tr><td>0</td><td>**Completion of Memory Read (CMR):** The completion of a memory read from any Persistent Memory Region address ensures that all prior writes to the Persistent Memory Region have completed and are persistent.</td></tr></table> |

---

72
===== page_number= 73, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 58, coordinate:(115,105,880,460) -->
**Figure 58: Offset E00h: PMRCAP – Persistent Memory Region Capabilities**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 9:8 | RO | Impl Spec | **Persistent Memory Region Time Units (PMRTU):** Indicates Persistent Memory Region time units. <br> <table><tr><th>Value</th><th>Persistent Memory Region Time Units</th></tr><tr><td>00b</td><td>500 milliseconds</td></tr><tr><td>01b</td><td>minutes</td></tr><tr><td>10b to 11b</td><td>Reserved</td></tr></table> |
| 7:5 | RO | Impl Spec | **Base Indicator Register (BIR):** This field indicates the Base Address Register (BAR) that specifies the address and size of the Persistent Memory Region. Values 010b, 011b, 100b, and 101b are valid. |
| 4 | RO | Impl Spec | **Write Data Support (WDS):** If this bit is set to '1', then the controller supports data and metadata in the Persistent Memory Region for commands that transfer data from the host to the controller (e.g., Write). If this bit is cleared to '0', then data and metadata for commands that transfer data from the host to the controller shall not be transferred to the Persistent Memory Region. <br> If PMRCAP.CMSS is cleared to '0', this bit shall be cleared to '0'. |
| 3 | RO | Impl Spec | **Read Data Support (RDS):** If this bit is set to '1', then the controller supports data and metadata in the Persistent Memory Region for commands that transfer data from the controller to the host (e.g., Read). If this bit is cleared to '0', then all data and metadata for commands that transfer data from the controller to the host shall not be transferred from the Persistent Memory Region. <br> If PMRCAP.CMSS is cleared to '0', this bit shall be cleared to '0'. |
| 2:0 | RO | 000b | Reserved |

**3.1.4.23 Offset E04h: PMRCTL – Persistent Memory Region Control**

This optional property controls the operation of the Persistent Memory Region. If the controller does not support the Persistent Memory Region feature, then this property shall be cleared to 0h.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

<!-- Figure 59, coordinate:(115,565,880,675) -->
**Figure 59: Offset E04h: PMRCTL – Persistent Memory Region Control**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:1 | RO | 0h | Reserved |
| 0 | RW | 0b | **Enable (EN):** When set to '1', then the Persistent Memory Region is ready to process PCI Express memory read and write requests once PMRSTS.NRDY is cleared to '0'. When cleared to '0', then the Persistent Memory Region is disabled and PMRSTS.NRDY shall be set to '1' once the Persistent Memory Region is ready to be re-enabled. |

**3.1.4.24 Offset E08h: PMRSTS – Persistent Memory Region Status**

This optional property provides the status of the Persistent Memory Region. If the controller does not support the Persistent Memory Region feature, then this property shall be cleared to 0h.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

<!-- Figure 60, coordinate:(115,780,880,835) -->
**Figure 60: Offset E08h: PMRSTS – Persistent Memory Region Status**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:13 | RO | 0h | Reserved |

___
===== page_number= 74, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 60, coordinate:(114,106,880,722) -->
**Figure 60: Offset E08h: PMRSTS – Persistent Memory Region Status**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 12 | RO | 0b | **Controller Base Address Invalid (CBAI):** This field indicates whether the controller has failed to enable the Persistent Memory Region’s controller memory space because the controller 64-bit base address specified by PMRMSCU.CBA and PMRMSCL.CBA are invalid. If PMRCAP.CMSS is set to ‘1’, PMRMSCU.CMSE is set to ‘1’, and the controller 64-bit base address specified by PMRMSCU.CBA and PMRMSCL.CBA is invalid, this bit shall be set to ‘1’. Otherwise, this bit shall be cleared to ‘0’. |
| 11:9 | RO | 000b | **Health Status (HSTS):** If the Persistent Memory Region (PMR) is ready, then this field indicates the health status of the Persistent Memory Region. This field is always cleared to 000b when the Persistent Memory Region is not ready. <br><br> The health status values are defined as: <br><br> | Value | Definition | <br> | 000b | **Normal Operation:** The Persistent Memory Region is operating normally. | <br> | 001b | **Restore Error:** The Persistent Memory Region is operating normally and is persistent; however, the contents of the Persistent Memory Region may not have been restored correctly (i.e., may not contain the contents prior to the last power cycle, NVM Subsystem Reset, Controller Level Reset, or Persistent Memory Region disable). | <br> | 010b | **Read Only:** The Persistent Memory Region is read only. PMR writes do not update the Persistent Memory Region. PMR reads return the data that was last written. Refer to section 8.2.4 for details of PMR writes and PMR reads. | <br> | 011b | **Unreliable:** The Persistent Memory Region has become unreliable. PMR reads may return invalid data. PCI Express PMR reads may generate poisoned PCI Express TLP(s). PMR writes may not update memory or may update memory with undefined data. The Persistent Memory Region may also have become non-persistent. | <br> | 100b to 111b | Reserved |
| 8 | RO | 0b | **Not Ready (NRDY):** This bit indicates if the Persistent Memory Region is ready for use. If this bit is cleared to ‘0’ and the PMRCTL.EN is set to ‘1’, then the Persistent Memory Region is ready to accept and process PMR reads and PMR writes. If this bit is set to ‘1’ or the PMRCTL.EN bit is cleared to ‘0’, then the Persistent Memory Region is not ready to process PMR reads and PMR writes. |
| 7:0 | RO | 0h | **Error (ERR):** When the Persistent Memory Region is ready and operating normally, this field indicates whether previous PMR writes have completed without error. If this field is cleared to 0h, then previous PMR writes have completed without error and the values written are persistent. A non-zero value in this field indicates the occurrence of an error that may have caused one or more of the previous PMR writes to not have completed successfully. The meaning of any particular non-zero value is vendor specific. <br><br> Once this field takes on a non-zero value, it maintains a non-zero value until the PCI Function is reset. |

**3.1.4.25 Offset E0Ch: PMREBS – Persistent Memory Region Elasticity Buffer Size**

This optional property identifies to the host the size of the PMR elasticity buffer. A value of 0h in this property indicates to the host that no information regarding the presence or size of a PMR elasticity buffer is available.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.
===== page_number= 75, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 61, coordinate:(115,105,878,428) -->
**Figure 61: Offset E0Ch: PMREBS – Persistent Memory Region Elasticity Buffer Size**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **PMR Elasticity Buffer Size Base (PMRWBZ)**: Indicates the size of the PMR elasticity buffer. The actual size of the PMR elasticity buffer is equal to the value in this field multiplied by the value specified by the PMR Elasticity Buffer Size Units field. |
| 7:5 | RO | 000b | Reserved |
| 4 | RO | Impl Spec | **PMR Read Bypass Behavior (PMRRBB)**: If a memory read does not conflict with any memory write in the PMR Elasticity Buffer (i.e., if the set of memory addresses specified by a read is disjoint from the set of memory addresses specified by all writes in the PMR Elasticity Buffer), and this bit is:<br>a) set to ‘1’, then memory reads not conflicting with memory writes in the PMR Elasticity Buffer shall bypass those writes; and<br>b) cleared to ‘0’, then memory reads not conflicting with memory writes in the PMR Elasticity Buffer may bypass those memory writes. |
| 3:0 | RO | Impl Spec | **PMR Elasticity Buffer Size Units (PMRSZU)**: Indicates the granularity of the PMR Elasticity Buffer Size Base field.<br><br>**Value** | **Definition**<br>0h | Bytes<br>1h | 1 KiB<br>2h | 1 MiB<br>3h | 1 GiB<br>4h to Fh | Reserved |

---

**3.1.4.26 Offset E10h: PMRSWTP – Persistent Memory Region Sustained Write Throughput**

This optional property identifies to the host the maximum PMR sustained write throughput. A value of 0h in this property indicates to the host that no information regarding the PMR sustained write throughput is available.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

<!-- Figure 62, coordinate:(115,545,878,790) -->
**Figure 62: Offset E10h: PMRSWTP – Persistent Memory Region Sustained Write Throughput**

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **PMR Sustained Write Throughput (PMRSWTY)**: Indicates the sustained write throughput of the PMR at the maximum payload size specified by the applicable NVMe Transport binding specification (e.g., the PCIe TLP payload size, as specified in the Max_Payload_Size (MPS) field of the PCI Express Device Control (PXDC) register). The actual sustained write throughput of the PMR is equal to the value in this field multiplied by the units specified by the PMR Sustained Write Throughput Units field. |
| 7:4 | RO | 0h | Reserved |
| 3:0 | RO | Impl Spec | **PMR Sustained Write Throughput Units (PMRSWTU)**: Indicates the granularity of the PMR Sustained Write Throughput field.<br><br>**Value** | **Definition**<br>0h | Bytes per second<br>1h | 1 KiB / s<br>2h | 1 MiB / s<br>3h | 1 GiB / s<br>7h to Fh | Reserved |

---

**3.1.4.27 Offset E14h: PMRMSCL – Persistent Memory Region Memory Space Control Lower**

This optional property and the PMRMSCU property specify how the controller references the Persistent Memory Region with host-supplied addresses. If the controller supports the Persistent Memory Region’s controller memory space (PMRCAP.CMSS), this property is mandatory. Otherwise, this property is reserved.

For a memory-based controller, the host shall access this property with aligned 32-bit accesses.
===== page_number= 76, page_type= body ==___

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

**Figure 63: Offset E14h: PMRMSCl – Persistent Memory Region Memory Space Control Lower**

<!-- Figure 63, coordinate:(114,140,880,525) -->

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:12 | RW | 0h | **Controller Base Address (CBA):** This field specifies the 20 least significant bits of the 52 most significant bits of the 64-bit base address for the Persistent Memory Region’s controller address range. The Persistent Memory Region’s controller base address and its size determine its controller address range.<br><br>The 64-bit base address specified by this field and PMRMSCU.CBA when the CMSE bit is set to ‘1’ shall be valid only under the following conditions:<br><br>a) no part of the Persistent Memory Region’s controller address range is greater than 2<sup>64</sup> – 1; and<br><br>b) if the Controller Memory Buffer’s controller memory space is enabled, then the Persistent Memory Region’s controller address range does not overlap the Controller Memory Buffer’s controller address range. |
| 11:02 | RO | 0h | Reserved |
| 01 | RW | 0b | **Controller Memory Space Enable (CMSE):** This bit specifies whether addresses supplied by the host are permitted to reference the Persistent Memory Region.<br><br>If this bit is set to ‘1’ and the controller base address is valid, then the Persistent Memory Region’s controller memory space is enabled. Otherwise, the controller memory space is not enabled.<br><br>If the Persistent Memory Region’s controller memory space is enabled, then addresses supplied by the host that fall within the Persistent Memory Region’s controller address range shall reference the Persistent Memory Region.<br><br>If the Persistent Memory Region’s controller memory space is not enabled, then no address supplied by the host shall reference the Persistent Memory Region. Instead, such addresses shall reference memory spaces other than the Persistent Memory Region. |
| 00 | RO | 0b | Reserved |

**3.1.4.28 Offset E18h: PMRMSCU – Persistent Memory Region Memory Space Control Upper**

This optional property and the PMRMSCl property specify how the controller references the Persistent Memory Region with host-supplied addresses. If the controller supports the Persistent Memory Region’s controller memory space (PMRCAP.CMSS), this property is mandatory. Otherwise, this property is reserved.

For a memory-based controller, the host shall access this property with aligned 32-bit accesses.

This property shall not be reset by a Controller Level Reset initiated by a Controller Reset.

**Figure 64: Offset E18h: PMRMSCU – Persistent Memory Region Memory Space Control Upper**

<!-- Figure 64, coordinate:(114,697,880,770) -->

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RW | 0h | **Controller Base Address (CBA):** This field specifies the 32 most significant bits of the 52 most significant bits of the 64-bit base address for the Persistent Memory Region’s controller address range. The Persistent Memory Region’s controller base address and its size determine its controller address range. |

**3.2 NVM Subsystem Entities**

**3.2.1 Namespaces**

**3.2.1.1 Namespace Overview**

A namespace is a formatted quantity of non-volatile memory that may be directly accessed by a host. A namespace ID (NSID) is an identifier used by a controller to provide access to a namespace.
===== page_number= 77, page_type= body ==___

# NVM Express® Base Specification, Revision 2.3



| Bits  | Type | Reset     | Description |
|-------|------|-----------|-------------|
| 31:16 | RO   | Impl Spec | **Controller Ready Independent of Media Timeout (CRIMT):** If the CAP.CRMS.CRIMS bit is cleared to '0', then the controller shall clear this field to 0h and the host should ignore this field. <br><br> If the CAP.CRMS.CRIMS bit is set to '1', then this field contains the worst-case time that a host should wait after CC.EN transitions from '0' to '1' for the controller to become ready and be able to successfully process all commands that do not access attached namespaces and Admin commands that do not require access to media when the controller is in Controller Ready Independent of Media mode (i.e., the CC.CRIME bit is set to '1'). Attached namespaces and media required to process Admin commands may or may not be ready within this time period (refer to section 3.5.3, section 3.5.4, and Figure 84). <br><br> This worst-case time may be experienced after events such as an abrupt shutdown or activation of a new firmware image; typical times are expected to be much shorter. This field is in 500 millisecond units. <br><br> The value of this field should not exceed FFh (i.e., 127.5 seconds). |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 15:0 | RO | Impl Spec | **Controller Ready With Media Timeout (CRWMT):** This field contains the worst-case time that a host should wait after CC.EN transitions from '0' to '1' for:<br>a) the controller to become ready and be able to successfully process all commands; and<br>b) all attached namespaces and media required to process Admin commands to become ready,<br>independent of which ready mode (refer to CC.CRIME) the controller is in (refer to section 3.5.3 and section 3.5.4).<br><br>This worst-case time may be experienced after events such as an abrupt shutdown or activation of a new firmware image; typical times are expected to be much shorter. This field is in 500 millisecond units.<br><br>The value of this field shall be greater than or equal to the value of the CRTO.CRIMT field and may be significantly larger than the value of the CRTO.CRIMT field. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:25 | RO | 0h | Reserved |
| 24 | RO | Impl Spec | **Controller Memory Space Supported (CMSS):** If this bit is set to '1', then the addresses supplied by the host are permitted to reference the Persistent Memory Region only if the host has enabled the Persistent Memory Region's controller memory space.<br><br>If the controller supports referencing the Persistent Memory Region with host-supplied addresses, then this bit shall be set to '1'. Otherwise, this bit shall be cleared to '0'. |
| 23:16 | RO | Impl Spec | **Persistent Memory Region Timeout (PMRTO):** This field contains the minimum amount of time that a host should wait for the Persistent Memory Region to become ready or not ready after PMRCTLEN is modified. The time in this field is expressed in Persistent Memory Region time units (refer to PMRCAP.PMRTU). |
| 15:14 | RO | 00b | Reserved |
| 13:10 | RO | Impl Spec | **Persistent Memory Region Write Barrier Mechanisms (PMRWBM):** This field lists mechanisms that may be used to ensure that previous writes to the Persistent Memory Region have completed and are persistent when the Persistent Memory Region is ready and operating normally. A bit in this field is set to '1' if the corresponding mechanism to ensure persistence is supported. A bit in this field is cleared to '0' if the corresponding mechanism to ensure persistence is not supported.<br><br>At least one bit in this field shall be set to '1'.<br><br><table><tr><th>Bits</th><th>Description</th></tr><tr><td>3:2</td><td>Reserved</td></tr><tr><td>1</td><td>**Completion of PMRSTS Read (CPMTSTSR):** The completion of a read to the PMRSTS property shall ensure that all prior writes to the Persistent Memory Region have completed and are persistent.</td></tr><tr><td>0</td><td>**Completion of Memory Read (CMR):** The completion of a memory read from any Persistent Memory Region address ensures that all prior writes to the Persistent Memory Region have completed and are persistent.</td></tr></table> |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 9:8 | RO | Impl Spec | **Persistent Memory Region Time Units (PMRTU):** Indicates Persistent Memory Region time units. <br> <table><tr><th>Value</th><th>Persistent Memory Region Time Units</th></tr><tr><td>00b</td><td>500 milliseconds</td></tr><tr><td>01b</td><td>minutes</td></tr><tr><td>10b to 11b</td><td>Reserved</td></tr></table> |
| 7:5 | RO | Impl Spec | **Base Indicator Register (BIR):** This field indicates the Base Address Register (BAR) that specifies the address and size of the Persistent Memory Region. Values 010b, 011b, 100b, and 101b are valid. |
| 4 | RO | Impl Spec | **Write Data Support (WDS):** If this bit is set to '1', then the controller supports data and metadata in the Persistent Memory Region for commands that transfer data from the host to the controller (e.g., Write). If this bit is cleared to '0', then data and metadata for commands that transfer data from the host to the controller shall not be transferred to the Persistent Memory Region. <br> If PMRCAP.CMSS is cleared to '0', this bit shall be cleared to '0'. |
| 3 | RO | Impl Spec | **Read Data Support (RDS):** If this bit is set to '1', then the controller supports data and metadata in the Persistent Memory Region for commands that transfer data from the controller to the host (e.g., Read). If this bit is cleared to '0', then all data and metadata for commands that transfer data from the controller to the host shall not be transferred from the Persistent Memory Region. <br> If PMRCAP.CMSS is cleared to '0', this bit shall be cleared to '0'. |
| 2:0 | RO | 000b | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:1 | RO | 0h | Reserved |
| 0 | RW | 0b | **Enable (EN):** When set to '1', then the Persistent Memory Region is ready to process PCI Express memory read and write requests once PMRSTS.NRDY is cleared to '0'. When cleared to '0', then the Persistent Memory Region is disabled and PMRSTS.NRDY shall be set to '1' once the Persistent Memory Region is ready to be re-enabled. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:13 | RO | 0h | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 12 | RO | 0b | **Controller Base Address Invalid (CBAI):** This field indicates whether the controller has failed to enable the Persistent Memory Region’s controller memory space because the controller 64-bit base address specified by PMRMSCU.CBA and PMRMSCL.CBA are invalid. If PMRCAP.CMSS is set to ‘1’, PMRMSCU.CMSE is set to ‘1’, and the controller 64-bit base address specified by PMRMSCU.CBA and PMRMSCL.CBA is invalid, this bit shall be set to ‘1’. Otherwise, this bit shall be cleared to ‘0’. |
| 11:9 | RO | 000b | **Health Status (HSTS):** If the Persistent Memory Region (PMR) is ready, then this field indicates the health status of the Persistent Memory Region. This field is always cleared to 000b when the Persistent Memory Region is not ready. <br><br> The health status values are defined as: <br><br> | Value | Definition | <br> | 000b | **Normal Operation:** The Persistent Memory Region is operating normally. | <br> | 001b | **Restore Error:** The Persistent Memory Region is operating normally and is persistent; however, the contents of the Persistent Memory Region may not have been restored correctly (i.e., may not contain the contents prior to the last power cycle, NVM Subsystem Reset, Controller Level Reset, or Persistent Memory Region disable). | <br> | 010b | **Read Only:** The Persistent Memory Region is read only. PMR writes do not update the Persistent Memory Region. PMR reads return the data that was last written. Refer to section 8.2.4 for details of PMR writes and PMR reads. | <br> | 011b | **Unreliable:** The Persistent Memory Region has become unreliable. PMR reads may return invalid data. PCI Express PMR reads may generate poisoned PCI Express TLP(s). PMR writes may not update memory or may update memory with undefined data. The Persistent Memory Region may also have become non-persistent. | <br> | 100b to 111b | Reserved |
| 8 | RO | 0b | **Not Ready (NRDY):** This bit indicates if the Persistent Memory Region is ready for use. If this bit is cleared to ‘0’ and the PMRCTL.EN is set to ‘1’, then the Persistent Memory Region is ready to accept and process PMR reads and PMR writes. If this bit is set to ‘1’ or the PMRCTL.EN bit is cleared to ‘0’, then the Persistent Memory Region is not ready to process PMR reads and PMR writes. |
| 7:0 | RO | 0h | **Error (ERR):** When the Persistent Memory Region is ready and operating normally, this field indicates whether previous PMR writes have completed without error. If this field is cleared to 0h, then previous PMR writes have completed without error and the values written are persistent. A non-zero value in this field indicates the occurrence of an error that may have caused one or more of the previous PMR writes to not have completed successfully. The meaning of any particular non-zero value is vendor specific. <br><br> Once this field takes on a non-zero value, it maintains a non-zero value until the PCI Function is reset. |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **PMR Elasticity Buffer Size Base (PMRWBZ)**: Indicates the size of the PMR elasticity buffer. The actual size of the PMR elasticity buffer is equal to the value in this field multiplied by the value specified by the PMR Elasticity Buffer Size Units field. |
| 7:5 | RO | 000b | Reserved |
| 4 | RO | Impl Spec | **PMR Read Bypass Behavior (PMRRBB)**: If a memory read does not conflict with any memory write in the PMR Elasticity Buffer (i.e., if the set of memory addresses specified by a read is disjoint from the set of memory addresses specified by all writes in the PMR Elasticity Buffer), and this bit is:<br>a) set to ‘1’, then memory reads not conflicting with memory writes in the PMR Elasticity Buffer shall bypass those writes; and<br>b) cleared to ‘0’, then memory reads not conflicting with memory writes in the PMR Elasticity Buffer may bypass those memory writes. |
| 3:0 | RO | Impl Spec | **PMR Elasticity Buffer Size Units (PMRSZU)**: Indicates the granularity of the PMR Elasticity Buffer Size Base field.<br><br>**Value** | **Definition**<br>0h | Bytes<br>1h | 1 KiB<br>2h | 1 MiB<br>3h | 1 GiB<br>4h to Fh | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:8 | RO | Impl Spec | **PMR Sustained Write Throughput (PMRSWTY)**: Indicates the sustained write throughput of the PMR at the maximum payload size specified by the applicable NVMe Transport binding specification (e.g., the PCIe TLP payload size, as specified in the Max_Payload_Size (MPS) field of the PCI Express Device Control (PXDC) register). The actual sustained write throughput of the PMR is equal to the value in this field multiplied by the units specified by the PMR Sustained Write Throughput Units field. |
| 7:4 | RO | 0h | Reserved |
| 3:0 | RO | Impl Spec | **PMR Sustained Write Throughput Units (PMRSWTU)**: Indicates the granularity of the PMR Sustained Write Throughput field.<br><br>**Value** | **Definition**<br>0h | Bytes per second<br>1h | 1 KiB / s<br>2h | 1 MiB / s<br>3h | 1 GiB / s<br>7h to Fh | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:12 | RW | 0h | **Controller Base Address (CBA):** This field specifies the 20 least significant bits of the 52 most significant bits of the 64-bit base address for the Persistent Memory Region’s controller address range. The Persistent Memory Region’s controller base address and its size determine its controller address range.<br><br>The 64-bit base address specified by this field and PMRMSCU.CBA when the CMSE bit is set to ‘1’ shall be valid only under the following conditions:<br><br>a) no part of the Persistent Memory Region’s controller address range is greater than 2<sup>64</sup> – 1; and<br><br>b) if the Controller Memory Buffer’s controller memory space is enabled, then the Persistent Memory Region’s controller address range does not overlap the Controller Memory Buffer’s controller address range. |
| 11:02 | RO | 0h | Reserved |
| 01 | RW | 0b | **Controller Memory Space Enable (CMSE):** This bit specifies whether addresses supplied by the host are permitted to reference the Persistent Memory Region.<br><br>If this bit is set to ‘1’ and the controller base address is valid, then the Persistent Memory Region’s controller memory space is enabled. Otherwise, the controller memory space is not enabled.<br><br>If the Persistent Memory Region’s controller memory space is enabled, then addresses supplied by the host that fall within the Persistent Memory Region’s controller address range shall reference the Persistent Memory Region.<br><br>If the Persistent Memory Region’s controller memory space is not enabled, then no address supplied by the host shall reference the Persistent Memory Region. Instead, such addresses shall reference memory spaces other than the Persistent Memory Region. |
| 00 | RO | 0b | Reserved |

| Bits | Type | Reset | Description |
|------|------|-------|-------------|
| 31:00 | RW | 0h | **Controller Base Address (CBA):** This field specifies the 32 most significant bits of the 52 most significant bits of the 64-bit base address for the Persistent Memory Region’s controller address range. The Persistent Memory Region’s controller base address and its size determine its controller address range. |


---

## 3.2.1.2 Valid and Invalid NSIDs

Valid NSIDs are the range of possible NSIDs that may be used to refer to namespaces that exist in the NVM subsystem. Any NSID is valid, except if that NSID is 0h or greater than the Number of Namespaces field reported in the Identify Controller data structure (refer to Figure 328). NSID FFFFFFFFh is a broadcast value that is used to specify all namespaces. An invalid NSID is any value that is not a valid NSID and is also not the broadcast value.

**Valid NSIDs are:**
a) allocated or unallocated in the NVM subsystem; and  
b) active or inactive for a specific controller.



---

## 3.2.1.3 Allocated and Unallocated NSID Types

In the NVM subsystem, a valid NSID is:
a) an allocated NSID; or  
b) an unallocated NSID.

Allocated NSIDs refer to namespaces that exist in the NVM subsystem. Unallocated NSIDs do not refer to any namespaces that exist in the NVM subsystem.



---

## 3.2.1.4 Active and Inactive NSID Types

For a specific controller, an allocated NSID is:
a) an active NSID; or  
b) an inactive NSID.

Active NSIDs for a controller refer to namespaces that are attached to that controller. Allocated NSIDs that are inactive for a controller refer to namespaces that are not attached to that controller.

Unallocated NSIDs are inactive NSIDs for all controllers in the NVM subsystem.

An allocated NSID may be an active NSID for some controllers and an inactive NSID for other controllers in the same NVM subsystem if the namespace that the NSID refers to is attached to some controllers, but not all controllers, in the NVM subsystem.

Refer to section 8.1.16 for actions associated with a namespace being detached or deleted.



---

## 3.2.1.5 NSID and Namespace Relationships

Unless otherwise noted, specifying an inactive NSID in a command that uses the Namespace Identifier (NSID) field shall cause the controller to abort the command with a status code of Invalid Field in Command. Specifying an invalid NSID in a command that uses the NSID field shall cause the controller to abort the command with a status code of Invalid Namespace or Format.

Figure 65 summarizes the valid NSID types and Figure 66 visually shows the NSID types and how they relate.

---

### Figure 65: NSID Types and Relationship to Namespace

<!-- Figure 65, coordinate:(114,740,870,878) -->

| Valid NSID Type   | NSID relationship to namespace                                      | Reference  |
|-------------------|---------------------------------------------------------------------|------------|
| Unallocated       | Does not refer to any namespace that exists in the NVM subsystem    | 3.2.1.3    |
| Allocated         | Refers to a namespace that exists in the NVM subsystem              | 3.2.1.3    |
| Inactive          | Does not refer to a namespace that is attached to the controller¹   | 3.2.1.4    |
| Active            | Refers to a namespace that is attached to the controller            | 3.2.1.4    |

**Notes:**
1. If allocated, refers to a namespace that is not attached to the controller. If unallocated, does not refer to any namespace.

---
===== page_number= 78, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 66: NSID Types, coordinate:(112,95,908,460) -->

**Figure 66: NSID Types**

The diagram illustrates the structure and usage of NSID (Namespace Identifier) values within the NVM subsystem and controller.

- **NSID Range**: From 0 to FFFFFFFFh (2^32 - 1).
- **NSID 0**: Invalid (Inv.).
- **NSID 1 to NN**: Valid.
- **NSID NN+1 to FFFFFFFFh**: Invalid, except for the last value (FFFFFFFFh), which is the Broadcast Value (B).

The diagram also shows the relationship between NSID states and the NVM Subsystem and Controller:

- **Allocated** (blue) → corresponds to **Active** (blue) in the Controller.
- **Unallocated** (brown) → corresponds to **Inactive** (brown) in the Controller.
- An arrow from **Inactive** to **Allocated** indicates a transition.

---



| Valid NSID Type   | NSID relationship to namespace                                      | Reference  |
|-------------------|---------------------------------------------------------------------|------------|
| Unallocated       | Does not refer to any namespace that exists in the NVM subsystem    | 3.2.1.3    |
| Allocated         | Refers to a namespace that exists in the NVM subsystem              | 3.2.1.3    |
| Inactive          | Does not refer to a namespace that is attached to the controller¹   | 3.2.1.4    |
| Active            | Refers to a namespace that is attached to the controller            | 3.2.1.4    |


![Figure 66](restored_images/Figure_66.png)
**Figure 66**


---

### 3.2.1.6 NSID and Namespace Usage

NSIDs shall be unique within the NVM subsystem (e.g., NSID of 3 shall refer to the same physical namespace regardless of the accessing controller) if:

a) Namespace Management (refer to section 8.1.16), ANA Reporting (refer to section 8.1.1), or NVM Sets (refer to section 3.2.2) capabilities are supported; or  
b) The Sanitize Namespace command is supported.

If the Namespace Management capability, the ANA Reporting capability, the NVM Sets capability, and the Sanitize Namespace command are not supported, then NSIDs:

a) for shared namespaces shall be unique within the NVM subsystem; and  
b) for private namespaces are not required to be unique within the NVM subsystem.

The Identify command (refer to section 5.2.13) may be used to determine the active NSIDs for a controller and the allocated NSIDs in the NVM subsystem.

If the MNAN field (refer to Figure 328) is cleared to 0h, then the maximum number of allocated NSIDs is the same as the value reported in the NN field (refer to Figure 328). If the MNAN field is non-zero, then the maximum number of allocated NSIDs may be less than the number of namespaces (e.g., an NVM subsystem may support a maximum valid NSID value (i.e., the NN field) set to 1,000,000 but support a maximum of 10 allocated NSID values).

To determine the active NSIDs for a particular controller, the host may follow either of the following methods:

1. Issue an Identify command with the CNS field cleared to 0h for each valid NSID (based on the Number of Namespaces value (i.e., MNAN field or NN field) in the Identify Controller data structure). If a non-zero data structure is returned for a particular NSID, then that is an active NSID; or  
2. Issue an Identify command with a CNS field set to 2h to retrieve a list of up to 1,024 active NSIDs. If there are more than 1,024 active NSIDs, continue to issue Identify commands with a CNS field set to 2h until all active NSIDs are retrieved.
===== page_number= 79, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

To determine the allocated NSIDs in the NVM subsystem, the host may issue an Identify command with the CNS field set to 10h to retrieve a list of up to 1,024 allocated NSIDs. If there are more than 1,024 allocated NSIDs, continue to issue Identify commands with a CNS field set to 10h until all allocated NSIDs are retrieved.

Namespace IDs may change across power off conditions. However, it is recommended that namespace IDs remain static across power off conditions to avoid issues with a host. To determine if the same namespace has been encountered, the host may use the:

a) UUID field in the Namespace Identification Descriptor (refer to Figure 331), if present;  
b) NGUID field in the Identify Namespace data (refer to the applicable NVM Express I/O Command Set specification) or in the Namespace Identification Descriptor, if present; or  
c) EUI64 field in the Identify Namespace data or in the Namespace Identification Descriptor, if present.

UIDREUSE bit in the NSFEAT field (refer to Figure 335 or the Identify Namespace data structure in the NVM Express NVM Command Set Specification, if applicable) indicates NGUID and EUI64 reuse characteristics.

If Asymmetric Namespace Access Reporting is supported (i.e., the Asymmetric Namespace Access Reporting Support (ANARS) bit is set to ‘1’ in the CMIC field in the Identify Controller data structure (refer to Figure 328)), refer to the applicable NVM Express I/O Command Set specification for additional detail, if any.

A namespace may or may not have a relationship to a Submission Queue; this relationship is determined by the host implementation. The controller shall support access to any attached namespace from any I/O Submission Queue.



---

### 3.2.1.7 I/O Command Set Associations

A namespace is associated with exactly one I/O Command Set. For I/O commands and I/O Command Set specific Admin commands, the I/O Command Set with which a submission queue entry is associated is determined by the Namespace Identifier (NSID) field in the command.

An NVM subsystem may contain namespaces each of which is associated with a different I/O Command Set. A controller may support attached namespaces that use any of the I/O Command Sets that the controller simultaneously supports as indicated in the I/O Command Set Profile (refer to section 5.2.26.1.17).



---

### 3.2.2 NVM Sets

An NVM Set is a collection of NVM that is separate (logically and potentially physically) from NVM in other NVM Sets. One or more namespaces that contain formatted storage may be created within an NVM Set and those namespaces inherit the attributes of the NVM Set. A namespace that contains formatted storage is wholly contained within a single NVM Set and shall not span more than one NVM Set.

Figure 67 shows an example of three NVM Sets. NVM Set A contains three namespaces (NS A1, NS A2, and NS A3). NVM Set B contains two namespaces (NS B1 and NS B2). NVM Set C contains one namespace (NS C1). Each NVM Set shown also contains 'Unallocated' regions that consist of NVM that is not yet allocated to a namespace.

<!-- Figure 67, coordinate:(115,675,885,735) -->
===== page_number= 80, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 67: NVM Sets and Associated Namespaces, coordinate:(238,88,765,475) -->
**Figure 67: NVM Sets and Associated Namespaces**

The diagram shows three NVM Sets (A, B, and C), each containing multiple namespaces or unallocated space:

- **NVM Set A** (yellow border):
  - NS A1
  - NS A2
  - NS A3
  - Unallocated

- **NVM Set B** (blue border):
  - NS B1
  - NS B2
  - Unallocated

- **NVM Set C** (green border):
  - NS C1
  - Unallocated

There is a subset of Admin commands that are NVM Set aware as described in Figure 68.

**Figure 68: NVM Set Aware Admin Commands**

| Admin Command             | Details                                                                                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Identify                  | - The Identify Namespace data structure includes the associated NVM Set Identifier.<br>- The NVM Set List data structure includes attributes for each NVM Set.                                               |
| Capacity Management       | - The Create NVM Set action returns the NVM Set Identifier of the NVM Set that is created.<br>- The Delete NVM Set action includes the NVM Set Identifier of the NVM Set that is to be deleted.             |
| Namespace Management      | - The create action includes the NVM Set Identifier as a host specified field.                                                                                                                          |
| Get Features and Set Features | - The Read Recovery Level Feature specifies the associated NVM Set Identifier.<br>- The Predictable Latency Mode Config Feature specifies the associated NVM Set Identifier.<br>- The Predictable Latency Mode Window Feature specifies the associated NVM Set Identifier. |
| Connect                   | - The Connect command includes the associated NVM Set Identifier.                                                                                                                                       |
| Create I/O Submission Queue | - The Create I/O Submission Queue command includes the associated NVM Set Identifier.                                                                                                                   |
| Get Log Page              | - The Predictable Latency Per NVM Set log page specifies the associated NVM Set Identifier.                                                                                                              |

The host determines the NVM Sets present and their attributes using the Identify command with CNS value of 04h to retrieve the NVM Set List (refer to Figure 333). For each NVM Set, the attributes include:
- an identifier associated with the NVM Set;
- the optimal size for writes to the NVM Set;
===== page_number= 81, page_type= body ====

- the total capacity of the NVM Set; and
- the unallocated capacity for the NVM Set.

An NVM Set Identifier is a 16-bit value that specifies the NVM Set with which an action is associated. An NVM Set Identifier is unique with the NVM subsystem. An NVM Set Identifier may be specified in NVM Set aware Admin commands (refer to Figure 68). An NVM Set Identifier value of 0h is reserved and is not a valid NVM Set Identifier. Unless otherwise specified, if the host specifies an NVM Set Identifier cleared to 0h for a command that requires an NVM Set Identifier, then that command shall abort with a status code of Invalid Field in Command.

Each NVM Set is associated with exactly one Endurance Group (refer to section 3.2.3).

The NVM Set with which a namespace that contains formatted storage is associated is reported in the Identify Namespace data structure (refer to the applicable NVM Express I/O Command Set specification). When a host creates a namespace that contains formatted storage using the Namespace Management command, the host specifies the NVM Set Identifier of the NVM Set that the namespace is to be created in. The namespace that is created inherits attributes from the NVM Set (e.g., the optimal write size to the NVM).

If NVM Sets are supported, then all controllers in the NVM subsystem shall:
- Indicate support for NVM Sets in the Controller Attributes field in the Identify Controller data structure;
- Support the NVM Set Identifier in all commands that use the NVM Set Identifier;
- Support the NVM Set List for the Identify command;
- Indicate the NVM Set Identifier with which any namespace that contains formatted storage is associated in the Identify Namespace data structure for that namespace;
- Support Endurance Groups; and
- For each NVM Set, indicate the associated Endurance Group as an attribute.

If support for NVM Sets is not reported (i.e., the NVM Sets bit is cleared to '0' in the CTRATT field; refer to Figure 328), then the NVM Set Identifier field shall be cleared to 0h in all commands and data structures that support an NVM Set Identifier field.



| Admin Command             | Details                                                                                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Identify                  | - The Identify Namespace data structure includes the associated NVM Set Identifier.<br>- The NVM Set List data structure includes attributes for each NVM Set.                                               |
| Capacity Management       | - The Create NVM Set action returns the NVM Set Identifier of the NVM Set that is created.<br>- The Delete NVM Set action includes the NVM Set Identifier of the NVM Set that is to be deleted.             |
| Namespace Management      | - The create action includes the NVM Set Identifier as a host specified field.                                                                                                                          |
| Get Features and Set Features | - The Read Recovery Level Feature specifies the associated NVM Set Identifier.<br>- The Predictable Latency Mode Config Feature specifies the associated NVM Set Identifier.<br>- The Predictable Latency Mode Window Feature specifies the associated NVM Set Identifier. |
| Connect                   | - The Connect command includes the associated NVM Set Identifier.                                                                                                                                       |
| Create I/O Submission Queue | - The Create I/O Submission Queue command includes the associated NVM Set Identifier.                                                                                                                   |
| Get Log Page              | - The Predictable Latency Per NVM Set log page specifies the associated NVM Set Identifier.                                                                                                              |


![Figure 67](restored_images/Figure_67.png)
**Figure 67**


---

### 3.2.3 Endurance Groups

Endurance may be managed within a single NVM Set (refer to section 3.2.2) or across a collection of NVM Sets. Each NVM Set is associated with an Endurance Group (refer to Figure 333). If two or more NVM Sets have the same Endurance Group Identifier, then endurance is managed by the NVM subsystem across that collection of NVM Sets. If only one NVM Set is associated with a specific Endurance Group Identifier, then endurance is managed locally to that NVM Set.

If NVM Sets are not supported, then endurance is managed by the NVM subsystem:
- within each Endurance Group if Endurance Groups are supported; or
- within the domain if Endurance Groups are not supported.

An Endurance Group shall be part of only one domain (refer to section 3.2.5).

An Endurance Group Identifier is a 16-bit value that specifies the Endurance Group with which an action is associated. An Endurance Group Identifier is unique within the NVM subsystem. An Endurance Group Identifier value of 0h is reserved and is not a valid Endurance Group Identifier. Unless otherwise specified, if the host specifies an Endurance Group Identifier cleared to 0h for a command that requires an Endurance Group Identifier, then that command shall abort with a status code of Invalid Field in Command.

The information that describes an Endurance Group is indicated in the Endurance Group Information log page (refer to section 5.2.12.1.10).

Figure 69 shows Endurance Groups added to the example in Figure 67. In this example, the endurance of NVM Set A and NVM Set B are managed together as part of Endurance Group Y, while the endurance of NVM Set C is managed only within NVM Set C which is the only NVM Set that is part of Endurance Group Z.

<!-- Figure 68, coordinate:(115,135,350,150) -->
<!-- Figure 328, coordinate:(115,495,200,510) -->
<!-- Figure 333, coordinate:(115,565,200,580) -->
<!-- Figure 67, coordinate:(115,845,180,860) -->
<!-- Figure 69, coordinate:(115,845,180,860) -->
===== page_number= 82, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 69: NVM Sets and Associated Namespaces, coordinate:(238,97,778,515) -->

If Endurance Groups are supported, then the NVM subsystem and all controllers shall:
- indicate support for Endurance Groups in the Controller Attributes field in the Identify Controller data structure;
- indicate the Endurance Group Identifier with which the namespace is associated in the Identify Namespace data structure;
- support the Endurance Group Information log page; and
- support the Endurance Group Event Aggregate log page if more than one Endurance Group is supported in the NVM subsystem.

If Endurance Groups are not supported and the host sends a command in which an Endurance Group Identifier field is defined (e.g., Get Log Page), then that field shall be ignored by the controller.

If Endurance Groups are not supported and the controller returns information to the host that contains an Endurance Group Identifier field, then that field shall be cleared to 0h.



![Figure 68](restored_images/Figure_68.png)
**Figure 68**
![Figure 328](restored_images/Figure_328.png)
**Figure 328**
![Figure 333](restored_images/Figure_333.png)
**Figure 333**
![Figure 67](restored_images/Figure_67.png)
**Figure 67**
![Figure 69](restored_images/Figure_69.png)
**Figure 69**


---

### 3.2.3.1 Configuring and Managing Endurance Group Events

The host may configure asynchronous events to be triggered when certain events occur for an Endurance Group. The host submits a Set Features command specifying the Endurance Group Event Configuration feature (refer to section 5.2.26.1.16), the Endurance Group, and the specific event(s) that shall trigger adding an entry to the Endurance Group Event Aggregate log page (refer to section 5.2.12.1.15).

The host configures events using a Set Features command for each Endurance Group.

The host submits a Set Features command specifying the Asynchronous Event Configuration feature (refer to section 5.2.26.1.5) with the Endurance Group Event Aggregate Log Change Notices bit set to ‘1’ to specify that adding an entry to the Endurance Group Event Aggregate log page shall trigger an Endurance Group Event Aggregate Log Page Change Notice event to the host (refer to Figure 428).
===== page_number= 83, page_type= body ====

The host determines the Endurance Groups that have outstanding events by reading the Endurance Group Event Aggregate log page. An entry is returned for each Endurance Group that has an event outstanding. The host may use the Endurance Group Identifier Maximum value reported in the Identify Controller data structure to determine the maximum size of this log page.

To determine the specific event(s) that have occurred for a reported Endurance Group, the host reads the Endurance Group Information log page (refer to Figure 222) for that Endurance Group. The Critical Warning field indicates the event(s) that have occurred (e.g., that all namespaces in the Endurance Group have been placed in read-only mode). All events for an Endurance Group are cleared if the controller successfully processes a read for the Endurance Group Information log page for that Endurance Group, where the Get Log Page command has the Retain Asynchronous Event bit cleared to '0'. If the Critical Warning field in the Endurance Group Information log page is cleared to 0h, then events for that Endurance Group are not reported in the Endurance Group Event Aggregate log page.



---

### 3.2.4 Reclaim Groups, Reclaim Unit Handles, and Reclaim Units

If Flexible Data Placement is enabled in an Endurance Group (refer to section 5.2.26.1.20), then the logical view of the non-volatile storage capacity in that Endurance Group is shown in Figure 70 and consists of:

- a set of one or more Reclaim Groups numbered from 0 to *P*-1 where *P* is the value of the Number of Reclaim Groups field in the FDP Configuration Descriptor (refer to Figure 287). A Reclaim Group consists of one or more Reclaim Units; and
- one or more Reclaim Unit Handles numbered from 0 to *N*-1 where *N* is the value of the Number of Reclaim Unit Handles field in the FDP Configuration Descriptor (refer to Figure 287).

A Reclaim Unit Handle consists of a reference to a Reclaim Unit in each Reclaim Group where user data from a write command is placed. A Reclaim Unit referenced by the Reclaim Unit Handle is only allowed to be referenced by at most one Reclaim Unit Handle. However, a specific Reclaim Unit is referenced by the same or different Reclaim Unit Handles as the Reclaim Unit is cycled from erased and back into use. When a Reclaim Unit is written to capacity, the controller updates that Reclaim Unit Handle to reference a different Reclaim Unit that is available for writing user data (e.g., non-volatile storage media that has been erased which is required prior to writing for program in place memories) and has not been written with any user data (i.e., an empty Reclaim Unit). Refer to section 8.1.11 for the details of how a host is able to issue a write command and place the user data into a Reclaim Unit.

<!-- Figure 70, coordinate:(x1,y1,x2,y2) -->  
<!-- Figure 222, coordinate:(x1,y1,x2,y2) -->  
<!-- Figure 287, coordinate:(x1,y1,x2,y2) -->
===== page_number= 84, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 70, coordinate:(158,115,842,540) -->
**Figure 70: Flexible Data Placement Logical View of Non-Volatile Storage**

**3.2.5 Domains and Divisions**

**3.2.5.1 Overview**

An NVM subsystem may be made up of a single domain or multiple domains (i.e., two or more). A domain is the smallest indivisible unit that shares state (e.g., power state, capacity information). An NVM subsystem that supports multiple domains shall support Asymmetric Namespace Access Reporting (refer to section 8.1.1).

A common example of a simple implementation of an NVM subsystem is one that consists of a single domain (i.e., multiple domains are not supported).

Each domain is independent, and the boundaries between domains are communication boundaries (e.g., fault boundaries, management boundaries). If multiple domains are present in an NVM subsystem, then those domains cooperate in the operation of that NVM subsystem. If a domain is unable to cooperate in the operation of the NVM subsystem, then the NVM subsystem has become divided.

A division is an event (e.g., failure of a domain) or action (e.g., management action or reconfiguration) within the NVM subsystem that affects communication between the domains contained in the NVM subsystem (refer to Figure 71 and Figure 72). If a division exists, global state within the NVM subsystem may be impacted (e.g., a controller may only have information about the state of the domains with which the controller is able to communicate). A division event or action may:

- affect access to namespaces (refer to section 8.1.1); or
- impact operations that have NVM subsystem scope (e.g., TNVMCAP, sanitize, format, SMART information).
===== page_number= 85, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

A domain is comprised of:
- zero or more controllers; and
- zero or more NVM Endurance Groups.

If an NVM subsystem supports multiple domains, then all controllers in that NVM subsystem shall:
- set the MDS bit to ‘1’ in the CTRATT field in the Identify Controller data structure (refer to Figure 328);
- set the Domain Identifier in each Endurance Group descriptor, if supported, to a non-zero value; and
- set the Domain Identifier in each Identify Controller data structure to a non-zero value.

If an NVM subsystem supports multiple domains, then controllers in that NVM subsystem may:
- support Endurance Groups (refer to Endurance Groups bit in the CTRATT field of Identify Controller data structure).

For an NVM subsystem that supports multiple domains, each domain shall be assigned a domain identifier that is unique within the NVM subsystem (refer to the Domain Identifier field in Figure 328 and section 3.2.5.4). For an NVM subsystem that does not support multiple domains, Domain Identifier fields are cleared to 0h.

Figure 71 shows an example of an NVM subsystem that consists of three domains. Domain 1 contains two controllers and some amount of NVM storage capacity which has been allocated to two private namespaces (i.e., NS A and NS C) and a shared namespace (i.e., NS B). Domain 2 contains two controllers and some amount of NVM storage capacity which has been allocated to two shared namespaces (i.e., NS D and NS E). Domain 3 contains one controller, and no NVM storage capacity.

**Figure 71: Example 1 Domain Structure**

<!-- Figure 71, coordinate:(115,480,925,755) -->

If, in the example shown in Figure 71, a division event occurs that results in Domain 1 no longer being able to communicate with Domain 2 and Domain 3, then the NVM subsystem would consist of two parts. The first part consists of Domain 1 and the second part consists of Domain 2 and Domain 3.

Figure 72 shows an example of an NVM subsystem that consists of six domains, of which, three are domains that contain controllers. Domain 1 is a domain that contains two controllers and some amount of NVM storage capacity from which NVM Endurance Groups have been created that contain a private namespace (i.e., NS A) and a shared namespace (i.e., NS C). Domain 2 is a domain that contains no controllers and contains some amount of NVM storage capacity from which NVM Endurance Groups have been created that contain a shared namespace (i.e., NS B). Domain 3 is a domain that contains two

85
===== page_number= 86, page_type= body ==___

controllers and no NVM storage capacity. Domain 4 is a domain that contains no controllers and contains some amount of NVM storage capacity from which NVM Endurance Groups have been created that contain two shared namespaces (i.e., NS D and NS E). Domain 5 is a domain that contains one controller and no NVM storage capacity. Domain 6 is a domain that contains no controllers and no NVM storage capacity allocated to an NVM Endurance Group (i.e., an empty domain).

**Figure 72: Example 2 Domain Structure**

<!-- Figure 72, coordinate:(115,198,975,535) -->

**Key**: `---` (Dashed Line) – Communication Boundary



![Figure 70](restored_images/Figure_70.png)
**Figure 70**
![Figure 71](restored_images/Figure_71.png)
**Figure 71**
![Figure 72](restored_images/Figure_72.png)
**Figure 72**


---

### 3.2.5.2 Domains and Reservations

If an NVM subsystem supports multiple domains and Persistent Reservations (refer to section 8.1.24), then resumption after a division event (e.g., resumption of operation, resumption of communication) requires that all persistent reservation state within the domains in the NVM subsystem that are no longer divided be synchronized (i.e., updated).

If the reservation state for a namespace is not synchronized, then the ANA Group that contains that namespace shall transition to the ANA Inaccessible state (refer to section 8.1.1.6) and remain in that state until the Persistent Reservation state is synchronized. If the Persistent Reservation state is not able to be synchronized, then:

- a transition to the ANA Persistent Loss state occurs and commands are processed as described in section 8.1.1.7; or
- the controller may stop processing commands and set the Controller Fatal Status (CSTS.CFS) bit to '1' (refer to section 9.5).



---

### 3.2.5.3 Domains and Sanitize Operations

If an NVM subsystem supports multiple domains and supports performing a sanitize operation (refer to section 8.1.26), then performing a sanitize operation is affected by division events and the existence of divisions.

If a division exists and the controller is not able to successfully perform a sanitize operation as specified in section 8.1.26 (e.g., if the division prevents access to some objects in the scope of the sanitize operation,
===== page_number= 87, page_type= body ====

refer to Figure 704) then the controller is not able to start a sanitize operation and the command requesting the sanitize operation is aborted as specified in section 8.1.26.1.

If a division event occurs during a sanitize operation, then that division event:
- may prevent successful completion of that sanitize operation as specified in section 8.1.26 (e.g., the division prevents access to some objects in the scope of the sanitize operation, refer to Figure 704, and those objects have not already been sanitized by that sanitize operation); or
- may not affect the sanitize operation (i.e., if the sanitize operation is able to be processed successfully as described in section 8.1.26).

If a division exists that impacts global state within the NVM subsystem (refer to section 3.2.5.1), then a controller may or may not be able to return valid information in a Sanitize Status log page (refer to section 5.2.12.1.36) or a Sanitize Namespace Status List log page (refer to section 5.2.12.1.34).



---

### 3.2.5.4 Domain Identifier Use (Informative)

Domain Identifier values indicate the parts of the NVM subsystem that comprise a domain.

The host may use these values to determine which Endurance Groups (refer to section 3.2.3) are contained in the same domain and which are contained in a different domain. Examples of host use of the domain identifier include:
- host data redundancy software (e.g., RAID) that may use the Endurance Group’s Domain Identifier to determine which Endurance Groups may fail together (e.g., Endurance Groups in the same domain) and which Endurance Groups may fail independently (e.g., Endurance Groups in different domains); and
- host application software may use the controller’s Domain Identifier to determine which controllers share domains (e.g., controllers that may fail together) and which controllers are a part of different domains (e.g., controllers that may fail independently).



---

### 3.3 NVM Queue Models

The NVM Express interface is based on a paired Submission and Completion Queue mechanism. Commands are placed by a host into a Submission Queue. Completions are placed into the associated Completion Queue by the controller. When using a memory-based transport queue model (refer to section 3.3.1), multiple Submission Queues may utilize the same Completion Queue. When using a message-based transport queue model (refer to section 3.3.2) each Submission Queue maps to a single Completion Queue.



---

#### 3.3.1 Memory-based Transport Queue Model (PCIe)



---

##### 3.3.1.1 Queue Setup and Initialization

To setup and initialize I/O Submission Queues and I/O Completion Queues for use, a host follows these steps:
1. Configures the Admin Submission Queue and the Admin Completion Queues by initializing the Admin Queue Attributes (AQA), Admin Submission Queue Base Address (ASQ), and Admin Completion Queue Base Address (ACQ) properties appropriately;
2. Configures the size of the I/O Submission Queues (CC.IOSQES) and I/O Completion Queues (CC.IOCQES);
3. Submits a Set Features command with the Number of Queues attribute set to the requested number of I/O Submission Queues and I/O Completion Queues. The completion queue entry for this Set Features command indicates the number of I/O Submission Queues and I/O Completion Queues allocated by the controller;
4. Determines the maximum number of entries supported per queue (CAP.MQES) and whether the queues are required to be physically contiguous (CAP.CQR);
===== page_number= 88, page_type= body ====

5. Creates I/O Completion Queues within the limitations of the number allocated by the controller and the queue attributes supported (maximum entries and physically contiguous requirements) by using the Create I/O Completion Queue command; and  
6. Creates I/O Submission Queues within the limitations of the number allocated by the controller and the queue attributes supported (maximum entries and physically contiguous requirements) by using the Create I/O Submission Queue command.

At the end of this process, I/O Submission Queues and I/O Completion Queues have been setup and initialized and may be used to complete I/O commands.



---

### 3.3.1.2 Queue Usage

The submitter of entries to a memory-based transport queue uses the current Tail entry pointer to identify the next open queue slot. The submitter increments the Tail entry pointer after placing the new entry to the open queue slot. If the Tail entry pointer increment exceeds the queue size, the Tail entry shall roll to zero. The submitter may continue to place entries in free queue slots as long as the Full queue condition is not met (refer to section 3.3.1.5).

**Note:** The submitter shall take queue wrap conditions into account.

The consumer of entries on a memory-based transport queue uses the current Head entry pointer to identify the slot containing the next entry to be consumed. The consumer increments the Head entry pointer after consuming the next entry from the queue. If the Head entry pointer increment exceeds the queue size, the Head entry pointer shall roll to zero. The consumer may continue to consume entries from the queue as long as the Empty queue condition is not met (refer to section 3.3.1.4).

**Note:** The consumer shall take queue wrap conditions into account.

Creation and deletion of memory-based transport Submission Queue and associated Completion Queues are required to be ordered correctly by a host. A host creates the Completion Queue before creating any associated Submission Queue. Submission Queues may be created at any time after the associated Completion Queue is created. A host deletes all associated Submission Queues prior to deleting a Completion Queue. To abort all commands submitted to the Submission Queue, a host issues a Delete I/O Submission Queue command for that queue (refer to section 3.3.1.3).

A host writes the Submission Queue Tail Doorbell and the Completion Queue Head Doorbell (refer to the Transport Specific Controller Properties section in the NVMe over PCIe Transport Specification) to communicate new values of the corresponding entry pointers to the controller. If a host writes an invalid value to the Submission Queue Tail Doorbell or Completion Queue Head Doorbell property and an Asynchronous Event Request command is outstanding, then an asynchronous event is posted to the Admin Completion Queue with a status code of Invalid Doorbell Write Value. The associated queue is then deleted and recreated by a host. For a Submission Queue that experiences this error, the controller may complete previously consumed commands; no additional commands are consumed. This condition may be caused by a host attempting to add an entry to a full Submission Queue or remove an entry from an empty Completion Queue.

A host checks completion queue entry Phase Tag (P) bits in memory to determine whether new completion queue entries have been posted (refer to section 4.2.4). The Completion Queue Tail pointer is only used internally by the controller and is not visible to the host. The controller uses the SQ Head Pointer (SQHD) field in completion queue entries to communicate new values of the Submission Queue Head Pointer to the host. A new SQHD value indicates that submission queue entries have been consumed, but does not indicate either execution or completion of any command. Refer to section 4.2.

A submission queue entry is submitted to the controller when the host writes the associated Submission Queue Tail Doorbell with a new value that indicates that the Submission Queue Tail Pointer has moved to or past the slot in which that submission queue entry was placed. A Submission Queue Tail Doorbell write may indicate that one or more submission queue entries have been submitted.

A submission queue entry has been consumed by the controller when a completion queue entry is posted that indicates that the Submission Queue Head Pointer has moved past the slot in which that submission

<!-- Embeded_Image 1, coordinate:(0,0,1000,999) -->
===== page_number= 89, page_type= body ====

queue entry was placed. A completion queue entry may indicate that one or more submission queue entries have been consumed.

A completion queue entry is posted to the Completion Queue when the controller write of that completion queue entry to the next free Completion Queue slot inverts the Phase Tag (P) bit from its previous value in memory (refer to section 4.2.4). The controller may generate an interrupt to the host to indicate that one or more completion queue entries have been posted.

A completion queue entry has been consumed by the host when the host writes the associated Completion Queue Head Doorbell with a new value that indicates that the Completion Queue Head Pointer has moved past the slot in which that completion queue entry was placed. A Completion Queue Head Doorbell write may indicate that one or more completion queue entries have been consumed.

Once a submission queue entry or a completion queue entry has been consumed, the slot in which it was placed is free and available for reuse. Altering a submission queue entry after an entry has been submitted but before that entry has been consumed results in undefined behavior. Altering a completion queue entry after that entry has been posted but before that entry has been consumed results in undefined behavior.



![Embeded_Image 1](restored_images/Embeded_Image_1.png)
**Embeded_Image 1**


---

### 3.3.1.2.1 Completion Queue Flow Control

If there are no free slots in a Completion Queue, then the controller shall not post status to that Completion Queue until slots become available. In this case, the controller may stop processing additional submission queue entries associated with the affected Completion Queue until slots become available. The controller shall continue processing for other Submission Queues not associated with the affected Completion Queue.



---

### 3.3.1.3 Queue Abort

To abort a large number of commands, the host may use:
- the Cancel command (refer to section 7.1); or
- delete and recreate the I/O Submission Queue (refer to section 3.7.3).

Specifically, to abort all commands that are submitted to an I/O Submission Queue, a host should:
- issue a Cancel command to that queue with the Cancel Action set to Multiple Command Cancel and the NSID field set to FFFFFFFFh; or
- issue a Delete I/O Submission Queue command for that queue. After that submission queue has been successfully deleted, indicating that all commands have been completed or aborted, then a host should recreate the queue by submitting a Create I/O Submission Queue command. A host may then re-submit commands to the associated I/O Submission Queue.

If the host is no longer able to communicate with the controller before that host receives either:
- completions for all outstanding commands submitted on that I/O Submission Queue (refer to section 3.4.5); or
- a successful completion for the Delete I/O Submission Queue command for that I/O Submission Queue,

then it is strongly recommended that the host take the steps described in section 9.6 to avoid possible data corruption caused by interaction between outstanding commands and subsequent commands submitted by that host to another controller.



---

### 3.3.1.4 Empty Queue

The queue is Empty when the Head entry pointer equals the Tail entry pointer. Figure 73 defines the Empty Queue condition.

<!-- Figure 73, coordinate:(112,790,880,820) -->
===== page_number= 90, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

<!-- Figure 73: Empty Queue Definition, coordinate:(214,112,785,337) -->
**Figure 73: Empty Queue Definition**

- Queue Base Address → points to top of stack of blue boxes labeled "empty"
- Head (Consumer) → points to the same box as Tail (Producer)
- Tail (Producer) → points to the same box as Head (Consumer)
- All boxes in the queue are labeled "empty"

---



![Figure 73](restored_images/Figure_73.png)
**Figure 73**


---

### 3.3.1.5 Full Queue

The queue is Full when the Head equals one more than the Tail. The number of entries in a queue when full is one less than the queue size. Figure 74 defines the Full Queue condition.

**Note:** Queue wrap conditions shall be taken into account when determining whether a queue is Full.

<!-- Figure 74: Full Queue Definition, coordinate:(214,458,785,683) -->
**Figure 74: Full Queue Definition**

- Queue Base Address → points to top of stack of blue boxes
- Head (Consumer) → points to a box labeled "empty"
- Tail (Producer) → points to the box immediately below the "empty" box
- The boxes are labeled: "occupied", "occupied", "empty", "occupied", "occupied", ..., "occupied", "occupied", "occupied"
- The "empty" box is the only one not occupied, and it is the one pointed to by the Head.

---



![Figure 74](restored_images/Figure_74.png)
**Figure 74**


---

### 3.3.2 Message-based Transport Queue Model (Fabrics)

For NVMe over Fabrics, a queue is a unidirectional communication channel that is used to send capsules between a host and a controller. A host uses Submission Queues to send command capsules (refer to section 3.3.2.1.1) to a controller. A controller uses Completion Queues to send response capsules (refer to section 3.3.2.1.2) to a host. Submission and Completion Queues are created in pairs using the Connect command (refer to section 3.3.2.2).

The NVMe Transport is responsible for delivering command capsules to the controller and notifying the controller of capsule arrival in a transport-specific fashion.

Altering a command capsule between host submission to the Submission Queue and transport delivery of that capsule to the controller results in undefined behavior.

---

90
===== page_number= 91, page_type= body ====

NVM Express® Base Specification, Revision 2.3

NVMe Transports are not required to provide any additional end-to-end flow control. Specific NVMe Transports may require low level flow control for congestion avoidance and reliability; any such additional NVMe Transport flow control is outside the scope of this specification.

Flow control differs for Submission Queues (refer to section 3.3.2.1.1, section 3.3.2.6, and section 3.3.2.7) and Completion Queues (refer to section 3.3.2.1.2, section 3.3.2.8, and section 3.3.1.2.1).



---

### 3.3.2.1 Capsules and Data Transfers

This section describes capsules and data transfer mechanisms necessary to support message-based transport queues. These mechanisms are used for Fabrics commands, Admin commands, and I/O commands when using the message-based transport queue model.

A capsule is an NVMe unit of information exchanged between a host and a controller. A capsule may contain commands, responses, SGLs, and/or data. The data may include user data (e.g., logical block data and metadata that is transferred as a contiguous part of the logical block) and data structures associated with the command.

The capsule size for the Admin Queue commands and responses is fixed and defined in the NVMe Transport binding specification. The controller indicates in the Identify Controller data structure the capsule command and response sizes that the host shall use with I/O commands.

The controller shall support SGL based data transfers for commands on both the Admin Queue and I/O Queues. Data may be transferred within the capsule or through memory transactions based on the underlying NVMe Transport as indicated in the SGL descriptors associated with the command capsule. The SGL types supported by an NVMe Transport are specified in the NVMe Transport binding specification.

The value of unused and not reserved capsule fields (e.g., the capsule is larger than the command / response and associated data) is undefined and shall not be interpreted by the recipient.



---

#### 3.3.2.1.1 Command Capsules

A command capsule is sent from a host to a controller. It contains a submission queue entry (SQE) and may optionally contain data or SGLs. The SQE is 64 bytes in size and contains the Admin command, I/O command, or Fabrics command to be executed.

**Figure 75: Command Capsule**

<!-- Figure 75, coordinate:(125,580,835,695) -->

The Command Identifier field in the SQE shall be unique among all outstanding commands associated with that queue. If there is data or additional SGLs to be transferred within the capsule, then the SGL descriptor in the SQE contains a Data Block, Segment Descriptor, or Last Segment Descriptor specifying an appropriate Offset address. The definition for the submission queue entry when the command is a Fabrics command is shown in section 4.1.2. The definition for the submission queue entry when the command is an Admin command or I/O command is shown in section 4.1.1. Bytes 03:00 share a common format across commands.



![Figure 75](restored_images/Figure_75.png)
**Figure 75**


---

#### 3.3.2.1.2 Response Capsules

A response capsule is sent from the NVM subsystem to the host. It contains a completion queue entry (CQE) and may optionally contain data. The CQE is the completion queue entry associated with a previously issued command capsule.
===== page_number= 92, page_type= body ==___

If a command requests data and the SGL in the associated command capsule specifies a Data Block descriptor with an Offset, the data is included in the response capsule. If the SGL(s) in the command capsule specify a region in host memory, then data is transferred via memory transactions.

<!-- Figure 76: Response Capsule, coordinate:(144,147,855,288) -->

The completion queue entry is 16 bytes in size and contains a two byte status field.

The definition for the completion queue entry for a Fabrics command is shown in section 4.2.2. The definition for the completion queue entry when the command is an Admin command or I/O command is defined in section 4.2.1, where the SQ Identifier and Phase Tag fields are reserved because they are not used in NVMe over Fabrics. Use of the SQHD field depends on whether SQ flow control is disabled for the queue pair, refer to Section 6.3.



![Figure 76](restored_images/Figure_76.png)
**Figure 76**


---

### 3.3.2.1.3 Data Transfers

Data may be transferred within capsules or by memory transfers. SGLs are used to specify the location of data. Metadata, if transferred, is a contiguous part of the user data with which that metadata is associated. The SGL descriptor(s) (refer to section 4.3.2) specify whether the command’s data is transferred through memory or within the capsule. The capsule may contain either SGLs or data (not a mixture of both) following the SQE. If additional SGLs are required, then the SGLs are included in the capsule immediately after the SQE. If an invalid offset is specified in an SGL descriptor, then a status code of SGL Offset Invalid shall be returned.

SGLs shall be supported within a capsule. The NVMe Transport binding specification defines the SGL Descriptor Types and Sub Types that are supported for the corresponding NVMe Transport. The NVMe Transport binding specification also specifies if SGLs may be supported in host memory.



---

### 3.3.2.1.3.1 Data and SGL Locations within a Command Capsule

The submission queue entry within the command capsule includes one SGL entry. If there are additional SGL entries to be transferred in the command capsule, then those entries shall be contiguous and located immediately after the submission queue entry.

An NVMe Transport binding specification defines the support for data as part of the command capsule. The controller indicates the starting location of data within a command capsule via the In Capsule Data Offset (ICDOFF) field in the Identify Controller data structure.

There are restrictions for SGLs that the host should follow:

- if the ICDOFF field is a non-zero value, then all SGL descriptors following the submission queue entry shall not have a total size greater than (ICDOFF * 16);
- if the SGL descriptors following the submission queue entry have a total size greater than (ICDOFF * 16), then the controller shall abort the command with a status code of Invalid Number of SGL Descriptors;
- the host shall not place more SGL Data Block or Keyed SGL Data Block descriptors within a capsule than the maximum indicated in the Identify Controller data structure; and
- if the host places more SGL Data Block of Keyed SGL Data Block descriptors in a capsule than the maximum indicated in the Maximum SGL Data Block Descriptors field in the Identify Controller data structure, then the controller shall abort the command with a status code of Invalid Number of SGL Descriptors.
===== page_number= 93, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

The host shall start data (if present) in command capsules at byte offset (ICDOFF * 16) from the end of the submission queue entry.

**Figure 77: Data and SGL Locations within a Command Capsule**

<!-- Figure 77, coordinate:(120,135,950,485) -->

**3.3.2.1.3.2 Data Transfer Examples**

The data transfer examples in Figure 78 and Figure 79 show SGL examples for a Write command where data is transferred via a memory transaction or within the capsule. The SGL may use a key as part of the data transfer depending on the requirements of the NVMe Transport used.

The first example shows an 8KiB write where all of the data is transferred via memory transactions. In this case, there is one SGL descriptor that is contained within the submission queue entry at CMD.SGL1. The SGL descriptor is a Keyed SGL Data Block descriptor. If more SGLs are required to complete the command, the additional SGLs are contained in the command capsule.
===== page_number= 94, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 78: SGL Example Using Memory Transactions, coordinate:(288,112,838,378) -->
**Figure 78: SGL Example Using Memory Transactions**

- **Host DRAM**
  - Contains **Data Block A** (blue rectangle)

- **SGL Descriptor** (gray box)
  - **Address = Data Block A** (blue)
  - **Key = Tag A** (orange)
  - **Length = 8KiB** (green)
  - **SGL Identifier = 40h** (yellow)

- **Keyed Data Block descriptor** specifies to transfer 8KiB through memory.

*Text below figure:*
> The second example shows an 8KiB write where all of the data is transferred within the capsule. In this case, the SGL descriptor is an SGL Data Block descriptor specifying an Offset of 20h based on an ICDOFF value of 2h.

<!-- Figure 79: SGL Example Using In Capsule Data Transfer, coordinate:(180,440,860,728) -->
**Figure 79: SGL Example Using In Capsule Data Transfer**

- **Capsule Layout** (horizontal bar)
  - **Byte 0 – 63**: Submission Queue Entry (blue)
  - **Byte 64 – 95**: Undefined (gray)
  - **Byte 96 – (N-1)**: Data (dark blue)
    - Contains **Data Block A** (light blue rectangle)

- **Destination SGL Segment 0** (gray box)
  - **Offset = 20h** (blue)
  - **Length = 8KiB** (green)
  - **SGL Identifier = 01h** (yellow)

- **SGL Data Block descriptor** specifies to transfer 8KiB within the capsule at offset 20h.

---



![Figure 77](restored_images/Figure_77.png)
**Figure 77**
![Figure 78](restored_images/Figure_78.png)
**Figure 78**
![Figure 79](restored_images/Figure_79.png)
**Figure 79**


---

### 3.3.2.2 Queue Creation

Message-based controllers use the Connect command (refer to section 6.3) to create Admin Queues or I/O Queues. The creation of an Admin Queue establishes an association between a host and the corresponding controller. The message-based transport queue model does not support the Admin Submission Queue Base Address (ASQ), Admin Completion Queue Base Address (ACQ), and Admin Queue Attributes (AQA) properties as all information necessary to establish an Admin Queue is contained in the Connect command. The message-based transport queue does not support the Admin commands associated with I/O Queue creation and deletion (i.e., Create I/O Completion Queue, Create I/O Submission Queue, Delete I/O Completion Queue, Delete I/O Submission Queue).
===== page_number= 95, page_type= body ====

An NVMe Transport connection is established between a host and an NVMe subsystem prior to the transfer of any capsules or data. The mechanism used to establish an NVMe Transport connection is NVMe Transport specific and defined by the corresponding NVMe Transport binding specification. The NVMe Transport may require a separate NVMe Transport connection for each Admin Queue or I/O Queue or may utilize the same NVMe Transport connection for all Admin and I/O Queues associated with a particular controller. An NVMe Transport may also require that NVMe layer information be passed between the host and controller in the process of establishing an NVMe Transport connection (e.g., exchange queue size to appropriately size send and receive buffers).

The Connect command specifies the Queue ID and type (Admin or I/O), the size of the Submission and Completion Queues, queue attributes, Host NQN, NVM Subsystem NQN, and Host Identifier. The Connect command may specify a particular controller if the NVM subsystem supports a static controller model. The Connect response indicates whether the connection was successfully established as well as whether NVMe in-band authentication is required.

The Connect command is submitted to the same Admin Queue or I/O Queue that the Connect command creates. The underlying NVMe Transport connection that is used for that queue is created first and the Connect command and response capsules are sent over that NVMe Transport connection. The Connect command shall be sent once to a queue.

When a Connect command successfully completes, the corresponding Submission and Completion Queues are created. If NVMe in-band authentication is required as indicated in the Connect response, then NVMe in-band authentication shall be performed before the queues may be used to perform other Fabrics commands, Admin commands, or I/O commands.

Once a Connect command for an Admin Queue has completed successfully (and NVMe in-band authentication, if required, has succeeded), only Fabrics commands may be submitted until the controller is ready (CSTS.RDY = 1). Both Fabrics commands and Admin commands may be submitted to the Admin Queue while the controller is ready. A Connect command for an I/O Queue may be submitted after the controller is ready. Once a Connect command for an I/O Queue has completed successfully (and NVMe in-band authentication, if required, has succeeded), I/O commands may be submitted to the queue.

The Connect response contains the controller ID allocated to the host.

After an Admin Queue is created on a controller, all subsequent Connect commands sent from the same host to that controller, to create an I/O Queue, are required to:
- utilize the same NVMe Transport;
- have the same Host NQN;
- have the same NVM Subsystem NQN; and
- either have the:
  - same Host Identifier value; or
  - a Host Identifier value of 0h, if supported (refer to section 5.2.12.3.3).



---

### 3.3.2.3 Queue Initialization and Queue State

When a Connect command successfully completes, the corresponding Admin Submission and Completion Queue or I/O Submission and Completion Queues are created. If the host sends a Connect command specifying the Queue ID of a queue which already exists, then the controller shall abort the command with a status code of Command Sequence Error.

The Authentication Requirements (AUTHREQ) field in the Connect response indicates if NVMe in-band authentication is required. If AUTHREQ is cleared to 0h, the created queue is ready for use after the Connect command completes successfully. If AUTHREQ is set to a non-zero value, the created queue is ready for use after NVMe in-band authentication has been performed successfully using the Authentication Send and Authentication Receive Fabrics commands.

If a controller requires or is undergoing NVMe in-band authentication for a queue pair, then a controller shall abort all commands received on that queue other than authentication commands with a status code of Authentication Required. After the NVMe in-band authentication has been performed successfully on a
===== page_number= 96, page_type= body ====

queue, then a controller shall abort all authentication commands on that queue with a status code of Command Sequence Error.

When an Admin Queue is first created, the associated controller is disabled (i.e., CC.EN is initialized to '0'). A disabled controller shall abort all commands other than Fabrics commands on the Admin Queue with a status code of Command Sequence Error. While a controller is enabled, that controller shall accept all supported Admin commands in addition to Fabrics commands.

A created I/O queue shall abort all commands with a status code of Command Sequence Error if the associated controller is disabled.



---

### 3.3.2.4 I/O Queue Deletion

NVMe over Fabrics deletes an individual I/O Queue and may delete the associated NVMe Transport connection as a result of:

- the exchange of a Disconnect command and response (refer to section 6.4) between a host and controller; or
- the detection and processing of a transport error on an NVMe Transport connection.

The host indicates support for the deletion of an individual I/O Queue by setting the Individual I/O Queue Deletion Support (INDIVIOQDELS) bit to '1' in the CATTR field in the Connect command (refer to Figure 579) used to create the Admin Queue. The controller indicates support for the deletion of an individual I/O Queue by setting the Disconnect Command Support (DCS) bit to '1' in the OFCS field of the Identify Controller data structure (refer to Figure 328).

If both the host and the controller support deletion of an individual I/O Queue, then the termination of an individual I/O Queue impacts only that I/O Queue (i.e., the association and all other I/O Queues and their associated NVMe Transport connections are not impacted). If either the host or the controller does not support deletion of an individual I/O Queue, then the deletion of an individual I/O Queue or the termination of an NVMe Transport connection causes the association to be terminated.

NVMe over Fabrics uses the Disconnect command to delete an Individual I/O Queue. This command is sent on the I/O Submission Queue to be deleted and affects only that I/O Submission Queue and its associated I/O Completion Queue (i.e., other I/O Queues are not affected). To delete an I/O Queue, the NVMe Transport connection for that I/O Queue is used. If all Queues associated with an NVMe Transport connection are deleted, then the NVMe Transport connection may be deleted after completion of the Disconnect command. Actions necessary to delete the NVMe Transport connection are transport specific. The association between the host and the controller is not affected.

If a Disconnect command returns a status code other than success, the host may delete an I/O Queue using other methods including:

- waiting a vendor specific amount of time and retry the Disconnect command;
- deleting the NVMe Transport connection (note: this may impact other I/O Queues);
- performing a Controller Level Reset (note: this impacts other I/O Queues); or
- ending the host to controller association.

If the transport requires a separate NVMe Transport connection for each Admin and I/O Queue (refer to section 3.3.2.2), then the host should not delete an NVMe Transport connection until after:

- a Disconnect command has been submitted to the I/O Submission Queue; and
- the response for that Disconnect command has been received by the host on the corresponding I/O Completion Queue or a vendor specific timeout (refer to section 3.9) has occurred while waiting for that response.

If the transport requires a separate NVMe Transport connection for each Admin and I/O Queue, then the controller should not delete an NVMe Transport connection until after:

- a Disconnect command has been received on the I/O Submission Queue and processed by the controller;
===== page_number= 97, page_type= body ====

- the responses for commands received by the controller on that I/O Submission Queue prior to receiving the Disconnect command have been sent to the host on the corresponding I/O Completion Queue; and
- the resulting response for that Disconnect command has been sent to the host on the corresponding I/O Completion queue (i.e., this response is the last response sent). It is recommended that the controller delay destroying the NVMe Transport connection to allow time for the Disconnect command response to be received by the host (e.g., a transport specific event occurs or a transport specific time period elapses).

If the transport utilizes the same NVMe Transport connection for all Admin and I/O Queues associated with a particular controller (refer to section 3.3.2.2), then the deletion of an individual I/O Queue has no impact on the NVMe Transport connection.

A Disconnect command is the last I/O Submission Queue entry processed by the controller for an I/O Queue. Controller processing of the Disconnect command completes or aborts all commands on the I/O Queue on which the Disconnect command was received. The controller determines whether to complete or abort each of those commands. Until the controller sends a successful completion for a Disconnect command, outstanding commands may continue being processed by the controller. The controller ensures that there is no further processing of any command sent on that I/O Queue after posting the completion queue entry for the Disconnect command as described in section 6.4.

The response to the Disconnect command is the last I/O Completion Queue entry processed by the host for an I/O Queue. To avoid command aborts, the host should wait for all outstanding commands on an I/O Queue to complete before sending the Disconnect command.

If the controller terminates an NVMe Transport connection or detects an NVMe Transport connection loss, then the controller shall stop processing all commands received on I/O Queues associated with that NVMe Transport connection within the time reported in the CQT field (refer to Figure 328), if non-zero.

If the host terminates an NVMe Transport connection or detects an NVMe Transport connection loss before the responses are received for all outstanding commands submitted to the associated I/O Queue (refer to section 3.4.5), then it is strongly recommended that the host take the steps described in section 9.6 to avoid possible data corruption caused by interaction between outstanding commands and subsequent commands submitted by that host to another controller.



---

### 3.3.2.5 Submission Queue Flow Control Negotiation

Use of Submission Queue (SQ) flow control is negotiated for each queue pair by the Connect command and the controller response to the Connect command. SQ flow control shall be used unless it is disabled as a result of that negotiation. If SQ flow control is disabled, then the Submission Queue Head Pointer (SQHD) field is reserved in all Fabrics response capsules for that queue pair after the response to the Connect command (i.e., in all subsequent response capsules for that queue pair, the controller shall clear the SQHD field to 0h and the host should ignore the SQHD field).

If the host requests that SQ flow control be disabled for a queue pair, then the host should size each Submission Queue to support the maximum number of commands that the host could have outstanding at one time for that Submission Queue.

The maximum size of the Admin Submission Queue is specified in the Admin Max SQ Size (ASQSZ) field of the Discovery Log Page Entry for the NVM subsystem (refer to section 5.2.12.3.3).

The maximum size of an I/O Submission Queue is specified in the Maximum Queue Entries Supported (MQES) field of the Controller Capabilities (CAP) property for the controller (refer to section 3.1.4.1).

The value of the Maximum Outstanding Commands (MAXCMD) field in the Identify Controller data structure indicates the maximum number of commands that the controller processes at one time for a particular I/O Queue. The host may use this value to size I/O Submission Queues and optimize the number of commands submitted at one time per queue to achieve the best performance.

If SQ flow control is disabled, then the host should limit the number of outstanding commands for a queue pair to be less than the size of the Submission Queue. If the controller detects that the number of
===== page_number= 98, page_type= body ====

outstanding commands for a queue pair is greater than or equal to the size of the Submission Queue, then the controller shall:

a) stop processing commands and set the Controller Fatal Status (CSTS.CFS) bit to ‘1’ (refer to section 9.5); and  
b) terminate the NVMe Transport connection and end the association between the host and the controller.



---

### 3.3.2.6 Submission Queue Flow Control

This section applies only to Submission Queues that use SQ flow control.

The Submission Queue has a Head entry pointer and a Tail entry pointer that are used to manage the queue and determine the number of Submission Queue capsules available to the host for new submissions. The Head and Tail entry pointers are initialized to 0h when a queue is created. All arithmetic operations and comparisons on entry pointers are performed modulo the queue size with queue wrap conditions taken into account. The host increments the Tail entry pointer when the host adds a capsule to a queue. The controller increments the Head entry pointer when that controller removes a capsule from the queue.

The Submission Queue Head entry pointer is maintained by the controller and is communicated to the host in the SQHD field of completion queue entries. The host uses the received SQHD values for Submission Queue management (e.g., to determine whether the Submission Queue is full).

The Submission Queue Tail entry pointer is local to the host and is not communicated to the controller.

The Submission Queue is full when the Head entry pointer equals one more than the Tail entry pointer (i.e., incrementing the Tail entry pointer has caused it to wrap around to just behind the Head entry pointer). A full Submission Queue contains one less capsule than the queue size. A host may continue to submit commands to a Submission Queue as long as the queue is not full.

If the controller detects that the host has submitted a command capsule to a full Submission Queue, then the controller shall:

a) stop processing commands and set the Controller Fatal Status (CSTS.CFS) bit to ‘1’ (refer to section 9.5); and  
b) terminate the NVMe Transport connection and end the association between the host and the controller.

The Submission Queue is empty when the Head entry pointer equals the Tail entry pointer.



---

### 3.3.2.7 Submission Queue Head Pointer Update Optimization

Submission Queue Head Pointer update optimization does not apply to queue pairs for which Submission Queue (SQ) flow control is disabled, as the SQHD field is reserved if SQ flow control is disabled, refer to section 3.3.2.5 and to section 6.3.

The NVMe Transport may omit transmission of the SQHD value for a response capsule that:

a) contains a Generic Command status (i.e., Status Code Type 0h) indicating successful completion of a command (i.e., Status Code 00h);  
b) is not a Connect response capsule; and  
c) is not a Disconnect response capsule.

If a new SQHD value is not received in a response capsule, the host continues to use its previous SQHD value. Thus, at the NVMe layer there is a logical progression of SQHD values despite the fact that the NVMe Transport may not actually transfer the SQHD value in each response capsule.

The NVMe Transport may deliver response capsules that do not contain an SQHD value to the host in any order. The applicable NVMe Transport binding specification defines how presence versus absence of an SQHD value in a response capsule is indicated by the NVMe Transport.

Periodic SQHD updates at the host are required to avoid Submission Queue (SQ) starvation as SQHD value transmission in responses is the only means of releasing SQ slots for host reuse.
===== page_number= 99, page_type= body ====

An NVMe Transport may transmit an SQHD value in every response capsule. If an NVMe Transport does not transmit an SQHD value in every response capsule, then an SQHD value should be transmitted periodically (e.g., in at least one of every n response capsules on a CQ, where n is 10% of the size of the associated SQ) or more often. An SQHD value should always be transmitted if 90% or more of the slots in the associated SQ are occupied at the subsystem.



---

### 3.3.2.8 Completion Queue Considerations

Completion Queue flow control (refer to section 3.3.1.2.1) is not used in the message-based transport queue model. Message-based transport Completion Queues do not use either Head entry pointers or Tail entry pointers.

The host should size each Completion Queue to support the maximum number of commands that the host could have outstanding at one time for a particular Submission Queue. The Completion Queue size may be larger than the size of the corresponding Submission Queue to accommodate responses for commands that are being processed by the controller in addition to responses for commands that are still in the Submission Queue.

If the size of a Completion Queue is too small for the number of outstanding commands and the controller submits a response capsule to a full Completion Queue, then the results are undefined.

The value of the Maximum Outstanding Commands (MAXCMD) field in the Identify Controller data structure indicates the maximum number of commands that the controller processes at one time for a particular I/O Queue. The host may use this value to size I/O Completion Queues and optimize the number of commands submitted at one time per queue to achieve the best performance.

Altering a response capsule between controller submission to the Completion Queue and transport delivery of that capsule to the host results in undefined behavior.



---

### 3.3.2.9 Transport Requirements

This section defines requirements that all NVMe Transports that support an NVMe over Fabrics implementation shall meet.

The NVMe Transport may support NVMe Transport error detection and report errors to the NVMe layer in command status values. The controller may record NVMe Transport specific errors in the Error Information log page (refer to section 5.2.12.1.2). Transport errors that cause loss of a message or loss of data in a way that the low-level NVMe Transport cannot replay or recover should cause:

- the deletion of the individual I/O Queues (refer to section 3.3.2.4) and the associated NVMe Transport connection on which that NVMe Transport level error occurred; or
- termination of the NVMe Transport connection and the association between the host and controller.

The NVMe Transport shall provide reliable delivery of capsules between a host and NVM subsystem (and allocated controller) over each connection. The NVMe Transport may deliver command capsules in any order on each queue except for I/O commands that are part of fused operations (refer to section 3.4.2).

For command capsules that are part of fused operations for I/O commands, the NVMe Transport:

1. shall deliver the first and second command capsules for each fused operation to the queue in-order; and
2. shall not deliver any other command capsule for the same Submission Queue between delivery of the two command capsules for a fused operation.

The NVMe Transport shall provide reliable delivery of response capsules from an NVMe subsystem to a host over each connection. The NVMe Transport shall deliver response capsules that include an SQ Head Pointer (SQHD) value to the host in-order; this includes all Connect response capsules and all Disconnect response capsules.
===== page_number= 100, page_type= body ====



---

# 3.3.3 Queueing Attributes



---

## 3.3.3.1 Queue Size

The queue size is the number of slots in the queue. The minimum size for a queue is two slots. The maximum size for either an I/O Submission Queue or an I/O Completion Queue is defined as 65,536 slots, limited by the maximum queue size supported by the controller that is reported in the CAP.MQES field. The maximum size for the Admin Submission Queue and Admin Completion Queue is defined as 4,096 slots. One slot in each queue is not available for use due to Head and Tail entry pointer definition.

For Message-based controllers, the maximum size for the Admin Submission Queue is limited by the value indicated in the ASQSZ field in the Discovery Log Page Entry data structure (refer to Figure 310).



---

## 3.3.3.2 Queue Identifier

Each queue is identified through a 16-bit ID value that is assigned to the queue when it is created. Both I/O Submission Queue identifiers and I/O Completion Queue identifiers are a value from 1 to 65,535.



---

## 3.3.3.3 Queue Priority

If the weighted round robin with urgent priority class arbitration mechanism is supported, then a host may assign a queue priority service class of Urgent, High, Medium, or Low. If the weighted round robin with urgent priority class arbitration mechanism is not supported, then the priority setting is not used and is ignored by the controller.



---

## 3.3.3.4 Queue Coordination

There is one Admin Queue pair associated with multiple I/O queue pairs. The Admin Submission Queue and Completion Queue are used to carry out functions that impact the entire controller. An I/O Submission Queue and Completion Queue may be used to carry out I/O (read/write) operations and may be distributed across CPU cores and threads.

An Admin command may impact one or more I/O queue pairs. The host should ensure that Admin actions are coordinated with threads that are responsible for the I/O queue pairs to avoid unnecessary error conditions. The details of this coordination are outside the scope of this specification.



---

# 3.4 Command Processing

This section describes the command issue and completion mechanism. It also describes how commands are built by a host and command completion processing.

Commands shall only be submitted by the host when the controller is ready as indicated in the Controller Status property (CSTS.RDY) and after appropriate I/O Submission Queue(s) and I/O Completion Queue(s) have been created.



---

## 3.4.1 Command Ordering Requirements

Commands which are not part of a fused operation (refer to section 3.4.2) and which comply with atomic operations requirements (refer to section 3.4.3), are processed as independent entities without reference to other commands submitted to the same I/O Submission Queue or to commands submitted to other I/O Submission Queues. For example, the controller is not responsible for checking the LBA of an NVM Command Set Read command or Write command to ensure any type of ordering between commands. If a Read command is submitted for LBA x and there is a Write command also submitted for LBA x, there is no guarantee of the order of completion for those commands (the Read command may finish first or the Write command may finish first). If there are ordering requirements between these commands, a host or the associated application is required to enforce that ordering above the level of the controller.
===== page_number= 101, page_type= body ====

# NVM Express® Base Specification, Revision 2.3



---

## 3.4.2 Fused Operations

Fused operations enable a more complex command by “fusing” together two simpler commands. This feature is optional; support for this feature is indicated in the FUSES field in the Identify Controller data structure in Figure 328.

Whether a command is part of a fused operation is specified by the Fused Operation (FUSE) field of Command Dword 0 shown in Figure 91. The FUSE field also specifies whether the command is the first command in the fused operation or the second command in the fused operation. If the FUSE field is set to a non-zero value and the controller does not support the requested fused operation, then the controller should abort the command with a status code of Invalid Field in Command.

In a fused operation, the requirements are:

- The commands shall be executed in sequence as an atomic unit. The controller shall behave as if no other operations have been executed between these two commands;
- The operation ends at the point an error is encountered in either command. If the first command in the sequence failed, then the second command in the sequence shall be aborted. If the second command in the sequence failed, then the completion status of the first command is sequence specific and is defined within the Fused Operation section of the applicable NVM Express I/O Command Set specification;
- The commands shall be inserted next to each other in the same Submission Queue. If the controller processes a command violating this condition (e.g., a command with the FUSE field cleared to 00b (i.e., Normal operation) is inserted immediately after a command specifying the FUSE field set to 01b (i.e., Fused operation, first command), or is inserted immediately before a command specifying the FUSE field set to 10b (i.e., Fused operation, second command)), then the controller shall abort the command specifying non-zero values of the FUSE field with a status code of Command Aborted due to Missing Fused Command. If the first command is in the last slot in the Submission Queue, then the second command shall be in the first slot in the Submission Queue as part of wrapping around. In the memory-based transport queue model, the Submission Queue Tail doorbell pointer update shall indicate both commands as part of one doorbell update. In the message-based transport queue model, the command capsules shall be submitted in-order;
- To abort the fused operation, the host submits an Abort command separately for each of the commands; and
- A completion queue entry is posted by the controller for each of the commands.

Refer to each NVM Express I/O Command Set specification for applicability and additional details, if any.



---

## 3.4.3 Atomic Operations

The definition for atomic operations is command set specific. Refer to each NVM Express I/O Command Set specification for applicability and additional details, if any.



---

## 3.4.4 Command Arbitration

After a command has been submitted to the controller (refer to section 1.5.19), the controller transfers submitted commands into the controller for subsequent processing using a vendor specific algorithm.

A command is being processed when the controller and/or namespace state is being accessed or modified by the command such as:

- a Feature setting is being accessed;
- a Feature setting is being modified;
- user data (e.g., a logical block as defined by the NVM Express NVM Command Set Specification) is being accessed; or
- user data is being modified.

A command is completed when a completion queue entry for the command has been posted to the corresponding Completion Queue. Upon completion, all controller state and/or namespace state modifications made by that command are globally visible to all subsequently submitted commands.
===== page_number= 102, page_type= body ====

A candidate command is a submitted command which has been transferred into the controller that the controller deems ready for processing. The controller selects command(s) for processing from the pool of submitted commands for each Submission Queue. The commands that comprise a fused operation shall be processed together and in order by the controller. The controller may select candidate commands for processing in any order. The order in which commands are selected for processing does not imply the order in which commands are completed.

Arbitration is the method used to determine the Submission Queue from which the controller starts processing the next candidate command(s). Once a Submission Queue is selected using arbitration, the Arbitration Burst setting determines the maximum number of commands that the controller may start processing from that Submission Queue before arbitration shall again take place. A fused operation may be considered as one or two commands by the controller.

All controllers shall support the round robin command arbitration mechanism. A controller may optionally implement weighted round robin with urgent priority class and/or a vendor specific arbitration mechanism. The Arbitration Mechanism Supported field in the Controller Capabilities property (CC.AMS) indicates optional arbitration mechanisms supported by the controller.

In order to make efficient use of the non-volatile memory, it is often advantageous to execute multiple commands from a Submission Queue in parallel. For Submission Queues that are using weighted round robin with urgent priority class or round robin arbitration, a host may configure an Arbitration Burst setting. The Arbitration Burst setting indicates the maximum number of commands that the controller may launch at one time from a particular Submission Queue. It is recommended that a host configure the Arbitration Burst setting as close to the recommended value by the controller as possible (specified in the Recommended Arbitration Burst field of the Identify Controller data structure in Figure 328), taking into consideration any latency requirements. Refer to section 5.2.26.1.1.



---

### 3.4.4.1 Round Robin Arbitration

If the round robin arbitration mechanism is selected, the controller shall implement round robin command arbitration amongst all Submission Queues, including the Admin Submission Queue. In this case, all Submission Queues are treated with equal priority. The controller may select multiple candidate commands for processing from each Submission Queue per round based on the Arbitration Burst setting.

**Figure 80: Round Robin Arbitration**

<!-- Figure 80, coordinate:(275,557,715,733) -->



![Figure 80](restored_images/Figure_80.png)
**Figure 80**


---

### 3.4.4.2 Weighted Round Robin with Urgent Priority Class Arbitration

In this arbitration mechanism, there are three strict priority classes and three weighted round robin priority levels. If Submission Queue A is of higher strict priority than Submission Queue B, then all candidate commands in Submission Queue A shall start processing before candidate commands from Submission Queue B start processing.

The highest strict priority class is the Admin class that includes any command submitted to the Admin Submission Queue. This class has the highest strict priority above commands submitted to any other Submission Queue.
===== page_number= 103, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

The next highest strict priority class is the Urgent class. Any I/O Submission Queue assigned to the Urgent priority class is serviced next after commands submitted to the Admin Submission Queue, and before any commands submitted to a weighted round robin priority level. A host should use care in assigning any I/O Submission Queue to the Urgent priority class since there is the potential to starve I/O Submission Queues in the weighted round robin priority levels as there is no fairness protocol between I/O Submission Queues that are Urgent priority class and I/O Submission Queues that are not Urgent priority class.

The lowest strict priority class is the Weighted Round Robin class. This class consists of the three weighted round robin priority levels (High, Medium, and Low) that share the remaining bandwidth using weighted round robin arbitration. A host controls the weights for the High, Medium, and Low service classes via the Set Features command. Round robin is used to arbitrate within multiple Submission Queues assigned to the same weighted round robin priority level. The number of candidate commands that may start processing from each Submission Queue per round is either the Arbitration Burst setting or the remaining weighted round robin credits, whichever is smaller.

**Figure 81: Weighted Round Robin with Urgent Priority Class Arbitration**

<!-- Figure 81, coordinate:(118,310,918,775) -->

In Figure 81, the Priority decision point selects the highest priority candidate command selected next to start processing.

**3.4.4.3 Vendor Specific Arbitration**

A vendor may choose to implement a vendor specific arbitration mechanism. The mechanism(s) are outside the scope of this specification.
===== page_number= 104, page_type= body ==___



![Figure 81](restored_images/Figure_81.png)
**Figure 81**


---

# 3.4.5 Outstanding Commands

A command is outstanding if:
- the host has submitted that command to the controller;
- the host has not received a completion for that command; and
- as described in this section:
  - the host has not performed an action that causes that command to no longer be outstanding; and
  - the host has not otherwise determined that that command is no longer outstanding.

A submitted command is no longer outstanding after the host:
- receives a completion for that command;
- receives a successful completion with Immediate Abort Not Performed bit cleared to ‘0’ in Dword 0 of the completion queue entry for an Abort command specifying that outstanding command (refer to section 5.2.1);
- receives a successful completion with the Commands Aborted field set to 1h for a Cancel command with an Action Code of Single Command Cancel and specifying that outstanding command (refer to section 7.1);
- reads a CSTS.RDY bit value that indicates a controller is not able to process commands except for Fabrics commands (i.e., a value of ‘0’), if that outstanding command is not a Fabrics command (refer to section 3.7.2);
- reads a CSTS.SHST field value that indicates that the controller shutdown is complete (i.e., a value of 10b), if that outstanding command is not a Fabrics command (refer to section 3.6.1 for memory-based transports and section 3.6.2 for message-based transports);
- if using a memory-based transport, receives a successful completion for a Delete I/O Submission Queue command if that outstanding command was sent on the deleted I/O Submission queue (refer to section 3.3.1.3); and
- if using a message-based transport:
  - receives a successful completion for a Disconnect command if that outstanding command was sent on the same I/O queue as the Disconnect command (refer to section 3.3.2.4); or
  - restores communication to the same controller after losing communication to that controller (refer to section 3.9.5).

If an outstanding command ceases to be outstanding for one of these reasons, then further controller processing of that command is no longer possible.



---

# 3.5 Controller Initialization

This section describes the recommended procedure for initializing a controller.



---

## 3.5.1 Memory-based Controller Initialization (PCIe)

Upon completion of the transport-specific controller initialization steps defined within the relevant NVMe Transport binding specification, the host should perform the following sequence of actions to initialize the controller to begin executing commands:

1. The host waits for the controller to indicate that any previous reset is complete by waiting for CSTS.RDY to become ‘0’;
2. The host configures the Admin Queue by setting the Admin Queue Attributes (AQA), Admin Submission Queue Base Address (ASQ), and Admin Completion Queue Base Address (ACQ) to appropriate values;
3. The host determines the supported I/O Command Sets by checking the state of CAP.CSS and appropriately initializing CC.CSS as follows:
   a. If the CAP.CSS.NOIOCSS bit is set to ‘1’, then the CC.CSS field should be set to 111b;
   b. If the CAP.CSS.IOCSS bit is set to ‘1’, then the CC.CSS field should be set to 110b; and

<!-- Embeded_Image 1, coordinate:(0,0,1000,999) -->
===== page_number= 105, page_type= body ====

c. If the CAP.CSS.IOCSS bit is cleared to ‘0’ and the CAP.CSS.NCSS bit is set to ‘1’, then the CC.CSS field should be set to 000b;

4. The controller settings should be configured. Specifically:
a. The arbitration mechanism should be selected in CC.AMS; and
b. The memory page size should be initialized in CC.MPS;

5. The host enables the controller by setting CC.EN to ‘1’;

6. The host waits for the controller to indicate that the controller is ready to process commands. The controller is ready to process commands when CSTS.RDY is set to ‘1’;

7. The host determines the configuration of the controller by issuing the Identify command specifying the Identify Controller data structure (i.e., CNS 01h);

8. The host determines any I/O Command Set specific configuration information as follows:
a. If the CAP.CSS.IOCSS bit is set to ‘1’, then the host does the following:
i. Issue the Identify command specifying the Identify I/O Command Set data structure (CNS 1Ch); and
ii. Issue the Set Features command with the I/O Command Set Profile Feature Identifier (FID 19h) specifying the index of the I/O Command Combination (refer to Figure 343) to be enabled;

and

b. For each I/O Command Set that is enabled (Note: the NVM Command Set is enabled if the CC.CSS field is set to 000b):
i. Issue the Identify command specifying the I/O Command Set specific Active Namespace ID list (CNS 07h) with the appropriate Command Set Identifier (CSI) value of that I/O Command Set; and
ii. For each NSID that is returned:
1. If the enabled I/O Command Set is the NVM Command Set or an I/O Command Set based on the NVM Command Set (e.g., the Zoned Namespace Command Set) issue the Identify command specifying the Identify Namespace data structure (CNS 00h); and
2. Issue the Identify command specifying each of the following data structures (refer to Figure 326): the I/O Command Set specific Identify Namespace data structure, the I/O Command Set specific Identify Controller data structure, and the I/O Command Set independent Identify Namespace data structure;

9. If the controller implements I/O queues, then the host should determine the number of I/O Submission Queues and I/O Completion Queues supported using the Set Features command with the Number of Queues feature identifier. After determining the number of I/O Queues, the NVMe Transport specific interrupt registers (e.g., MSI and/or MSI-X registers) should be configured;

10. If the controller implements I/O queues, then the host should allocate the appropriate number of I/O Completion Queues based on the number required for the system configuration and the number supported by the controller. The I/O Completion Queues are allocated using the Create I/O Completion Queue command;

11. If the controller implements I/O queues, then the host should allocate the appropriate number of I/O Submission Queues based on the number required for the system configuration and the number supported by the controller. The I/O Submission Queues are allocated using the Create I/O Submission Queue command; and

12. To enable asynchronous notification of optional events, the host should issue a Set Features command specifying the events to enable. To enable asynchronous notification of events, the host should submit an appropriate number of Asynchronous Event Request commands. This step may be done at any point after the controller signals that the controller is ready (i.e., CSTS.RDY is set to ‘1’).
===== page_number= 106, page_type= body ==___

After performing these steps, the controller shall be ready to process Admin or I/O commands issued by the host.

For exit of the D3 power state (refer to the PCI Express Base Specification), the initialization steps outlined should be followed.



![Embeded_Image 1](restored_images/Embeded_Image_1.png)
**Embeded_Image 1**


---

## 3.5.2 Message-based Controller Initialization (Fabrics)

The host selects the NVM subsystem with which to create a host to controller association. The host first establishes an NVMe Transport connection with the NVM subsystem. Next the host forms an association with a controller and creates the Admin Queue using the Fabrics Connect command. Finally, the host configures the controller and creates I/O Queues. Figure 82 is a ladder diagram that describes the queue creation process for an Admin Queue or an I/O Queue.

### Figure 82: Queue Creation Flow

<!-- Figure 82, coordinate:(185,294,880,655) -->

The controller initialization steps after an association is established are described below. For determining capabilities or configuring properties, the host uses the Property Get command and Property Set command, respectively.

1. NVMe in-band authentication is performed if required (refer to section 8.3.5.2);
2. The host determines the controller capabilities;
3. The host determines the supported I/O Command Sets by checking the state of CAP.CSS and appropriately initializing CC.CSS as follows:
   a. If the CAP.CSS.NOIOCSS bit is set to '1', then the CC.CSS field should be set to 111b;
   b. If the CAP.CSS.IOCSS bit is set to '1', then the CC.CSS field should be set to 110b; and
   c. If the CAP.CSS.IOCSS bit is cleared to '0' and the CAP.CSS.NCSS bit is set to '1', then the CC.CSS field should be set to 000b;
4. The host configures controller settings. Specific settings include:
   a. The arbitration mechanism should be selected in CC.AMS; and
   b. The memory page size should be initialized in CC.MPS;
===== page_number= 107, page_type= body ====

NVM Express® Base Specification, Revision 2.3

5. The controller should be enabled by setting CC.EN to ‘1’;
6. The host should wait for the controller to indicate the controller is ready to process commands. The controller is ready to process commands when CSTS.RDY is set to ‘1’;
7. The host determines the configuration of the controller by issuing the Identify command specifying the Identify Controller data structure (i.e., CNS 01h);
8. The host determines any I/O Command Set specific configuration information as follows:
    a. If the CAP.CSS.IOCSS bit is set to ‘1’, then the host does the following:
        i. Issue the Identify command specifying the Identify I/O Command Set data structure (CNS 1Ch); and
        ii. Issue the Set Features command with the I/O Command Set Profile Feature Identifier (FID 19h) specifying the index of the I/O Command Set Combination (refer to Figure 343) to be enabled;
    and
    b. For each I/O Command Set that is enabled (Note: the NVM Command Set is enabled if the CC.CSS field is set to 000b):
        i. Issue the Identify command specifying the I/O Command Set specific Active Namespace ID list (CNS 07h) with the appropriate Command Set Identifier (CSI) value of that I/O Command Set; and
        ii. For each NSID that is returned:
            1. If the enabled I/O Command Set is the NVM Command Set or an I/O Command Set based on the NVM Command Set (e.g., the Zoned Namespace Command Set) issue the Identify command specifying the Identify Namespace data structure (CNS 00h); and
            2. Issue the Identify command specifying each of the following data structures (refer to Figure 326: the I/O Command Set specific Identify Namespace data structure, the I/O Command Set specific Identify Controller data structure, and the I/O Command Set independent Identify Namespace data structure;
9. The host should determine:
    a. the maximum I/O Queue size using CAP.MQES; and
    b. the number of I/O Submission Queues and I/O Completion Queues supported using the response from the Set Features command with the Number of Queues feature identifier;
10. The host should use the Connect command (refer to section 6.3) to create I/O Submission and Completion Queue pairs; and
11. To enable asynchronous notification of optional events, the host should issue a Set Features command specifying the events to enable. The host may submit one or more Asynchronous Event Request commands to be notified of asynchronous events as described by section 5.2.2. This step may be done at any point after the controller signals that the controller is ready (i.e., CSTS.RDY is set to ‘1’).

The association may be removed if step 5 (i.e., setting CC.EN to ‘1’) is not completed within 2 minutes after establishing the association.

**3.5.2.1 Discovery Controller Initialization**

The initialization process for Discovery controllers is described in Figure 83.

<!-- Figure 83, coordinate:(115,780,665,795) -->
===== page_number= 108, page_type= body ====

NVM Express® Base Specification, Revision 2.3

<!-- Figure 83: Discovery Controller Initialization process flow, coordinate:(268,88,875,545) -->

**Figure 83: Discovery Controller Initialization process flow**

**Notes:**
1. Refer to section 6.3.
2. Refer to the Keep Alive command in section 5.2.14.
3. Refer to the Asynchronous Event Request command in section 5.2.2.
4. Refer to the following steps in this section.

After the Connect command completes with a status of Successful Completion, the host performs the following steps:
1. NVMe authentication is performed if required (refer to section 8.3.5.2);
2. The host determines the controller’s capabilities by reading the Controller Capabilities property;
3. The host configures the controller’s settings by writing the Controller Configuration property, including setting CC.EN to ‘1’ to enable command processing;
4. The host waits for the controller to indicate that the controller is ready to process commands. The controller is ready to process commands when CSTS.RDY is set to ‘1’ in the Controller Status property; and
5. The host determines the features and capabilities of the controller by issuing an Identify command, specifying each applicable Controller data structure.

After initializing the Discovery controller, the host reads the Discovery log page. Refer to section 5.2.12.3.3.



![Figure 82](restored_images/Figure_82.png)
**Figure 82**
![Figure 83](restored_images/Figure_83.png)
**Figure 83**


---

### 3.5.3 Controller Ready Modes During Initialization

There are two controller ready modes:

- **Controller Ready With Media**: By the time the controller becomes ready (i.e., by the time that CSTS.RDY transitions from ‘0’ to ‘1’) after the controller is enabled (i.e., CC.EN transitions from ‘0’ to ‘1’), then:
  a) the controller shall be able to process all commands without error as described in section 3.5.4.1; and
===== page_number= 109, page_type= body ==___

b) all namespaces attached to the controller and all media required to process Admin commands shall be ready (i.e., commands are not permitted to be aborted with a status code of Namespace Not Ready with the Do Not Retry bit cleared to '0' or Admin Command Media Not Ready with the Do Not Retry bit cleared to '0').

- **Controller Ready Independent of Media**: After the controller is enabled, all namespaces attached to the controller and media required to process Admin commands may or may not become ready by the time the controller becomes ready. Any Admin command or I/O command that specifies one or more namespaces attached to the controller is permitted to be aborted with a status code of Namespace Not Ready with the Do Not Retry bit cleared to '0' until CRTO.CRWMТ amount of time after the controller is enabled.

Admin commands that require access to the media are permitted to be aborted with a status code of Admin Command Media Not Ready with the Do Not Retry bit cleared to '0' until CRTO.CRWMТ amount of time after the controller is enabled. Refer to Figure 84 for a list of Admin commands that are permitted to be aborted with a status code of Admin Command Media Not Ready.

The controller shall be able to process without error as described in section 3.5.4.1:

a) all Admin commands not listed in Figure 84 by the time the controller is ready;

b) all Admin commands listed in Figure 84 no later than CRTO.CRWMТ amount of time after the controller is enabled; and

c) all I/O commands no later than CRTO.CRWMТ amount of time after the controller is enabled.

**Figure 84: Admin Commands Permitted to Return a Status Code of Admin Command Media Not Ready**

<!-- Figure 84, coordinate:(114,465,882,900) -->

| Admin Command             | Additional Restrictions                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Capacity Management       |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Device Self-test          | If the Device Self-Test would result in testing one or more namespaces, then returning a status code of Admin Command Media Not Ready is permitted. If the Device Self-Test would not result in testing any namespaces, then returning a status code of Admin Command Media Not Ready is not permitted.                                                                                                                              |
| Firmware Commit           |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Firmware Image Download   |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Get LBA Status            |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Get Log Page              | Get Log Page is only permitted to return a status code of Admin Command Media Not Ready for the following log pages: <ul><li>Device Self-test</li><li>Firmware Slot Information</li><li>Telemetry Controller-Initiated</li><li>Telemetry Host-Initiated</li><li>Predictable Latency Per NVM Set</li><li>Predictable Latency Event Aggregate</li><li>Persistent Event Log</li><li>LBA Status Information</li><li>Endurance Group Event Aggregate</li><li>Media Unit Status</li><li>Supported Capacity Configuration List</li><li>Boot Partition</li><li>Reservation Notification</li><li>Rotational Media Information</li><li>Vendor Specific</li></ul> |
| Namespace Attachment      |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Namespace Management      |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Format NVM                |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Sanitize                  |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Sanitize Namespace        |                                                                                                                                                                                                                                                                                                                                                                                                                       |

109
===== page_number= 110, page_type= body ==___

NVM Express® Base Specification, Revision 2.3

## Figure 84: Admin Commands Permitted to Return a Status Code of Admin Command Media Not Ready

| Admin Command         | Additional Restrictions |
|-----------------------|-------------------------|
| Security Receive¹     |                         |
| Security Send¹        |                         |
| Vendor Specific       |                         |

**Notes:**
1. A host may require discovery operations performed via Security Send/Receive (e.g., TCG Level 0 Discovery) to be processed prior to media being ready. Therefore, it is recommended that controllers not return Admin Command Media Not Ready for such discovery operations.

The Controller Ready Modes Supported (CAP.CRMS) field (refer to Figure 36) indicates which controller ready modes are supported. The CAP.CRMS field consists of two bits:
- the Controller Ready With Media Support (CAP.CRMS.CRWMS) bit; and
- the Controller Ready Independent of Media Support (CAP.CRMS.CRIMS) bit.

Controllers shall set the CAP.CRMS.CRWMS bit to ‘1’ (i.e., set the CAP.CRMS field to 01b or 11b). The CAP.CRMS.CRWMS bit was not defined prior to NVM Express Base Specification, Revision 2.0. Controllers compliant with revisions earlier than NVM Express Base Specification, Revision 2.0 may clear the CAP.CRMS field to 00b.

The Controller Ready Independent of Media Enable (CC.CRIME) bit (refer to Figure 41) controls the controller ready mode based on the value of the CAP.CRMS field as follows:
- a) If the CAP.CRMS field is cleared to 00b, the controller ready mode is not able to be selected. In this case, the read-only CC.CRIME bit shall be cleared to ‘0’ and should be ignored by a host;
- b) If the CAP.CRMS field is set to 01b (i.e., the CAP.CRMS.CRIMS bit is cleared to ‘0’ and the CAP.CRMS.CRWMS bit is set to ‘1’), then the controller is in Controller Ready With Media mode and the read-only CC.CRIME bit shall be cleared to ‘0’; and
- c) If the CAP.CRMS field is set to 11b, then both controller ready modes are supported, and the host may select the controller ready mode by modifying the value of the CC.CRIME bit. In this situation, the host should set the controller ready mode by writing to the CC.CRIME bit before the controller is enabled (e.g., as part of the initialization sequence of actions described in section 3.5).



| Admin Command             | Additional Restrictions                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Capacity Management       |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Device Self-test          | If the Device Self-Test would result in testing one or more namespaces, then returning a status code of Admin Command Media Not Ready is permitted. If the Device Self-Test would not result in testing any namespaces, then returning a status code of Admin Command Media Not Ready is not permitted.                                                                                                                              |
| Firmware Commit           |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Firmware Image Download   |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Get LBA Status            |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Get Log Page              | Get Log Page is only permitted to return a status code of Admin Command Media Not Ready for the following log pages: <ul><li>Device Self-test</li><li>Firmware Slot Information</li><li>Telemetry Controller-Initiated</li><li>Telemetry Host-Initiated</li><li>Predictable Latency Per NVM Set</li><li>Predictable Latency Event Aggregate</li><li>Persistent Event Log</li><li>LBA Status Information</li><li>Endurance Group Event Aggregate</li><li>Media Unit Status</li><li>Supported Capacity Configuration List</li><li>Boot Partition</li><li>Reservation Notification</li><li>Rotational Media Information</li><li>Vendor Specific</li></ul> |
| Namespace Attachment      |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Namespace Management      |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Format NVM                |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Sanitize                  |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Sanitize Namespace        |                                                                                                                                                                                                                                                                                                                                                                                                                       |

| Admin Command         | Additional Restrictions |
|-----------------------|-------------------------|
| Security Receive¹     |                         |
| Security Send¹        |                         |
| Vendor Specific       |                         |


---

### 3.5.4 Controller Ready Timeouts During Initialization

The CAP.CRMS field was not defined prior to NVM Express Base Specification, Revision 2.0. Controllers compliant with revisions earlier than NVM Express Base Specification, Revision 2.0 may clear the CAP.CRMS field to 00b. This section is applicable to controllers that clear the CAP.CRMS field to 00b and controllers that set CAP.CRMS to a non-zero value.

There are three controller ready timeout fields:
1. CAP.TO (refer to Figure 36);
2. CRTO.CRWMТ (refer to Figure 57); and
3. CRTO.CRIMT (refer to Figure 57).

The details regarding these timeouts during controller initialization are as follows:
- a) The CAP.TO field shall be set as described in Figure 36;
- b) If the CAP.CRMS field is cleared to 00b, then the worst-case time the host should wait after the controller is enabled (i.e., CC.EN transitions from ‘0’ to ‘1’) for the controller to become ready (CSTS.RDY transitions from ‘0’ to ‘1’) is indicated by CAP.TO;
- c) If the controller is in Controller Ready With Media mode (i.e., the CC.CRIME bit is cleared to ‘0’), then:
    - i. the Controller Ready Independent of Media Timeout (CRTO.CRIMT) field is not applicable; and

<!-- Figure 84, coordinate:(114,104,878,264) -->
===== page_number= 111, page_type= body ====

ii. the Controller Ready With Media Timeout (CRTO.CRWMT) indicates the worst-case time the host should wait after the controller is enabled for:
    1. the controller to become ready and be able to process all commands without error as described in section 3.5.4.1; and
    2. all attached namespaces and media required to process Admin commands to become ready;

and

d) If the controller is in Controller Ready Independent of Media mode (i.e., the CC.CRIME bit is set to '1'), then
    i. the Controller Ready With Media Timeout (CRTO.CRWMT) field indicates the worst-case time that a host should wait for all attached namespaces and media required to process Admin commands to become ready after the controller is enabled; and
    ii. the Controller Ready Independent of Media Timeout (CRTO.CRIMT) field indicates the worst-case time the host should wait after the controller is enabled for the controller to become ready and be able to process:
        1. all commands that do not access attached namespaces; and
        2. Admin commands that do not require access to media,
        without error as described in section 3.5.4.1.

Changes to the value of the CC.CRIME bit shall have no effect on the values of the CRTO.CRWMT and CRTO.CRIMT fields. Changes to the value of the CC.CRIME bit may have an effect on the value of the CAP.TO field (refer to Figure 36).



![Figure 84](restored_images/Figure_84.png)
**Figure 84**


---

### 3.5.4.1 Handling Errors During Initialization

If the CAP.CRMS field is non-zero and the controller has been enabled by transitioning CC.EN from '0' to '1' and the controller encounters a failure that prevents:

a) at least one:
    - command that does not access attached namespaces; or
    - Admin command that does not require access to media (refer to Figure 84),
    from being able to be processed without error by the amount of time indicated by the:
    - Controller Ready Independent of Media Timeout (CRTO.CRIMT) field since the controller was enabled if the controller is in Controller Ready Independent of Media mode (i.e., the CC.CRIME bit is set to '1'); or
    - Controller Ready With Media Timeout (CRTO.CRWMT) field since the controller was enabled if the controller is in Controller Ready With Media mode (i.e., the CC.CRIME bit is cleared to '0');

b) at least one namespace attached to the controller from becoming ready by the amount of time indicated by the Controller Ready With Media Timeout (CRTO.CRWMT) field since the controller was enabled; or

c) media required by at least one Admin command from becoming ready by the amount of time indicated by the Controller Ready With Media Timeout (CRTO.CRWMT) field since the controller was enabled,

then:

a) if the controller has not become ready, then the controller shall become ready (i.e., set CSTS.RDY to '1') no later than CRTO.CRWMT amount of time after the controller was enabled; and

b) if the Persistent Event log page is supported, then the controller shall record an NVM Subsystem Hardware Error Event with the NVM Subsystem Hardware Error Event code set to a value of Controller Ready Timeout Exceeded in the Persistent Event log page (refer to Figure 240).
===== page_number= 112, page_type= body ==___



---

# 3.6 Shutdown Processing

This section describes the recommended procedure for shutdown processing prior to a power-off condition.

There are two shutdown processing mechanisms, controller shutdown (refer to sections 3.6.1 and 3.6.2) and NVM Subsystem Shutdown (refer to section 3.6.3). The CSTS.ST bit indicates the shutdown mechanism that is in progress, if any (refer to Figure 42). A host requests a controller shutdown by modifying the CC.SHN field (refer to Figure 41). A host requests an NVM Subsystem Shutdown by modifying the NSSD property (refer to section 3.1.4.20) or by issuing an NVMe-MI Shutdown command to a Management Endpoint (refer to the NVM Express Management Interface Specification).

At most one shutdown processing mechanism is able to be in progress for a controller at any time. If an NVM Subsystem Shutdown is requested while a controller shutdown is in progress, then the NVM Subsystem Shutdown overrides the controller shutdown. The progress and completion of shutdown processing is indicated by the CSTS.SHST field (refer to Figure 42).

NVM Subsystem Shutdown should not be supported by any NVM subsystem that does not support more than one controller, without counting virtual controllers (e.g., NVM Subsystem Shutdown should not be supported by an NVM subsystem that supports one primary controller and multiple secondary controllers) (refer to section 8.2.6).

Figure 85 describes the interactions of the shutdown processing state indicated by the CSTS.SHST field with the state of the controller indicated by the CC.EN bit (refer to Figure 41) and by the CSTS.RDY bit (refer to Figure 42). The four possible media states in Figure 85 are: shutdown, shutdown in progress, usable, and initialization in progress.

## Figure 85: Shutdown Processing Interactions

<!-- Figure 85, coordinate:(120,455,870,825) -->

| CC.EN | CSTS.RDY | CSTS.SHST | Controller able to process Admin and I/O commands⁴ | Media state | Controller ready to be powered off |
|-------|----------|-----------|----------------------------------------------------|-------------|------------------------------------|
| 0     | 0        | 00b       | no                                                 | any         | implementation specific¹          |
| 0     | 0        | 01b       | no³                                                | shutdown in progress | no                             |
| 0     | 0        | 10b       | no                                                 | shutdown    | yes                               |
| 1     | 1        | 00b       | yes                                                | initialization in progress or usable² | no                             |
| 1     | 1        | 01b       | no³                                                | shutdown in progress | no                             |
| 1     | 1        | 10b       | no                                                 | shutdown    | yes                               |

**Notes:**

1. In some cases (e.g., following initial application of power, or following a Controller Level Reset that occurred while shutdown processing was reported as complete), the controller is permitted to initialize the media and cease being ready to be powered off as a consequence.

2. If the CC.CRIME bit is cleared to '0', then the media is usable. If the CC.CRIME bit is set to '1', then either media initialization is in progress or the media is usable (refer to Figure 41).

3. While shutdown processing is in progress, the controller may abort any command with a status code of Commands Aborted due to Power Loss Notification.

4. I/O commands are only able to be processed by a controller that supports I/O commands. Fabrics commands are always able to be processed by a controller that supports Fabrics commands.

Figure 85 does not include transition conditions for a controller that is becoming ready or is undergoing reset. During these transitions, the CC.EN bit and the CSTS.RDY bit have different values (refer to Figure 41 and Figure 42). The media may or may not be usable during these transitions.
===== page_number= 113, page_type= body ====

Figure 85 does not include the NVMe-MI effects of processing an Admin command that requires access to the media (refer to Figure 84) and specifies the Ignore Shutdown bit set to '1' is processed by the controller via the out-of-band mechanism (refer to the NVM Express Management Interface Specification). Processing of such a command causes the media to become usable, after which the media may or may not be returned to its previous condition.

If the Controller Power Scope (i.e., CAP.CPS) field is cleared to 00b (i.e., Not Reported) or set to 01b (i.e., Controller scope), it is recommended that the host wait until the controller is ready to be powered off before removing power. The controller is ready to be powered off when that controller reports shutdown processing is complete (i.e., CSTS.SHST field is set to 10b).

If the CAP.CPS field is set to 10b (i.e., Domain scope), it is recommended that the host wait until the domain is ready to be powered off before removing power. The domain is ready to be powered off when all the controllers in that domain report shutdown processing is complete (i.e., CSTS.SHST field is set to 10b on all controllers in the domain).

If the CAP.CPS field is set to 11b (i.e., NVM subsystem scope), it is recommended that the host wait until the NVM subsystem is ready to be powered off before removing power. The NVM subsystem is ready to be powered off when all controllers in the NVM subsystem report shutdown processing is complete (i.e., CSTS.SHST field is set to 10b on all controllers in the NVM subsystem).



| CC.EN | CSTS.RDY | CSTS.SHST | Controller able to process Admin and I/O commands⁴ | Media state | Controller ready to be powered off |
|-------|----------|-----------|----------------------------------------------------|-------------|------------------------------------|
| 0     | 0        | 00b       | no                                                 | any         | implementation specific¹          |
| 0     | 0        | 01b       | no³                                                | shutdown in progress | no                             |
| 0     | 0        | 10b       | no                                                 | shutdown    | yes                               |
| 1     | 1        | 00b       | yes                                                | initialization in progress or usable² | no                             |
| 1     | 1        | 01b       | no³                                                | shutdown in progress | no                             |
| 1     | 1        | 10b       | no                                                 | shutdown    | yes                               |


---

### 3.6.1 Memory-based Controller Shutdown (PCIe)

It is recommended that the host perform an orderly shutdown of the controller by following the procedure in this section when a power-off or shutdown condition is imminent.

The host should perform the following actions in sequence for a normal controller shutdown:

1. If the controller is enabled (i.e., CC.EN (refer to Figure 41) is set to '1'):
   a. Stop submitting any new I/O commands to the controller and allow any outstanding commands to complete;
   b. If the controller implements I/O queues, then the host should delete all I/O Submission Queues, using the Delete I/O Submission Queue command (refer to section 5.3.4). A result of the successful completion of the Delete I/O Submission Queue command is that any remaining commands outstanding are aborted;
   c. If the controller implements I/O queues, then the host should delete all I/O Completion Queues, using the Delete I/O Completion Queue command (refer to section 5.3.3);

and

2. The host should set the Shutdown Notification (CC.SHN) field (refer to Figure 41) to 01b to indicate a normal controller shutdown operation. The controller indicates when shutdown processing is completed by updating the Shutdown Status (CSTS.SHST) field to 10b and the Shutdown Type (CSTS.ST) field (refer to Figure 42) is cleared to '0'.

The host should perform the following actions in sequence for an abrupt shutdown:

1. If the controller is enabled (i.e., CC.EN is set to '1'), then stop submitting any new I/O commands to the controller; and
2. The host should set the Shutdown Notification (CC.SHN) field (refer to Figure 41) to 10b to indicate an abrupt shutdown operation. The controller indicates when shutdown processing is completed by updating the Shutdown Status (CSTS.SHST) field (refer to Figure 42) to 10b and CSTS.ST (refer to Figure 42) is cleared to '0'.

For entry to the D3 power state (refer to the PCI Express Base Specification), the shutdown steps outlined for a normal controller shutdown should be followed.

It is recommended that the host wait a minimum of the RTD3 Entry Latency reported in the Identify Controller data structure (refer to Figure 328) for the shutdown operations to complete; if the value reported in RTD3 Entry Latency is 0h, then the host should wait for a minimum of one second. While shutdown processing is in progress on a controller, it is not recommended to disable that controller via the CC.EN bit
===== page_number= 114, page_type= body ==___

(i.e., via a Controller Reset), which may impact the time required to complete shutdown processing. While shutdown processing is in progress on a controller, that controller may abort any command with a status code of Commands Aborted due to Power Loss Notification.

The controller is ready to be powered off (e.g., the media is in the shutdown state (refer to Figure 85)) when the CSTS.ST bit is cleared to '0', and the CSTS.SHST field indicates that controller shutdown processing is complete (i.e., the CSTS.SHST field is set to 10b), regardless of the value of the CC.EN bit. The controller remains ready to be powered off (e.g., the media remains in the shutdown state) until:

- A. the controller is enabled (i.e., the CC.EN bit transitions from '0' to '1');
- B. the controller is reset by a Controller Level Reset; or
- C. an Admin command that requires access to the media (refer to Figure 84) and specifies the Ignore Shutdown bit set to '1' is processed by the controller via the out-of-band mechanism (refer to the NVMe Express Management Interface Specification).

If a Controller Level Reset occurs while controller shutdown processing is reported as complete (i.e., the CSTS.ST bit is cleared to '0' and the CSTS.SHST field is set to 10b), then the controller may remain ready to be powered off (e.g., the media remains in the shutdown state) or the controller may cease being ready to be powered off (e.g., because the controller is preparing the media for use (refer to section 3.7.2)).

If the power scope for the controller includes multiple controllers (e.g., the CAP.CPS field is set to 10b or is set to 11b), and any controller included in that power scope is not ready to be powered off, then the portion of the NVMe subsystem included in that power scope is not ready to be powered off.

To start executing commands on the controller after that controller reports controller shutdown processing complete (i.e., the CSTS.ST bit is cleared to '0' and the CSTS.SHST field is set to 10b) utilizing the CC.EN bit:

- if the CC.EN bit is set to '1', then a Controller Level Reset is required to clear the CC.EN bit to '0' on that controller and the CC.EN bit is subsequently required to be set to '1' as part of the initialization sequence (refer to section 3.5); and
- if the CC.EN bit is cleared to '0', then:
  - a Controller Level Reset is required and the CC.EN bit is subsequently required to be set to '1' as part of the initialization sequence (refer to section 3.5); or
  - the CC.EN bit is required to be set to '1' and the CC.SHN field is required to be cleared to 00b with the same write to the CC property (refer to Figure 41). The controller clears the CSTS.SHST field to 00b in response to that write.

The initialization sequence (refer to section 3.5) should then be executed on that controller.

It is an implementation choice whether the host aborts all outstanding commands to the Admin Queue prior to the controller shutdown. The only commands that should be outstanding to the Admin Queue when the controller reports shutdown processing complete are Asynchronous Event Request commands.

If the host is no longer able to communicate with the controller before that host receives either:

- completions for all outstanding commands submitted to that controller (refer to section 3.4.5); or
- a CSTS.SHST field value that indicates that the controller shutdown is complete,

then it is strongly recommended that the host take the steps described in section 9.6 to avoid possible data corruption caused by interaction between outstanding commands and subsequent commands submitted by that host to another controller.



---

### 3.6.2 Message-based Controller Shutdown (Fabrics)

To initiate a shutdown of a controller, the host should use the Property Set command (refer to section 6.6) to set the Shutdown Notification (CC.SHN) field to:

- 01b to initiate a normal shutdown operation; or
- 10b to initiate an abrupt shutdown operation.

<!-- Figure 85, coordinate:(114,140,885,155) -->
<!-- Figure 84, coordinate:(114,230,885,245) -->
<!-- Figure 41, coordinate:(114,570,885,585) -->
===== page_number= 115, page_type= body ====

NVM Express® Base Specification, Revision 2.3

After the host initiates a controller shutdown, the host may either disconnect at the NVMe Transport level or the host may choose to poll CSTS.SHST to determine when the controller shutdown is complete (i.e., the controller should not initiate a disconnect at the NVMe Transport level). It is an implementation choice whether the host aborts all outstanding commands prior to initiating the shutdown.

If the host is no longer able to communicate with the controller before that host receives either:
- completions for all outstanding commands submitted to that controller (refer to section 3.4.5); or
- a CSTS.SHST field value that indicates that the controller shutdown is complete,

then it is strongly recommended that the host take the steps described in section 9.6 to avoid possible data corruption caused by interaction between outstanding commands and subsequent commands submitted by that host to another controller.

The CC.EN field is not used to shutdown the controller (i.e., it is used for Controller Reset, refer to section 3.7.2.1).

From the time a controller shutdown is initiated until:
- a Controller Level Reset occurs; or
- the controller, if dynamic, is removed from the NVM subsystem,

the controller shall:
- process only Fabrics commands (refer to Figure 574); and
- disable the Keep Alive timer, if supported.

To start executing commands on the controller after that controller reports controller shutdown processing complete (i.e., the CSTS.ST bit is cleared to '0' and the CSTS.SHST field is set to 10b) utilizing the CC.EN bit:
- if the CC.EN bit is set to '1', then a Controller Level Reset is required to clear the CC.EN bit to '0' on that controller and the CC.EN bit is subsequently required to be set to '1' as part of the initialization sequence (refer to section 3.5); and
- if the CC.EN bit is cleared to '0', then:
  - a Controller Level Reset is required and the CC.EN bit is subsequently required to be set to '1' as part of the initialization sequence (refer to section 3.5); or
  - the CC.EN bit is required to be set to '1' and the CC.SHN field is required to be cleared to 00b with a single Property Set command (refer to section 6.6) that changes the CC property (refer to Figure 41). The controller clears the CSTS.SHST field to 00b in response to that write.

The initialization sequence (refer to section 3.5) should then be executed on that controller.



![Figure 85](restored_images/Figure_85.png)
**Figure 85**
![Figure 84](restored_images/Figure_84.png)
**Figure 84**
![Figure 41](restored_images/Figure_41.png)
**Figure 41**


---

### 3.6.3 NVM Subsystem Shutdown

An NVM Subsystem Shutdown initiates a shutdown of all controllers in a domain or NVM subsystem from a single controller.

Interactions between NVM Subsystem Shutdown and Power Loss Signaling processing are described in section 8.2.5.

A controller indicates support for the NVM Subsystem Shutdown Feature by setting the CAP.NSSS bit to '1' (refer to Figure 36).

The NVM Subsystem Shutdown Feature defined in this revision of the NVM Express Base Specification includes some functionality that differs from the functionality of the NVM Subsystem Shutdown Feature defined in revision 2.0 of the NVM Express Base Specification. A controller indicates support for these functionality differences by setting the NVM Subsystem Shutdown Enhancements Supported (CAP.NSSES) bit to '1' (refer to Figure 36).

<!-- Figure 574, coordinate:(0,0,0,0) -->
<!-- Figure 41, coordinate:(0,0,0,0) -->
<!-- Figure 36, coordinate:(0,0,0,0) -->
===== page_number= 116, page_type= body ====

If a controller sets the CAP.NSSES bit to ‘1’, then while an NVM Subsystem Shutdown is reported as in progress or is reported as complete (i.e., while the CSTS.ST bit is set to ‘1’ and the CSTS.SHST field is set to 01b or is set to 10b):

a. a Controller Reset initiates a Controller Level Reset (CLR) (refer to section 3.7.2); and  
b. the values of both the CSTS.ST bit and the CSTS.SHST field (refer to Figure 40) are not changed by a CLR initiated by any method other than an NVM Subsystem Reset.

If a controller clears the CAP.NSSES bit to ‘0’, then, as defined in revision 2.0 of the NVM Express Base Specification:

a. while an NVM Subsystem Shutdown is reported as in progress or is reported as complete, a Controller Reset does not initiate a CLR (i.e., Controller Reset is disabled); and  
b. while an NVM Subsystem Shutdown is reported as complete, any CLR initiated by any transport-specific reset type may clear the value of the CSTS.ST bit to ‘0’ and may clear the value of the CSTS.SHST field to 00b.

A host is able to support NVM Subsystem Shutdown functionality both on controllers that set the CAP.NSSES bit to ‘1’ and on controllers that clear the CAP.NSSES bit to ‘0’ by ensuring that any NVM Subsystem Shutdown is followed by an NVM Subsystem Reset regardless of the value of the CSTS.ST bit and the value of the CSTS.SHST field.



---

### 3.6.3.1 NVM Subsystem Shutdown in a Single Domain NVM Subsystem

A normal shutdown on all controllers within the NVM subsystem (i.e., normal NVM Subsystem Shutdown) is initiated by:

- a host writing the value 4E726D6Ch ("NrmI") to NSSD.NSSC when CAP.CPS is set to 11b; or  
- issuing an NVMe-MI Shutdown command to a Management Endpoint (refer to the NVM Express Management Interface Specification) specifying a normal shutdown.

For each controller in the NVM subsystem for this normal NVM Subsystem Shutdown, if:

- CSTS.SHST is set to 00b; and  
- An outstanding Asynchronous Event Request command exists,

then the controller shall issue a Normal NVM Subsystem Shutdown event prior to shutting down the controller.

An abrupt shutdown on all controllers within the NVM subsystem (i.e., abrupt NVM Subsystem Shutdown) is initiated by:

- a host writing the value 41627074h ("Abpt") to NSSD.NSSC when CAP.CPS is set to 11b; or  
- issuing an NVMe-MI Shutdown command to a Management Endpoint (refer to the NVM Express Management Interface Specification) specifying an abrupt shutdown.

While NVM Subsystem Shutdown processing is in progress, any controller in the NVM subsystem may abort any command with a status code of Commands Aborted due to Power Loss Notification.

It is recommended that the host wait a minimum of the NVM Subsystem Shutdown Latency reported in the Identify Controller data structure (refer to Figure 328) for NVM Subsystem Shutdown processing to complete; if the reported NVM Subsystem Shutdown Latency value is 0h, then the host should wait for a minimum of 30 seconds. While an NVM Subsystem Shutdown is reported as in progress, it is not recommended to reset the NVM subsystem via an NVM Subsystem Reset or a power cycle (which causes an NVM Subsystem Reset). This aborts the NVM Subsystem Shutdown which may impact the subsequent time required for the NVM subsystem to become ready to perform I/O (e.g., after power is reapplied following a power cycle).

For either a normal or an abrupt NVM Subsystem Shutdown, the NVM subsystem is ready to be powered off (e.g., the media is in the shutdown state (refer to Figure 85)) when the CSTS.ST bit is set to ‘1’ and the CSTS.SHST field indicates that shutdown processing is complete (i.e., the CSTS.SHST field is set to 10b) on any controller in the NVM subsystem. The NVM subsystem shall not set the CSTS.SHST field to 10b on

<!-- Figure 40, coordinate:(115,158,350,185) -->
<!-- Figure 328, coordinate:(115,735,350,762) -->
<!-- Figure 85, coordinate:(115,845,350,872) -->
===== page_number= 117, page_type= body ====

any controller in the NVM subsystem until the entire NVM subsystem is ready to be powered off. The NVM Subsystem shall indicate that NVM Subsystem Shutdown processing is complete by setting the CSTS.SHST field to 10b on all controllers in the NVM subsystem. The NVM subsystem remains ready to be powered off (e.g., the media remains in the shutdown state) until:

- A. an NVM Subsystem Reset; or
- B. an Admin command that requires access to the media (refer to Figure 84) and specifies the Ignore Shutdown bit set to ‘1’ is processed by any controller via the out-of-band mechanism (refer to the NVM Express Management Interface Specification).

If a normal or an abrupt NVM Subsystem Shutdown is reported as in progress or is reported as complete within the NVM subsystem (i.e., the CSTS.ST bit is set to ‘1’ and the CSTS.SHST field is set to either 01b or 10b on all controllers in the NVM subsystem, indicating that an NVM Subsystem Reset has not occurred since initiation of that NVM Subsystem Shutdown), then:

- **an NVM Subsystem Reset:**
  - shall abort any in progress NVM Subsystem Shutdown;
  - clears the CSTS.SHST field to 00b in all controllers in the NVM subsystem; and
  - clears the CSTS.ST bit to ‘0’ in all controllers in the NVM subsystem;

and

- **a Controller Level Reset of any controller in the NVM subsystem that is initiated by any other method (refer to section 3.7.2):**
  - shall not abort any in progress NVM Subsystem Shutdown;
  - does not change the values of the CSTS.ST bit and the CSTS.SHST field, as described in Figure 42; and
  - shall not cause that NVM subsystem to cease being ready to be powered off (e.g., shall not transition the media out of the shutdown state) if that NVM Subsystem was ready to be powered off when that Controller Level Reset was initiated.

To start executing commands on the controller after that controller reports NVM Subsystem Shutdown processing complete (i.e., the CSTS.ST bit is set to ‘1’ and the CSTS.SHST field is set to 10b):

- regardless of the value of the CC.EN bit, an NVM Subsystem Reset is required; and
- the CC.EN bit is subsequently required to be set to ‘1’ as part of the initialization sequence (refer to section 3.5).

The initialization sequence (refer to section 3.5) should then be executed on that controller.



![Figure 40](restored_images/Figure_40.png)
**Figure 40**
![Figure 328](restored_images/Figure_328.png)
**Figure 328**
![Figure 85](restored_images/Figure_85.png)
**Figure 85**


---

### 3.6.3.2 Domain Shutdown in a Multiple Domain NVM Subsystem

A normal NVM Subsystem Shutdown on this controller and all controllers within the associated domain is initiated by:

- a host writing the value 4E726D6Ch ("NrmI") to NSSD.NSSC when CAP.CPS is set to 10b; or
- issuing an NVMe-MI Shutdown command to a Management Endpoint (refer to the NVM Express Management Interface Specification) specifying a normal shutdown.

For each controller in the domain for this normal NVM subsystem shutdown, if:

- CSTS.SHST is cleared to 00b; and
- An outstanding Asynchronous Event Request command exists,

then the controller shall issue a Normal NVM Subsystem Shutdown event prior to shutting down the controller.

An abrupt NVM Subsystem Shutdown to this controller and all controllers within the associated domain is initiated by:

- a host writing the value 41627074h ("Abpt") to NSSD.NSSC when CAP.CPS is set to 10b; or

<!-- Figure 84, coordinate:(115,165,885,215) -->
<!-- Figure 42, coordinate:(230,445,885,475) -->
===== page_number= 118, page_type= body ====

- issuing an NVMe-MI Shutdown command to a Management Endpoint (refer to the NVM Express Management Interface Specification) specifying an abrupt shutdown.

While NVM Subsystem Shutdown processing is in progress, any controller in the domain may abort any command with a status code of Commands Aborted due to Power Loss Notification.

It is recommended that the host wait a minimum of the NVM Subsystem Shutdown Latency reported in the Identify Controller data structure (refer to Figure 328) for NVM Subsystem Shutdown processing on a domain to complete; if the reported NVM Subsystem Shutdown Latency value is 0h, then the host should wait for a minimum of 30 seconds. While an NVM Subsystem Shutdown is reported as in progress, it is not recommended to reset the domain via either an NVM Subsystem Reset on the domain or power cycling the domain (which causes an NVM Subsystem Reset on the domain). This aborts the NVM Subsystem Shutdown which may impact the subsequent time required for the domain to become ready to perform I/O (e.g., after power is reapplied following a power cycle).

For either a normal or an abrupt NVM Subsystem Shutdown on the domain, the domain is ready to be powered off (e.g., the media is in the shutdown state (refer to Figure 85)) when the CSTS.ST bit is set to ‘1’ and the CSTS.SHST field indicates that shutdown processing is complete (i.e., the CSTS.SHST field is set to 10b) on any controller in the domain. The NVM subsystem shall not set the CSTS.SHST field to 10b on any controller in the domain until the entire domain is ready to be powered off. The NVM Subsystem shall indicate that NVM Subsystem Shutdown processing is complete by setting the CSTS.SHST field to 10b on all controllers in the domain. The domain remains ready to be powered off (e.g., the media remains in the shutdown state) until:

A. an NVM Subsystem Reset occurs on that domain; or  
B. an Admin command that requires access to the media (refer to Figure 84) and specifies the Ignore Shutdown bit set to ‘1’ is processed by any controller in the domain via the out-of-band mechanism (refer to the NVM Express Management Interface Specification).

If a normal or an abrupt NVM Subsystem Shutdown is reported as in progress or is reported as complete within a domain (i.e., the CSTS.ST bit is set to ‘1’ and the CSTS.SHST field is set to either 01b or 10b on all controllers in the domain, indicating that an NVM Subsystem Reset on the domain has not occurred since initiation of that NVM Subsystem Shutdown), then:

- an NVM Subsystem Reset on the domain:
  - shall abort any in progress NVM Subsystem Shutdown on the domain; and
  - clears the CSTS.SHST field to 00b in all controllers in the domain; and
  - clears the CSTS.ST bit to ‘0’ in all controllers in the domain;

and

- a Controller Level Reset of any controller in the domain that is initiated by any other method (refer to section 3.7.2)
  - shall not abort any in progress NVM Subsystem Shutdown on the domain;
  - does not change the values of the CSTS.ST bit and the CSTS.SHST field, as described in Figure 42; and
  - shall not cause the domain to cease being ready to be powered off (e.g., shall not transition the media out of the shutdown state) if the domain was ready to be powered off when that Controller Level Reset was initiated.

To start executing commands on the controller after that controller reports NVM Subsystem Shutdown processing complete (i.e., the CSTS.ST bit is set to ‘1’ and the CSTS.SHST field is set to 10b):

- regardless of the value of CC.EN, an NVM Subsystem Reset on that domain is required; and
- the CC.EN bit is subsequently required to be set to ‘1’ as part of the initialization sequence (refer to section 3.5).

The initialization sequence (refer to section 3.5) should then be executed on that controller.
===== page_number= 119, page_type= body ====

# NVM Express® Base Specification, Revision 2.3



![Figure 84](restored_images/Figure_84.png)
**Figure 84**
![Figure 42](restored_images/Figure_42.png)
**Figure 42**


---

## 3.7 Resets



---

### 3.7.1 NVM Subsystem Reset

Interactions between NVM Subsystem Reset and Power Loss Signaling processing are described in section 8.2.5.



---

### 3.7.1.1 Single Domain NVM Subsystems

The scope of an NVM Subsystem Reset depends on whether the NVM subsystem supports multiple domains. In an NVM subsystem that does not support multiple domains, the scope of the NVM Subsystem Reset is the entire NVM subsystem.

An NVM Subsystem Reset is initiated when:
- Main power is applied to the NVM subsystem;
- A value of 4E564D65h (“NVMe”) is written to the NSSR.NSSRC field;
- Requested using a method defined in the NVM Express Management Interface Specification; or
- A vendor specific event occurs.

When an NVM Subsystem Reset occurs, the entire NVM subsystem is reset. This includes the initiation of a Controller Level Reset on all controllers that make up the NVM subsystem, disabling of the Persistent Memory Region associated with all controllers that make up the NVM subsystem, and any transport specific actions defined in the applicable NVM Express Transport specification.

The occurrence of an NVM Subsystem Reset while power is applied to the NVM subsystem is reported by the initial value of the CSTS.NSSRO field following the NVM Subsystem Reset. This field may be used by a host to determine if the sudden loss of communication with a controller was due to an NVM Subsystem Reset or some other condition.

The ability for a host to initiate an NVM Subsystem Reset by writing to the NSSR.NSSRC field is an optional capability of a controller indicated by the state of the CAP.NSSRS field. An implementation may protect the NVM subsystem from an inadvertent NVM Subsystem Reset by not providing this capability to one or more controllers that make up the NVM subsystem.

The occurrence of a vendor specific event that results in an NVM Subsystem Reset is intended to allow implementations to recover from a severe NVM subsystem internal error that prevents continued normal operation (e.g., fatal hardware or firmware error).



---

### 3.7.1.2 Multiple Domain NVM Subsystems

The scope of an NVM Subsystem Reset depends on whether the NVM subsystem supports multiple domains. In an NVM subsystem that supports multiple domains, the scope of the NVM Subsystem Reset is either the controllers that are in a domain or the entire NVM subsystem.

An NVM Subsystem Reset on a domain is initiated when:
- Power is applied to that domain;
- A value of 4E564D65h (i.e., “NVMe”) is written to the NSSR.NSSRC field of one of the controllers in that domain; or
- A vendor specific event occurs within that domain.

When an NVM Subsystem Reset occurs the entire domain is reset. This includes the initiation of a Controller Level Reset on all controllers that are in the domain, disabling of the Persistent Memory Region associated with all controllers that are in the domain, and any transport specific actions defined in the applicable NVM Express Transport specification.

Alternatively, an NVM Subsystem Reset in an NVM subsystem that supports multiple domains may reset the entire NVM subsystem.

The occurrence of an NVM Subsystem Reset while power is applied to the domain is reported by the initial value of the CSTS.NSSRO field following the NVM Subsystem Reset. This field may be used by a host to

<!-- Embeded_Image 1, coordinate:(112,48,888,925) -->
===== page_number= 120, page_type= body ====

determine if the sudden loss of communication with a controller was due to an NVM Subsystem Reset or some other condition.

The ability for a host to initiate an NVM Subsystem Reset by writing to the NSSR.NSSRC field is an optional capability of a controller indicated by the state of the CAP.NSSRS field. An implementation may protect the domain from an inadvertent NVM Subsystem Reset by not providing this capability to one or more controllers that are in the domain.



![Embeded_Image 1](restored_images/Embeded_Image_1.png)
**Embeded_Image 1**


---

### 3.7.2 Controller Level Reset

The following methods initiate a Controller Level Reset (CLR):

- NVM Subsystem Reset;
- Controller Reset (i.e., the host writes the CC property to clear the CC.EN bit from ‘1’ to ‘0’);
- Cross-Controller Reset command (refer to section 5.4.3); and
- Transport specific reset types (refer to the applicable NVMe Transport binding specification), if any.

A CLR consists of the following actions:

- The controller stops processing any outstanding Admin or I/O commands;
- All I/O Submission Queues are deleted;
- All I/O Completion Queues are deleted;
- The controller is brought to an idle state. When this is complete, the CSTS.RDY bit is cleared to ‘0’; and
- All NVMe controller properties defined in either section 3.1.4 or the applicable NVMe Transport binding specification and all internal controller state are reset, with the following exceptions:

  - for memory-based controllers:

    - the following are not reset as part of a CLR initiated by a Controller Reset:
      - Admin Queue properties (i.e., AQA, ASQ, and ACQ);
      - Persistent Memory Region properties (i.e., PMRCAP, PMRCTL, PMRSTS, PMREBS, PMRSWTP, PMRMSCU, and PMRMSCL); and
      - The Controller Memory Buffer Memory Space Control property (CMBMSC);

    and

    - the following are not reset as part of a CLR initiated by a Function Level Reset:
      - the Controller Memory Buffer Memory Space Control property (CMBMSC);

    and

  - for message-based controllers:
    - there are no exceptions.

For all CLRs except those initiated by a Controller Reset, the controller properties defined by the transport (e.g., the PCIe registers defined by the PCIe Base Specification) are reset as defined by the applicable NVMe Transport binding specification (e.g., refer the NVMe over PCIe Transport Specification).

Upon completion of a CLR, if the media is not usable and an NVM Subsystem Shutdown that includes the controller is neither reported as in progress nor reported as complete (i.e., the CSTS.ST bit is cleared to ‘0’ or the CSTS.SHST field is cleared to 00b), then the controller is permitted to initialize the media for use.

To continue after a CLR, the host should:

- update transport specific state and controller property state as appropriate;
- set the CC.EN bit to ‘1’;
- wait for the CSTS.RDY bit to be set to ‘1’;
- configure the controller using Admin commands as needed;
- create I/O Completion Queues and I/O Submission Queues as needed; and
- proceed with normal I/O operations.


---

