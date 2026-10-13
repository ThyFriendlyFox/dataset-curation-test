# 4. Trie

`B-Trie` · [B_wiki_history_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Trie&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 1060 revisions in history; 41 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 1 | 0 | 0.00 | source_title |
| 1 | earliest_version | 76 | 0 | 0.03 | enwiki rev 290348 (2001-12-10) |
| 2 | early_revision | 3039 | 23 | 0.38 | enwiki rev 1067014548 (2022-01-21) |
| 3 | late_revision | 2458 | 24 | 0.67 | enwiki rev 1082648229 (2022-04-14) |
| 4 | final | 2498 | 30 | 1.00 | enwiki rev 1357162034 (2026-06-01) |

<details><summary><b>Step 0 — title</b> (1 words)</summary>

````text
Trie
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (76 words)</summary>

````text
A trie is a tree data structure that is used for searching a key/value map. In the case of a trie, the keys are restricted to strings whose alphabet has limited cardinality (e.g. the English alphabet). Each node has at most N+1 children (where N is the cardinality of the alphabet), and all of the children of that node share a common prefix denoted by the node's position and value in the tree.

See search algorithm
````

</details>

<details><summary><b>Step 2 — early_revision</b> (3039 words)</summary>

````text
In computer science, a trie, also called digital tree or prefix tree, is a type of k-ary search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key.

Unlike a binary search tree, nodes in the trie do not store their associated key. Instead, a node's position in the trie defines the key with which it is associated. This distributes the value of each key across the data structure, and means that not every node necessarily has an associated value.

All the children of a node have a common prefix of the string associated with that parent node, and the root is associated with the empty string. This task of storing data accessible by its prefix can be accomplished in a memory-optimized way by employing a radix tree.

Though tries can be keyed by character strings, they need not be. The same algorithms can be adapted for ordered lists of any underlying type, e.g. permutations of digits or shapes. In particular, a bitwise trie is keyed on the individual bits making up a piece of fixed-length binary data, such as an integer or memory address.

## History, etymology, and pronunciation

The idea of a trie for representing a set of strings was first abstractly described by Axel Thue in 1912.[1,2] Tries were first described in a computer context by René de la Briandais in 1959.[3,2,4] The idea was independently described in 1960 by Edward Fredkin,[5] who coined the term trie, pronouncing it (as "tree"), after the middle syllable of retrieval.[6,7] However, other authors pronounce it (as "try"), in an attempt to distinguish it verbally from "tree".[6,7,2]

## Operations

Tries support various operations: insertion, deletion, and lookup of a string key. Tries are composed of \text{nodes} that contain links that are either references to other child suffix child nodes, or \text{nil} . Except for root, each node is pointed to by just one other node, called the parent. Each node contains \text{R} links, where \text{R} is the cardinality of the set of alphabets, although tries have a substantial number of \text{nil} links. In most cases, the size of \text{Children} array is bitlength of the character encoding - 256 in the case of (unsigned) ASCII.[8]

The \text{nil} links within \text{Children} in \text{Node} emphasizes the following charactertics:

Characters and string keys are implicitly stored in the trie data structure representation.

Each node contains one possiable link to a prefix of strong keys of the set.

A basic structure type of nodes in the trie is as follows; \text{Node} may contain an optional \text{Value} , which is associated with each key stored in the last character of string, or terminal node.

### Searching

Searching a \text{Value} in a trie is guided by the characters in the search string key, as each node in the trie contains a corresponding link to each possible character in the given string. Thus, following the string within the trie yields the associated \text{Value} for the given string key. A \text{nil} link within search execution indicates the inexistence of the key.

In the above pseudocode, \text{x} and \text{key} correspond to the pointer of trie's root node and the string key respectively. The worse case performance of search is O(m) where \text{m} is the length of the string key; binary search trees, on the other hand, take O(m \log n) , since the search depends on the height ( n ) of the BST, which is logarathmic in number of keys in a balanced tree. Additionally, tries also accupy less space in comparation with BST. The terminal node of the tree contains a non-nil \text{Value} , and it's a search hit if the associated value is found in the trie, and search miss if it isn't.

### Insertion

Insertion into trie is guided by using the character sets as the indexes into the \text{Children} array until last character of the string key is reached.

If a \text{nil} link is encountered prior to reaching the last character of the string key, a new \text{Node} is created, such along lines 3-5. \text{x.Value} gets assigend to input \text{value} ; if \text{x.Value} wasn't \text{nil} at the time of insertion, the value associated with the given string key gets subsituted with the current one.

### Deletion

Deletion of a key-value pair from a trie involves finding the terminal node with the corresponding string key, marking the terminal indicator and value to false and \text{nil} correspondingly.

Following is a recursive procedure for removing a string key ( \text{key} ) from rooted trie ( \text{x} ).

The procedures begins by examining the \text{key} ; \text{nil} denotes the arrival of a terminal node or end of string key. If terminal, the node gets removed from the trie (line 9 assign the character index to \text{nil} ). However, an end of string key without the node being terminal indicates that the key doesn't exist, thus the procedure doesn't modify the trie. The recursion proceeds by incrementing \text{key} 's index.

## Replacing other data structures

### Replacement for hash tables

A trie can be used to replace a hash table, over which it has the following advantages:

Looking up data in a trie is faster in the worst case, O(m) time (where m is the length of a search string), compared to an imperfect hash table. The worst-case lookup speed in an imperfect hash table is O(N) time, but far more typically is O(1), with O(m) time spent evaluating the hash.

There are no collisions of different keys in a trie. (An imperfect hash table can have key collisions. A key collision is the hash function mapping of different keys to the same position in a hash table.)

Buckets in a trie, which are analogous to hash table buckets that store key collisions, are necessary only if a single key is associated with more than one value.

There is no need to provide a hash function or to change hash functions as more keys are added to a trie.

A trie can provide an alphabetical ordering of the entries by key.

However, a trie also has some drawbacks compared to a hash table:

Trie lookup can be slower than hash table lookup, especially if the data is directly accessed on a hard disk drive or some other secondary storage device where the random-access time is high compared to main memory.[5]

Some keys, such as floating point numbers, can lead to long chains and prefixes that are not particularly meaningful. Nevertheless, a bitwise trie can handle standard IEEE single and double format floating point numbers.

Some tries can require more space than a hash table, as memory may be allocated for each character in the search string, rather than a single chunk of memory for the whole entry, as in most hash tables.

### DFSA representation

A trie can be seen as a tree-shaped deterministic finite automaton. Each finite language is generated by a trie automaton, and each trie can be compressed into a deterministic acyclic finite state automaton.

## Implementation strategies

There are several ways to represent tries, corresponding to different trade-offs between memory use and speed of the operations. The basic form is that of a linked set of nodes, where each node contains an array of child pointers, one for each symbol in the alphabet (so for the English alphabet, one would store 26 child pointers and for the alphabet of bytes, 256 pointers). This is simple but wasteful in terms of memory: using the alphabet of bytes (size 256) and four-byte pointers, each node requires a kilobyte of storage, and when there is little overlap in the strings' prefixes, the number of required nodes is roughly the combined length of the stored strings. Put another way, the nodes near the bottom of the tree tend to have few children and there are many of them, so the structure wastes space storing null pointers.[9]

The storage problem can be alleviated by an implementation technique called alphabet reduction, whereby the original strings are reinterpreted as longer strings over a smaller alphabet. E.g., a string of n bytes can alternatively be regarded as a string of 2n four-bit units and stored in a trie with sixteen pointers per node. Lookups need to visit twice as many nodes in the worst case, but the storage requirements go down by a factor of eight.

An alternative implementation represents a node as a triple and links the children of a node together as a singly linked list: points to the node's first child, to the parent node's next child.[9,10] The set of children can also be represented as a binary search tree; one instance of this idea is the ternary search tree developed by Bentley and Sedgewick.

Another alternative in order to avoid the use of an array of 256 pointers (ASCII), as suggested before, is to store the alphabet array as a bitmap of 256 bits representing the ASCII alphabet, reducing dramatically the size of the nodes.[11]

### Bitwise tries

Bitwise tries are much the same as a normal character-based trie except that individual bits are used to traverse what effectively becomes a form of binary tree. Generally, implementations use a special CPU instruction to very quickly find the first set bit in a fixed length key (e.g., GCC's __builtin_clz() intrinsic). This value is then used to index a 32- or 64-entry table which points to the first item in the bitwise trie with that number of leading zero bits. The search then proceeds by testing each subsequent bit in the key and choosing child[0] or child[1] appropriately until the item is found.

Although this process might sound slow, it is very cache-local and highly parallelizable due to the lack of register dependencies and therefore in fact has excellent performance on modern out-of-order execution CPUs. A red–black tree for example performs much better on paper, but is highly cache-unfriendly and causes multiple pipeline and TLB stalls on modern CPUs which makes that algorithm bound by memory latency rather than CPU speed. In comparison, a bitwise trie rarely accesses memory, and when it does, it does so only to read, thus avoiding SMP cache coherency overhead. Hence, it is increasingly becoming the algorithm of choice for code that performs many rapid insertions and deletions, such as memory allocators (e.g., recent versions of the famous Doug Lea's allocator (dlmalloc) and its descendants). The worst case of steps for lookup is the same as bits used to index bins in the tree.[12]

Alternatively, the term "bitwise trie" can more generally refer to a binary tree structure holding integer values, sorting them by their binary prefix. An example is the x-fast trie.

### Compressing tries

Compressing the trie and merging the common branches can sometimes yield large performance gains. This works best under the following conditions:

The trie is (mostly) static, so that no key insertions to or deletions are required (e.g., after bulk creation of the trie).

Only lookups are needed.

The trie nodes are not keyed by node-specific data, or the nodes' data are common.[13]

The total set of stored keys is very sparse within their representation space (so compression pays off).

For example, it may be used to represent sparse bitsets; i.e., subsets of a much larger, fixed enumerable set. In such a case, the trie is keyed by the bit element position within the full set. The key is created from the string of bits needed to encode the integral position of each element. Such tries have a very degenerate form with many missing branches. After detecting the repetition of common patterns or filling the unused gaps, the unique leaf nodes (bit strings) can be stored and compressed easily, reducing the overall size of the trie.

Such compression is also used in the implementation of the various fast lookup tables for retrieving Unicode character properties. These could include case-mapping tables (e.g., for the Greek letter pi, from Π to π), or lookup tables normalizing the combination of base and combining characters (like the a-umlaut in German, ä, or the dalet-patah-dagesh-ole in Biblical Hebrew, ). For such applications, the representation is similar to transforming a very large, unidimensional, sparse table (e.g., Unicode code points) into a multidimensional matrix of their combinations, and then using the coordinates in the hyper-matrix as the string key of an uncompressed trie to represent the resulting character. The compression will then consist of detecting and merging the common columns within the hyper-matrix to compress the last dimension in the key. For example, to avoid storing the full, multibyte Unicode code point of each element forming a matrix column, the groupings of similar code points can be exploited. Each dimension of the hyper-matrix stores the start position of the next dimension, so that only the offset (typically a single byte) need be stored. The resulting vector is itself compressible when it is also sparse, so each dimension (associated to a layer level in the trie) can be compressed separately.

Some implementations do support such data compression within dynamic sparse tries and allow insertions and deletions in compressed tries. However, this usually has a significant cost when compressed segments need to be split or merged. Some tradeoff has to be made between data compression and update speed. A typical strategy is to limit the range of global lookups for comparing the common branches in the sparse trie.

The result of such compression may look similar to trying to transform the trie into a directed acyclic graph (DAG), because the reverse transform from a DAG to a trie is obvious and always possible. However, the shape of the DAG is determined by the form of the key chosen to index the nodes, in turn constraining the compression possible.

Another compression strategy is to "unravel" the data structure into a single byte array.[14]

This approach eliminates the need for node pointers, substantially reducing the memory requirements. This in turn permits memory mapping and the use of virtual memory to efficiently load the data from disk.

One more approach is to "pack" the trie.[7] Liang describes a space-efficient implementation of a sparse packed trie applied to automatic hyphenation, in which the descendants of each node may be interleaved in memory.

### External memory tries

Several trie variants are suitable for maintaining sets of strings in external memory, including suffix trees. A combination of trie and B-tree, called the B-trie has also been suggested for this task; compared to suffix trees, they are limited in the supported operations but also more compact, while performing update operations faster.[15]

## Applications

Trie data structures are commonly used in predictive text or autocomplete dictionaries, and approximate matching algorithms.[16] Tries enable faster searches, occupy less space, especially when the set contains large number of short strings, thus used in spell checking, hyphenation applications and longest prefix match algorithms.[7,17] However, if storing dictionary words is all that is required (i.e. there is no need to store metadata associated with each word), a minimal deterministic acyclic finite state automaton (DAFSA) or radix tree would use less storage space than a trie. This is because DAFSAs and radix trees can compress identical branches from the trie which correspond to the same suffixes (or parts) of different words being stored.

### Autocomplete

Tries can be used to return a list of keys with a given prefix. This can also be modified to allow for wildcards in the prefix search.

Python example:

### Sorting

Lexicographic sorting of a set of keys can be accomplished by building a trie from them, with the children of each node sorted lexicographically, and traversing it in pre-order, printing any values in either the interior nodes or in the leaf nodes.[18] This algorithm is a form of radix sort.[19]

A trie is the fundamental data structure of Burstsort, which (in 2007) was the fastest known string sorting algorithm due to its efficient cache use.[20] Now there are faster ones.[21]

### Full-text search

A special kind of trie, called a suffix tree, can be used to index all suffixes in a text in order to carry out fast full text searches.

References:
[1] Thue, Axel. (1912). Über die gegenseitige Lage gleicher Teile gewisser Zeichenreihen. Skrifter udgivne af Videnskabs-Selskabet i Christiania. https://archive.org/details/skrifterutgitavv121chri/page/n11/mode/2up
[2] Knuth, Donald. (1997). The Art of Computer Programming Volume 3: Sorting and Searching. Addison-Wesley.
[3] de la Briandais, René. (1959). File searching using variable length keys. https://pdfs.semanticscholar.org/3ce3/f4cc1c91d03850ed84ef96a08498e018d18f.pdf
[4] Brass, Peter. (8 September 2008). Advanced Data Structures. Cambridge University Press. doi:10.1017/CBO9780511800191
[5] Edward Fredkin. (1960). Trie Memory. Communications of the ACM. doi:10.1145/367390.367400
[6] Black, Paul E.. (2009-11-16). trie. Dictionary of Algorithms and Data Structures. https://xlinux.nist.gov/dads/HTML/trie.html
[7] Franklin Mark Liang. (1983). Word Hy-phen-a-tion By Com-put-er. Stanford University. http://www.tug.org/docs/liang/liang-thesis.pdf
[8] Sedgewick, Robert. (3 April 2011). Algorithms. Addison-Wesley, Princeton University. https://algs4.cs.princeton.edu/home/
[9] Allison, Lloyd. Tries. http://www.allisons.org/ll/AlgDS/Tree/Trie/
[10] Sahni, Sartaj. Tries. Data Structures, Algorithms, & Applications in Java. https://www.cise.ufl.edu/~sahni/dsaaj/enrich/c16/tries.htm
[11] Bellekens, Xavier. (2014). Proceedings of the 7th International Conference on Security of Information and Networks - SIN '14. ACM. doi:10.1145/2659651.2659723
[12] Lee, Doug. A Memory Allocator. http://gee.cs.oswego.edu/dl/html/malloc.html
[13] (2000). Incremental Construction of Minimal Acyclic Finite-State Automata. Computational Linguistics. doi:10.1162/089120100561601
[14] (2009). Tightly packed tries: how to fit large models into memory, and make them load fast, too. ACL Workshops: Proceedings of the Workshop on Software Engineering, Testing, and Quality Assurance for Natural Language Processing. http://www.aclweb.org/anthology/W/W09/W09-1505.pdf
[15] Askitis, Nikolas. (2008). B-tries for Disk-based String Management. VLDB Journal. http://people.eng.unimelb.edu.au/jzobel/fulltext/vldbj09.pdf
[16] Aho, Alfred V.. (Jun 1975). Efficient String Matching: An Aid to Bibliographic Search. Communications of the ACM. doi:10.1145/360825.360855
[17] Thareja, Reema. (13 October 2018). Data Structures Using C. Oxford University Press. https://global.oup.com/academic/product/data-structures-using-c-9780198099307
[18] Kärkkäinen, Juha. Lecture 2. University of Helsinki. https://www.cs.helsinki.fi/u/tpkarkka/opetus/12s/spa/lecture02.pdf
[19] Kallis, Rafael. (2018). The Adaptive Radix Tree (Report #14-708-887). University of Zurich: Department of Informatics, Research Publications. https://www.ifi.uzh.ch/dam/jcr:27d15f69-2a44-40f9-8b41-6d11b5926c67/ReportKallisMScBasis.pdf
[20] Ranjan Sinha and Justin Zobel and David Ring. (Feb 2006). Cache-Efficient String Sorting Using Copying. ACM Journal of Experimental Algorithmics. doi:10.1145/1187436.1187439
[21] J. Kärkkäinen and T. Rantala. (2008). String Processing and Information Retrieval, Proc. SPIRE. Springer. doi:10.1007/978-3-540-89097-3_3
````

</details>

<details><summary><b>Step 3 — late_revision</b> (2458 words)</summary>

````text
In computer science, a trie, also called digital tree or prefix tree, is a type of k-ary search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key.

Unlike a binary search tree, nodes in the trie do not store their associated key. Instead, a node's position in the trie defines the key with which it is associated. This distributes the value of each key across the data structure, and means that not every node necessarily has an associated value.

All the children of a node have a common prefix of the string associated with that parent node, and the root is associated with the empty string. This task of storing data accessible by its prefix can be accomplished in a memory-optimized way by employing a radix tree.

Though tries can be keyed by character strings, they need not be. The same algorithms can be adapted for ordered lists of any underlying type, e.g. permutations of digits or shapes. In particular, a bitwise trie is keyed on the individual bits making up a piece of fixed-length binary data, such as an integer or memory address.

## History, etymology, and pronunciation

The idea of a trie for representing a set of strings was first abstractly described by Axel Thue in 1912.[1,2] Tries were first described in a computer context by René de la Briandais in 1959.[3,2,4] The idea was independently described in 1960 by Edward Fredkin,[5] who coined the term trie, pronouncing it (as "tree"), after the middle syllable of retrieval.[6,7] However, other authors pronounce it (as "try"), in an attempt to distinguish it verbally from "tree".[6,7,2]

## Operations

Tries support various operations: insertion, deletion, and lookup of a string key. Tries are composed of \text{nodes} that contain links that are either references to other child suffix child nodes, or \text{nil} . Except for root, each node is pointed to by just one other node, called the parent. Each node contains \text{R} links, where \text{R} is the cardinality of the set of alphabets, although tries have a substantial number of \text{nil} links. In most cases, the size of \text{Children} array is bitlength of the character encoding - 256 in the case of (unsigned) ASCII.[8]

The \text{nil} links within \text{Children} in \text{Node} emphasizes the following characteristics:

Characters and string keys are implicitly stored in the trie data structure representation, and include a character sentinel value indicating string-termination.

Each node contains one possible link to a prefix of strong keys of the set.

A basic structure type of nodes in the trie is as follows; \text{Node} may contain an optional \text{Value} , which is associated with each key stored in the last character of string, or terminal node.

### Searching

Searching a \text{Value} in a trie is guided by the characters in the search string key, as each node in the trie contains a corresponding link to each possible character in the given string. Thus, following the string within the trie yields the associated \text{Value} for the given string key. A \text{nil} link within search execution indicates the inexistence of the key.

Following pseudocode implements the search procedure for a given string key ( \text{key} ) in a rooted trie ( \text{x} ).[9]

In the above pseudocode, \text{x} and \text{key} correspond to the pointer of trie's root node and the string key respectively. The search operation, in a standard trie, takes O(\text{dm}) , \text{m} is the size of the string parameter \text{key} , and \text{d} corresponds to the alphabet size.[10] binary search trees, on the other hand, take O(m \log n) on the worst case, since the search depends on the height of the tree ( \log n ) of the BST (in case of balanced trees), where \text{n} and \text{m} being number of keys and the length of the keys; tries occupy less space in comparison with BST if it encompasses a large number of short strings, since nodes share common initial string subsequences and stores the keys implicitly on the structure. The terminal node of the tree contains a non-nil \text{Value} , and it's a search hit if the associated value is found in the trie, and search miss if it isn't.

### Insertion

Insertion into trie is guided by using the character sets as the indexes into the \text{Children} array until last character of the string key is reached. Each node in the trie corresponds to one call of the radix sorting routine, as the trie structure reflects the execution of patten of the top-down radix sort.

If a \text{nil} link is encountered prior to reaching the last character of the string key, a new \text{Node} is created, such along lines 3-5. \text{x.Value} gets assigned to input \text{value} ; if \text{x.Value} wasn't \text{nil} at the time of insertion, the value associated with the given string key gets substituted with the current one.

### Deletion

Deletion of a key-value pair from a trie involves finding the terminal node with the corresponding string key, marking the terminal indicator and value to false and \text{nil} correspondingly.

Following is a recursive procedure for removing a string key ( \text{key} ) from rooted trie ( \text{x} ).

The procedures begins by examining the \text{key} ; \text{nil} denotes the arrival of a terminal node or end of string key. If terminal, the node gets removed from the trie (line 9 assign the character index to \text{nil} ). However, an end of string key without the node being terminal indicates that the key doesn't exist, thus the procedure doesn't modify the trie. The recursion proceeds by incrementing \text{key} 's index.

## Replacing other data structures

### Replacement for hash tables

A trie can be used to replace a hash table, over which it has the following advantages:

Searching for a node with an associated key of size m has the complexity of O(m) , whereas an imperfect hash function may have numerous colliding keys, and the worst-case lookup speed of such a table would be O(N) , where N denotes the total number of nodes within the table.

Tries do not need a hash function for the operation, unlike a hash table; there are also no collisions of different keys in a trie.

Buckets in a trie, which are analogous to hash table buckets that store key collisions, are necessary only if a single key is associated with more than one value.

String keys within the trie can be sorted using a predetermined alphabetical ordering.

However, tries are less efficient than a hash table when the data is directly accessed on a secondary storage device such as a hard disk drive that has higher random access time than the main memory.[5] Tries are also disadvantageous when the key value cannot be easily represented as string, such as floating point numbers where multiple representations are possible (e.g. 1 is equivalent to 1.0, +1.0, 1.00, etc.), however it can be disambigiously represented as a binary number in IEEE 754 format.

### DFSA representation

A trie can be seen as a tree-shaped deterministic finite automaton. Each finite language is generated by a trie automaton, and each trie can be compressed into a deterministic acyclic finite state automaton.[11]

## Implementation strategies

Tries can be represented in several ways, corresponding to different trade-offs between memory use and speed of the operations. Using a vector for representing a trie consumes enormous space; however, memory space can be reduced at the expense of running time if a singly linked list is used for each node vector, as most entries of the vector contains \text{nil} .

Techniques such as alphabet reduction may alleviate the high space complexity by reinterpreting the original string as a long string over a smaller alphabet i.e. a string of n bytes can alternatively be regarded as a string of 2n four-bit units and stored in a trie with sixteen pointers per node. However, lookups need to visit twice as many nodes in the worst-case, although space requirements go down by a factor of eight. Other techniques include storing a vector of 256 ASCII pointers as a bitmap of 256 bits representing ASCII alphabet, which reduces the size of individual nodes dramatically.[12]

### Bitwise tries

Bitwise tries are used to address the enormous space requirement for the trie nodes in the simple pointer vector implementations. Each character in the string key set is represented via individual bits, which are used to traverse the trie over a string key. The implementations for these types of trie use vectorized CPU instructions to find the first set bit in a fixed-length key input (e.g. GCC's __builtin_clz() intrinsic function). Accordingly, the set bit is used to index the first item, or child node, in the 32- or 64-entry based bitwise tree. Search then proceeds by testing each subsequent bit in the key.[13]

This procedure is also cache-local and highly parallelizable due to register independency, and thus performant on out-of-order execution CPUs.

### Compressed tries

Radix tree, also known as a compressed trie, is a space-optimized variant of a trie in which nodes with only one child get merged with its parents; elimination of branches of the nodes with a single child results in better in both space and time metrics.[14] This works best under the following conditions where the trie remains static and set of keys stored are very sparse within their representation space.[15]

One more approach is to "pack" the trie, in which a space-efficient implementation of a sparse packed trie applied to automatic hyphenation, in which the descendants of each node may be interleaved in memory.[7]

### External memory tries

Several trie variants are suitable for maintaining sets of strings in external memory, including suffix trees. A combination of trie and B-tree, called the B-trie has also been suggested for this task; compared to suffix trees, they are limited in the supported operations but also more compact while performing update operations faster.[16]

## Applications

Trie data structures are commonly used in predictive text or autocomplete dictionaries, and approximate matching algorithms.[17] Tries enable faster searches, occupy less space, especially when the set contains large number of short strings, thus used in spell checking, hyphenation applications and longest prefix match algorithms.[7,18] However, if storing dictionary words is all that is required (i.e. there is no need to store metadata associated with each word), a minimal deterministic acyclic finite state automaton (DAFSA) or radix tree would use less storage space than a trie. This is because DAFSAs and radix trees can compress identical branches from the trie which correspond to the same suffixes (or parts) of different words being stored. String dictionaries are also utilized in natural language processing, such as finding lexicon of a text corpus.[19]

### Sorting

Lexicographic sorting of a set of string keys can be implemented by building a trie for the given keys and traversing the tree in pre-order fashion;[20] this is also a form of radix sort.[21] Tries are also fundamental data structures for burstsort, which is notable for being the fastest string sorting algorithm as of 2007,[22] which is accompanied for its efficient use of CPU cache.[23]

### Full-text search

A special kind of trie, called a suffix tree, can be used to index all suffixes in a text to carry out fast full-text searches.[24]

### Web search engines

A specialized kind of trie called a compressed trie, is used in web search engines for storing the indexes - a collection of all searchable words. Each terminal node is associated with a list of URLs—called occurrence list—to pages that match the keyword. The trie is stored in the main memory, whereas the occurrence is kept in an external storage, frequently in large clusters.

### Bioinformatics

Tries are used in Bioinformatics, notably in sequence alignment software applications such as BLAST, which indexes all the different substring of length k (called k-mers) of a text by storing the positions of their occurrences in a compressed trie sequence databases.

### Internet routing

Compressed variants of tries, such as databases for managing Forwarding Information Base (FIB), are used in storing IP address prefixes within routers and bridges for prefix-based lookup to resolve mask-based operations in IP routing.

References:
[1] Thue, Axel. (1912). Über die gegenseitige Lage gleicher Teile gewisser Zeichenreihen. Skrifter Udgivne Af Videnskabs-Selskabet I Christiania. https://archive.org/details/skrifterutgitavv121chri/page/n11/mode/2up
[2] Knuth, Donald. (1997). The Art of Computer Programming Volume 3: Sorting and Searching. Addison-Wesley.
[3] de la Briandais, René. (1959). File searching using variable length keys. doi:10.1145/1457838.1457895
[4] Brass, Peter. (8 September 2008). Advanced Data Structures. Cambridge University Press. doi:10.1017/CBO9780511800191
[5] Edward Fredkin. (1960). Trie Memory. Communications of the ACM. doi:10.1145/367390.367400
[6] Black, Paul E.. (2009-11-16). trie. Dictionary of Algorithms and Data Structures. https://xlinux.nist.gov/dads/HTML/trie.html
[7] Franklin Mark Liang. (1983). Word Hy-phen-a-tion By Com-put-er. Stanford University. http://www.tug.org/docs/liang/liang-thesis.pdf
[8] Sedgewick, Robert. (3 April 2011). Algorithms. Addison-Wesley, Princeton University. https://algs4.cs.princeton.edu/home/
[9] Gonnet, Gaston H.. (1 May 1991). Handbook of Algorithms and Data Structures in Pascal and C. Addison-Wesley, ETH Zurich. https://dl.acm.org/doi/book/10.5555/103324
[10] Patil, Virsha H.. (10 May 2012). Data Structures using C++. Oxford University Press. https://global.oup.com/academic/product/data-structures-using-c-9780198066231?cc=ca&lang=en&
[11] Daciuk, Jan. (24 June 2003). Comparison of Construction Algorithms for Minimal, Acyclic, Deterministic, Finite-State Automata from Sets of Strings. Springer Publishing. doi:10.1007/3-540-44977-9_26
[12] Bellekens, Xavier. (2014). Proceedings of the 7th International Conference on Security of Information and Networks - SIN '14. ACM. doi:10.1145/2659651.2659723
[13] Willar, Dan E.. (27 January 1983). Log-logarithmic worst-case range queries are possible in space O(n). Information Processing Letters. doi:10.1016/0020-0190(83)90075-3
[14] Mehta, Dinesh P.. (7 March 2018). Handbook of Data Structures and Applications. Chapman & Hall, University of Florida. https://www.routledge.com/Handbook-of-Data-Structures-and-Applications/Mehta-Sahni/p/book/9780367572006
[15] (1 March 2000). Incremental Construction of Minimal Acyclic Finite-State Automata. Computational Linguistics. doi:10.1162/089120100561601
[16] Askitis, Nikolas. (2008). B-tries for Disk-based String Management. VLDB Journal. http://people.eng.unimelb.edu.au/jzobel/fulltext/vldbj09.pdf
[17] Aho, Alfred V.. (Jun 1975). Efficient String Matching: An Aid to Bibliographic Search. Communications of the ACM. doi:10.1145/360825.360855
[18] Thareja, Reema. (13 October 2018). Data Structures Using C. Oxford University Press. https://global.oup.com/academic/product/data-structures-using-c-9780198099307
[19] Martinez-Prieto, Miguel A.. (March 2016). Practical compressed string dictionaries. Information Systems. doi:10.1016/j.is.2015.08.008
[20] Kärkkäinen, Juha. Lecture 2. University of Helsinki. https://www.cs.helsinki.fi/u/tpkarkka/opetus/12s/spa/lecture02.pdf
[21] Kallis, Rafael. (2018). The Adaptive Radix Tree (Report #14-708-887). University of Zurich: Department of Informatics, Research Publications. https://www.ifi.uzh.ch/dam/jcr:27d15f69-2a44-40f9-8b41-6d11b5926c67/ReportKallisMScBasis.pdf
[22] Ranjan Sinha and Justin Zobel and David Ring. (Feb 2006). Cache-Efficient String Sorting Using Copying. ACM Journal of Experimental Algorithmics. doi:10.1145/1187436.1187439
[23] J. Kärkkäinen and T. Rantala. (2008). String Processing and Information Retrieval, Proc. SPIRE. Springer. doi:10.1007/978-3-540-89097-3_3
[24] Giancarlo, Raffaele. (28 May 1992). A Generalization of the Suffix Tree to Square Matrices, with Applications. SIAM Journal on Computing. doi:10.1137/S0097539792231982
````

</details>

<details><summary><b>Step 4 — final</b> (2498 words)</summary>

````text
In computer science, a trie (, ), also known as a digital tree or prefix tree,[1] is a specialized search tree data structure used to store and retrieve strings from a dictionary or set. Unlike a binary search tree, nodes in a trie do not store their associated key. Instead, each node's position within the trie determines its associated key, with the connections between nodes defined by individual characters rather than the entire key.

Tries are particularly effective for tasks such as autocomplete, spell checking, and IP routing, offering advantages over hash tables due to their prefix-based organization and lack of hash collisions. Every child node shares a common prefix with its parent node, and the root node represents the empty string. While basic trie implementations can be memory-intensive, various optimization techniques such as compression and bitwise representations have been developed to improve their efficiency. A notable optimization is the radix tree, which provides more efficient prefix-based storage.

While tries store character strings, they can be adapted to work with any ordered sequence of elements, such as permutations of digits or shapes. A notable variant is the bitwise trie, which uses individual bits from fixed-length binary data (such as integers or memory addresses) as keys.

## History, etymology, and pronunciation

The idea of a trie for representing a set of strings was first abstractly described by Axel Thue in 1912.[2,3] Tries were first described in a computer context by René de la Briandais in 1959.[4,3,5]

The idea was independently described in 1960 by Edward Fredkin,[6] who coined the term trie, pronouncing it (as "tree"), after the middle syllable of retrieval.[7,8] However, other authors pronounce it (as "try"), in an attempt to distinguish it verbally from "tree".[7,8,3]

## Overview

Tries are a form of string-indexed look-up data structure, which is used to store a dictionary list of words that can be searched on in a manner that allows for efficient generation of completion lists.[9,10] A prefix trie is an ordered tree data structure used in the representation of a set of strings over a finite alphabet set, which allows efficient storage of words with common prefixes.[1]

Tries can be efficacious on string-searching algorithms such as predictive text, approximate string matching, and spell checking in comparison to binary search trees.[11,8] A trie can be seen as a tree-shaped deterministic finite automaton.[12]

## Operations

Tries support various operations: insertion, deletion, and lookup of a string key. Tries are composed of nodes that contain links, which either point to other suffix child nodes or null. As for every tree, each node except the root is pointed to by only one other node, called its parent. Each node contains as many links as the number of characters in the applicable alphabet (although tries tend to have a substantial number of null links). In some cases, the alphabet used is simply that of the character encoding—resulting in, for example, a size of 128 in the case of ASCII.[13]

The null links within the children of a node emphasize the following characteristics:

Characters and string keys are implicitly stored in the trie, and include a character sentinel value indicating string termination.

Each node contains one possible link to a prefix of strong keys of the set.

A basic structure type of nodes in the trie is as follows: \text{Node} may contain an optional \text{Value} , which is associated with the key that corresponds to the node.

### Searching

Searching for a value in a trie is guided by the characters in the search string key, as each node in the trie contains a corresponding link to each possible character in the given string. Thus, following the string within the trie yields the associated value for the given string key. A null link during the search indicates the inexistence of the key.

The following pseudocode implements the search procedure for a given string in a rooted trie .

In the above pseudocode, and correspond to the pointer of the trie's root node and the string key, respectively. The search operation takes O(m) time, where m is the size of the string parameter . In a balanced binary search tree, on the other hand, it takes O(m \log n) time, in the worst case, since needs to be compared with O(\log n) other keys and each comparison takes O(m) time, in the worst case.

The trie occupies less space, in comparison with a binary search tree, in the case of a large number of short strings, since nodes share common initial string subsequences and store the keys implicitly.

### Insertion

Insertion into a trie is guided by using the character sets as indexes to the children array until the last character of the string key is reached. Each node in the trie corresponds to one call of the radix sorting routine, as the trie structure reflects the execution pattern of the top-down radix sort.

If null links are encountered before reaching the last character of the string key, new nodes are created. The input value is assigned to the value of the last node traversed, which is the node that corresponds to the key.

### Deletion

Deletion of a key–value pair from a trie involves finding the node corresponding to the key, setting its value to null, and recursively removing nodes that have no children.

The procedure begins by examining ; an empty string indicates arrival at the node corresponding to the (original) key, in which case its value is set to null. If the node, then, has null value and no children, it is removed from the trie by returning null; otherwise, the node is kept by returning the node itself.

## Replacing other data structures

### Replacement for hash tables

A trie can be used to replace a hash table, over which it has the following advantages:

Searching for a node with an associated key of size m has the complexity of O(m) , whereas an imperfect hash function may have numerous colliding keys, and the worst-case lookup speed of such a table would be O(N) , where N denotes the total number of nodes within the table.

Tries do not need a hash function for the operation, unlike a hash table; there are also no collisions of different keys in a trie.

Within a trie, keys can be efficiently sorted lexicographically.

However, tries are less efficient than a hash table when the data is directly accessed on a secondary storage device such as a hard disk drive that has higher random access time than the main memory.[6]

## Implementation strategies

Tries can be represented in several ways, corresponding to different trade-offs between memory use and speed of the operations. Using a vector of pointers for representing a trie consumes enormous space; however, memory space can be reduced at the expense of running time if a singly linked list is used for each node vector, as most entries of the vector contains \text{nil} .

Techniques such as alphabet reduction may reduce the large space requirements by reinterpreting the original string as a longer string over a smaller alphabet. For example, a string of n bytes can alternatively be regarded as a string of 2n four-bit units. This can reduce memory usage by a factor of eight; but lookups need to visit twice as many nodes in the worst case. Another technique includes storing a vector of 256 ASCII pointers as a bitmap of 256 bits representing ASCII alphabet, which reduces the size of individual nodes dramatically.[14]

### Bitwise tries

Bitwise tries are used to address the enormous space requirement for the trie nodes in a naive simple pointer vector implementations. Each character in the string key set is represented via individual bits, which are used to traverse the trie over a string key. The implementations for these types of trie use vectorized CPU instructions to find the first set bit in a fixed-length key input (e.g. GCC's __builtin_clz() intrinsic function). Accordingly, the set bit is used to index the first item, or child node, in the 32- or 64-entry based bitwise tree. Search then proceeds by testing each subsequent bit in the key.[15]

This procedure is also cache-local and highly parallelizable due to register independency, and thus performant on out-of-order execution CPUs.[15]

### Compressed tries

Radix tree, also known as a compressed trie, is a space-optimized variant of a trie in which any node with only one child gets merged with its parent; elimination of branches of the nodes with a single child results in better metrics in both space and time.[16,17] This works best when the trie remains static and set of keys stored are very sparse within their representation space.[18]

One more approach for static tries is to "pack" the trie by storing disjoint sets of children in the same memory location, interleaved.[8]

### Patricia trees

Patricia trees are a particular implementation of the compressed binary trie that uses the binary encoding of the string keys in its representation.[19,20] Every node in a Patricia tree contains an index, known as a "skip number", that stores the node's branching index to avoid empty subtrees during traversal. A naive implementation of a trie consumes immense storage due to larger number of leaf-nodes caused by the sparse distribution of keys; Patricia trees can be efficient for such cases.

A representation of a Patricia tree is shown to the right. Each index value adjacent to the nodes represents the "skip number"—the index of the bit with which branching is to be decided.[21] The skip number 1 at node 0 corresponds to the position 1 in the binary encoded ASCII where the leftmost bit differed in the key set X. The skip number is crucial for search, insertion, and deletion of nodes in the Patricia tree, and a bit masking operation is performed during every iteration.

## Applications

Trie data structures are commonly used in predictive text or autocomplete dictionaries, and approximate matching algorithms.[11] Tries enable faster searches, occupy less space, especially when the set contains large number of short strings, thus used in spell checking, hyphenation applications and longest prefix match algorithms.[8,22] However, if storing dictionary words is all that is required (i.e. there is no need to store metadata associated with each word), a minimal deterministic acyclic finite state automaton (DAFSA) or radix tree would use less storage space than a trie. This is because DAFSAs and radix trees can compress identical branches from the trie that correspond to the same suffixes (or parts) of different words being stored. String dictionaries are also utilized in natural language processing, such as finding lexicon of a text corpus.[23]

### Sorting

Lexicographic sorting of a set of string keys can be implemented by building a trie for the given keys and traversing the tree in pre-order fashion;[24] this is also a form of radix sort.[25] Tries are also fundamental data structures for burstsort, which is notable for being the fastest string sorting algorithm as of 2007,[26] accomplished by its efficient use of CPU cache.[27]

### Full-text search

A special kind of trie, called a suffix tree, can be used to index all suffixes in a text to carry out fast full-text searches.[28]

### Web search engines

A specialized kind of trie called a compressed trie, is used in web search engines for storing the indexes - a collection of all searchable words.[29] Each terminal node is associated with a list of URLs—called occurrence list—to pages that match the keyword. The trie is stored in the main memory, whereas the occurrence is kept in an external storage, frequently in large clusters, or the in-memory index points to documents stored in an external location.[30]

### Bioinformatics

Tries are used in Bioinformatics, notably in sequence alignment software applications such as BLAST, which indexes all the different substrings of length k (called k-mers) of a text by storing the positions of their occurrences in a compressed trie sequence databases.

### Internet routing

Compressed variants of tries, such as databases for managing Forwarding Information Base (FIB), are used in storing IP address prefixes within routers and bridges for prefix-based lookup to resolve mask-based operations in IP routing.

References:
[1] Maabar, Maha. (17 November 2014). Trie Data Structure. CVR, University of Glasgow. https://bioinformatics.cvr.ac.uk/trie-data-structure/
[2] Thue, Axel. (1912). Über die gegenseitige Lage gleicher Teile gewisser Zeichenreihen. Skrifter Udgivne Af Videnskabs-Selskabet I Christiania. https://archive.org/details/skrifterutgitavv121chri/page/n11/mode/2up
[3] Knuth, Donald. (1997). The Art of Computer Programming Volume 3: Sorting and Searching. Addison-Wesley.
[4] de la Briandais, René. (1959). File searching using variable length keys. doi:10.1145/1457838.1457895
[5] Brass, Peter. (8 September 2008). Advanced Data Structures. Cambridge University Press. doi:10.1017/CBO9780511800191
[6] Edward Fredkin. (1960). Trie Memory. Communications of the ACM. doi:10.1145/367390.367400
[7] Black, Paul E.. (2009-11-16). trie. Dictionary of Algorithms and Data Structures. https://xlinux.nist.gov/dads/HTML/trie.html
[8] Franklin Mark Liang. (1983). Word Hy-phen-a-tion By Com-put-er. Stanford University. http://www.tug.org/docs/liang/liang-thesis.pdf
[9] (2022). Trie. School of Arts and Science, Rutgers University. https://ds.cs.rutgers.edu/assignment-trie/
[10] Connelly, Richard H.. (1993). A generalization of the trie data structure. Mathematical Structures in Computer Science. doi:10.1017/S0960129500000803
[11] Aho, Alfred V.. (Jun 1975). Efficient String Matching: An Aid to Bibliographic Search. Communications of the ACM. doi:10.1145/360825.360855
[12] Daciuk, Jan. (24 June 2003). Comparison of Construction Algorithms for Minimal, Acyclic, Deterministic, Finite-State Automata from Sets of Strings. Springer Publishing. doi:10.1007/3-540-44977-9_26
[13] Sedgewick, Robert. (3 April 2011). Algorithms. Addison-Wesley, Princeton University. https://algs4.cs.princeton.edu/home/
[14] Bellekens, Xavier. (2014). Proceedings of the 7th International Conference on Security of Information and Networks - SIN '14. ACM. doi:10.1145/2659651.2659723
[15] Willar, Dan E.. (27 January 1983). Log-logarithmic worst-case range queries are possible in space O(n). Information Processing Letters. doi:10.1016/0020-0190(83)90075-3
[16] Sartaj Sahni. (2004). Data Structures, Algorithms, & Applications in C++: Tries. University of Florida. https://www.cise.ufl.edu/~sahni/dsaac/enrich/c16/tries.htm
[17] Mehta, Dinesh P.. (7 March 2018). Handbook of Data Structures and Applications. Chapman & Hall, University of Florida. https://www.routledge.com/Handbook-of-Data-Structures-and-Applications/Mehta-Sahni/p/book/9780367572006
[18] (1 March 2000). Incremental Construction of Minimal Acyclic Finite-State Automata. Computational Linguistics. doi:10.1162/089120100561601
[19] Patricia tree. National Institute of Standards and Technology. https://xlinux.nist.gov/dads/HTML/patriciatree.html
[20] Gonnet, G. H.. (January 1991). Handbook of algorithms and data structures: in Pascal and C. Addison-Wesley. https://dl.acm.org/doi/book/10.5555/103324
[21] Crochemore, Maxime. (2009). Encyclopedia of Database Systems. Springer Publishing. doi:10.1007/978-0-387-39940-9
[22] Thareja, Reema. (13 October 2018). Data Structures Using C. Oxford University Press. https://global.oup.com/academic/product/data-structures-using-c-9780198099307
[23] Martinez-Prieto, Miguel A.. (March 2016). Practical compressed string dictionaries. Information Systems. doi:10.1016/j.is.2015.08.008
[24] Kärkkäinen, Juha. Lecture 2. University of Helsinki. https://www.cs.helsinki.fi/u/tpkarkka/opetus/12s/spa/lecture02.pdf
[25] Kallis, Rafael. (2018). The Adaptive Radix Tree (Report #14-708-887). University of Zurich: Department of Informatics, Research Publications. https://www.ifi.uzh.ch/dam/jcr:27d15f69-2a44-40f9-8b41-6d11b5926c67/ReportKallisMScBasis.pdf
[26] Ranjan Sinha and Justin Zobel and David Ring. (Feb 2006). Cache-Efficient String Sorting Using Copying. ACM Journal of Experimental Algorithmics. doi:10.1145/1187436.1187439
[27] J. Kärkkäinen and T. Rantala. (2008). String Processing and Information Retrieval, Proc. SPIRE. Springer. doi:10.1007/978-3-540-89097-3_3
[28] Giancarlo, Raffaele. (28 May 1992). A Generalization of the Suffix Tree to Square Matrices, with Applications. SIAM Journal on Computing. doi:10.1137/S0097539792231982
[29] Yang, Lai. (23 March 2012). An enhanced dynamic hash TRIE algorithm for lexicon search. Enterprise Information Systems. doi:10.1080/17517575.2012.665483
[30] Transier, Frederik. (December 2010). Engineering basic algorithms of an in-memory text search engine. ACM Transactions on Information Systems. doi:10.1145/1877766.1877768
````

</details>
