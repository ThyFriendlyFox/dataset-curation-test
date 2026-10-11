# 8. Byzantine fault

`B-Byzantine_fault` · [B_wiki_history_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Byzantine_fault&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 614 revisions in history; 38 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | revision_1 | 359 | 0 | 0.12 | enwiki rev 5757207 (2004-09-08) |
| 2 | revision_2 | 470 | 0 | 0.16 | enwiki rev 22715788 (2005-09-06) |
| 3 | revision_3 | 1444 | 15 | 0.22 | enwiki rev 642311550 (2015-01-13) |
| 4 | revision_4 | 2254 | 32 | 0.34 | enwiki rev 703021728 (2016-02-03) |
| 5 | revision_5 | 2749 | 37 | 0.41 | enwiki rev 1125034931 (2022-12-01) |
| 6 | revision_6 | 3054 | 38 | 0.86 | enwiki rev 1244996099 (2024-09-10) |
| 7 | revision_7 | 3350 | 43 | 0.93 | enwiki rev 1358110069 (2026-06-06) |
| 8 | final | 3151 | 41 | 1.00 | enwiki rev 1362230504 (2026-07-02) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Byzantine fault
````

</details>

<details><summary><b>Step 1 — revision_1</b> (359 words)</summary>

````text
## Byzantine Fault Tolerance

The Byzantine Generals problem and several solutions were originally described by Lamport, Shostak, and Pease in ACM Transaction on Progamming Languages and Systems in 1982.

The Byzantine Generals problem describes a group of generals, each commanding a division of the Byzantine army, encircling a city. These generals wish to formulate a plan for attacking the city. In its simplest form, the generals must only decide whether to attack or retreat. Some generals may prefer to attack, while others prefer to retreat. The important thing is that every general agrees on a common decision, for a halfhearted attack by a few generals would be worse than a coordinated attack or a coordinated retreat.

The problem is made difficult by the presence of traitorous generals who may not only give out false information, they may do so selectively. For instance, if nine generals are voting what to do, four of whom support attacking while four others are in favor of retreat, the ninth general may give a vote of retreat to a few generals and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers).

Byzantine fault tolerance can be achieved if the loyal generals compare notes and disregard conficting information.

More generally, a Byzantine fault is one in which a component of some system not only behaves erroneously, but also behaves inconsistently. Correctly functioning components of a Byzantine fault tolerant system will behave consistently regardless of Byzantine faulty components.

## Solutions

Lamport, Shostak, and Pease propose several solutions. One allows messages to be forged, and is Byzantine Fault Tolerant as long as the number of traitorous generals does not exceed roughly one third.

A second solution requires unforgeable signatures (in modern computer systems, this may be achieved through public key cryptography), but maintains Byzantine Fault Tolerance in the presence of an arbitrary number of traitorous generals.

Also presented is a variation on the first two solutions allowing Byzantine Fault Tolerant behavior in some situations where not all generals can communicate directly with each other.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (470 words)</summary>

````text
The Byzantine Generals problem and several solutions were originally described by Lamport, Shostak, and Pease in ACM Transaction on Progamming Languages and Systems in 1982 (see References).

The Byzantine Generals problem describes a group of generals, each commanding a division of the Byzantine army, encircling a city. These generals wish to formulate a plan for attacking the city. In its simplest form, the generals must only decide whether to attack or retreat. Some generals may prefer to attack, while others prefer to retreat. The important thing is that every general agrees on a common decision, for a halfhearted attack by a few generals would be worse than a coordinated attack or a coordinated retreat.

The problem is made difficult by the presence of traitorous generals who may not only cast a vote for a suboptimal strategy, they may do so selectively. For instance, if nine generals are voting, four of whom support attacking while four others are in favor of retreat, the ninth general may give a vote of retreat to a few generals and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers).

Byzantine fault tolerance can be achieved if the loyal generals have a strategy to compare notes with each other such that conflicting information is disregarded.

More generally, a Byzantine fault is one in which a component of some system not only behaves erroneously, but also fails to behave consistently when interacting with multiple other components. Correctly functioning components of a Byzantine fault tolerant system will be able to reach the same group decisions regardless of Byzantine faulty components.

## Solutions

Lamport, Shostak, and Pease propose several solutions. They begin by noting that the Generals Problem can be reduced to solving a Commander and Lieutenants problem where Loyal Lieutenants must all act in unison and that their action must correspond to what the Commander ordered in the case that the Commander is Loyal. Roughly speaking, the Generals vote by treating each others orders as votes.

One allows scenarios in which messages may be forged, and is Byzantine Fault Tolerant as long as the number of traitorous generals does not equal or exceed one third. The impossibility of dealing with one-third or more traitors ultimately reduces to proving that the 1 Commander + 2 Lieutenants problem cannot be solved if the Commander is traitorous.

A second solution requires unforgeable signatures (in modern computer systems, this may be achieved through public key cryptography), but maintains Byzantine Fault Tolerance in the presence of an arbitrary number of traitorous generals.

Also presented is a variation on the first two solutions allowing Byzantine Fault Tolerant behavior in some situations where not all generals can communicate directly with each other.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (1444 words)</summary>

````text
In fault-tolerant computer systems, Byzantine fault tolerance is a sub-field of fault tolerance research inspired by the Byzantine Generals' Problem, which is a generalized version of the Two Generals' Problem.

The objective of Byzantine fault tolerance is to be able to defend against Byzantine failures, in which components of a system fail in arbitrary ways (i.e., not just by stopping or crashing but by processing requests incorrectly, corrupting their local state, and/or producing incorrect or inconsistent outputs). Correctly functioning components of a Byzantine fault tolerant system will be able to correctly provide the system's service assuming there are not too many Byzantine faulty components.

## Failure modes

A Byzantine fault is an arbitrary fault that occurs during the execution of an algorithm by a distributed system. It encompasses both omission failures (e.g., crash failures, failing to receive a request, or failing to send a response) and commission failures (e.g., processing a request incorrectly, corrupting local state, and/or sending an incorrect or inconsistent response to a request). When a Byzantine failure has occurred, the system may respond in any unpredictable way, unless it is designed to have Byzantine fault tolerance.

For example, if the output of one function is the input of another, then small round-off errors in the first function can produce much larger errors in the second. If the second function were fed into a third, the problem could grow even larger, until the values produced are worthless. Another example is in compiling source code. One minor syntactical error early on in the code can produce large numbers of perceived errors later, as the parser of the compiler gets out-of-phase with the lexical and syntactic information in the source program. Such failures have brought down major Internet services. For example, in 2008 Amazon S3 was brought down for several hours when a single-bit hardware error propagated through the system.[1]

In a Byzantine fault tolerant (BFT) algorithm, steps are taken by processes, the logical abstractions that represent the execution path of the algorithms. A faulty process is one that at some point exhibits any of the above failures. A process that is not faulty is correct.

The Byzantine failure assumption models real-world environments in which computers and networks may behave in unexpected ways due to hardware failures, network congestion and disconnection, as well as malicious attacks. Byzantine failure-tolerant algorithms must cope with such failures and still satisfy the specifications of the problems they are designed to solve. Such algorithms are commonly characterized by their resilience t, the number of faulty processes with which an algorithm can cope.

Many classic agreement problems, such as the Byzantine Generals' Problem, have no solution unless n ≥ 3t + 1, where n is the number of processes in the system and t is the number of traitors (faults). In other words, the algorithm can ensure correct operation only if fewer than one third of the processes are faulty.

## Origin

Byzantine refers to the Byzantine Generals' Problem, an agreement problem (first proposed by Marshall Pease, Robert Shostak, and Leslie Lamport in their 1980 paper, "Reaching Agreement in the Presence of Faults") in which generals of the Byzantine Empire's army must decide unanimously whether to attack some enemy army. (The Byzantine Army was chosen as an example for the problem as the Byzantine state experienced frequent treachery in the high levels of its administration.) The problem is complicated by the geographic separation of the generals who must communicate by sending messengers to each other, and by the presence of traitors amongst the generals. These traitors can act arbitrarily in order to achieve the following aims: trick some generals into attacking; force a decision that is not consistent with the generals' desires, e.g. forcing an attack when no general wishes to attack; or confusing some generals to the point that they are unable to make up their minds. If the traitors succeed in any of these goals any resulting attack is doomed, as only a concerted effort can result in victory.

Byzantine fault tolerance can be achieved if the loyal (non-faulty) generals have a unanimous agreement on their strategy. Note that if the source general is correct, all loyal generals must agree upon that value; otherwise, the choice of strategy agreed upon is irrelevant.

## Early solutions

Several solutions were originally described by Lamport, Shostak, and Pease in 1982. They began by noting that the Generals' Problem can be reduced to solving a "Commander and Lieutenants" problem where Loyal Lieutenants must all act in unison and that their action must correspond to what the Commander ordered in the case that the Commander is Loyal. Roughly speaking, the Generals vote by treating each other's orders as votes.

One solution considers scenarios in which messages may be forged, but which will be Byzantine-fault-tolerant as long as the number of traitorous generals does not equal or exceed one third. The impossibility of dealing with one-third or more traitors ultimately reduces to proving that the 1 Commander/2 Lieutenants problem cannot be solved, if the Commander is traitorous. To see this, suppose we have a traitorous Commander A, and two Lieutenants, B and C: when A tells B to attack and C to retreat, and B and C send messages to each other, forwarding A's message, neither B nor C can figure out who is the traitor, since it isn't necessarily A—the other commander could have forged the message purportedly from A. It can be shown that if n is the number of generals in total, and t is the number of traitors in that n, then there are solutions to the problem only when n > 3t.[2]

A second solution requires unforgeable signatures (in modern computer systems, this may be achieved in practice using public-key cryptography), but maintains Byzantine fault tolerance in the presence of an arbitrary number of traitorous generals.

Also presented is a variation on the first two solutions allowing Byzantine-fault-tolerant behavior in some situations where not all generals can communicate directly with each other.

## Practical Byzantine fault tolerance

Byzantine fault tolerant replication protocols were long considered too expensive to be practical. Then in 1999, Miguel Castro and Barbara Liskov introduced the "Practical Byzantine Fault Tolerance" (PBFT) algorithm,[3] which provides high-performance Byzantine state machine replication, processing thousands of requests per second with sub-millisecond increases in latency.

PBFT triggered a renaissance in BFT replication research, with protocols like Q/U,[4] HQ,[5] Zyzzyva,[6] and ABsTRACTs [7] working to lower costs and improve performance and protocols like Aardvark[8] and RBFT[9] working to improve robustness.

UpRight[10] is an open source library for constructing services that tolerate both crashes ("up") and Byzantine behaviors ("right") that incorporates many of these protocols' innovations.

One example of BFT in use is Bitcoin, a peer-to-peer digital currency system. The Bitcoin network works in parallel to generate a chain of Hashcash style proof-of-work. The proof-of-work chain is the key to overcome Byzantine failures and to reach a coherent global view of the system state.[11] Hyperledger utilizes PBFT to achieve similar results to Bitcoin but with known entities operating the consensus nodes.[12]

Additionally to PBFT and Upright, there is also the BFT-SMaRt library,[13] a high-performance Byzantine fault-tolerant state machine replication library developed in Java. This library implements a protocol very similar to PBFT's, plus complementary protocols which offer state transfer and on-the-fly reconfiguration of hosts. BFT-SMaRt is the most recent effort to implement state machine replication, still being actively maintained.

Archistar[14] utilizes a slim BFT layer[15] for communication. It prototypes a secure multi-cloud storage system within Java using GPLv2. Focus lies on simplicity and readability, it aims to be the foundation for further research projects.

References:
[1] (July 20, 2008). S3 Availability Event. Amazon. http://status.aws.amazon.com/s3-20080720.html
[2] Feldman, P.. (1997). An optimal probabilistic protocol for synchronous Byzantine agreement. SIAM J. Computing. doi:10.1137/s0097539790187084
[3] Castro, M.. (2002). Practical Byzantine Fault Tolerance and Proactive Recovery. ACM Transactions on Computer Systems. doi:10.1145/571637.571640
[4] Abd-El-Malek. (2005). Fault-scalable Byzantine Fault-Tolerant Services. Association for Computing Machinery. doi:10.1145/1095809.1095817
[5] Cowling, James. (2006). HQ Replication: A Hybrid Quorum Protocol for Byzantine Fault Tolerance. http://portal.acm.org/citation.cfm?id=1298455.1298473
[6] Kotla, Ramakrishna. (December 2009). Zyzzyva: Speculative Byzantine Fault Tolerance. ACM Transactions on Computer Systems. doi:10.1145/1658357.1658358
[7] Guerraoui, Rachid. (2010). The Next 700 BFT Protocols. EuroSys. http://infoscience.epfl.ch/record/144158
[8] Clement, A.. (April 22–24, 2009). Making Byzantine Fault Tolerant Systems Tolerate Byzantine Faults. USENIX. http://www.usenix.org/events/nsdi09/tech/full_papers/clement/clement.pdf
[9] Aublin, P.-L.. (July 8–11, 2013). RBFT: Redundant Byzantine Fault Tolerance. International Conference on Distributed Computing Systems. http://www.temple.edu/cis/icdcs2013/program.html
[10] UpRight. Google Code repository for the UpRight replication library.
[11] bitcointalk.org The Byzantine Generals' Problem
[12] hyperledger.com Hyperledger
[13] BFT-SMaRt. Google Code repository for the BFT-SMaRt replication library.
[14] Archistar. github repository for the Archistar project.
[15] Archistar-bft BFT state-machine. github repository for the Archistar project.
````

