# 6. Fenwick tree

`B-Fenwick_tree` · [B_wiki_history_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Fenwick_tree&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 849 revisions in history; 34 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | earliest_version | 173 | 0 | 0.03 | enwiki rev 290045396 (2009-05-15) |
| 2 | early_revision | 922 | 4 | 0.22 | enwiki rev 1060356795 (2021-12-15) |
| 3 | late_revision | 893 | 7 | 0.43 | enwiki rev 1179649150 (2023-10-11) |
| 4 | final | 1954 | 10 | 1.00 | enwiki rev 1371848142 (2026-08-28) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Fenwick tree
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (173 words)</summary>

````text
A Fenwick Tree is a Binary Indexed Tree that can be used to store frequency related data for items or intervals.

## Structure

A Fenwick Tree is a binary tree that is indexed by the bits of the key for that tree. This tree can only be implemented for keys that are integers and have a fixed range.

We typically implement Fenwick Trees using an array.

## Applications

Fenwick Trees are used to implement the arithmetic coding algorithm, so the operations it supports are guided primarily by the use that it will be put to in the application above.

## Operations Supported

The Fenwick Tree supports 4 basic operations each of which take time <i>O(log2n)<i>.

### Change the frequency at some position and update the tree

### Read the Cumulative Frequency for a given key

### Read the actual(not cumulative) frequency at a certain position

### Find the index with a given cumulative frequency

It also supports a scaling operation which takes time O(n).

### Scale the entire tree by a certain factor
````

</details>

<details><summary><b>Step 2 — early_revision</b> (922 words)</summary>

````text
A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers.

This structure was proposed by Boris Ryabko in 1989[1]

with a further modification published in 1992.[2]

It has subsequently become known under the name Fenwick tree after Peter Fenwick, who described this structure in his 1994 article.[3]

When compared with a flat array of numbers, the Fenwick tree achieves a much better balance between two operations: element update and prefix sum calculation. A flat array of n numbers can either store the elements or the prefix sums. In the first case, computing prefix sums requires linear time; in the second case, updating the array elements requires linear time (in both cases, the other operation can be performed in constant time). Fenwick trees allow both operations to be performed in O(\log n) time. This is achieved by representing the numbers as a tree, where the value of each node is the sum of the numbers in that subtree. The tree structure allows operations to be performed using only O(\log n) node accesses.

## Motivation

Given a table of elements, it is sometimes desirable to calculate the running total of values up to each index according to some associative binary operation (addition on integers being by far the most common). Fenwick trees provide a method to query the running total at any index, in addition to allowing changes to the underlying value table and having all further queries reflect those changes.

Fenwick trees are particularly designed to implement the arithmetic coding algorithm, which maintains counts of each symbol produced and needs to convert those to the cumulative probability of a symbol less than a given symbol. Development of operations it supports were primarily motivated by use in that case.

Using a Fenwick tree it requires only O(\log n) operations to compute any desired cumulative sum, or more generally the sum of any range of values (not necessarily starting at zero).

Fenwick trees can be extended to update and query subarrays of multidimensional arrays. These operations can be performed with complexity O(4^d \log^d n) , where d is number of dimensions and n is the number of elements along each dimension.[4]

## Description

Although Fenwick trees are trees in concept, in practice they are implemented as an implicit data structure using a flat array analogous to implementations of a binary heap. Given an index in the array representing a vertex, the index of a vertex's parent or child is calculated through bitwise operations on the binary representation of its index. Each element of the array contains the pre-calculated sum of a range of values, and by combining that sum with additional ranges encountered during an upward traversal to the root, the prefix sum is calculated. When a table value is modified, all range sums that contain the modified value are in turn modified during a similar traversal of the tree. The range sums are defined such that both queries and modifications to the table are executed in asymptotically equivalent time ( O(\log n) in the worst case).

The initial process of building the Fenwick tree over a table of values runs in O(n) time. Other efficient operations include locating the index of a value if all values are positive, or all indices with a given value if all values are non-negative. Also supported is the scaling of all values by a constant factor in O(n) time.

A Fenwick tree is most easily understood by considering a one-based array. Each element whose index i is a power of 2 contains the sum of the first i elements. Elements whose indices are the sum of two (distinct) powers of 2 contain the sum of the elements since the preceding power of 2. In general, each element contains the sum of the values since its parent in the tree, and that parent is found by clearing the least significant bit in the index.

To find the sum up to any given index, consider the binary expansion of the index and add elements corresponding to each 1 bit in the binary form.

For example, say one wishes to find the sum of the first eleven values. Eleven is 10112 in binary. This contains three 1 bits, so three elements must be added: 10002, 10102, and 10112. These contain the sums of values 1–8, 9–10, and 11, respectively.

To modify the eleventh value, the elements that must be modified are 10112, 11002, 100002, and all higher powers of 2 up to the size of the array. These contain the sums of values 11, 9–12, and 1–16, respectively. The maximum number of elements that may need to be updated is limited by the number of bits in the size of the array.

## Implementation

### Basic implementation in C

### Useful functions in C

### Implementation in C++

## Updating and querying the tree

The following table describes various ways in which Fenwick tree can be used. More importantly, it states the right API to be called or used in order to achieve the desired result along with an example explaining the use case.

References:
[1] Boris Ryabko. (1989). A fast on-line code. Soviet Math. Dokl.. http://boris.ryabko.net/dan1989.pdf
[2] Boris Ryabko. (1992). A fast on-line adaptive code. IEEE Transactions on Information Theory. http://boris.ryabko.net/ryabko1992.pdf
[3] Peter M. Fenwick. (1994). A new data structure for cumulative frequency tables. Software: Practice and Experience. doi:10.1002/spe.4380240306
[4] Pushkar Mishra. (2013). A New Algorithm for Updating and Querying Sub-arrays of Multidimensional Arrays. doi:10.13140/RG.2.1.2394.2485
````

</details>

<details><summary><b>Step 3 — late_revision</b> (893 words)</summary>

````text
A Fenwick tree or binary indexed tree (BIT) is a data structure that can efficiently update values and calculate prefix sums in an array of values.

This structure was proposed by Boris Ryabko in 1989[1]

with a further modification published in 1992.[2]

It has subsequently become known under the name Fenwick tree after Peter Fenwick, who described this structure in his 1994 article.[3]

When compared with a flat array of values, the Fenwick tree achieves a much better balance between two operations: value update and prefix sum calculation. A flat array of n values can either store the values or the prefix sums. In the first case, computing prefix sums requires linear time; in the second case, updating the array values requires linear time (in both cases, the other operation can be performed in constant time). Fenwick trees allow both operations to be performed in O(\log n) time. This is achieved by representing the values as a tree with n+1 nodes where the value of each node in the tree is the prefix sum of the array from the index of the parent (inclusive) up to the index of the node (exclusive). The tree itself is implicit and can be stored as an array of n values, with the implicit root node omitted from the array. The tree structure allows the operations of value retrieval, value update, prefix sum, and range sum to be performed using only O(\log n) node accesses.

## Motivation

Given an array of values, it is sometimes desirable to calculate the running total of values up to each index according to some associative binary operation (addition on integers being by far the most common). Fenwick trees provide a method to query the running total at any index, in addition to allowing changes to the underlying value array and having all further queries reflect those changes.

Fenwick trees are particularly designed to implement the arithmetic coding algorithm, which maintains counts of each symbol produced and needs to convert those to the cumulative probability of a symbol less than a given symbol. Development of operations it supports were primarily motivated by use in that case.

## Description

A Fenwick tree is most easily understood by considering a one-based array A[n] with n values. The corresponding Fenwick tree has n+1 nodes with an implicit node 0 at the root. Each level k of the tree contains nodes with indices corresponding to sums of k distinct powers of 2 (with k=0 representing an empty sum 0). For example, level k=1 contains nodes 1=2^0, 2=2^1, 4=2^2, ... and level k=2 contains nodes 3=2^1 + 2^0, 5 = 2^2 + 2^0, 6 = 2^2 + 2^1, ... The parent of a given node can be found by clearing the last set bit (LSB) in its index, corresponding to the smallest power of 2 in its sum. For example, the parent of 6 = 1102 is 4 = 1002.

The below diagram shows the structure of a 16-node Fenwick tree, corresponding to a 15-element array A:

Let A(i,j] = \{ A[k] \}_{k=i+1}^j . The value of a node at index i corresponds to the range sum of values in A(\mathrm{parent}(i),i] , that is, the values of A starting after the parent's index up to the current node's index, inclusive. The values A(\mathrm{parent}(i),i] are considered to be the "range of responsibility" for the current node, and consist of \mathrm{lsb}(i) = (i\ \&\ (-i)) (where & denotes bitwise AND) values. Note that the indices in this range do not directly correspond to children of i : for example, the range of responsibility for node 2 is A(0,2] = \{A[1], A[2]\} but node 1 is not a child of node 2. The root node 0 contains the sum of the empty range A(0,0] = \{\} with value 0.

The initial process of building the Fenwick tree over an array of values runs in O(n \log n) time.

## Pseudocode

A simple pseudocode implementation of the two main operations on a Fenwick tree—query and update—is as following:

function query(tree, index) is

sum := 0

while index > 0 do

sum += tree[index]

index -= lso(index)

return sum

function update(tree, index, value) is

while index < size(tree) do

tree[index] += value

index += lso(index)

The function \text{lso}(n) computes the least significant 1-bit or last set bit of the given n or, equivalently, the largest power of two that is also a divisor of n . For example, \text{lso}(20) = 4 , as shown in its binary representation: \text{lso}(10\textbf{1}00_2) = 100_2 = 4 . This function can be simply implemented in code through a bitwise AND operation: lso(n) = n & (-n), assuming a signed integer data type.[3]

### Construction

One naive algorithm to construct a Fenwick tree consists of initializing the tree with null values and updating each index individually. This solution works in O(n\log{n}) time, but an O(n) construction is possible:[4]

function construct(values) is

tree := values

for every index, value in tree do

parentIndex := index + lso(index)

if parentIndex < size(tree) then

tree[parentIndex] += value

return tree

References:
[1] Boris Ryabko. (1989). A fast on-line code. Soviet Math. Dokl.. http://boris.ryabko.net/dan1989.pdf
[2] Boris Ryabko. (1992). A fast on-line adaptive code. IEEE Transactions on Information Theory. http://boris.ryabko.net/ryabko1992.pdf
[3] Peter M. Fenwick. (1994). A new data structure for cumulative frequency tables. Software: Practice and Experience. doi:10.1002/spe.4380240306
[4] Halim, Steven. Competitive Programming.
````

</details>

<details><summary><b>Step 4 — final</b> (1954 words)</summary>

````text
A Fenwick tree or binary indexed tree (BIT) is a data structure that stores an array of values and can efficiently compute prefix sums of the values and update the values. It also supports an efficient rank-search operation for finding the longest prefix whose sum is no more than a specified value. Its primary use is operating on the cumulative distribution function of a statistical frequency table which is updated often.

This structure was proposed by Boris Ryabko in 1989[1]

with a further modification published in 1992.[2]

It has subsequently become known under the name Fenwick tree after Peter Fenwick, who described this structure in his 1994 article.[3]

A simple array of values is trivial (constant-time) to update but requires O(n) time to compute a prefix sum or search for a prefix length.

An array of prefix sums can return a prefix sum in constant time, and search for a prefix length in O(\log n) time, but requires O(n) time to update one of the values.

A Fenwick tree allows all three operations to be performed in O(\log n) time. This is achieved by representing the values as a tree with n+1 nodes where each node in the tree stores the sum of the values from the index of its parent (exclusive) up to the index of the node (inclusive). The tree itself is implicit and can be stored as an array of n values, with the implicit root node omitted from the array. The tree structure allows the operations of value retrieval, value update, prefix sum, and range sum to be performed using only O(\log n) node accesses.

## Motivation

Given an array of values, it is sometimes desirable to calculate the running total of values up to each index according to some associative binary operation (addition on integers being by far the most common). Fenwick trees provide a method to query the running total at any index, or prefix sum, while allowing changes to the underlying value array and having all further queries reflect those changes.

Fenwick trees are particularly designed to implement adaptive arithmetic coding, which maintains counts of each symbol produced and needs to convert those to the cumulative probability of a symbol less than a given symbol. Development of operations it supports were primarily motivated by use in that case.

## Description

A Fenwick tree is an implicit tree where nodes are consecutively numbered, and parent-child relationships are determined by arithmetic on the node indexes.

An important function in this index arithmetic is the least significant set bit. This is the greatest power of two which divides an index i . This is the power of two (1, 2, 4, 8, ...) and not the exponent (0, 1, 2, 3, ...). It can be efficiently computed in two's complement arithmetic as \operatorname{lsb}(i) = i\mathbin\& -i (where & denotes bitwise AND).

A Fenwick tree is most easily understood using a one-based array A[n] with n values. Using half-open interval syntax, let A(i,j] = \{ A[k] \}_{k=i+1}^j, the range from i (exclusive) to j (inclusive). The corresponding Fenwick array F[n] stores the range sums \textstyle F[i] = \sum A(i-\operatorname{lsb}(i),i] . That is, the sum of \operatorname{lsb}(i) values ending with and including A[i] .

A fictitious node 0 is used in some descriptions, but is never actually accessed and need not be explicitly stored. \operatorname{lsb}(0) = \infty, but the value is never actually needed. F[0] may be considered to contain the sum of the empty range A(0,0] = \{\} with value 0.

A "Fenwick tree" is actually three implicit trees over the same array: the interrogation tree used for translating indexes to prefix sums, the update tree used for updating elements, and the search tree for translating prefix sums to indexes (rank queries).[4] The first two are normally walked upwards, while the third is usually walked downwards.

### The interrogation tree

The interrogation tree is defined so that the parent of node i is i - \operatorname{lsb}(i) = i \mathbin\& (i-1) . For example, the parent of 6 = 1102 is 4 = 1002. Implicit node 0 is the root.

Each level k of the tree contains nodes with indices corresponding to sums of k distinct powers of 2 (with k=0 representing an empty sum 0). For example, level k=1 contains nodes 1=2^0, 2=2^1, 4=2^2, ... and level k=2 contains nodes 3=2^1 + 2^0, 5 = 2^2 + 2^0, 6 = 2^2 + 2^1, ...

Node i has \log_2(\operatorname{lsb}(i)) children ( i+1, i+2, i+4, ..., i+\operatorname{lsb}(i)/2 ), and \operatorname{lsb}(i)-1 total descendants. (These numbers include nodes greater than n , which are omitted and never accessed.)

The below diagram shows the structure of a 16-node Fenwick tree's interrogation tree, including the root, so it corresponds to a 15-element array A:

To find the prefix sum A[1] + \cdots + A[i] , sum the values in i , its parent, its parent's parent, and so on up to (but not including) the root. To compute a range sum A[i] + \cdots + A[j] , subtract the prefix sums for i-1 and j .

This can be optimized by stopping at their first common ancestor. An extreme example is asking for a single entry A[j] . In this case, the common ancestor of j and i = j-1 is j - \operatorname{lsb}(j) , so start with F[j] and then, as long as i \neq j - \operatorname{lsb}(j) , subtract F[i] and update i := i - lsb(i).

### The update tree

The update tree is the mirror image of the interrogation tree. The parent of node i is i + \operatorname{lsb}(i) = (i \mathbin| (i - 1)) + 1 (where | denotes bitwise OR). For example, the parent of 6 = 1102 is 8 = 10002.

This conceptual tree is infinite, but only the part with indexes up to n is stored or used. Excluding the fictitious nodes with indexes greater than n it will be a forest of disjoint trees, one for each bit set in the binary representation of n .

Here, a node's ancestors are all nodes whose range sums include its own. For example, F[6] holds the sum of A(4,6] , F[8] holds the sum of A(0,8] , and so on.

To modify one of the values A[i] , add the change to F[i] , then i 's parent, then its grandparent, and so on, until the index exceeds n .

### The search tree

Unlike the other two trees, the search tree is a binary tree, arranged in an order Knuth calls a "sideways heap". Each node is assigned a height equal to the number of trailing zeros in the binary representation of its index, with the parent and children being the numerically closest index(es) of the adjacent height. Nodes with odd indexes ( \operatorname{lsb}(i) = 1 ) are leaves. Nodes with even indexes have the closest two nodes of the next-lowest index as children, i \pm \operatorname{lsb}(i)/2 . Node i 's parent in the search tree is (i - \operatorname{lsb}(i)) \mathbin| (2 \cdot \operatorname{lsb}(i)) .

For example, the children of 6 = 1102 are 5 = 1012 and 7 = 1112, and its parent is 4 = 1002.

Although this tree is potentially infinite, we may define its root to be the highest existing node, whose index is the greatest power of 2 less than or equal to n .

It is possible for a node to have a fictitious parent with an index greater than n yet still have an existing grandparent. If the example above applied to a 5-node tree, then node 5 would have a fictitious parent 6, but an existing grandparent 4.

The search tree may be considered a combination of the previous two trees. A node's left subtree contains all of its descendants in the update tree, while its right subtree contains all of its descendants in the interrogation tree. A node's parent in the search tree is either its interrogation or update parent (depending on whether the node is a right or left child, respectively), and the other type of parent may be found by multiple upward steps in the search tree.

However, upward traversals in the search tree are uncommon; its primary use is to perform rank queries: given a prefix sum, at what index does it appear? This is done by a downward traversal through the search tree. During the traversal, three variables are maintained: The current node's index, the rank being sought in the subtree rooted at the current node, and a "fallback index" to be returned if the rank sought is greater than can be found in the subtree.

Initially, the current node is the root, the rank sought is the original query, and the fallback index is a special "overflow" value indicating that the rank is not in the tree. (Depending on the application, 0 or n+1 might be used for this purpose.)

Each step, either the current node is a fictitious node (index greater than n ), or we must decide if the position sought is to the left or right of the end of the current node. If the rank sought is less than the Fenwick array value F[i] for the current node, we must search its left subtree. If it is greater, search its right subtree. If it is equal, the direction chosen depends on how you wish to handle searches for sums lying exactly between two nodes.

These three possibilities are then further divided based on whether the current node is a leaf or not:

If the current node is a leaf and:

the target is in its (empty) left subtree, return the current index.

it is fictitious or the target is in its right subtree, return the fallback index.

If the current node is not a leaf and:

it is fictitious, search for the same rank in its left subtree with an unchanged fallback index.

the target is in its left subtree, search for the same rank in its left subtree with the current index as the fallback index.

the target is in its right subtree, search for the target rank minus the current node's value in the right subtree, with an unchanged fallback index.

## Pseudocode

A simple pseudocode implementation of the two main operations on a Fenwick tree—query and update—is as following:

function query(tree, index) is

sum := 0

while index > 0 do

sum += tree[index]

index -= lsb(index)

return sum

function update(tree, index, value) is

while index < size(tree) do

tree[index] += value

index += lsb(index)

The function \text{lsb}(n) computes the least significant set bit of the given n or, equivalently, the largest power of two that is also a divisor of n . For example, \text{lsb}(20) = 4 , as shown in its binary representation: \text{lsb}(10\textbf{1}00_2) = 100_2 = 4 . This function can be simply implemented in code through a bitwise AND operation: lsb(n) = n & (-n), assuming two's complement negation.[3]

### Construction

One naïve algorithm to construct a Fenwick tree consists of initializing the tree with null values and updating each index individually. This solution works in O(n\log{n}) time, but an O(n) construction is possible:[5]

function construct(values) is

tree := values

for index from 1 to size(tree) do

parentIndex := index + lsb(index)

if parentIndex < size(tree) then

tree[parentIndex] += tree[index]

return tree

References:
[1] Boris Ryabko. (1989). A fast on-line code. Soviet Math. Dokl.. http://boris.ryabko.net/dan1989.pdf
[2] Boris Ryabko. (1992). A fast on-line adaptive code. IEEE Transactions on Information Theory. http://boris.ryabko.net/ryabko1992.pdf
[3] Peter M. Fenwick. (1994). A new data structure for cumulative frequency tables. Software: Practice and Experience. doi:10.1002/spe.4380240306
[4] Marchini, Stefano. (14 October 2019). Compact Fenwick trees for dynamic ranking and selection.
[5] Halim, Steven. (3 December 2018). Competitive Programming 4. Lulu Press, Incorporated.
````

</details>
