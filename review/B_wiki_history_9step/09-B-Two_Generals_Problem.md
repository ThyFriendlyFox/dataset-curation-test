# 9. Two Generals' Problem

`B-Two_Generals_Problem` · [B_wiki_history_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Two_Generals'_Problem&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 220 revisions in history; 29 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 3 | 0 | 0.00 | source_title |
| 1 | revision_1 | 483 | 0 | 0.26 | enwiki rev 39448056 (2006-02-13) |
| 2 | revision_2 | 916 | 0 | 0.48 | enwiki rev 52746370 (2006-05-11) |
| 3 | revision_3 | 1215 | 0 | 0.57 | enwiki rev 154831579 (2007-08-31) |
| 4 | revision_4 | 1422 | 4 | 0.65 | enwiki rev 439304735 (2011-07-13) |
| 5 | revision_5 | 1597 | 4 | 0.74 | enwiki rev 552635985 (2013-04-28) |
| 6 | revision_6 | 1856 | 5 | 0.84 | enwiki rev 911979564 (2019-08-22) |
| 7 | revision_7 | 1688 | 4 | 0.93 | enwiki rev 1059453358 (2021-12-09) |
| 8 | final | 1737 | 9 | 1.00 | enwiki rev 1376663237 (2026-09-25) |

<details><summary><b>Step 0 — title</b> (3 words)</summary>

````text
Two Generals' Problem
````

</details>

<details><summary><b>Step 1 — revision_1</b> (483 words)</summary>

````text
In computing, the Two Generals' Problem is a thought experiment meant to illustrate the pitfalls and design challenges of communicating over an unreliable link. It is a simplification of the more general Byzantine Generals' Problem and appears often in introductory classes about computer networking (particularly with regards to the Transport Control Protocol), although it can also apply to other types of communication.

## Definition

Two armies, each led by a general, are preparing to attack a city. The armies are encamped outside of the city, each on its own hill. A valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders, and there is a chance that any given messenger sent through the valley will be captured. Note that the two generals have never met beforehand to arrange a schedule or anything of the sort; each general has no idea when and if the other will send a messenger, nor do they know (immediately) whether a messenger they have sent was captured or not, or how long it will take for any individual messenger to reach the other side.

The two generals must attack the city at the same time to succeed. They must thus communicate with each other to decide on a time to attack. The thought experiment involves considering how they might go about doing this.

## Provable Uncertainty

The first general may start by sending a message "Let us attack at 9 o'clock in the morning." However, once dispatched, the first general has no idea whether or not the messenger got through. Any amount of uncertainty may lead the first general to hesitate to attack, since if the second general does not also attack at that time, the city will repel the advance. Knowing this, the second general may send a confirmation back to the first: "I received your message and will attack at 9 o'clock." However, what if the confirmation messenger were captured? The second general, knowing that the first will hesitate without the confirmation, may himself hesitate. A solution would be to have the first general send a second confirmation: "I received your confirmation of the planned attack." However, what if that messenger were captured? It quickly becomes evident that no matter how many rounds of confirmation are made, neither general can be absolutely sure of the other's plans.

## Engineering Solutions

The "solution" to the two generals' problem is to use schemes that acknowledge the uncertainty of the communications link and do not attempt to eliminate it, but rather to mediate it to an acceptable degree. For example, the generals could send 100 messengers each time, knowing that the probability of all being captured is low; or they could continue sending messengers until a confirmation is received, using sequence numbers to keep track of each message.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (916 words)</summary>

````text
In computing, the Two Generals' Problem is a thought experiment meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. It is related to the more general Byzantine Generals' Problem (though published long before later generalization) and appears often in introductory classes about computer networking (particularly with regards to the Transport Control Protocol), though it can also apply to other types of communication.

## Definition

Two armies, each led by a general, are preparing to attack a city. The armies are encamped outside of the city, each on its own hill. A valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders and there's a chance that any given messenger sent through the valley will be captured. Note that the two generals haven't agreed upon a time of attack before taking up their positions on their respective hills.

The two generals must attack the city at the same time to succeed. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time. The thought experiment involves considering how they might go about doing this. In its simplest form one general (referred to as the "first general" below) is known to be the leader, decides on the time of attack, and must communicate this time to the other general. The requirement that causes the "problem" is that either both generals must attack at the agreed upon time to succeed. Having a single general attack is considered a disastrous failure.

## Illustrating the Problem

The first general may start by sending a message "Let us attack at 9 o'clock in the morning." However, once dispatched, the first general has no idea whether or not the messenger got through. Any amount of uncertainty may lead the first general to hesitate to attack, since if the second general does not also attack at that time, the city will repel the advance, with grievous losses for that attacking general. Knowing this, the second general may send a confirmation back to the first: "I received your message and will attack at 9 o'clock." However, what if the confirmation messenger were captured? The second general, knowing that the first will hesitate without the confirmation, may himself hesitate. A solution might seem to be to have the first general send a second confirmation: "I received your confirmation of the planned attack." However, what if that messenger were captured? It quickly becomes evident that no matter how many rounds of confirmation are made there is no way to guarantee the second requirement that both generals agree the message was delivered.

## Proof

Suppose there is any sequence of messages, some successfully delivered and some not, which suffice to meet the requirement of shared certainty. In that case there must be some minimal subset of the successfully delivered messages that suffices. Consider the last such message that was successfully delivered. If that message had not been successfully delivered then the requirement wouldn't have been met. However, the sender of that last message has no way of knowing whether or not that message was delivered and so can't be certain that the message was delivered and the criteria were met. If the sender attacks and the message wasn't delivered then the requirement will fail to be met because not receiving that message will keep the other general from getting the assurance needed to attack. Alternatively if the sender doesn't attack and the message was delivered then the requirement will fail to be met as the receiver will attack. This contradicts the original assumption about achieving shared certainty.

## Engineering Approaches

A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the uncertainty of the communications channel and do not attempt to eliminate it, but rather mediate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach the first general will attack no matter what and the second general will attack if any message is received. Alternatively the first general could send a stream messages and the second general could send acknowledgements to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There's no algorithm that they can use (e.g. attack if more than 4 messages are received) which will be certain to prevent one from attacking without the other. If the channel can be made to be reliable then one message will suffice and additional messages do not help. The last is a likely to get lost as the first.

## History

The Two Generals' Problem and it's impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Tradeoffs in the Design of Network Communications" where it's described starting on page 73 in the context of communication between two groups of gangsters.

This problem was given the name the Two Generals Paradox by Jim Grey in 1978 in "Notes on Data Base Operating Systems" starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as above.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (1215 words)</summary>

````text
In computing, the Two Generals' Problem is a thought experiment meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. It is related to the more general Byzantine Generals' Problem (though published long before that later generalization) and appears often in introductory classes about computer networking (particularly with regards to the Transmission Control Protocol), though it can also apply to other types of communication. Some authors also refer to this as the Two army problem.

## Definition

Two armies, each led by a general, are preparing to attack a city. The armies are encamped outside of the city, each on its own hill. A valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders and there's a chance that any given messenger sent through the valley will be captured. Note that while the two generals have agreed that they will attack, they haven't agreed upon a time for attack before taking up their positions on their respective hills.

The two generals must attack the city at the same time to succeed. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time. The thought experiment involves considering how they might go about doing this. In its simplest form one general (referred to as the "first general" below) is known to be the leader, decides on the time of attack, and must communicate this time to the other general. The requirement that causes the "problem" is that both generals must attack at the agreed upon time to succeed. Having a single general attack is considered a disastrous failure. The problem is to come up with algorithms that the generals can use, including sending messages and processing received messages, that can allow them to correctly conclude:

Yes, we will both attack at the agreed upon time.

Note that it is quite simple for the generals to come to an agreement on the time to attack. One successful message with a successful acknowledgement suffices for that. The subtlety of the Two Generals' Problem is in the impossibility of designing algorithms for the generals to use to safely agree to the above statement.

## Illustrating the problem

The first general may start by sending a message "Let us attack at 9 o'clock in the morning." However, once dispatched, the first general has no idea whether or not the messenger got through. Any amount of uncertainty may lead the first general to hesitate to attack, since if the second general does not also attack at that time, the city will repel the advance, with grievous losses for that attacking general. Knowing this, the second general may send a confirmation back to the first: "I received your message and will attack at 9 o'clock." However, what if the confirmation messenger were captured? The second general, knowing that the first will hesitate without the confirmation, may himself hesitate. A solution might seem to be to have the first general send a second confirmation: "I received your confirmation of the planned attack." However, what if that messenger were captured? It quickly becomes evident that no matter how many rounds of confirmation are made there is no way to guarantee the second requirement that both generals agree the message was delivered.

## Proof

### For deterministic protocols with a fixed number of messages

Suppose there is any fixed-length sequence of messages, some successfully delivered and some not, that suffice to meet the requirement of shared certainty for both generals to attack. In that case there must be some minimal subset of the successfully delivered messages that suffices (at least one message with the time/plan must be delivered). Consider the last such message that was successfully delivered in such a minimal sequence. If that last message had not been successfully delivered then the requirement wouldn't have been met and one general at least (presumably the receiver) would decide not to attack. From the viewpoint of the sender of that last message, however, the sequence of messages sent and delivered is exactly the same as it would have been had that message been delivered. Therefore the general sending that last message will still decide to attack (since the protocol is deterministic). We've now constructed a circumstance where with the purported solution algorithms one general will attack and the other will not - contradicting the assumption that the algorithms were a solution to the problem.

### For nondeterministic and variable-length protocols

Such a protocol can be modelled as a labelled finite forest, where each node

represents a run of the protocol up to a specified point. The roots are labelled

with the possible starting messages, and the children of a node N are labelled

with the possible next messages after N. Leaf nodes represent runs in which the

protocol terminates after sending the message the node is labelled with. The

empty forest represents the protocol that terminates before sending any message.

Let P be a protocol that solves the Two Generals' problem. Then, by a

similar argument to the one used for fixed-length protocols above, P' must also solve

the Two Generals' problem, where P' is obtained from P by removing all

leaf nodes. Since P is finite, it follows that the protocol represented by the

empty forest solves the coordinated attack problem. But clearly it does not,

contradicting the existence of P.

## Engineering approaches

A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the uncertainty of the communications channel and do not attempt to eliminate it, but rather mediate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach the first general will attack no matter what and the second general will attack if any message is received. Alternatively the first general could send a stream of messages and the second general could send acknowledgements to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There's no algorithm that they can use (e.g. attack if more than 4 messages are received) which will be certain to prevent one from attacking without the other. If the channel can be made to be reliable then one message will suffice and additional messages do not help. The last is as likely to get lost as the first.

## History

The Two Generals' Problem and its impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Tradeoffs in the Design of Network Communications" where it's described starting on page 73 in the context of communication between two groups of gangsters.

This problem was given the name the Two Generals Paradox by Jim Gray in 1978 in "Notes on Data Base Operating Systems" starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as above.

ru:Задача двух генералов
````

</details>

<details><summary><b>Step 4 — revision_4</b> (1422 words)</summary>

````text
In computing, the Two Generals' Problem is a thought experiment meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. It is related to the more general Byzantine Generals' Problem (though published long before that later generalization) and appears often in introductory classes about computer networking (particularly with regard to the Transmission Control Protocol), though it can also apply to other types of communication. It is also an important concept in epistemic logic, and the importance of common knowledge. Some authors refer to this as the Two Armies Problem or the Coordinated Attack Problem.[1,2]

## Definition

Two armies, each led by a general, are preparing to attack a fortified city. The armies are encamped near the city, each on its own hill. A valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders and there's a chance that any given messenger sent through the valley will be captured. Note that while the two generals have agreed that they will attack, they haven't agreed upon a time for attack before taking up their positions on their respective hills.

The two generals must have their armies attack the city at the same time in order to succeed. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time, and each general must know that the other general knows that they have agreed to the attack plan. Because acknowledgement of message receipt can be lost as easily as the original message, a potentially infinite series of messages is required to come to consensus.

The thought experiment involves considering how they might go about coming to consensus. In its simplest form one general (referred to as the "first general" below) is known to be the leader, decides on the time of attack, and must communicate this time to the other general. The requirement that causes the "problem" is that both generals must attack at the agreed-upon time to succeed. Having a solitary general attack is considered a disastrous failure. The problem is to come up with algorithms that the generals can use, including sending messages and processing received messages, that can allow them to correctly conclude:

Yes, we will both attack at the agreed-upon time.

Note that it is quite simple for the generals to come to an agreement on the time to attack. One successful message with a successful acknowledgement suffices for that. The subtlety of the Two Generals' Problem is in the impossibility of designing algorithms for the generals to use to safely agree to the above statement.

## Illustrating the problem

The first general may start by sending a message "Let us attack at 0900 on August 4." However, once dispatched, the first general has no idea whether or not the messenger got through. Any amount of uncertainty may lead the first general to hesitate to attack, since if the second general does not also attack at that time, the city's garrison will repel the advance, leading to the destruction of that attacking general's forces.

Knowing this, the second general may send a confirmation back to the first: "I received your message and will attack at 0900 on August 4." However, what if the confirmation messenger were captured? Or what if the message was merely a ruse of the enemy? The second general, knowing that the first will hesitate without the confirmation, may himself hesitate.

A solution might seem to be to have the first general send a second confirmation: "I received your confirmation of the planned attack at 0900 on August 4." However, what if that messenger were captured? It quickly becomes evident that no matter how many rounds of confirmation are made, there is no way to guarantee the second requirement that both generals agree the message was delivered and that the enemy did not alter any of the messages.

## Proof

### For deterministic protocols with a fixed number of messages

Suppose there is any fixed-length sequence of messages, some successfully delivered and some not, that suffice to meet the requirement of shared certainty for both generals to attack. In that case there must be some minimal non-empty subset of the successfully delivered messages that suffices (at least one message with the time/plan must be delivered). Consider the last such message that was successfully delivered in such a minimal sequence. If that last message had not been successfully delivered then the requirement wouldn't have been met, and one general at least (presumably the receiver) would decide not to attack. From the viewpoint of the sender of that last message, however, the sequence of messages sent and delivered is exactly the same as it would have been, had that message been delivered. Therefore the general sending that last message will still decide to attack (since the protocol is deterministic). We've now constructed a circumstance where the purported protocol leads one general to attack and the other not to attack - contradicting the assumption that the protocol was a solution to the problem.

### For nondeterministic and variable-length protocols

Such a protocol can be modeled as a labeled finite forest, where each node

represents a run of the protocol up to a specified point. The roots are labeled

with the possible starting messages, and the children of a node N are labeled

with the possible next messages after N. Leaf nodes represent runs in which the

protocol terminates after sending the message the node is labeled with. The

empty forest represents the protocol that terminates before sending any message.

Let P be a protocol that solves the Two Generals' problem. Then, by a

similar argument to the one used for fixed-length protocols above, P' must also solve

the Two Generals' problem, where P' is obtained from P by removing all

leaf nodes. Since P is finite, it follows that the protocol represented by the

empty forest solves the Two Generals' problem. But clearly it does not,

contradicting the existence of P.

## Engineering approaches

A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the uncertainty of the communications channel and not attempt to eliminate it, but rather mitigate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach the first general will attack no matter what, and the second general will attack if any message is received. Alternatively the first general could send a stream of messages and the second general could send acknowledgments to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There's no algorithm that they can use (e.g. attack if more than four messages are received) which will be certain to prevent one from attacking without the other. Also, the first general can send a marking on each message saying it is message 1, 2, 3 ... of n. This method will allow the second general to know how reliable the channel is and send an appropriate number of messages back to ensure a high probability of at least one message being received. If the channel can be made to be reliable, then one message will suffice and additional messages do not help. The last is as likely to get lost as the first.

## History

The Two Generals' Problem and its impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Trade-offs in the Design of Network Communications",[3] where it is described starting on page 73 in the context of communication between two groups of gangsters.

This problem was given the name the Two Generals Paradox by Jim Gray[4] in 1978 in "Notes on Data Base Operating Systems"[5] starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as above.

References:
[1] Decision-theoretic recursive modeling and the coordinated attack problem. Portal.acm.org. http://portal.acm.org/citation.cfm?id=139492.139503
[2] The coordinated attack and the jealous amazons Alessandro Panconesi. Retrieved 2011-05-17.
[3] Some constraints and trade-offs in the design of network communications. Portal.acm.org. http://portal.acm.org/citation.cfm?id=806523
[4] (2004-05-03). Jim Gray Summary Home Page. Research.microsoft.com. http://research.microsoft.com/~Gray/JimGrayHomePageSummary.htm
[5] Notes on Data Base Operating Systems. Portal.acm.org. http://portal.acm.org/citation.cfm?coll=GUIDE&dl=GUIDE&id=723863
````

</details>

<details><summary><b>Step 5 — revision_5</b> (1597 words)</summary>

````text
In computing, the Two Generals' Problem is a thought experiment meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. It is related to the more general Byzantine Generals' Problem (though published long before that later generalization) and appears often in introductory classes about computer networking (particularly with regard to the Transmission Control Protocol), though it can also apply to other types of communication. A key concept in epistemic logic, this problem highlights the importance of common knowledge. Some authors also refer to this as the Two Armies Problem or the Coordinated Attack Problem.[1,2]

## Definition

Two armies, each led by a general, are preparing to attack a fortified city. The armies are encamped near the city, each on its own hill. A valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders and there's a chance that any given messenger sent through the valley will be captured (this scenario assumes that while the two generals have agreed that they will attack, they haven't agreed upon a time for attack before taking up their positions on their respective hills).