</details>

<details><summary><b>Step 4 — revision_4</b> (2254 words)</summary>

````text
In fault-tolerant computer systems, and in particular distributed computing systems, Byzantine fault tolerance

is the characteristic of a system that tolerates the class of failures known as the Byzantine Generals' Problem,[1] which is a generalized version of the

Two Generals' Problem - for which there is an unsolvability proof. The phrases interactive consistency or source congruency have been used to refer to Byzantine fault tolerance, particularly among the members of some early implementation teams.[2]

The objective of Byzantine fault tolerance is to be able to defend against Byzantine failures, in which components of a system fail with symptoms that prevent some components of the system from reaching agreement among themselves, where such agreement is needed for the correct operation of the system. Correctly functioning components of a Byzantine fault tolerant system will be able to provide the system's service, assuming there are not too many faulty components.

The following practical, concise definitions are helpful in understanding Byzantine fault tolerance:[3,4]

Byzantine fault

Any fault presenting different symptoms to different observers

Byzantine failure

The loss of a system service due to a Byzantine fault in systems that require consensus

The terms fault and failure are used here according to the standard definitions[5]

originally created by a joint committee on "Fundamental Concepts and Terminology" formed by the IEEE Computer Society's Technical Committee on Dependable Computing and Fault-Tolerance and IFIP Working Group 10.4 on Dependable Computing and Fault Tolerance.[6] A version of these definitions is also described in the Dependability Wikipedia page. The type of system services which Byzantine faults affect are agreement (a.k.a consensus) services.

## Origin

Byzantine refers to the Byzantine Generals' Problem, an agreement problem (described by Leslie Lamport, Robert Shostak and Marshall Pease in their 1982 paper, "The Byzantine Generals Problem")[1] in which a group of generals, each commanding

a portion of the Byzantine army, encircle a city. These generals wish to formulate a plan for attacking the city. In its simplest form, the generals must only decide whether to attack or retreat. Some generals may prefer to attack, while others prefer to retreat. The important thing is that every general agrees on a common decision, for a halfhearted attack by a few generals would become a rout and be worse than a coordinated attack or a coordinated retreat.

The problem is complicated by the presence of traitorous generals who may not only cast a vote for a suboptimal strategy, they may do so selectively. For instance, if nine generals are voting, four of whom support attacking while four others are in favor of retreat, the ninth general may send a vote of retreat to those generals in favor of retreat, and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers). The problem is complicated further by the generals being physically separated and must send their votes via messengers who may fail to deliver votes or may forge false votes.

Byzantine fault tolerance can be achieved if the loyal (non-faulty) generals have a unanimous agreement on their strategy. Note that there can be a default vote value given to missing messages. For example, missing messages can be given the value <Null>. Further, if the agreement is that the <Null> votes are in the majority, a pre-assigned default strategy can be used (e.g., retreat).

The typical mapping of this story on to computer systems is that the computers are the generals and their digital communication system links are the messengers.

## Known examples of Byzantine failures

Several examples of Byzantine failures that have occurred are given in two equivalent journal

papers.[3,4]

These and other examples are described on the NASA DASHlink web pages.[7] These web pages also describe some phenomenology that can cause Byzantine faults.

Byzantine errors were observed infrequently and at irregular points during endurance testing for the New Virginia Class submarine.[8]

## Early solutions

Several solutions were described by Lamport, Shostak, and Pease in 1982.[1] They began by noting that the Generals' Problem can be reduced to solving a "Commander and Lieutenants" problem where loyal Lieutenants must all act in unison and that their action must correspond to what the Commander ordered in the case that the Commander is loyal.

One solution considers scenarios in which messages may be forged, but which will be Byzantine-fault-tolerant as long as the number of traitorous generals does not equal or exceed one third of the generals. The impossibility of dealing with one-third or more traitors ultimately reduces to proving that the one Commander and two Lieutenants problem cannot be solved, if the Commander is traitorous. To see this, suppose we have a traitorous Commander A, and two Lieutenants, B and C: when A tells B to attack and C to retreat, and B and C send messages to each other, forwarding A's message, neither B nor C can figure out who is the traitor, since it is not necessarily A—another Commander could have forged the message purportedly from A. It can be shown that if n is the number of generals in total, and t is the number of traitors in that n, then there are solutions to the problem only when n > 3t and the communication is synchronous (bounded delay).[9]

A second solution requires unforgeable message signatures. For security-critical systems, digital signatures (in modern computer systems, this may be achieved in practice using public-key cryptography) can provide Byzantine fault tolerance in the presence of an arbitrary number of traitorous generals. However, for safety-critical systems, simple error detecting codes, such as CRCs, provide the same or better coverage at a much lower cost. This is true for both Byzantine and non-Byzantine faults. Thus, cryptographic digital signature methods are not a good choice for safety-critical systems, unless there is also a specific security threat as well.[10] While error detecting codes, such as CRCs, are better than cryptographic techniques, neither provide adequate coverage for active electronics in safety-critical systems. This is illustrated by the Schrödinger CRC scenario where a CRC-protected message with a single Byzantine faulty bit presents different data to different observers and each observer sees a valid CRC.[3,4]

Also presented is a variation on the first two solutions allowing Byzantine-fault-tolerant behavior in some situations where not all generals can communicate directly with each other.

Several system architectures were designed c. 1980 that implemented Byzantine fault tolerance. These include: Draper's FTMP,[11]

Honeywell's MMFCS,[12]

and SRI's SIFT.[13]

## Practical Byzantine fault tolerance

In 1999, Miguel Castro and Barbara Liskov introduced the "Practical Byzantine Fault Tolerance" (PBFT) algorithm,[14] which provides high-performance Byzantine state machine replication, processing thousands of requests per second with sub-millisecond increases in latency.

PBFT triggered a renaissance in Byzantine fault tolerant replication research, with protocols like Q/U,[15]

HQ,[16]

Zyzzyva,[17]

and ABsTRACTs[18]

working to lower costs and improve performance and protocols like Aardvark[19]

and RBFT[20]

working to improve robustness.

## Byzantine fault tolerance example

In computer system, when the processor and devices suffer from a malicious failure, and give an aggregate output, this type of failure is called Byzantine failure.

Suppose we have one server, and two processors named as P1 and P2. The processors know the temperature of the sensor using a communication link. The processor P1 gets the information from a sensor have a temperature 25° C and processor P2 gets the information from the sensor is 45° C. So there is a fault occurring in this system.

Problem: Sensor informs the processor P1 a temperature 25° C and processor P2 the temperature 45° C. So we don’t know the actual problem in this system. We don’t know whether the problem is is n processor P1 or processor P2.

So to solve this problem, we use a Byzantine algorithm. It has three main parts Byz (N,M). Here N is the number of receiver, M is the fault.

Byz (N,M) algorithm

Step 1: The original source sends information to the receiver.

Step 2: If M > 0, the original source sends the information to the receiver (N-1), then original source (N-1) sends the information to its successor [N-1, M-1].

Step 3: If M = 0, bypass the step.

Step 4: In step 4, we use a voter, for a majority voting rates, and in voter, suppose we use processors P1, P2 and P3 which perform the same function, then we check output of these processors. If the processor fails, then other can continue to carry the operation of the system function.

Output is given by the majority of the voters.

Advantage: It gives the accurate output high accurate quality of the result.

## Byzantine fault tolerance software

UpRight[21] is an open source library for constructing services that tolerate both crashes ("up") and Byzantine behaviors ("right") that incorporates many of these protocols' innovations.

In addition to PBFT and Upright, there is the BFT-SMaRt library,[22] a high-performance Byzantine fault-tolerant state machine replication library developed in Java. This library implements a protocol very similar to PBFT's, plus complementary protocols which offer state transfer and on-the-fly reconfiguration of hosts. BFT-SMaRt is the most recent effort to implement state machine replication, still being actively maintained.

Archistar[23] utilizes a slim BFT layer[24] for communication. It prototypes a secure multi-cloud storage system using Java licensed under LGPLv2. Focus lies on simplicity and readability, it aims to be the foundation for further research projects.

Askemos [25] is a concurrent, garbage-collected, persistent programming platform atop of replicated state machines which tolerates byzantine faults. It prototypes an execution environment facilitating Smart contracts.

## Byzantine fault tolerance in practice

One example of BFT in use is bitcoin, a peer-to-peer digital currency system. The bitcoin network works in parallel to generate a chain of Hashcash style proof-of-work. The proof-of-work chain is the key to overcome Byzantine failures and to reach a coherent global view of the system state.

Some aircraft systems, such as the Boeing 777 Aircraft Information Management System (via its ARINC 659 SAFEbus® network),[26,27]

the Boeing 777 flight control system,[28]

and the Boeing 787 flight control systems, use Byzantine fault tolerance. Because these are real-time systems, their Byzantine fault tolerance solutions must have very low latency. For example, SAFEbus can achieve Byzantine fault tolerance with on the order of a microsecond of added latency.

Some spacecraft such as the SpaceX Dragon flight system and the NASA Crew Exploration Vehicle consider Byzantine fault tolerance in their design.

Byzantine fault tolerance mechanisms use components that repeat an incoming message (or just its signature) to other recipients of that incoming message. All these mechanisms make the assumption that the act of repeating a message blocks the propagation of Byzantine symptoms. For systems that have a high degree of safety or security criticality, these assumptions must be proven to be true to an acceptable level of fault coverage. When providing proof through testing, one difficulty is creating a sufficiently wide range of signals with Byzantine symptoms.[29] Such testing likely will require specialized fault injectors.[30,31]

References:
[1] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[2] Kirrmann, Hubert. (n.d.). Fault Tolerant Computing in Industrial Automation. ABB Research Center. http://lamspeople.epfl.ch/kirrmann/Pubs/FaultTolerance/Fault_Tolerance_Tutorial_HK.pdf#page=94
[3] Driscoll, K.. (2004). The Real Byzantine Generals. doi:10.1109/DASC.2004.1390734
[4] Driscoll, Kevin. (2003). Byzantine Fault Tolerance, from Theory to Reality. doi:10.1007/978-3-540-39878-3_19
[5] Avizienis, A.. (2004). Basic concepts and taxonomy of dependable and secure computing. IEEE Transactions on Dependable and Secure Computing. doi:10.1109/TDSC.2004.2
[6] Dependable Computing and Fault Tolerance. http://www.dependability.org
[7] Driscoll, Kevin. (2012-12-11). Real System Failures. DASHlink. https://c3.nasa.gov/dashlink/resources/624/
[8] Walter, C.. (2005). The Reliable Platform Service: A Property-Based Fault Tolerant Service Architecture. doi:10.1109/HASE.2005.23
[9] Feldman, P.. (1997). An optimal probabilistic protocol for synchronous Byzantine agreement. SIAM J. Computing. doi:10.1137/s0097539790187084
[10] Paulitsch, M.. (2005). Coverage and the Use of Cyclic Redundancy Codes in Ultra-Dependable Systems. doi:10.1109/DSN.2005.31
[11] Hopkins, Albert L.. (1987). The Evolution of Fault Tolerant Computing at the Charles Stark Draper Laboratory, 1955–85. doi:10.1007/978-3-7091-8871-2_6
[12] Driscoll, Kevin. (1984). Multi-Microprocessor Flight Control System. AFWAL/FIGL U.S. Air Force Systems Command.
[13] (1979). SIFT: design and analysis of a fault-tolerant computer for aircraft control. Microelectronics Reliability. doi:10.1016/0026-2714(79)90211-7
[14] Castro, M.. (2002). Practical Byzantine Fault Tolerance and Proactive Recovery. ACM Transactions on Computer Systems. doi:10.1145/571637.571640
[15] Abd-El-Malek. (2005). Fault-scalable Byzantine Fault-Tolerant Services. Association for Computing Machinery. doi:10.1145/1095809.1095817
[16] Cowling, James. (2006). HQ Replication: A Hybrid Quorum Protocol for Byzantine Fault Tolerance. http://portal.acm.org/citation.cfm?id=1298455.1298473
[17] Kotla, Ramakrishna. (December 2009). Zyzzyva: Speculative Byzantine Fault Tolerance. ACM Transactions on Computer Systems. doi:10.1145/1658357.1658358
[18] Guerraoui, Rachid. (2010). The Next 700 BFT Protocols. EuroSys. http://infoscience.epfl.ch/record/144158
[19] Clement, A.. (April 22–24, 2009). Making Byzantine Fault Tolerant Systems Tolerate Byzantine Faults. USENIX. http://www.usenix.org/events/nsdi09/tech/full_papers/clement/clement.pdf
[20] Aublin, P.-L.. (July 8–11, 2013). RBFT: Redundant Byzantine Fault Tolerance. International Conference on Distributed Computing Systems. http://www.temple.edu/cis/icdcs2013/program.html
[21] UpRight. Google Code repository for the UpRight replication library.
[22] BFT-SMaRt. Google Code repository for the BFT-SMaRt replication library.
[23] Archistar. github repository for the Archistar project.
[24] Archistar-bft BFT state-machine. github repository for the Archistar project.
[25] Askemos/BALL project home page
[26] M., Paulitsch. (9 January 2015). Industrial Communication Technology Handbook, Second Edition. CRC Press. http://books.google.com/books?id=ppzNBQAAQBAJ
[27] (26 September 2001). Embedded Software: First International Workshop, EMSOFT 2001, Tahoe City, CA, USA, October 8-10, 2001. Proceedings. Springer Science & Business Media. http://www.csl.sri.com/papers/emsoft01/emsoft01.pdf
[28] Yeh, Y.C.. (2001). Safety critical avionics for the 777 primary flight controls system. doi:10.1109/DASC.2001.963311
[29] Nanya, T.. (1989). The Byzantine hardware fault model. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. doi:10.1109/43.41508
[30] Martins, Rolando. (2013). Experiences with Fault-Injection in a Byzantine Fault-Tolerant Protocol. doi:10.1007/978-3-642-45065-5_3
[31] Method for testing the sensitive input range of Byzantine filters.
````

