# 2. Skip list

`B-Skip_list` · [B_wiki_history_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Skip_list&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 503 revisions in history; 37 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | revision_1 | 40 | 0 | 0.01 | enwiki rev 1779834 (2003-10-08) |
| 2 | revision_2 | 417 | 0 | 0.25 | enwiki rev 1851676 (2003-12-01) |
| 3 | revision_3 | 1403 | 0 | 0.37 | enwiki rev 72756785 (2006-08-30) |
| 4 | revision_4 | 2038 | 3 | 0.52 | enwiki rev 338154094 (2010-01-16) |
| 5 | revision_5 | 2269 | 5 | 0.64 | enwiki rev 524964031 (2012-11-26) |
| 6 | revision_6 | 1715 | 6 | 0.81 | enwiki rev 593057848 (2014-01-30) |
| 7 | revision_7 | 2041 | 22 | 0.90 | enwiki rev 1107702329 (2022-08-31) |
| 8 | final | 1972 | 17 | 1.00 | enwiki rev 1373738569 (2026-09-07) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Skip list
````

</details>

<details><summary><b>Step 1 — revision_1</b> (40 words)</summary>

````text
A skip list is a probabalistic data structure, with efficiency greater than a binary tree (order O(log n)). It uses the idea of "heights" and parallel linked lists.

This article is a stub. You can help Wikipedia by fixing it.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (417 words)</summary>

````text
A skip list is a probabilistic data structure, based on parallel linked lists, with efficiency comparable to a binary tree (order O(log n) time for most operations).

A skip list is built in layers. The bottom layer is an ordinary sorted linked list. Each higher layer acts as an "express lane" for the lists below, where an element in layer i appears in layer i+1 with some fixed probability p. On average, each element appears in 1/(1-p) lists, and the tallest element (usually a special head element at the front of the skip list) appears in O(log1/p n) lists.

To search for a target element, start with the head element and the top list and scan along each linked list until you reach the last element in it that is less than or equal to the target. The expected number of steps in each linked list is easily seen to be 1/p, by tracing the search path backwards from the target until reaching an element that appears in the next higher list. So the total cost of a search is O(log1/p n / p), which is O(log n) when p is a constant. By choosing different values of p, it is possible to trade search costs against storage costs.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

Skip lists do not provide the same absolute worst-case performance guarantees of more traditional balanced-tree data structures, because it is always possible (though with very low probability) that the coin-flips used to build the skip list will produce a badly unbalanced structure. However, they work well in practice, and the randomized balancing scheme is easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in parallel computing, where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure.

## History

Skip lists were invented by William Pugh. He details how

they work in Skip lists: a probabilistic alternative to balanced trees

in Communications of the ACM, June 1990, 33(6) 668-676.

See also .

To quote the inventor:

Skip lists are a probabilistic data structure that seem likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (1403 words)</summary>

````text
A skip list is a probabilistic data structure, based on parallel linked lists, with efficiency comparable to a binary search tree (order O(log n) average time for most operations).

Basically, a skip list is an augmentation of an ordered linked list with additional forward links, added in a randomized way with a Geometric/Negative Binomial distribution (See William Pugh's original paper), so that a search in the list may quickly skip parts of the list (hence the name). Insert, search and delete operations are performed in logarithmic randomized time.

Invented in 1990 by William Pugh, the skip list is among the youngest of the important algorithms used in computer science (Pugh 1990).

## Description

A skip list is built in layers. The bottom layer is an ordinary sorted linked list. Each higher layer acts as an "express lane" for the lists below, where an element in layer i appears in layer i+1 with some fixed probability p. On average, each element appears in 1/(1-p) lists, and the tallest element (usually a special head element at the front of the skip list) appears in O(log1/p n) lists.

To search for a target element, start with the head element and the top list and scan along each linked list until you reach the last element in it that is less than or equal to the target. The expected number of steps in each linked list is easily seen to be 1/p, by tracing the search path backwards from the target until reaching an element that appears in the next higher list. So the total cost of a search is O(log1/p n / p), which is O(log n) when p is a constant. By choosing different values of p, it is possible to trade search costs against storage costs.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

Also, Θ(n) operations, which force us to visit every node in ascending order (PrintEntireListToScreen(), etc.) provide us with the opportunity to perform a behind-the-scenes derandomization of the level structure of the skip-list in an optimal way (Choose the level of the i'th finite node to be 1 plus the number of times we can repeatedly divide i by 2 before it becomes odd. Also, i=0 for the negative infinity header as we have the usual special case of choosing the highest possible level for negative and/or positive infinite nodes.). However this also allows someone to know where all of the higher-than-level 1 nodes are and delete them.

Alternatively, we could make the level structure quasi-random in the following way: First, make all of the nodes level 1. Next, for each i'th node at level 1 or higher, if i is odd, randomly choose whether or not to promote it to level 2, otherwise, if i is even, promote it to level 2 if and only if the previous node i-1 was not promoted to level 2. Is the number of nodes promoted greater than 1? If so, then repeat the "Next, for each i'th..." above only substituting "level 2" and "level 3" for "level 1" and "level 2". How about now, is the number of nodes promoted greater than 1? If so, then repeat the "Next, for each i'th..." above only now for levels 3 and 4. Keep going like this until the number of nodes promoted is less than or equal to 1. Like the derandomized version, we only want to quasi-randomize when we have some other reason to be running a Θ(n) operation (which visits every node?) anyway. The advantage of this quasi-randomness, over the totally derandomized version in the paragraph above, is that it doesn't give away nearly as much level-structure related information, to an adversarial user, as the de-randomized one. Yet, just like the totally derandomized one above, the search performance is now guaranteed to be logarithmic.

One may be tempted to make the following "optimization": In the part which says "Next, for each i'th...", forget about doing a coin-flip for each even-odd pair. Just flip a coin once to decide whether or not to promote only the even ones or only the odd ones. Instead of Θ(n lg n) coin flips, we would only have Θ(lg n) of them. Unfortunately, this gives the adversarial user a 50/50 chance of being correct upon guessing that all of the even numbered nodes (among the ones at level 1 or higher) are higher than level one. This is despite the property that he/she has a very low probability of guessing that a particular node is at level N for some integer N.

Let us prove these two claims concerning the advantages of quasi-randomness over the totally derandomized version. First, to prove that the search time is guaranteed to be logarithmic. Suppose we search for and find node n where n is the position of the found node among the nodes of level 1 or higher. If n is even, then there is a 50/50 chance that it is higher than level 1. This time, though, if it is not higher than level 1 then node n-1 is guaranteed to be higher than level 1. If n is odd, then there is a 50/50 chance that it is higher than level 1. Given that it is not, there is a 50/50 chance that node n-1 is higher than level 1. Given that this is not either, we are guaranteed that node n-2 is higher than level 1. We repeat the analysis for nodes of level 2 or higher, level 3 or higher, etc. always keeping in mind that n is the position of the node among the ones of level k or higher for integer k. So the search time is constant in the best case (if the found node is the highest possible level) and 2 times the worst case for the search time for the totally derandomized skip-list (because we have to keep moving left twice rather than keep moving left once).

Next, let's prove something about the probability of an adversarial user's guess of a node being level k or higher being correct. First, the adversarial user has a 50/50 chance of correctly guessing that a particular node is level 2 or higher. This event is independent of whether or not he/she correctly guesses at some other node being level 2 or higher. If he/she knows the positions of two consecutive nodes of level 2 or higher, and knows that the one on the left is in an odd numbered position among the nodes of level 2 or higher, he/she has a 50/50 chance of correctly guessing which one is of level 3 or higher. So, his/her probibility of being correct, when guessing that a node is level 3 or higher, is 1/4. Inductively continuing this analysis, we see that his/her probability of guessing that a particular node is level k or higher is 1/(2^(k-1)).

A skip list, upon which we have not recently performed either of the above mentioned Θ(n) operations, does not provide the same absolute worst-case performance guarantees as more traditional balanced tree data structures, because it is always possible (though with very low probability) that the coin-flips used to build the skip list will produce a badly balanced structure. However, they work well in practice, and the randomized balancing scheme has been argued to be easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in parallel computing, where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure.

There has been some evidence that skip lists have worse real-world performance and space requirements than B trees due to memory locality and other issues .

## History

Skip lists were invented by William Pugh. He details how they work in Skip lists: a probabilistic alternative to balanced trees in Communications of the ACM, June 1990, 33(6) 668-676.

See also citations and downloadable documents.

To quote the inventor:

Skip lists are a probabilistic data structure that seem likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space.

These claims of space and speed advantages were subsequently disputed, however .
````

</details>

<details><summary><b>Step 4 — revision_4</b> (2038 words)</summary>

````text
A skip list is a data structure for storing a sorted list of items, using a hierarchy of linked lists that connect increasingly sparse subsequences of the items. These auxiliary lists allow item lookup with efficiency comparable to balanced binary search trees (that is, with number of probes proportional to log n instead of n).

Each link of the sparser lists skips over many items of the full list in one step, hence the structure's name. These forward links may be added in a randomized way with a geometric / negative binomial distribution [1]. Insert, search and delete operations are performed in logarithmic expected time. The links may also be added in a non-probabilistic way so as to guarantee amortized (rather than merely expected) logarithmic cost.

## Description

A skip list is built in layers. The bottom layer is an ordinary ordered linked list. Each higher layer acts as an "express lane" for the lists below, where an element in layer i appears in layer i+1 with some fixed probability p (two commonly-used values for p are 1/2 or 1/4). On average, each element appears in 1/(1-p) lists, and the tallest element (usually a special head element at the front of the skip list) in \log_{1/p} n\, lists.

A search for a target element begins at the head element in the top list, and proceeds horizontally until the current element is greater than or equal to the target. If the current element is equal to the target, it has been found. If the current element is greater than the target, the procedure is repeated after returning to the previous element and dropping down vertically to the next lower list. The expected number of steps in each linked list is at most 1/p, which can be seen by tracing the search path backwards from the target until reaching an element that appears in the next higher list or reaching the beginning of the current list. Therefore, the total expected cost of a search is (\log_{1/p} n)/p,\, which is \mathcal{O}(\log n)\, when p is a constant. By choosing different values of p, it is possible to trade search costs against storage costs.

### Implementation details

The elements used for a skip list can contain more than one pointer since they can participate in more than one list.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

Θ(n) operations, which force us to visit every node in ascending order (such as printing the entire list), provide the opportunity to perform a behind-the-scenes derandomization of the level structure of the skip-list in an optimal way, bringing the skip list to \mathcal{O}(\log n) search time. (Choose the level of the i'th finite node to be 1 plus the number of times we can repeatedly divide i by 2 before it becomes odd. Also, i=0 for the negative infinity header as we have the usual special case of choosing the highest possible level for negative and/or positive infinite nodes.) However this also allows someone to know where all of the higher-than-level 1 nodes are and delete them.

Alternatively, we could make the level structure quasi-random in the following way:

make all nodes level 1

j = 1

while the number of nodes at level j > 1

for each i'th node at level j

if i is odd

if i is not the last node at level j

randomly choose whether to promote it to level j+1

else

do not promote

end if

else if i is even and node i-1 was not promoted

promote it to level j+1

end if

end for

j = j + 1

end while

Like the derandomized version, quasi-randomization is only done when there is some other reason to be running a Θ(n) operation (which visits every node).

The advantage of this quasi-randomness is that it doesn't give away nearly as much level-structure related information to an adversarial user as the de-randomized one. This is desirable because an adversarial user who is able to tell which nodes are not at the lowest level can pessimize performance by simply deleting higher-level nodes. The search performance is still guaranteed to be logarithmic.

It would be tempting to make the following "optimization": In the part which says "Next, for each i'th...", forget about doing a coin-flip for each even-odd pair. Just flip a coin once to decide whether to promote only the even ones or only the odd ones. Instead of Θ(n lg n) coin flips, there would only be Θ(lg n) of them. Unfortunately, this gives the adversarial user a 50/50 chance of being correct upon guessing that all of the even numbered nodes (among the ones at level 1 or higher) are higher than level one. This is despite the property that he has a very low probability of guessing that a particular node is at level N for some integer N.

The following proves these two claims concerning the advantages of quasi-randomness over the totally derandomized version. First, to prove that the search time is guaranteed to be logarithmic. Suppose a node n is searched for, where n is the position of the found node among the nodes of level 1 or higher. If n is even, then there is a 50/50 chance that it is higher than level 1. However, if it is not higher than level 1 then node n-1 is guaranteed to be higher than level 1. If n is odd, then there is a 50/50 chance that it is higher than level 1. Suppose that it is not; there is a 50/50 chance that node n-1 is higher than level 1. Suppose that this is not either; we are guaranteed that node n-2 is higher than level 1. The analysis can then be repeated for nodes of level 2 or higher, level 3 or higher, etc. always keeping in mind that n is the position of the node among the ones of level k or higher for integer k. So the search time is constant in the best case (if the found node is the highest possible level) and 2 times the worst case for the search time for the totally derandomized skip-list (because we have to keep moving left twice rather than keep moving left once).

Next, an examination of the probability of an adversarial user's guess of a node being level k or higher being correct. First, the adversarial user has a 50/50 chance of correctly guessing that a particular node is level 2 or higher. This event is independent of whether or not the user correctly guesses at some other node being level 2 or higher. If the user knows the positions of two consecutive nodes of level 2 or higher, and knows that the one on the left is in an odd numbered position among the nodes of level 2 or higher, the user has a 50/50 chance of correctly guessing which one is of level 3 or higher. So, the user's probability of being correct, when guessing that a node is level 3 or higher, is 1/4. Inductively continuing this analysis, we see that the user's probability of guessing that a particular node is level k or higher is 1/(2^(k-1)).

The above analyses only work when the number of nodes is a power of two. However, because of the third rule which says, "Finally, if i is odd and also the last node at level 1 then do not promote." (where we substitute the appropriate level number for 1) it becomes a sequence of exact-power-of-two-sized skiplists, concatenated onto each other, for which the analysis does work. In fact, the exact powers of two correspond to the binary representation for the number of nodes in the whole list.

A skip list, upon which we have not recently performed either of the above mentioned Θ(n) operations, does not provide the same absolute worst-case performance guarantees as more traditional balanced tree data structures, because it is always possible (though with very low probability) that the coin-flips used to build the skip list will produce a badly balanced structure. However, they work well in practice, and the randomized balancing scheme has been argued to be easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in parallel computing, where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure. Such parallelism can be especially advantageous for resource discovery in an ad-hoc Wireless network because a randomized skip list can be made robust to the loss of any single node[2].

There has been some evidence that skip lists have worse real-world performance and space requirements than B trees due to memory locality and other issues.[3]

### Indexable Skiplist

As described above, a skiplist is capable of fast Θ(log n) insertion and removal of values from a sorted sequence, but it has only slow Θ(n) lookups of values at a given position in the sequence (i.e. return the 500th value); however, with a minor modification the speed of random access indexed lookups can be improved to Θ(log n).

For every link, also store the width of the link (the number of bottom layer links being traversed by higher layer "express lane" links. In the example at the top of the page, the highest level has a link of width 1 (between the head and node 1) and

another of width 10 (between node 1 and NIL). The next highest level has link of width 1 (between the head and node 1), a link of width 3 (between node 1 and node 4), a link of width 2 (between node 4 and node 6), and a link of width 5 (between node 6 and NIL). Notice that the sum of the widths on any level is number of skip list entries plus one (10 entries + 1 is eleven).

When inserting new values or removing old values, a pair of width entries on each level needs to be updated to reflect the insertion or removal.

To index the skiplist (i.e. find the ith value), traverse the skiplist while counting down the widths of each traversed link:

Function LookupByPostionIndex(i)

node = head

level = top

i = i + 1 # don't count the head as a step

while True

if i >= node.width[level] # if next step is not too far

i = i - node.width[level] # subtract the current width

node = node.next[level] # traverse forward at the current level

else if level is bottom # if we are at the bottom level

return node.value # we've found the i-th value

level = level - 1 # otherwise, go down one level

See Running Median using an Indexable Skiplist for a complete implementation written in Python and an example of it being used to solve a computationally intensive statistics problem.

## History

Skip lists were invented in 1990 by William Pugh. He details how they work in Skip lists: a probabilistic alternative to balanced trees in Communications of the ACM, June 1990, 33(6) 668-676.

See also citations and downloadable documents.

To quote the inventor:

Skip lists are a probabilistic data structure that seem likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space.

## Usages

List of applications and frameworks that use skip lists:

QMap template class of Qt that provides a dictionary.

skipdb is an open-source database format using ordered key/value pairs.

Running Median using an Indexable Skiplist is a Python implementation of a skiplist augmented by link widths to make the structure indexable (giving fast access to the nth item). The indexable skiplist is used to efficiently solve the running median problem (recomputing medians and quartiles as values are added and removed from a large sliding window).

References:
[1] Pugh, William. (1990). Skip lists: a probabilistic alternative to balanced trees. Communications of the ACM. doi:10.1145/78973.78977
[2] Shah, Gauri Ph.D.. (December 2003). Distributed Data Structures for Peer-to-Peer Systems. http://www.cs.yale.edu/homes/shah/pubs/thesis.pdf
[3] http://resnet.uoregon.edu/~gurney_j/jmpc/skiplist.html
````

</details>

<details><summary><b>Step 5 — revision_5</b> (2269 words)</summary>

````text
A skip list is a data structure for storing a sorted list of items using a hierarchy of linked lists that connect increasingly sparse subsequences of the items. These auxiliary lists allow item lookup with efficiency comparable to balanced binary search trees (that is, with number of probes proportional to log n instead of n).

Each link of the sparser lists skips over many items of the full list in one step, hence the structure's name. These forward links may be added in a randomized way with a geometric / negative binomial distribution.[1] Insert, search and delete operations are performed in logarithmic expected time. The links may also be added in a non-probabilistic way so as to guarantee amortized (rather than merely expected) logarithmic cost.[2]

## Description

A skip list is built in layers. The bottom layer is an ordinary ordered linked list. Each higher layer acts as an "express lane" for the lists below, where an element in layer i appears in layer i+1 with some fixed probability p (two commonly used values for p are 1/2 or 1/4). On average, each element appears in 1/(1-p) lists, and the tallest element (usually a special head element at the front of the skip list) in \log_{1/p} n\, lists.

A search for a target element begins at the head element in the top list, and proceeds horizontally until the current element is greater than or equal to the target. If the current element is equal to the target, it has been found. If the current element is greater than the target, or the search reaches the end of the linked list, the procedure is repeated after returning to the previous element and dropping down vertically to the next lower list. The expected number of steps in each linked list is at most 1/p, which can be seen by tracing the search path backwards from the target until reaching an element that appears in the next higher list or reaching the beginning of the current list. Therefore, the total expected cost of a search is (\log_{1/p} n)/p,\, which is \mathcal{O}(\log n)\, when p is a constant. By choosing different values of p, it is possible to trade search costs against storage costs.

### Implementation details

The elements used for a skip list can contain more than one pointer since they can participate in more than one list.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

\mathcal{O}(n) operations, which force us to visit every node in ascending order (such as printing the entire list), provide the opportunity to perform a behind-the-scenes derandomization of the level structure of the skip-list in an optimal way, bringing the skip list to \mathcal{O}(\log n) search time. (Choose the level of the i'th finite node to be 1 plus the number of times we can repeatedly divide i by 2 before it becomes odd. Also, i=0 for the negative infinity header as we have the usual special case of choosing the highest possible level for negative and/or positive infinite nodes.) However this also allows someone to know where all of the higher-than-level 1 nodes are and delete them.

Alternatively, we could make the level structure quasi-random in the following way:

make all nodes level 1

j ← 1

while the number of nodes at level j > 1 do

for each i'th node at level j do

if i is odd

if i is not the last node at level j

randomly choose whether to promote it to level j+1

else

do not promote

end if

else if i is even and node i-1 was not promoted

promote it to level j+1

end if

repeat

j ← j + 1

repeat

Like the derandomized version, quasi-randomization is only done when there is some other reason to be running a \mathcal{O}(n) operation (which visits every node).

The advantage of this quasi-randomness is that it doesn't give away nearly as much level-structure related information to an adversarial user as the de-randomized one. This is desirable because an adversarial user who is able to tell which nodes are not at the lowest level can pessimize performance by simply deleting higher-level nodes. The search performance is still guaranteed to be logarithmic.

It would be tempting to make the following "optimization": In the part which says "Next, for each i'th...", forget about doing a coin-flip for each even-odd pair. Just flip a coin once to decide whether to promote only the even ones or only the odd ones. Instead of \mathcal{O}(n \log n) coin flips, there would only be \mathcal{O}(\log n) of them. Unfortunately, this gives the adversarial user a 50/50 chance of being correct upon guessing that all of the even numbered nodes (among the ones at level 1 or higher) are higher than level one. This is despite the property that he has a very low probability of guessing that a particular node is at level N for some integer N.

The following proves these two claims concerning the advantages of quasi-randomness over the totally derandomized version. First, to prove that the search time is guaranteed to be logarithmic. Suppose a node n is searched for, where n is the position of the found node among the nodes of level 1 or higher. If n is even, then there is a 50/50 chance that it is higher than level 1. However, if it is not higher than level 1 then node n-1 is guaranteed to be higher than level 1. If n is odd, then there is a 50/50 chance that it is higher than level 1. Suppose that it is not; there is a 50/50 chance that node n-1 is higher than level 1. Suppose that this is not either; we are guaranteed that node n-2 is higher than level 1. The analysis can then be repeated for nodes of level 2 or higher, level 3 or higher, etc. always keeping in mind that n is the position of the node among the ones of level k or higher for integer k. So the search time is constant in the best case (if the found node is the highest possible level) and 2 times the worst case for the search time for the totally derandomized skip-list (because we have to keep moving left twice rather than keep moving left once).

Next, an examination of the probability of an adversarial user's guess of a node being level k or higher being correct. First, the adversarial user has a 50/50 chance of correctly guessing that a particular node is level 2 or higher. This event is independent of whether or not the user correctly guesses at some other node being level 2 or higher. If the user knows the positions of two consecutive nodes of level 2 or higher, and knows that the one on the left is in an odd numbered position among the nodes of level 2 or higher, the user has a 50/50 chance of correctly guessing which one is of level 3 or higher. So, the user's probability of being correct, when guessing that a node is level 3 or higher, is 1/4. Inductively continuing this analysis, we see that the user's probability of guessing that a particular node is level k or higher is 1/2^{k-1} .

The above analyses only work when the number of nodes is a power of two. However, because of the third rule which says, "Finally, if i is odd and also the last node at level 1 then do not promote." (where we substitute the appropriate level number for 1) it becomes a sequence of exact-power-of-two-sized skiplists, concatenated onto each other, for which the analysis does work. In fact, the exact powers of two correspond to the binary representation for the number of nodes in the whole list.

A skip list, upon which we have not recently performed either of the above mentioned \mathcal{O}(n) operations, does not provide the same absolute worst-case performance guarantees as more traditional balanced tree data structures, because it is always possible (though with very low probability) that the coin-flips used to build the skip list will produce a badly balanced structure. However, they work well in practice, and the randomized balancing scheme has been argued to be easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in parallel computing, where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure. Such parallelism can be especially advantageous for resource discovery in an ad-hoc Wireless network because a randomized skip list can be made robust to the loss of any single node.[3]

There has been some evidence that skip lists have worse real-world performance and space requirements than B trees due to memory locality and other issues.[4]

### Indexable skiplist

As described above, a skiplist is capable of fast Θ(log n) insertion and removal of values from a sorted sequence, but it has only slow Θ(n) lookups of values at a given position in the sequence (i.e. return the 500th value); however, with a minor modification the speed of random access indexed lookups can be improved to Θ(log n).

For every link, also store the width of the link. The width is defined as the number of bottom layer links being traversed by each of the higher layer "express lane" links.

For example, here are the widths of the links in the example at the top of the page:

o-----> o-----------------------------------------------------------------------------> o Top level

o-----> o---------------------> o-------------> o-------------------------------------> o Level 3

o-----> o-------------> o-----> o-------------> o-------------------------------------> o Level 2

o-----> o-----> o-----> o-----> o-----> o-----> o-----> o-----> o-----> o-----> o-----> o Bottom level

Head Node1 Node2 Node3 Node4 Node5 Node6 Node7 Node8 Node9 Node10 NIL

Notice that the width of a higher level link is the sum of the component links below it (i.e. the width 10 link spans the links of widths 3, 2 and 5 immediately below it). Consequently, the sum of all widths is the same on every level (10 + 1 = 1 + 3 + 2 + 5 = 1 + 2 + 1 + 2 + 5).

To index the skiplist and find the i-th value, traverse the skiplist while counting down the widths of each traversed link. Descend a level whenever the upcoming width would be too large.

For example, to find the node in the fifth position (Node 5), traverse a link of width 1 at the top level. Now four more steps are needed but the next width on this level is ten which is too large, so drop one level. Traverse one link of width 3. Since another step of width 2 would be too far, drop down to the bottom level. Now traverse the final link of width 1 to reach the target running total of 5 (1+3+1).

function lookupByPositionIndex(i)

node ← head

i ← i + 1 # don't count the head as a step

for level from top to bottom do

while i ≥ node.width[level] do # if next step is not too far

i ← i - node.width[level] # subtract the current width

node ← node.next[level] # traverse forward at the current level

repeat

repeat

return node.value

end function

This method of implementing indexing is detailed in Section 3.4 Linear List Operations in "A skip list cookbook" by William Pugh.

Also, see Running Median using an Indexable Skiplist for a complete implementation written in Python and for an example of it being used to solve a computationally intensive statistics problem. And see Regaining Lost Knowledge for the history of that solution.

## History

Skip lists were first described in 1990 by William Pugh. He details how they work in

To quote the author:

Skip lists are a probabilistic data structure that seem likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space.

## Usages

List of applications and frameworks that use skip lists:

Cyrus IMAP server offers a "skiplist" backend DB implementation (source file)

QMap (up to Qt 4) template class of Qt that provides a dictionary.

Redis, an ANSI-C open-source persistent key/value store for Posix systems, uses skip lists in its implementation of ordered sets.

nessDB, a very fast key-value embedded Database Storage Engine (Using log-structured-merge (LSM) trees), uses skip lists for its memtable.

skipdb is an open-source database format using ordered key/value pairs.

Running Median using an Indexable Skiplist is a Python implementation of a skiplist augmented by link widths to make the structure indexable (giving fast access to the nth item). The indexable skiplist is used to efficiently solve the running median problem (recomputing medians and quartiles as values are added and removed from a large sliding window).

ConcurrentSkipListSet and ConcurrentSkipListMap in the Java 1.6 API.

Skip lists are also used in distributed applications (where the nodes represent physical computers, and pointers represent network connections) and for implementing highly scalable concurrent priority queues with less lock contention,[5] or even without locking, as well lockless concurrent dictionaries. There are also several US patents for using skip lists to implement (lockless) priority queues and concurrent dictionaries.

References:
[1] Pugh, William. (1990). Skip lists: a probabilistic alternative to balanced trees. Communications of the ACM. doi:10.1145/78973.78977
[2] Deterministic skip lists
[3] Shah, Gauri Ph.D.. (December 2003). Distributed Data Structures for Peer-to-Peer Systems. http://www.cs.yale.edu/homes/shah/pubs/thesis.pdf
[4] http://resnet.uoregon.edu/~gurney_j/jmpc/skiplist.html
[5] Skiplist-based concurrent priority queues
````

</details>

<details><summary><b>Step 6 — revision_6</b> (1715 words)</summary>

````text
In computer science, a skip list is a data structure that allows fast search within an ordered sequence of elements. Fast search is made possible by maintaining a linked hierarchy of subsequences, each skipping over fewer elements. Searching starts in the sparsest subsequence until two consecutive elements have been found, one smaller and one larger than the element searched for. Via the linked hierarchy these two elements link to elements of the next sparsest subsequence where searching is continued until finally we are searching in the full sequence. The elements that are skipped over may be chosen probabilistically.[1,2]

## Description

A skip list is built in layers. The bottom layer is an ordinary ordered linked list. Each higher layer acts as an "express lane" for the lists below, where an element in layer i appears in layer i+1 with some fixed probability p (two commonly used values for p are 1/2 or 1/4). On average, each element appears in 1/(1-p) lists, and the tallest element (usually a special head element at the front of the skip list) in \log_{1/p} n\, lists.

A search for a target element begins at the head element in the top list, and proceeds horizontally until the current element is greater than or equal to the target. If the current element is equal to the target, it has been found. If the current element is greater than the target, or the search reaches the end of the linked list, the procedure is repeated after returning to the previous element and dropping down vertically to the next lower list. The expected number of steps in each linked list is at most 1/p, which can be seen by tracing the search path backwards from the target until reaching an element that appears in the next higher list or reaching the beginning of the current list. Therefore, the total expected cost of a search is (\log_{1/p} n)/p,\, which is \mathcal{O}(\log n)\, when p is a constant. By choosing different values of p, it is possible to trade search costs against storage costs.

### Implementation details

The elements used for a skip list can contain more than one pointer since they can participate in more than one list.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

\mathcal{O}(n) operations, which force us to visit every node in ascending order (such as printing the entire list), provide the opportunity to perform a behind-the-scenes derandomization of the level structure of the skip-list in an optimal way, bringing the skip list to \mathcal{O}(\log n) search time. (Choose the level of the i'th finite node to be 1 plus the number of times we can repeatedly divide i by 2 before it becomes odd. Also, i=0 for the negative infinity header as we have the usual special case of choosing the highest possible level for negative and/or positive infinite nodes.) However this also allows someone to know where all of the higher-than-level 1 nodes are and delete them.

Alternatively, we could make the level structure quasi-random in the following way:

make all nodes level 1

j ← 1

while the number of nodes at level j > 1 do

for each i'th node at level j do

if i is odd

if i is not the last node at level j

randomly choose whether to promote it to level j+1

else

do not promote

end if

else if i is even and node i-1 was not promoted

promote it to level j+1

end if

repeat

j ← j + 1

repeat

Like the derandomized version, quasi-randomization is only done when there is some other reason to be running a \mathcal{O}(n) operation (which visits every node).

The advantage of this quasi-randomness is that it doesn't give away nearly as much level-structure related information to an adversarial user as the de-randomized one. This is desirable because an adversarial user who is able to tell which nodes are not at the lowest level can pessimize performance by simply deleting higher-level nodes. The search performance is still guaranteed to be logarithmic.

It would be tempting to make the following "optimization": In the part which says "Next, for each i'th...", forget about doing a coin-flip for each even-odd pair. Just flip a coin once to decide whether to promote only the even ones or only the odd ones. Instead of \mathcal{O}(n \log n) coin flips, there would only be \mathcal{O}(\log n) of them. Unfortunately, this gives the adversarial user a 50/50 chance of being correct upon guessing that all of the even numbered nodes (among the ones at level 1 or higher) are higher than level one. This is despite the property that he has a very low probability of guessing that a particular node is at level N for some integer N.

A skip list does not provide the same absolute worst-case performance guarantees as more traditional balanced tree data structures, because it is always possible (though with very low probability) that the coin-flips used to build the skip list will produce a badly balanced structure. However, they work well in practice, and the randomized balancing scheme has been argued to be easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in parallel computing, where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure. Such parallelism can be especially advantageous for resource discovery in an ad-hoc Wireless network because a randomized skip list can be made robust to the loss of any single node.[3]

There has been some evidence that skip lists have worse real-world performance and space requirements than B trees due to memory locality and other issues.[4]

### Indexable skiplist

As described above, a skiplist is capable of fast \mathcal{O}(\log n) insertion and removal of values from a sorted sequence, but it has only slow \mathcal{O}(n) lookups of values at a given position in the sequence (i.e. return the 500th value); however, with a minor modification the speed of random access indexed lookups can be improved to \mathcal{O}(\log n) .

For every link, also store the width of the link. The width is defined as the number of bottom layer links being traversed by each of the higher layer "express lane" links.

For example, here are the widths of the links in the example at the top of the page:

o---> o---------------------------------------------------------> o Top level

o---> o---------------> o---------> o---------------------------> o Level 3

o---> o---------> o---> o---------> o---------------------------> o Level 2

o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o Bottom level

Head 1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th NIL

Node Node Node Node Node Node Node Node Node Node

Notice that the width of a higher level link is the sum of the component links below it (i.e. the width 10 link spans the links of widths 3, 2 and 5 immediately below it). Consequently, the sum of all widths is the same on every level (10 + 1 = 1 + 3 + 2 + 5 = 1 + 2 + 1 + 2 + 5).

To index the skiplist and find the i'th value, traverse the skiplist while counting down the widths of each traversed link. Descend a level whenever the upcoming width would be too large.

For example, to find the node in the fifth position (Node 5), traverse a link of width 1 at the top level. Now four more steps are needed but the next width on this level is ten which is too large, so drop one level. Traverse one link of width 3. Since another step of width 2 would be too far, drop down to the bottom level. Now traverse the final link of width 1 to reach the target running total of 5 (1+3+1).

function lookupByPositionIndex(i)

node ← head

i ← i + 1 # don't count the head as a step

for level from top to bottom do

while i ≥ node.width[level] do # if next step is not too far

i ← i - node.width[level] # subtract the current width

node ← node.next[level] # traverse forward at the current level

repeat

repeat

return node.value

end function

This method of implementing indexing is detailed in Section 3.4 Linear List Operations in "A skip list cookbook" by William Pugh.

## History

Skip lists were first described in 1990 by William Pugh.[1]

To quote the author:

Skip lists are a probabilistic data structure that seem likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space.

## Usages

List of applications and frameworks that use skip lists:

Cyrus IMAP server offers a "skiplist" backend DB implementation (source file)

Lucene uses skip lists to search delta-encoded posting lists in logarithmic time.

QMap (up to Qt 4) template class of Qt that provides a dictionary.

Redis, an ANSI-C open-source persistent key/value store for Posix systems, uses skip lists in its implementation of ordered sets.[5]

nessDB, a very fast key-value embedded Database Storage Engine (Using log-structured-merge (LSM) trees), uses skip lists for its memtable.

skipdb is an open-source database format using ordered key/value pairs.

ConcurrentSkipListSet and ConcurrentSkipListMap in the Java 1.6 API.

leveldb, a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values

Skip lists are used for efficient statistical computations of running medians (also known as moving medians).

Skip lists are also used in distributed applications (where the nodes represent physical computers, and pointers represent network connections) and for implementing highly scalable concurrent priority queues with less lock contention,[6] or even without locking, as well lockless concurrent dictionaries. There are also several US patents for using skip lists to implement (lockless) priority queues and concurrent dictionaries.

References:
[1] Pugh, William. (June 1990). Skip lists: a probabilistic alternative to balanced trees. Communications of the ACM. doi:10.1145/78973.78977
[2] Deterministic skip lists
[3] Shah, Gauri Ph.D.. (December 2003). Distributed Data Structures for Peer-to-Peer Systems. http://www.cs.yale.edu/homes/shah/pubs/thesis.pdf
[4] http://resnet.uoregon.edu/~gurney_j/jmpc/skiplist.html
[5] Redis ordered set implementation. https://github.com/antirez/redis/blob/unstable/src/t_zset.c
[6] Skiplist-based concurrent priority queues
````

</details>

<details><summary><b>Step 7 — revision_7</b> (2041 words)</summary>

````text
In computer science, a skip list is a probabilistic data structure that allows \mathcal{O}(\log n) search complexity as well as \mathcal{O}(\log n) insertion complexity within an ordered sequence of n elements. Thus it can get the best features of a sorted array (for searching) while maintaining a linked list-like structure that allows insertion, which is not possible with a static array. Fast search is made possible by maintaining a linked hierarchy of subsequences, with each successive subsequence skipping over fewer elements than the previous one (see the picture below on the right). Searching starts in the sparsest subsequence until two consecutive elements have been found, one smaller and one larger than or equal to the element searched for. Via the linked hierarchy, these two elements link to elements of the next sparsest subsequence, where searching is continued until finally we are searching in the full sequence. The elements that are skipped over may be chosen probabilistically[1] or deterministically,[2] with the former being more common.

## Description

A skip list is built in layers. The bottom layer is an ordinary ordered linked list. Each higher layer acts as an "express lane" for the lists below, where an element in layer i appears in layer i+1 with some fixed probability p (two commonly used values for p are 1/2 or 1/4 ). On average, each element appears in 1/(1-p) lists, and the tallest element (usually a special head element at the front of the skip list) appears in all the lists. The skip list contains \log_{1/p}n\, (i.e. logarithm base 1/p of n ) lists.

A search for a target element begins at the head element in the top list, and proceeds horizontally until the current element is greater than or equal to the target. If the current element is equal to the target, it has been found. If the current element is greater than the target, or the search reaches the end of the linked list, the procedure is repeated after returning to the previous element and dropping down vertically to the next lower list. The expected number of steps in each linked list is at most 1/p , which can be seen by tracing the search path backwards from the target until reaching an element that appears in the next higher list or reaching the beginning of the current list. Therefore, the total expected cost of a search is \tfrac{1}{p}\log_{1/p}n which is \mathcal{O}(\log n)\, , when p is a constant. By choosing different values of p , it is possible to trade search costs against storage costs.

### Implementation details

The elements used for a skip list can contain more than one pointer since they can participate in more than one list.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

\mathcal{O}(n) operations, which force us to visit every node in ascending order (such as printing the entire list), provide the opportunity to perform a behind-the-scenes derandomization of the level structure of the skip-list in an optimal way, bringing the skip list to \mathcal{O}(\log n) search time. (Choose the level of the i'th finite node to be 1 plus the number of times we can repeatedly divide i by 2 before it becomes odd. Also, i=0 for the negative infinity header as we have the usual special case of choosing the highest possible level for negative and/or positive infinite nodes.) However this also allows someone to know where all of the higher-than-level 1 nodes are and delete them.

Alternatively, we could make the level structure quasi-random in the following way:

make all nodes level 1

j ← 1

while the number of nodes at level j > 1 do

for each i'th node at level j do

if i is odd and i is not the last node at level j

randomly choose whether to promote it to level j+1

else if i is even and node i-1 was not promoted

promote it to level j+1

end if

repeat

j ← j + 1

repeat

Like the derandomized version, quasi-randomization is only done when there is some other reason to be running an \mathcal{O}(n) operation (which visits every node).

The advantage of this quasi-randomness is that it doesn't give away nearly as much level-structure related information to an adversarial user as the de-randomized one. This is desirable because an adversarial user who is able to tell which nodes are not at the lowest level can pessimize performance by simply deleting higher-level nodes. (Bethea and Reiter however argue that nonetheless an adversary can use probabilistic and timing methods to force performance degradation.[3]) The search performance is still guaranteed to be logarithmic.

It would be tempting to make the following "optimization": In the part which says "Next, for each ith...", forget about doing a coin-flip for each even-odd pair. Just flip a coin once to decide whether to promote only the even ones or only the odd ones. Instead of \mathcal{O}(n \log n) coin flips, there would only be \mathcal{O}(\log n) of them. Unfortunately, this gives the adversarial user a 50/50 chance of being correct upon guessing that all of the even numbered nodes (among the ones at level 1 or higher) are higher than level one. This is despite the property that there is a very low probability of guessing that a particular node is at level N for some integer N.

A skip list does not provide the same absolute worst-case performance guarantees as more traditional balanced tree data structures, because it is always possible (though with very low probability[4]) that the coin-flips used to build the skip list will produce a badly balanced structure. However, they work well in practice, and the randomized balancing scheme has been argued to be easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in parallel computing, where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure. Such parallelism can be especially advantageous for resource discovery in an ad-hoc wireless network because a randomized skip list can be made robust to the loss of any single node.[5]

### Indexable skiplist

As described above, a skip list is capable of fast \mathcal{O}(\log n) insertion and removal of values from a sorted sequence, but it has only slow \mathcal{O}(n) lookups of values at a given position in the sequence (i.e. return the 500th value); however, with a minor modification the speed of random access indexed lookups can be improved to \mathcal{O}(\log n) .

For every link, also store the width of the link. The width is defined as the number of bottom layer links being traversed by each of the higher layer "express lane" links.

For example, here are the widths of the links in the example at the top of the page:

o---> o---------------------------------------------------------> o Top level

o---> o---------------> o---------> o---------------------------> o Level 3

o---> o---------> o---> o---------> o---------------> o---------> o Level 2

o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o Bottom level

Head 1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th NIL

Node Node Node Node Node Node Node Node Node Node

Notice that the width of a higher level link is the sum of the component links below it (i.e. the width 10 link spans the links of widths 3, 2 and 5 immediately below it). Consequently, the sum of all widths is the same on every level (10 + 1 = 1 + 3 + 2 + 5 = 1 + 2 + 1 + 2 + 3 + 2).

To index the skip list and find the i'th value, traverse the skip list while counting down the widths of each traversed link. Descend a level whenever the upcoming width would be too large.

For example, to find the node in the fifth position (Node 5), traverse a link of width 1 at the top level. Now four more steps are needed but the next width on this level is ten which is too large, so drop one level. Traverse one link of width 3. Since another step of width 2 would be too far, drop down to the bottom level. Now traverse the final link of width 1 to reach the target running total of 5 (1+3+1).

function lookupByPositionIndex(i)

node ← head

i ← i + 1 # don't count the head as a step

for level from top to bottom do

while i ≥ node.width[level] do # if next step is not too far

i ← i - node.width[level] # subtract the current width

node ← node.next[level] # traverse forward at the current level

repeat

repeat

return node.value

end function

This method of implementing indexing is detailed in "A skip list cookbook" by William Pugh[6]

## History

Skip lists were first described in 1989 by William Pugh.[7]

To quote the author:

## Usages

List of applications and frameworks that use skip lists:

Apache Portable Runtime implements skip lists.[8]

MemSQL uses lock-free skip lists as its prime indexing structure for its database technology.

Cyrus IMAP server offers a "skiplist" backend DB implementation[9]

Lucene uses skip lists to search delta-encoded posting lists in logarithmic time.

The "QMap" key/value dictionary (up to Qt 4) template class of Qt is implemented with skip lists.[10]

Redis, an ANSI-C open-source persistent key/value store for Posix systems, uses skip lists in its implementation of ordered sets.[11]

"nessDB", a very fast key-value embedded Database Storage Engine (Using log-structured-merge (LSM) trees), uses skip lists for its memtable.[12]

"skipdb" is an open-source implementation of an ACID ordered key/value database, implemented with a skip list instead of a b-tree.[13]

ConcurrentSkipListSet and ConcurrentSkipListMap in the Java 1.6 API.[14] Used by Apache HBase.

Speed Tables are a fast key-value datastore for Tcl that use skiplists for indexes and lockless shared memory.

"leveldb" is a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values[15]

Con Kolivas' MuQSS[16] Scheduler for the Linux kernel uses skip lists

SkiMap uses skip lists as base data structure to build a more complex 3D Sparse Grid for Robot Mapping systems.[17]

"IOWOW" is a persistent C11 key/value storage library that uses skip lists as its main data structure.[18]

Skip lists are used for efficient statistical computations of running medians (also known as moving medians).[19]

Skip lists are also used in distributed applications (where the nodes represent physical computers, and pointers represent network connections) and for implementing highly scalable concurrent priority queues with less lock contention,[20] or even without locking,[21,22,23] as well as lock-free concurrent dictionaries.[24] There are also several US patents for using skip lists to implement (lockless) priority queues and concurrent dictionaries.

References:
[1] Pugh, W.. (1990). Skip lists: A probabilistic alternative to balanced trees. Communications of the ACM. doi:10.1145/78973.78977
[2] Munro, J. Ian. (1992). Deterministic skip lists. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA. https://www.ic.unicamp.br/~celio/peer2peer/skip-net-graph/deterministic-skip-lists-munro.pdf
[3] Bethea, Darrell. (September 21–23, 2009). Data Structures with Unpredictable Timing. doi:10.1007/978-3-642-04444-1_28
[4] Sen, Sandeep. (1991). Some observations on skip lists. Information Processing Letters. doi:10.1016/0020-0190(91)90175-H
[5] Shah, Gauri. (2003). Distributed Data Structures for Peer-to-Peer Systems. Yale University. http://www.cs.yale.edu/homes/shah/pubs/thesis.pdf
[6] William Pugh. "A skip list cookbook". 1990. Section 3.4 Linear List Operations .
[7] Pugh, William. (April 1989). Concurrent Maintenance of Skip Lists. http://drum.lib.umd.edu/handle/1903/542
[8] Apache Portable Runtime APR 1.6 documentation
[9] Cyrus IMAP server. skiplist source file
[10] QMap
[11] Redis ordered set implementation. GitHub. https://github.com/antirez/redis/blob/unstable/src/t_zset.c
[12] nessDB
[13] skipdb
[14] ConcurrentSkipListSet and ConcurrentSkipListMap
[15] leveldb
[16] LKML: Con Kolivas: [ANNOUNCE] Multiple Queue Skiplist Scheduler version 0.120. lkml.org. https://lkml.org/lkml/2016/10/29/4
[17] Gregorio, Daniele De. (2017). SkiMap: An Efficient Mapping Framework for Robot Navigation.
[18] IOWOW
[19] Raymond Hettinger. "Efficient running median using an indexable skiplist (Python)". 2009.
[20] Shavit, N.. (2000). Proceedings 14th International Parallel and Distributed Processing Symposium. IPDPS 2000. doi:10.1109/IPDPS.2000.845994
[21] Sundell, H.. (2003). Proceedings International Parallel and Distributed Processing Symposium. doi:10.1109/IPDPS.2003.1213189
[22] Fomitchev, Mikhail. (2004). Lock-free linked lists and skip lists. doi:10.1145/1011767.1011776
[23] Bajpai, R.. (2008). 2008 IEEE International Symposium on Parallel and Distributed Processing with Applications. doi:10.1109/ISPA.2008.90
[24] Sundell, H. K.. (2004). Proceedings of the 2004 ACM symposium on Applied computing - SAC '04. doi:10.1145/967900.968188
````

</details>

<details><summary><b>Step 8 — final</b> (1972 words)</summary>

````text
In computer science, a skip list (or skiplist) is a probabilistic data structure that allows \mathcal O(\log n) average complexity for search as well as \mathcal O(\log n) average complexity for insertion within an ordered sequence of n elements. Thus it can get the best features of a sorted array (for searching) while maintaining a linked list-like structure that allows insertion, which is not possible with a static array. Fast search is made possible by maintaining a linked hierarchy of subsequences, with each successive subsequence skipping over fewer elements than the previous one (see the picture below). Searching starts in the sparsest subsequence until two consecutive elements have been found, one smaller and one larger than or equal to the element searched for. Via the linked hierarchy, these two elements link to elements of the next sparsest subsequence, where searching is continued until finally searching in the full sequence. The elements that are skipped over may be chosen probabilistically[1] or deterministically,[2] with the former being more common.

## Description

A skip list is built in layers. The bottom layer 1 is an ordinary ordered linked list. Each higher layer acts as an "express lane" for the lists below, where an element in layer i appears in layer i+1 with some fixed probability p (two commonly used values for p are 1/2 or 1/4 ). On average, each element appears in 1/(1-p) lists, and the tallest element (usually a special head element at the front of the skip list) appears in all the lists. The skip list contains \log_{1/p}n\, (i.e. logarithm base 1/p of n ) lists.

A search for a target element begins at the head element in the top list, and proceeds horizontally until the current element is greater than or equal to the target. If the current element is equal to the target, it has been found. If the current element is greater than the target, or the search reaches the end of the linked list, the procedure is repeated after returning to the previous element and dropping down vertically to the next lower list. The expected number of steps in each linked list is at most 1/p , which can be seen by tracing the search path backwards from the target until reaching an element that appears in the next higher list or reaching the beginning of the current list. Therefore, the total expected cost of a search is \tfrac{1}{p}\log_{1/p}n which is \mathcal O(\log n)\, , when p is a constant. By choosing different values of p , it is possible to trade search costs against storage costs. For example, the value p=1/e minimizes the average search time of skip lists, whereas the value p=1/2 simplifies their implementation.

### Implementation details

The elements used for a skip list can contain more than one pointer since they can participate in more than one list.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

\mathcal O(n) operations, which force us to visit every node in ascending order (such as printing the entire list), provide the opportunity to perform a behind-the-scenes derandomization of the level structure of the skip-list in an optimal way, bringing the skip list to \mathcal O(\log n) search time. (Choose the level of the i'th finite node to be 1 plus the number of times it is possible to repeatedly divide i by 2 before it becomes odd. Also, i=0 for the negative infinity header as there is the usual special case of choosing the highest possible level for negative and/or positive infinite nodes.) However this also allows someone to know where all of the higher-than-level 1 nodes are and delete them.

Alternatively, the level structure could be made quasi-random in the following way:

make all nodes level 1

j ← 1

while the number of nodes at level j > 1 do

for each i'th node at level j do

if i is odd and i is not the last node at level j

randomly choose whether to promote it to level j+1

else if i is even and node i-1 was not promoted

promote it to level j+1

end if

repeat

j ← j + 1

repeat

Like the derandomized version, quasi-randomization is only done when there is some other reason to be running an \mathcal O(n) operation (which visits every node).

The advantage of this quasi-randomness is that it doesn't give away nearly as much level-structure related information to an adversarial user as the de-randomized one. This is desirable because an adversarial user who is able to tell which nodes are not at the lowest level can pessimize performance by simply deleting higher-level nodes. (Bethea and Reiter however argue that nonetheless an adversary can use probabilistic and timing methods to force performance degradation.[3]) The search performance is still guaranteed to be logarithmic.

It would be tempting to make the following "optimization": In the part which says "Next, for each ith...", forget about doing a coin-flip for each even-odd pair. Just flip a coin once to decide whether to promote only the even ones or only the odd ones. Instead of \mathcal O(n \log n) coin flips, there would only be \mathcal O(\log n) of them. Unfortunately, this gives the adversarial user a 50/50 chance of being correct upon guessing that all of the even numbered nodes (among the ones at level 1 or higher) are higher than level one. This is despite the property that there is a very low probability of guessing that a particular node is at level N for some integer N.

A skip list does not provide the same absolute worst-case performance guarantees as more traditional balanced tree data structures, because it is always possible (though with very low probability[4]) that the coin-flips used to build the skip list will produce a badly balanced structure. However, they work well in practice, and the randomized balancing scheme has been argued to be easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in parallel computing, where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure. Such parallelism can be especially advantageous for resource discovery in an ad-hoc wireless network because a randomized skip list can be made robust to the loss of any single node.[5]

### Indexable skiplist

As described above, a skip list is capable of fast \mathcal O(\log n) insertion and removal of values from a sorted sequence, but it has only slow \mathcal O(n) lookups of values at a given position in the sequence (i.e. return the 500th value); however, with a minor modification the speed of random access indexed lookups can be improved to \mathcal O(\log n) .

For every link, also store the width of the link. The width is defined as the number of bottom layer links being traversed by each of the higher layer "express lane" links.

For example, here are the widths of the links in the example at the top of the page:

o---> o---------------------------------------------------------> o Top level

o---> o---------------> o---------> o---------------------------> o Level 3

o---> o---------> o---> o---------> o---------------> o---------> o Level 2

o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o Bottom level

Head 1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th NIL

Node Node Node Node Node Node Node Node Node Node

Notice that the width of a higher level link is the sum of the component links below it (i.e. the width 10 link spans the links of widths 3, 2 and 5 immediately below it). Consequently, the sum of all widths is the same on every level (10 + 1 = 1 + 3 + 2 + 5 = 1 + 2 + 1 + 2 + 3 + 2).

To index the skip list and find the i'th value, traverse the skip list while counting down the widths of each traversed link. Descend a level whenever the upcoming width would be too large.

For example, to find the node in the fifth position (Node 5), traverse a link of width 1 at the top level. Now four more steps are needed but the next width on this level is ten which is too large, so drop one level. Traverse one link of width 3. Since another step of width 2 would be too far, drop down to the bottom level. Now traverse the final link of width 1 to reach the target running total of 5 (1+3+1).

function lookupByPositionIndex(i)

node ← head

i ← i + 1 # don't count the head as a step

for level from top to bottom do

while i ≥ node.width[level] do # if next step is not too far

i ← i - node.width[level] # subtract the current width

node ← node.next[level] # traverse forward at the current level

repeat

repeat

return node.value

end function

This method of implementing indexing is detailed in "A skip list cookbook" by William Pugh[6]

## History

Skip lists were first described in 1989 by William Pugh.[7]

To quote the author:

## Usages

List of applications and frameworks that use skip lists:

Apache Portable Runtime implements skip lists.[8]

MemSQL uses lock-free skip lists as its prime indexing structure for its database technology.

MuQSS, for the Linux kernel, is a CPU scheduler built on skip lists.[9,10]

Cyrus IMAP server offers a "skiplist" backend DB implementation[11]

IBM DOORS offers skip lists as a data type in its DOORS/DXL (DOORS eXtension Language) scripting language

Lucene uses skip lists to search delta-encoded posting lists in logarithmic time.

The "QMap" key/value dictionary (up to Qt 4) template class of Qt is implemented with skip lists.[12]

Redis, an ANSI-C open-source persistent key/value store for Posix systems, uses skip lists in its implementation of ordered sets.[13]

Discord uses skip lists to handle storing and updating the list of members in a server.[14]

RocksDB uses skip lists for its default Memtable implementation.[15]

Java uses skip lists for its ConcurrentSkipListSet and ConcurrentSkipListMap.

Skip lists are also used in distributed applications (where the nodes represent physical computers, and pointers represent network connections) and for implementing highly scalable concurrent priority queues with less lock contention,[16] or even without locking,[17,18,19] as well as lock-free concurrent dictionaries.[20] There are also several US patents for using skip lists to implement (lockless) priority queues and concurrent dictionaries.

References:
[1] Pugh, W.. (1990). Skip lists: A probabilistic alternative to balanced trees. Communications of the ACM. doi:10.1145/78973.78977
[2] Munro, J. Ian. (1992). Deterministic skip lists. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA. https://www.ic.unicamp.br/~celio/peer2peer/skip-net-graph/deterministic-skip-lists-munro.pdf
[3] Bethea, Darrell. (September 21–23, 2009). Data Structures with Unpredictable Timing. doi:10.1007/978-3-642-04444-1_28
[4] Sen, Sandeep. (1991). Some observations on skip lists. Information Processing Letters. doi:10.1016/0020-0190(91)90175-H
[5] Shah, Gauri. (2003). Distributed Data Structures for Peer-to-Peer Systems. Yale University. http://www.cs.yale.edu/homes/shah/pubs/thesis.pdf
[6] William Pugh. "A skip list cookbook". 1990. Section 3.4 Linear List Operations .
[7] Pugh, William. (April 1989). Concurrent Maintenance of Skip Lists. http://drum.lib.umd.edu/handle/1903/542
[8] Apache Portable Runtime APR 1.6 documentation
[9] LWN's article
[10] LKML: Con Kolivas: [ANNOUNCE] Multiple Queue Skiplist Scheduler version 0.120. lkml.org. https://lkml.org/lkml/2016/10/29/4
[11] Cyrus IMAP server. skiplist source file
[12] QMap
[13] Redis ordered set implementation. GitHub. https://github.com/antirez/redis/blob/unstable/src/t_zset.c
[14] Nowack, Matt. Using Rust to Scale Elixir for 11 Million Concurrent Users. Discord Blog. https://discord.com/blog/using-rust-to-scale-elixir-for-11-million-concurrent-users
[15] MemTable. GitHub. https://github.com/facebook/rocksdb/wiki/MemTable
[16] Shavit, N.. (2000). Proceedings 14th International Parallel and Distributed Processing Symposium. IPDPS 2000. doi:10.1109/IPDPS.2000.845994
[17] Sundell, H.. (2003). Proceedings International Parallel and Distributed Processing Symposium. doi:10.1109/IPDPS.2003.1213189
[18] Fomitchev, Mikhail. (2004). Lock-free linked lists and skip lists. doi:10.1145/1011767.1011776
[19] Bajpai, R.. (2008). 2008 IEEE International Symposium on Parallel and Distributed Processing with Applications. doi:10.1109/ISPA.2008.90
[20] Sundell, H. K.. (2004). Proceedings of the 2004 ACM symposium on Applied computing - SAC '04. doi:10.1145/967900.968188
````

</details>