The two generals must have their armies attack the city at the same time in order to succeed. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time, and each general must know that the other general knows that they have agreed to the attack plan. Because acknowledgement of message receipt can be lost as easily as the original message, a potentially infinite series of messages are required to come to consensus.

The thought experiment involves considering how they might go about coming to consensus. In its simplest form one general (referred to as the "first general" below) is known to be the leader, decides on the time of attack, and must communicate this time to the other general. The requirement that causes the "problem" is that both generals must attack at the agreed-upon time to succeed. Having a solitary general attack is considered a disastrous failure. The problem is to come up with algorithms that the generals can use, including sending messages and processing received messages, that can allow them to correctly conclude:

Yes, we will both attack at the agreed-upon time.

Allowing that it is quite simple for the generals to come to an agreement on the time to attack (i.e. one successful message with a successful acknowledgement), the subtlety of the Two Generals' Problem is in the impossibility of designing algorithms for the generals to use to safely agree to the above statement.

## Illustrating the problem

The first general may start by sending a message "Let us attack at 0900 on August 4." However, once dispatched, the first general has no idea whether or not the messenger got through. Any amount of uncertainty may lead the first general to hesitate to attack, since if the second general does not also attack at that time, the city's garrison will repel the advance, leading to the destruction of that attacking general's forces.

