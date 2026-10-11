# 5. Rope (data structure)

`B-Rope_data_structure` · [B_wiki_history_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 298 revisions in history; 31 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 3 | 0 | 0.00 | source_title |
| 1 | earliest_version | 29 | 0 | 0.02 | enwiki rev 16948440 (2005-01-26) |
| 2 | early_revision | 1338 | 1 | 0.29 | enwiki rev 479253703 (2012-02-28) |
| 3 | late_revision | 1181 | 1 | 0.65 | enwiki rev 593682215 (2014-02-03) |
| 4 | final | 1199 | 1 | 1.00 | enwiki rev 1372318141 (2026-08-31) |

<details><summary><b>Step 0 — title</b> (3 words)</summary>

````text
Rope (data structure)
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (29 words)</summary>

````text
The concept of a heavyweight string, called a rope, involving the use of a concatenation tree representation, was introduced in a paper called "Ropes: an Alternative to Strings".

http://www.cs.ubc.ca/local/reading/proceedings/spe91-95/spe/vol25/issue12/spe986.pdf
````

</details>

<details><summary><b>Step 2 — early_revision</b> (1338 words)</summary>

````text
In computer programming a rope, or cord, is a data structure for efficiently storing and manipulating a very long string. For example, a text editing program may use a rope to represent the text being edited, so that operations such as insertion, deletion, and random access can be done efficiently.[1]

## Description

A rope is a binary tree in which each node has a weight. Leaf nodes (as well as some single-child internal nodes) also contain a short string. The weight of a node is equal to the length of its string plus the sum of all the weights in its left subtree. Thus a node with two children divides the whole string into two parts: the left subtree stores the first part of the string, the right subtree stores the second part, and the weight is the length of the first part.

Seen from another perspective, the binary tree of a rope can be seen as several levels of nodes. The bottom level contains all the nodes that have a short string. Higher levels have fewer and fewer nodes, until finally there is just one root node in the top level. We can build the rope by putting all the nodes with short strings in the bottom level, then randomly picking half those nodes in order to form parent nodes in the next level. Nodes with no parent (for example, the two nodes storing the strings "my_" and "me_i" in the diagram above) become the right child of the node located immediately to their left, thus forming a chain. In this way, we can build higher levels one level at a time. We stop when there is only one node remaining.

## Operations

### Search

Definition: Search(i): return the character at position i

Time complexity: O(log N) where N is the length of the rope

To retrieve the i-th character, we begin a recursive search from the root node:

// Note: Assumes 1-based indexing.

function search(RopeNode node, integer i)

if node.weight < i then

return search(node.right, i - node.weight)

else

if exists(node.left) then

return search(node.left, i)

else

return node.string[i]

endif

endif

end

For example, suppose we are looking for the character at i=10 in the following rope. We start at the root node, find that 22 is greater than 10 and there's a left child, so we go to the left child. Next we find that 9 is less than 10, so we subtract 9 from 10 (leaving i=1) and go to the right child. Then because 7 is greater than 1 and there's a left child, we go to the left child. There we find that 6 is greater than 1 and there's a left child, so we go to the left child again. Finally we see that 2 is greater than 1 but there is no left child, so we take the character at index 1 of the short string "na", returning "n" as the final answer.

### Split

Definition: Split (i, S): split the string S into two new strings S1 and S2, S1 = C1,…Ci and S2 = Ci+1, …, Cm.

There are two cases: in the first, the i-th character is the end of an array like the following picture; in the second, the character is in the middle of an array. We can reduce the second case to the first case as follows: first we split the node at the character into two nodes each with part of the array and make the second node as the right child of first node. We handle the first case as explained in the following example.

For example, we want to split the following rope into two parts. First we query the i-th character to locate the node v at the bottom level. Then we cut down the link between v and the right child of v, which we'll call v’. Then go up to the parent u and subtract the weight of v’ from the weight of u. Since the parent has the right child of u, which we'll call u’, modify u’ to link to v’ and increase the weight of u’ by the weight of its new left child v’. The former left child of u’ become the right child of v’. The result is shown in the second picture below. In this way, we continue up and reach the parent of u, which we'll call w. First subtract the weight of v’ from the weight of w. Then modify the right child of w, which we'll call w’, to link to u’ and the former child of w’ becomes the right child of u’. Then increase the weight of w’ by the weight of v’. Then go up and reach the parent of w, which we'll call x. Since w is already the right child of x, there is no need for further modification. Then go up and reach the parent of x, which we'll call y, and reduce the weight of x by the weight of w’.Clearly, the expected cost is O(log N).

### Concat

Definition: Concat(S1, S2): concatenate two rope S1, S2 into one single rope.

This operation can be considered as the reversion of split. The time complexity is also O(log N). Alternatively, create a new root node with left=S1 and right=S2. This is constant time, but can lead to an unbalanced tree.

### Insert

Definition: Insert(i, S’): insert the string S’ beginning at position i in the string s, to form a new string C1,….,Ci, S’, Ci+1,…, Cm.

This operation can be done by a split() and a concat(). First split the rope at the i-th character, the add a new node v with string(v) = S’ to the right child of the rightmost node of the first rope. Then update the weight of nodes in the path from the new node to root. Finally concatenate the two ropes. Because the split() and concat() both cost O(logN) time, the time complexity of this operation is also O(logN).

### Delete

Definition: Delete(i, j): delete the substring Ci, …, Ci+j-1, from s to form a new string C1, …, Ci-1, Ci+j, …, Cm.

This operation can be done by two split() and a concat(). First, split the rope into three ropes divided by i-th and j-th character respectively,that is, first split S into S1 and S2 at i-th character, then split S1 into S3 and S4 at (j-i)-th character, then concatenate the S1 and S2. Because the split() and concat() both cost O(logN) time, the time complexity of this operation is also O(logN).

### Report

Definition: Report(i, j): output the string Ci, …, Ci+j-1.

To report the string Ci, …, Ci+j-1, we first search for the node u that contains ci and weight(u) >=j, and then traverse T starting at node u. we can then output Ci, …, Ci+j-1 in O(j+logN) expected time by doing an in-order traversal of T starting at node u.

## Advantages and disadvantages

Advantages:

Ropes enable much faster insertion and deletion of text than ordinary strings.

Ropes don't need the extra O(n) memory that arrays need for copying operations, and ropes don't require a large contiguous memory space to store a string.

Disadvantages:

Slightly greater overall space usage (mainly to store the nodes that don't have strings)

Increase in time that the extra storage requires

## Comparison to array-based strings

This table compares the algorithmic characteristics of string and rope implementations, not their "raw speed". Array-based strings have smaller overhead, so (for example) concatenation and split operations are faster on small datasets. However, when array-based strings are used for large sets of data, time complexity and memory usage for insertion and deletion of characters becomes unacceptably large. A rope data structure, on the other hand, has a stable performance regardless of data size. Moreover, the space complexity for ropes and arrays are both O(n). In summary, ropes are better suited when the data is large and frequently modified.

References:
[1] Boehm, Hans-J. (December 1995). Ropes: an Alternative to Strings. Software—Practice & Experience. doi:10.1002/spe.4380251203
````

</details>

<details><summary><b>Step 3 — late_revision</b> (1181 words)</summary>

````text
In computer programming a rope, or cord, is a data structure composed of smaller strings that is used for efficiently storing and manipulating a very long string. For example, a text editing program may use a rope to represent the text being edited, so that operations such as insertion, deletion, and random access can be done efficiently.[1]

## Description

A rope is a binary tree having leaf nodes that contain a short string. Each node has a "weight" equal to the length of its string plus the sum of all the weights in its left subtree. Thus a node with two children divides the whole string into two parts: the left subtree stores the first part of the string. The right subtree stores the second part and its weight is the sum of the left child's weight and the length of its contained string.

The binary tree can be seen as several levels of nodes. The bottom level contains all the nodes that contain a string. Higher levels have fewer and fewer nodes. The top level consists of a single "root" node. The rope is built by putting the nodes with short strings in the bottom level, then attaching a random half of the nodes to parent nodes in the next level.

## Operations

In the following definitions, N is the length of the rope.

### Index

Definition: Index(i): return the character at position i

Time complexity: O(log N)

To retrieve the i-th character, we begin a recursive search from the root node:

For example, to find the character at i=10 in Figure 2.1 shown on the right, start at the root node (A), find that 22 is greater than 10 and there is a left child, so go to the left child (B). 9 is less than 10, so subtract 9 from 10 (leaving i=1) and go to the right child (D). Then because 7 is greater than 1 and there's a left child, go to the left child (G). 6 is greater than 1 and there's a left child, so go to the left child again (J). Finally 2 is greater than 1 but there is no left child, so the character at index 1 of the short string "na", is the answer.

### Split

Definition: Split (i, S): split the string S into two new strings S1 and S2, S1 = C1, …, Ci and S2 = , …, Cm.

Time complexity: O(log N)

There are two cases that must be dealt with:

The split point is at the end of a string (i.e. after the last character of a leaf node)

The split point is in the middle of a string.

The second case reduces to the first by splitting the string at the split point into two strings each with part of the parent string and create a new node that is the parent of the two component strings.

For example, to split the 22-character rope pictured in Figure 2.2 into two equal component ropes of length 11, query the 12th character to locate the node K at the bottom level. Remove the link between K and the right child of G. Go to the parent G and subtract the weight of K from the weight of G. Travel up the tree and remove any right links, subtracting the weight of K from these nodes (only node D, in this case). Finally, build up the newly-orphaned nodes K and H by adding new parent nodes and setting the weight of the parent node to the total weight of the left child K.

### Concat

Definition: Concat(S1, S2): concatenate two ropes, S1 and S2, into a single rope.

Time complexity: O(log N)

This operation is the reverse of split, and requires O(log N) time on average to produce a rope with a balanced tree. (If one drops the constraint that the output tree should be balanced, a concatenation can be performed simply by creating a new root node with left = S1 and right = S2, which is constant time. Complexity estimates of other operations do however require ropes with balanced trees as input.)

Note also that this is a destructive concatenation, in that the input ropes S1 and S2 no longer exist after the operation is performed. When comparing with array concatenation, one should keep in mind that the latter is usually a non-destructive operation.

### Insert

Definition: Insert(i, S’): insert the string S’ beginning at position i in the string s, to form a new string C1, …, Ci, S’, , …, Cm.

Time complexity: O(log N).

This operation can be done by a Split() and two Concat() operations. The cost is the sum of the three.

### Delete

Definition: Delete(i, j): delete the substring Ci, …, , from s to form a new string C1, …, , , …, Cm.

Time complexity: O(log N).

This operation can be done by two Split() and one Concat() operation. First, split the rope in three, divided by i-th and i+j-th character respectively, which extracts the string to delete in a separate node. Then concatenate the other two nodes.

### Report

Definition: Report(i, j): output the string Ci, …, .

Time complexity: O(j + log N)

To report the string Ci, …, , find the node u that contains Ci and weight(u) >= j, and then traverse T starting at node u. Output Ci, …, by doing an in-order traversal of T starting at node u.

## Comparison with monolithic arrays

Advantages:

Ropes enable much faster insertion and deletion of text than monolithic string arrays, on which operations have time complexity O(n).

Ropes don't require O(n) extra memory when operated upon (arrays need that for copying operations)

Ropes don't require large contiguous memory spaces.

If only nondestructive versions of operations are used, rope is a persistent data structure. For the text editing program example, this leads to an easy support for multiple undo levels.

Disadvantages:

Greater overall space usage when not being operated on, mainly to store parent nodes. There is a trade-off between how much of the total memory is such overhead and how long pieces of data are being processed as strings; note that the strings in example figures above are unrealistically short for modern architectures. The overhead is always O(n), but the constant can be made arbitrarily small.

Increase in time to manage the extra storage

Increased complexity of source code; greater risk for bugs

This table compares the algorithmic characteristics of string and rope implementations, not their "raw speed". Array-based strings have smaller overhead, so (for example) concatenation and split operations are faster on small datasets. However, when array-based strings are used for longer strings, time complexity and memory usage for insertion and deletion of characters become unacceptably large. A rope data structure, on the other hand, has stable performance regardless of data size. Moreover, the space complexity for ropes and arrays are both O(n). In summary, ropes are better suited when the data is large and frequently modified.

References:
[1] Boehm, Hans-J. (December 1995). Ropes: an Alternative to Strings. Software—Practice & Experience. doi:10.1002/spe.4380251203
````

</details>

<details><summary><b>Step 4 — final</b> (1199 words)</summary>

````text
In computer programming, a rope, or cord, is a data structure composed of smaller strings that is used to efficiently store and manipulate longer strings or entire texts. For example, a text editing program may use a rope to represent the text being edited, so that operations such as insertion, deletion, and random access can be done efficiently.[1]

## Description

A rope is a type of binary tree where each leaf (end node) holds a string of manageable size and length (also known as a weight), and each node further up the tree holds the sum of the lengths of all the leaves in its left subtree. A node with two children thus divides the whole string into two parts: the left subtree stores the first part of the string, the right subtree stores the second part of the string, and a node's weight is the length of the first part.

For rope operations, the strings stored in nodes are assumed to be constant immutable objects in the typical nondestructive case, allowing for some copy-on-write behavior. Leaf nodes are usually implemented as basic fixed-length strings with a reference count attached for deallocation when no longer needed, although other garbage collection methods can be used as well.

## Operations

In the following definitions, N is the length of the rope, that is, the weight of the root node. These examples are defined in the Java programming language.

### Collect leaves

Definition: Create a stack S and a list L. Traverse down the left-most spine of the tree until reaching a leaf l', adding each node n to S. Add l' to L. The parent of l' (p) is at the top of the stack. Repeat the procedure for p's right subtree.

### Rebalance

Definition: Collect the set of leaves L and rebuild the tree from the bottom-up.

### Insert

Definition: Insert(i, S’): insert the string S’ beginning at position i in the string s, to form a new string {{math|C1, ..., Ci, S''', Ci + 1, ..., Cm}}.

Time complexity: .

This operation can be done by a Split() and two Concat() operations. The cost is the sum of the three.

### Index

Definition: Index(i): return the character at position i Time complexity:

To retrieve the i-th character, we begin a recursive search from the root node:

For example, to find the character at in Figure 2.1 shown on the right, start at the root node (A), find that 22 is greater than 10 and there is a left child, so go to the left child (B). 9 is less than 10, so subtract 9 from 10 (leaving ) and go to the right child (D). Then because 6 is greater than 1 and there's a left child, go to the left child (G). 2 is greater than 1 and there's a left child, so go to the left child again (J). Finally 2 is greater than 1 but there is no left child, so the character at index 1 of the short string "na" (ie "n") is the answer. (1-based index)

### Concat

Definition: Concat(S1, S2): concatenate two ropes, S1 and S2, into a single rope.

Time complexity: (or time to compute the root weight)

A concatenation can be performed simply by creating a new root node with and , which is constant time. The weight of the parent node is set to the length of the left child S1, which would take time, if the tree is balanced.

As most rope operations require balanced trees, the tree may need to be re-balanced after concatenation.

### Split

Definition: Split (i, S): split the string S into two new strings S1 and S2, and .

Time complexity:

There are two cases that must be dealt with:

The split point is at the end of a string (i.e. after the last character of a leaf node)

The split point is in the middle of a string.

The second case reduces to the first by splitting the string at the split point to create two new leaf nodes, then creating a new node that is the parent of the two component strings.

For example, to split the 22-character rope pictured in Figure 2.3 into two equal component ropes of length 11, query the 12th character to locate the node K at the bottom level. Remove the link between K and G. Go to the parent of G and subtract the weight of K from the weight of D. Travel up the tree and remove any right links to subtrees covering characters past position 11, subtracting the weight of K from their parent nodes (only node D and A, in this case). Finally, build up the newly orphaned nodes K and H by concatenating them and creating a new parent P with weight equal to the length of the left node K.

As most rope operations require balanced trees, the tree may need to be re-balanced after splitting.

### Remove

Definition: Remove(i, j): remove the substring , from s to form a new string .

Time complexity: .

This operation can be done by two Split() and one Concat() operation. First, split the rope in three, divided by i-th and i+j-th character respectively, which extracts the string to remove in a separate node. Then concatenate the other two nodes.

### Report

Definition: Report(i, j): output the string .

Time complexity:

To report the string , find the node u that contains Ci and , and then traverse T starting at node u. Output by doing an in-order traversal of T starting at node u.

## Comparison with monolithic arrays

Advantages:

Ropes enable much faster insertion and deletion of text than monolithic string arrays, on which operations have time complexity O(n).

Ropes do not require O(n) extra memory when operated upon (which arrays need for copying operations).

Ropes do not require large contiguous memory spaces.

If only nondestructive versions of operations are used, rope is a persistent data structure. For the text editing program example, this leads to an easy support for multiple undo levels.

Disadvantages:

Greater overall space use when not being operated on, mainly to store parent nodes. There is a trade-off between how much of the total memory is such overhead and how long pieces of data are being processed as strings. The strings in example figures above are unrealistically short for modern architectures. The overhead is always O(n), but the constant can be made arbitrarily small.

Increase in time to manage the extra storage

Increased complexity of source code; greater risk of bugs

This table compares the algorithmic traits of string and rope implementations, not their raw speed''. Array-based strings have smaller overhead, so (for example) concatenation and split operations are faster on small datasets. However, when array-based strings are used for longer strings, time complexity and memory use for inserting and deleting characters becomes unacceptably large. In contrast, a rope data structure has stable performance regardless of data size. Further, the space complexity for ropes and arrays are both O(n). In summary, ropes are preferable when the data is large and modified often.

References:
[1] Boehm, Hans-J. (December 1995). Ropes: an Alternative to Strings. Software: Practice and Experience. doi:10.1002/spe.4380251203
````

</details>
