# 10. Dining philosophers problem

`B-Dining_philosophers_problem` · [B_wiki_history_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Dining_philosophers_problem&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 953 revisions in history; 35 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 3 | 0 | 0.00 | source_title |
| 1 | earliest_version | 107 | 0 | 0.04 | enwiki rev 1649406 (2003-07-31) |
| 2 | early_revision | 1384 | 0 | 0.35 | enwiki rev 296767424 (2009-06-16) |
| 3 | late_revision | 1552 | 3 | 0.67 | enwiki rev 932405921 (2019-12-25) |
| 4 | final | 1667 | 6 | 1.00 | enwiki rev 1374736883 (2026-09-13) |

<details><summary><b>Step 0 — title</b> (3 words)</summary>

````text
Dining philosophers problem
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (107 words)</summary>

````text
Dining Philosphers Problem is an illustrative example of of a common computing problem.

Dijkstra used the example of a group of philosophers who are sharing a circular table with a single fork between each philosopher. Each philospher divides his time between eating and thinking, but in order to eat the philosopher must use two forks. The example is used to show how problems in resource sharing can be avoided.

The obvious conclusion in the example is that no adjacent pair of philosophers can eat at the same time. The problem is to avoid starvation (or deadlock) where each philosopher grabs 1 fork each.

See also: concurrency, deadlock.
````

</details>

<details><summary><b>Step 2 — early_revision</b> (1384 words)</summary>

````text
In computer science, the dining philosophers problem is an illustrative example of a common computing problem in concurrency. It is a classic multi-process synchronization problem.

In 1965, Edsger Dijkstra set an examination question on a synchronization problem where five computers competed for access to five shared tape drive peripherals. Soon afterwards the problem was retold by Tony Hoare as the dining philosophers problem.

This is a theoretical explanation of deadlock and resource starvation by assuming that each philosopher takes a different fork as a first priority and then looks for another.

## Problem

The dining philosophers problem is summarized as five philosophers sitting at a table doing one of two things: eating or thinking. While eating, they are not thinking, and while thinking, they are not eating. The five philosophers sit at a circular table with a large bowl of spaghetti in the center. A fork is placed in between each pair of adjacent philosophers, and as such, each philosopher has one fork to his left and one fork to his right. As spaghetti is difficult to serve and eat with a single fork, it is assumed that a philosopher must eat with two forks. Each philosopher can only use the forks on his immediate left and immediate right.

The dining philosophers problem is sometimes explained using rice and chopsticks rather than spaghetti and forks, as it is more intuitively obvious that two chopsticks are required to begin eating.

The philosophers never speak to each other, which creates a dangerous possibility of deadlock when every philosopher holds a left fork and waits perpetually for a right fork (or vice versa).

Originally used as a means of illustrating the problem of deadlock, this system reaches deadlock when there is a 'cycle of unwarranted requests'. In this case philosopher P1 waits for the fork grabbed by philosopher P2 who is waiting for the fork of philosopher P3 and so forth, making a circular chain.

Starvation (and the pun was intended in the original problem description) might also occur independently of deadlock if a philosopher is unable to acquire both forks because of a timing problem. For example there might be a rule that the philosophers put down a fork after waiting five minutes for the other fork to become available and wait a further five minutes before making their next attempt. This scheme eliminates the possibility of deadlock (the system can always advance to a different state) but still suffers from the problem of livelock. If all five philosophers appear in the dining room at exactly the same time and each picks up their left fork at the same time the philosophers will wait five minutes until they all put their forks down and then wait a further five minutes before they all pick them up again.

The lack of available forks is an analogy to the lacking of shared resources in real computer programming, a situation known as concurrency. Locking a resource is a common technique to ensure the resource is accessed by only one program or chunk of code at a time. When a program is interested in a resource which is already locked by another one, the program waits until it is unlocked. When several programs are involved in locking resources, deadlock might happen, depending on the circumstances. For example, one program needs two files to process. When two such programs lock one file each, both programs wait for the other one to unlock the other file, which will never happen.

In general the dining philosophers problem is a generic and abstract problem used for explaining various issues which arise in problems which hold mutual exclusion as a core idea. For example, as in the above case deadlock/livelock is well explained with the dining philosophers problem.

## Solutions

### Waiter solution

A relatively simple solution is achieved by introducing a waiter at the table. Philosophers must ask his permission before taking up any forks. Because the waiter is aware of which forks are in use, he is able to arbitrate and prevent deadlock. When four of the forks are in use, the next philosopher to request one has to wait for the waiter's permission, which is not given until a fork has been released. The logic is kept simple by specifying that philosophers always seek to pick up their left hand fork before their right hand fork (or vice versa).

To illustrate how this works, consider the philosophers are labelled clockwise from A to E. If A and C are eating, four forks are in use. B sits between A and C so has neither fork available, whereas D and E have one unused fork between them. Suppose D wants to eat. Were he to take up the fifth fork, deadlock becomes likely. If instead he asks the waiter and is told to wait, we can be sure that next time two forks are released there will certainly be at least one philosopher who could successfully request a pair of forks. Therefore deadlock cannot happen.

### Resource hierarchy solution

Another simple solution is achieved by assigning a partial order, or hierarchy, to the resources (the forks, in this case), and establishing the convention that all resources will be requested in order, and released in reverse order, and that no two resources unrelated by order will ever be used by a single unit of work at the same time. Here, the resources (forks) will be numbered 1 through 5, in some order, and each unit of work (philosopher) will always pick up the lower-numbered fork first, and then the higher-numbered fork, from among the two forks he plans to use. Then, he will always put down the higher numbered fork first, followed by the lower numbered fork. In this case, if four of the five philosophers simultaneously pick up their lower-numbered fork, only the highest numbered fork will remain on the table, so the fifth philosopher will not be able to pick up any fork. Moreover, only one philosopher will have access to that highest-numbered fork, so he will be able to eat using two forks. When he finishes using the forks, he will put down the highest-numbered fork first, followed by the lower-numbered fork, freeing another philosopher to grab the latter and begin eating.

While the resource hierarchy solution avoids deadlocks, it is not always practical, especially when the list of required resources is not completely known in advance. For example, if a unit of work holds resources 3 and 5 and then determines it needs resource 2, it must release 5, then 3 before acquiring 2, and then it must re-acquire 3 and 5 in that order. Computer programs that access large numbers of database records would not run efficiently if they were required to release all higher-numbered records before accessing a new record, making the method impractical for that purpose.

This is often the most practical solution for real world Computer Science problems; by assigning a constant hierarchy of locks, and by enforcing the ordering of obtaining the locks this problem can be avoided.

### Chandy / Misra solution

In 1984, K. Mani Chandy and J. Misra proposed a different solution to the dining philosophers problem to allow for arbitrary agents (numbered P1, ..., Pn) to contend for an arbitrary number of resources, unlike Dijkstra's solution. It is also completely distributed and requires no central authority after initialization.

For every pair of philosophers contending for a resource, create a fork and give it to the philosopher with the lower ID. Each fork can either be dirty or clean. Initially, all forks are dirty.

When a philosopher wants to use a set of resources (i.e. eat), he must obtain the forks from his contending neighbors. For all such forks he does not have, he sends a request message.

When a philosopher with a fork receives a request message, he keeps the fork if it is clean, but gives it up when it is dirty. If he sends the fork over, he cleans the fork before doing so.

After a philosopher is done eating, all his forks become dirty. If another philosopher had previously requested one of the forks, he cleans the fork and sends it.

This solution also allows for a large degree of concurrency, and will solve an arbitrarily large problem.
````

</details>

<details><summary><b>Step 3 — late_revision</b> (1552 words)</summary>

````text
In computer science, the dining philosophers problem is an example problem often used in concurrent algorithm design to illustrate synchronization issues and techniques for resolving them.

It was originally formulated in 1965 by Edsger Dijkstra as a student exam exercise, presented in terms of computers competing for access to tape drive peripherals.

Soon after, Tony Hoare gave the problem its present formulation.[1,2]

## Problem statement

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right forks. Each fork can be held by only one philosopher and so a philosopher can use the fork only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both forks so that the forks become available to others. A philosopher can take the fork on their right or the one on their left as they become available, but cannot start eating before getting both forks.

Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite supply and an infinite demand are assumed.

The problem is how to design a discipline of behavior (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.

### Problems

The problem was designed to illustrate the challenges of avoiding deadlock, a system state in which no progress is possible.

To see that a proper solution to this problem is not obvious, consider a proposal in which each philosopher is instructed to behave as follows:

think until the left fork is available; when it is, pick it up;

think until the right fork is available; when it is, pick it up;

when both forks are held, eat for a fixed amount of time;

then, put the right fork down;

then, put the left fork down;

repeat from the beginning.

This attempted solution fails because it allows the system to reach a deadlock state, in which no progress is possible. This is a state in which each philosopher has picked up the fork to the left, and is waiting for the fork to the right to become available. With the given instructions, this state can be reached, and when it is reached, each philosopher will eternally wait for another (the one to the right) to release a fork.

Resource starvation might also occur independently of deadlock if a particular philosopher is unable to acquire both forks because of a timing problem. For example, there might be a rule that the philosophers put down a fork after waiting ten minutes for the other fork to become available and wait a further ten minutes before making their next attempt. This scheme eliminates the possibility of deadlock (the system can always advance to a different state) but still suffers from the problem of livelock. If all five philosophers appear in the dining room at exactly the same time and each picks up the left fork at the same time the philosophers will wait ten minutes until they all put their forks down and then wait a further ten minutes before they all pick them up again.

Mutual exclusion is the basic idea of the problem; the dining philosophers create a generic and abstract scenario useful for explaining issues of this type. The failures these philosophers may experience are analogous to the difficulties that arise in real computer programming when multiple programs need exclusive access to shared resources. These issues are studied in concurrent programming. The original problems of Dijkstra were related to external devices like tape drives. However, the difficulties exemplified by the dining philosophers problem arise far more often when multiple processes access sets of data that are being updated. Complex systems such as operating system kernels use thousands of locks and synchronizations that require strict adherence to methods and protocols if such problems as deadlock, starvation, and data corruption are to be avoided.

## Solutions

### Resource hierarchy solution

This solution to the problem is the one originally proposed by Dijkstra. It assigns a partial order to the resources (the forks, in this case), and establishes the convention that all resources will be requested in order, and that no two resources unrelated by order will ever be used by a single unit of work at the same time. Here, the resources (forks) will be numbered 1 through 5 and each unit of work (philosopher) will always pick up the lower-numbered fork first, and then the higher-numbered fork, from among the two forks they plan to use. The order in which each philosopher puts down the forks does not matter. In this case, if four of the five philosophers simultaneously pick up their lower-numbered fork, only the highest-numbered fork will remain on the table, so the fifth philosopher will not be able to pick up any fork. Moreover, only one philosopher will have access to that highest-numbered fork, so they will be able to eat using two forks.

While the resource hierarchy solution avoids deadlocks, it is not always practical, especially when the list of required resources is not completely known in advance. For example, if a unit of work holds resources 3 and 5 and then determines it needs resource 2, it must release 5, then 3 before acquiring 2, and then it must re-acquire 3 and 5 in that order. Computer programs that access large numbers of database records would not run efficiently if they were required to release all higher-numbered records before accessing a new record, making the method impractical for that purpose.[1]

### Arbitrator solution

Another approach is to guarantee that a philosopher can only pick up both forks or none by introducing an arbitrator, e.g., a waiter. In order to pick up the forks, a philosopher must ask permission of the waiter. The waiter gives permission to only one philosopher at a time until the philosopher has picked up both of their forks. Putting down a fork is always allowed. The waiter can be implemented as a mutex.

In addition to introducing a new central entity (the waiter), this approach can result in reduced parallelism: if a philosopher is eating and one of their neighbors is requesting the forks, all other philosophers must wait until this request has been fulfilled even if forks for them are still available.

### Chandy/Misra solution

In 1984, K. Mani Chandy and J. Misra[3] proposed a different solution to the dining philosophers problem to allow for arbitrary agents (numbered P1, ..., Pn) to contend for an arbitrary number of resources, unlike Dijkstra's solution. It is also completely distributed and requires no central authority after initialization. However, it violates the requirement that "the philosophers do not speak to each other" (due to the request messages).

For every pair of philosophers contending for a resource, create a fork and give it to the philosopher with the lower ID (n for agent Pn). Each fork can either be dirty or clean. Initially, all forks are dirty.

When a philosopher wants to use a set of resources (i.e. eat), said philosopher must obtain the forks from their contending neighbors. For all such forks the philosopher does not have, they send a request message.

When a philosopher with a fork receives a request message, they keep the fork if it is clean, but give it up when it is dirty. If the philosopher sends the fork over, they clean the fork before doing so.

After a philosopher is done eating, all their forks become dirty. If another philosopher had previously requested one of the forks, the philosopher that has just finished eating cleans the fork and sends it.

This solution also allows for a large degree of concurrency, and will solve an arbitrarily large problem.

It also solves the starvation problem. The clean / dirty labels act as a way of giving preference to the most "starved" processes, and a disadvantage to processes that have just "eaten". One could compare their solution to one where philosophers are not allowed to eat twice in a row without letting others use the forks in between. Chandy and Misra's solution is more flexible than that, but has an element tending in that direction.

In their analysis they derive a system of preference levels from the distribution of the forks and their clean/dirty states. They show that this system may describe an acyclic graph, and if so, the operations in their protocol cannot turn that graph into a cyclic one. This guarantees that deadlock cannot occur. However, if the system is initialized to a perfectly symmetric state, like all philosophers holding their left side forks, then the graph is cyclic at the outset, and their solution cannot prevent a deadlock. Initializing the system so that philosophers with lower IDs have dirty forks ensures the graph is initially acyclic.

References:
[1] (1981). Formalization of Programming Concepts: International Colloquium, Peniscola, Spain, April 19–25, 1981. Proceedings. Birkhäuser. https://books.google.com/books?id=pl4VJKQlcG4C
[2] Hoare, C. A. R.. (2004). Communicating Sequential Processes. usingcsp.com. http://www.usingcsp.com/cspbook.pdf
[3] Chandy, K.M.; Misra, J. (1984). The Drinking Philosophers Problem. ACM Transactions on Programming Languages and Systems.
````

</details>

<details><summary><b>Step 4 — final</b> (1667 words)</summary>

````text
In computer science, the dining philosophers problem is an example problem often used in concurrent algorithm design to illustrate synchronization issues and techniques for resolving them.

It was originally formulated in 1965 by Edsger Dijkstra as a student exam exercise, presented in terms of computers competing for access to tape drive peripherals and then formulated in terms of diners, dubbed the "dining quintet".

Soon after, Tony Hoare gave the problem its present name.[1,2,3]

## Problem statement

Five philosophers dine together at the same table. Each philosopher has their own plate at the table. There is a fork between each pair of adjacent plates. The dish served is a kind of spaghetti that must be eaten with two forks. Each philosopher can only alternately think and eat. Moreover, a philosopher can only eat their spaghetti when they have both a left and a right fork. Thus, two forks will only be available when their two nearest neighbors are thinking, not eating. After an individual philosopher finishes eating, they will put down both forks.

The problem is how to design a regimen (a concurrent algorithm) such that any philosopher will not starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think (an issue of incomplete information).

### Problems

The problem was designed to illustrate the challenges of avoiding deadlock, a system state in which no progress is possible. To see that a proper solution to this problem is not obvious, consider a proposal in which each philosopher is instructed to behave as follows:

think unless the left fork is available; when it is, pick it up;

think unless the right fork is available; when it is, pick it up;

when both forks are held, eat for a fixed amount of time;

put the left fork down;

put the right fork down;

repeat from the beginning.

With these instructions, the situation may arise where each philosopher holds the fork to their left; in that situation, they will all be stuck forever, waiting for the other fork to be available: it is a deadlock.

Resource starvation, mutual exclusion, and livelock are other types of sequence and access problems.

## Solutions

These four conditions are necessary for a deadlock to occur:

mutual exclusion (no fork can be simultaneously used by multiple philosophers)

resource holding (the philosophers hold a fork while waiting for the second)

non-preemption (no philosopher can take a fork from another), and

circular wait (each philosopher may be waiting on the philosopher to their left)

A solution must negate at least one of those four conditions. In practice, negating mutual exclusion or non-preemption somehow can give a valid solution, but most theoretical treatments assume that those assumptions are non-negotiable, instead attacking resource holding or circular waiting (often both).

### Dijkstra's solution

Dijkstra's solution negates resource holding; the philosophers atomically pick up both forks or wait, never holding exactly one fork outside of a critical section. To accomplish this, Dijkstra's solution uses one mutex, one semaphore per philosopher, and one state variable per philosopher. This solution is more complex than the resource hierarchy solution.[3] This is a C++20 version of Dijkstra's solution with changes by Andrew S. Tanenbaum:

The function test() and its use in take_forks() and put_forks() make the Dijkstra solution deadlock-free.

### Resource hierarchy solution

This solution negates circular waiting by assigning a partial order to the resources (the forks, in this case), and establishes the convention that all resources will be requested in order, and that no two resources unrelated by order will ever be used by a single unit of work at the same time. Here, the resources (forks) will be numbered 1 through 5, and each unit of work (philosopher) will always pick up the lower-numbered fork first, and then the higher-numbered fork, from among the two forks he plans to use. The order in which each philosopher puts down the forks does not matter. In this case, if four of the five philosophers simultaneously pick up their lower-numbered forks, only the highest-numbered fork will remain on the table, so the fifth philosopher will not be able to pick up any fork. Moreover, only one philosopher will have access to that highest-numbered fork, so he will be able to eat using two forks. This can intuitively be thought of as having one "left-handed" philosopher at the table, who – unlike all the other philosophers – takes his fork from the left first.

While the resource hierarchy solution avoids deadlocks, it is not always practical, especially when the list of required resources is not completely known in advance. For example, if a unit of work holds resources 3 and 5 and then determines it needs resource 2, it must release 5, then 3, before acquiring 2, and then it must re-acquire 3 and 5 in that order. Computer programs that access large numbers of database records would not run efficiently if they were required to release all higher-numbered records before accessing a new record, making the method impractical for that purpose.[1]

The resource hierarchy solution is not fair. If philosopher 1 is slow to take a fork, and if philosopher 2 is quick to think and pick their forks back up, then philosopher 1 will never get to pick up both forks. A fair solution must guarantee that each philosopher will eventually eat, no matter how slowly that philosopher moves relative to the others.

The following source code is a C++11 implementation of the resource hierarchy solution for five philosophers. The sleep_for() function simulates the time normally spent with business logic.[4]

For GCC: compile with

### Arbitrator solution

Another approach is to guarantee that a philosopher can only pick up both forks or none by introducing an arbitrator to replace circular waiting, e.g., a waiter. To pick up the forks, a philosopher must ask permission of the waiter. The waiter gives permission to only one philosopher at a time until the philosopher has picked up both of his forks. Putting down a fork is always allowed. The waiter can be implemented as a mutex.

In addition to introducing a new central entity (the waiter), this approach can result in reduced parallelism: if a philosopher is eating and one of his neighbors is requesting the forks, all other philosophers must wait until this request has been fulfilled, even if forks for them are still available.

### Limiting the number of diners in the table

A solution presented by William Stallings[5] is to allow a maximum of n-1 philosophers to sit down at any time. The last philosopher would have to wait (for example, using a semaphore) for someone to finish dining before he "sits down" and requests access to any fork. This negates circular wait, guaranteeing that at least one philosopher may always acquire both forks, allowing the system to make progress.

### Chandy/Misra solution

In 1984, K. Mani Chandy and J. Misra[6] proposed a different solution to the dining philosophers problem to allow for arbitrary agents (numbered P1, ..., Pn) to contend for an arbitrary number of resources, unlike Dijkstra's solution. It is also completely distributed and requires no central authority after initialization. However, it violates the requirement that "the philosophers do not speak to each other" (due to the request messages).

For every pair of philosophers contending for a resource, create a fork and give it to the philosopher with the lower ID (n for agent Pn). Each fork can either be dirty or clean. Initially, all forks are dirty.

When a philosopher wants to use a set of resources (i.e., eat), the said philosopher must obtain the forks from his contending neighbors. For all such forks that the philosopher does not have, he sends a request message.

When a philosopher with a fork receives a request message, he keeps the fork if it is clean, but gives it up when it is dirty. If the philosopher sends the fork over, he cleans the fork before doing so.

After a philosopher is done eating, all his forks become dirty. If another philosopher had previously requested one of the forks, the philosopher who has just finished eating cleans the fork and sends it.

This solution also allows for a large degree of concurrency and will solve an arbitrarily large problem.

It also solves the starvation problem. The clean/dirty labels act as a way of giving preference to the most "starved" processes, and a disadvantage to processes that have just "eaten". One could compare their solution to one where philosophers are not allowed to eat twice in a row without letting others use the forks in between. Chandy and Misra's solution is more flexible than that, but has an element tending in that direction.

In their analysis, they derive a system of preference levels from the distribution of the forks and their clean/dirty states. They show that this system may describe a directed acyclic graph, and if so, the operations in their protocol cannot turn that graph into a cyclic one. This guarantees that deadlock cannot occur by negating circular waiting. However, if the system is initialized to a perfectly symmetric state, like all philosophers holding their left side forks, then the graph is cyclic at the outset, and their solution cannot prevent a deadlock. Initializing the system so that philosophers with lower IDs have dirty forks ensures the graph is initially acyclic.

References:
[1] (1981). Formalization of Programming Concepts: International Colloquium, Peniscola, Spain, April 19–25, 1981. Proceedings. Birkhäuser. https://books.google.com/books?id=pl4VJKQlcG4C
[2] Hoare, C. A. R.. (2004). Communicating Sequential Processes. usingcsp.com. http://www.usingcsp.com/cspbook.pdf
[3] Tanenbaum, Andrew S.. (2006). Operating Systems - Design and Implementation, 3rd edition [Chapter: 2.3.1 The Dining Philosophers Problem]. Pearson Education, Inc..
[4] Tanenbaum, Andrew S.. (2006). Operating Systems - Design and Implementation, 3rd edition [Chapter: 3.3.5 Deadlock Prevention]. Pearson Education, Inc..
[5] Stallings, William. (2018). Operating systems : internals and design principles. Pearson.
[6] Chandy, K.M.; Misra, J. (1984). The Drinking Philosophers Problem. ACM Transactions on Programming Languages and Systems.
````

</details>