Knowing this, the second general may send a confirmation back to the first: "I received your message and will attack at 0900 on August 4." However, if the confirmation messenger were captured, the second general (knowing that the first will hesitate without the confirmation) may himself hesitate.

A solution might seem to be to have the first general send a second confirmation: "I received your confirmation of the planned attack at 0900 on August 4." However, if that messenger were captured, it quickly becomes evident that no matter how many rounds of confirmation are made, there is no way to guarantee the second requirement that both generals agree the message was delivered and that the enemy did not alter any of the messages.

## Proof

### For deterministic protocols with a fixed number of messages

Suppose there is any fixed-length sequence of messages, some successfully delivered and some not, that suffice to meet the requirement of shared certainty for both generals to attack. In that case there must be some minimal non-empty subset of the successfully delivered messages that suffices (at least one message with the time/plan must be delivered). Consider the last such message that was successfully delivered in such a minimal sequence. If that last message had not been successfully delivered then the requirement wouldn't have been met, and one general at least (presumably the receiver) would decide not to attack. From the viewpoint of the sender of that last message, however, the sequence of messages sent and delivered is exactly the same as it would have been, had that message been delivered. Therefore the general sending that last message will still decide to attack (since the protocol is deterministic). We've now constructed a circumstance where the purported protocol leads one general to attack and the other not to attack - contradicting the assumption that the protocol was a solution to the problem.

