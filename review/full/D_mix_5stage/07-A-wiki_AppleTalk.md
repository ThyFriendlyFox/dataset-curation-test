# 7. AppleTalk — Protocols

`A-wiki_AppleTalk` · [full/D_mix_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=AppleTalk&oldid=1365415813> · License: https://creativecommons.org/licenses/by-sa/4.0/

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | prompt | 40 | 0 | 0.01 | reconstructed |
| 1 | outline | 596 | 0 | 0.35 | reconstructed |
| 2 | rough_draft | 1329 | 0 | 0.73 | reconstructed |
| 3 | cited_draft | 1364 | 9 | 0.75 | reconstructed |
| 4 | final | 1294 | 9 | 1.00 | source |

<details><summary><b>Step 0 — prompt</b> (40 words)</summary>

````text
Write the "Protocols" section of an encyclopedia article on AppleTalk, with a short subsection for each protocol in the suite (address resolution, data stream, filing, session, transaction, datagram delivery, name binding, echo, printer access, routing table maintenance and zone information).
````

</details>

<details><summary><b>Step 1 — outline</b> (596 words)</summary>

````text
- AARP
  - resolves AppleTalk addresses to link layer addresses; functionally equivalent to ARP, very similar method
  - fairly simple: on power-on, broadcast AARP probe asking for a network address, hoping routers etc. answer
  - no answer -> pick random address from "base subnet", 0
  - broadcast "I am selecting this address", wait for complaints; if taken, pick another, repeat until free
  - many machines -> several tries; successful address saved in NVRAM, default in future
  - real-world setups (machines added a few at a time): one or two tries, address effectively constant
- ADSP
  - late addition; needed a TCP-style reliable connection-oriented transport
  - differences from TCP: connection attempt can be rejected
  - no "half-open" connections; one end tears down -> whole connection closed (full-duplex, not dual simplex)
  - attention messages: short messages bypassing normal stream; reliable but out of order; delivered asap, not waiting for current stream byte sequence point
- AFP
  - formerly AppleTalk Filing Protocol; talks to AppleShare file servers
  - built on ASP (legacy AFP over DDP) or Data Stream Interface (AFP over TCP)
  - user authentication (extensible, incl. two-way random-number exchange); Macintosh HFS filesystem operations
  - AFP over TCP in macOS until Big Sur; most other AppleTalk protocols removed in Snow Leopard
- ASP
  - intermediate protocol on top of ATP; foundation of AFP
  - requesting responses to arbitrary commands; out-of-band status queries
  - server can send asynchronous attention messages to client
- ATP
  - original reliable transport-level protocol, on top of DDP
  - full TCP-like protocol considered too expensive for most intended uses
  - simple request/response, no connection setup/teardown
  - one request -> up to eight response packets; requestor acks with bit mask of what arrived, responder retransmits rest
  - "at-least-once" vs "exactly-once" mode; exactly-once essential for non-idempotent ops
  - exactly-once: responder keeps response buffers until release packet or timeout; duplicates with same transaction ID get resent data, operation not redone
- DDP
  - lowest-level data-link-independent transport protocol; datagram service, no delivery guarantees
  - all application-level protocols on top, incl. NBP, RTMP, ZIP
  - corresponds closely to OSI Network layer
- NBP
  - dynamic, distributed system for managing names
  - service starts -> registers name chosen by human administrator; NBP checks nobody else has it
  - clients use NBP to query machines and find service
  - browsability ("what are the names of all the services available?") + find by name
  - names human-readable: spaces, upper/lower case, searching
- AEP
  - transport layer protocol for testing reachability of nodes
  - packet marked as AEP in Type field; passed to source DDP, forwarded, examined by destination DDP
  - copied, a field altered -> AEP reply, returned to source
- PAP
  - standard way to talk to PostScript printers; on top of ATP
  - on open, each end sends other an ATP request meaning "send me more data"
  - client answers with block of PostScript; server answers with diagnostic messages; then new "send-more-data" request
  - automatic flow control: only send when there's an outstanding ATP request
  - out-of-band status queries via separate ATP transactions; server answers status requests from any number of clients while busy
  - other Macs on LAN can show that printer is busy and with what job
- RTMP
  - routers keep each other informed about network topology
  - only part of AppleTalk needing periodic unsolicited broadcasts: every 10 seconds, list of network numbers known and how far away
- ZIP
  - associates network numbers with zone names
  - zone = human-meaningful subdivision (e.g. "Accounting Department")
  - network number = topologically contiguous section; zone can include several discontiguous portions
````

</details>

<details><summary><b>Step 2 — rough_draft</b> (1329 words)</summary>

````text
### AppleTalk Address Resolution Protocol

The AppleTalk Address Resolution Protocol (AARP) is used to resolve AppleTalk addresses to link layer addresses. It is basically the same thing as ARP, and it does the address resolution in a way that is very similar to ARP.

AARP is a pretty simple system. When an AppleTalk machine is powered on, it broadcasts an AARP probe packet that asks for a network address, and it expects to hear back from controllers like routers. If it does not get an address, it picks one at random from the "base subnet", 0. Then it broadcasts another packet that says "I am selecting this address", and it waits to see if anyone else on the network complains about it. If some other machine already has that address, the new machine picks a different address, and it keeps trying until it finds one that is free. When there are many machines on the network it can take several tries to find a free address, so to help performance the address that worked is stored in NVRAM and used as the default address from then on. In most real-world setups machines get added a few at a time, so only one or two tries are needed and after that the address is effectively constant.

### AppleTalk Data Stream Protocol

The AppleTalk Data Stream Protocol (ADSP) was added to the AppleTalk protocol suite fairly late, when it became clear that a reliable connection-oriented transport like TCP was needed. It was different from TCP in some significant ways:

A connection attempt could be rejected.

There were no "half-open" connections. Once one end started to tear down the connection, the whole connection was closed (so ADSP is full-duplex, not dual simplex).

AppleTalk included an attention message system that let short messages be sent so that they bypassed the normal stream data flow. These were delivered reliably, but out of order with respect to the stream. An attention message was delivered as soon as possible and did not wait for the current stream byte sequence point to become current.

### Apple Filing Protocol

The Apple Filing Protocol (AFP), which used to be called the AppleTalk Filing Protocol, is the protocol used to communicate with AppleShare file servers. It is built on top of AppleTalk Session Protocol (for legacy AFP over DDP) or on top of the Data Stream Interface (for AFP over TCP). It provides services for authenticating users, which can be extended to different authentication methods including two-way random-number exchange, and for doing operations that are specific to the Macintosh HFS filesystem. Most of the other AppleTalk protocols were removed in Snow Leopard, but AFP over TCP was still used in macOS until Big Sur.

### AppleTalk Session Protocol

The AppleTalk Session Protocol (ASP) was an intermediate protocol. It was built on top of AppleTalk Transaction Protocol (ATP), and it was the foundation of AFP. It gave basic services for requesting responses to arbitrary commands and for doing out-of-band status queries. It also let the server send asynchronous attention messages to the client.

### AppleTalk Transaction Protocol

The AppleTalk Transaction Protocol (ATP) was the original reliable transport-level protocol for AppleTalk, and it was built on top of DDP. When it was being developed, a full reliable connection-oriented protocol like TCP was thought to be too expensive to implement for most of the things AppleTalk was meant to be used for. So ATP was just a simple request/response exchange, and connections did not need to be set up or torn down.

One ATP request packet could get up to eight response packets as an answer. The requestor then sent back an acknowledgement packet with a bit mask that showed which response packets it had received, so that the responder could retransmit the rest.

ATP could work in either "at-least-once" mode or "exactly-once" mode. Exactly-once mode was essential for operations that were not idempotent. In this mode the responder kept a copy of the response buffers in memory until it successfully received a release packet from the requestor, or until a timeout ran out. That way, if a duplicate request came in with the same transaction ID, it could send the same response data again without doing the actual operation a second time.

### Datagram Delivery Protocol

The Datagram Delivery Protocol (DDP) was the lowest-level transport protocol that was independent of the data link. It gave a datagram service with no guarantees of delivery. All of the application-level protocols were built on top of DDP, including the infrastructure protocols NBP, RTMP and ZIP. AppleTalk's DDP corresponds closely to the Network layer of the Open Systems Interconnection (OSI) communication model.

### Name Binding Protocol

The Name Binding Protocol (NBP) was a dynamic and distributed system for managing AppleTalk names. When a service started up on a machine, it registered a name for itself, which was chosen by a human administrator. At that point NBP gave a way of checking that no other machine had already registered the same name. Later, when a client wanted to get to that service, it used NBP to query machines to find the service. NBP provided browsability ("what are the names of all the services available?") and it also provided the ability to find a service that had a particular name. Names were human-readable. They could have spaces and upper- and lower-case letters, and searching was supported.

### AppleTalk Echo Protocol

The AppleTalk Echo Protocol (AEP) was a transport layer protocol that was designed to test whether network nodes could be reached. AEP generates packets to send to the network node, and the packet is marked as an AEP packet in its Type field. First the packet is passed to the source DDP. After it is identified as an AEP packet it is forwarded to the node, and there the packet is examined by the DDP at the destination. After the packet is identified as an AEP packet, it is copied and a field in it is changed to make an AEP reply packet, and then it is sent back to the source node.

### Printer Access Protocol

The Printer Access Protocol (PAP) was the standard way to communicate with PostScript printers. It was built on top of ATP. When a PAP connection was opened, each end sent the other end an ATP request which basically meant "send me more data". The client responded to the server by sending a block of PostScript code, and the server could respond with any diagnostic messages that might come out of it, and after that another "send-more-data" request was sent. Using ATP this way gave automatic flow control, because each end could only send data to the other end if there was an outstanding ATP request it could respond to.

PAP also provided out-of-band status queries, and these were handled by separate ATP transactions. A PAP server could keep responding to status requests from any number of other clients even while it was busy with a print job from one client. Because of this, other Macintoshes on the LAN that were waiting to print could show status messages saying that the printer was busy and what job it was busy with.

### Routing Table Maintenance Protocol

The Routing Table Maintenance Protocol (RTMP) was the protocol routers used to keep each other informed about the topology of the network. It was the only part of AppleTalk that needed periodic unsolicited broadcasts. Every 10 seconds, each router had to send out a list of all the network numbers it knew about and how far away it thought they were.

### Zone Information Protocol

The Zone Information Protocol (ZIP) was the protocol that associated AppleTalk network numbers with zone names. A zone was a subdivision of the network that made sense to humans (for example, "Accounting Department"). But a network number had to be assigned to a topologically contiguous section of the network, while a zone could include several different discontiguous parts of the network.
````

</details>

<details><summary><b>Step 3 — cited_draft</b> (1364 words)</summary>

````text
### AppleTalk Address Resolution Protocol

The AppleTalk Address Resolution Protocol (AARP) is used to resolve AppleTalk addresses to link layer addresses.[1] It is basically the same thing as ARP, and it does the address resolution in a way that is very similar to ARP.[2]

AARP is a pretty simple system. When an AppleTalk machine is powered on, it broadcasts an AARP probe packet that asks for a network address, and it expects to hear back from controllers like routers. If it does not get an address, it picks one at random from the "base subnet", 0. Then it broadcasts another packet that says "I am selecting this address", and it waits to see if anyone else on the network complains about it. If some other machine already has that address, the new machine picks a different address, and it keeps trying until it finds one that is free.[3] When there are many machines on the network it can take several tries to find a free address, so to help performance the address that worked is stored in NVRAM and used as the default address from then on. In most real-world setups machines get added a few at a time, so only one or two tries are needed and after that the address is effectively constant.

### AppleTalk Data Stream Protocol

The AppleTalk Data Stream Protocol (ADSP) was added to the AppleTalk protocol suite fairly late, when it became clear that a reliable connection-oriented transport like TCP was needed. It was different from TCP in some significant ways:

A connection attempt could be rejected.

There were no "half-open" connections. Once one end started to tear down the connection, the whole connection was closed (so ADSP is full-duplex, not dual simplex).

AppleTalk included an attention message system that let short messages be sent so that they bypassed the normal stream data flow. These were delivered reliably, but out of order with respect to the stream. An attention message was delivered as soon as possible and did not wait for the current stream byte sequence point to become current.

### Apple Filing Protocol

The Apple Filing Protocol (AFP), which used to be called the AppleTalk Filing Protocol, is the protocol used to communicate with AppleShare file servers. It is built on top of AppleTalk Session Protocol (for legacy AFP over DDP) or on top of the Data Stream Interface (for AFP over TCP). It provides services for authenticating users, which can be extended to different authentication methods including two-way random-number exchange, and for doing operations that are specific to the Macintosh HFS filesystem. Most of the other AppleTalk protocols were removed in Snow Leopard, but AFP over TCP was still used in macOS until Big Sur.

### AppleTalk Session Protocol

The AppleTalk Session Protocol (ASP) was an intermediate protocol. It was built on top of AppleTalk Transaction Protocol (ATP), and it was the foundation of AFP. It gave basic services for requesting responses to arbitrary commands and for doing out-of-band status queries. It also let the server send asynchronous attention messages to the client.

### AppleTalk Transaction Protocol

The AppleTalk Transaction Protocol (ATP) was the original reliable transport-level protocol for AppleTalk, and it was built on top of DDP. When it was being developed, a full reliable connection-oriented protocol like TCP was thought to be too expensive to implement for most of the things AppleTalk was meant to be used for. So ATP was just a simple request/response exchange, and connections did not need to be set up or torn down.

One ATP request packet could get up to eight response packets as an answer. The requestor then sent back an acknowledgement packet with a bit mask that showed which response packets it had received, so that the responder could retransmit the rest.

ATP could work in either "at-least-once" mode or "exactly-once" mode. Exactly-once mode was essential for operations that were not idempotent. In this mode the responder kept a copy of the response buffers in memory until it successfully received a release packet from the requestor, or until a timeout ran out. That way, if a duplicate request came in with the same transaction ID, it could send the same response data again without doing the actual operation a second time.[4]

### Datagram Delivery Protocol

The Datagram Delivery Protocol (DDP) was the lowest-level transport protocol that was independent of the data link. It gave a datagram service with no guarantees of delivery. All of the application-level protocols were built on top of DDP, including the infrastructure protocols NBP, RTMP and ZIP. AppleTalk's DDP corresponds closely to the Network layer of the Open Systems Interconnection (OSI) communication model.

### Name Binding Protocol

The Name Binding Protocol (NBP) was a dynamic and distributed system for managing AppleTalk names. When a service started up on a machine, it registered a name for itself, which was chosen by a human administrator. At that point NBP gave a way of checking that no other machine had already registered the same name. Later, when a client wanted to get to that service, it used NBP to query machines to find the service. NBP provided browsability ("what are the names of all the services available?") and it also provided the ability to find a service that had a particular name.[1] Names were human-readable. They could have spaces and upper- and lower-case letters, and searching was supported.

### AppleTalk Echo Protocol

The AppleTalk Echo Protocol (AEP) was a transport layer protocol that was designed to test whether network nodes could be reached.[1] AEP generates packets to send to the network node, and the packet is marked as an AEP packet in its Type field. First the packet is passed to the source DDP. After it is identified as an AEP packet it is forwarded to the node, and there the packet is examined by the DDP at the destination. After the packet is identified as an AEP packet, it is copied and a field in it is changed to make an AEP reply packet, and then it is sent back to the source node.

### Printer Access Protocol

The Printer Access Protocol (PAP) was the standard way to communicate with PostScript printers. It was built on top of ATP.[1] When a PAP connection was opened, each end sent the other end an ATP request which basically meant "send me more data". The client responded to the server by sending a block of PostScript code, and the server could respond with any diagnostic messages that might come out of it, and after that another "send-more-data" request was sent. Using ATP this way gave automatic flow control, because each end could only send data to the other end if there was an outstanding ATP request it could respond to.

PAP also provided out-of-band status queries, and these were handled by separate ATP transactions. A PAP server could keep responding to status requests from any number of other clients even while it was busy with a print job from one client. Because of this, other Macintoshes on the LAN that were waiting to print could show status messages saying that the printer was busy and what job it was busy with.

### Routing Table Maintenance Protocol

The Routing Table Maintenance Protocol (RTMP) was the protocol routers used to keep each other informed about the topology of the network.[1] It was the only part of AppleTalk that needed periodic unsolicited broadcasts. Every 10 seconds, each router had to send out a list of all the network numbers it knew about and how far away it thought they were.

### Zone Information Protocol

The Zone Information Protocol (ZIP) was the protocol that associated AppleTalk network numbers with zone names.[1] A zone was a subdivision of the network that made sense to humans (for example, "Accounting Department"). But a network number had to be assigned to a topologically contiguous section of the network, while a zone could include several different discontiguous parts of the network.

References:
[1] (2010-02-02). AppleTalk Overview. Cisco. https://www.cisco.com/c/en/us/td/docs/ios/at/configuration/guide/12_2sx/atk_12_2sx_book/overview_appletalk.pdf
[2] AppleTalk Address Resolution Protocol. DevX. https://www.devx.com/terms/appletalk-address-resolution-protocol/
[3] Faas, Ryan. (2005-03-15). Inside the Mac OS: A look at AppleTalk and zones. Macworld. https://www.macworld.com/article/174889/appletalk.html
[4] AppleTalk Transaction Protocol. https://developer.apple.com/library/archive/documentation/mac/pdf/Networking/ATP.pdf
````

</details>

<details><summary><b>Step 4 — final</b> (1294 words)</summary>

````text
### AppleTalk Address Resolution Protocol

The AppleTalk Address Resolution Protocol (AARP) resolves AppleTalk addresses to link layer addresses.[1] It is functionally equivalent to ARP and obtains address resolution by a method very similar to ARP.[2]

AARP is a fairly simple system. When powered on, an AppleTalk machine broadcasts an AARP probe packet asking for a network address, intending to hear back from controllers such as routers. If no address is provided, one is picked at random from the "base subnet", 0. It then broadcasts another packet saying "I am selecting this address", and then waits to see if anyone else on the network complains. If another machine has that address, the newly connecting machine will pick another address, and keep trying until it finds a free one.[3] On a network with many machines it may take several tries before a free address is found, so for performance purposes the successful address is recorded in NVRAM and used as the default address in the future. This means that in most real-world setups where machines are added a few at a time, only one or two tries are needed before the address effectively becomes constant.

### AppleTalk Data Stream Protocol

The AppleTalk Data Stream Protocol (ADSP) was a comparatively late addition to the AppleTalk protocol suite, done when it became clear that a TCP-style reliable connection-oriented transport was needed. Significant differences from TCP were that:

A connection attempt could be rejected.

There were no "half-open" connections; once one end initiated a tear-down of the connection, the whole connection would be closed (i.e., ADSP is full-duplex, not dual simplex).

AppleTalk had an included attention message system which allowed short messages to be sent which would bypass the normal stream data flow. These were delivered reliably but out of order with respect to the stream. Any attention message would be delivered as soon as possible instead of waiting for the current stream byte sequence point to become current.

### Apple Filing Protocol

The Apple Filing Protocol (AFP), formerly AppleTalk Filing Protocol, is the protocol for communicating with AppleShare file servers. Built on top of AppleTalk Session Protocol (for legacy AFP over DDP) or the Data Stream Interface (for AFP over TCP), it provides services for authenticating users (extensible to different authentication methods including two-way random-number exchange) and for performing operations specific to the Macintosh HFS filesystem. AFP over TCP remained in use in macOS until Big Sur, even though most other AppleTalk protocols were removed in Snow Leopard.

### AppleTalk Session Protocol

The AppleTalk Session Protocol (ASP) was an intermediate protocol, built on top of AppleTalk Transaction Protocol (ATP), which in turn was the foundation of AFP. It provided basic services for requesting responses to arbitrary commands and performing out-of-band status queries. It also allowed the server to send asynchronous attention messages to the client.

### AppleTalk Transaction Protocol

The AppleTalk Transaction Protocol (ATP) was the original reliable transport-level protocol for AppleTalk, built on top of DDP. At the time it was being developed, a full, reliable connection-oriented protocol like TCP was considered to be too expensive to implement for most of the intended uses of AppleTalk. Thus, ATP was a simple request/response exchange, with no need to set up or tear down connections.

An ATP request packet could be answered by up to eight response packets. The requestor then sent an acknowledgement packet containing a bit mask indicating which of the response packets it received, so the responder could retransmit the remainder.

ATP could operate in either "at-least-once" mode or "exactly-once" mode. Exactly-once mode was essential for operations which were not idempotent; in this mode, the responder kept a copy of the response buffers in memory until successful receipt of a release packet from the requestor, or until a timeout elapsed. This way, it could respond to duplicate requests with the same transaction ID by resending the same response data, without performing the actual operation again.[4]

### Datagram Delivery Protocol

The Datagram Delivery Protocol (DDP) was the lowest-level data-link-independent transport protocol. It provided a datagram service with no guarantees of delivery. All application-level protocols, including the infrastructure protocols NBP, RTMP and ZIP, were built on top of DDP. AppleTalk's DDP corresponds closely to the Network layer of the Open Systems Interconnection (OSI) communication model.

### Name Binding Protocol

The Name Binding Protocol (NBP) was a dynamic, distributed system for managing AppleTalk names. When a service started up on a machine, it registered a name for itself as chosen by a human administrator. At this point, NBP provided a system for checking that no other machine had already registered the same name. Later, when a client wanted to access that service, it used NBP to query machines to find that service. NBP provided browsability ("what are the names of all the services available?") as well as the ability to find a service with a particular name.[1] Names were human-readable, containing spaces and upper- and lower-case letters, and including support for searching.

### AppleTalk Echo Protocol

The AppleTalk Echo Protocol (AEP) was a transport layer protocol designed to test the reachability of network nodes.[1] AEP generates packets to be sent to the network node and is identified in the Type field of a packet as an AEP packet. The packet is first passed to the source DDP. After it is identified as an AEP packet, it is forwarded to the node where the packet is examined by the DDP at the destination. After the packet is identified as an AEP packet, the packet is then copied and a field in the packet is altered to create an AEP reply packet, and is then returned to the source node.

### Printer Access Protocol

The Printer Access Protocol (PAP) was the standard way of communicating with PostScript printers. It was built on top of ATP.[1] When a PAP connection was opened, each end sent the other an ATP request which basically meant "send me more data". The client's response to the server was to send a block of PostScript code, while the server could respond with any diagnostic messages that might be generated as a result, after which another "send-more-data" request was sent. This use of ATP provided automatic flow control; each end could only send data to the other end if there was an outstanding ATP request to respond to.

PAP also provided for out-of-band status queries, handled by separate ATP transactions. Even while it was busy servicing a print job from one client, a PAP server could continue to respond to status requests from any number of other clients. This allowed other Macintoshes on the LAN that were waiting to print to display status messages indicating that the printer was busy, and what the job was that it was busy with.

### Routing Table Maintenance Protocol

The Routing Table Maintenance Protocol (RTMP) was the protocol by which routers kept each other informed about the topology of the network.[1] This was the only part of AppleTalk that required periodic unsolicited broadcasts: every 10 seconds, each router had to send out a list of all the network numbers it knew about and how far away it thought they were.

### Zone Information Protocol

The Zone Information Protocol (ZIP) was the protocol by which AppleTalk network numbers were associated with zone names.[1] A zone was a subdivision of the network that made sense to humans (for example, "Accounting Department"); but while a network number had to be assigned to a topologically contiguous section of the network, a zone could include several different discontiguous portions of the network.

References:
[1] (2010-02-02). AppleTalk Overview. Cisco. https://www.cisco.com/c/en/us/td/docs/ios/at/configuration/guide/12_2sx/atk_12_2sx_book/overview_appletalk.pdf
[2] AppleTalk Address Resolution Protocol. DevX. https://www.devx.com/terms/appletalk-address-resolution-protocol/
[3] Faas, Ryan. (2005-03-15). Inside the Mac OS: A look at AppleTalk and zones. Macworld. https://www.macworld.com/article/174889/appletalk.html
[4] AppleTalk Transaction Protocol. https://developer.apple.com/library/archive/documentation/mac/pdf/Networking/ATP.pdf
````

</details>
