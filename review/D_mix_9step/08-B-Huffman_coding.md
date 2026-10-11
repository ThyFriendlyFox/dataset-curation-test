# 8. Huffman coding

`B-Huffman_coding` · [D_mix_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Huffman_coding&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 1223 revisions in history; 39 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | revision_1 | 375 | 0 | 0.07 | enwiki rev 257246 (2001-10-30) |
| 2 | revision_2 | 1356 | 6 | 0.25 | enwiki rev 6365439 (2004-10-05) |
| 3 | revision_3 | 2115 | 0 | 0.47 | enwiki rev 71294823 (2006-08-23) |
| 4 | revision_4 | 3264 | 0 | 0.57 | enwiki rev 373470238 (2010-07-14) |
| 5 | revision_5 | 3336 | 1 | 0.68 | enwiki rev 417660352 (2011-03-07) |
| 6 | revision_6 | 4065 | 6 | 0.77 | enwiki rev 751110319 (2016-11-23) |
| 7 | revision_7 | 3664 | 6 | 0.85 | enwiki rev 786618513 (2017-06-20) |
| 8 | final | 4033 | 14 | 1.00 | enwiki rev 1379018579 (2026-10-07) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Huffman coding
````

</details>

<details><summary><b>Step 1 — revision_1</b> (375 words)</summary>

````text
Huffman coding is an algorithm used for data compression.

The basic idea is borrowed from an older and slightly less efficient method called

Shannon-Fano coding.

The text to be compressed is considered as a string of symbols. Symbols that are likely to be frequent are represented by a short sequence of bits, and symbols that are likely to be rare are represented by a longer sequences of bits.

Huffman coding uses a specific method for choosing the representations for each symbol.

It has been proven that Huffman coding is the most effective compression method of this type, that is, no other mapping of source symbols to strings of bits will produce a smaller output when the actual symbol frequencies agree with those used to create the code.

Huffman coding is optimal when the frequencies of input characters are powers of two.

Arithmetic coding produces slight gains over Huffman coding,

but in practice these gains have not been large enough to offset arithmetic coding's higher computational complexity and patent royalties (as of November 2001, IBM owns patents on the core concepts of arithmetic coding in several jurisdictions).

Huffman works by creating a binary tree of symbols:

Start with as many trees as there are symbols.

While there is more than one tree:

Find the two trees with the smallest total probability.

Combine the trees into one, setting one as the left child and the other as the right.

Now the tree contains all the symbols. A '0' represents following the left child; a '1' represents following the right child.

There are variations.

The frequencies used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

(This variation requires that a frequency table or other hint as to the encoding must be stored with the compressed text; implementations employ various tricks to store these tables efficiently.)

A variation called "adaptive Huffman coding" calculates the frequencies dynamically based on recent actual frequencies in the source string.

Huffman coding today is often used as a "back-end" to some other compression method.

deflation (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by Huffman coding.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (1356 words)</summary>

````text
de:Huffman-Code ja:ハフマン符号 nl:Huffmancodering pl:Kodowanie Huffmana fi:Huffmanin_koodaus

In computer science, Huffman coding is an entropy encoding algorithm used for data compression that finds the optimal system of encoding strings based on the relative frequency of each character. It was developed by David A. Huffman as a PhD student at MIT in 1952, and published in A Method for the Construction of Minimum-Redundancy Codes.

Huffman coding uses a specific method for choosing the representations for each symbol, resulting in a prefix-free code (that is, no bit string of any symbol is a prefix of the bit string of any other symbol) that expresses the most common characters in the shortest way possible. It has been proven that Huffman coding is the most effective compression method of this type: no other mapping of source symbols to strings of bits will produce a smaller output when the actual symbol frequencies agree with those used to create the code.

For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding.

## History

In 1951, David Huffman and his MIT information theory classmates were given the choice of a term paper or a final exam. The professor, Robert M. Fano, assigned a term paper on the problem of finding the most efficient binary code. Huffman, unable to prove any codes were the most efficient, was about to give up and start studying for the final when he hit upon the idea of using a frequency-sorted binary tree, and quickly proved this method the most efficient.

In doing so, the student outdid his professor, who had worked with information theory inventor Claude Shannon to develop a similar code. Huffman avoided the major flaw of Shannon-Fano coding by building the tree from the bottom up instead of from the top down.

## Problem definition

### Informal description

Given. A set of symbols and their costs..

Find. A prefix binary character code (a sets of codewords) with minimum weighted path length..

Note-1. A code wherein each character is represented by a unique binary string (codeword) is called a binary character code..

Note-2. A prefix code is a code having the property that no codeword is a prefix of any other codeword.

### Formalized description

Input.

Alphabet A = {a[1], a[2], ..., a[n]} which is the symbol alphabet of size n.

Set C = {c[1], c[2], ..., c[n]} which is the set of the symbol costs, i.e., c[i] = cost (a[i]), 1 <= i <= n.

Output.

Code H(A,C) = {h[1], h[2], ..., h[n]} which is the set of (binary) codewords, where h[i] is codeword of a[i], 1 <= i <= n.

Goal.

Let S(H) = sum (c[i] * lenght (h[i])) (1 <= i <= n) be weighted path length of code H. Must be: S(H) <= S(T) for any code T(A,C).

### Samples

### Sample-1

Input.

Symbol alphabet A = {a, b, c, d, e, f, g, h, i },

Set of costs C = {10, 15, 5, 15, 20, 5, 15, 30, 5 }.

Output.

Code H(A,C) = {001, 010, 00000, 011, 101, 00001, 100, 11, 0001}.

Sum S(H) = 10*3 + 15*3 + 5*5 + 15*3 + 20*3 + 5*4 + 15*3 + 30*2 + 5*4 = 355.

### Sample-2

Input.

Symbol alphabet A = {a, b, c, d, e, f, g, h, i),

Set of costs C = {3, 21, 2, 1, 8, 34, 1, 13, 5}.

Output.

Code H(A,C) = {000001, 01, 0000001, 00000000, 0001, 1, 00000001, 001, 00001}.

Sum S(H) = 3*6 + 21*2 + 2*7 + 1*8 + 8*4 + 34*1 + 1*8 + 13*3 + 5*5 = 220.

## Basic technique

The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which depends on the number of symbols(N). A node can be either a leaf node or an internal node. Initially, all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node. Internal nodes contain symbol weight, links to two child nodes and the optional link to a parent node. As a common convention, bit '0' represents following the left child and bit '1' represents following the right child. A finished tree has N leaf nodes and N−1 internal nodes.

A fast way to create a Huffman tree is to use the heap data structure, which keeps the nodes in partially sorted order according to a predetermined criterion. In this case, the node with the lowest weight is always kept at the root of the heap for easy access.

Creating the tree:

Start with as many leaves as there are symbols.

Push all leaf nodes into the heap.

While there is more than one node in the heap:

Remove two nodes with the lowest weight from the heap.

Put the two nodes into the tree, noting their location.

If parent links are used, set the children of any internal nodes to point at their parents.

Create a new internal node, using the two nodes as children and their combined weight as the weight.

Push the new node into the heap.

The remaining node is the root node.

## Main properties

The frequencies used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

(This variation requires that a frequency table or other hint as to the encoding must be stored with the compressed text; implementations employ various tricks to store these tables efficiently.)

Huffman coding is optimal when the probability of each input symbol is a negative power of two. Prefix-free codes tend to have slight inefficiency on small alphabets, where probabilities often fall between these optimal points. Expanding the alphabet size by coalescing multiple symbols into "words" before Huffman coding can help a bit. The worst case for Huffman coding can happen when the probability of a symbol exceeds 2-1 making the upper limit of inefficiency unbounded. To prevent this, run-length encoding can be used to preprocess the symbols.

Extreme cases of Huffman codes are connected with Fibonacci and Lucas numbers.

Arithmetic coding produces slight gains over Huffman coding, but in practice these gains have not been large enough to offset arithmetic coding's higher computational complexity and patent royalties (As of November 2001, IBM owns patents on the core concepts of arithmetic coding in several jurisdictions.)

## Variations

### Adaptive Huffman coding

A variation called adaptive Huffman coding calculates the frequencies dynamically based on recent actual frequencies in the source string. This is somewhat related to the LZ family of algorithms.

### Huffman Template algorithm

Most often, the weights used in implementations of Huffman coding represent numeric probabilities, but the algorithm given above does not require this; it requires only a way to order weights and to add them. Huffman Template algorithm enables to use non-numerical weights (costs, frequencies).

### n-ary Huffman coding

The n-ary Huffman algorithm uses the {0, 1, ..., n-1} alphabet to encode message and build an n-ary tree.

### Huffman coding with unequal letter costs

In the standard Huffman coding problem, one is given a set of words and for each word a positive frequency. The goal is to encode each word w as a codeword c(w) over a given alphabet.

Huffman coding with unequal letter costs is the generalization in which the letters of the encoding alphabet may have non-uniform lengths. The goal is to minimize the weighted average codeword length.

## Applications

Arithmetic coding can be viewed as a generalization of Huffman coding.

Although arithmetic coding offers better performance than Huffman coding, Huffman coding is still in wide use because of its simplicity and lack of encumbrance by patents.

Huffman coding today is often used as a "back-end" to some other compression method.

DEFLATE (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by Huffman coding.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (2115 words)</summary>

````text
In computer science and information theory, Huffman coding is an entropy encoding algorithm used for lossless data compression. The term refers to the use of a variable-length code table for encoding a source symbol (such as a character in a file) where the variable-length code table has been derived in a particular way based on the estimated probability of occurrence for each possible value of the source symbol. It was developed by David A. Huffman while he was a Ph.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes." Huffman became a member of the MIT faculty upon graduation and was later the founding member of the Computer Science Department at the University of California, Santa Cruz, now a part of the Baskin School of Engineering.

Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix-free code (that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol) that expresses the most common characters using shorter strings of bits than are used for less common source symbols. Huffman was able to design the most efficient compression method of this type: no other mapping of individual source symbols to unique strings of bits will produce a smaller average output size when the actual symbol frequencies agree with those used to create the code. A method was later found to do this in linear time if input probabilities (also known as weights) are sorted.

For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding, e.g., ASCII coding. Huffman coding is such a widespread method for creating prefix-free codes that the term "Huffman code" is widely used as a synonym for "prefix-free code" even when such a code is not produced by Huffman's algorithm.

Although Huffman coding is optimal for a symbol-by-symbol coding with a known input probability distribution, its optimality can sometimes accidentally be over-stated. For example, arithmetic coding and LZW coding often have better compression capability. Both these methods can combine an arbitrary number of symbols for more efficient coding, and generally adapt to the actual input statistics, the latter of which is useful when input probabilities are not precisely known.

## History

In 1951, David Huffman and his MIT information theory classmates were given the choice of a term paper or a final exam. The professor, Robert M. Fano, assigned a term paper on the problem of finding the most efficient binary code. Huffman, unable to prove any codes were the most efficient, was about to give up and start studying for the final when he hit upon the idea of using a frequency-sorted binary tree, and quickly proved this method the most efficient.

In doing so, the student outdid his professor, who had worked with information theory inventor Claude Shannon to develop a similar code. Huffman avoided the major flaw of the suboptimal Shannon-Fano coding by building the tree from the bottom up instead of from the top down.

## Problem definition

### Informal description

Given. A set of symbols and their weights (usually probabilities).

Find. A prefix-free binary code (a set of codewords) with minimum expected codeword length (equivalently, a tree with minimum weighted path length).

### Formalized description

Input.

Alphabet A = \left\{a_{1},a_{2},\cdots,a_{n}\right\} , which is the symbol alphabet of size n .

Set W = \left\{w_{1},w_{2},\cdots,w_{n}\right\} , which is the set of the (positive) symbol weights (usually probabilities), i.e. w_{i} = \mathrm{weight}\left(a_{i}\right), 1\leq i \leq n .

Output.

Code C\left(A,W\right) = \left\{c_{1},c_{2},\cdots,c_{n}\right\} , which is the set of (binary) codewords, where c_{i} is the codeword for a_{i}, 1 \leq i \leq n .

Goal.

Let L\left(C\right) = \sum_{i=1}^{n}{w_{i}\times\mathrm{length}\left(c_{i}\right)} be the weighted path length of code C . Condition: L\left(C\right) \leq L\left(T\right) for any code T\left(A,W\right) .

### Samples

### Sample-1

The sum of the probability budgets across all symbols is always less than or equal to one. In this case, the sum is strictly equal to one; as a result, the code in this example is termed a complete code.

Note that, in general, a Huffman code need not be unique, but it is always one of the codes minimizing L(C) .

## Basic technique

The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which depends on the number of symbols(N). A node can be either a leaf node or an internal node. Initially, all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node. Internal nodes contain symbol weight, links to two child nodes and the optional link to a parent node. As a common convention, bit '0' represents following the left child and bit '1' represents following the right child. A finished tree has N leaf nodes and N−1 internal nodes.

A linear-time method to create a Huffman tree is to use two queues, the first one containing the initial weights (along with pointers to the associated leaves), and combined weights (along with pointers to the trees) being put in the back of the second queue. This assures that the lowest weight is always kept at the front of one of the two queues.

Creating the tree:

Start with as many leaves as there are symbols.

Queue all leaf nodes into the first queue (in order).

While there is more than one node in the queues:

Remove two nodes with the lowest weight from the queues.

Create a new internal node, with the two just-removed nodes as children (either node can be either child) and the sum of their weights as the new weight.

Update the parent links in the two just-removed nodes to point to the just-created parent node.

Queue the new node into the second queue.

The remaining node is the root node; the tree has now been generated.

It is generally beneficial to minimize the variance of codeword length. For example, a communication buffer receiving Huffman-encoded data may need to be larger to deal with especially long symbols if the tree is especially unbalanced. To minimize variance, simply break ties between queues by choosing the item in the first queue. This modification will retain the mathematical optimality of the Huffman coding while both minimizing variance and minimizing the length of the longest character code.

## Main properties

The frequencies used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

(This variation requires that a frequency table or other hint as to the encoding must be stored with the compressed text; implementations employ various tricks to store

tables efficiently.)

Huffman coding is optimal when the probability of each input symbol is a negative power of two. Prefix-free codes tend to have slight inefficiency on small alphabets, where probabilities often fall between these optimal points. "Blocking", or expanding the alphabet size by coalescing multiple symbols into "words" of fixed or variable length before Huffman coding, usually helps, especially when adjacent symbols are correlated (as in the case of natural language text). The worst case for Huffman coding can happen when the probability of a symbol exceeds 2-1 = 0.5, making the upper limit of inefficiency unbounded. These situations often respond well to a form of blocking called run-length encoding.

Arithmetic coding produces slight gains over Huffman coding, but in practice these gains have seldom been large enough to offset arithmetic coding's higher computational complexity and patent royalties. (As of July 2006, IBM owns patents on many methods of arithmetic coding in several jurisdictions; see US patents on arithmetic coding.)

## Variations

Many variations of Huffman coding exist, some of which use a Huffman-like algorithm, and others of which find optimal prefix codes (while, for example, putting different restrictions on the output). Note that, in the latter case, the method need not be Huffman-like, and, indeed, need not even be polynomial time. An exhaustive list of papers on Huffman coding on its variations is given by "Code and Parse Trees for Lossless Source Encoding".

### n-ary Huffman coding

The n-ary Huffman algorithm uses the {0, 1, ..., n − 1} alphabet to encode message and build an n-ary tree. This approach was considered by Huffman in his original paper.

### Adaptive Huffman coding

A variation called adaptive Huffman coding calculates the frequencies dynamically based on recent actual frequencies in the source string. This is somewhat related to the LZ family of algorithms.

### Huffman template algorithm

Most often, the weights used in implementations of Huffman coding represent numeric probabilities, but the algorithm given above does not require this; it requires only a way to order weights and to add them. The Huffman template algorithm enables one to use any kind of weights (costs, frequencies, pairs of weights, non-numerical weights) and one of many combining methods (not just addition). Such algorithms can solve other minimization problems, such as minimizing \max_i\left[w_{i}+\mathrm{length}\left(c_{i}\right)\right] , a problem first applied to circuit design.

### Length-limited Huffman coding

Length-limited Huffman coding is a variant where the goal is still to achieve a minimum weighted path length, but there is an additional restriction that the length of each codeword must be less than a given constant. No algorithm is known to solve this in the same manner or with the same efficiency as conventional Huffman coding.

### Huffman coding with unequal letter costs

In the standard Huffman coding problem, it is assumed that each symbol in the set that the code words are constructed from has an equal cost to transmit: a code word whose length is N digits will always have a cost of N, no matter how many of those digits are 0s, how many are 1s, etc. When working under this assumption, minimizing the total cost of the message and minimizing the total number of digits are the same thing.

Huffman coding with unequal letter costs is the generalization in which this assumption is no longer assumed true: the letters of the encoding alphabet may have non-uniform lengths, due to characteristics of the transmission medium. An example is the encoding alphabet of Morse code, where a 'dash' takes longer to send than a 'dot', and therefore the cost of a dash in transmission time is higher. The goal is still to minimize the weighted average codeword length, but it is no longer sufficient just to minimize the number of symbols used by the message. No algorithm is known to solve this in the same manner or with the same efficiency as conventional Huffman coding.

### Optimal alphabetic binary trees (Hu-Tucker coding and Huffman-Shannon-Fano coding)

In the standard Huffman coding problem, it is assumed that any codeword can correspond to any input symbol. In the alphabetic version, the alphabetic order of inputs and outputs must be identical. Thus, for example, A = \left\{a,b,c\right\} could not be assigned code H\left(A,C\right) = \left\{00,1,01\right\} , but instead should be assigned either H\left(A,C\right) =\left\{00,01,1\right\} or H\left(A,C\right) = \left\{0,10,11\right\} . This is also known as the Hu-Tucker problem, after the authors of the paper presenting the first linearithmic solution to this optimal binary alphabetic problem, which has some similarities to Huffman algorithm, but is not a variation of this algorithm. These optimal alphabetic binary trees are often used as binary search trees. If weights corresponding to the alphabetically ordered inputs are in numerical order, the Huffman code has the same lengths as the optimal alphabetic code, which can be found from calculating these lengths. This is sometimes called Huffman-Shannon-Fano coding, since it is optimal like Huffman coding, but alphabetic in weight probability, like Shannon-Fano coding. The Huffman-Shannon-Fano code corresponding to the example is \{000,001,01,10,11\} , which, having the same codeword lengths as the original solution, is also optimal.

## Applications

Arithmetic coding can be viewed as a generalization of Huffman coding; indeed, in practice arithmetic coding is often preceded by Huffman coding, as it is easier to find an arithmetic code for a binary input than for a nonbinary input. Also, although arithmetic coding offers better compression performance than Huffman coding, Huffman coding is still in wide use because of its simplicity, high speed and lack of encumbrance by patents.

Huffman coding today is often used as a "back-end" to some other compression method.

DEFLATE (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by Huffman coding.
````

</details>

<details><summary><b>Step 4 — revision_4</b> (3264 words)</summary>

````text
In computer science and information theory, Huffman coding is an entropy encoding algorithm used for lossless data compression. The term refers to the use of a variable-length code table for encoding a source symbol (such as a character in a file) where the variable-length code table has been derived in a particular way based on the estimated probability of occurrence for each possible value of the source symbol. It was developed by David A. Huffman while he was a Ph.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".

Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code (sometimes called "prefix-free codes", that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol) that expresses the most common source symbols using shorter strings of bits than are used for less common source symbols. Huffman was able to design the most efficient compression method of this type: no other mapping of individual source symbols to unique strings of bits will produce a smaller average output size when the actual symbol frequencies agree with those used to create the code. A method was later found to design a Huffman code in linear time if input probabilities (also known as weights) are sorted.

For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding, e.g., ASCII coding. Huffman coding is such a widespread method for creating prefix codes that the term "Huffman code" is widely used as a synonym for "prefix code" even when such a code is not produced by Huffman's algorithm.

Although Huffman's original algorithm is optimal for a symbol-by-symbol coding (i.e. a stream of unrelated symbols) with a known input probability distribution, it is not optimal when the symbol-by-symbol restriction is dropped, or when the probability mass functions are unknown, not identically distributed, or not independent (e.g., "cat" is more common than "cta"). Other methods such as arithmetic coding and LZW coding often have better compression capability: both of these methods can combine an arbitrary number of symbols for more efficient coding, and generally adapt to the actual input statistics, the latter of which is useful when input probabilities are not precisely known or vary significantly within the stream. However, the limitations of Huffman coding should not be overstated; it can be used adaptively, accommodating unknown, changing, or context-dependent probabilities. In the case of known independent and identically-distributed random variables, combining symbols together reduces inefficiency in a way that approaches optimality as the number of symbols combined increases.

## History

In 1951, David A. Huffman and his MIT information theory classmates were given the choice of a term paper or a final exam. The professor, Robert M. Fano, assigned a term paper on the problem of finding the most efficient binary code. Huffman, unable to prove any codes were the most efficient, was about to give up and start studying for the final when he hit upon the idea of using a frequency-sorted binary tree and quickly proved this method the most efficient.

In doing so, the student outdid his professor, who had worked with information theory inventor Claude Shannon to develop a similar code. Huffman avoided the major flaw of the suboptimal Shannon-Fano coding by building the tree from the bottom up instead of from the top down.

## Problem definition

### Informal description

Given A set of symbols and their weights (usually proportional to probabilities).

Find A prefix-free binary code (a set of codewords) with minimum expected codeword length (equivalently, a tree with minimum weighted path length from the root).

### Formalized description

Input.

Alphabet A = \left\{a_{1},a_{2},\cdots,a_{n}\right\} , which is the symbol alphabet of size n .

Set W = \left\{w_{1},w_{2},\cdots,w_{n}\right\} , which is the set of the (positive) symbol weights (usually proportional to probabilities), i.e. w_{i} = \mathrm{weight}\left(a_{i}\right), 1\leq i \leq n .

Output.

Code C \left(A,W\right) = \left\{c_{1},c_{2},\cdots,c_{n}\right\} , which is the set of (binary) codewords, where c_{i} is the codeword for a_{i}, 1 \leq i \leq n .

Goal.

Let L\left(C\right) = \sum_{i=1}^{n}{w_{i}\times\mathrm{length}\left(c_{i}\right)} be the weighted path length of code C . Condition: L\left(C\right) \leq L\left(T\right) for any code T\left(A,W\right) .

### Samples

For any code that is biunique, meaning that the code is uniquely decodeable, the sum of the probability budgets across all symbols is always less than or equal to one. In this example, the sum is strictly equal to one; as a result, the code is termed a complete code. If this is not the case, you can always derive an equivalent code by adding extra symbols (with associated null probabilities), to make the code complete while keeping it biunique.

As defined by Shannon (1948), the information content h (in bits) of each symbol ai with non-null probability is

h(a_i) = \log_2{1 \over w_i}.

The entropy H (in bits) is the weighted sum, across all symbols ai with non-zero probability wi, of the information content of each symbol:

H(A) = \sum_{w_i > 0} w_i h(a_i) = \sum_{w_i > 0} w_i \log_2{1 \over w_i} = - \sum_{w_i > 0} w_i \log_2{w_i}.

(Note: A symbol with zero probability has zero contribution to the entropy. When w = 0, w \log_2 (1/w) = 0 \cdot \infty is an indefinite form; so by L'Hôpital's rule:

\lim_{w \to 0^+} \frac{\log_2 \frac{1}{w}}{\frac{1}{w}} = \lim_{w \to 0^+} \frac{-\frac{1}{w \ln 2}}{-\frac{1}{w^2}} = \lim_{w \to 0^+} \frac{w}{\ln 2} = 0 .

For simplicity, symbols with zero probability are left out of the formula above.)

As a consequence of Shannon's source coding theorem, the entropy is a measure of the smallest codeword length that is theoretically possible for the given alphabet with associated weights. In this example, the weighted average codeword length is 2.25 bits per symbol, only slightly larger than the calculated entropy of 2.205 bits per symbol. So not only is this code optimal in the sense that no other feasible code performs better, but it is very close to the theoretical limit established by Shannon.

Note that, in general, a Huffman code need not be unique, but it is always one of the codes minimizing L(C) .

## Basic technique

The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which depends on the number of symbols, n . A node can be either a leaf node or an internal node. Initially, all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node. Internal nodes contain symbol weight, links to two child nodes and the optional link to a parent node. As a common convention, bit '0' represents following the left child and bit '1' represents following the right child. A finished tree has up to n leaf nodes and n-1 internal nodes. A Huffman tree that omits unused symbols produces the most optimal code lengths.

The process essentially begins with the leaf nodes containing the probabilities of the symbol they represent, then a new node whose children are the 2 nodes with smallest probability is created, such that the new node's probability is equal to the sum of the children's probability. With the previous 2 nodes merged into one node (thus not considering them anymore), and with the new node being now considered, the procedure is repeated until only one node remains, the Huffman tree.

The simplest construction algorithm uses a priority queue where the node with lowest probability is given highest priority:

Create a leaf node for each symbol and add it to the priority queue.

While there is more than one node in the queue:

Remove the two nodes of highest priority (lowest probability) from the queue

Create a new internal node with these two nodes as children and with probability equal to the sum of the two nodes' probabilities.

Add the new node to the queue.

The remaining node is the root node and the tree is complete.

Since efficient priority queue data structures require O(log n) time per insertion, and a tree with n leaves has 2n−1 nodes, this algorithm operates in O(n log n) time.

If the symbols are sorted by probability, there is a linear-time (O(n)) method to create a Huffman tree using two queues, the first one containing the initial weights (along with pointers to the associated leaves), and combined weights (along with pointers to the trees) being put in the back of the second queue. This assures that the lowest weight is always kept at the front of one of the two queues:

Start with as many leaves as there are symbols.

Enqueue all leaf nodes into the first queue (by probability in increasing order so that the least likely item is in the head of the queue).

While there is more than one node in the queues:

Dequeue the two nodes with the lowest weight by examining the fronts of both queues.

Create a new internal node, with the two just-removed nodes as children (either node can be either child) and the sum of their weights as the new weight.

Enqueue the new node into the rear of the second queue.

The remaining node is the root node; the tree has now been generated.

It is generally beneficial to minimize the variance of codeword length. For example, a communication buffer receiving Huffman-encoded data may need to be larger to deal with especially long symbols if the tree is especially unbalanced. To minimize variance, simply break ties between queues by choosing the item in the first queue. This modification will retain the mathematical optimality of the Huffman coding while both minimizing variance and minimizing the length of the longest character code.

Here's an example using the French subject string "j'aime aller sur le bord de l'eau les jeudis ou les jours impairs":

## Main properties

The probabilities used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

(This variation requires that a frequency table or other hint as to the encoding must be stored with the compressed text; implementations employ various tricks to store tables efficiently.)

Huffman coding is optimal when the probability of each input symbol is a negative power of two. Prefix codes tend to have inefficiency on small alphabets, where probabilities often fall between these optimal points. "Blocking", or expanding the alphabet size by grouping multiple symbols into "words" of fixed or variable-length before Huffman coding helps both to reduce that inefficiency and to take advantage of statistical dependencies between input symbols within the group (as in the case of natural language text). The worst case for Huffman coding can happen when the probability of a symbol exceeds 2−1 = 0.5, making the upper limit of inefficiency unbounded. These situations often respond well to a form of blocking called run-length encoding; for the simple case of Bernoulli processes, Golomb coding is a provably optimal run-length code.

Arithmetic coding produces some gains over Huffman coding, although arithmetic coding has higher computational complexity. Also, arithmetic coding was historically a subject of some concern over patent issues. However, as of mid-2010, various well-known effective techniques for arithmetic coding have passed into the public domain as the early patents have expired.

## Variations

Many variations of Huffman coding exist, some of which use a Huffman-like algorithm, and others of which find optimal prefix codes (while, for example, putting different restrictions on the output). Note that, in the latter case, the method need not be Huffman-like, and, indeed, need not even be polynomial time. An exhaustive list of papers on Huffman coding and its variations is given by "Code and Parse Trees for Lossless Source Encoding".

### n-ary Huffman coding

The n-ary Huffman algorithm uses the {0, 1, ... , n − 1} alphabet to encode message and build an n-ary tree. This approach was considered by Huffman in his original paper. The same algorithm applies as for binary (n equals 2) codes, except that the n least probable symbols are taken together, instead of just the 2 least probable. Note that for n greater than 2, not all sets of source words can properly form an n-ary tree for Huffman coding. In this case, additional 0-probability place holders must be added. This is because the tree must form an n to 1 contractor; for binary coding, this is a 2 to 1 contractor, and any sized set can form such a contractor. If the number of source words is congruent to 1 modulo n-1, then the set of source words will form a proper Huffman tree.

### Adaptive Huffman coding

A variation called adaptive Huffman coding involves calculating the probabilities dynamically based on recent actual frequencies in the sequence of source symbols, and changing the coding tree structure to match the updated probability estimates.

### Huffman template algorithm

Most often, the weights used in implementations of Huffman coding represent numeric probabilities, but the algorithm given above does not require this; it requires only a way to order weights and to add them. The Huffman template algorithm enables one to use any kind of weights (costs, frequencies, pairs of weights, non-numerical weights) and one of many combining methods (not just addition). Such algorithms can solve other minimization problems, such as minimizing \max_i\left[w_{i}+\mathrm{length}\left(c_{i}\right)\right] , a problem first applied to circuit design .

### Length-limited Huffman coding

Length-limited Huffman coding is a variant where the goal is still to achieve a minimum weighted path length, but there is an additional restriction that the length of each codeword must be less than a given constant. The package-merge algorithm solves this problem with a simple greedy approach very similar to that used by Huffman's algorithm. Its time complexity is O(nL) , where L is the maximum length of a codeword. No algorithm is known to solve this problem in linear or linearithmic time, unlike the presorted and unsorted conventional Huffman problems, respectively.

### Huffman coding with unequal letter costs

In the standard Huffman coding problem, it is assumed that each symbol in the set that the code words are constructed from has an equal cost to transmit: a code word whose length is N digits will always have a cost of N, no matter how many of those digits are 0s, how many are 1s, etc. When working under this assumption, minimizing the total cost of the message and minimizing the total number of digits are the same thing.

Huffman coding with unequal letter costs is the generalization in which this assumption is no longer assumed true: the letters of the encoding alphabet may have non-uniform lengths, due to characteristics of the transmission medium. An example is the encoding alphabet of Morse code, where a 'dash' takes longer to send than a 'dot', and therefore the cost of a dash in transmission time is higher. The goal is still to minimize the weighted average codeword length, but it is no longer sufficient just to minimize the number of symbols used by the message. No algorithm is known to solve this in the same manner or with the same efficiency as conventional Huffman coding.

### Optimal alphabetic binary trees (Hu-Tucker coding)

In the standard Huffman coding problem, it is assumed that any codeword can correspond to any input symbol. In the alphabetic version, the alphabetic order of inputs and outputs must be identical. Thus, for example, A = \left\{a,b,c\right\} could not be assigned code H\left(A,C\right) = \left\{00,1,01\right\} , but instead should be assigned either H\left(A,C\right) =\left\{00,01,1\right\} or H\left(A,C\right) = \left\{0,10,11\right\} . This is also known as the Hu-Tucker problem, after the authors of the paper presenting the first linearithmic solution to this optimal binary alphabetic problem, which has some similarities to Huffman algorithm, but is not a variation of this algorithm. These optimal alphabetic binary trees are often used as binary search trees.

### The canonical Huffman code

If weights corresponding to the alphabetically ordered inputs are in numerical order, the Huffman code has the same lengths as the optimal alphabetic code, which can be found from calculating these lengths, rendering Hu-Tucker coding unnecessary. The code resulting from numerically (re-)ordered input is sometimes called the canonical Huffman code and is often the code used in practice, due to ease of encoding/decoding. The technique for finding this code is sometimes called Huffman-Shannon-Fano coding, since it is optimal like Huffman coding, but alphabetic in weight probability, like Shannon-Fano coding. The Huffman-Shannon-Fano code corresponding to the example is \{000,001,01,10,11\} , which, having the same codeword lengths as the original solution, is also optimal.

### Model reconstruction

Decompression generally requires transmission of information in order to reconstruct the compression model (methods such as adaptive Huffman do not, although they typically produce less than optimal code lengths). Originally, symbol frequencies were passed along to the decompressor, but this method is very inefficient, as it can produce an unacceptable level of overhead. The most common technique utilizes canonical Huffman encoding, which only requires Bn bits of information (where B is the number of bits per symbol and n is the size of the symbol's alphabet). Other methods, such as the "direct transmission" of the Huffman tree, produce variable-length encoding of the model which can reduce the overhead to just a few bytes, in some cases.

Because the compressed data can include unused "trailing bits", the decompressor must be able to determine when to stop producing output. This can be accomplished by either transmitting the length of the decompressed data along with the compression model or by defining a special code symbol to signify the end of input (the latter method can adversely affect code length optimality, however).

## Applications

Arithmetic coding can be viewed as a generalization of Huffman coding; indeed, in practice arithmetic coding is often preceded by Huffman coding, as it is easier to find an arithmetic code for a binary input than for a nonbinary input. Also, although arithmetic coding offers better compression performance than Huffman coding, Huffman coding is still in wide use because of its simplicity and high speed.

Huffman coding today is often used as a "back-end" to some other compression method.

DEFLATE (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by Huffman coding (or variable-length prefix-free codes with a similar structure, although perhaps not necessarily designed by using Huffman's algorithm).

It is during the computing era, when we recognized that we can actually save memory space by representing frequently used characters with less bits. Interestingly enough, the Huffman Coding idea was actually used to design Indo-Aryan languages like Sanskrit and Gujarati. This fact reveals the algorithmic nature of mind of the civilization that was behind the creation of the Indo-Aryan languages. The creators of these languages must have studied how certain sounds appear frequently before writing the alphabets of the language. It was obvious to them that vowels were frequented more than constants as seen by their alphabetic design. Not only do the alphabets of the language use short symbols for vowels but they are separated from the main alphabet set in a special way and are called matras. The matras qualify vowel sounds of a consonant. Historically, the Huffman Coding idea was actually applied in the design of Indo-Aryan languages by the ancient civilization.
````

</details>

<details><summary><b>Step 5 — revision_5</b> (3336 words)</summary>

````text
In computer science and information theory, Huffman coding is an entropy encoding algorithm used for lossless data compression. The term refers to the use of a variable-length code table for encoding a source symbol (such as a character in a file) where the variable-length code table has been derived in a particular way based on the estimated probability of occurrence for each possible value of the source symbol. It was developed by David A. Huffman while he was a Ph.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".

Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code (sometimes called "prefix-free codes", that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol) that expresses the most common source symbols using shorter strings of bits than are used for less common source symbols. Huffman was able to design the most efficient compression method of this type: no other mapping of individual source symbols to unique strings of bits will produce a smaller average output size when the actual symbol frequencies agree with those used to create the code. A method was later found to design a Huffman code in linear time if input probabilities (also known as weights) are sorted.

For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding, e.g., ASCII coding. Huffman coding is such a widespread method for creating prefix codes that the term "Huffman code" is widely used as a synonym for "prefix code" even when such a code is not produced by Huffman's algorithm.

Although Huffman's original algorithm is optimal for a symbol-by-symbol coding (i.e. a stream of unrelated symbols) with a known input probability distribution, it is not optimal when the symbol-by-symbol restriction is dropped, or when the probability mass functions are unknown, not identically distributed, or not independent (e.g., "cat" is more common than "cta"). Other methods such as arithmetic coding and LZW coding often have better compression capability: both of these methods can combine an arbitrary number of symbols for more efficient coding, and generally adapt to the actual input statistics, the latter of which is useful when input probabilities are not precisely known or vary significantly within the stream. However, the limitations of Huffman coding should not be overstated; it can be used adaptively, accommodating unknown, changing, or context-dependent probabilities. In the case of known independent and identically-distributed random variables, combining symbols together reduces inefficiency in a way that approaches optimality as the number of symbols combined increases.

## History

In 1951, David A. Huffman and his MIT information theory classmates were given the choice of a term paper or a final exam. The professor, Robert M. Fano, assigned a term paper on the problem of finding the most efficient binary code. Huffman, unable to prove any codes were the most efficient, was about to give up and start studying for the final when he hit upon the idea of using a frequency-sorted binary tree and quickly proved this method the most efficient.[1]

In doing so, the student outdid his professor, who had worked with information theory inventor Claude Shannon to develop a similar code. Huffman avoided the major flaw of the suboptimal Shannon-Fano coding by building the tree from the bottom up instead of from the top down.

## Problem definition

### Informal description

Given A set of symbols and their weights (usually proportional to probabilities).

Find A prefix-free binary code (a set of codewords) with minimum expected codeword length (equivalently, a tree with minimum weighted path length from the root).

### Formalized description

Input.

Alphabet A = \left\{a_{1},a_{2},\cdots,a_{n}\right\} , which is the symbol alphabet of size n .

Set W = \left\{w_{1},w_{2},\cdots,w_{n}\right\} , which is the set of the (positive) symbol weights (usually proportional to probabilities), i.e. w_{i} = \mathrm{weight}\left(a_{i}\right), 1\leq i \leq n .

Output.

Code C \left(A,W\right) = \left\{c_{1},c_{2},\cdots,c_{n}\right\} , which is the set of (binary) codewords, where c_{i} is the codeword for a_{i}, 1 \leq i \leq n .

Goal.

Let L\left(C\right) = \sum_{i=1}^{n}{w_{i}\times\mathrm{length}\left(c_{i}\right)} be the weighted path length of code C . Condition: L\left(C\right) \leq L\left(T\right) for any code T\left(A,W\right) .

### Samples

For any code that is biunique, meaning that the code is uniquely decodeable, the sum of the probability budgets across all symbols is always less than or equal to one. In this example, the sum is strictly equal to one; as a result, the code is termed a complete code. If this is not the case, you can always derive an equivalent code by adding extra symbols (with associated null probabilities), to make the code complete while keeping it biunique.

As defined by Shannon (1948), the information content h (in bits) of each symbol ai with non-null probability is

h(a_i) = \log_2{1 \over w_i}.

The entropy H (in bits) is the weighted sum, across all symbols ai with non-zero probability wi, of the information content of each symbol:

H(A) = \sum_{w_i > 0} w_i h(a_i) = \sum_{w_i > 0} w_i \log_2{1 \over w_i} = - \sum_{w_i > 0} w_i \log_2{w_i}.

(Note: A symbol with zero probability has zero contribution to the entropy, since \lim_{w \to 0^+} w \log_2 w = 0 So for simplicity, symbols with zero probability can be left out of the formula above.)

As a consequence of Shannon's source coding theorem, the entropy is a measure of the smallest codeword length that is theoretically possible for the given alphabet with associated weights. In this example, the weighted average codeword length is 2.25 bits per symbol, only slightly larger than the calculated entropy of 2.205 bits per symbol. So not only is this code optimal in the sense that no other feasible code performs better, but it is very close to the theoretical limit established by Shannon.

Note that, in general, a Huffman code need not be unique, but it is always one of the codes minimizing L(C) .

## Basic technique

### Compression

The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which depends on the number of symbols, n . A node can be either a leaf node or an internal node. Initially, all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node. Internal nodes contain symbol weight, links to two child nodes and the optional link to a parent node. As a common convention, bit '0' represents following the left child and bit '1' represents following the right child. A finished tree has up to n leaf nodes and n-1 internal nodes. A Huffman tree that omits unused symbols produces the most optimal code lengths.

The process essentially begins with the leaf nodes containing the probabilities of the symbol they represent, then a new node whose children are the 2 nodes with smallest probability is created, such that the new node's probability is equal to the sum of the children's probability. With the previous 2 nodes merged into one node (thus not considering them anymore), and with the new node being now considered, the procedure is repeated until only one node remains, the Huffman tree.

The simplest construction algorithm uses a priority queue where the node with lowest probability is given highest priority:

Create a leaf node for each symbol and add it to the priority queue.

While there is more than one node in the queue:

Remove the two nodes of highest priority (lowest probability) from the queue

Create a new internal node with these two nodes as children and with probability equal to the sum of the two nodes' probabilities.

Add the new node to the queue.

The remaining node is the root node and the tree is complete.

Since efficient priority queue data structures require O(log n) time per insertion, and a tree with n leaves has 2n−1 nodes, this algorithm operates in O(n log n) time.

If the symbols are sorted by probability, there is a linear-time (O(n)) method to create a Huffman tree using two queues, the first one containing the initial weights (along with pointers to the associated leaves), and combined weights (along with pointers to the trees) being put in the back of the second queue. This assures that the lowest weight is always kept at the front of one of the two queues:

Start with as many leaves as there are symbols.

Enqueue all leaf nodes into the first queue (by probability in increasing order so that the least likely item is in the head of the queue).

While there is more than one node in the queues:

Dequeue the two nodes with the lowest weight by examining the fronts of both queues.

Create a new internal node, with the two just-removed nodes as children (either node can be either child) and the sum of their weights as the new weight.

Enqueue the new node into the rear of the second queue.

The remaining node is the root node; the tree has now been generated.

It is generally beneficial to minimize the variance of codeword length. For example, a communication buffer receiving Huffman-encoded data may need to be larger to deal with especially long symbols if the tree is especially unbalanced. To minimize variance, simply break ties between queues by choosing the item in the first queue. This modification will retain the mathematical optimality of the Huffman coding while both minimizing variance and minimizing the length of the longest character code.

Here's an example using the French subject string "j'aime aller sur le bord de l'eau les jeudis ou les jours impairs":

### Decompression

Generally speaking, the process of decompression is simply a matter of translating the stream of prefix codes to individual byte values, usually by traversing the Huffman tree node by node as each bit is read from the input stream (reaching a leaf node necessarily terminates the search for that particular byte value). Before this can take place, however, the Huffman tree must be somehow reconstructed. In the simplest case, where character frequencies are fairly predictable, the tree can be preconstructed (and even statistically adjusted on each compression cycle) and thus reused every time, at the expense of at least some measure of compression efficiency. Otherwise, the information to reconstruct the tree must be sent a priori. A naive approach might be to prepend the frequency count of each character to the compression stream. Unfortunately, the overhead in such a case could amount to several kilobytes, so this method has little practical use. If the data is compressed using canonical encoding, the compression model can be precisely reconstructed with just B2^B bits of information (where B is the number of bits per symbol). Another method is to simply prepend the Huffman tree, bit by bit, to the output stream. For example, assuming that the value of 0 represents a parent node and 1 a leaf node, whenever the latter is encountered the tree building routine simply reads the next 8 bits to determine the character value of that particular leaf. The process continues recursively until the last leaf node is reached; at that point, the Huffman tree will thus be faithfully reconstructed. The overhead using such a method ranges from roughly 2 to 320 bytes (assuming an 8-bit alphabet). Many other techniques are possible as well. In any case, since the compressed data can include unused "trailing bits" the decompressor must be able to determine when to stop producing output. This can be accomplished by either transmitting the length of the decompressed data along with the compression model or by defining a special code symbol to signify the end of input (the latter method can adversely affect code length optimality, however).

## Main properties

The probabilities used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

(This variation requires that a frequency table or other hint as to the encoding must be stored with the compressed text; implementations employ various tricks to store tables efficiently.)

Huffman coding is optimal when the probability of each input symbol is a negative power of two. Prefix codes tend to have inefficiency on small alphabets, where probabilities often fall between these optimal points. "Blocking", or expanding the alphabet size by grouping multiple symbols into "words" of fixed or variable-length before Huffman coding helps both to reduce that inefficiency and to take advantage of statistical dependencies between input symbols within the group (as in the case of natural language text). The worst case for Huffman coding can happen when the probability of a symbol exceeds 2−1 = 0.5, making the upper limit of inefficiency unbounded. These situations often respond well to a form of blocking called run-length encoding; for the simple case of Bernoulli processes, Golomb coding is a provably optimal run-length code.

Arithmetic coding produces some gains over Huffman coding, although arithmetic coding has higher computational complexity. Also, arithmetic coding was historically a subject of some concern over patent issues. However, as of mid-2010, various well-known effective techniques for arithmetic coding have passed into the public domain as the early patents have expired.

## Variations

Many variations of Huffman coding exist, some of which use a Huffman-like algorithm, and others of which find optimal prefix codes (while, for example, putting different restrictions on the output). Note that, in the latter case, the method need not be Huffman-like, and, indeed, need not even be polynomial time. An exhaustive list of papers on Huffman coding and its variations is given by "Code and Parse Trees for Lossless Source Encoding".

### n-ary Huffman coding

The n-ary Huffman algorithm uses the {0, 1, ... , n − 1} alphabet to encode message and build an n-ary tree. This approach was considered by Huffman in his original paper. The same algorithm applies as for binary (n equals 2) codes, except that the n least probable symbols are taken together, instead of just the 2 least probable. Note that for n greater than 2, not all sets of source words can properly form an n-ary tree for Huffman coding. In this case, additional 0-probability place holders must be added. This is because the tree must form an n to 1 contractor; for binary coding, this is a 2 to 1 contractor, and any sized set can form such a contractor. If the number of source words is congruent to 1 modulo n-1, then the set of source words will form a proper Huffman tree.

### Adaptive Huffman coding

A variation called adaptive Huffman coding involves calculating the probabilities dynamically based on recent actual frequencies in the sequence of source symbols, and changing the coding tree structure to match the updated probability estimates.

### Huffman template algorithm

Most often, the weights used in implementations of Huffman coding represent numeric probabilities, but the algorithm given above does not require this; it requires only a way to order weights and to add them. The Huffman template algorithm enables one to use any kind of weights (costs, frequencies, pairs of weights, non-numerical weights) and one of many combining methods (not just addition). Such algorithms can solve other minimization problems, such as minimizing \max_i\left[w_{i}+\mathrm{length}\left(c_{i}\right)\right] , a problem first applied to circuit design .

### Length-limited Huffman coding

Length-limited Huffman coding is a variant where the goal is still to achieve a minimum weighted path length, but there is an additional restriction that the length of each codeword must be less than a given constant. The package-merge algorithm solves this problem with a simple greedy approach very similar to that used by Huffman's algorithm. Its time complexity is O(nL) , where L is the maximum length of a codeword. No algorithm is known to solve this problem in linear or linearithmic time, unlike the presorted and unsorted conventional Huffman problems, respectively.

### Huffman coding with unequal letter costs

In the standard Huffman coding problem, it is assumed that each symbol in the set that the code words are constructed from has an equal cost to transmit: a code word whose length is N digits will always have a cost of N, no matter how many of those digits are 0s, how many are 1s, etc. When working under this assumption, minimizing the total cost of the message and minimizing the total number of digits are the same thing.

Huffman coding with unequal letter costs is the generalization in which this assumption is no longer assumed true: the letters of the encoding alphabet may have non-uniform lengths, due to characteristics of the transmission medium. An example is the encoding alphabet of Morse code, where a 'dash' takes longer to send than a 'dot', and therefore the cost of a dash in transmission time is higher. The goal is still to minimize the weighted average codeword length, but it is no longer sufficient just to minimize the number of symbols used by the message. No algorithm is known to solve this in the same manner or with the same efficiency as conventional Huffman coding.

### Optimal alphabetic binary trees (Hu-Tucker coding)

In the standard Huffman coding problem, it is assumed that any codeword can correspond to any input symbol. In the alphabetic version, the alphabetic order of inputs and outputs must be identical. Thus, for example, A = \left\{a,b,c\right\} could not be assigned code H\left(A,C\right) = \left\{00,1,01\right\} , but instead should be assigned either H\left(A,C\right) =\left\{00,01,1\right\} or H\left(A,C\right) = \left\{0,10,11\right\} . This is also known as the Hu-Tucker problem, after the authors of the paper presenting the first linearithmic solution to this optimal binary alphabetic problem, which has some similarities to Huffman algorithm, but is not a variation of this algorithm. These optimal alphabetic binary trees are often used as binary search trees.

### The canonical Huffman code

If weights corresponding to the alphabetically ordered inputs are in numerical order, the Huffman code has the same lengths as the optimal alphabetic code, which can be found from calculating these lengths, rendering Hu-Tucker coding unnecessary. The code resulting from numerically (re-)ordered input is sometimes called the canonical Huffman code and is often the code used in practice, due to ease of encoding/decoding. The technique for finding this code is sometimes called Huffman-Shannon-Fano coding, since it is optimal like Huffman coding, but alphabetic in weight probability, like Shannon-Fano coding. The Huffman-Shannon-Fano code corresponding to the example is \{000,001,01,10,11\} , which, having the same codeword lengths as the original solution, is also optimal.

## Applications

Arithmetic coding can be viewed as a generalization of Huffman coding, in the sense that they produce the same output when every symbol has a probability of the form 1/2k; in particular it tends to offer significantly better compression for small alphabet sizes. Huffman coding nevertheless remains in wide use because of its simplicity and high speed. Intuitively, arithmetic coding can offer better compression than Huffman coding because its "code words" can have effectively non-integer bit lengths, whereas code words in Huffman coding can only have an integer number of bits. Therefore, there is an inefficiency in Huffman coding where a code word of length k only optimally matches a symbol of probability 1/2k and other probabilities are not represented as optimally; whereas the code word length in arithmetic coding can be made to exactly match the true probability of the symbol.

Huffman coding today is often used as a "back-end" to some other compression methods.

DEFLATE (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by Huffman coding (or variable-length prefix-free codes with a similar structure, although perhaps not necessarily designed by using Huffman's algorithm).

References:
[1] see Ken Huffman (1991)
````

</details>

<details><summary><b>Step 6 — revision_6</b> (4065 words)</summary>

````text
In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding and/or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Ph.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".[1]

The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file). The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted.[2] However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods.

Specifically, Huffman coding is optimal if probabilities of symbols are natural powers of 1/2, what is usually inaccurate. For example symbol of probability 0.99 carries only log(1/0.99)\approx 0.014 bits of information, while Huffman coding would need to use 1 bit for this symbol. This sub-optimality is repaired in arithmetic coding and recent faster Asymmetric Numeral Systems family of entropy codings.

## History

In 1951, David A. Huffman and his MIT information theory classmates were given the choice of a term paper or a final exam. The professor, Robert M. Fano, assigned a term paper on the problem of finding the most efficient binary code. Huffman, unable to prove any codes were the most efficient, was about to give up and start studying for the final when he hit upon the idea of using a frequency-sorted binary tree and quickly proved this method the most efficient.[3]

In doing so, Huffman outdid Fano, who had worked with information theory inventor Claude Shannon to develop a similar code. By building the tree from the bottom up instead of

the top down, Huffman avoided the major flaw of the suboptimal Shannon-Fano coding.

## Terminology

Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code (sometimes called "prefix-free codes", that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol). Huffman coding is such a widespread method for creating prefix codes that the term "Huffman code" is widely used as a synonym for "prefix code" even when such a code is not produced by Huffman's algorithm.

## Problem definition

### Informal description

Given A set of symbols and their weights (usually proportional to probabilities).

Find A prefix-free binary code (a set of codewords) with minimum expected codeword length (equivalently, a tree with minimum weighted path length from the root).

### Formalized description

Input.

Alphabet A = \left\{a_{1},a_{2},\cdots,a_{n}\right\} , which is the symbol alphabet of size n .

Set W = \left\{w_{1},w_{2},\cdots,w_{n}\right\} , which is the set of the (positive) symbol weights (usually proportional to probabilities), i.e. w_{i} = \mathrm{weight}\left(a_{i}\right), 1\leq i \leq n .

Output.

Code C \left(A,W\right) = (c_{1},c_{2},\cdots,c_{n}) , which is the tuple of (binary) codewords, where c_{i} is the codeword for a_{i}, 1 \leq i \leq n .

Goal.

Let L\left(C\right) = \sum_{i=1}^{n}{w_{i}\times\mathrm{length}\left(c_{i}\right)} be the weighted path length of code C . Condition: L\left(C\right) \leq L\left(T\right) for any code T\left(A,W\right) .

### Example

We give an example of the result of Huffman coding for a code with five characters and given weights. We will not verify that it minimizes L over all codes, but we will compute L and compare it to the Shannon entropy H of the given set of weights; the result is nearly optimal.

For any code that is biunique, meaning that the code is uniquely decodeable, the sum of the probability budgets across all symbols is always less than or equal to one. In this example, the sum is strictly equal to one; as a result, the code is termed a complete code. If this is not the case, you can always derive an equivalent code by adding extra symbols (with associated null probabilities), to make the code complete while keeping it biunique.

As defined by Shannon (1948), the information content h (in bits) of each symbol ai with non-null probability is

h(a_i) = \log_2{1 \over w_i}.

The entropy H (in bits) is the weighted sum, across all symbols ai with non-zero probability wi, of the information content of each symbol:

H(A) = \sum_{w_i > 0} w_i h(a_i) = \sum_{w_i > 0} w_i \log_2{1 \over w_i} = - \sum_{w_i > 0} w_i \log_2{w_i}.

(Note: A symbol with zero probability has zero contribution to the entropy, since \lim_{w \to 0^+} w \log_2 w = 0 So for simplicity, symbols with zero probability can be left out of the formula above.)

As a consequence of Shannon's source coding theorem, the entropy is a measure of the smallest codeword length that is theoretically possible for the given alphabet with associated weights. In this example, the weighted average codeword length is 2.25 bits per symbol, only slightly larger than the calculated entropy of 2.205 bits per symbol. So not only is this code optimal in the sense that no other feasible code performs better, but it is very close to the theoretical limit established by Shannon.

In general, a Huffman code need not be unique. Thus the set of Huffman codes for a given probability distribution is a non-empty subset of the codes minimizing L(C) for that probability distribution. (However, for each minimizing codeword length assignment, there exists at least one Huffman code with those lengths.)

## Basic technique

### Compression

The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which depends on the number of symbols, n . A node can be either a leaf node or an internal node. Initially, all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node. Internal nodes contain symbol weight, links to two child nodes and the optional link to a parent node. As a common convention, bit '0' represents following the left child and bit '1' represents following the right child. A finished tree has up to n leaf nodes and n-1 internal nodes. A Huffman tree that omits unused symbols produces the most optimal code lengths.

The process essentially begins with the leaf nodes containing the probabilities of the symbol they represent, then a new node whose children are the 2 nodes with smallest probability is created, such that the new node's probability is equal to the sum of the children's probability. With the previous 2 nodes merged into one node (thus not considering them anymore), and with the new node being now considered, the procedure is repeated until only one node remains, the Huffman tree.

The simplest construction algorithm uses a priority queue where the node with lowest probability is given highest priority:

Create a leaf node for each symbol and add it to the priority queue.

While there is more than one node in the queue:

Remove the two nodes of highest priority (lowest probability) from the queue

Create a new internal node with these two nodes as children and with probability equal to the sum of the two nodes' probabilities.

Add the new node to the queue.

The remaining node is the root node and the tree is complete.

Since efficient priority queue data structures require O(log n) time per insertion, and a tree with n leaves has 2n−1 nodes, this algorithm operates in O(n log n) time, where n is the number of symbols.

If the symbols are sorted by probability, there is a linear-time (O(n)) method to create a Huffman tree using two queues, the first one containing the initial weights (along with pointers to the associated leaves), and combined weights (along with pointers to the trees) being put in the back of the second queue. This assures that the lowest weight is always kept at the front of one of the two queues:

Start with as many leaves as there are symbols.

Enqueue all leaf nodes into the first queue (by probability in increasing order so that the least likely item is in the head of the queue).

While there is more than one node in the queues:

Dequeue the two nodes with the lowest weight by examining the fronts of both queues.

Create a new internal node, with the two just-removed nodes as children (either node can be either child) and the sum of their weights as the new weight.

Enqueue the new node into the rear of the second queue.

The remaining node is the root node; the tree has now been generated.

Although linear-time given sorted input, in the general case of arbitrary input, using this algorithm requires pre-sorting. Thus, since sorting takes O(n log n) time in the general case, both methods have the same overall complexity.

In many cases, time complexity is not very important in the choice of algorithm here, since n here is the number of symbols in the alphabet, which is typically a very small number (compared to the length of the message to be encoded); whereas complexity analysis concerns the behavior when n grows to be very large.

It is generally beneficial to minimize the variance of codeword length. For example, a communication buffer receiving Huffman-encoded data may need to be larger to deal with especially long symbols if the tree is especially unbalanced. To minimize variance, simply break ties between queues by choosing the item in the first queue. This modification will retain the mathematical optimality of the Huffman coding while both minimizing variance and minimizing the length of the longest character code.

Here's an example of optimized Huffman coding using the French subject string "j'aime aller sur le bord de l'eau les jeudis ou les jours impairs". Note that the original Huffman coding tree structure would be different from the given example:

### Decompression

Generally speaking, the process of decompression is simply a matter of translating the stream of prefix codes to individual byte values, usually by traversing the Huffman tree node by node as each bit is read from the input stream (reaching a leaf node necessarily terminates the search for that particular byte value). Before this can take place, however, the Huffman tree must be somehow reconstructed. In the simplest case, where character frequencies are fairly predictable, the tree can be preconstructed (and even statistically adjusted on each compression cycle) and thus reused every time, at the expense of at least some measure of compression efficiency. Otherwise, the information to reconstruct the tree must be sent a priori. A naive approach might be to prepend the frequency count of each character to the compression stream. Unfortunately, the overhead in such a case could amount to several kilobytes, so this method has little practical use. If the data is compressed using canonical encoding, the compression model can be precisely reconstructed with just B2^B bits of information (where B is the number of bits per symbol). Another method is to simply prepend the Huffman tree, bit by bit, to the output stream. For example, assuming that the value of 0 represents a parent node and 1 a leaf node, whenever the latter is encountered the tree building routine simply reads the next 8 bits to determine the character value of that particular leaf. The process continues recursively until the last leaf node is reached; at that point, the Huffman tree will thus be faithfully reconstructed. The overhead using such a method ranges from roughly 2 to 320 bytes (assuming an 8-bit alphabet). Many other techniques are possible as well. In any case, since the compressed data can include unused "trailing bits" the decompressor must be able to determine when to stop producing output. This can be accomplished by either transmitting the length of the decompressed data along with the compression model or by defining a special code symbol to signify the end of input (the latter method can adversely affect code length optimality, however).

## Main properties

The probabilities used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

This requires that a frequency table must be stored with the compressed text. See the Decompression section above for more information about the various techniques employed for this purpose.

### Optimality

Although Huffman's original algorithm is optimal for a symbol-by-symbol coding (i.e., a stream of unrelated symbols) with a known input probability distribution, it is not optimal when the symbol-by-symbol restriction is dropped, or when the probability mass functions are unknown. Also, if symbols are not independent and identically distributed, a single code may be insufficient for optimality. Other methods such as arithmetic coding and LZW coding often have better compression capability: Both of these methods can combine an arbitrary number of symbols for more efficient coding, and generally adapt to the actual input statistics, useful when input probabilities are not precisely known or vary significantly within the stream. However, these methods have higher computational complexity. Also, both arithmetic coding and LZW were historically a subject of some concern over patent issues. However, as of mid-2010, the most commonly used techniques for these alternatives to Huffman coding have passed into the public domain as the early patents have expired.

However, the limitations of Huffman coding should not be overstated; it can be used adaptively, accommodating unknown, changing, or context-dependent probabilities. In the case of known independent and identically distributed random variables, combining symbols ("blocking") reduces inefficiency in a way that approaches optimality as the number of symbols combined increases. Huffman coding is optimal when each input symbol is a known independent and identically distributed random variable having a probability that is the inverse of a power of two.

Prefix codes tend to have inefficiency on small alphabets, where probabilities often fall between these optimal points. The worst case for Huffman coding can happen when the probability of a symbol exceeds 2−1 = 0.5, making the upper limit of inefficiency unbounded. These situations often respond well to a form of blocking called run-length encoding; for the simple case of Bernoulli processes, Golomb coding is a probably optimal run-length code.

For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding, e.g., ASCII coding. This reflects the fact that compression is not possible with such an input.

## Variations

Many variations of Huffman coding exist, some of which use a Huffman-like algorithm, and others of which find optimal prefix codes (while, for example, putting different restrictions on the output). Note that, in the latter case, the method need not be Huffman-like, and, indeed, need not even be polynomial time. An exhaustive list of papers on Huffman coding and its variations is given by "Code and Parse Trees for Lossless Source Encoding".[4]

### n-ary Huffman coding

The n-ary Huffman algorithm uses the {0, 1, ... , n − 1} alphabet to encode message and build an n-ary tree. This approach was considered by Huffman in his original paper. The same algorithm applies as for binary (n equals 2) codes, except that the n least probable symbols are taken together, instead of just the 2 least probable. Note that for n greater than 2, not all sets of source words can properly form an n-ary tree for Huffman coding. In these cases, additional 0-probability place holders must be added. This is because the tree must form an n to 1 contractor; for binary coding, this is a 2 to 1 contractor, and any sized set can form such a contractor. If the number of source words is congruent to 1 modulo n-1, then the set of source words will form a proper Huffman tree.

### Adaptive Huffman coding

A variation called adaptive Huffman coding involves calculating the probabilities dynamically based on recent actual frequencies in the sequence of source symbols, and changing the coding tree structure to match the updated probability estimates. It is used rarely in practice, since the cost of updating the tree makes it slower than optimized adaptive arithmetic coding, which is more flexible and has better compression.

### Huffman template algorithm

Most often, the weights used in implementations of Huffman coding represent numeric probabilities, but the algorithm given above does not require this; it requires only that the weights form a totally ordered commutative monoid, meaning a way to order weights and to add them. The Huffman template algorithm enables one to use any kind of weights (costs, frequencies, pairs of weights, non-numerical weights) and one of many combining methods (not just addition). Such algorithms can solve other minimization problems, such as minimizing \max_i\left[w_{i}+\mathrm{length}\left(c_{i}\right)\right] , a problem first applied to circuit design.

### Length-limited Huffman coding/minimum variance Huffman coding

Length-limited Huffman coding is a variant where the goal is still to achieve a minimum weighted path length, but there is an additional restriction that the length of each codeword must be less than a given constant. The package-merge algorithm solves this problem with a simple greedy approach very similar to that used by Huffman's algorithm. Its time complexity is O(nL) , where L is the maximum length of a codeword. No algorithm is known to solve this problem in linear or linearithmic time, unlike the presorted and unsorted conventional Huffman problems, respectively.

### Huffman coding with unequal letter costs

In the standard Huffman coding problem, it is assumed that each symbol in the set that the code words are constructed from has an equal cost to transmit: a code word whose length is N digits will always have a cost of N, no matter how many of those digits are 0s, how many are 1s, etc. When working under this assumption, minimizing the total cost of the message and minimizing the total number of digits are the same thing.

Huffman coding with unequal letter costs is the generalization without this assumption: the letters of the encoding alphabet may have non-uniform lengths, due to characteristics of the transmission medium. An example is the encoding alphabet of Morse code, where a 'dash' takes longer to send than a 'dot', and therefore the cost of a dash in transmission time is higher. The goal is still to minimize the weighted average codeword length, but it is no longer sufficient just to minimize the number of symbols used by the message. No algorithm is known to solve this in the same manner or with the same efficiency as conventional Huffman coding, though it has been solved by Karp whose solution has been refined for the case of integer costs by Golin.

### Optimal alphabetic binary trees (Hu–Tucker coding)

In the standard Huffman coding problem, it is assumed that any codeword can correspond to any input symbol. In the alphabetic version, the alphabetic order of inputs and outputs must be identical. Thus, for example, A = \left\{a,b,c\right\} could not be assigned code H\left(A,C\right) = \left\{00,1,01\right\} , but instead should be assigned either H\left(A,C\right) =\left\{00,01,1\right\} or H\left(A,C\right) = \left\{0,10,11\right\} . This is also known as the Hu–Tucker problem, after T. C. Hu and Alan Tucker, the authors of the paper presenting the first linearithmic solution to this optimal binary alphabetic problem,[5] which has some similarities to Huffman algorithm, but is not a variation of this algorithm. These optimal alphabetic binary trees are often used as binary search trees.

### The canonical Huffman code

If weights corresponding to the alphabetically ordered inputs are in numerical order, the Huffman code has the same lengths as the optimal alphabetic code, which can be found from calculating these lengths, rendering Hu–Tucker coding unnecessary. The code resulting from numerically (re-)ordered input is sometimes called the canonical Huffman code and is often the code used in practice, due to ease of encoding/decoding. The technique for finding this code is sometimes called Huffman-Shannon-Fano coding, since it is optimal like Huffman coding, but alphabetic in weight probability, like Shannon-Fano coding. The Huffman-Shannon-Fano code corresponding to the example is \{000,001,01,10,11\} , which, having the same codeword lengths as the original solution, is also optimal. But in canonical Huffman code, the result is \{110,111,00,01,10\} .

## Relationship with tANS coding - generalization to include fractional bits

Huffman coding approximates informational content of symbols to a natural number of bits (approximates probabilities with powers of 1/2). It turns out its decoder can be seen as a special case of tabled variant of Asymmetric Numeral Systems entropy coding (tANS), used for example in Facebook Zstandard compressor, which allows to include fractional bits into considerations to improve compression ration. Their common decoding step can be implemented as:

where x is a natural number acting as a bit buffer, which for Huffman coding contains the maximal number of bits used per symbol (D being depth of the prefix tree). Some number of its oldest bits determine the symbol to decode, the remaining bits have to be shifted to the oldest position of x, and its youngest positions are refilled with bits from the bitstream. Finally, for Huffman coding we have decodingTable[x].newX = (x << nbBits) & mask , where mask=2^D-1 allows to extract D bits.

The tANS coding also uses the above decoding step, but instead of just shifting the remaining unused bits, they are modified accordingly to the remaining fractional number of bits by a proper choice of decodingTable[x].newX table. Its specific choice is determined by assigning a symbol to every possible value of x, such that the number of symbol appearances are proportional to the assumed probability distribution. While tANS has a freedom of choosing a specific assignment, it becomes Huffman decoder if every symbol is assigned a range of length being a power of 2, for example "aaaabcdd" assignment for a->0, b->100, c->101, d->11 prefix code, which is optimal for Pr(a)=4/8, Pr(b)=1/8, Pr(c)=1/8, Pr(d)=2/8 probability distribution. In contrast, tANS could also use e.g. "abdacdac" assignment, which would provide a better compression ratio for Pr(a)=3/8, Pr(b)=1/8, Pr(c)=2/8, Pr(d)=2/8 probability distribution.

## Applications

Arithmetic coding can be viewed as a generalization of Huffman coding, in the sense that they produce the same output when every symbol has a probability of the form 1/2k; in particular it tends to offer significantly better compression for small alphabet sizes. Huffman coding nevertheless remains in wide use because of its simplicity, high speed, and lack of patent coverage. Intuitively, arithmetic coding can offer better compression than Huffman coding because its "code words" can have effectively non-integer bit lengths, whereas code words in Huffman coding can only have an integer number of bits. Therefore, there is an inefficiency in Huffman coding where a code word of length k only optimally matches a symbol of probability 1/2k and other probabilities are not represented as optimally; whereas the code word length in arithmetic coding can be made to exactly match the true probability of the symbol.

In 2013 faster alternative to Arithmetic coding was proposed, capable of using fractional number of bits to store codewords with Asymmetric Numeral Systems (ANS).[6] This variant is used in Facebook's Zstandard (2016) and in Apple's LZFSE (2015).

Huffman coding today is often used as a "back-end" to some other compression methods.

DEFLATE (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by Huffman coding (or variable-length prefix-free codes with a similar structure, although perhaps not necessarily designed by using Huffman's algorithm).

References:
[1] Huffman, D.. (1952). A Method for the Construction of Minimum-Redundancy Codes. Proceedings of the IRE. doi:10.1109/JRPROC.1952.273898
[2] Van Leeuwen, Jan. (1976). On the construction of Huffman trees. ICALP. http://www.staff.science.uu.nl/~leeuw112/huffman.pdf
[3] see Ken Huffman (1991)
[4] Abrahams, J.. (1997-06-11). Code and Parse Trees for Lossless Source Encoding. Compression and Complexity of Sequences 1997 Proceedings. doi:10.1109/SEQUEN.1997.666911
[5] Hu, T. C.. (1971). Optimal Computer Search Trees and Variable-Length Alphabetical Codes. SIAM Journal on Applied Mathematics. doi:10.1137/0121057
[6] Duda, Jarosław. (2015-01-31). ASYMMETRIC NUMERAL SYSTEMS AS ACCURATE RELACEMENT FOR HUFFMAN CODING. http://fit2015.mimuw.edu.pl/wp-content/uploads/2015/01/ANSshort1.pdf
````

</details>

<details><summary><b>Step 7 — revision_7</b> (3664 words)</summary>

````text
In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding and/or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".[1]

The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file). The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted.[2] However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods.

## History

In 1951, David A. Huffman and his MIT information theory classmates were given the choice of a term paper or a final exam. The professor, Robert M. Fano, assigned a term paper on the problem of finding the most efficient binary code. Huffman, unable to prove any codes were the most efficient, was about to give up and start studying for the final when he hit upon the idea of using a frequency-sorted binary tree and quickly proved this method the most efficient.[3]

In doing so, Huffman outdid Fano, who had worked with information theory inventor Claude Shannon to develop a similar code. By building the tree from the bottom up instead of

the top down, Huffman avoided the major flaw of the suboptimal Shannon-Fano coding.

## Terminology

Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code (sometimes called "prefix-free codes", that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol). Huffman coding is such a widespread method for creating prefix codes that the term "Huffman code" is widely used as a synonym for "prefix code" even when such a code is not produced by Huffman's algorithm.

## Problem definition

### Informal description

Given A set of symbols and their weights (usually proportional to probabilities).

Find A prefix-free binary code (a set of codewords) with minimum expected codeword length (equivalently, a tree with minimum weighted path length from the root).

### Formalized description

Input.

Alphabet A = \left\{a_{1},a_{2},\cdots,a_{n}\right\} , which is the symbol alphabet of size n .

Set W = \left\{w_{1},w_{2},\cdots,w_{n}\right\} , which is the set of the (positive) symbol weights (usually proportional to probabilities), i.e. w_{i} = \mathrm{weight}\left(a_{i}\right), 1\leq i \leq n .

Output.

Code C \left(A,W\right) = (c_{1},c_{2},\cdots,c_{n}) , which is the tuple of (binary) codewords, where c_{i} is the codeword for a_{i}, 1 \leq i \leq n .

Goal.

Let L\left(C\right) = \sum_{i=1}^{n}{w_{i}\times\mathrm{length}\left(c_{i}\right)} be the weighted path length of code C . Condition: L\left(C\right) \leq L\left(T\right) for any code T\left(A,W\right) .

### Example

We give an example of the result of Huffman coding for a code with five characters and given weights. We will not verify that it minimizes L over all codes, but we will compute L and compare it to the Shannon entropy H of the given set of weights; the result is nearly optimal.

For any code that is biunique, meaning that the code is uniquely decodeable, the sum of the probability budgets across all symbols is always less than or equal to one. In this example, the sum is strictly equal to one; as a result, the code is termed a complete code. If this is not the case, you can always derive an equivalent code by adding extra symbols (with associated null probabilities), to make the code complete while keeping it biunique.

As defined by Shannon (1948), the information content h (in bits) of each symbol ai with non-null probability is

h(a_i) = \log_2{1 \over w_i}.

The entropy H (in bits) is the weighted sum, across all symbols ai with non-zero probability wi, of the information content of each symbol:

H(A) = \sum_{w_i > 0} w_i h(a_i) = \sum_{w_i > 0} w_i \log_2{1 \over w_i} = - \sum_{w_i > 0} w_i \log_2{w_i}.

(Note: A symbol with zero probability has zero contribution to the entropy, since \lim_{w \to 0^+} w \log_2 w = 0 So for simplicity, symbols with zero probability can be left out of the formula above.)

As a consequence of Shannon's source coding theorem, the entropy is a measure of the smallest codeword length that is theoretically possible for the given alphabet with associated weights. In this example, the weighted average codeword length is 2.25 bits per symbol, only slightly larger than the calculated entropy of 2.205 bits per symbol. So not only is this code optimal in the sense that no other feasible code performs better, but it is very close to the theoretical limit established by Shannon.

In general, a Huffman code need not be unique. Thus the set of Huffman codes for a given probability distribution is a non-empty subset of the codes minimizing L(C) for that probability distribution. (However, for each minimizing codeword length assignment, there exists at least one Huffman code with those lengths.)

## Basic technique

### Compression

The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which depends on the number of symbols, n . A node can be either a leaf node or an internal node. Initially, all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node. Internal nodes contain a weight, links to two child nodes and an optional link to a parent node. As a common convention, bit '0' represents following the left child and bit '1' represents following the right child. A finished tree has up to n leaf nodes and n-1 internal nodes. A Huffman tree that omits unused symbols produces the most optimal code lengths.

The process begins with the leaf nodes containing the probabilities of the symbol they represent. Then, the process takes the two nodes with smallest probability, and creates a new internal node having these two nodes as children. The weight of the new node is set to the sum of the weight of the children. We then apply the process again, on the new internal node and on the remaining nodes (i.e., we exclude the two leaf nodes), we repeat this process until only one node remains, which is the root of the Huffman tree.

The simplest construction algorithm uses a priority queue where the node with lowest probability is given highest priority:

Create a leaf node for each symbol and add it to the priority queue.

While there is more than one node in the queue:

Remove the two nodes of highest priority (lowest probability) from the queue

Create a new internal node with these two nodes as children and with probability equal to the sum of the two nodes' probabilities.

Add the new node to the queue.

The remaining node is the root node and the tree is complete.

Since efficient priority queue data structures require O(log n) time per insertion, and a tree with n leaves has 2n−1 nodes, this algorithm operates in O(n log n) time, where n is the number of symbols.

If the symbols are sorted by probability, there is a linear-time (O(n)) method to create a Huffman tree using two queues, the first one containing the initial weights (along with pointers to the associated leaves), and combined weights (along with pointers to the trees) being put in the back of the second queue. This assures that the lowest weight is always kept at the front of one of the two queues:

Start with as many leaves as there are symbols.

Enqueue all leaf nodes into the first queue (by probability in increasing order so that the least likely item is in the head of the queue).

While there is more than one node in the queues:

Dequeue the two nodes with the lowest weight by examining the fronts of both queues.

Create a new internal node, with the two just-removed nodes as children (either node can be either child) and the sum of their weights as the new weight.

Enqueue the new node into the rear of the second queue.

The remaining node is the root node; the tree has now been generated.

Although linear-time given sorted input, in the general case of arbitrary input, using this algorithm requires pre-sorting. Thus, since sorting takes O(n log n) time in the general case, both methods have the same overall complexity.

In many cases, time complexity is not very important in the choice of algorithm here, since n here is the number of symbols in the alphabet, which is typically a very small number (compared to the length of the message to be encoded); whereas complexity analysis concerns the behavior when n grows to be very large.

It is generally beneficial to minimize the variance of codeword length. For example, a communication buffer receiving Huffman-encoded data may need to be larger to deal with especially long symbols if the tree is especially unbalanced. To minimize variance, simply break ties between queues by choosing the item in the first queue. This modification will retain the mathematical optimality of the Huffman coding while both minimizing variance and minimizing the length of the longest character code.

### Decompression

Generally speaking, the process of decompression is simply a matter of translating the stream of prefix codes to individual byte values, usually by traversing the Huffman tree node by node as each bit is read from the input stream (reaching a leaf node necessarily terminates the search for that particular byte value). Before this can take place, however, the Huffman tree must be somehow reconstructed. In the simplest case, where character frequencies are fairly predictable, the tree can be preconstructed (and even statistically adjusted on each compression cycle) and thus reused every time, at the expense of at least some measure of compression efficiency. Otherwise, the information to reconstruct the tree must be sent a priori. A naive approach might be to prepend the frequency count of each character to the compression stream. Unfortunately, the overhead in such a case could amount to several kilobytes, so this method has little practical use. If the data is compressed using canonical encoding, the compression model can be precisely reconstructed with just B2^B bits of information (where B is the number of bits per symbol). Another method is to simply prepend the Huffman tree, bit by bit, to the output stream. For example, assuming that the value of 0 represents a parent node and 1 a leaf node, whenever the latter is encountered the tree building routine simply reads the next 8 bits to determine the character value of that particular leaf. The process continues recursively until the last leaf node is reached; at that point, the Huffman tree will thus be faithfully reconstructed. The overhead using such a method ranges from roughly 2 to 320 bytes (assuming an 8-bit alphabet). Many other techniques are possible as well. In any case, since the compressed data can include unused "trailing bits" the decompressor must be able to determine when to stop producing output. This can be accomplished by either transmitting the length of the decompressed data along with the compression model or by defining a special code symbol to signify the end of input (the latter method can adversely affect code length optimality, however).

## Main properties

The probabilities used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

This requires that a frequency table must be stored with the compressed text. See the Decompression section above for more information about the various techniques employed for this purpose.

### Optimality

Although Huffman's original algorithm is optimal for a symbol-by-symbol coding (i.e., a stream of unrelated symbols) with a known input probability distribution, it is not optimal when the symbol-by-symbol restriction is dropped, or when the probability mass functions are unknown. Also, if symbols are not independent and identically distributed, a single code may be insufficient for optimality. Other methods such as arithmetic coding and LZW coding often have better compression capability: Both of these methods can combine an arbitrary number of symbols for more efficient coding, and generally adapt to the actual input statistics, useful when input probabilities are not precisely known or vary significantly within the stream. However, these methods have higher computational complexity. Also, both arithmetic coding and LZW were historically a subject of some concern over patent issues. However, as of mid-2010, the most commonly used techniques for these alternatives to Huffman coding have passed into the public domain as the early patents have expired.

However, Huffman coding still has advantages: it can be used adaptively, accommodating unknown, changing, or context-dependent probabilities. In the case of known independent and identically distributed random variables, combining symbols ("blocking") reduces inefficiency in a way that approaches optimality as the number of symbols combined increases. Huffman coding is optimal when each input symbol is a known independent and identically distributed random variable having a probability that is the inverse of a power of two.

Prefix codes tend to have inefficiency on small alphabets, where probabilities often fall between these optimal points. The worst case for Huffman coding can happen when the probability of a symbol exceeds 2−1 = 0.5, making the upper limit of inefficiency unbounded. Combining symbols together ("blocking") can be used to make Huffman coding as efficient as theoretically possible. A form of blocking called run-length encoding, in which lengths of repeated symbols are counted, is in particularly wide use. For the simple case of Bernoulli processes, Golomb coding is optimal among run-length codes, a fact proved via the techniques of Huffman coding.[4] A similar approach is taken by fax machines using modified Huffman coding.

For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding, e.g., ASCII coding. This reflects the fact that compression is not possible with such an input.

## Variations

Many variations of Huffman coding exist,[5] some of which use a Huffman-like algorithm, and others of which find optimal prefix codes (while, for example, putting different restrictions on the output). Note that, in the latter case, the method need not be Huffman-like, and, indeed, need not even be polynomial time.

### n-ary Huffman coding

The n-ary Huffman algorithm uses the {0, 1, ... , n − 1} alphabet to encode message and build an n-ary tree. This approach was considered by Huffman in his original paper. The same algorithm applies as for binary (n equals 2) codes, except that the n least probable symbols are taken together, instead of just the 2 least probable. Note that for n greater than 2, not all sets of source words can properly form an n-ary tree for Huffman coding. In these cases, additional 0-probability place holders must be added. This is because the tree must form an n to 1 contractor; for binary coding, this is a 2 to 1 contractor, and any sized set can form such a contractor. If the number of source words is congruent to 1 modulo n-1, then the set of source words will form a proper Huffman tree.

### Adaptive Huffman coding

A variation called adaptive Huffman coding involves calculating the probabilities dynamically based on recent actual frequencies in the sequence of source symbols, and changing the coding tree structure to match the updated probability estimates. It is used rarely in practice, since the cost of updating the tree makes it slower than optimized adaptive arithmetic coding, which is more flexible and has better compression.

### Huffman template algorithm

Most often, the weights used in implementations of Huffman coding represent numeric probabilities, but the algorithm given above does not require this; it requires only that the weights form a totally ordered commutative monoid, meaning a way to order weights and to add them. The Huffman template algorithm enables one to use any kind of weights (costs, frequencies, pairs of weights, non-numerical weights) and one of many combining methods (not just addition). Such algorithms can solve other minimization problems, such as minimizing \max_i\left[w_{i}+\mathrm{length}\left(c_{i}\right)\right] , a problem first applied to circuit design.

### Length-limited Huffman coding/minimum variance Huffman coding

Length-limited Huffman coding is a variant where the goal is still to achieve a minimum weighted path length, but there is an additional restriction that the length of each codeword must be less than a given constant. The package-merge algorithm solves this problem with a simple greedy approach very similar to that used by Huffman's algorithm. Its time complexity is O(nL) , where L is the maximum length of a codeword. No algorithm is known to solve this problem in linear or linearithmic time, unlike the presorted and unsorted conventional Huffman problems, respectively.

### Huffman coding with unequal letter costs

In the standard Huffman coding problem, it is assumed that each symbol in the set that the code words are constructed from has an equal cost to transmit: a code word whose length is N digits will always have a cost of N, no matter how many of those digits are 0s, how many are 1s, etc. When working under this assumption, minimizing the total cost of the message and minimizing the total number of digits are the same thing.

Huffman coding with unequal letter costs is the generalization without this assumption: the letters of the encoding alphabet may have non-uniform lengths, due to characteristics of the transmission medium. An example is the encoding alphabet of Morse code, where a 'dash' takes longer to send than a 'dot', and therefore the cost of a dash in transmission time is higher. The goal is still to minimize the weighted average codeword length, but it is no longer sufficient just to minimize the number of symbols used by the message. No algorithm is known to solve this in the same manner or with the same efficiency as conventional Huffman coding, though it has been solved by Karp whose solution has been refined for the case of integer costs by Golin.

### Optimal alphabetic binary trees (Hu–Tucker coding)

In the standard Huffman coding problem, it is assumed that any codeword can correspond to any input symbol. In the alphabetic version, the alphabetic order of inputs and outputs must be identical. Thus, for example, A = \left\{a,b,c\right\} could not be assigned code H\left(A,C\right) = \left\{00,1,01\right\} , but instead should be assigned either H\left(A,C\right) =\left\{00,01,1\right\} or H\left(A,C\right) = \left\{0,10,11\right\} . This is also known as the Hu–Tucker problem, after T. C. Hu and Alan Tucker, the authors of the paper presenting the first linearithmic solution to this optimal binary alphabetic problem,[6] which has some similarities to Huffman algorithm, but is not a variation of this algorithm. These optimal alphabetic binary trees are often used as binary search trees.

### The canonical Huffman code

If weights corresponding to the alphabetically ordered inputs are in numerical order, the Huffman code has the same lengths as the optimal alphabetic code, which can be found from calculating these lengths, rendering Hu–Tucker coding unnecessary. The code resulting from numerically (re-)ordered input is sometimes called the canonical Huffman code and is often the code used in practice, due to ease of encoding/decoding. The technique for finding this code is sometimes called Huffman-Shannon-Fano coding, since it is optimal like Huffman coding, but alphabetic in weight probability, like Shannon-Fano coding. The Huffman-Shannon-Fano code corresponding to the example is \{000,001,01,10,11\} , which, having the same codeword lengths as the original solution, is also optimal. But in canonical Huffman code, the result is \{110,111,00,01,10\} .

## Applications

Arithmetic coding and Huffman coding produce equivalent results — achieving entropy — when every symbol has a probability of the form 1/2k. In other circumstances, arithmetic coding can offer better compression than Huffman coding because — intuitively — its "code words" can have effectively non-integer bit lengths, whereas code words in prefix codes such as Huffman codes can only have an integer number of bits. Therefore, a code word of length k only optimally matches a symbol of probability 1/2k and other probabilities are not represented optimally; whereas the code word length in arithmetic coding can be made to exactly match the true probability of the symbol. This difference is especially striking for small alphabet sizes.

Prefix codes nevertheless remain in wide use because of their simplicity, high speed, and lack of patent coverage. They are often used as a "back-end" to other compression methods. DEFLATE (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by the use of prefix codes; these are often called "Huffman codes" even though most applications use pre-defined variable-length codes rather than codes designed using Huffman's algorithm.

References:
[1] Huffman, D.. (1952). A Method for the Construction of Minimum-Redundancy Codes. Proceedings of the IRE. doi:10.1109/JRPROC.1952.273898
[2] Van Leeuwen, Jan. (1976). On the construction of Huffman trees. ICALP. http://www.staff.science.uu.nl/~leeuw112/huffman.pdf
[3] Huffman, Ken. (1991). Profile: David A. Huffman: Encoding the “Neatness” of Ones and Zeroes. Scientific American. http://www.huffmancoding.com/my-uncle/scientific-american
[4] Gallager, R.G.. (1975). Optimal source codes for geometrically distributed integer alphabets. IEEE Transactions on Information Theory.
[5] Abrahams, J.. (1997-06-11). Code and Parse Trees for Lossless Source Encoding. Compression and Complexity of Sequences 1997 Proceedings. doi:10.1109/SEQUEN.1997.666911
[6] Hu, T. C.. (1971). Optimal Computer Search Trees and Variable-Length Alphabetical Codes. SIAM Journal on Applied Mathematics. doi:10.1137/0121057
````

</details>

<details><summary><b>Step 8 — final</b> (4033 words)</summary>

````text
In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding or using such a code is Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".[1]

The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file). The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted.[2] However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods – it is replaced with arithmetic coding[3] if a better compression ratio is required.

## History

In 1951, David A. Huffman and his MIT information theory classmates were given the choice of a term paper or a final exam. The professor, Robert M. Fano, assigned a term paper on the problem of finding the most efficient binary code. Huffman, unable to prove any codes were the most efficient, was about to give up and start studying for the final when he hit upon the idea of using a frequency-sorted binary tree and quickly proved this method the most efficient.[4]

In doing so, Huffman outdid Fano, who had worked with Claude Shannon to develop a similar code. Building the tree from the bottom up guaranteed optimality, unlike the top-down approach of Shannon–Fano coding.

## Terminology

Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code (sometimes called "prefix-free codes", that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol). Huffman coding is such a widespread method for creating prefix codes that the term "Huffman code" is widely used as a synonym for "prefix code" even when such a code is not produced by Huffman's algorithm.

## Problem definition

### Informal description

Given A set of symbols S and for each symbol x \in S , the frequency f_x representing the fraction of symbols in the text that are equal to x .[5]

Find A prefix-free binary code (a set of codewords) with minimum expected codeword length (equivalently, a tree with minimum weighted path length from the root).

### Formalized description

Input.

Alphabet A = (a_{1},a_{2},\dots,a_{n}) , which is the symbol alphabet of size n .

Tuple W = (w_{1},w_{2},\dots,w_{n}) , which is the tuple of the (positive) symbol weights (usually proportional to probabilities), i.e. w_{i} = \operatorname{weight}\left(a_{i}\right),\, i \in \{1, 2, \dots, n\} .

Output.

Code C\left(W\right) = (c_{1},c_{2},\dots,c_{n}) , which is the tuple of (binary) codewords, where c_{i} is the codeword for a_{i},\, i \in \{1, 2, \dots, n\} .

Goal.

Let L(C(W)) = \sum_{i=1}^n w_i\operatorname{length}(c_i) be the weighted path length of code C . Condition: L(C(W)) \leq L(T(W)) for any code T(W) .

### Example

We give an example of the result of Huffman coding for a code with five characters and given weights. We will not verify that it minimizes L over all codes, but we will compute L and compare it to the Shannon entropy H of the given set of weights; the result is nearly optimal.

For any code that is biunique, meaning that the code is uniquely decodeable, the sum of the probability budgets across all symbols is always less than or equal to one. In this example, the sum is strictly equal to one; as a result, the code is termed a complete code. If this is not the case, one can always derive an equivalent code by adding extra symbols (with associated null probabilities), to make the code complete while keeping it biunique.

As defined by Shannon (1948), the information content h (in bits) of each symbol ai with non-null probability is

h(a_i) = \log_2{1 \over w_i}.

The entropy H (in bits) is the weighted sum, across all symbols ai with non-zero probability wi, of the information content of each symbol:

H(A) = \sum_{w_i > 0} w_i h(a_i) = \sum_{w_i > 0} w_i \log_2 {1 \over w_i} = - \sum_{w_i > 0} w_i \log_2 w_i.

(Note: A symbol with zero probability has zero contribution to the entropy, since \lim_{w \to 0^+} w \log_2 w = 0 . So for simplicity, symbols with zero probability can be left out of the formula above.)

As a consequence of Shannon's source coding theorem, the entropy is a measure of the smallest codeword length that is theoretically possible for the given alphabet with associated weights. In this example, the weighted average codeword length is 2.25 bits per symbol, only slightly larger than the calculated entropy of 2.205 bits per symbol. So not only is this code optimal in the sense that no other feasible code performs better, but it is very close to the theoretical limit established by Shannon.

In general, a Huffman code need not be unique. Thus the set of Huffman codes for a given probability distribution is a non-empty subset of the codes minimizing L(C) for that probability distribution. (However, for each minimizing codeword length assignment, there exists at least one Huffman code with those lengths.)

## Basic technique

### Compression

The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which depends on the number of symbols, n . A node can be either a leaf node or an internal node. Initially, all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node. Internal nodes contain a weight, links to two child nodes and an optional link to a parent node. As a common convention, bit '0' represents following the left child and bit '1' represents following the right child. A finished tree has up to n leaf nodes and n-1 internal nodes. A Huffman tree that omits unused symbols produces the most optimal code lengths.

The process begins with the leaf nodes containing the probabilities of the symbol they represent. Then, the process takes the two nodes with smallest probability, and creates a new internal node having these two nodes as children. The weight of the new node is set to the sum of the weight of the children. We then apply the process again, on the new internal node and on the remaining nodes (i.e., we exclude the two leaf nodes), we repeat this process until only one node remains, which is the root of the Huffman tree.

The simplest construction algorithm uses a priority queue where the node with lowest probability is given highest priority:

Create a leaf node for each symbol and add it to the priority queue.

While there is more than one node in the queue:

Remove the two nodes of highest priority (lowest probability) from the queue

Create a new internal node with these two nodes as children and with probability equal to the sum of the two nodes' probabilities.

Add the new node to the queue.

The remaining node is the root node and the tree is complete.

Since efficient priority queue data structures require O(log n) time per insertion, and a tree with n leaves has 2n−1 nodes, this algorithm operates in O(n log n) time, where n is the number of symbols.

If the symbols are sorted by probability, there is a linear-time (O(n)) method to create a Huffman tree using two queues, the first one containing the initial weights (along with pointers to the associated leaves), and combined weights (along with pointers to the trees) being put in the back of the second queue. This assures that the lowest weight is always kept at the front of one of the two queues:[2]

Start with as many leaves as there are symbols.

Enqueue all leaf nodes into the first queue (by probability in increasing order so that the least likely item is in the head of the queue).

While there is more than one node in the queues:

Dequeue the two nodes with the lowest weight by examining the fronts of both queues.

Create a new internal node, with the two just-removed nodes as children (either node can be either child) and the sum of their weights as the new weight.

Enqueue the new node into the rear of the second queue.

The remaining node is the root node; the tree has now been generated.

Once the Huffman tree has been generated, it is traversed to generate a dictionary which maps the symbols to binary codes as follows:

Start with current node set to the root.

If node is not a leaf node, label the edge to the left child as 0 and the edge to the right child as 1. Repeat the process at both the left child and the right child.

The final encoding of any symbol is then read by a concatenation of the labels on the edges along the path from the root node to the symbol.

In many cases, time complexity is not very important in the choice of algorithm here, since n here is the number of symbols in the alphabet, which is typically a very small number (compared to the length of the message to be encoded); whereas complexity analysis concerns the behavior when n grows to be very large.

It is generally beneficial to minimize the variance of codeword length. For example, a communication buffer receiving Huffman-encoded data may need to be larger to deal with especially long symbols if the tree is especially unbalanced. To minimize variance, simply break ties between queues by choosing the item in the first queue. This modification will retain the mathematical optimality of the Huffman coding while both minimizing variance and minimizing the length of the longest character code.

### Decompression

Generally speaking, the process of decompression is simply a matter of translating the stream of prefix codes to individual byte values, usually by traversing the Huffman tree node by node as each bit is read from the input stream (reaching a leaf node necessarily terminates the search for that particular byte value). Before this can take place, however, the Huffman tree must be somehow reconstructed. In the simplest case, where character frequencies are fairly predictable, the tree can be preconstructed (and even statistically adjusted on each compression cycle) and thus reused every time, at the expense of at least some measure of compression efficiency. Otherwise, the information to reconstruct the tree must be sent a priori. A naive approach might be to prepend the frequency count of each character to the compression stream. Unfortunately, the overhead in such a case could amount to several kilobytes, so this method has little practical use. If the data is compressed using canonical encoding, the compression model can be precisely reconstructed with just B\cdot 2^B bits of information (where B is the number of bits per symbol). Another method is to simply prepend the Huffman tree, bit by bit, to the output stream. For example, assuming that the value of 0 represents a parent node and 1 a leaf node, whenever the latter is encountered the tree building routine simply reads the next 8 bits to determine the character value of that particular leaf. The process continues recursively until the last leaf node is reached; at that point, the Huffman tree will thus be faithfully reconstructed. The overhead using such a method ranges from roughly 2 to 320 bytes (assuming an 8-bit alphabet). Many other techniques are possible as well. In any case, since the compressed data can include unused "trailing bits" the decompressor must be able to determine when to stop producing output. This can be accomplished by either transmitting the length of the compressed data along with the compression model or by defining a special code symbol to signify the end of input (the latter method can adversely affect code length optimality, however).

## Main properties

The probabilities used can be generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed.

This requires that a frequency table must be stored with the compressed text. See the Decompression section above for more information about the various techniques employed for this purpose.

### Optimality

Huffman's original algorithm is optimal for a symbol-by-symbol coding with a known input probability distribution, i.e., separately encoding unrelated symbols in such a data stream. However, it is not optimal when the symbol-by-symbol restriction is dropped, or when the probability mass functions are unknown. Also, if symbols are not independent and identically distributed, a single code may be insufficient for optimality. Other methods such as arithmetic coding often have better compression capability.

Although both aforementioned methods can combine an arbitrary number of symbols for more efficient coding and generally adapt to the actual input statistics, arithmetic coding does so without significantly increasing its computational or algorithmic complexities (though the simplest version is slower and more complex than Huffman coding). Such flexibility is especially useful when input probabilities are not precisely known or vary significantly within the stream. However, Huffman coding is usually faster and arithmetic coding was historically a subject of some concern over patent issues. Thus many technologies have historically avoided arithmetic coding in favor of Huffman and other prefix coding techniques. As of mid-2010, the most commonly used techniques for this alternative to Huffman coding have passed into the public domain as the early patents have expired.

For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding, e.g., ASCII coding. This reflects the fact that compression is not possible with such an input, no matter what the compression method, i.e., doing nothing to the data is the optimal thing to do.

Huffman coding is optimal among all methods in any case where each position in the input stream is a known independent and identically distributed random variable having a probability that is dyadic. Prefix codes, and thus Huffman coding in particular, tend to have inefficiency on small alphabets, where probabilities often fall between these optimal (dyadic) points. The worst case for Huffman coding can happen when the probability of the most likely symbol far exceeds 2−1 = 0.5, making the upper limit of inefficiency unbounded.

There are two related approaches for getting around this particular inefficiency while still using Huffman coding. Combining a fixed number of symbols together ("blocking") often increases (and never decreases) compression. As the size of the block approaches infinity, Huffman coding theoretically approaches the entropy limit, i.e., optimal compression.[6] However, blocking arbitrarily large groups of symbols is impractical, as the complexity of a Huffman code is linear in the number of possibilities to be encoded, a number that is exponential in the size of a block. This limits the amount of blocking that is done in practice.

A practical alternative, in widespread use, is run-length encoding. This technique adds one step in advance of entropy coding, specifically counting (runs) of repeated symbols, which are then encoded. For the simple case of Bernoulli processes, Golomb coding is optimal among prefix codes for coding run length, a fact proved via the techniques of Huffman coding.[7] A similar approach is taken by fax machines using modified Huffman coding. However, run-length coding is not as adaptable to as many input types as other compression technologies.

## Variations

Many variations of Huffman coding exist,[8] some of which use a Huffman-like algorithm, and others of which find optimal prefix codes (while, for example, putting different restrictions on the output). Note that, in the latter case, the method need not be Huffman-like, and, indeed, need not even be polynomial time.

### n-ary Huffman coding

The n-ary Huffman algorithm uses an alphabet of size n, typically {0, 1, ..., n-1}, to encode messages and build an n-ary tree. This approach was considered by Huffman in his original paper. The same algorithm applies as for binary ( n = 2 ) codes, but instead of combining the two least likely symbols, the n least likely symbols are grouped together.

Note that for n > 2, not all sets of source words can properly form a complete n-ary tree for Huffman coding. In these cases, additional placeholder symbols with 0 probability may need to be added. This is because the structure of the tree needs to repeatedly join n branches into one - also known as an "n to 1" combination. For binary coding, this is a "2 to 1" combination, which works with any number of symbols. For n-ary coding, a complete tree is only possible when the total number of symbols (real + placeholders) leaves a remainder of 1 when divided by (n-1).[1]

### Adaptive Huffman coding

A variation called adaptive Huffman coding involves calculating the probabilities dynamically based on recent actual frequencies in the sequence of source symbols, and changing the coding tree structure to match the updated probability estimates. It is used rarely in practice, since the cost of updating the tree makes it slower than optimized adaptive arithmetic coding, which is more flexible and has better compression.

### Huffman template algorithm

Most often, the weights used in implementations of Huffman coding represent numeric probabilities, but the algorithm given above does not require this; it requires only that the weights form a totally ordered commutative monoid, meaning a way to order weights and to add them. The Huffman template algorithm enables one to use any kind of weights (costs, frequencies, pairs of weights, non-numerical weights) and one of many combining methods (not just addition). Such algorithms can solve other minimization problems, such as minimizing \max_i\left[w_{i}+\mathrm{length}\left(c_{i}\right)\right] , a problem first applied to circuit design.

### Length-limited Huffman coding/minimum variance Huffman coding

Length-limited Huffman coding is a variant where the goal is still to achieve a minimum weighted path length, but there is an additional restriction that the length of each codeword must be less than a given constant. The package-merge algorithm solves this problem with a simple greedy approach very similar to that used by Huffman's algorithm. Its time complexity is O(nL) , where L is the maximum length of a codeword. No algorithm is known to solve this problem in O(n) or O(n\log n) time, unlike the presorted and unsorted conventional Huffman problems, respectively.

### Huffman coding with unequal letter costs

In the standard Huffman coding problem, it is assumed that each symbol in the set that the code words are constructed from has an equal cost to transmit: a code word whose length is N digits will always have a cost of N, no matter how many of those digits are 0s, how many are 1s, etc. When working under this assumption, minimizing the total cost of the message and minimizing the total number of digits are the same thing.

Huffman coding with unequal letter costs is the generalization without this assumption: the letters of the encoding alphabet may have non-uniform lengths, due to characteristics of the transmission medium. An example is the encoding alphabet of Morse code, where a 'dash' takes longer to send than a 'dot', and therefore the cost of a dash in transmission time is higher. The goal is still to minimize the weighted average codeword length, but it is no longer sufficient just to minimize the number of symbols used by the message. No algorithm is known to solve this in the same manner or with the same efficiency as conventional Huffman coding, though it has been solved by Richard M. Karp[9] whose solution has been refined for the case of integer costs by Mordecai J. Golin.[10]

### Optimal alphabetic binary trees (Hu–Tucker coding)

In the standard Huffman coding problem, it is assumed that any codeword can correspond to any input symbol. In the alphabetic version, the alphabetic order of inputs and outputs must be identical. Thus, for example, A = \left\{a,b,c\right\} could not be assigned code H\left(A,C\right) = \left\{00,1,01\right\} , but instead should be assigned either H\left(A,C\right) =\left\{00,01,1\right\} or H\left(A,C\right) = \left\{0,10,11\right\} . This is also known as the Hu–Tucker problem, after T. C. Hu and Alan Tucker, the authors of the paper presenting the first O(n\log n) -time solution to this optimal binary alphabetic problem,[11] which has some similarities to Huffman algorithm, but is not a variation of this algorithm. A later method, the Garsia–Wachs algorithm of Adriano Garsia and Michelle L. Wachs (1977), uses simpler logic to perform the same comparisons in the same total time bound. These optimal alphabetic binary trees are often used as binary search trees.[12]

### The canonical Huffman code

If weights corresponding to the alphabetically ordered inputs are in numerical order, the Huffman code has the same lengths as the optimal alphabetic code, which can be found from calculating these lengths, rendering Hu–Tucker coding unnecessary. The code resulting from numerically (re-)ordered input is sometimes called the canonical Huffman code and is often the code used in practice, due to ease of encoding/decoding. The technique for finding this code is sometimes called Huffman–Shannon–Fano coding, since it is optimal like Huffman coding, but alphabetic in weight probability, like Shannon–Fano coding. The Huffman–Shannon–Fano code corresponding to the example is \{000,001,01,10,11\} , which, having the same codeword lengths as the original solution, is also optimal. But in canonical Huffman code, the result is \{110,111,00,01,10\} .

## Applications

Arithmetic coding and Huffman coding produce equivalent results — achieving entropy — when every symbol has a probability of the form 1/2k. In other circumstances, arithmetic coding can offer better compression than Huffman coding because — intuitively — its "code words" can have effectively non-integer bit lengths, whereas code words in prefix codes such as Huffman codes can only have an integer number of bits. Therefore, a code word of length k only optimally matches a symbol of probability 1/2k and other probabilities are not represented optimally; whereas the code word length in arithmetic coding can be made to exactly match the true probability of the symbol. This difference is especially striking for small alphabet sizes.

Prefix codes nevertheless remain in wide use because of their simplicity, high speed, and lack of patent coverage. They are often used as a "back-end" to other compression methods. Deflate (PKZIP's algorithm) and multimedia codecs such as JPEG and MP3 have a front-end model and quantization followed by the use of prefix codes; these are often called "Huffman codes" even though most applications use pre-defined variable-length codes rather than codes designed using Huffman's algorithm.

References:
[1] Huffman, D.. (1952). A Method for the Construction of Minimum-Redundancy Codes. Proceedings of the IRE. doi:10.1109/JRPROC.1952.273898
[2] Van Leeuwen, Jan. (1976). On the construction of Huffman trees. ICALP. http://www.staff.science.uu.nl/~leeuw112/huffman.pdf
[3] (9 April 2014). Fundamentals of Multimedia. Springer Science & Business Media. https://books.google.com/books?id=R6vBBAAAQBAJ
[4] Huffman, Ken. (1991). Profile: David A. Huffman: Encoding the "Neatness" of Ones and Zeroes. Scientific American. http://www.huffmancoding.com/my-uncle/scientific-american
[5] Kleinberg, Jon. (March 16, 2005). Algorithm Design. Pearson Education. https://www.pearson.com/en-us/subject-catalog/p/algorithm-design/P200000003259/9780137546350
[6] Gribov, Alexander. (2017-04-10). Optimal Compression of a Polyline with Segments and Arcs.
[7] Gallager, R.G.. (1975). Optimal source codes for geometrically distributed integer alphabets. IEEE Transactions on Information Theory. doi:10.1109/TIT.1975.1055357
[8] Abrahams, J.. (1997-06-11). Proceedings. Compression and Complexity of SEQUENCES 1997 (Cat. No.97TB100171). IEEE. doi:10.1109/SEQUEN.1997.666911
[9] Karp, Richard M.. Minimum-redundancy coding for the discrete noiseless channel. IRE Transactions on Information Theory. doi:10.1109/TIT.1961.1057615
[10] Golin, Mordekai J.. (January 1998). A Dynamic Programming Algorithm for Constructing Optimal Prefix-Free Codes with Unequal Letter Costs. IEEE Transactions on Information Theory. doi:10.1109/18.705558
[11] Hu, T. C.. (1971). Optimal Computer Search Trees and Variable-Length Alphabetical Codes. SIAM Journal on Applied Mathematics. doi:10.1137/0121057
[12] Knuth, Donald E.. (1998). The Art of Computer Programming, Vol. 3: Sorting and Searching. Addison–Wesley.
````

</details>