### For nondeterministic and variable-length protocols

Such a protocol can be modeled as a labeled finite forest, where each node

represents a run of the protocol up to a specified point. The roots are labeled

with the possible starting messages, and the children of a node N are labeled

with the possible next messages after N. Leaf nodes represent runs in which the

protocol terminates after sending the message the node is labeled with. The

empty forest represents the protocol that terminates before sending any message.

Let P be a protocol that solves the Two Generals' problem. Then, by a

similar argument to the one used for fixed-length protocols above, P' must also solve

the Two Generals' problem, where P' is obtained from P by removing all

leaf nodes. Since P is finite, it follows that the protocol represented by the

empty forest solves the Two Generals' problem. But clearly it does not,

contradicting the existence of P.

## Engineering approaches

A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the uncertainty of the communications channel and not attempt to eliminate it, but rather mitigate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach the first general will attack no matter what, and the second general will attack if any message is received. Alternatively the first general could send a stream of messages and the second general could send acknowledgments to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There's no algorithm that they can use (e.g. attack if more than four messages are received) which will be certain to prevent one from attacking without the other. Also, the first general can send a marking on each message saying it is message 1, 2, 3 ... of n. This method will allow the second general to know how reliable the channel is and send an appropriate number of messages back to ensure a high probability of at least one message being received. If the channel can be made to be reliable, then one message will suffice and additional messages do not help. The last is as likely to get lost as the first.

Assuming that the generals must sacrifice lives every time a messenger is sent and intercepted, an algorithm can be designed to minimize the amount of messengers required to achieve the maximum amount of confidence the attack is coordinated. To save us from sacrificing hundreds of lives to achieve a very high confidence in coordination, the generals could agree to use the absence of messengers as an indication that the general who began the transaction has received at least one confirmation, and has promised to attack. Suppose it takes a messenger 1 minute to cross the danger zone, allowing 200 minutes of silence to occur after confirmations have been received will allow us to achieve extremely high confidence while not sacrificing messenger lives. In this case messengers are used only in the case where a party has not received the attack time. At the end of 200 minutes, each general can reason: "I have not received an additional message for 200 minutes; either 200 messengers failed to cross the danger zone, or it means the other general has confirmed and committed to the attack and has faith I will too".

## History

The Two Generals' Problem and its impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Trade-offs in the Design of Network Communications",[3] where it is described starting on page 73 in the context of communication between two groups of gangsters.

This problem was given the name the Two Generals Paradox by Jim Gray[4] in 1978 in "Notes on Data Base Operating Systems"[5] starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as above.

References:
[1] Decision-theoretic recursive modeling and the coordinated attack problem. Portal.acm.org. http://portal.acm.org/citation.cfm?id=139492.139503
[2] The coordinated attack and the jealous amazons Alessandro Panconesi. Retrieved 2011-05-17.
[3] Some constraints and trade-offs in the design of network communications. Portal.acm.org. http://portal.acm.org/citation.cfm?id=806523
[4] (2004-05-03). Jim Gray Summary Home Page. Research.microsoft.com. http://research.microsoft.com/~Gray/JimGrayHomePageSummary.htm
[5] Notes on Data Base Operating Systems. Portal.acm.org. http://portal.acm.org/citation.cfm?coll=GUIDE&dl=GUIDE&id=723863
````