</details>

<details><summary><b>Step 5 — revision_5</b> (2749 words)</summary>

````text
A Byzantine fault (also Byzantine generals problem, interactive consistency, source congruency, error avalanche, Byzantine agreement problem, and Byzantine failure[1]) is a condition of a computer system, particularly distributed computing systems, where components may fail and there is imperfect information on whether a component has failed. The term takes its name from an allegory, the "Byzantine generals problem",[2] developed to describe a situation in which, in order to avoid catastrophic failure of the system, the system's actors must agree on a concerted strategy, but some of these actors are unreliable.

In a Byzantine fault, a component such as a server can inconsistently appear both failed and functioning to failure-detection systems, presenting different symptoms to different observers. It is difficult for the other components to declare it failed and shut it out of the network, because they need to first reach a consensus regarding which component has failed in the first place. Byzantine fault tolerance (BFT) is the resiliency of a fault-tolerant computer system to such conditions.

## Analogy

In its simplest form, a number of generals are attacking a fortress and they must decide as a group whether to attack or retreat. Some generals may prefer to attack, while others prefer to retreat. The important thing is that all generals agree on a common decision, for a halfhearted attack by a few generals would become a rout, and would be worse than either a coordinated attack or a coordinated retreat.

The problem is complicated by the presence of treacherous generals who may not only cast a vote for a suboptimal strategy, they may do so selectively. For instance, if nine generals are voting, four of whom support attacking while four others are in favor of retreat, the ninth general may send a vote of retreat to those generals in favor of retreat, and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers). The problem is complicated further by the generals being physically separated and having to send their votes via messengers who may fail to deliver votes or may forge false votes.

### Resolution

Byzantine fault tolerance can be achieved if the loyal (non-faulty) generals have a majority agreement on their strategy. There can be a default vote value given to missing messages. For example, missing messages can be given a "null" value. Further, if the agreement is that the null votes are in the majority, a pre-assigned default strategy can be used (e.g. retreat).[3]

The typical mapping of this story onto computer systems is that the computers are the generals and their digital communication system links are the messengers. Although the problem is formulated in the analogy as a decision-making and security problem, in electronics, it cannot be solved by cryptographic digital signatures alone, because failures such as incorrect voltages can propagate through the encryption process. Thus, a component may appear functioning to one component and faulty to another, which prevents forming a consensus as to whether the component is faulty or not.

## Characteristics

A Byzantine fault is any fault presenting different symptoms to different observers.[4] A Byzantine failure is the loss of a system service due to a Byzantine fault in systems that require consensus among distributed nodes.[5]

The objective of Byzantine fault tolerance is to be able to defend against failures of system components with or without symptoms that prevent other components of the system from reaching an agreement among themselves, where such an agreement is needed for the correct operation of the system.

The remaining operationally correct components of a Byzantine fault tolerant system will be able to continue providing the system's service as originally intended, assuming there are a sufficient number of accurately-operating components to maintain the service.

Byzantine failures are considered the most general and most difficult class of failures among the failure modes. The so-called fail-stop failure mode occupies the simplest end of the spectrum. Whereas fail-stop failure mode simply means that the only way to fail is a node crash, detected by other nodes, Byzantine failures imply no restrictions, which means that the failed node can generate arbitrary data, including data that makes it appear like a functioning node. Thus, Byzantine failures can confuse failure detection systems, which makes fault tolerance difficult. Despite the analogy, a Byzantine failure is not necessarily a security problem involving hostile human interference: it can arise purely from electrical or software faults.

The terms fault and failure are used here according to the standard definitions[6] originally created by a joint committee on "Fundamental Concepts and Terminology" formed by the IEEE Computer Society's Technical Committee on Dependable Computing and Fault-Tolerance and IFIP Working Group 10.4 on Dependable Computing and Fault Tolerance.[7] See also dependability.

### Caveat

Byzantine fault tolerance is only concerned with broadcast consistency, that is, the property that when one component broadcasts a single consistent value to other components (i.e., sends the same value to the other components), they all receive exactly the same value, or in the case that the broadcaster is not consistent, the other components agree on a common value. This kind of fault tolerance does not encompass the correctness of the value itself; for example, an adversarial component that deliberately sends an incorrect value, but sends that same value consistently to all components, will not be caught in the Byzantine fault tolerance scheme.

## Formal definition

Setting:[8]

Given a system of n components, t of which are dishonest, and assuming only point-to-point channel between all the components.

Whenever a component A tries to broadcast a value x, the other components are allowed to discuss with each other and verify the consistency of A's broadcast, and eventually settle on a common value y.

Property: The system is said to resist Byzantine faults if a component A can broadcast a value x, and then:

If A is honest, then all honest components agree on the value x.

In any case, all honest components agree on the same value y.

Variants: The problem has been studied in the case of both synchronous and asynchronous communications.

The communication graph above is assumed to be the complete graph (i.e. each component can discuss with every other), but the communication graph can be restricted.

It can also be relaxed in a more "realistic" problem where the faulty components do not collude together in an attempt to lure the others into error. It is in this setting that practical algorithms have been devised.

## History

The problem of obtaining Byzantine consensus was conceived and formalized by Robert Shostak, who dubbed it the interactive consistency problem. This work was done in 1978 in the context of the NASA-sponsored SIFT[9] project in the Computer Science Lab at SRI International. SIFT (for Software Implemented Fault Tolerance) was the brain child of John Wensley, and was based on the idea of using multiple general-purpose computers that would communicate through pairwise messaging in order to reach a consensus, even if some of the computers were faulty.

At the beginning of the project, it was not clear how many computers in total were needed to guarantee that a conspiracy of n faulty computers could not "thwart" the efforts of the correctly-operating ones to reach consensus. Shostak showed that a minimum of 3n+1 are needed, and devised a two-round 3n+1 messaging protocol that would work for n=1. His colleague Marshall Pease generalized the algorithm for any n > 0, proving that 3n+1 is both necessary and sufficient. These results, together with a later proof by Leslie Lamport of the sufficiency of 3n using digital signatures, were published in the seminal paper, Reaching Agreement in the Presence of Faults.[10] The authors were awarded the 2005 Edsger W. Dijkstra Prize for this paper.

To make the interactive consistency problem easier to understand, Lamport devised a colorful allegory in which a group of army generals formulate a plan for attacking a city. In its original version, the story cast the generals as commanders of the Albanian army. The name was changed, eventually settling on "Byzantine", at the suggestion of Jack Goldberg to future-proof any potential offense giving.[11] This formulation of the problem, together with some additional results, were presented by the same authors in their 1982 paper, "The Byzantine Generals Problem".[3]

## Examples

Several examples of Byzantine failures that have occurred are given in two equivalent journal papers.[4,5] These and other examples are described on the NASA DASHlink web pages.[12]

Byzantine errors were observed infrequently and at irregular points during endurance testing for the newly constructed Virginia class submarines, at least through 2005 (when the issues were publicly reported).[13]

### Implementations

One example of BFT in use is Bitcoin, a peer-to-peer digital cash system.[14] The Bitcoin network works in parallel to generate a blockchain with proof-of-work allowing the system to overcome Byzantine failures and reach a coherent global view of the system's state. Some proof of stake blockchains also use BFT algorithms.

Some aircraft systems, such as the Boeing 777 Aircraft Information Management System (via its ARINC 659 SAFEbus network),

the Boeing 777 flight control system, and the Boeing 787 flight control systems use Byzantine fault tolerance; because these are real-time systems, their Byzantine fault tolerance solutions must have very low latency. For example, SAFEbus can achieve Byzantine fault tolerance within the order of a microsecond of added latency.[15,16,17] The SpaceX Dragon considers Byzantine fault tolerance in its design.[18]

Byzantine fault tolerance mechanisms use components that repeat an incoming message (or just its signature) to other recipients of that incoming message. All these mechanisms make the assumption that the act of repeating a message blocks the propagation of Byzantine symptoms. For systems that have a high degree of safety or security criticality, these assumptions must be proven to be true to an acceptable level of fault coverage. When providing proof through testing, one difficulty is creating a sufficiently wide range of signals with Byzantine symptoms.[19] Such testing likely will require specialized fault injectors.[20,21]

## Solutions

Several early solutions were described by Lamport, Shostak, and Pease in 1982.[3] They began by noting that the Generals' Problem can be reduced to solving a "Commander and Lieutenants" problem where loyal Lieutenants must all act in unison and that their action must correspond to what the Commander ordered in the case that the Commander is loyal:

One solution considers scenarios in which messages may be forged, but which will be Byzantine-fault-tolerant as long as the number of disloyal generals is less than one third of the generals. The impossibility of dealing with one-third or more traitors ultimately reduces to proving that the one Commander and two Lieutenants problem cannot be solved, if the Commander is traitorous. To see this, suppose we have a traitorous Commander A, and two Lieutenants, B and C: when A tells B to attack and C to retreat, and B and C send messages to each other, forwarding A's message, neither B nor C can figure out who is the traitor, since it is not necessarily A—the other Lieutenant could have forged the message purportedly from A. It can be shown that if n is the number of generals in total, and t is the number of traitors in that n, then there are solutions to the problem only when n > 3t and the communication is synchronous (bounded delay).[22]

A second solution requires unforgeable message signatures. For security-critical systems, digital signatures (in modern computer systems, this may be achieved in practice using public-key cryptography) can provide Byzantine fault tolerance in the presence of an arbitrary number of traitorous generals. However, for safety-critical systems (where "security" addresses intelligent threats while "safety" addresses the inherent dangers of an activity or mission), simple error detecting codes, such as CRCs, provide weaker but often sufficient coverage at a much lower cost. This is true for both Byzantine and non-Byzantine faults. Furthermore, sometimes security measures weaken safety and vice versa. Thus, cryptographic digital signature methods are not a good choice for safety-critical systems, unless there is also a specific security threat as well.[23] While error detecting codes, such as CRCs, are better than cryptographic techniques, neither provide adequate coverage for active electronics in safety-critical systems. This is illustrated by the Schrödinger CRC scenario where a CRC-protected message with a single Byzantine faulty bit presents different data to different observers and each observer sees a valid CRC.[4,5]

Also presented is a variation on the first two solutions allowing Byzantine-fault-tolerant behavior in some situations where not all generals can communicate directly with each other.

Several system architectures were designed c. 1980 that implemented Byzantine fault tolerance. These include: Draper's FTMP,[24] Honeywell's MMFCS,[25] and SRI's SIFT.[9]

### Advanced solutions

In 1999, Miguel Castro and Barbara Liskov introduced the "Practical Byzantine Fault Tolerance" (PBFT) algorithm,[26] which provides high-performance Byzantine state machine replication, processing thousands of requests per second with sub-millisecond increases in latency.

