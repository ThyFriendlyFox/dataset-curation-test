# 9. Hash table — Hash function

`A-wiki_Hash_table` · [A_reconstructed_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Hash_table&oldid=1376684313> · License: https://creativecommons.org/licenses/by-sa/4.0/

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | prompt | 36 | 0 | 0.03 | reconstructed |
| 1 | outline | 352 | 0 | 0.38 | reconstructed |
| 2 | rough_draft | 618 | 0 | 0.66 | reconstructed |
| 3 | cited_draft | 896 | 8 | 0.87 | reconstructed |
| 4 | final | 892 | 8 | 1.00 | source |

<details><summary><b>Step 0 — prompt</b> (36 words)</summary>

````text
Write the "Hash function" section of the Wikipedia article on hash tables: what the hash function does in a table, the usual schemes for integer keys, hashing strings, and what matters when choosing a hash function.
````

</details>

<details><summary><b>Step 1 — outline</b> (352 words)</summary>

````text
- hash function h:U\rightarrow \{0,...,m-1\}: universe U of keys -> indices / slots of the table; h(x)\in \{0,...,m-1\} for x\in U
- conventional implementations: integer universe assumption — all elements from U=\{0,...,u-1\}, bit length of u within word size of the computer architecture
- perfect hash function for a set S: injective on S (each x\in S to a different value in {0,...,m-1})
- perfect hash possible if all keys known ahead of time

## Integer universe assumption
- schemes: hashing by division, by multiplication, universal hashing, dynamic perfect hashing, static perfect hashing
- division = the commonly used one

## Hashing by division
- h(x)\ =\ x\,{\bmod {\,}}m; h(x) = hash value of x\in S, m = table size

## Hashing by multiplication
- h(x)=\lfloor m{\bigl (}(xA){\bmod {1}}{\bigr)}\rfloor; A non-integer real-valued constant, m table size
- advantage: m not critical
- any A works; Donald Knuth suggests golden ratio

## String hashing
- strings commonly used as keys
- The C++ Programming Language (3rd ed.): unsigned int starting at zero, left shift one bit, xor with integer value of next character; result modulo table size
- non-circular shift: string length at least eight bits less than size of the unsigned int in bits
- alternative: polynomial rolling hash function

## Choosing a hash function
- uniform distribution of hash values = fundamental requirement
- non-uniform -> more collisions, higher cost of resolving them
- hard to ensure by design; evaluate empirically with statistical tests, e.g. Pearson's chi-squared test for discrete uniform distributions
- uniformity only needed for table sizes that occur in the application
  - dynamic resizing, exact doubling/halving -> only power-of-two sizes; index = range of bits of the hash
  - some hashing algorithms prefer prime sizes
- open addressing: avoid runs (two or more keys -> consecutive slots); lookup cost can skyrocket even with low load factor and infrequent collisions
- popular multiplicative hash claimed to have particularly poor run behavior
- K-independent hashing: prove no bad keysets for a given type of hashtable
  - results known for linear probing, cuckoo hashing
  - then focus on fastest such function
````

</details>

<details><summary><b>Step 2 — rough_draft</b> (618 words)</summary>

````text
A hash function h:U\rightarrow \{0,...,m-1\} maps the universe U of keys to indices or slots in the table, which means h(x)\in \{0,...,m-1\} for x\in U. Conventional implementations of hash functions are based on the integer universe assumption, which is that all the elements of the table come from the universe U=\{0,...,u-1\}, where the bit length of u is confined within the word size of a computer architecture.

A hash function h is called perfect for a given set S if it is injective on S, which means that each element x\in S maps to a different value in {0,...,m-1}. If all of the keys are known ahead of time, a perfect hash function can be created.

## Integer universe assumption

There are several hashing schemes that are used under the integer universe assumption: hashing by division, hashing by multiplication, universal hashing, dynamic perfect hashing, and static perfect hashing. But hashing by division is the scheme that is commonly used.

## Hashing by division

In hashing by division the scheme is: h(x)\ =\ x\,{\bmod {\,}}m, where h(x) is the hash value of x\in S and m is the size of the table.

## Hashing by multiplication

In hashing by multiplication the scheme is: h(x)=\lfloor m{\bigl (}(xA){\bmod {1}}{\bigr)}\rfloor where A is a non-integer real-valued constant and m is the size of the table. One advantage of hashing by multiplication is that m is not critical. Any value A produces a hash function, but Donald Knuth suggests using the golden ratio.

## String hashing

A string is commonly used as the key to the hash function. The third edition of The C++ Programming Language describes a simple hash function where an unsigned integer that starts at zero is repeatedly left shifted one bit and then xor'ed with the integer value of the next character, and then this hash value is taken modulo the table size. If the left shift is not circular, the string length should be at least eight bits less than the size of the unsigned integer in bits. A polynomial rolling hash function is another common way to hash a string to an integer.

## Choosing a hash function

A fundamental requirement of a hash function is uniform distribution of the hash values. If the distribution is not uniform, the number of collisions goes up and so does the cost of resolving them. It is sometimes hard to ensure uniformity by design, but it can be evaluated empirically with statistical tests, e.g., a Pearson's chi-squared test for discrete uniform distributions.

The distribution only has to be uniform for the table sizes that occur in the application. In particular, if dynamic resizing is used with exact doubling and halving of the table size, then the hash function only needs to be uniform when the size is a power of two. In that case the index can be computed as some range of bits of the hash function. On the other hand some hashing algorithms prefer the size to be a prime number.

For open addressing schemes the hash function should also avoid runs, which is the mapping of two or more keys to consecutive slots. Runs like this may cause the lookup cost to skyrocket, even when the load factor is low and collisions are infrequent. The popular multiplicative hash is claimed to have particularly poor run behavior.

K-independent hashing gives a way to prove that a certain hash function does not have bad keysets for a given type of hashtable. A number of K-independence results are known for collision resolution schemes like linear probing and cuckoo hashing. Since K-independence can prove that a hash function works, one can then focus on finding the fastest possible such hash function.
````

</details>

<details><summary><b>Step 3 — cited_draft</b> (896 words)</summary>

````text
A hash function h:U\rightarrow \{0,...,m-1\} maps the universe U of keys to indices or slots in the table, which means h(x)\in \{0,...,m-1\} for x\in U. Conventional implementations of hash functions are based on the integer universe assumption, which is that all the elements of the table come from the universe U=\{0,...,u-1\}, where the bit length of u is confined within the word size of a computer architecture.

A hash function h is called perfect for a given set S if it is injective on S, which means that each element x\in S maps to a different value in {0,...,m-1}. [1,2] If all of the keys are known ahead of time, a perfect hash function can be created. [1]

## Integer universe assumption

There are several hashing schemes that are used under the integer universe assumption: hashing by division, hashing by multiplication, universal hashing, dynamic perfect hashing, and static perfect hashing. But hashing by division is the scheme that is commonly used. [3]

## Hashing by division

In hashing by division the scheme is: h(x)\ =\ x\,{\bmod {\,}}m, where h(x) is the hash value of x\in S and m is the size of the table.

## Hashing by multiplication

In hashing by multiplication the scheme is: h(x)=\lfloor m{\bigl (}(xA){\bmod {1}}{\bigr)}\rfloor where A is a non-integer real-valued constant and m is the size of the table. One advantage of hashing by multiplication is that m is not critical. Any value A produces a hash function, but Donald Knuth suggests using the golden ratio.

## String hashing

A string is commonly used as the key to the hash function. The third edition of The C++ Programming Language describes a simple hash function where an unsigned integer that starts at zero is repeatedly left shifted one bit and then xor'ed with the integer value of the next character, and then this hash value is taken modulo the table size. [4] If the left shift is not circular, the string length should be at least eight bits less than the size of the unsigned integer in bits. A polynomial rolling hash function is another common way to hash a string to an integer.

## Choosing a hash function

A fundamental requirement of a hash function is uniform distribution of the hash values. If the distribution is not uniform, the number of collisions goes up and so does the cost of resolving them. It is sometimes hard to ensure uniformity by design, but it can be evaluated empirically with statistical tests, e.g., a Pearson's chi-squared test for discrete uniform distributions. [5,6]

The distribution only has to be uniform for the table sizes that occur in the application. In particular, if dynamic resizing is used with exact doubling and halving of the table size, then the hash function only needs to be uniform when the size is a power of two. In that case the index can be computed as some range of bits of the hash function. On the other hand some hashing algorithms prefer the size to be a prime number. [7]

For open addressing schemes the hash function should also avoid runs, which is the mapping of two or more keys to consecutive slots. Runs like this may cause the lookup cost to skyrocket, even when the load factor is low and collisions are infrequent. The popular multiplicative hash is claimed to have particularly poor run behavior. [7,8]

K-independent hashing gives a way to prove that a certain hash function does not have bad keysets for a given type of hashtable. A number of K-independence results are known for collision resolution schemes like linear probing and cuckoo hashing. Since K-independence can prove that a hash function works, one can then focus on finding the fastest possible such hash function. [9]

References:
[1] Lu, Yi; Prabhakar, Balaji; Bonomi, Flavio (2006). Perfect Hashing for Network Applications. 2006 IEEE International Symposium on Information Theory. pp. 2774– 2778. doi: 10.1109/ISIT.2006.261567. ISBN 1-4244-0505-X. S2CID 1494710.
[2] Belazzougui, Djamal; Botelho, Fabiano C.; Dietzfelbinger, Martin (2009). "Hash, displace, and compress" (PDF). Algorithms—ESA 2009: 17th Annual European Symposium, Copenhagen, Denmark, September 7–9, 2009, Proceedings. Lecture Notes in Computer Science. Vol. 5757. Berlin: Springer. pp. 682– 693. CiteSeerX 10.1.1.568.130. doi: 10.1007/978-3-642-04128-0_61. MR 2557794. {{ cite conference }}: Cite uses deprecated parameter | citeseerx= (help)
[3] Owolabi, Olumide (February 2003). "Empirical studies of some hashing functions". Information and Software Technology. 45 (2): 109– 112. doi: 10.1016/S0950-5849(02)00174-X.
[4] Stroustrup, Bjarne (1997). The C++ Programming Language Third Edition. Reading Massachusetts: Addison-Wesley. p. 503. ISBN 0-201-88954-4.
[5] Pearson, Karl (1900). "On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling". Philosophical Magazine. Series 5. 50 (302): 157– 175. doi: 10.1080/14786440009463897.
[6] Plackett, Robin (1983). "Karl Pearson and the Chi-Squared Test". International Statistical Review. 51 (1): 59– 72. doi: 10.2307/1402731. JSTOR 1402731.
[7] Wang, Thomas (March 1997). "Prime Double Hash Table". Archived from the original on September 3, 1999. Retrieved May 10, 2015.
[8] Knuth, Donald E. (April 24, 1998). The Art of Computer Programming: Volume 3: Sorting and Searching (2nd ed.). Addison-Wesley Professional. ISBN 978-0-201-89685-5.
[9] Wegman, Mark N.; Carter, J.Lawrence (June 1981). "New hash functions and their use in authentication and set equality". Journal of Computer and System Sciences. 22 (3): 265– 279. Bibcode: 1981JCoSS..22..265W. doi: 10.1016/0022-0000(81)90033-7.
````

</details>

<details><summary><b>Step 4 — final</b> (892 words)</summary>

````text
A hash function h:U\rightarrow \{0,...,m-1\} maps the universe U of keys to indices or slots within the table, that is, h(x)\in \{0,...,m-1\} for x\in U. The conventional implementations of hash functions are based on the integer universe assumption that all elements of the table stem from the universe U=\{0,...,u-1\}, where the bit length of u is confined within the word size of a computer architecture.: 2

A hash function h is said to be perfect for a given set S if it is injective on S, that is, if each element x\in S maps to a different value in {0,...,m-1}. [1,2] A perfect hash function can be created if all the keys are known ahead of time. [1]

## Integer universe assumption

The schemes of hashing used in integer universe assumption include hashing by division, hashing by multiplication, universal hashing, dynamic perfect hashing, and static perfect hashing.: 2 However, hashing by division is the commonly used scheme.: 264 [3]: 110

## Hashing by division

The scheme in hashing by division is as follows:: 2 h(x)\ =\ x\,{\bmod {\,}}m, where h(x) is the hash value of x\in S and m is the size of the table.

## Hashing by multiplication

The scheme in hashing by multiplication is as follows:: 2–3 h(x)=\lfloor m{\bigl (}(xA){\bmod {1}}{\bigr)}\rfloor Where A is a non-integer real-valued constant and m is the size of the table. An advantage of the hashing by multiplication is that the m is not critical.: 2–3 Although any value A produces a hash function, Donald Knuth suggests using the golden ratio.: 3

## String hashing

Commonly a string is used as a key to the hash function. The third edition of The C++ Programming Language describes a simple hash function in which an unsigned integer that is initially zero is repeatedly left shifted one bit and then xor'ed with the integer value of the next character. This hash value is then taken modulo the table size. [4] If the left shift is not circular, then the string length should be at least eight bits less than the size of the unsigned integer in bits. Another common way to hash a string to an integer is with a polynomial rolling hash function.

## Choosing a hash function

Uniform distribution of the hash values is a fundamental requirement of a hash function. A non-uniform distribution increases the number of collisions and the cost of resolving them. Uniformity is sometimes difficult to ensure by design, but may be evaluated empirically using statistical tests, e.g., a Pearson's chi-squared test for discrete uniform distributions. [5,6]

The distribution needs to be uniform only for table sizes that occur in the application. In particular, if one uses dynamic resizing with exact doubling and halving of the table size, then the hash function needs to be uniform only when the size is a power of two. Here the index can be computed as some range of bits of the hash function. On the other hand, some hashing algorithms prefer to have the size be a prime number. [7]

For open addressing schemes, the hash function should also avoid runs, the mapping of two or more keys to consecutive slots. Such runs may cause the lookup cost to skyrocket, even if the load factor is low and collisions are infrequent. The popular multiplicative hash is claimed to have particularly poor run behavior. [7,8]

K-independent hashing offers a way to prove a certain hash function does not have bad keysets for a given type of hashtable. A number of K-independence results are known for collision resolution schemes such as linear probing and cuckoo hashing. Since K-independence can prove a hash function works, one can then focus on finding the fastest possible such hash function. [9]

References:
[1] Lu, Yi; Prabhakar, Balaji; Bonomi, Flavio (2006). Perfect Hashing for Network Applications. 2006 IEEE International Symposium on Information Theory. pp. 2774– 2778. doi: 10.1109/ISIT.2006.261567. ISBN 1-4244-0505-X. S2CID 1494710.
[2] Belazzougui, Djamal; Botelho, Fabiano C.; Dietzfelbinger, Martin (2009). "Hash, displace, and compress" (PDF). Algorithms—ESA 2009: 17th Annual European Symposium, Copenhagen, Denmark, September 7–9, 2009, Proceedings. Lecture Notes in Computer Science. Vol. 5757. Berlin: Springer. pp. 682– 693. CiteSeerX 10.1.1.568.130. doi: 10.1007/978-3-642-04128-0_61. MR 2557794. {{ cite conference }}: Cite uses deprecated parameter | citeseerx= (help)
[3] Owolabi, Olumide (February 2003). "Empirical studies of some hashing functions". Information and Software Technology. 45 (2): 109– 112. doi: 10.1016/S0950-5849(02)00174-X.
[4] Stroustrup, Bjarne (1997). The C++ Programming Language Third Edition. Reading Massachusetts: Addison-Wesley. p. 503. ISBN 0-201-88954-4.
[5] Pearson, Karl (1900). "On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling". Philosophical Magazine. Series 5. 50 (302): 157– 175. doi: 10.1080/14786440009463897.
[6] Plackett, Robin (1983). "Karl Pearson and the Chi-Squared Test". International Statistical Review. 51 (1): 59– 72. doi: 10.2307/1402731. JSTOR 1402731.
[7] Wang, Thomas (March 1997). "Prime Double Hash Table". Archived from the original on September 3, 1999. Retrieved May 10, 2015.
[8] Knuth, Donald E. (April 24, 1998). The Art of Computer Programming: Volume 3: Sorting and Searching (2nd ed.). Addison-Wesley Professional. ISBN 978-0-201-89685-5.
[9] Wegman, Mark N.; Carter, J.Lawrence (June 1981). "New hash functions and their use in authentication and set equality". Journal of Computer and System Sciences. 22 (3): 265– 279. Bibcode: 1981JCoSS..22..265W. doi: 10.1016/0022-0000(81)90033-7.
````

</details>