</details>

<details><summary><b>Step 6 — revision_6</b> (1856 words)</summary>

````text
In computing, the Two Generals Problem is a thought experiment meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. In the experiment, two generals are only able to communicate with one another by sending a messenger through enemy territory. The experiment asks how they might reach an agreement on the time to launch an attack, while knowing that any messenger they send could be captured.

It is related to the more general Byzantine Generals Problem and appears often in introductory classes about computer networking (particularly with regard to the Transmission Control Protocol, where it shows that TCP can't guarantee state consistency between endpoints and why this is the case), though it applies to any type of two-party communication where failures of communication are possible. A key concept in epistemic logic, this problem highlights the importance of common knowledge. Some authors also refer to this as the Two Generals Paradox, the Two Armies Problem, or the Coordinated Attack Problem.[1,2] The Two Generals Problem was the first computer communication problem to be proved to be unsolvable. An important consequence of this proof is that generalizations like the Byzantine Generals problem are also unsolvable in the face of arbitrary communication failures, thus providing a base of realistic expectations for any distributed consistency protocols.

## Definition

Two armies, each led by a different general, are preparing to attack a fortified city. The armies are encamped near the city, each in its own valley. A third valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders and there's a chance that any given messenger sent through the valley will be captured.

While the two generals have agreed that they will attack, they haven't agreed upon a time for attack. It is required that the two generals have their armies attack the city at the same time in order to succeed, else the lone attacker army will die trying. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time, and each general must know that the other general knows that they have agreed to the attack plan. Because acknowledgement of message receipt can be lost as easily as the original message, a potentially infinite series of messages is required to come to consensus.

The thought experiment involves considering how they might go about coming to consensus. In its simplest form one general is known to be the leader, decides on the time of attack, and must communicate this time to the other general. The problem is to come up with algorithms that the generals can use, including sending messages and processing received messages, that can allow them to correctly conclude:

Yes, we will both attack at the agreed-upon time.

Allowing that it is quite simple for the generals to come to an agreement on the time to attack (i.e. one successful message with a successful acknowledgement), the subtlety of the Two Generals' Problem is in the impossibility of designing algorithms for the generals to use to safely agree to the above statement.

## Illustrating the problem

The first general may start by sending a message "Attack at 0900 on August 4." However, once dispatched, the first general has no idea whether or not the messenger got through. This uncertainty may lead the first general to hesitate to attack due to the risk of being the sole attacker.

To be sure, the second general may send a confirmation back to the first: "I received your message and will attack at 0900 on August 4." However, the messenger carrying the confirmation could face capture and the second general may hesitate, knowing that the first might hold back without the confirmation.

Further confirmations may seem like a solution—let the first general send a second confirmation: "I received your confirmation of the planned attack at 0900 on August 4." However, this new messenger from the first general is liable to be captured, too. Thus it quickly becomes evident that no matter how many rounds of confirmation are made, there is no way to guarantee the second requirement that each general be sure the other has agreed to the attack plan. Both generals will always be left wondering whether their last messenger got through.

## Proof

### For deterministic protocols with a fixed number of messages

Because this protocol is deterministic, suppose there is a sequence of a fixed number of messages, one or more successfully delivered and one or more not. The assumption is that there should be a shared certainty for both generals to attack.

Consider the last such message that was successfully delivered. If that last message had not been successfully delivered, then one general at least (presumably the receiver) would decide not to attack. From the viewpoint of the sender of that last message, however, the sequence of messages sent and delivered is exactly the same as it would have been, had that message been delivered.

Since the protocol is deterministic, the general sending that last message will still decide to attack.

We've now created a situation where the suggested protocol leads one general to attack and the other not to attack—contradicting the assumption that the protocol was a solution to the problem.

### For nondeterministic and variable-length protocols

A nondeterministic protocol with a variable message count can be compared to a finite tree, where each leaf or branch (node) in the tree represents an explored example up to a specified point.

The roots of this tree are labeled with the possible starting messages, and the branch nodes stemming from these roots are labeled with the possible next messages. Leaf nodes represent examples which end after sending the last message. A protocol that terminates before sending any messages is represented by a null tree.

Suppose there exists a nondeterministic protocol which solves the problem. Then, by a similar argument to the deterministic example in the previous section, where a deterministic protocol can be obtained from the non-deterministic one by removing all leaf nodes, the deterministic protocol must then also solve the problem.

Since the nondeterministic protocol is finite, it then follows that the protocol represented by the empty tree would solve the problem. Clearly this is not possible. Therefore a nondeterministic protocol which solves the problem cannot exist.[3]

### Proof by symmetry

Because the problem is devised in such a way that the defender cannot be distinguished with one of the attackers, for all theoretical purposes the defender acts as one of the attackers but inverts the message of the other attacker. Since no message can distinguish the defender from one of the attackers it is impossible to coordinate. This can be seen by simply removing one attacker and treating the problem as two players that must coordinate but in which one always can thwart any coordination(through error or intent). The only solution to the problem is to be able to distinguish the defender from the attacker which solves the problem trivially.

These problems show up in many games such as chess where one player can always make a move that prevents the other from achieving an end goal such as perpetual check and which external "rules" must be imposed to get around it.

## Engineering approaches

A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the uncertainty of the communications channel and not attempt to eliminate it, but rather mitigate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach the first general will attack no matter what, and the second general will attack if any message is received. Alternatively the first general could send a stream of messages and the second general could send acknowledgments to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There's no algorithm that they can use (e.g. attack if more than four messages are received) which will be certain to prevent one from attacking without the other. Also, the first general can send a marking on each message saying it is message 1, 2, 3 ... of n. This method will allow the second general to know how reliable the channel is and send an appropriate number of messages back to ensure a high probability of at least one message being received. If the channel can be made to be reliable, then one message will suffice and additional messages do not help. The last is as likely to get lost as the first.

Assuming that the generals must sacrifice lives every time a messenger is sent and intercepted, an algorithm can be designed to minimize the number of messengers required to achieve the maximum amount of confidence the attack is coordinated. To save them from sacrificing hundreds of lives to achieve a very high confidence in coordination, the generals could agree to use the absence of messengers as an indication that the general who began the transaction has received at least one confirmation, and has promised to attack. Suppose it takes a messenger 1 minute to cross the danger zone, allowing 200 minutes of silence to occur after confirmations have been received will allow us to achieve extremely high confidence while not sacrificing messenger lives. In this case messengers are used only in the case where a party has not received the attack time. At the end of 200 minutes, each general can reason: "I have not received an additional message for 200 minutes; either 200 messengers failed to cross the danger zone, or it means the other general has confirmed and committed to the attack and has confidence I will too".

## History

The Two Generals Problem and its impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Trade-offs in the Design of Network Communications",[4] where it is described starting on page 73 in the context of communication between two groups of gangsters.

This problem was given the name the Two Generals Paradox by Jim Gray[5] in 1978 in "Notes on Data Base Operating Systems"[6] starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as mentioned above.

References:
[1] Gmytrasiewicz, Piotr J.. (1992). Decision-theoretic recursive modeling and the coordinated attack problem. Proceedings of the First International Conference on Artificial Intelligence Planning Systems. doi:10.1016/B978-0-08-049944-4.50016-1
[2] The coordinated attack and the jealous amazons Alessandro Panconesi. Retrieved 2011-05-17.
[3] Kennard, Fredrick. Thought Experiments: Popular Thought Experiments in Philosophy, Physics, Ethics, Computer Science & Mathematics. Lulu.com. https://books.google.nl/books?id=sX-pCQAAQBAJ
[4] Akkoyunlu, E. A.. (1975). Some constraints and trade-offs in the design of network communications. Portal.acm.org. doi:10.1145/800213.806523
[5] (2004-05-03). Jim Gray Summary Home Page. Research.microsoft.com. http://research.microsoft.com/~Gray/JimGrayHomePageSummary.htm
[6] Notes on Data Base Operating Systems. Portal.acm.org. http://portal.acm.org/citation.cfm?coll=GUIDE&dl=GUIDE&id=723863
````

</details>

<details><summary><b>Step 7 — revision_7</b> (1688 words)</summary>

````text
In computing, the Two Generals' Problem is a thought experiment meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. In the experiment, two generals are only able to communicate with one another by sending a messenger through enemy territory. The experiment asks how they might reach an agreement on the time to launch an attack, while knowing that any messenger they send could be captured.

It is related to the more general Byzantine Generals Problem and appears often in introductory classes about computer networking (particularly with regard to the Transmission Control Protocol, where it shows that TCP can't guarantee state consistency between endpoints and why this is the case), though it applies to any type of two-party communication where failures of communication are possible. A key concept in epistemic logic, this problem highlights the importance of common knowledge. Some authors also refer to this as the Two Generals' Paradox, the Two Armies Problem, or the Coordinated Attack Problem.[1,2] The Two Generals' Problem was the first computer communication problem to be proved to be unsolvable. An important consequence of this proof is that generalizations like the Byzantine Generals problem are also unsolvable in the face of arbitrary communication failures, thus providing a base of realistic expectations for any distributed consistency protocols.

## Definition

Two armies, each led by a different general, are preparing to attack a fortified city. The armies are encamped near the city, each in its own valley. A third valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders and there's a chance that any given messenger sent through the valley will be captured.

While the two generals have agreed that they will attack, they haven't agreed upon a time for attack. It is required that the two generals have their armies attack the city at the same time in order to succeed, lest the lone attacker army will die trying. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time, and each general must know that the other general knows that they have agreed to the attack plan. Because acknowledgement of message receipt can be lost as easily as the original message, a potentially infinite series of messages is required to come to consensus.

The thought experiment involves considering how they might go about coming to consensus. In its simplest form one general is known to be the leader, decides on the time of attack, and must communicate this time to the other general. The problem is to come up with algorithms that the generals can use, including sending messages and processing received messages, that can allow them to correctly conclude:

Yes, we will both attack at the agreed-upon time.

Allowing that it is quite simple for the generals to come to an agreement on the time to attack (i.e. one successful message with a successful acknowledgement), the subtlety of the Two Generals' Problem is in the impossibility of designing algorithms for the generals to use to safely agree to the above statement.

## Illustrating the problem

The first general may start by sending a message "Attack at 0900 on August 4." However, once dispatched, the first general has no idea whether or not the messenger got through. This uncertainty may lead the first general to hesitate to attack due to the risk of being the sole attacker.

To be sure, the second general may send a confirmation back to the first: "I received your message and will attack at 0900 on August 4." However, the messenger carrying the confirmation could face capture and the second general may hesitate, knowing that the first might hold back without the confirmation.

Further confirmations may seem like a solution—let the first general send a second confirmation: "I received your confirmation of the planned attack at 0900 on August 4." However, this new messenger from the first general is liable to be captured, too. Thus it quickly becomes evident that no matter how many rounds of confirmation are made, there is no way to guarantee the second requirement that each general be sure the other has agreed to the attack plan. Both generals will always be left wondering whether their last messenger got through.

## Proof

### For deterministic protocols with a fixed number of messages

Because this protocol is deterministic, suppose there is a sequence of a fixed number of messages, one or more successfully delivered and one or more not. The assumption is that there should be a shared certainty for both generals to attack.

Consider the last such message that was successfully delivered. If that last message had not been successfully delivered, then one general at least (presumably the receiver) would decide not to attack. From the viewpoint of the sender of that last message, however, the sequence of messages sent and delivered is exactly the same as it would have been, had that message been delivered.

Since the protocol is deterministic, the general sending that last message will still decide to attack.

We've now created a situation where the suggested protocol leads one general to attack and the other not to attack—contradicting the assumption that the protocol was a solution to the problem.

### For nondeterministic and variable-length protocols

A nondeterministic protocol with a potentially variable message count can be compared to an edge-labeled finite tree, where each node in the tree represents an explored example up to a specified point. A protocol that terminates before sending any messages is represented by a tree containing only a root node. The edges from a node to each child are labeled with the messages sent in order to reach the child state. Leaf nodes represent points at which the protocol terminates.

Suppose there exists a nondeterministic protocol P which solves the Two Generals' Problem. Then, by a similar argument to the one used for fixed-length deterministic protocols above, P' must also solve the Two Generals' Problem, where the tree representing P' is obtained from that for P by removing all leaf nodes and the edges leading to them.

Since P is finite, it then follows that the protocol that terminates before sending any messages would solve the problem. But clearly it does not. Therefore a nondeterministic protocol which solves the problem cannot exist.

## Engineering approaches

A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the uncertainty of the communications channel and not attempt to eliminate it, but rather mitigate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach the first general will attack no matter what, and the second general will attack if any message is received. Alternatively the first general could send a stream of messages and the second general could send acknowledgments to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There is no algorithm that they can use (e.g. attack if more than four messages are received) which will be certain to prevent one from attacking without the other. Also, the first general can send a marking on each message saying it is message 1, 2, 3 ... of n. This method will allow the second general to know how reliable the channel is and send an appropriate number of messages back to ensure a high probability of at least one message being received. If the channel can be made to be reliable, then one message will suffice and additional messages do not help. The last is as likely to get lost as the first.

Assuming that the generals must sacrifice lives every time a messenger is sent and intercepted, an algorithm can be designed to minimize the number of messengers required to achieve the maximum amount of confidence the attack is coordinated. To save them from sacrificing hundreds of lives to achieve a very high confidence in coordination, the generals could agree to use the absence of messengers as an indication that the general who began the transaction has received at least one confirmation, and has promised to attack. Suppose it takes a messenger 1 minute to cross the danger zone, allowing 200 minutes of silence to occur after confirmations have been received will allow us to achieve extremely high confidence while not sacrificing messenger lives. In this case messengers are used only in the case where a party has not received the attack time. At the end of 200 minutes, each general can reason: "I have not received an additional message for 200 minutes; either 200 messengers failed to cross the danger zone, or it means the other general has confirmed and committed to the attack and has confidence I will too".

## History

The Two Generals' Problem and its impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Trade-offs in the Design of Network Communications",[3] where it is described starting on page 73 in the context of communication between two groups of gangsters.

This problem was given the name the Two Generals Paradox by Jim Gray[4] in 1978 in "Notes on Data Base Operating Systems"[5] starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as mentioned above.

References:
[1] Gmytrasiewicz, Piotr J.. (1992). Decision-theoretic recursive modeling and the coordinated attack problem. Proceedings of the First International Conference on Artificial Intelligence Planning Systems. doi:10.1016/B978-0-08-049944-4.50016-1
[2] The coordinated attack and the jealous amazons Alessandro Panconesi. Retrieved 2011-05-17.
[3] Akkoyunlu, E. A.. (1975). Some constraints and trade-offs in the design of network communications. Portal.acm.org. doi:10.1145/800213.806523
[4] (2004-05-03). Jim Gray Summary Home Page. Research.microsoft.com. http://research.microsoft.com/~Gray/JimGrayHomePageSummary.htm
[5] (January 1978). Notes on Data Base Operating Systems. Portal.acm.org. http://portal.acm.org/citation.cfm?coll=GUIDE&dl=GUIDE&id=723863
````

</details>

<details><summary><b>Step 8 — final</b> (1737 words)</summary>

````text
In computing, the Two Generals' Problem (or Chinese Generals Problem[1]) is a thought experiment meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. In the experiment, two generals are only able to communicate with one another by sending a messenger through enemy territory. The experiment asks how they might reach an agreement on the time to launch an attack, while knowing that any messenger they send could be captured.

The Two Generals' Problem appears often as an introduction to the more general Byzantine Generals problem in introductory classes about computer networking (particularly with regard to the Transmission Control Protocol, where it shows that TCP cannot guarantee state consistency between endpoints and why this is the case), though it applies to any type of two-party communication where failures of communication are possible. A key concept in epistemic logic, this problem highlights the importance of common knowledge. Some authors also refer to this as the Two Generals' Paradox, the Two Armies Problem, or the Coordinated Attack Problem.[2,3] The Two Generals' Problem was the first computer communication problem to be proven to be unsolvable.[4] An important consequence of this proof is that generalizations such as the Byzantine Generals problem are also unsolvable in the face of arbitrary communication failures, thus providing a base of realistic expectations for any distributed consistency protocols.

## Definition

Two armies, each led by a different general, are preparing to attack a fortified city. The armies are encamped near the city, each in its own valley. A third valley separates the two hills, and the only way for the two generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city's defenders and there is a chance that any given messenger sent through the valley will be captured.[5]

While the two generals have agreed that they will attack, they haven't agreed upon a time for an attack. It is required that the two generals have their armies attack the city simultaneously to succeed, lest the lone attacker army die trying. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time, and each general must know that the other general knows that they have agreed to the attack plan. Because acknowledgement of message receipt can be lost as easily as the original message, a potentially infinite series of messages is required to come to consensus.[6]

The thought experiment involves considering how they might go about coming to a consensus. In its simplest form, one general is known to be the leader, decides on the time of the attack, and must communicate this time to the other general. The problem is to come up with algorithms that the generals can use, including sending messages and processing received messages, that can allow them to correctly conclude:

Allowing that it is quite simple for the generals to come to an agreement on the time to attack (i.e. one successful message with a successful acknowledgement), the subtlety of the Two Generals' Problem is in the impossibility of designing algorithms for the generals to use to safely agree to the above statement.

## Illustrating the problem

The first general may start by sending a message: "Attack at 0900 on August 4." However, once dispatched, the first general has no idea whether or not the messenger got through. This uncertainty may lead the first general to hesitate to attack due to the risk of being the sole attacker.

To be sure, the second general may send a confirmation back to the first: "I received your message and will attack at 0900 on August 4." However, the messenger carrying the confirmation could face capture, and the second general may hesitate, knowing that the first might hold back without the confirmation.

Further confirmations may seem like a solution—let the first general send a second confirmation: "I received your confirmation of the planned attack at 0900 on August 4." However, this new messenger from the first general is liable to be captured, too. Thus, it quickly becomes evident that no matter how many rounds of confirmation are made, there is no way to guarantee the second requirement that each general is sure the other has agreed to the attack plan. Both generals will always be left wondering whether their last messenger got through.[7]

## Proof

Because this protocol is deterministic, suppose there is a sequence of a fixed number of messages, one or more successfully delivered and one or more not. The assumption is that there should be a shared certainty for both generals to attack. Consider the last such message that was successfully delivered. If that last message had not been successfully delivered, then one general at least (presumably the receiver) would decide not to attack. From the viewpoint of the sender of that last message, however, the sequence of messages sent and delivered is exactly the same as it would have been, had that message been delivered. Since the protocol is deterministic, the general sending that last message will still decide to attack. We've now created a situation where the suggested protocol leads one general to attack and the other not to attack—contradicting the assumption that the protocol was a solution to the problem.

A non-deterministic protocol with a potentially variable message count can be compared to an edge-labeled finite tree, where each node in the tree represents an explored example up to a specified point. A protocol that terminates before sending any messages is represented by a tree containing only a root node. The edges from a node to each child are labeled with the messages sent in order to reach the child state. Leaf nodes represent points at which the protocol terminates. Suppose there exists a non-deterministic protocol P which solves the Two Generals' Problem. Then, by a similar argument to the one used for fixed-length deterministic protocols above, P' must also solve the Two Generals' Problem, where the tree representing P' is obtained from that for P by removing all leaf nodes and the edges leading to them. Since P is finite, it then follows that the protocol that terminates before sending any messages would solve the problem. But clearly, it does not. Therefore, a non-deterministic protocol that solves the problem cannot exist.

## Engineering approaches

A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the uncertainty of the communications channel and not attempt to eliminate it, but rather mitigate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach, the first general will attack no matter what, and the second general will attack if any message is received. Alternatively, the first general could send a stream of messages and the second general could send acknowledgments to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There is no algorithm that they can use (e.g. attack if more than four messages are received) that will be certain to prevent one from attacking without the other. Also, the first general can send a marking on each message saying it is message 1, 2, 3 ... of n. This method will allow the second general to know how reliable the channel is and send an appropriate number of messages back to ensure a high probability of at least one message being received. If the channel can be made to be reliable, then one message will suffice and additional messages do not help. The last is as likely to get lost as the first.

Assuming that the generals must sacrifice lives every time a messenger is sent and intercepted, an algorithm can be designed to minimize the number of messengers required to achieve the maximum amount of confidence the attack is coordinated. To save them from sacrificing hundreds of lives to achieve very high confidence in coordination, the generals could agree to use the absence of messengers as an indication that the general who began the transaction has received at least one confirmation and has promised to attack. Suppose it takes a messenger 1 minute to cross the danger zone, allowing 200 minutes of silence to occur after confirmations have been received will allow us to achieve extremely high confidence while not sacrificing messenger lives. In this case, messengers are used only in the case where a party has not received the attack time. At the end of 200 minutes, each general can reason: "I have not received an additional message for 200 minutes; either 200 messengers failed to cross the danger zone, or it means the other general has confirmed and committed to the attack and has confidence I will too".

## History

The Two Generals' Problem and its impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Trade-offs in the Design of Network Communications",[8] where it is described starting on page 73 in the context of communication between two groups of gangsters.

This problem was given the name the Two Generals Paradox by Jim Gray[9] in 1978 in "Notes on Data Base Operating Systems"[10] starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as mentioned above.

References:
[1] Lamport, Leslie. (1982-07-05). The Byzantine Generals Problem. ACM Transactions on Programming Languages and Systems. https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/
[2] Gmytrasiewicz, Piotr J.. (1992). Artificial Intelligence Planning Systems. Proceedings of the First International Conference on Artificial Intelligence Planning Systems. doi:10.1016/B978-0-08-049944-4.50016-1
[3] The coordinated attack and the jealous amazons Alessandro Panconesi. Retrieved 2011-05-17.
[4] Leslie Lamport. "Solved Problems, Unsolved Problems and Non-Problems in Concurrency". 1983. p. 8.
[5] Ruby, Matt. How the Byzantine General's Problem Relates to You in 2024. Swan Bitcoin. https://www.swanbitcoin.com/byzantine-generals-problem/
[6] The Byzantine Generals Problem (Consensus in the presence of uncertainties). Imperial College London. https://www.doc.ic.ac.uk/~jnm/DistrAlg/Notes/Byzantine-4up-final.pdf
[7] Lamport, Leslie. The Byzantine Generals Problem. SRI International. https://lamport.azurewebsites.net/pubs/byz.pdf
[8] Akkoyunlu, E. A.. (1975). Some constraints and trade-offs in the design of network communications. Portal.acm.org. doi:10.1145/800213.806523
[9] (2004-05-03). Jim Gray Summary Home Page. Research.microsoft.com. http://research.microsoft.com/~Gray/JimGrayHomePageSummary.htm
[10] R. Bayer, R. M. Graham, and G. Seegmüller. (1978). Operating Systems. Springer-Verlag.
````

</details>