After PBFT, several BFT protocols were introduced to improve its robustness and performance. For instance, Q/U,[27] HQ,[28] Zyzzyva,[29] and ABsTRACTs,[30] addressed the performance and cost issues; whereas other protocols, like Aardvark[31] and RBFT,[32] addressed its robustness issues. Furthermore, Adapt[33] tried to make use of existing BFT protocols, through switching between them in an adaptive way, to improve system robustness and performance as the underlying conditions change. Furthermore, BFT protocols were introduced that leverage trusted components to reduce the number of replicas, e.g., A2M-PBFT-EA[34] and MinBFT.[35]

References:
[1] Kirrmann, Hubert. (n.d.). Fault Tolerant Computing in Industrial Automation. ABB Research Center. http://lamspeople.epfl.ch/kirrmann/Pubs/FaultTolerance/Fault_Tolerance_Tutorial_HK.pdf#page=94
[2] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[3] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[4] Driscoll, K.. (2004). The 23rd Digital Avionics Systems Conference (IEEE Cat. No.04CH37576). doi:10.1109/DASC.2004.1390734
[5] Driscoll, Kevin. (2003). Computer Safety, Reliability, and Security. doi:10.1007/978-3-540-39878-3_19
[6] Avizienis, A.. (2004). Basic concepts and taxonomy of dependable and secure computing. IEEE Transactions on Dependable and Secure Computing. doi:10.1109/TDSC.2004.2
[7] Dependable Computing and Fault Tolerance. http://www.dependability.org
[8] Matthias Fitzi. (2002). Generalized Communication and Security Models in Byzantine Agreement. ETH Zurich. https://www.crypto.ethz.ch/publications/files/Fitzi03.pdf
[9] (1979). SIFT: design and analysis of a fault-tolerant computer for aircraft control. Microelectronics Reliability. doi:10.1016/0026-2714(79)90211-7
[10] Pease, Marshall. (April 1980). Reaching Agreement in the Presence of Faults. Journal of the Association for Computing Machinery. doi:10.1145/322186.322188
[11] Lamport, Leslie. (2016-12-19). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/
[12] Driscoll, Kevin. (2012-12-11). Real System Failures. DASHlink. https://c3.nasa.gov/dashlink/resources/624/
[13] Walter, C.. (2005). Ninth IEEE International Symposium on High-Assurance Systems Engineering (HASE'05). doi:10.1109/HASE.2005.23
[14] Bitcoin - Open source P2P money. bitcoin.org. https://bitcoin.org/en/
[15] M., Paulitsch. (9 January 2015). Industrial Communication Technology Handbook, Second Edition. CRC Press.
[16] (26 September 2001). Embedded Software: First International Workshop, EMSOFT 2001, Tahoe City, CA, USA, October 8-10, 2001. Proceedings. Springer Science & Business Media. http://www.csl.sri.com/papers/emsoft01/emsoft01.pdf
[17] Yeh, Y.C.. (2001). 20th DASC. 20th Digital Avionics Systems Conference (Cat. No.01CH37219). doi:10.1109/DASC.2001.963311
[18] ELC: SpaceX lessons learned [LWN.net]. https://lwn.net/Articles/540368/
[19] Nanya, T.. (1989). The Byzantine hardware fault model. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. doi:10.1109/43.41508
[20] Martins, Rolando. (2013). Middleware 2013. doi:10.1007/978-3-642-45065-5_3
[21] Method for testing the sensitive input range of Byzantine filters.
[22] Feldman, P.. (1997). An optimal probabilistic protocol for synchronous Byzantine agreement. SIAM J. Comput.. doi:10.1137/s0097539790187084
[23] Paulitsch, M.. (2005). 2005 International Conference on Dependable Systems and Networks (DSN'05). doi:10.1109/DSN.2005.31
[24] Hopkins, Albert L.. (1987). The Evolution of Fault-Tolerant Computing. doi:10.1007/978-3-7091-8871-2_6
[25] Driscoll, Kevin. (1984). Multi-Microprocessor Flight Control System. AFWAL/FIGL U.S. Air Force Systems Command.
[26] Castro, M.. (2002). Practical Byzantine Fault Tolerance and Proactive Recovery. ACM Transactions on Computer Systems. doi:10.1145/571637.571640
[27] Abd-El-Malek, M.. (2005). Fault-scalable Byzantine Fault-Tolerant Services. ACM SIGOPS Operating Systems Review. doi:10.1145/1095809.1095817
[28] Cowling, James. (2006). HQ Replication: A Hybrid Quorum Protocol for Byzantine Fault Tolerance. http://portal.acm.org/citation.cfm?id=1298455.1298473
[29] Kotla, Ramakrishna. (December 2009). Zyzzyva: Speculative Byzantine Fault Tolerance. ACM Transactions on Computer Systems. doi:10.1145/1658357.1658358
[30] Guerraoui, Rachid. (2010). The Next 700 BFT Protocols. EuroSys. http://infoscience.epfl.ch/record/144158
[31] Clement, A.. (April 22–24, 2009). Making Byzantine Fault Tolerant Systems Tolerate Byzantine Faults. USENIX. http://www.usenix.org/events/nsdi09/tech/full_papers/clement/clement.pdf
[32] Aublin, P.-L.. (July 8–11, 2013). RBFT: Redundant Byzantine Fault Tolerance. International Conference on Distributed Computing Systems. http://www.temple.edu/cis/icdcs2013/program.html
[33] Bahsoun, J. P.. (2015-05-01). Making BFT Protocols Really Adaptive. Parallel and Distributed Processing Symposium (IPDPS), 2015 IEEE International. doi:10.1109/IPDPS.2015.21
[34] Chun, Byung-Gon. (2007-01-01). Attested Append-only Memory: Making Adversaries Stick to Their Word. Proceedings of Twenty-First ACM SIGOPS Symposium on Operating Systems Principles. doi:10.1145/1294261.1294280
[35] Veronese, G. S.. (2013-01-01). Efficient Byzantine Fault-Tolerance. IEEE Transactions on Computers. doi:10.1109/TC.2011.221
````

</details>

<details><summary><b>Step 6 — revision_6</b> (3054 words)</summary>

````text
A Byzantine fault is a condition of a system, particularly a distributed computing system, where a fault occurs such that different symptoms are presented to different observers, including imperfect information on whether a system component has failed. The term takes its name from an allegory, the "Byzantine generals problem",[1] developed to describe a situation in which, to avoid catastrophic failure of a system, the system's actors must agree on a strategy, but some of these actors are unreliable in such a way as to cause other (good) actors to disagree on the strategy and they may be unaware of the disagreement.

A Byzantine fault is also known as a Byzantine generals problem, a Byzantine agreement problem, or a Byzantine failure.

Byzantine fault tolerance (BFT) is the resilience of a fault-tolerant computer system or similar system to such conditions.

## Definition

A Byzantine fault is any fault presenting different symptoms to different observers.[2] A Byzantine failure is the loss of a system service due to a Byzantine fault in systems that require consensus among multiple components.[3]

The Byzantine allegory considers a number of generals who are attacking a fortress. The generals must decide as a group whether to attack or retreat; some may prefer to attack, while others prefer to retreat. The important thing is that all generals agree on a common decision, for a halfhearted attack by a few generals would become a rout, and would be worse than either a coordinated attack or a coordinated retreat.

The problem is complicated by the presence of treacherous generals who may not only cast a vote for a suboptimal strategy; they may do so selectively. For instance, if nine generals are voting, four of whom support attacking while four others are in favor of retreat, the ninth general may send a vote of retreat to those generals in favor of retreat, and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers). The problem is complicated further by the generals being physically separated and having to send their votes via messengers who may fail to deliver votes or may forge false votes.

Byzantine fault tolerance can be achieved if the number of loyal (non-faulty) generals is greater than three times the number of disloyal (faulty) generals. There can be a default vote value given to missing messages. For example, missing messages can be given a "null" value. Further, if the agreement is that the null votes are in the majority, a pre-assigned default strategy can be used (e.g., retreat).[4]

The typical mapping of this allegory onto computer systems is that the computers are the generals and their digital communication system links are the messengers. Although the problem is formulated in the allegory as a decision-making and security problem, in electronics, it cannot be solved by cryptographic digital signatures alone, because failures such as incorrect voltages can propagate through the encryption process. Thus, a faulty message could be sent such that some recipients detect the message as faulty (bad signature), others see it is having a good signature, and a third group also sees a good signature but with different message contents than the second group.[2]

## History

The problem of obtaining Byzantine consensus was conceived and formalized by Robert Shostak, who dubbed it the interactive consistency problem. This work was done in 1978 in the context of the NASA-sponsored SIFT[5] project in the Computer Science Lab at SRI International. SIFT (for Software Implemented Fault Tolerance) was the brainchild of John Wensley, and was based on the idea of using multiple general-purpose computers that would communicate through pairwise messaging in order to reach a consensus, even if some of the computers were faulty.

At the beginning of the project, it was not clear how many computers in total were needed to guarantee that a conspiracy of n faulty computers could not "thwart" the efforts of the correctly-operating ones to reach consensus. Shostak showed that a minimum of 3n+1 are needed, and devised a two-round 3n+1 messaging protocol that would work for n=1. His colleague Marshall Pease generalized the algorithm for any n > 0, proving that 3n+1 is both necessary and sufficient. These results, together with a later proof by Leslie Lamport of the sufficiency of 3n using digital signatures, were published in the seminal paper, Reaching Agreement in the Presence of Faults.[6] The authors were awarded the 2005 Edsger W. Dijkstra Prize for this paper.

To make the interactive consistency problem easier to understand, Lamport devised a colorful allegory in which a group of army generals formulate a plan for attacking a city. In its original version, the story cast the generals as commanders of the Albanian army. The name was changed, eventually settling on "Byzantine", at the suggestion of Jack Goldberg to future-proof any potential offense-giving.[7] This formulation of the problem, together with some additional results, were presented by the same authors in their 1982 paper, "The Byzantine Generals Problem".[4]

## Mitigation

The objective of Byzantine fault tolerance is to be able to defend against failures of system components with or without symptoms that prevent other components of the system from reaching an agreement among themselves, where such an agreement is needed for the correct operation of the system.

The remaining operationally correct components of a Byzantine fault tolerant system will be able to continue providing the system's service as originally intended, assuming there are a sufficient number of accurately-operating components to maintain the service.

When considering failure propagation only via errors, Byzantine failures are considered the most general and most difficult class of failures among the failure modes. The so-called fail-stop failure mode occupies the simplest end of the spectrum. Whereas the fail-stop failure mode simply means that the only way to fail is a node crash, detected by other nodes, Byzantine failures imply no restrictions on what errors can be created, which means that a failed node can generate arbitrary data, including data that makes it appear like a functioning node to a subset of other nodes. Thus, Byzantine failures can confuse failure detection systems, which makes fault tolerance difficult. Despite the allegory, a Byzantine failure is not necessarily a security problem involving hostile human interference: it can arise purely from physical or software faults.

The terms fault and failure are used here according to the standard definitions[8] originally created by a joint committee on "Fundamental Concepts and Terminology" formed by the IEEE Computer Society's Technical Committee on Dependable Computing and Fault-Tolerance and IFIP Working Group 10.4 on Dependable Computing and Fault Tolerance.[9] See also dependability.

Byzantine fault tolerance is only concerned with broadcast consistency, that is, the property that when a component broadcasts a value to all the other components, they all receive exactly this same value, or in the case that the broadcaster is not consistent, the other components agree on a common value themselves. This kind of fault tolerance does not encompass the correctness of the value itself; for example, an adversarial component that deliberately sends an incorrect value, but sends that same value consistently to all components, will not be caught in the Byzantine fault tolerance scheme.

## Solutions

Several early solutions were described by Lamport, Shostak, and Pease in 1982.[4] They began by noting that the Generals' Problem can be reduced to solving a "Commander and Lieutenants" problem where loyal Lieutenants must all act in unison and that their action must correspond to what the Commander ordered in the case that the Commander is loyal:

One solution considers scenarios in which messages may be forged, but which will be Byzantine-fault-tolerant as long as the number of disloyal generals is less than one third of the generals. The impossibility of dealing with one-third or more traitors ultimately reduces to proving that the one Commander and two Lieutenants problem cannot be solved, if the Commander is traitorous. To see this, suppose we have a traitorous Commander A, and two Lieutenants, B and C: when A tells B to attack and C to retreat, and B and C send messages to each other, forwarding A's message, neither B nor C can figure out who is the traitor, since it is not necessarily A—the other Lieutenant could have forged the message purportedly from A. It can be shown that if n is the number of generals in total, and t is the number of traitors in that n, then there are solutions to the problem only when n > 3t and the communication is synchronous (bounded delay).[10] The full set of BFT requirements are: For F number of Byzantine failures, there needs to be at least 3F+1 players (fault containment zones), 2F+1 independent communication paths, and F+1 rounds of communication. There can be hybrid fault models in which benign (non-Byzantine) faults as well as Byzantine faults may exist simultaneously. For each additional benign fault that must be tolerated, the above numbers need to be incremented by one. If the BFT rounds of communication don't exist, Byzantine failures can occur even with no faulty hardware.

A second solution requires unforgeable message signatures. For security-critical systems, digital signatures (in modern computer systems, this may be achieved, in practice, by using public-key cryptography) can provide Byzantine fault tolerance in the presence of an arbitrary number of traitorous generals. However, for safety-critical systems (where "security" addresses intelligent threats while "safety" addresses the inherent dangers of an activity or mission, i.e., faults due to natural phenomena), error detecting codes, such as CRCs, provide stronger coverage at a much lower cost. (Note that CRCs can provide guaranteed coverage for errors that cryptography cannot. If an encryption scheme could provide some guarantee of coverage for message errors, it would have a structure that would make it insecure.[11]) But neither digital signatures nor error detecting codes such as CRCs provide a known level of protection against Byzantine errors from natural causes. And more generally, security measures can weaken safety and vice versa. Thus, cryptographic digital signature methods are not a good choice for safety-critical systems, unless there is also a specific security threat as well.[12] While error detecting codes, such as CRCs, are better than cryptographic techniques, neither provide adequate coverage for active electronics in safety-critical systems. This is illustrated by the Schrödinger CRC scenario where a CRC-protected message with a single Byzantine faulty bit presents different data to different observers and each observer sees a valid CRC.[2,3]

Also presented is a variation on the first two solutions allowing Byzantine-fault-tolerant behavior in some situations where not all generals can communicate directly with each other.

There are many systems that claim BFT without meeting the above minimum requirements (e.g., blockchain). Given that there is mathematical proof that this is impossible, these claims need to include a caveat that their definition of BFT strays from the original. That is, systems such as blockchain don't guarantee agreement, they only make disagreement expensive.

Several system architectures were designed c. 1980 that implemented Byzantine fault tolerance. These include: Draper's FTMP,[13] Honeywell's MMFCS,[14] and SRI's SIFT.[5]

In 1999, Miguel Castro and Barbara Liskov introduced the "Practical Byzantine Fault Tolerance" (PBFT) algorithm,[15] which provides high-performance Byzantine state machine replication, processing thousands of requests per second with sub-millisecond increases in latency.

After PBFT, several BFT protocols were introduced to improve its robustness and performance. For instance, Q/U,[16] HQ,[17] Zyzzyva,[18] and ABsTRACTs,[19] addressed the performance and cost issues; whereas other protocols, like Aardvark[20] and RBFT,[21] addressed its robustness issues. Furthermore, Adapt[22] tried to make use of existing BFT protocols, through switching between them in an adaptive way, to improve system robustness and performance as the underlying conditions change. Furthermore, BFT protocols were introduced that leverage trusted components to reduce the number of replicas, e.g., A2M-PBFT-EA[23] and MinBFT.[24]

## Applications

Several examples of Byzantine failures that have occurred are given in two equivalent journal papers.[2,3] These and other examples are described on the NASA DASHlink web pages.[25]

### Applications in computing

Byzantine fault tolerance mechanisms use components that repeat an incoming message (or just its signature, which can be reduced to just a single bit of information if self-checking pairs are used for nodes). to other recipients of that incoming message. All these mechanisms make the assumption that the act of repeating a message blocks the propagation of Byzantine symptoms. For systems that have a high degree of safety or security criticality, these assumptions must be proven to be true to an acceptable level of fault coverage. When providing proof through testing, one difficulty is creating a sufficiently wide range of signals with Byzantine symptoms.[26] Such testing will likely require specialized fault injectors.[27,28]

### Military applications

Byzantine errors were observed infrequently and at irregular points during endurance testing for the newly constructed Virginia class submarines, at least through 2005 (when the issues were publicly reported).[29]

### Cryptocurrency applications

The Bitcoin network works in parallel to generate a blockchain with proof-of-work allowing the system to overcome Byzantine failures and reach a coherent global view of the system's state.[30,31] Some proof of stake blockchains also use BFT algorithms.

### Blockchain Technology

Byzantine Fault Tolerance (BFT) is a crucial concept in blockchain technology, ensuring that a network can continue to function even when some nodes[32] (participants) fail or act maliciously. This tolerance is necessary because blockchains are decentralized systems with no central authority, making it essential to achieve consensus among nodes, even if some try to disrupt the process.

### Applications and Examples of Byzantine Fault Tolerance in Blockchain

Safety Mechanisms: Different blockchains use various BFT-based consensus mechanisms like Practical Byzantine Fault Tolerance (PBFT), Tendermint, and Delegated Proof of Stake (DPoS) to handle Byzantine faults. These protocols ensure that the majority of honest nodes can agree on the next block in the chain, securing the network against attacks and preventing double-spending and other types of fraud. Practical examples of networks include Hyperledger Fabric, Cosmos and Klever in this sequence.

51% Attack Mitigation: While traditional blockchains like Bitcoin use Proof of Work (PoW), which is susceptible to a 51% attack, BFT-based systems are designed to tolerate up to one-third of faulty or malicious nodes without compromising the network's integrity.

Decentralized Trust: Byzantine Fault Tolerance underpins the trust model in decentralized networks. Instead of relying on a central authority, the network's security depends on the ability of honest nodes to outnumber and outmaneuver malicious ones.

Private and Permissioned Blockchains: BFT is especially important in private or permissioned blockchains, where a limited number of known participants need to reach a consensus quickly and securely. These networks often use BFT protocols to enhance performance and security.

### Applications in aviation

Some aircraft systems, such as the Boeing 777 Aircraft Information Management System (via its ARINC 659 SAFEbus network), the Boeing 777 flight control system, and the Boeing 787 flight control systems, use Byzantine fault tolerance; because these are real-time systems, their Byzantine fault tolerance solutions must have very low latency. For example, SAFEbus can achieve Byzantine fault tolerance within the order of a microsecond of added latency.[33,34,35] The SpaceX Dragon considers Byzantine fault tolerance in its design.[36]

References:
[1] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[2] Driscoll, K.. (2004). The 23rd Digital Avionics Systems Conference (IEEE Cat. No.04CH37576). doi:10.1109/DASC.2004.1390734
[3] Driscoll, Kevin. (2003). Computer Safety, Reliability, and Security. doi:10.1007/978-3-540-39878-3_19
[4] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[5] (1979). SIFT: design and analysis of a fault-tolerant computer for aircraft control. Microelectronics Reliability. doi:10.1016/0026-2714(79)90211-7
[6] Pease, Marshall. (April 1980). Reaching Agreement in the Presence of Faults. Journal of the Association for Computing Machinery. doi:10.1145/322186.322188
[7] Lamport, Leslie. (2016-12-19). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/
[8] Avizienis, A.. (2004). Basic concepts and taxonomy of dependable and secure computing. IEEE Transactions on Dependable and Secure Computing. doi:10.1109/TDSC.2004.2
[9] Dependable Computing and Fault Tolerance. http://www.dependability.org
[10] Feldman, P.. (1997). An optimal probabilistic protocol for synchronous Byzantine agreement. SIAM J. Comput.. doi:10.1137/s0097539790187084
[11] Koopman, Philip; Driscoll, Kevin; Hall, Brendan (March 2015). "Cyclic Redundancy Code and Checksum Algorithms to Ensure Critical Data Integrity" (PDF). Federal Aviation Administration. DOT/FAA/TC-14/49. Archived (PDF) from the original on 18 May 2015. Retrieved 9 May 2015.
[12] Paulitsch, M.. (2005). 2005 International Conference on Dependable Systems and Networks (DSN'05). doi:10.1109/DSN.2005.31
[13] Hopkins, Albert L.. (1987). The Evolution of Fault-Tolerant Computing. doi:10.1007/978-3-7091-8871-2_6
[14] Driscoll, Kevin. (1984). Multi-Microprocessor Flight Control System. AFWAL/FIGL U.S. Air Force Systems Command.
[15] Castro, M.. (2002). Practical Byzantine Fault Tolerance and Proactive Recovery. ACM Transactions on Computer Systems. doi:10.1145/571637.571640
[16] Abd-El-Malek, M.. (2005). Fault-scalable Byzantine Fault-Tolerant Services. ACM SIGOPS Operating Systems Review. doi:10.1145/1095809.1095817
[17] Cowling, James. (2006). HQ Replication: A Hybrid Quorum Protocol for Byzantine Fault Tolerance. http://portal.acm.org/citation.cfm?id=1298455.1298473
[18] Kotla, Ramakrishna. (December 2009). Zyzzyva: Speculative Byzantine Fault Tolerance. ACM Transactions on Computer Systems. doi:10.1145/1658357.1658358
[19] Guerraoui, Rachid. (2010). The Next 700 BFT Protocols. EuroSys. http://infoscience.epfl.ch/record/144158
[20] Clement, A.. (April 22–24, 2009). Making Byzantine Fault Tolerant Systems Tolerate Byzantine Faults. USENIX. http://www.usenix.org/events/nsdi09/tech/full_papers/clement/clement.pdf
[21] Aublin, P.-L.. (July 8–11, 2013). RBFT: Redundant Byzantine Fault Tolerance. International Conference on Distributed Computing Systems. http://www.temple.edu/cis/icdcs2013/program.html
[22] Bahsoun, J. P.. (2015-05-01). 2015 IEEE International Parallel and Distributed Processing Symposium. doi:10.1109/IPDPS.2015.21
[23] Chun, Byung-Gon. (2007-01-01). Proceedings of twenty-first ACM SIGOPS symposium on Operating systems principles. ACM. doi:10.1145/1294261.1294280
[24] Veronese, G. S.. (2013-01-01). Efficient Byzantine Fault-Tolerance. IEEE Transactions on Computers. doi:10.1109/TC.2011.221
[25] Driscoll, Kevin. (2012-12-11). Real System Failures. DASHlink. https://c3.nasa.gov/dashlink/resources/624/
[26] Nanya, T.. (1989). The Byzantine hardware fault model. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. doi:10.1109/43.41508
[27] Martins, Rolando. (2013). Middleware 2013. doi:10.1007/978-3-642-45065-5_3
[28] Method for testing the sensitive input range of Byzantine filters.
[29] Walter, C.. (2005). Ninth IEEE International Symposium on High-Assurance Systems Engineering (HASE'05). doi:10.1109/HASE.2005.23
[30] Rubby, Matt. (20 January 2024). How Byzantine Generals Problem Relates to You in 2024. Swan Bitcoin. https://www.swanbitcoin.com/byzantine-generals-problem/
[31] Tholoniat, Pierre. (2022). Formal Verification of Blockchain Byzantine Fault Tolerance. Handbook on Blockchain. doi:10.1007/978-3-031-07535-3_12
[32] Node Operations. https://docs.klever.org/node-operations
[33] M., Paulitsch. (9 January 2015). Industrial Communication Technology Handbook, Second Edition. CRC Press.
[34] (26 September 2001). Embedded Software: First International Workshop, EMSOFT 2001, Tahoe City, CA, USA, October 8-10, 2001. Proceedings. Springer Science & Business Media. http://www.csl.sri.com/papers/emsoft01/emsoft01.pdf
[35] Yeh, Y.C.. (2001). 20th DASC. 20th Digital Avionics Systems Conference (Cat. No.01CH37219). doi:10.1109/DASC.2001.963311
[36] ELC: SpaceX lessons learned [LWN.net]. https://lwn.net/Articles/540368/
````

</details>

<details><summary><b>Step 7 — revision_7</b> (3350 words)</summary>

````text
A Byzantine fault is a condition of a system, particularly a distributed computing system, where a fault occurs such that different symptoms are presented to different observers, including imperfect information on whether a system component has failed. The term takes its name from an allegory, the "Byzantine generals problem",[1] developed to describe a situation in which, to avoid catastrophic failure of a system, the system's actors must agree on a strategy, but some of these actors are unreliable in a way which causes other (good) actors to disagree on the strategy and they may be unaware of the disagreement.

A Byzantine fault is also known as a Byzantine generals problem, a Byzantine agreement problem, or a Byzantine failure.

Byzantine fault tolerance (BFT) is the resilience of a fault-tolerant computer system or similar system to such conditions.

## Definition

A Byzantine fault is any fault presenting different symptoms to different observers.[2] A Byzantine failure is the loss of a system service due to a Byzantine fault in systems that require consensus among multiple components.[3]

The Byzantine allegory considers a number of generals who are attacking a fortress. The generals must decide as a group whether to attack or retreat; some may prefer to attack, while others prefer to retreat. The important thing is that all generals agree on a common decision, for a half-hearted attack by a few generals would become a rout, and would be worse than either a coordinated attack or a coordinated retreat.

The problem is complicated by the presence of treacherous generals who may not only cast a vote for a suboptimal strategy; they may do so selectively. For instance, if nine generals are voting, four of whom support attacking while four others are in favor of retreat, the ninth general may send a vote of retreat to those generals in favor of retreat, and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers). The problem is complicated further by the generals being physically separated and having to send their votes via messengers who may fail to deliver votes or may forge false votes.

Without message signing, Byzantine fault tolerance can only be achieved if the total number of generals is greater than three times the number of disloyal (faulty) generals. There can be a default vote value given to missing messages. For example, missing messages can be given a "null" value. Further, if the agreement is that the null votes are in the majority, a pre-assigned default strategy can be used (e.g., retreat).[4]

The typical mapping of this allegory onto computer systems is that the computers are the generals and their digital communication system links are the messengers. Although the problem is formulated in the allegory as a decision-making and security problem, in electronics, it cannot be solved by cryptographic digital signatures alone, because failures such as incorrect voltages can propagate through the encryption process. Thus, a faulty message could be sent such that some recipients detect the message as faulty (bad signature), others see it is having a good signature, and a third group also sees a good signature but with different message contents than the second group.[2]

## History

The problem of obtaining Byzantine consensus was conceived and formalized by Robert Shostak, who dubbed it the interactive consistency problem. This work was done in 1978 in the context of the NASA-sponsored SIFT[5] project in the Computer Science Lab at SRI International. SIFT (for Software Implemented Fault Tolerance) was the brainchild of John Wensley, and was based on the idea of using multiple general-purpose computers that would communicate through pairwise messaging in order to reach a consensus, even if some of the computers were faulty.

At the beginning of the project, it was not clear how many computers in total were needed to guarantee that a conspiracy of n faulty computers could not "thwart" the efforts of the correctly-operating ones to reach consensus. Shostak showed that a minimum of 3n+1 are needed, and devised a two-round 3n+1 messaging protocol that would work for n=1. His colleague Marshall Pease generalized the algorithm for any n > 0, proving that 3n+1 is both necessary and sufficient. These results, together with a later proof by Leslie Lamport of the sufficiency of 3n using digital signatures, were published in the seminal paper, Reaching Agreement in the Presence of Faults.[6] The authors were awarded the 2005 Edsger W. Dijkstra Prize for this paper.

To make the interactive consistency problem easier to understand, Lamport devised a colorful allegory in which a group of army generals formulate a plan for attacking a city. In its original version, the story cast the generals as commanders of the Albanian army. The name was changed, eventually settling on "Byzantine", at the suggestion of Jack Goldberg to future-proof any potential offense-giving.[7] This formulation of the problem, together with some additional results, were presented by the same authors in their 1982 paper, "The Byzantine Generals Problem".[4]

## Mitigation

The objective of Byzantine fault tolerance is to be able to defend against failures of system components with or without symptoms that prevent other components of the system from reaching an agreement among themselves, where such an agreement is needed for the correct operation of the system.

The remaining operationally correct components of a Byzantine fault tolerant system will be able to continue providing the system's service as originally intended, assuming there are a sufficient number of accurately-operating components to maintain the service.

When considering failure propagation only via errors, Byzantine failures are considered the most general and most difficult class of failures among the failure modes. The so-called fail-stop failure mode occupies the simplest end of the spectrum. Whereas the fail-stop failure mode simply means that the only way to fail is a node crash, detected by other nodes, Byzantine failures imply no restrictions on what errors can be created, which means that a failed node can generate arbitrary data, including data that makes it appear like a functioning node to a subset of other nodes. Thus, Byzantine failures can confuse failure detection systems, which makes fault tolerance difficult. Despite the allegory, a Byzantine failure is not necessarily a security problem involving hostile human interference: it can arise purely from physical or software faults.

The terms fault and failure are used here according to the standard definitions[8] originally created by a joint committee on "Fundamental Concepts and Terminology" formed by the IEEE Computer Society's Technical Committee on Dependable Computing and Fault-Tolerance and IFIP Working Group 10.4 on Dependable Computing and Fault Tolerance.[9] See also dependability.

Byzantine fault tolerance is only concerned with broadcast consistency, that is, the property that when a component broadcasts a value to all the other components, they all receive exactly this same value, or in the case that the broadcaster is not consistent, the other components agree on a common value themselves. This kind of fault tolerance does not encompass the correctness of the value itself; for example, an adversarial component that deliberately sends an incorrect value, but sends that same value consistently to all components, will not be caught in the Byzantine fault tolerance scheme.

## Solutions

Several early solutions were described by Lamport, Shostak, and Pease in 1982.[4] They began by noting that the Generals' Problem can be reduced to solving a "Commander and Lieutenants" problem where loyal Lieutenants must all act in unison and that their action must correspond to what the Commander ordered in the case that the Commander is loyal:

One solution considers scenarios in which messages may be forged, but which will be Byzantine-fault-tolerant as long as the number of disloyal generals is less than one third of the generals. The impossibility of dealing with one-third or more traitors ultimately reduces to proving that the one Commander and two Lieutenants problem cannot be solved, if the Commander is traitorous. To see this, suppose we have a traitorous Commander A, and two Lieutenants, B and C: when A tells B to attack and C to retreat, and B and C send messages to each other, forwarding A's message, neither B nor C can figure out who is the traitor, since it is not necessarily A—the other Lieutenant could have forged the message purportedly from A. It can be shown that if n is the number of generals in total, and t is the number of traitors in that n, then there are solutions to the problem only when n > 3t and the communication is synchronous (bounded delay).[10] The full set of BFT requirements are: For F number of Byzantine failures, there needs to be at least 3F+1 players (fault containment zones), 2F+1 independent communication paths, and F+1 rounds of communication. There can be hybrid fault models in which benign (non-Byzantine) faults as well as Byzantine faults may exist simultaneously. For each additional benign fault that must be tolerated, the above numbers need to be incremented by one. If the BFT rounds of communication do not exist, Byzantine failures can occur even with no faulty hardware.

A second solution requires unforgeable message signatures. For security-critical systems, digital signatures (in modern computer systems, this may be achieved, in practice, by using public-key cryptography) can provide Byzantine fault tolerance in the presence of an arbitrary number of traitorous generals. However, for safety-critical systems (where "security" addresses intelligent threats while "safety" addresses the inherent dangers of an activity or mission, i.e., faults due to natural phenomena), error detecting codes, such as CRCs, provide stronger coverage at a much lower cost. (Note that CRCs can provide guaranteed coverage for errors that cryptography cannot. If an encryption scheme could provide some guarantee of coverage for message errors, it would have a structure that would make it insecure.[11] ) But neither digital signatures nor error detecting codes such as CRCs provide a known level of protection against Byzantine errors from natural causes. More generally, security measures can weaken safety and vice versa. Thus, cryptographic digital signature methods are not a good choice for safety-critical systems, unless there is also a specific security threat as well.[12] While error detecting codes, such as CRCs, are better than cryptographic techniques, neither provide adequate coverage for active electronics in safety-critical systems. This is illustrated by the Schrödinger CRC scenario where a CRC-protected message with a single Byzantine faulty bit presents different data to different observers and each observer sees a valid CRC.[2,3]

Also presented is a variation on the first two solutions allowing Byzantine-fault-tolerant behavior in some situations where not all generals can communicate directly with each other.[1]

There are many systems that claim BFT without meeting the above minimum requirements (e.g., blockchain). Given that there is mathematical proof that this is impossible, these claims need to include a caveat that their definition of BFT strays from the original. That is, systems such as blockchain don't guarantee agreement. They use resource-intensive mechanisms that make disagreements impractical to maintain.

Several system architectures were designed c. 1980 that implemented Byzantine fault tolerance. These include: Draper's FTMP,[13] Honeywell's MMFCS,[14] and SRI's SIFT.[5]

In 1999, Miguel Castro and Barbara Liskov introduced the "Practical Byzantine Fault Tolerance" (PBFT) algorithm,[15] which provides high-performance Byzantine state machine replication, processing thousands of requests per second with sub-millisecond increases in latency.

After PBFT, several BFT protocols were introduced to improve its robustness and performance. For instance, Q/U,[16] HQ,[17] Zyzzyva,[18] and ABsTRACTs,[19] addressed the performance and cost issues; whereas other protocols, like Aardvark[20] and RBFT,[21] addressed its robustness issues. Furthermore, Adapt[22] tried to make use of existing BFT protocols, through switching between them in an adaptive way, to improve system robustness and performance as the underlying conditions change. Furthermore, BFT protocols were introduced that leverage trusted components to reduce the number of replicas, e.g., A2M-PBFT-EA[23] and MinBFT.[24]

Recent research addresses the scalability limits of traditional BFT implementations (which often incur O(n^2) communication complexity) by parallelizing consensus. For example, the Cerberus protocol maps data to a large, fixed state space to couple consensus instances with specific transaction sets. This allows BFT processes to run independently in parallel, enabling linear scalability relative to the network size.[25]

## Applications

Several examples of Byzantine failures that have occurred are given in two equivalent journal papers.[2,3] These and other examples are described on the NASA DASHlink web pages.[26]

### Applications in computing

Byzantine fault tolerance mechanisms use components that repeat an incoming message (or just its signature, which can be reduced to just a single bit of information if self-checking pairs are used for nodes) to other recipients of that incoming message. All these mechanisms make the assumption that the act of repeating a message blocks the propagation of Byzantine symptoms. For systems that have a high degree of safety or security criticality, these assumptions must be proven to be true to an acceptable level of fault coverage. When providing proof through testing, one difficulty is creating a sufficiently wide range of signals with Byzantine symptoms.[27] Such testing will likely require specialized fault injectors.[28,29]

### Military applications

Byzantine errors were observed infrequently and at irregular points during endurance testing for the newly constructed , at least through 2005 (when the issues were publicly reported).[30]

### Cryptocurrency applications

The Bitcoin network works in parallel to generate a blockchain with proof of work allowing the system to overcome Byzantine failures and reach a coherent global view of the system's state.[31,32] Some proof of stake blockchains also use BFT algorithms.

### Blockchain

Byzantine fault tolerance is a crucial concept in blockchain technology, ensuring that a network can continue to function even when some nodes[33] (participants) fail or act maliciously. This tolerance is necessary because blockchains are decentralized systems with no central authority, making it essential to achieve consensus among nodes, even if some try to disrupt the process.

### Artificial Intelligence

Ensuring that an AI system behaves reliably and as intended, especially in the presence of unexpected faults or adversarial conditions, is a complex challenge. By accepting that components may fail, and further that frontier AI models may deceive, Byzantine fault tolerance has been proposed as an approach towards AI safety.[34] Structuring AI systems as ensembles of AI artifacts or modules that check and balance each other leads to strong assurances that no single errant or deceptive component can easily steer the system into an unsafe state.

### Applications and examples

Safety mechanismsDifferent blockchains use various BFT-based consensus mechanisms like Practical Byzantine Fault Tolerance (PBFT), Tendermint, and Delegated Proof of Stake (DPoS) to handle Byzantine faults. These protocols ensure that the majority of honest nodes can agree on the next block in the chain, securing the network against attacks and preventing double-spending and other types of fraud. Practical examples of networks include Hyperledger Fabric, Cosmos and Klever in this sequence.

51% attack mitigation While traditional blockchains like Bitcoin use proof of work (PoW), which is susceptible to a 51% attack, BFT-based systems are designed to tolerate up to one-third of faulty or malicious nodes without compromising the network's integrity.

Decentralized trust Byzantine fault tolerance underpins the trust model in decentralized networks. Instead of relying on a central authority, the network's security depends on the ability of honest nodes to outnumber and outmaneuver malicious ones.

Private and permissioned blockchains BFT is especially important in private or permissioned blockchains, where a limited number of known participants need to reach a consensus quickly and securely. These networks often use BFT protocols to enhance performance and security.

### In aviation

Some aircraft systems, such as the Boeing 777 Aircraft Information Management System (via its ARINC 659 SAFEbus network), the Boeing 777 flight control system, and the Boeing 787 flight control systems, use Byzantine fault tolerance; because these are real-time systems, their Byzantine fault tolerance solutions must have very low latency. For example, SAFEbus can achieve Byzantine fault tolerance within the order of a microsecond of added latency.[35,36,37]

### In space systems

The SpaceX Dragon considers Byzantine fault tolerance in its design.[38] The Ares rocket avionics, now the Space Launch System (SLS), utilizes a triplex with an interstage of accomplish Byzantine resilience.[39,40] The Orion spacecraft utilizes self-checking pairs to detect and mask Byzantine faults.[41]

### In democracy and civil societies

In legislatures, civil societies, polls, statistical surveys, and so forth, systems that require a minimum supermajority threshold agreement greater than two-thirds are similar to consensus reflective of Byzantine Fault Tolerant -like characteristics. By contrast, systems that operate on the sub-supermajority basis of simple majorities or a minority government could be vulnerable to Byzantine fault -like behavior.

References:
[1] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[2] Driscoll, K.. (2004). The 23rd Digital Avionics Systems Conference (IEEE Cat. No. 04CH37576). doi:10.1109/DASC.2004.1390734
[3] Driscoll, Kevin. (2003). Computer Safety, Reliability, and Security. doi:10.1007/978-3-540-39878-3_19
[4] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[5] (1979). SIFT: design and analysis of a fault-tolerant computer for aircraft control. Microelectronics Reliability. doi:10.1016/0026-2714(79)90211-7
[6] Pease, Marshall. (April 1980). Reaching Agreement in the Presence of Faults. Journal of the Association for Computing Machinery. doi:10.1145/322186.322188
[7] Lamport, Leslie. (2016-12-19). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/
[8] Avizienis, A.. (2004). Basic concepts and taxonomy of dependable and secure computing. IEEE Transactions on Dependable and Secure Computing. doi:10.1109/TDSC.2004.2
[9] Dependable Computing and Fault Tolerance. IEEE Computer Society. http://www.dependability.org
[10] Feldman, P.. (1997). An optimal probabilistic protocol for synchronous Byzantine agreement. SIAM Journal on Computing. doi:10.1137/s0097539790187084
[11] Koopman, Philip; Driscoll, Kevin; Hall, Brendan (March 2015). "Cyclic Redundancy Code and Checksum Algorithms to Ensure Critical Data Integrity" (PDF). Federal Aviation Administration. DOT/FAA/TC-14/49.
[12] Paulitsch, M.. (2005). 2005 International Conference on Dependable Systems and Networks (DSN'05). doi:10.1109/DSN.2005.31
[13] Hopkins, Albert L.. (1987). The Evolution of Fault-Tolerant Computing. doi:10.1007/978-3-7091-8871-2_6
[14] Driscoll, Kevin. (1984). Multi-Microprocessor Flight Control System. AFWAL/FIGL U.S. Air Force Systems Command.
[15] Castro, M.. (2002). Practical Byzantine Fault Tolerance and Proactive Recovery. ACM Transactions on Computer Systems. doi:10.1145/571637.571640
[16] Abd-El-Malek, M.. (2005). Fault-scalable Byzantine Fault-Tolerant Services. ACM SIGOPS Operating Systems Review. doi:10.1145/1095809.1095817
[17] Cowling, James. (2006). HQ Replication: A Hybrid Quorum Protocol for Byzantine Fault Tolerance. http://portal.acm.org/citation.cfm?id=1298455.1298473
[18] Kotla, Ramakrishna. (December 2009). Zyzzyva: Speculative Byzantine Fault Tolerance. ACM Transactions on Computer Systems. doi:10.1145/1658357.1658358
[19] Guerraoui, Rachid. (2010). The Next 700 BFT Protocols. EuroSys. http://infoscience.epfl.ch/record/144158
[20] Clement, A.. (April 22–24, 2009). Making Byzantine Fault Tolerant Systems Tolerate Byzantine Faults. USENIX. http://www.usenix.org/events/nsdi09/tech/full_papers/clement/clement.pdf
[21] Aublin, P.-L.. (July 8–11, 2013). RBFT: Redundant Byzantine Fault Tolerance. International Conference on Distributed Computing Systems. http://www.temple.edu/cis/icdcs2013/program.html
[22] Bahsoun, J. P.. (2015-05-01). 2015 IEEE International Parallel and Distributed Processing Symposium. doi:10.1109/IPDPS.2015.21
[23] Chun, Byung-Gon. (2007-01-01). Proceedings of twenty-first ACM SIGOPS symposium on Operating systems principles. ACM. doi:10.1145/1294261.1294280
[24] Veronese, G. S.. (2013-01-01). Efficient Byzantine Fault-Tolerance. IEEE Transactions on Computers. doi:10.1109/TC.2011.221
[25] Hellings, Jelle. (2021). Cerberus: Minimalistic Multi-shard Byzantine-resilient Transaction Processing. Proceedings of the VLDB Endowment. doi:10.14778/3476249.3476274
[26] Driscoll, Kevin. (2012-12-11). Real System Failures. DASHlink. https://c3.nasa.gov/dashlink/resources/624/
[27] Nanya, T.. (1989). The Byzantine hardware fault model. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. doi:10.1109/43.41508
[28] Martins, Rolando. (2013). Middleware 2013. doi:10.1007/978-3-642-45065-5_3
[29] Method for testing the sensitive input range of Byzantine filters.
[30] Walter, C.. (2005). Ninth IEEE International Symposium on High-Assurance Systems Engineering (HASE'05). doi:10.1109/HASE.2005.23
[31] Rubby, Matt. (20 January 2024). How Byzantine Generals Problem Relates to You in 2024. Swan Bitcoin. https://www.swanbitcoin.com/byzantine-generals-problem/
[32] Tholoniat, Pierre. (2022). Formal Verification of Blockchain Byzantine Fault Tolerance. Handbook on Blockchain. doi:10.1007/978-3-031-07535-3_12
[33] Node Operations. https://docs.klever.org/node-operations
[34] deVadoss, John. (2025). A Byzantine Fault Tolerance Approach towards AI Safety.
[35] M., Paulitsch. (9 January 2015). Industrial Communication Technology Handbook. CRC Press.
[36] Rushby, John. (26 September 2001). Bus Architectures For Safety-Critical Embedded Systems. Springer Science & Business Media. http://www.csl.sri.com/papers/emsoft01/emsoft01.pdf
[37] Yeh, Y. C.. (2001). Safety critical avionics for the 777 primary flight controls system. doi:10.1109/DASC.2001.963311
[38] ELC: SpaceX lessons learned. LWN. https://lwn.net/Articles/540368/
[39] SLS (Space Launch System) Avionics: The “Brains” of SLS. nasa.gov. https://www.nasa.gov/wp-content/uploads/2024/12/sls-4964-sls-avionics-fact-sheet-dec2024-508.pdf?emrc=442235
[40] Loveless, Andrew. (7 November 2016). Notional 1FT Voting Architecture with Time-Triggered Ethernet. nasa.gov. https://ntrs.nasa.gov/api/citations/20170001652/downloads/20170001652.pdf
[41] Baggerman, Clint. (2 August 2013). Avionics System Architecture for NASA Orion Vehicle. ntrs.nasa.gov. https://ntrs.nasa.gov/citations/20100040584
````

</details>

<details><summary><b>Step 8 — final</b> (3151 words)</summary>

````text
A Byzantine fault is a condition of a system, particularly a distributed computing system, where a fault occurs such that different symptoms are presented to different observers, including imperfect information on whether a system component has failed. The term takes its name from an allegory, the "Byzantine generals problem",[1] developed to describe a situation in which, to avoid catastrophic failure of a system, the system's actors must agree on a strategy, but some of these actors are unreliable in a way which causes other (good) actors to disagree on the strategy and they may be unaware of the disagreement.

A Byzantine fault is also known as a Byzantine generals problem, a Byzantine agreement problem, or a Byzantine failure.

Byzantine fault tolerance (BFT) is the resilience of a fault-tolerant computer system or similar system to such conditions.

## Definition

A Byzantine fault is any fault presenting different symptoms to different observers.[2] A Byzantine failure is the loss of a system service due to a Byzantine fault in systems that require consensus among multiple components.[3]

The Byzantine allegory considers a number of generals who are attacking a fortress. The generals must decide as a group whether to attack or retreat; some may prefer to attack, while others prefer to retreat. The important thing is that all generals agree on a common decision, for a half-hearted attack by a few generals would become a rout, and would be worse than either a coordinated attack or a coordinated retreat.

The problem is complicated by the presence of treacherous generals who may not only cast a vote for a suboptimal strategy; they may do so selectively. For instance, if nine generals are voting, four of whom support attacking while four others are in favor of retreat, the ninth general may send a vote of retreat to those generals in favor of retreat, and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers). The problem is complicated further by the generals being physically separated and having to send their votes via messengers who may fail to deliver votes or may forge false votes.

Without message signing, Byzantine fault tolerance can only be achieved if the total number of generals is greater than three times the number of disloyal (faulty) generals. There can be a default vote value given to missing messages. For example, missing messages can be given a "null" value. Further, if the agreement is that the null votes are in the majority, a pre-assigned default strategy can be used (e.g., retreat).[4]

The typical mapping of this allegory onto computer systems is that the computers are the generals and their digital communication system links are the messengers. Although the problem is formulated in the allegory as a decision-making and security problem, in electronics, it cannot be solved by cryptographic digital signatures alone, because failures such as incorrect voltages can propagate through the encryption process. Thus, a faulty message could be sent such that some recipients detect the message as faulty (bad signature), others see it is having a good signature, and a third group also sees a good signature but with different message contents than the second group.[2]

## History

The problem of obtaining Byzantine consensus was conceived and formalized by Robert Shostak, who dubbed it the interactive consistency problem. This work was done in 1978 in the context of the NASA-sponsored SIFT[5] project in the Computer Science Lab at SRI International. SIFT (for Software Implemented Fault Tolerance) was the brainchild of John Wensley, and was based on the idea of using multiple general-purpose computers that would communicate through pairwise messaging in order to reach a consensus, even if some of the computers were faulty.

At the beginning of the project, it was not clear how many computers in total were needed to guarantee that a conspiracy of n faulty computers could not "thwart" the efforts of the correctly-operating ones to reach consensus. Shostak showed that a minimum of 3n+1 are needed, and devised a two-round 3n+1 messaging protocol that would work for n=1. His colleague Marshall Pease generalized the algorithm for any n > 0, proving that 3n+1 is both necessary and sufficient. These results, together with a later proof by Leslie Lamport of the sufficiency of 3n using digital signatures, were published in the seminal paper, Reaching Agreement in the Presence of Faults.[6] The authors were awarded the 2005 Edsger W. Dijkstra Prize for this paper.

To make the interactive consistency problem easier to understand, Lamport devised a colorful allegory in which a group of army generals formulate a plan for attacking a city. In its original version, the story cast the generals as commanders of the Albanian army. The name was changed, eventually settling on "Byzantine", at the suggestion of Jack Goldberg to future-proof any potential offense-giving.[7] This formulation of the problem, together with some additional results, were presented by the same authors in their 1982 paper, "The Byzantine Generals Problem".[4]

## Mitigation

The objective of Byzantine fault tolerance is to be able to defend against failures of system components with or without symptoms that prevent other components of the system from reaching an agreement among themselves, where such an agreement is needed for the correct operation of the system.

The remaining operationally correct components of a Byzantine fault tolerant system will be able to continue providing the system's service as originally intended, assuming there are a sufficient number of accurately-operating components to maintain the service.

When considering failure propagation only via errors, Byzantine failures are considered the most general and most difficult class of failures among the failure modes. The so-called fail-stop failure mode occupies the simplest end of the spectrum. Whereas the fail-stop failure mode simply means that the only way to fail is a node crash, detected by other nodes, Byzantine failures imply no restrictions on what errors can be created, which means that a failed node can generate arbitrary data, including data that makes it appear like a functioning node to a subset of other nodes. Thus, Byzantine failures can confuse failure detection systems, which makes fault tolerance difficult. Despite the allegory, a Byzantine failure is not necessarily a security problem involving hostile human interference: it can arise purely from physical or software faults.

The terms fault and failure are used here according to the standard definitions[8] originally created by a joint committee on "Fundamental Concepts and Terminology" formed by the IEEE Computer Society's Technical Committee on Dependable Computing and Fault-Tolerance and IFIP Working Group 10.4 on Dependable Computing and Fault Tolerance.[9] See also dependability.

Byzantine fault tolerance is only concerned with broadcast consistency, that is, the property that when a component broadcasts a value to all the other components, they all receive exactly this same value, or in the case that the broadcaster is not consistent, the other components agree on a common value themselves. This kind of fault tolerance does not encompass the correctness of the value itself; for example, an adversarial component that deliberately sends an incorrect value, but sends that same value consistently to all components, will not be caught in the Byzantine fault tolerance scheme.

## Solutions

Several early solutions were described by Lamport, Shostak, and Pease in 1982.[4] They began by noting that the Generals' Problem can be reduced to solving a "Commander and Lieutenants" problem where loyal Lieutenants must all act in unison and that their action must correspond to what the Commander ordered in the case that the Commander is loyal:

One solution considers scenarios in which messages may be forged, but which will be Byzantine-fault-tolerant as long as the number of disloyal generals is less than one third of the generals. The impossibility of dealing with one-third or more traitors ultimately reduces to proving that the one Commander and two Lieutenants problem cannot be solved, if the Commander is traitorous. To see this, suppose we have a traitorous Commander A, and two Lieutenants, B and C: when A tells B to attack and C to retreat, and B and C send messages to each other, forwarding A's message, neither B nor C can figure out who is the traitor, since it is not necessarily A—the other Lieutenant could have forged the message purportedly from A. It can be shown that if n is the number of generals in total, and t is the number of traitors in that n, then there are solutions to the problem only when n > 3t and the communication is synchronous (bounded delay).[10] The full set of BFT requirements are: For F number of Byzantine failures, there needs to be at least 3F+1 players (fault containment zones), 2F+1 independent communication paths, and F+1 rounds of communication. There can be hybrid fault models in which benign (non-Byzantine) faults as well as Byzantine faults may exist simultaneously. For each additional benign fault that must be tolerated, the above numbers need to be incremented by one. If the BFT rounds of communication do not exist, Byzantine failures can occur even with no faulty hardware.

A second solution requires unforgeable message signatures. Digital signatures can provide Byzantine fault tolerance in the presence of an arbitrary number of traitorous generals provided that n > F+1 (the problem becomes vacuous otherwise). In particular, one Commander and two Lieutenants can reach consensus in the presence of a single traitor since the traitor cannot impersonate others. Solutions based on other cryptographic primitives such as Message Authentication Codes (MACs) were developed later[11].

Also presented is a variation on the first two solutions allowing Byzantine-fault-tolerant behavior in some situations where not all generals can communicate directly with each other.[1]

There are many systems that claim BFT without meeting the above minimum requirements (e.g., blockchain). Given that there is mathematical proof that this is impossible, these claims need to include a caveat that their definition of BFT strays from the original. That is, systems such as blockchain don't guarantee agreement. They use resource-intensive mechanisms that make disagreements impractical to maintain.

Several system architectures were designed c. 1980 that implemented Byzantine fault tolerance. These include: Draper's FTMP,[12] Honeywell's MMFCS,[13] and SRI's SIFT.[5]

In 1999, Miguel Castro and Barbara Liskov introduced the "Practical Byzantine Fault Tolerance" (PBFT) algorithm[11], which provides high-performance Byzantine state machine replication, processing thousands of requests per second with sub-millisecond increases in latency.

After PBFT, several BFT protocols were introduced to improve its robustness and performance. For instance, Q/U,[14] HQ,[15] Zyzzyva,[16] and ABsTRACTs,[17] addressed the performance and cost issues; whereas other protocols, like Aardvark[18] and RBFT,[19] addressed its robustness issues. Furthermore, Adapt[20] tried to make use of existing BFT protocols, through switching between them in an adaptive way, to improve system robustness and performance as the underlying conditions change. Furthermore, BFT protocols were introduced that leverage trusted components to reduce the number of replicas, e.g., A2M-PBFT-EA[21] and MinBFT.[22]

Recent research addresses the scalability limits of traditional BFT implementations (which often incur O(n^2) communication complexity) by parallelizing consensus. For example, the Cerberus protocol maps data to a large, fixed state space to couple consensus instances with specific transaction sets. This allows BFT processes to run independently in parallel, enabling linear scalability relative to the network size.[23]

## Applications

Several examples of Byzantine failures that have occurred are given in two equivalent journal papers.[2,3] These and other examples are described on the NASA DASHlink web pages.[24]

### Applications in computing

Byzantine fault tolerance mechanisms use components that repeat an incoming message (or just its signature, which can be reduced to just a single bit of information if self-checking pairs are used for nodes) to other recipients of that incoming message. All these mechanisms make the assumption that the act of repeating a message blocks the propagation of Byzantine symptoms. For systems that have a high degree of safety or security criticality, these assumptions must be proven to be true to an acceptable level of fault coverage. When providing proof through testing, one difficulty is creating a sufficiently wide range of signals with Byzantine symptoms.[25] Such testing will likely require specialized fault injectors.[26,27]

### Military applications

Byzantine errors were observed infrequently and at irregular points during endurance testing for the newly constructed , at least through 2005 (when the issues were publicly reported).[28]

### Cryptocurrency applications

The Bitcoin network works in parallel to generate a blockchain with proof of work allowing the system to overcome Byzantine failures and reach a coherent global view of the system's state.[29,30] Some proof of stake blockchains also use BFT algorithms.

### Blockchain

Byzantine fault tolerance is a crucial concept in blockchain technology, ensuring that a network can continue to function even when some nodes[31] (participants) fail or act maliciously. This tolerance is necessary because blockchains are decentralized systems with no central authority, making it essential to achieve consensus among nodes, even if some try to disrupt the process.

### Artificial Intelligence

Ensuring that an AI system behaves reliably and as intended, especially in the presence of unexpected faults or adversarial conditions, is a complex challenge. By accepting that components may fail, and further that frontier AI models may deceive, Byzantine fault tolerance has been proposed as an approach towards AI safety.[32] Structuring AI systems as ensembles of AI artifacts or modules that check and balance each other leads to strong assurances that no single errant or deceptive component can easily steer the system into an unsafe state.

### Applications and examples

Safety mechanismsDifferent blockchains use various BFT-based consensus mechanisms like Practical Byzantine Fault Tolerance (PBFT), Tendermint, and Delegated Proof of Stake (DPoS) to handle Byzantine faults. These protocols ensure that the majority of honest nodes can agree on the next block in the chain, securing the network against attacks and preventing double-spending and other types of fraud. Practical examples of networks include Hyperledger Fabric, Cosmos and Klever in this sequence.

51% attack mitigation While traditional blockchains like Bitcoin use proof of work (PoW), which is susceptible to a 51% attack, BFT-based systems are designed to tolerate up to one-third of faulty or malicious nodes without compromising the network's integrity.

Decentralized trust Byzantine fault tolerance underpins the trust model in decentralized networks. Instead of relying on a central authority, the network's security depends on the ability of honest nodes to outnumber and outmaneuver malicious ones.

Private and permissioned blockchains BFT is especially important in private or permissioned blockchains, where a limited number of known participants need to reach a consensus quickly and securely. These networks often use BFT protocols to enhance performance and security.

### In aviation

Some aircraft systems, such as the Boeing 777 Aircraft Information Management System (via its ARINC 659 SAFEbus network), the Boeing 777 flight control system, and the Boeing 787 flight control systems, use Byzantine fault tolerance; because these are real-time systems, their Byzantine fault tolerance solutions must have very low latency. For example, SAFEbus can achieve Byzantine fault tolerance within the order of a microsecond of added latency.[33,34,35]

### In space systems

The SpaceX Dragon considers Byzantine fault tolerance in its design.[36] The Ares rocket avionics, now the Space Launch System (SLS), utilizes a triplex with an interstage of accomplish Byzantine resilience.[37,38] The Orion spacecraft utilizes self-checking pairs to detect and mask Byzantine faults.[39]

### In democracy and civil societies

In legislatures, civil societies, polls, statistical surveys, and so forth, systems that require a minimum supermajority threshold agreement greater than two-thirds are similar to consensus reflective of Byzantine Fault Tolerant -like characteristics. By contrast, systems that operate on the sub-supermajority basis of simple majorities or a minority government could be vulnerable to Byzantine fault -like behavior.

References:
[1] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[2] Driscoll, K.. (2004). The 23rd Digital Avionics Systems Conference (IEEE Cat. No. 04CH37576). doi:10.1109/DASC.2004.1390734
[3] Driscoll, Kevin. (2003). Computer Safety, Reliability, and Security. doi:10.1007/978-3-540-39878-3_19
[4] Lamport, L.. (1982). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. doi:10.1145/357172.357176
[5] (1979). SIFT: design and analysis of a fault-tolerant computer for aircraft control. Microelectronics Reliability. doi:10.1016/0026-2714(79)90211-7
[6] Pease, Marshall. (April 1980). Reaching Agreement in the Presence of Faults. Journal of the Association for Computing Machinery. doi:10.1145/322186.322188
[7] Lamport, Leslie. (2016-12-19). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/
[8] Avizienis, A.. (2004). Basic concepts and taxonomy of dependable and secure computing. IEEE Transactions on Dependable and Secure Computing. doi:10.1109/TDSC.2004.2
[9] Dependable Computing and Fault Tolerance. IEEE Computer Society. http://www.dependability.org
[10] Feldman, P.. (1997). An optimal probabilistic protocol for synchronous Byzantine agreement. SIAM Journal on Computing. doi:10.1137/s0097539790187084
[11] Castro, M.. (2002). Practical Byzantine Fault Tolerance and Proactive Recovery. ACM Transactions on Computer Systems. doi:10.1145/571637.571640
[12] Hopkins, Albert L.. (1987). The Evolution of Fault-Tolerant Computing. doi:10.1007/978-3-7091-8871-2_6
[13] Driscoll, Kevin. (1984). Multi-Microprocessor Flight Control System. AFWAL/FIGL U.S. Air Force Systems Command.
[14] Abd-El-Malek, M.. (2005). Fault-scalable Byzantine Fault-Tolerant Services. ACM SIGOPS Operating Systems Review. doi:10.1145/1095809.1095817
[15] Cowling, James. (2006). HQ Replication: A Hybrid Quorum Protocol for Byzantine Fault Tolerance. http://portal.acm.org/citation.cfm?id=1298455.1298473
[16] Kotla, Ramakrishna. (December 2009). Zyzzyva: Speculative Byzantine Fault Tolerance. ACM Transactions on Computer Systems. doi:10.1145/1658357.1658358
[17] Guerraoui, Rachid. (2010). The Next 700 BFT Protocols. EuroSys. http://infoscience.epfl.ch/record/144158
[18] Clement, A.. (April 22–24, 2009). Making Byzantine Fault Tolerant Systems Tolerate Byzantine Faults. USENIX. http://www.usenix.org/events/nsdi09/tech/full_papers/clement/clement.pdf
[19] Aublin, P.-L.. (July 8–11, 2013). RBFT: Redundant Byzantine Fault Tolerance. International Conference on Distributed Computing Systems. http://www.temple.edu/cis/icdcs2013/program.html
[20] Bahsoun, J. P.. (2015-05-01). 2015 IEEE International Parallel and Distributed Processing Symposium. doi:10.1109/IPDPS.2015.21
[21] Chun, Byung-Gon. (2007-01-01). Proceedings of twenty-first ACM SIGOPS symposium on Operating systems principles. ACM. doi:10.1145/1294261.1294280
[22] Veronese, G. S.. (2013-01-01). Efficient Byzantine Fault-Tolerance. IEEE Transactions on Computers. doi:10.1109/TC.2011.221
[23] Hellings, Jelle. (2021). ByShard: sharding in a byzantine environment. Proceedings of the VLDB Endowment. doi:10.14778/3476249.3476275
[24] Driscoll, Kevin. (2012-12-11). Real System Failures. DASHlink. https://c3.nasa.gov/dashlink/resources/624/
[25] Nanya, T.. (1989). The Byzantine hardware fault model. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. doi:10.1109/43.41508
[26] Martins, Rolando. (2013). Middleware 2013. doi:10.1007/978-3-642-45065-5_3
[27] Method for testing the sensitive input range of Byzantine filters.
[28] Walter, C.. (2005). Ninth IEEE International Symposium on High-Assurance Systems Engineering (HASE'05). doi:10.1109/HASE.2005.23
[29] Rubby, Matt. (20 January 2024). How Byzantine Generals Problem Relates to You in 2024. Swan Bitcoin. https://www.swanbitcoin.com/byzantine-generals-problem/
[30] Tholoniat, Pierre. (2022). Handbook on Blockchain. Springer. doi:10.1007/978-3-031-07535-3_12
[31] Node Operations. https://docs.klever.org/node-operations
[32] deVadoss, John. (2025). A Byzantine Fault Tolerance Approach towards AI Safety.
[33] M., Paulitsch. (9 January 2015). Industrial Communication Technology Handbook. CRC Press.
[34] Rushby, John. (26 September 2001). Bus Architectures For Safety-Critical Embedded Systems. Springer Science & Business Media. http://www.csl.sri.com/papers/emsoft01/emsoft01.pdf
[35] Yeh, Y. C.. (2001). Safety critical avionics for the 777 primary flight controls system. doi:10.1109/DASC.2001.963311
[36] ELC: SpaceX lessons learned. LWN. https://lwn.net/Articles/540368/
[37] SLS (Space Launch System) Avionics: The “Brains” of SLS. nasa.gov. https://www.nasa.gov/wp-content/uploads/2024/12/sls-4964-sls-avionics-fact-sheet-dec2024-508.pdf?emrc=442235
[38] Loveless, Andrew. (7 November 2016). Notional 1FT Voting Architecture with Time-Triggered Ethernet. nasa.gov. https://ntrs.nasa.gov/api/citations/20170001652/downloads/20170001652.pdf
[39] Baggerman, Clint. (2 August 2013). Avionics System Architecture for NASA Orion Vehicle. ntrs.nasa.gov. https://ntrs.nasa.gov/citations/20100040584
````

</details>
