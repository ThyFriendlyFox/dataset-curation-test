# 1. Bloom filter

`B-Bloom_filter` · [B_wiki_history_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Bloom_filter&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 1039 revisions in history; 39 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | revision_1 | 409 | 0 | 0.09 | enwiki rev 4516533 (2004-07-08) |
| 2 | revision_2 | 2037 | 0 | 0.22 | enwiki rev 30821141 (2005-12-10) |
| 3 | revision_3 | 3463 | 0 | 0.35 | enwiki rev 245166497 (2008-10-14) |
| 4 | revision_4 | 3441 | 8 | 0.49 | enwiki rev 516448269 (2012-10-07) |
| 5 | revision_5 | 4681 | 13 | 0.63 | enwiki rev 641921171 (2015-01-10) |
| 6 | revision_6 | 5404 | 12 | 0.75 | enwiki rev 860372364 (2018-09-20) |
| 7 | revision_7 | 6937 | 24 | 0.88 | enwiki rev 988592536 (2020-11-14) |
| 8 | final | 7564 | 38 | 1.00 | enwiki rev 1374211015 (2026-09-10) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Bloom filter
````

</details>

<details><summary><b>Step 1 — revision_1</b> (409 words)</summary>

````text
A Bloom filter is a probabilistic data structure that is used to test whether or not an element is a member of a set. False positives are possible, but false negatives are not. Elements can be added to the set, but not removed. The more elements that are added to the set, the larger the probability of false positives.

## Algorithm description

An empty Bloom filter is an array of k bits, all set to 0. There must also be m different hash functions defined, each of which maps an element to one of the k array positions.

To insert an element, feed it to each of the m hash functions to get m array positions. Set the bits at all these positions to 1.

To test membership of an element, feed it to each of the m hash functions to get m array positions. If any of the bits at these indices are 0, the element is not in the set – if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have been set to 1 during the insertion of other elements.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. The probability that a certain bit is not set to one by a certain hash function during the insertion of an element is then 1-1/k. The probability that it is not set by any of the hash functions is

\left(1-\frac{1}{k}\right)^m .

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{k}\right)^{mn} ;

the probability that it is 1 is therefore

1-\left(1-\frac{1}{k}\right)^{mn} .

Now test membership of an element that is not in the set. Each of the m array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is then

\left(1-\left(1-\frac{1}{k}\right)^{mn}\right)^m \approx \left(1-e^{-mn/k}\right)^m .

Obviously, the probability of false positives decreases as k (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases. For a given k and n, the value of m (the number of hash functions) that minimizes the probability is

\frac{k}{n}\ln 2 ,

which gives a probability of

\left(\frac{1}{2^{\ln 2}}\right)^{k/n} .
````

</details>

<details><summary><b>Step 2 — revision_2</b> (2037 words)</summary>

````text
The Bloom filter, conceived by Burton H. Bloom in 1970, is a space-efficient probabilistic data structure that is used to test whether or not an element is a member of a set. False positives are possible, but false negatives are not. Elements can be added to the set, but not removed (though this can be addressed with a counting filter). The more elements that are added to the set, the larger the probability of false positives.

For example, one might use a Bloom filter to do spell-checking in a space-efficient way. A Bloom filter to which a dictionary of correct words have been added will accept all words in the dictionary and reject almost all words which are not, which is good enough in some cases. Depending on the false positive rate, the resulting data structure can require as little as a byte per dictionary word. One peculiar attribute of this spell-checker is that it is not possible to extract the list of correct words from it – at best, one can extract a list containing the correct words plus a significant number of false positives.

## Algorithm description

An empty Bloom filter is a bit array of m bits, all set to 0. There must also be k different hash functions defined, each of which maps a key value to one of the m array positions.

For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields.

To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To query for an element (test whether it is in the set), feed it to each of the k hash functions to get k array positions. If any of the bits at these positions are 0, the element is not in the set – if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have been set to 1 during the insertion of other elements.

Unfortunately, removing an element from this simple Bloom filter is impossible. The element maps to k bits, and although setting any one of these k bits to zero suffices to remove it, this has the side effect of removing any other elements that map onto that bit, and we have no way of determining whether any such elements have been added. The result is a possibility of false negatives, which are not allowed.

## Space and time advantages

While risking false positives, Bloom filters have a strong space advantage over other data structures for representing sets such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings (tries are an exception, since they can share storage between elements with equal prefixes). Linked structures incur an additional linear space overhead for pointers. A Bloom filter with 1% error and an optimal value of k, on the other hand, requires only about 9.6 bits per element — regardless of the size of the elements! This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. If a 1% false positive rate seems too high, each time we add about 4.8 bits per element we decrease it by ten times.But the space advantage is not in good discusssion.

However, if the number of potential values is small and many of them can be in the set, then the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Note also that hash tables gain a space and time advantage if they begin ignoring collisions and only store whether each bucket contains an entry; in this case, they have effectively become Bloom filters with k = 1.

Bloom filters also have the unusual property that the time needed to either add items or to check whether an item is in the set is a fixed constant, O(k), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. The probability that a certain bit is not set to one by a certain hash function during the insertion of an element is then

1 − 1/m.

The probability that it is not set by any of the hash functions is

\left(1-\frac{1}{m}\right)^k .

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{m}\right)^{kn} ;

the probability that it is 1 is therefore

1-\left(1-\frac{1}{m}\right)^{kn} .

Now test membership of an element that is not in the set. Each of the k array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is then

\left(1-\left(1-\frac{1}{m}\right)^{kn}\right)^k \approx \left(1-e^{-kn/m}\right)^k .

Obviously, the probability of false positives decreases as m (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases. For a given m and n, the value of k (the number of hash functions) that minimizes the probability is

\frac{m}{n}\ln 2 \approx \frac{9m}{13n} \approx 0.7\frac{m}{n} ,

which gives a probability of

\left(\frac{1}{2^{\ln 2}}\right)^{m/n} \approx 0.62^{m/n} .

## Interesting properties

Unlike sets based on hash tables, any Bloom filter can represent the entire universe of elements. In this case, all bits are 1. Another consequence of this property is that add never fails due to the data structure "filling up," although the false positive rate increases steadily as elements are added.

Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations, respectively.

## Counting filters

Counting filters provide a way to implement a delete operation on a Bloom filter without recreating the filter afresh. In a counting filter the array positions (buckets) are extended from being a single bit, to being an n-bit counter. In fact, regular Bloom filters can be considered as counting filters with a bucket size of one bit. Counting filters were introduced in L. Fan, P. Cao, J. Almeida, and A. Broder. Summary cache: A scalable wide-area Web cache sharing protocol. In Proceeding of SIGCOMM ’98, 1998.

The insert operation is extended to increment the value of the buckets and the lookup operation checks that each of the required buckets is non-zero. The delete operation, obviously, then consists of decrementing the value of each of the respective buckets.

Arithmetic overflow of the buckets is a problem and the buckets should be sufficiently large to make this case rare. If it does occur then the increment and decrement operations must leave the bucket set to the maximum possible value in order to retain the properties of a Bloom filter.

## Bloomier filters

In 2004, Bernard Chazelle, Joe Kilian, Ronitt Rubinfeld, and Ayellet Tal designed a generalization of Bloom filters that could associate a value with each element that had been inserted, implementing an associative array. Like Bloom filters, these structures achieve a small space overhead by accepting a small probability of false positives. In the case of "Bloomier filters", a false positive is defined as returning a result when the key is not in the map. The map will never return the wrong value for a key that is in the map.

The simplest Bloomier filter is near-optimal and fairly simple to describe. Suppose initially that the only possible values are 0 and 1. We create a pair of Bloom filters A0 and B0 which contain, respectively, all values mapping to 0 and all values mapping to 1. Then, to determine which value a given key maps to, we look it up in both filters. If it is in neither, then the key is not in the map. If the key is in A0 but not B0, then it does not map to 1, and has a high probability of mapping to 0. Conversely, if the key is in B0 but not A0, then it does not map to 0 and has a high probability of mapping to 1.

A problem arises, however, when both filters claim to contain the item. We never insert an item into both, so one or both of the filters is lying (producing a false positive), but we don't know which. To determine this, we have another, smaller pair of filters A1 and B1. A1 contains values that map to 0 and which are false positives in B0; B1 contains values that map to 1 and which are false positives in A0. But whenever A0 and B0 both produce positives, at most one of these cases must occur, and so we simply have to determine which if any of the two filters A1 and B1 contains the key, another instance of our original problem.

It may so happen again that both filters produce a positive; we apply the same idea recursively to solve this problem. Because each pair of filters only contains keys that are in the map and produced false positives on all previous filter pairs, the number of keys is extremely likely to quickly drop to a very small quantity that can be easily stored in an ordinary deterministic map, such as a pair of small arrays with linear search. Moreover, the average total search time is a constant, because almost all queries will be resolved by the first pair, almost all remaining queries by the second pair, and so on. The total space required is independent of n, and is almost entirely occupied by the first filter pair.

Now that we have the structure and a search algorithm, we also need to know how to insert new key/value pairs. The program must not attempt to insert the same key with both values. If the value is 0, insert the key into A0 and then test if the key is in B0. If so, this is a false positive for B0, and the key must also be inserted into A1 recursively in the same manner. If we reach the last level, we simply insert it. When the value is 1, the operation is similar but with A and B reversed.

Now that we can map a key to the value 0 or 1, how does this help us map to general values? This is simple. We create a single such Bloomier filter for each bit of the result. If the values are large, we can instead map keys to hash values that can be used to retrieve the actual values. The space required for a Bloomier filter with n-bit values is typically slightly more than the space for 2n Bloom filters.

## Compact approximators

In 2004, Paolo Boldi and Sebastiano Vigna proposed a lattice-based a generalization of Bloom filters. A compact approximator associates to each key an element of a lattice (the standard Bloom filters being the case of the Boolean two-element lattice). Instead of a bit array, we have an array of lattice elements. When adding a new association between a key and an element of the lattice, we maximize the current content of the k array locations associated to the key with the lattice element. When reading the value associated to a key, we minimize the values found in the k locations associated to the key. The resulting value approximates from above the original value.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (3463 words)</summary>

````text
The Bloom filter, conceived by Burton H. Bloom in 1970, is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. False positives are possible, but false negatives are not. Elements can be added to the set, but not removed (though this can be addressed with a counting filter). The more elements that are added to the set, the larger the probability of false positives.

## Example

Google BigTable uses Bloom filters to reduce the disk lookups for non-existent rows or columns. Avoiding costly disk lookups considerably increases the performance of a database query operation.

The Squid Web Proxy Cache uses Bloom filters for so-called cache digests.

## Algorithm description

An empty Bloom filter is a bit array of m bits, all set to 0. There must also be k different hash functions defined, each of which maps or hashes some set element to one of the m array positions with an even distribution.

To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To query for an element (test whether it is in the set), feed it to each of the k hash functions to get k array positions. If any of the bits at these positions are 0, the element is not in the set – if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have been set to 1 during the insertion of other elements.

The requirement of designing k different independent hash functions can be prohibitive for large k. For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields. Alternatively, one can pass k different initial values (such as 0, 1, ..., k-1) to a hash function that takes an initial value; or add (or append) these values to the key. For larger m and/or k, independence among the hash functions can be relaxed with negligible increase in false positive rate (, ). Specifically, show the effectiveness of using enhanced double hashing or triple hashing, variants of double hashing, to derive the k indices using simple arithmetic on two or three indices computed with independent hash functions.

Unfortunately, removing an element from this simple Bloom filter is impossible. The element maps to k bits, and although setting any one of these k bits to zero suffices to remove it, this has the side effect of removing any other elements that map onto that bit, and we have no way of determining whether any such elements have been added. Such removal would introduce a possibility for false negatives, which are not allowed.

Removal of an element from a Bloom filter can be simulated by having a second Bloom filter that contains items that have been removed. However, false positives in the second filter become false negatives in the composite filter, which are not permitted. This approach also limits the semantics of removal since re-adding a previously removed item is not possible.

However, it is often the case that all the keys are available but are expensive to enumerate (for example, requiring many disk reads). When the false positive rate gets too high, the filter can be regenerated; this should be a relatively rare event.

## Space and time advantages

While risking false positives, Bloom filters have a strong space advantage over other data structures for representing sets, such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings (tries are an exception, since they can share storage between elements with equal prefixes). Linked structures incur an additional linear space overhead for pointers. A Bloom filter with 1% error and an optimal value of k, on the other hand, requires only about 9.6 bits per element — regardless of the size of the elements. This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. If a 1% false positive rate seems too high, each time we add about 4.8 bits per element we decrease it by ten times.

However, if the number of potential values is small and many of them can be in the set, then the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Note also that hash tables gain a space and time advantage if they begin ignoring collisions and only store whether each bucket contains an entry; in this case, they have effectively become Bloom filters with k = 1.

Bloom filters also have the unusual property that the time needed to either add items or to check whether an item is in the set is a fixed constant, O(k), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

To understand its space efficiency, it is instructive to compare the general Bloom filter with its special case when k = 1. If k = 1, then in order to keep the false positive rate sufficiently low, a small fraction of bits should be set, which means the array must be very large and contain long runs of zeros. The information content of the array relative to its size is low. The generalized Bloom filter (k greater than 1) allows many more bits to be set while still maintaining a low false positive rate; if the parameters (k and m) are chosen well, about half of the bits will be set, and these will be apparently random, minimizing redundancy and maximizing information content.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. If m is the number of bits in the array, the probability that a certain bit is not set to one by a certain hash function during the insertion of an element is then

1-\frac{1}{m}.

The probability that it is not set by any of the hash functions is

\left(1-\frac{1}{m}\right)^k.

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{m}\right)^{kn};

the probability that it is 1 is therefore

1-\left(1-\frac{1}{m}\right)^{kn}.

Now test membership of an element that is not in the set. Each of the k array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is then

\left(1-\left(1-\frac{1}{m}\right)^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k.

Obviously, the probability of false positives decreases as m (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases. For a given m and n, the value of k (the number of hash functions) that minimizes the probability is

\frac{m}{n}\ln 2 \approx \frac{9m}{13n} \approx 0.7\frac{m}{n},

which gives the false positive probability of

\left(\frac{1}{2}\right)^{k} \approx {0.6185}^{m/n}.

## Interesting properties

Unlike sets based on hash tables, any Bloom filter can represent the entire universe of elements. In this case, all bits are 1. Another consequence of this property is that add never fails due to the data structure "filling up," although the false positive rate increases steadily as elements are added.

Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations, respectively.

## Alternatives to Bloom filters

Classic Bloom filters use 1.44\log2(1/\epsilon) bits of space per inserted key, where \epsilon is the false positive rate of the Bloom filter. However the space that is strictly necessary for any data structure playing the same role as a Bloom filter is only \log2(1/\epsilon) per key . Hence Bloom filters use 44% more space than a hypothetical equivalent optimal data structure. The number of hash functions used to achieve a given false positive rate \epsilon is proportional to 1/\epsilon which is not optimal as it has been proved that an optimal data structure would need only a constant number of hash functions independent of the false positive rate.

describe a probabilistic structure based on hash tables, hash compaction, which identify as significantly more accurate than a Bloom filter when each is configured optimally. Dillinger and Manolios, however, point out that the reasonable accuracy of any given Bloom filter over a wide range of numbers of additions makes it attractive for probabilistic enumeration of state spaces of unknown size. Hash compaction is, therefore, attractive when the number of additions can be predicted accurately; however, despite being very fast in software, hash compaction is poorly-suited for hardware because of worst-case linear access time.

have studied some variants of Bloom filters that are either faster or use less space than classic Bloom filters. The basic idea of the fast variant is to locate the k hash values associated with each key into one or two blocks having the same size as processor's memory cache blocks (usually 64 bytes). This will presumably improve performance by reducing the number of potential memory cache misses. The proposed variants have however the drawback of using about 32% more space than classic Bloom filters.

The space efficient variant relies on using a single hash function that generates for each key a value in the range \left[0\dots\frac{n}{\varepsilon}\right] where \epsilon is the requested false positive rate. The sequence of values is then sorted and compressed using golomb coding (or some other compression technique) to occupy a space close to n\log2(1/\epsilon) bits. To query the Bloom filter for a given key, it will suffice to check if its corresponding value is stored in the Bloom filter. Decompressing the whole Bloom filter for each query would make this variant totally unusable. To overcome this problem the sequence of values is divided into small blocks of equal size that are compressed separately. At query time only half a block will need to be decompressed on average. Because of decompression overhead, this variant may be slower than classic Bloom filters but this may be compensated by the fact that a single hash function need to be computed.

Another alternative to classic Bloom filter is the one based on space efficient variants of cuckoo hashing. In this case once the hash table is constructed, the keys stored in the hash table are replaced with short signatures of the keys. Those signatures are strings of bits computed using a hash function applied on the keys.

## Counting filters

Counting filters provide a way to implement a delete operation on a Bloom filter without recreating the filter afresh. In a counting filter the array positions (buckets) are extended from being a single bit, to being an n-bit counter. In fact, regular Bloom filters can be considered as counting filters with a bucket size of one bit. Counting filters were introduced by .

The insert operation is extended to increment the value of the buckets and the lookup operation checks that each of the required buckets is non-zero. The delete operation, obviously, then consists of decrementing the value of each of the respective buckets.

Arithmetic overflow of the buckets is a problem and the buckets should be sufficiently large to make this case rare. If it does occur then the increment and decrement operations must leave the bucket set to the maximum possible value in order to retain the properties of a Bloom filter.

The size of counters is usually 3 or 4 bits. Hence counting Bloom filters use 3 to 4 times more space than static Bloom filters. In theory, an optimal data structure equivalent to a counting Bloom filter should not use more space than a static Bloom filter.

Another issue with counting filters is in their scalability. Because the counting Bloom filter table can not be resized, the maximal number of keys to be stored simultaneously in the filter must be known in advance. Once the designed capacity of the table is exceeded the false positive rate will grow rapidly as more keys are inserted.

introduced a Data structure based on d-left hashing that is functionally equivalent but uses approximately half as much space as counting Bloom filters. The scalability

issue does not occur in this data structure. Once the designed capacity is exceeded, the keys could be reinserted in a new hash table of double size.

The space efficient variant by could also be used to implement counting filters by supporting insertions and deletions.

## Bloomier filters

designed a generalization of Bloom filters that could associate a value with each element that had been inserted, implementing an associative array. Like Bloom filters, these structures achieve a small space overhead by accepting a small probability of false positives. In the case of "Bloomier filters", a false positive is defined as returning a result when the key is not in the map. The map will never return the wrong value for a key that is in the map.

The simplest Bloomier filter is near-optimal and fairly simple to describe. Suppose initially that the only possible values are 0 and 1. We create a pair of Bloom filters A0 and B0 which contain, respectively, all values mapping to 0 and all values mapping to 1. Then, to determine which value a given key maps to, we look it up in both filters. If it is in neither, then the key is not in the map. If the key is in A0 but not B0, then it does not map to 1, and has a high probability of mapping to 0. Conversely, if the key is in B0 but not A0, then it does not map to 0 and has a high probability of mapping to 1.

A problem arises, however, when both filters claim to contain the item. We never insert an item into both, so one or both of the filters is lying (producing a false positive), but we don't know which. To determine this, we have another, smaller pair of filters A1 and B1. A1 contains values that map to 0 and which are false positives in B0; B1 contains values that map to 1 and which are false positives in A0. But whenever A0 and B0 both produce positives, at most one of these cases must occur, and so we simply have to determine which if any of the two filters A1 and B1 contains the key, another instance of our original problem.

It may so happen again that both filters produce a positive; we apply the same idea recursively to solve this problem. Because each pair of filters only contains keys that are in the map and produced false positives on all previous filter pairs, the number of keys is extremely likely to quickly drop to a very small quantity that can be easily stored in an ordinary deterministic map, such as a pair of small arrays with linear search. Moreover, the average total search time is a constant, because almost all queries will be resolved by the first pair, almost all remaining queries by the second pair, and so on. The total space required is independent of n, and is almost entirely occupied by the first filter pair.

Now that we have the structure and a search algorithm, we also need to know how to insert new key/value pairs. The program must not attempt to insert the same key with both values. If the value is 0, insert the key into A0 and then test if the key is in B0. If so, this is a false positive for B0, and the key must also be inserted into A1 recursively in the same manner. If we reach the last level, we simply insert it. When the value is 1, the operation is similar but with A and B reversed.

Now that we can map a key to the value 0 or 1, how does this help us map to general values? This is simple. We create a single such Bloomier filter for each bit of the result. If the values are large, we can instead map keys to hash values that can be used to retrieve the actual values. The space required for a Bloomier filter with n-bit values is typically slightly more than the space for 2n Bloom filters.

A very simple way to implement Bloomier filters is by means of minimal perfect hashing. A minimal perfect hash function h is first generated for the set of n keys. Then an array is filled with n pairs (signature,value) associated with each key at the positions given by function h when applied on each key. The signature of a key is a string of r bits computed by applying a hash function g of range 2^r on the key. The value of r is chosen such that 2^r>=1/\epsilon , where \epsilon is the requested false positive rate. To query for a given key, hash function h is first applied on the key. This will give a position into the array from which we retrieve a pair (signature,value). Then we compute the signature of the key using function g. If the computed signature is the same as retrieved signature we return the retrieved value. The probabaility of false positive is 1/2^r .

Another alternative to implement static bloomier and bloom filters based on matrix solving has been simultanesouly proposed in , and . The space usage of this method is optimal as it needs only \log_2(\epsilon) bits per key for a bloom filter. However time to generate the bloom or bloomier filter can be very high. The generation time can be reduced to a reasonable value at the price of a small increase in space usage.

Dynamic Bloomier filters have been studied by . They proved that any dynamic Bloomier filter needs at least around

\log(l) bits per key where l is the length of the key. A simple dynamic version of Bloomier filters can be implemented using two dynamic data structures. Let the two data structures be noted S1 and S2. S1 will store keys with their associated data while S2 will only store signatures of keys with their associated data. Those signatures are simply hash values of keys in the range [0..\frac{n}{\epsilon}] where n is the maximal number of keys to be stored in the Bloomier filter and \epsilon is the requested false positive rate. To insert a key in the Bloomier filter, its hash value is first computed. Then the algorithm checks if a key with the same hash value already exists in S2. If this is not the case, the hash value is inserted in S2 along with data associated with the key. If the same hash value already exists in S2 then the key is inserted into S1 along with its associated data. The deletion is symmetric : if the key already exists in S1 it will be deleted from there, otherwise the hash value associated with the key is deleted from S2. An issue with this algorithm is on how to store efficiently S1 and S2. For S1 any hash algorithm can be used. To store S2 golomb coding could be applied to compress signatures to use a space close to \log2(1/\epsilon) per key.

## Compact approximators

proposed a lattice-based generalization of Bloom filters. A compact approximator associates to each key an element of a lattice (the standard Bloom filters being the case of the Boolean two-element lattice). Instead of a bit array, they have an array of lattice elements. When adding a new association between a key and an element of the lattice, they maximize the current content of the k array locations associated to the key with the lattice element. When reading the value associated to a key, they minimize the values found in the k locations associated to the key. The resulting value approximates from above the original value.

### Implementations

Implementation in C++ and Object Pascal

Implementation in Erlang

Implementation in Haskell

Implementation in Java

Implementation in Javascript

Implementation in Lisp

Implementation in Perl

Implementation in Python

Implementation in Ruby

de:Bloomfilter

ko:블룸 필터

he:פילטר בלום

ja:ブルームフィルタ

zh:布隆过滤器
````

</details>

<details><summary><b>Step 4 — revision_4</b> (3441 words)</summary>

````text
A Bloom filter, conceived by Burton Howard Bloom in 1970,[1] is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. False positive retrieval results are possible, but false negatives are not; i.e. a query returns either "inside set (may be wrong)" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with a counting filter). The more elements that are added to the set, the larger the probability of false positives.

## Algorithm description

An empty Bloom filter is a bit array of m bits, all set to 0. There must also be k different hash functions defined, each of which maps or hashes some set element to one of the m array positions with a uniform random distribution.

To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To query for an element (test whether it is in the set), feed it to each of the k hash functions to get k array positions. If any of the bits at these positions are 0, the element is definitely not in the set – if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have by chance been set to 1 during the insertion of other elements, resulting in a false positive. In a simple bloom filter, there is no way to distinguish between the two cases, but more advanced techniques can address this problem.

The requirement of designing k different independent hash functions can be prohibitive for large k. For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields. Alternatively, one can pass k different initial values (such as 0, 1, ..., k − 1) to a hash function that takes an initial value; or add (or append) these values to the key. For larger m and/or k, independence among the hash functions can be relaxed with negligible increase in false positive rate (, ). Specifically, show the effectiveness of deriving the k indices using enhanced double hashing or triple hashing, variants of double hashing that are effectively simple random number generators seeded with the two or three hash values.

Removing an element from this simple Bloom filter is impossible because false negatives are not permitted. An element maps to k bits, and although setting any one of those k bits to zero suffices to remove the element, it also results in removing any other elements that happen to map onto that bit. Since there is no way of determining whether any other elements have been added that affect the bits for an element to be removed, clearing any of the bits would introduce the possibility for false negatives.

One-time removal of an element from a Bloom filter can be simulated by having a second Bloom filter that contains items that have been removed. However, false positives in the second filter become false negatives in the composite filter, which may be undesirable. In this approach re-adding a previously removed item is not possible, as one would have to remove it from the "removed" filter.

It is often the case that all the keys are available but are expensive to enumerate (for example, requiring many disk reads). When the false positive rate gets too high, the filter can be regenerated; this should be a relatively rare event.

## Space and time advantages

While risking false positives, Bloom filters have a strong space advantage over other data structures for representing sets, such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings (tries are an exception, since they can share storage between elements with equal prefixes). Linked structures incur an additional linear space overhead for pointers. A Bloom filter with 1% error and an optimal value of k, in contrast, requires only about 9.6 bits per element — regardless of the size of the elements. This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. If a 1% false-positive rate seems too high, adding about 4.8 bits per element decreases it by ten times.

However, if the number of potential values is small and many of them can be in the set, the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Note also that hash tables gain a space and time advantage if they begin ignoring collisions and store only whether each bucket contains an entry; in this case, they have effectively become Bloom filters with k = 1.

Bloom filters also have the unusual property that the time needed either to add items or to check whether an item is in the set is a fixed constant, O(k), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

To understand its space efficiency, it is instructive to compare the general Bloom filter with its special case when k = 1. If k = 1, then in order to keep the false positive rate sufficiently low, a small fraction of bits should be set, which means the array must be very large and contain long runs of zeros. The information content of the array relative to its size is low. The generalized Bloom filter (k greater than 1) allows many more bits to be set while still maintaining a low false positive rate; if the parameters (k and m) are chosen well, about half of the bits will be set, and these will be apparently random, minimizing redundancy and maximizing information content.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. If m is the number of bits in the array, and k is the number of hash functions, then the probability that a certain bit is not set to 1 by a certain hash function during the insertion of an element is then

1-\frac{1}{m}.

The probability that it is not set to 1 by any of the hash functions is

\left(1-\frac{1}{m}\right)^k.

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{m}\right)^{kn};

the probability that it is 1 is therefore

1-\left(1-\frac{1}{m}\right)^{kn}.

Now test membership of an element that is not in the set. Each of the k array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is often given as

\left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k.

This is not strictly correct as it assumes independence for the probabilities of each bit being set. However, assuming it is a close approximation we have that the probability of false positives decreases as m (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases. For a given m and n, the value of k (the number of hash functions) that minimizes the probability is

\frac{m}{n}\ln 2 \approx 0.7\frac{m}{n},

which gives the false positive probability of

2^{-k} \approx {0.6185}^{m/n}.

The required number of bits m, given n (the number of inserted elements) and a desired false positive probability p (and assuming the optimal value of k is used) can be computed by substituting the optimal value of k in the probability expression above:

p = \left( 1-e^{-(m/n\ln 2) n/m} \right)^{(m/n\ln 2)}

which can be simplified to:

\ln p = -\frac{m}{n} \left(\ln 2\right)^2.

This results in:

m=-\frac{n\ln p}{(\ln 2)^2}.

This means that for a given false positive probability p, the length of a Bloom filter m is proportionate to the number of elements being filtered n.[2] While the above formula is asymptotic (i.e. applicable as m,n → ∞), the agreement with finite values of m,n is also quite good; the false positive probability for a finite bloom filter with m bits, n elements, and k hash functions is at most

\left( 1-e^{-k(n+0.5)/(m-1)} \right)^k.

So we can use the asymptotic formula if we pay a penalty for at most half an extra element and at most one fewer bit.[3]

## Interesting properties

Unlike sets based on hash tables, any Bloom filter can represent the entire universe of elements. In this case, all bits are 1. Another consequence of this property is that add never fails due to the data structure "filling up." However, the false positive rate increases steadily as elements are added until all bits in the filter are set to 1, so a negative value is never returned. At this point, the Bloom filter completely ceases to differentiate between differing inputs, and is functionally useless.

Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations, respectively. The union operation on Bloom filters is lossless in the sense that the resulting Bloom filter is the same as the Bloom filter created from scratch using the union of the two sets. The intersect operation satisfies a weaker property: the false positive probability in the resulting Bloom filter is at most the false-positive probability in one of the constituent Bloom filters, but may be larger than the false positive probability in the Bloom filter created from scratch using the intersection of the two sets.

Some kinds of superimposed code can be seen as a Bloom filter implemented with physical edge-notched cards.

## Examples

Google BigTable uses Bloom filters to reduce the disk lookups for non-existent rows or columns. Avoiding costly disk lookups considerably increases the performance of a database query operation.[4]

The Squid Web Proxy Cache uses Bloom filters for cache digests.[5]

The Venti archival storage system uses Bloom filters to detect previously stored data.[6]

The SPIN model checker uses Bloom filters to track the reachable state space for large verification problems.[7]

The Google Chrome web browser uses Bloom filters to speed up its Safe Browsing service.[8]

## Alternatives

Classic Bloom filters use 1.44\log_2(1/\epsilon) bits of space per inserted key, where \epsilon is the false positive rate of the Bloom filter. However, the space that is strictly necessary for any data structure playing the same role as a Bloom filter is only \log_2(1/\epsilon) per key . Hence Bloom filters use 44% more space than a hypothetical equivalent optimal data structure. The number of hash functions used to achieve a given false positive rate \epsilon is proportional to 1/\epsilon which is not optimal as it has been proved that an optimal data structure would need only a constant number of hash functions independent of the false positive rate.

describe a probabilistic structure based on hash tables, hash compaction, which identify as significantly more accurate than a Bloom filter when each is configured optimally. Dillinger and Manolios, however, point out that the reasonable accuracy of any given Bloom filter over a wide range of numbers of additions makes it attractive for probabilistic enumeration of state spaces of unknown size. Hash compaction is, therefore, attractive when the number of additions can be predicted accurately; however, despite being very fast in software, hash compaction is poorly suited for hardware because of worst-case linear access time.

have studied some variants of Bloom filters that are either faster or use less space than classic Bloom filters. The basic idea of the fast variant is to locate the k hash values associated with each key into one or two blocks having the same size as processor's memory cache blocks (usually 64 bytes). This will presumably improve performance by reducing the number of potential memory cache misses. The proposed variants have however the drawback of using about 32% more space than classic Bloom filters.

The space efficient variant relies on using a single hash function that generates for each key a value in the range \left[0,n/\varepsilon\right] where \epsilon is the requested false positive rate. The sequence of values is then sorted and compressed using Golomb coding (or some other compression technique) to occupy a space close to n\log_2(1/\epsilon) bits. To query the Bloom filter for a given key, it will suffice to check if its corresponding value is stored in the Bloom filter. Decompressing the whole Bloom filter for each query would make this variant totally unusable. To overcome this problem the sequence of values is divided into small blocks of equal size that are compressed separately. At query time only half a block will need to be decompressed on average. Because of decompression overhead, this variant may be slower than classic Bloom filters but this may be compensated by the fact that a single hash function need to be computed.

Another alternative to classic Bloom filter is the one based on space efficient variants of cuckoo hashing. In this case once the hash table is constructed, the keys stored in the hash table are replaced with short signatures of the keys. Those signatures are strings of bits computed using a hash function applied on the keys.

## Extensions and applications

### Counting filters

Counting filters provide a way to implement a delete operation on a Bloom filter without recreating the filter afresh. In a counting filter the array positions (buckets) are extended from being a single bit, to an n-bit counter. In fact, regular Bloom filters can be considered as counting filters with a bucket size of one bit. Counting filters were introduced by .

The insert operation is extended to increment the value of the buckets and the lookup operation checks that each of the required buckets is non-zero. The delete operation, obviously, then consists of decrementing the value of each of the respective buckets.

Arithmetic overflow of the buckets is a problem and the buckets should be sufficiently large to make this case rare. If it does occur then the increment and decrement operations must leave the bucket set to the maximum possible value in order to retain the properties of a Bloom filter.

The size of counters is usually 3 or 4 bits. Hence counting Bloom filters use 3 to 4 times more space than static Bloom filters. In theory, an optimal data structure equivalent to a counting Bloom filter should not use more space than a static Bloom filter.

Another issue with counting filters is limited scalability. Because the counting Bloom filter table cannot be expanded, the maximal number of keys to be stored simultaneously in the filter must be known in advance. Once the designed capacity of the table is exceeded the false positive rate will grow rapidly as more keys are inserted.

introduced a data structure based on d-left hashing that is functionally equivalent but uses approximately half as much space as counting Bloom filters. The scalability issue does not occur in this data structure. Once the designed capacity is exceeded, the keys could be reinserted in a new hash table of double size.

The space efficient variant by could also be used to implement counting filters by supporting insertions and deletions.

### Data synchronization

Bloom filters can be used for approximate data synchronization as in . Counting Bloom filters can be used to approximate the number of differences between two sets and this approach is described in .

### Bloomier filters

designed a generalization of Bloom filters that could associate a value with each element that had been inserted, implementing an associative array. Like Bloom filters, these structures achieve a small space overhead by accepting a small probability of false positives. In the case of "Bloomier filters", a false positive is defined as returning a result when the key is not in the map. The map will never return the wrong value for a key that is in the map.

### Compact approximators

proposed a lattice-based generalization of Bloom filters. A compact approximator associates to each key an element of a lattice (the standard Bloom filters being the case of the Boolean two-element lattice). Instead of a bit array, they have an array of lattice elements. When adding a new association between a key and an element of the lattice, they maximize the current content of the k array locations associated to the key with the lattice element. When reading the value associated to a key, they minimize the values found in the k locations associated to the key. The resulting value approximates from above the original value.

### Stable Bloom filters

proposed Stable Bloom filters as a variant of Bloom filters for streaming data. The idea is that since there is no way to store the entire history of a stream (which can be infinite), Stable Bloom filters continuously evict stale information to make room for more recent elements. Since stale information is evicted, the Stable Bloom filter introduces false negatives, which do not appear in traditional bloom filters. The authors show that a tight upper bound of false positive rates is guaranteed, and the method is superior to standard bloom filters in terms of false positive rates and time efficiency when a small space and an acceptable false positive rate are given.

### Scalable Bloom filters

proposed a variant of Bloom filters that can adapt dynamically to the number of elements stored, while assuring a minimum false positive probability. The technique is based on sequences of standard bloom filters with increasing capacity and tighter false positive probabilities, so as to ensure that a maximum false positive probability can be set beforehand, regardless of the number of elements to be inserted.

### Attenuated Bloom filters

An attenuated bloom filter of depth D can be viewed as an array of D normal bloom filters. In the context of service discovery in a network, each node stores regular and attenuated bloom filters locally. The regular or local bloom filter indicates which services are offered by the node itself. The attenuated filter of level i indicates which services can be found on nodes that are i-hops away from the current node. The i-th value is constructed by taking a union of local bloom filters for nodes i-hops away from the node.

Lets take a small network shown on the graph below as an example. Say we are searching for a service A whose id hashes to bits 0,1, and 3 (pattern 11010). Let n1 node to be the starting point. First, we check whether service A is offered by n1 by checking its local filter. Since the patterns don't match, we check the attenuated bloom filter in order to determine which node should be the next hop. We see that n2 doesn't offer service A but lies on the path to nodes that do. Hence, we move to n2 and repeat the same procedure. We quickly find that n3 offers the service, and hence the destination is located.

By using attenuated Bloom filters consisting of multiple layers, services at more than one hop distance can be discovered while avoiding saturation of the Bloom filter by attenuating (shifting out) bits set by sources further away.

### Implementations

Implementation in C from literateprograms.org

Implementation in C++ and Object Pascal from partow.net

Implementation in C# from codeplex.com

Implementation in Erlang from sites.google.com

Implementation in Haskell from haskell.org

Implementation in Java from MagnusS on github.com

Implementation in Javascript from la.ma.la

Implementation in Lisp from lemonodor.com

Implementation in Perl from cpan.org

Implementation in PHP from code.google.com

Implementation in Python, Scalable Bloom Filter from pypi.python.org

Implementation in Ruby from rubyinside.com

Implementation in Scala from codecommit.com

Implementation in Tcl from kocjan.org

cs:Bloomův filtr

de:Bloomfilter

fa:فیلتر بولوم

fr:Filtre de Bloom

ko:블룸 필터

he:פילטר בלום

ja:ブルームフィルタ

pl:Filtr Blooma

ru:Фильтр Блума

sk:Bloomov filter

sr:Блумов филтер

vi:Bộ lọc Bloom

zh:布隆过滤器

References:
[1] Donald Knuth. The Art of Computer Programming, Errata for Volume 3 (2nd ed.). http://www-cs-faculty.stanford.edu/~knuth/err3.textxt
[2] .
[3] .
[4] .
[5] Wessels, Duane. (2004). Squid: The Definitive Guide. O'Reilly Media.
[6] http://plan9.bell-labs.com/magic/man2html/8/venti
[7] http://spinroot.com/
[8] http://src.chromium.org/viewvc/chrome/trunk/src/chrome/browser/safe_browsing/bloom_filter.h?view=markup
````

</details>

<details><summary><b>Step 5 — revision_5</b> (4681 words)</summary>

````text
A Bloom filter is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not, thus a Bloom filter has a 100% recall rate. In other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with a "counting" filter). The more elements that are added to the set, the larger the probability of false positives.

Bloom proposed the technique for applications where the amount of source data would require an impracticably large hash area in memory if "conventional" error-free hashing techniques were applied. He gave the example of a hyphenation algorithm for a dictionary of 500,000 words, out of which 90% follow simple hyphenation rules, but the remaining 10% require expensive disk accesses to retrieve specific hyphenation patterns. With sufficient core memory, an error-free hash could be used to eliminate all unnecessary disk accesses; on the other hand, with limited core memory, Bloom's technique uses a smaller hash area but still eliminates most unnecessary accesses. For example, a hash area only 15% of the size needed by an ideal error-free hash still eliminates 85% of the disk accesses ().

More generally, fewer than 10 bits per element are required for a 1% false positive probability, independent of the size or number of elements in the set ().

## Algorithm description

An empty Bloom filter is a bit array of m bits, all set to 0. There must also be k different hash functions defined, each of which maps or hashes some set element to one of the m array positions with a uniform random distribution.

To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To query for an element (test whether it is in the set), feed it to each of the k hash functions to get k array positions. If any of the bits at these positions are 0, the element is definitely not in the set – if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have by chance been set to 1 during the insertion of other elements, resulting in a false positive. In a simple Bloom filter, there is no way to distinguish between the two cases, but more advanced techniques can address this problem.

The requirement of designing k different independent hash functions can be prohibitive for large k. For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields. Alternatively, one can pass k different initial values (such as 0, 1, ..., k − 1) to a hash function that takes an initial value; or add (or append) these values to the key. For larger m and/or k, independence among the hash functions can be relaxed with negligible increase in false positive rate (, ). Specifically, show the effectiveness of deriving the k indices using enhanced double hashing or triple hashing, variants of double hashing that are effectively simple random number generators seeded with the two or three hash values.

Removing an element from this simple Bloom filter is impossible because false negatives are not permitted. An element maps to k bits, and although setting any one of those k bits to zero suffices to remove the element, it also results in removing any other elements that happen to map onto that bit. Since there is no way of determining whether any other elements have been added that affect the bits for an element to be removed, clearing any of the bits would introduce the possibility for false negatives.

One-time removal of an element from a Bloom filter can be simulated by having a second Bloom filter that contains items that have been removed. However, false positives in the second filter become false negatives in the composite filter, which may be undesirable. In this approach re-adding a previously removed item is not possible, as one would have to remove it from the "removed" filter.

It is often the case that all the keys are available but are expensive to enumerate (for example, requiring many disk reads). When the false positive rate gets too high, the filter can be regenerated; this should be a relatively rare event.

## Space and time advantages

While risking false positives, Bloom filters have a strong space advantage over other data structures for representing sets, such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings (tries are an exception, since they can share storage between elements with equal prefixes). Linked structures incur an additional linear space overhead for pointers. A Bloom filter with 1% error and an optimal value of k, in contrast, requires only about 9.6 bits per element — regardless of the size of the elements. This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. The 1% false-positive rate can be reduced by a factor of ten by adding only about 4.8 bits per element.

However, if the number of potential values is small and many of them can be in the set, the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Note also that hash tables gain a space and time advantage if they begin ignoring collisions and store only whether each bucket contains an entry; in this case, they have effectively become Bloom filters with k = 1.[1]

Bloom filters also have the unusual property that the time needed either to add items or to check whether an item is in the set is a fixed constant, O(k), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

To understand its space efficiency, it is instructive to compare the general Bloom filter with its special case when k = 1. If k = 1, then in order to keep the false positive rate sufficiently low, a small fraction of bits should be set, which means the array must be very large and contain long runs of zeros. The information content of the array relative to its size is low. The generalized Bloom filter (k greater than 1) allows many more bits to be set while still maintaining a low false positive rate; if the parameters (k and m) are chosen well, about half of the bits will be set,[2] and these will be apparently random, minimizing redundancy and maximizing information content.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. If m is the number of bits in the array, the probability that a certain bit is not set to 1 by a certain hash function during the insertion of an element is

1-\frac{1}{m}.

If k is the number of hash functions, the probability that the bit is not set to 1 by any of the hash functions is

\left(1-\frac{1}{m}\right)^k.

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{m}\right)^{kn};

the probability that it is 1 is therefore

1-\left(1-\frac{1}{m}\right)^{kn}.

Now test membership of an element that is not in the set. Each of the k array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is often given as

\left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k.

This is not strictly correct as it assumes independence for the probabilities of each bit being set. However, assuming it is a close approximation we have that the probability of false positives decreases as m (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases.

An alternative analysis arriving at the same approximation without the assumption of independence is given by Mitzenmacher and Upfal.[3] After all n items have been added to the Bloom filter, let q be the fraction of the m bits that are set to 0. (That is, the number of bits still set to 0 is qm.) Then, when testing membership of an element not in the set, for the array position given by any of the k hash functions, the probability that the bit is found set to 1 is 1-q . So the probability that all k hash functions find their bit set to 1 is (1 - q)^k . Further, the expected value of q is the probability that a given array position is left untouched by each of the k hash functions for each of the n items, which is (as above)

E[q] = \left(1 - \frac{1}{m}\right)^{kn} .

It is possible to prove, without the independence assumption, that q is very strongly concentrated around its expected value. In particular, from the Azuma–Hoeffding inequality, they prove that[4]

\Pr(\left|q - E[q]\right| \ge \frac{\lambda}{m}) \le 2\exp(-2\lambda^2/m)

Because of this, we can say that the exact probability of false positives is

\sum_{t} \Pr(q = t) (1 - t)^k \approx (1 - E[q])^k = \left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k

as before.

### Optimal number of hash functions

For a given m and n, the value of k (the number of hash functions) that minimizes the false positive probability is

k = \frac{m}{n} \ln 2,

which gives

2^{-k} \approx {0.6185}^{m/n}.

The required number of bits m, given n (the number of inserted elements) and a desired false positive probability p (and assuming the optimal value of k is used) can be computed by substituting the optimal value of k in the probability expression above:

p = \left( 1-e^{-(m/n\ln 2) n/m} \right)^{(m/n\ln 2)}

which can be simplified to:

\ln p = -\frac{m}{n} \left(\ln 2\right)^2.

This results in:

m=-\frac{n\ln p}{(\ln 2)^2}.

This means that for a given false positive probability p, the length of a Bloom filter m is proportionate to the number of elements being filtered n. While the above formula is asymptotic (i.e. applicable as m,n → ∞), the agreement with finite values of m,n is also quite good; the false positive probability for a finite bloom filter with m bits, n elements, and k hash functions is at most

\left( 1-e^{-k(n+0.5)/(m-1)} \right)^k.

So we can use the asymptotic formula if we pay a penalty for at most half an extra element and at most one fewer bit.[5]

## Approximating the number of items in a Bloom filter

showed that the number of items in a Bloom filter can be approximated with the following formula,

n^* = - \tfrac{ m \ln \left[ 1 - \tfrac{X}{m} \right] } { k}

where n^* is an estimate of the number of items in the filter, m is length of the filter, k is the number of hash functions per item, and X is the number of bits set to one.

## The union and intersection of sets

Bloom filters are a way of compactly representing a set of items. It is common to try to compute the size of the intersection or union between two sets. Bloom filters can be used to approximate the size of the intersection and union of two sets. showed that for two bloom filters of length m , their counts, respectively can be estimated as

n(A^*) = -m \ln \left[ 1 - n(A) / m \right] / k

and

n(B^*) = -m \ln \left[ 1 - n(B) / m \right]/k .

The size of their union can be estimated as

n(A^*\cup B^*) = -m \ln \left[ 1 - n(A \cup B) / m \right]/k ,

where n(A \cup B) is the number of bits set to one in either of the two bloom filters. Finally, the intersection can be estimated as

n(A^*\cap B^*) = n(A^*) + n(B^*) - n(A^*\cup B^*) ,

using the three formulas together.

## Interesting properties

Unlike a standard hash table, a Bloom filter of a fixed size can represent a set with an arbitrary large number of elements; adding an element never fails due to the data structure "filling up." However, the false positive rate increases steadily as elements are added until all bits in the filter are set to 1, at which point all queries yield a positive result.

Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations, respectively. The union operation on Bloom filters is lossless in the sense that the resulting Bloom filter is the same as the Bloom filter created from scratch using the union of the two sets. The intersect operation satisfies a weaker property: the false positive probability in the resulting Bloom filter is at most the false-positive probability in one of the constituent Bloom filters, but may be larger than the false positive probability in the Bloom filter created from scratch using the intersection of the two sets.

Some kinds of superimposed code can be seen as a Bloom filter implemented with physical edge-notched cards. An example is Zatocoding, invented by Calvin Mooers in 1947, in which the set of categories associated with a piece of information is represented by notches on a card, with a random pattern of four notches for each category.

## Examples

Google BigTable and Apache Cassandra use Bloom filters to reduce the disk lookups for non-existent rows or columns. Avoiding costly disk lookups considerably increases the performance of a database query operation.[6]

The Google Chrome web browser used to use a Bloom filter to identify malicious URLs. Any URL was first checked against a local Bloom filter, and only if the Bloom filter returned a positive result was a full check of the URL performed (and the user warned, if that too returned a positive result).[7,8]

The Squid Web Proxy Cache uses Bloom filters for cache digests.[9]

Bitcoin uses Bloom filters to speed up wallet synchronization.[10,11]

The Venti archival storage system uses Bloom filters to detect previously stored data.[12]

The SPIN model checker uses Bloom filters to track the reachable state space for large verification problems.[13]

The Cascading analytics framework uses Bloom filters to speed up asymmetric joins, where one of the joined data sets is significantly larger than the other (often called Bloom join in the database literature).[14]

## Alternatives

Classic Bloom filters use 1.44\log_2(1/\epsilon) bits of space per inserted key, where \epsilon is the false positive rate of the Bloom filter. However, the space that is strictly necessary for any data structure playing the same role as a Bloom filter is only \log_2(1/\epsilon) per key . Hence Bloom filters use 44% more space than a hypothetical equivalent optimal data structure. The number of hash functions used to achieve a given false positive rate \epsilon is proportional to log(1/\epsilon) which is not optimal as it has been proved that an optimal data structure would need only a constant number of hash functions independent of the false positive rate.

describe a probabilistic structure based on hash tables, hash compaction, which identify as significantly more accurate than a Bloom filter when each is configured optimally. Dillinger and Manolios, however, point out that the reasonable accuracy of any given Bloom filter over a wide range of numbers of additions makes it attractive for probabilistic enumeration of state spaces of unknown size. Hash compaction is, therefore, attractive when the number of additions can be predicted accurately; however, despite being very fast in software, hash compaction is poorly suited for hardware because of worst-case linear access time.

have studied some variants of Bloom filters that are either faster or use less space than classic Bloom filters. The basic idea of the fast variant is to locate the k hash values associated with each key into one or two blocks having the same size as processor's memory cache blocks (usually 64 bytes). This will presumably improve performance by reducing the number of potential memory cache misses. The proposed variants have however the drawback of using about 32% more space than classic Bloom filters.

The space efficient variant relies on using a single hash function that generates for each key a value in the range \left[0,n/\varepsilon\right] where \epsilon is the requested false positive rate. The sequence of values is then sorted and compressed using Golomb coding (or some other compression technique) to occupy a space close to n\log_2(1/\epsilon) bits. To query the Bloom filter for a given key, it will suffice to check if its corresponding value is stored in the Bloom filter. Decompressing the whole Bloom filter for each query would make this variant totally unusable. To overcome this problem the sequence of values is divided into small blocks of equal size that are compressed separately. At query time only half a block will need to be decompressed on average. Because of decompression overhead, this variant may be slower than classic Bloom filters but this may be compensated by the fact that a single hash function need to be computed.

Another alternative to classic Bloom filter is the one based on space efficient variants of cuckoo hashing. In this case once the hash table is constructed, the keys stored in the hash table are replaced with short signatures of the keys. Those signatures are strings of bits computed using a hash function applied on the keys.

## Extensions and applications

### Counting filters

Counting filters provide a way to implement a delete operation on a Bloom filter without recreating the filter afresh. In a counting filter the array positions (buckets) are extended from being a single bit to being an n-bit counter. In fact, regular Bloom filters can be considered as counting filters with a bucket size of one bit. Counting filters were introduced by .

The insert operation is extended to increment the value of the buckets and the lookup operation checks that each of the required buckets is non-zero. The delete operation, obviously, then consists of decrementing the value of each of the respective buckets.

Arithmetic overflow of the buckets is a problem and the buckets should be sufficiently large to make this case rare. If it does occur then the increment and decrement operations must leave the bucket set to the maximum possible value in order to retain the properties of a Bloom filter.

The size of counters is usually 3 or 4 bits. Hence counting Bloom filters use 3 to 4 times more space than static Bloom filters. In theory, an optimal data structure equivalent to a counting Bloom filter should not use more space than a static Bloom filter.

Another issue with counting filters is limited scalability. Because the counting Bloom filter table cannot be expanded, the maximal number of keys to be stored simultaneously in the filter must be known in advance. Once the designed capacity of the table is exceeded, the false positive rate will grow rapidly as more keys are inserted.

introduced a data structure based on d-left hashing that is functionally equivalent but uses approximately half as much space as counting Bloom filters. The scalability issue does not occur in this data structure. Once the designed capacity is exceeded, the keys could be reinserted in a new hash table of double size.

The space efficient variant by could also be used to implement counting filters by supporting insertions and deletions.

introduced a new general method based on variable increments that significantly improves the false positive probability of counting Bloom filters and their variants, while still supporting deletions. Unlike counting Bloom filters, at each element insertion, the hashed counters are incremented by a hashed variable increment instead of a unit increment. To query an element, the exact values of the counters are considered and not just their positiveness. If a sum represented by a counter value cannot be composed of the corresponding variable increment for the queried element, a negative answer can be returned to the query.

### Data synchronization

Bloom filters can be used for approximate data synchronization as in . Counting Bloom filters can be used to approximate the number of differences between two sets and this approach is described in .

### Bloomier filters

designed a generalization of Bloom filters that could associate a value with each element that had been inserted, implementing an associative array. Like Bloom filters, these structures achieve a small space overhead by accepting a small probability of false positives. In the case of "Bloomier filters", a false positive is defined as returning a result when the key is not in the map. The map will never return the wrong value for a key that is in the map.

### Compact approximators

proposed a lattice-based generalization of Bloom filters. A compact approximator associates to each key an element of a lattice (the standard Bloom filters being the case of the Boolean two-element lattice). Instead of a bit array, they have an array of lattice elements. When adding a new association between a key and an element of the lattice, they compute the maximum of the current contents of the k array locations associated to the key with the lattice element. When reading the value associated to a key, they compute the minimum of the values found in the k locations associated to the key. The resulting value approximates from above the original value.

### Stable Bloom filters

proposed Stable Bloom filters as a variant of Bloom filters for streaming data. The idea is that since there is no way to store the entire history of a stream (which can be infinite), Stable Bloom filters continuously evict stale information to make room for more recent elements. Since stale information is evicted, the Stable Bloom filter introduces false negatives, which do not appear in traditional bloom filters. The authors show that a tight upper bound of false positive rates is guaranteed, and the method is superior to standard bloom filters in terms of false positive rates and time efficiency when a small space and an acceptable false positive rate are given.

### Scalable Bloom filters

proposed a variant of Bloom filters that can adapt dynamically to the number of elements stored, while assuring a minimum false positive probability. The technique is based on sequences of standard bloom filters with increasing capacity and tighter false positive probabilities, so as to ensure that a maximum false positive probability can be set beforehand, regardless of the number of elements to be inserted.

### Layered Bloom filters

A layered bloom filter consists of multiple bloom filter layers. Layered bloom filters allow keeping track of how many times an item was added to the bloom filter by checking how many layers contain the item. With a layered bloom filter a check operation will normally return the deepest layer number the item was found in.[15,16]

### Attenuated Bloom filters

An attenuated bloom filter of depth D can be viewed as an array of D normal bloom filters. In the context of service discovery in a network, each node stores regular and attenuated bloom filters locally. The regular or local bloom filter indicates which services are offered by the node itself. The attenuated filter of level i indicates which services can be found on nodes that are i-hops away from the current node. The i-th value is constructed by taking a union of local bloom filters for nodes i-hops away from the node.

Let's take a small network shown on the graph below as an example. Say we are searching for a service A whose id hashes to bits 0,1, and 3 (pattern 11010). Let n1 node to be the starting point. First, we check whether service A is offered by n1 by checking its local filter. Since the patterns don't match, we check the attenuated bloom filter in order to determine which node should be the next hop. We see that n2 doesn't offer service A but lies on the path to nodes that do. Hence, we move to n2 and repeat the same procedure. We quickly find that n3 offers the service, and hence the destination is located.

By using attenuated Bloom filters consisting of multiple layers, services at more than one hop distance can be discovered while avoiding saturation of the Bloom filter by attenuating (shifting out) bits set by sources further away.

### Chemical structure searching

Bloom filters are often used to search large chemical structure databases (see chemical similarity). In the simplest case, the elements added to the filter (called a fingerprint in this field) are just the atomic numbers present in the molecule, or a hash based on the atomic number of each atom and the number and type of its bonds. This case is too simple to be useful. More advanced filters also encode atom counts, larger substructure features like carboxyl groups, and graph properties like the number of rings. In hash-based fingerprints, a hash function based on atom and bond properties is used to turn a subgraph into a PRNG seed, and the first first output values used to set bits in the Bloom filter.

Molecular fingerprints arose as a way to screen out obvious rejects in molecular subgraph searches. They are more often used in calculating molecular similarity, computed as the Tanimoto similarity between their respective fingerprints. The Daylight and Indigo fingerprints, use a variable length (which are restricted to be powers of two) that adapts to the number of items to ensure the final filter is not oversaturated. A length for the filter is chosen to keep the saturation of the filter approximately at a fixed value (for example 30%).

Strictly speaking, the MACCS keys and CACTVS keys are not Bloom filters, rather they are deterministic bit-arrays. Similarly, they are often incorrectly considered to be molecular fingerprints, but they are actually "structural keys". They do not use hash functions, but use a dictionary to map specific substructures to specific indices in the filter. In contrast with Bloom filters, this is a one-to-one mapping that does not use hash functions at all.

### Implementations

Implementation in C from literateprograms.org

Implementation in C++11 on github.com

Implementation in C# from codeplex.com

Implementation in Erlang from sites.google.com

Implementation in Haskell from haskell.org

Implementation in Java on github.com

Implementation in Javascript from la.ma.la

Implementation in JS for node.js on github.com

Implementation in Lisp from lemonodor.com

Implementation in Perl from CPAN

Implementation in PHP from code.google.com

Implementation in Python, Traditional Bloom Filter from pypi.python.org

Implementation in Python, Scalable Bloom Filter from pypi.python.org

Implementation in Ruby from rubyinside.com

Implementation in Scala from codecommit.com

Implementation in Tcl from kocjan.org

Implementation in TypeScript from codeplex.com

References:
[1] .
[2] , pp. 21–22
[3] , pp. 109–111, 308.
[4] , p. 308.
[5] .
[6] .
[7] Yakunin, Alex. (2010-03-25). Alex Yakunin's blog: Nice Bloom filter application. Blog.alexyakunin.com. http://blog.alexyakunin.com/2010/03/nice-bloom-filter-application.html
[8] Issue 10896048: Transition safe browsing from bloom filter to prefix set. - Code Review. Chromiumcodereview.appspot.com. https://chromiumcodereview.appspot.com/10896048/
[9] Wessels, Duane. (January 2004). Squid: The Definitive Guide. O'Reilly Media.
[10] Bitcoin 0.8.0
[11] Core Development Status Report #1
[12] Plan 9 /sys/man/8/venti. Plan9.bell-labs.com. http://plan9.bell-labs.com/magic/man2html/8/venti
[13] http://spinroot.com/
[14] BloomJoin: BloomFilter + CoGroup | LiveRamp Blog. Blog.liveramp.com. http://blog.liveramp.com/2013/04/03/bloomjoin-bloomfilter-cogroup/
[15] pmylund/go-bloom. Github.com. https://github.com/pmylund/go-bloom
[16] First Name Middle Name Last Name. (2010-08-22). IEEE Xplore Abstract - A multi-layer bloom filter for duplicated URL detection. Ieeexplore.ieee.org. doi:10.1109/ICACTE.2010.5578947
````

</details>

<details><summary><b>Step 6 — revision_6</b> (5404 words)</summary>

````text
A Bloom filter is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with a "counting" filter); the more elements that are added to the set, the larger the probability of false positives.

Bloom proposed the technique for applications where the amount of source data would require an impractically large amount of memory if "conventional" error-free hashing techniques were applied. He gave the example of a hyphenation algorithm for a dictionary of 500,000 words, out of which 90% follow simple hyphenation rules, but the remaining 10% require expensive disk accesses to retrieve specific hyphenation patterns. With sufficient core memory, an error-free hash could be used to eliminate all unnecessary disk accesses; on the other hand, with limited core memory, Bloom's technique uses a smaller hash area but still eliminates most unnecessary accesses. For example, a hash area only 15% of the size needed by an ideal error-free hash still eliminates 85% of the disk accesses.

More generally, fewer than 10 bits per element are required for a 1% false positive probability, independent of the size or number of elements in the set.

## Algorithm description

An empty Bloom filter is a bit array of m bits, all set to 0. There must also be k different hash functions defined, each of which maps or hashes some set element to one of the m array positions, generating a uniform random distribution. Typically, k is a constant, much smaller than m, which is proportional to the number of elements to be added; the precise choice of k and the constant of proportionality of m are determined by the intended false positive rate of the filter.

To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To query for an element (test whether it is in the set), feed it to each of the k hash functions to get k array positions. If any of the bits at these positions is 0, the element is definitely not in the set if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have by chance been set to 1 during the insertion of other elements, resulting in a false positive. In a simple Bloom filter, there is no way to distinguish between the two cases, but more advanced techniques can address this problem.

The requirement of designing k different independent hash functions can be prohibitive for large k. For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields. Alternatively, one can pass k different initial values (such as 0, 1, ..., k − 1) to a hash function that takes an initial value; or add (or append) these values to the key. For larger m and/or k, independence among the hash functions can be relaxed with negligible increase in false positive rate.[1] (Specifically, show the effectiveness of deriving the k indices using enhanced double hashing or triple hashing, variants of double hashing that are effectively simple random number generators seeded with the two or three hash values.)

Removing an element from this simple Bloom filter is impossible because false negatives are not permitted. An element maps to k bits, and although setting any one of those k bits to zero suffices to remove the element, it also results in removing any other elements that happen to map onto that bit. Since there is no way of determining whether any other elements have been added that affect the bits for an element to be removed, clearing any of the bits would introduce the possibility for false negatives.

One-time removal of an element from a Bloom filter can be simulated by having a second Bloom filter that contains items that have been removed. However, false positives in the second filter become false negatives in the composite filter, which may be undesirable. In this approach re-adding a previously removed item is not possible, as one would have to remove it from the "removed" filter.

It is often the case that all the keys are available but are expensive to enumerate (for example, requiring many disk reads). When the false positive rate gets too high, the filter can be regenerated; this should be a relatively rare event.

## Space and time advantages

While risking false positives, Bloom filters have a strong space advantage over other data structures for representing sets, such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings ( are an exception, since they can share storage between elements with equal prefixes). However, Bloom filters do not store the data items at all, and a separate solution must be provided for the actual storage. Linked structures incur an additional linear space overhead for pointers. A Bloom filter with 1% error and an optimal value of k, in contrast, requires only about 9.6 bits per element, regardless of the size of the elements. This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. The 1% false-positive rate can be reduced by a factor of ten by adding only about 4.8 bits per element.

However, if the number of potential values is small and many of them can be in the set, the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Note also that hash tables gain a space and time advantage if they begin ignoring collisions and store only whether each bucket contains an entry; in this case, they have effectively become Bloom filters with k = 1.

Bloom filters also have the unusual property that the time needed either to add items or to check whether an item is in the set is a fixed constant, O(k), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

To understand its space efficiency, it is instructive to compare the general Bloom filter with its special case when k = 1. If k = 1, then in order to keep the false positive rate sufficiently low, a small fraction of bits should be set, which means the array must be very large and contain long runs of zeros. The information content of the array relative to its size is low. The generalized Bloom filter (k greater than 1) allows many more bits to be set while still maintaining a low false positive rate; if the parameters (k and m) are chosen well, about half of the bits will be set,[2] and these will be apparently random, minimizing redundancy and maximizing information content.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. If m is the number of bits in the array, the probability that a certain bit is not set to 1 by a certain hash function during the insertion of an element is

1-\frac{1}{m}.

If k is the number of hash functions and each has no significant correlation between each other, then the probability that the bit is not set to 1 by any of the hash functions is

\left(1-\frac{1}{m}\right)^k.

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{m}\right)^{kn};

the probability that it is 1 is therefore

1-\left(1-\frac{1}{m}\right)^{kn}.

Now test membership of an element that is not in the set. Each of the k array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is often given as

\left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k.

This is not strictly correct as it assumes independence for the probabilities of each bit being set. However, assuming it is a close approximation we have that the probability of false positives decreases as m (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases.

An alternative analysis arriving at the same approximation without the assumption of independence is given by Mitzenmacher and Upfal.[3] After all n items have been added to the Bloom filter, let q be the fraction of the m bits that are set to 0. (That is, the number of bits still set to 0 is qm.) Then, when testing membership of an element not in the set, for the array position given by any of the k hash functions, the probability that the bit is found set to 1 is 1-q . So the probability that all k hash functions find their bit set to 1 is (1 - q)^k . Further, the expected value of q is the probability that a given array position is left untouched by each of the k hash functions for each of the n items, which is (as above)

E[q] = \left(1 - \frac{1}{m}\right)^{kn} .

It is possible to prove, without the independence assumption, that q is very strongly concentrated around its expected value. In particular, from the Azuma–Hoeffding inequality, they prove that[4]

\Pr(\left|q - E[q]\right| \ge \frac{\lambda}{m}) \le 2\exp(-2\lambda^2/kn)

Because of this, we can say that the exact probability of false positives is

\sum_{t} \Pr(q = t) (1 - t)^k \approx (1 - E[q])^k = \left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k

as before.

### Optimal number of hash functions

The number of hash functions, k, must be a positive integer. Putting this constraint aside, for a given m and n, the value of k that minimizes the false positive probability is

k = \frac{m}{n} \ln 2.

The required number of bits, m, given n (the number of inserted elements) and a desired false positive probability p (and assuming the optimal value of k is used) can be computed by substituting the optimal value of k in the probability expression above:

p = \left( 1-e^{-(\frac m n \ln 2) \frac n m} \right)^{\frac m n\ln 2}

which can be simplified to:

\ln p = -\frac{m}{n} \left(\ln 2\right)^2.

This results in:

m=-\frac{n\ln p}{(\ln 2)^2}

So the optimal number of bits per element is

\frac{m}{n}=-\frac{\log_2 p}{\ln 2}\approx-1.44{\log_2 p}

with the corresponding number of hash functions k (ignoring integrality):

k=-\frac{\ln p}{\ln 2}=-{\log_2 p}.

This means that for a given false positive probability p, the length of a Bloom filter m is proportionate to the number of elements being filtered n and the required number of hash functions only depends on the target false positive probability p.

The formula m=-\frac{n\ln p}{(\ln 2)^2} is approximate for three reasons. First, and of least concern, it approximates

1 - \frac{1}{m} as e^{-\frac{1}{m}} , which is a good asymptotic approximation (i.e., which holds as m →∞). Second, of more concern, it assumes that during the membership test the event that one tested bit is set to 1 is independent of the event that any other tested bit is set to 1. Third, of most concern, it assumes that k = \frac{m}{n} \ln 2 is fortuitously integral.

Goel and Gupta, however, give a rigorous upper bound that makes no approximations and requires no assumptions. They show that the false positive probability for a finite Bloom filter with m bits ( m > 1 ), n elements, and k hash functions is at most

\left( 1-e^{-\frac{k(n+0.5)}{m-1}} \right)^k.

This bound can be interpreted as saying that the approximate formula \left( 1-e^{-\frac{kn}m} \right)^k can be applied at a penalty of at most half an extra element and at most one fewer bit.

## Approximating the number of items in a Bloom filter

showed that the number of items in a Bloom filter can be approximated with the following formula,

n^* = -\frac{m}{k} \ln \left[ 1 - \frac{X}{m} \right],

where n^* is an estimate of the number of items in the filter, m is the length (size) of the filter, k is the number of hash functions, and X is the number of bits set to one.

## The union and intersection of sets

Bloom filters are a way of compactly representing a set of items. It is common to try to compute the size of the intersection or union between two sets. Bloom filters can be used to approximate the size of the intersection and union of two sets. showed that for two Bloom filters of length m, their counts, respectively can be estimated as

n(A^*) = -\frac{m}{k} \ln \left[ 1 - \frac{n(A)} m \right]

and

n(B^*) = -\frac{m}{k} \ln \left[ 1 - \frac{n(B)} m \right].

The size of their union can be estimated as

n(A^*\cup B^*) = -\frac{m}{k} \ln \left[ 1 - \frac{n(A \cup B)} m \right],

where n(A \cup B) is the number of bits set to one in either of the two Bloom filters. Finally, the intersection can be estimated as

n(A^*\cap B^*) = n(A^*) + n(B^*) - n(A^* \cup B^*),

using the three formulas together.

## Interesting properties

Unlike a standard hash table, a Bloom filter of a fixed size can represent a set with an arbitrarily large number of elements; adding an element never fails due to the data structure "filling up". However, the false positive rate increases steadily as elements are added until all bits in the filter are set to 1, at which point all queries yield a positive result.

Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations respectively. The union operation on Bloom filters is lossless in the sense that the resulting Bloom filter is the same as the Bloom filter created from scratch using the union of the two sets. The intersect operation satisfies a weaker property: the false positive probability in the resulting Bloom filter is at most the false-positive probability in one of the constituent Bloom filters, but may be larger than the false positive probability in the Bloom filter created from scratch using the intersection of the two sets.

Some kinds of superimposed code can be seen as a Bloom filter implemented with physical edge-notched cards. An example is Zatocoding, invented by Calvin Mooers in 1947, in which the set of categories associated with a piece of information is represented by notches on a card, with a random pattern of four notches for each category.

## Examples

Akamai's web servers use Bloom filters to prevent "one-hit-wonders" from being stored in its disk caches. One-hit-wonders are web objects requested by users just once, something that Akamai found applied to nearly three-quarters of their caching infrastructure. Using a Bloom filter to detect the second request for a web object and caching that object only on its second request prevents one-hit wonders from entering the disk cache, significantly reducing disk workload and increasing disk cache hit rates.

Google Bigtable, Apache HBase and Apache Cassandra, and Postgresql[5] use Bloom filters to reduce the disk lookups for non-existent rows or columns. Avoiding costly disk lookups considerably increases the performance of a database query operation.[6]

The Google Chrome web browser used to use a Bloom filter to identify malicious URLs. Any URL was first checked against a local Bloom filter, and only if the Bloom filter returned a positive result was a full check of the URL performed (and the user warned, if that too returned a positive result).[7,8]

The Squid Web Proxy Cache uses Bloom filters for cache digests.

Bitcoin uses Bloom filters to speed up wallet synchronization.[9]

The Venti archival storage system uses Bloom filters to detect previously stored data.[10]

The SPIN model checker uses Bloom filters to track the reachable state space for large verification problems.[11]

The Cascading analytics framework uses Bloom filters to speed up asymmetric joins, where one of the joined data sets is significantly larger than the other (often called Bloom join in the database literature).

The Exim mail transfer agent (MTA) uses Bloom filters in its rate-limit feature.[12]

Medium uses Bloom filters to avoid recommending articles a user has previously read.[13]

Ethereum uses Bloom filters for quickly finding logs on the Ethereum blockchain.

## Alternatives

Classic Bloom filters use 1.44\log_2(1/\epsilon) bits of space per inserted key, where \epsilon is the false positive rate of the Bloom filter. However, the space that is strictly necessary for any data structure playing the same role as a Bloom filter is only \log_2(1/\epsilon) per key. Hence Bloom filters use 44 % more space than an equivalent optimal data structure. Instead, Pagh et al. provide an optimal-space data structure. Moreover, their data structure has constant locality of reference independent of the false positive rate, unlike Bloom filters, where a smaller false positive rate \epsilon leads to a greater number of memory accesses per query, \log(1/\epsilon) . Also, it allows elements to be deleted without a space penalty, unlike Bloom filters. The same improved properties of optimal space usage, constant locality of reference, and the ability to delete elements are also provided by the cuckoo filter of , an open source implementation of which is available.

describe a probabilistic structure based on hash tables, hash compaction, which identify as significantly more accurate than a Bloom filter when each is configured optimally. Dillinger and Manolios, however, point out that the reasonable accuracy of any given Bloom filter over a wide range of numbers of additions makes it attractive for probabilistic enumeration of state spaces of unknown size. Hash compaction is, therefore, attractive when the number of additions can be predicted accurately; however, despite being very fast in software, hash compaction is poorly suited for hardware because of worst-case linear access time.

have studied some variants of Bloom filters that are either faster or use less space than classic Bloom filters. The basic idea of the fast variant is to locate the k hash values associated with each key into one or two blocks having the same size as processor's memory cache blocks (usually 64 bytes). This will presumably improve performance by reducing the number of potential memory cache misses. The proposed variants have however the drawback of using about 32 % more space than classic Bloom filters.

The space efficient variant relies on using a single hash function that generates for each key a value in the range \left[0,n/\varepsilon\right] where \epsilon is the requested false positive rate. The sequence of values is then sorted and compressed using Golomb coding (or some other compression technique) to occupy a space close to n\log_2(1/\epsilon) bits. To query the Bloom filter for a given key, it will suffice to check if its corresponding value is stored in the Bloom filter. Decompressing the whole Bloom filter for each query would make this variant totally unusable. To overcome this problem the sequence of values is divided into small blocks of equal size that are compressed separately. At query time only half a block will need to be decompressed on average. Because of decompression overhead, this variant may be slower than classic Bloom filters but this may be compensated by the fact that a single hash function need to be computed.

Another alternative to classic Bloom filter is the one based on space efficient variants of cuckoo hashing. In this case once the hash table is constructed, the keys stored in the hash table are replaced with short signatures of the keys. Those signatures are strings of bits computed using a hash function applied on the keys.

## Extensions and applications

### Cache filtering

Content delivery networks deploy web caches around the world to cache and serve web content to users with greater performance and reliability. A key application of Bloom filters is their use in efficiently determining which web objects to store in these web caches. Nearly three-quarters of the URLs accessed from a typical web cache are "one-hit-wonders" that are accessed by users only once and never again. It is clearly wasteful of disk resources to store one-hit-wonders in a web cache, since they will never be accessed again. To prevent caching one-hit-wonders, a Bloom filter is used to keep track of all URLs that are accessed by users. A web object is cached only when it has been accessed at least once before, i.e., the object is cached on its second request. The use of a Bloom filter in this fashion significantly reduces the disk write workload, since one-hit-wonders are never written to the disk cache. Further, filtering out the one-hit-wonders also saves cache space on disk, increasing the cache hit rates.

### Avoiding False Positives in a Finite Universe

Kiss et al. described a new construction for the Bloom filter that avoids false positives in addition to the typical non-existence of false negatives. The construction applies to a finite universe from which set elements are taken. It relies on existing non-adaptive combinatorial group testing scheme by Eppstein, Goodrich and Hirschberg. Unlike the typical Bloom filter, elements are hashed to a bit array through deterministic, fast and simple-to-calculate functions. The maximal set size for which false positives are completely avoided is a function of the universe size and is controlled by the amount of allocated memory.

### Counting filters

Counting filters provide a way to implement a delete operation on a Bloom filter without recreating the filter afresh. In a counting filter the array positions (buckets) are extended from being a single bit to being an n-bit counter. In fact, regular Bloom filters can be considered as counting filters with a bucket size of one bit. Counting filters were introduced by .

The insert operation is extended to increment the value of the buckets, and the lookup operation checks that each of the required buckets is non-zero. The delete operation then consists of decrementing the value of each of the respective buckets.

Arithmetic overflow of the buckets is a problem and the buckets should be sufficiently large to make this case rare. If it does occur then the increment and decrement operations must leave the bucket set to the maximum possible value in order to retain the properties of a Bloom filter.

The size of counters is usually 3 or 4 bits. Hence counting Bloom filters use 3 to 4 times more space than static Bloom filters. In contrast, the data structures of and also allow deletions but use less space than a static Bloom filter.

Another issue with counting filters is limited scalability. Because the counting Bloom filter table cannot be expanded, the maximal number of keys to be stored simultaneously in the filter must be known in advance. Once the designed capacity of the table is exceeded, the false positive rate will grow rapidly as more keys are inserted.

introduced a data structure based on d-left hashing that is functionally equivalent but uses approximately half as much space as counting Bloom filters. The scalability issue does not occur in this data structure. Once the designed capacity is exceeded, the keys could be reinserted in a new hash table of double size.

The space efficient variant by could also be used to implement counting filters by supporting insertions and deletions.

introduced a new general method based on variable increments that significantly improves the false positive probability of counting Bloom filters and their variants, while still supporting deletions. Unlike counting Bloom filters, at each element insertion, the hashed counters are incremented by a hashed variable increment instead of a unit increment. To query an element, the exact values of the counters are considered and not just their positiveness. If a sum represented by a counter value cannot be composed of the corresponding variable increment for the queried element, a negative answer can be returned to the query.

### Decentralized aggregation

Bloom filters can be organized in distributed data structures to perform fully decentralized computations of aggregate functions. Decentralized aggregation makes collective measurements locally available in every node of a distributed network without involving a centralized computational entity for this purpose.

### Data synchronization

Bloom filters can be used for approximate data synchronization as in . Counting Bloom filters can be used to approximate the number of differences between two sets and this approach is described in .

### Bloomier filters

designed a generalization of Bloom filters that could associate a value with each element that had been inserted, implementing an associative array. Like Bloom filters, these structures achieve a small space overhead by accepting a small probability of false positives. In the case of "Bloomier filters", a false positive is defined as returning a result when the key is not in the map. The map will never return the wrong value for a key that is in the map.

### Compact approximators

proposed a lattice-based generalization of Bloom filters. A compact approximator associates to each key an element of a lattice (the standard Bloom filters being the case of the Boolean two-element lattice). Instead of a bit array, they have an array of lattice elements. When adding a new association between a key and an element of the lattice, they compute the maximum of the current contents of the k array locations associated to the key with the lattice element. When reading the value associated to a key, they compute the minimum of the values found in the k locations associated to the key. The resulting value approximates from above the original value.

### Stable Bloom filters

proposed Stable Bloom filters as a variant of Bloom filters for streaming data. The idea is that since there is no way to store the entire history of a stream (which can be infinite), Stable Bloom filters continuously evict stale information to make room for more recent elements. Since stale information is evicted, the Stable Bloom filter introduces false negatives, which do not appear in traditional Bloom filters. The authors show that a tight upper bound of false positive rates is guaranteed, and the method is superior to standard Bloom filters in terms of false positive rates and time efficiency when a small space and an acceptable false positive rate are given.

### Scalable Bloom filters

proposed a variant of Bloom filters that can adapt dynamically to the number of elements stored, while assuring a minimum false positive probability. The technique is based on sequences of standard Bloom filters with increasing capacity and tighter false positive probabilities, so as to ensure that a maximum false positive probability can be set beforehand, regardless of the number of elements to be inserted.

### Spatial Bloom filters

Spatial Bloom filters (SBF) were originally proposed by as a data structure designed to store location information, especially in the context of cryptographic protocols for location privacy. However, the main characteristic of SBFs is their ability to store multiple sets in a single data structure, which makes them suitable for a number of different application scenarios. Membership of an element to a specific set can be queried, and the false positive probability depends on the set: the first sets to be entered into the filter during construction have higher false positive probabilities than sets entered at the end. This property allows a prioritization of the sets, where sets containing more "important" elements can be preserved.

### Layered Bloom filters

A layered Bloom filter consists of multiple Bloom filter layers. Layered Bloom filters allow keeping track of how many times an item was added to the Bloom filter by checking how many layers contain the item. With a layered Bloom filter a check operation will normally return the deepest layer number the item was found in.

### Attenuated Bloom filters

An attenuated Bloom filter of depth D can be viewed as an array of D normal Bloom filters. In the context of service discovery in a network, each node stores regular and attenuated Bloom filters locally. The regular or local Bloom filter indicates which services are offered by the node itself. The attenuated filter of level i indicates which services can be found on nodes that are i-hops away from the current node. The i-th value is constructed by taking a union of local Bloom filters for nodes i-hops away from the node.

Let's take a small network shown on the graph below as an example. Say we are searching for a service A whose id hashes to bits 0,1, and 3 (pattern 11010). Let n1 node to be the starting point. First, we check whether service A is offered by n1 by checking its local filter. Since the patterns don't match, we check the attenuated Bloom filter in order to determine which node should be the next hop. We see that n2 doesn't offer service A but lies on the path to nodes that do. Hence, we move to n2 and repeat the same procedure. We quickly find that n3 offers the service, and hence the destination is located.

By using attenuated Bloom filters consisting of multiple layers, services at more than one hop distance can be discovered while avoiding saturation of the Bloom filter by attenuating (shifting out) bits set by sources further away.

### Chemical structure searching

Bloom filters are often used to search large chemical structure databases (see chemical similarity). In the simplest case, the elements added to the filter (called a fingerprint in this field) are just the atomic numbers present in the molecule, or a hash based on the atomic number of each atom and the number and type of its bonds. This case is too simple to be useful. More advanced filters also encode atom counts, larger substructure features like carboxyl groups, and graph properties like the number of rings. In hash-based fingerprints, a hash function based on atom and bond properties is used to turn a subgraph into a PRNG seed, and the first output values used to set bits in the Bloom filter.

Molecular fingerprints started in the late 1940s as way to search for chemical structures searched on punched cards. However, it wasn't until around 1990 that Daylight introduced a hash-based method to generate the bits, rather than use a precomputed table. Unlike the dictionary approach, the hash method can assign bits for substructures which hadn't previously been seen. In the early 1990s, the term "fingerprint" was considered different from "structural keys", but the term has since grown to encompass most molecular characteristics which can be used for a similarity comparison, including structural keys, sparse count fingerprints, and 3D fingerprints. Unlike Bloom filters, the Daylight hash method allows the number of bits assigned per feature to be a function of the feature size, but most implementations of Daylight-like fingerprints use a fixed number of bits per feature, which makes them a Bloom filter. The original Daylight fingerprints could be used for both similarity and screening purposes. Many other fingerprint types, like the popular ECFP2, can be used for similarity but not for screening because they include local environmental characteristics that introduce false negatives when used as a screen. Even if these are constructed with the same mechanism, these are not Bloom filters because they cannot be used to filter.

References:
[1] ; .
[2] , pp. 21–22
[3] , pp. 109–111, 308.
[4] , p. 308.
[5] (2016-04-01). "Bloom index contrib module". Postgresql.org. https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=9ee014fc899a28a198492b074e32b60ed8915ea9
[6] ; .
[7] Yakunin, Alex. (2010-03-25). Alex Yakunin's blog: Nice Bloom filter application. Blog.alexyakunin.com. http://blog.alexyakunin.com/2010/03/nice-bloom-filter-application.html
[8] Issue 10896048: Transition safe browsing from bloom filter to prefix set. - Code Review. Chromiumcodereview.appspot.com. https://chromiumcodereview.appspot.com/10896048/
[9] (2012-10-24). BIP 0037. https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki
[10] Plan 9 /sys/man/8/venti. Plan9.bell-labs.com. http://plan9.bell-labs.com/magic/man2html/8/venti
[11] http://spinroot.com/
[12] Exim source code. github. https://github.com/Exim/exim/blob/master/src/src/acl.c#L2627
[13] What are Bloom filters?. Medium. https://medium.com/the-story/what-are-bloom-filters-1ec2a50c68ff#.xlkqtn1vy
````

</details>

<details><summary><b>Step 7 — revision_7</b> (6937 words)</summary>

````text
A Bloom filter is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with the counting Bloom filter variant); the more items added, the larger the probability of false positives.

Bloom proposed the technique for applications where the amount of source data would require an impractically large amount of memory if "conventional" error-free hashing techniques were applied. He gave the example of a hyphenation algorithm for a dictionary of 500,000 words, out of which 90% follow simple hyphenation rules, but the remaining 10% require expensive disk accesses to retrieve specific hyphenation patterns. With sufficient core memory, an error-free hash could be used to eliminate all unnecessary disk accesses; on the other hand, with limited core memory, Bloom's technique uses a smaller hash area but still eliminates most unnecessary accesses. For example, a hash area only 15% of the size needed by an ideal error-free hash still eliminates 85% of the disk accesses.

More generally, fewer than 10 bits per element are required for a 1% false positive probability, independent of the size or number of elements in the set.

## Algorithm description

An empty Bloom filter is a bit array of m bits, all set to 0. There must also be k different hash functions defined, each of which maps or hashes some set element to one of the m array positions, generating a uniform random distribution. Typically, k is a small constant which depends on the desired false error rate ε, while m is proportional to k and the number of elements to be added.

To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To query for an element (test whether it is in the set), feed it to each of the k hash functions to get k array positions. If any of the bits at these positions is 0, the element is definitely not in the set; if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have by chance been set to 1 during the insertion of other elements, resulting in a false positive. In a simple Bloom filter, there is no way to distinguish between the two cases, but more advanced techniques can address this problem.

The requirement of designing k different independent hash functions can be prohibitive for large k. For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields. Alternatively, one can pass k different initial values (such as 0, 1, ..., k − 1) to a hash function that takes an initial value; or add (or append) these values to the key. For larger m and/or k, independence among the hash functions can be relaxed with negligible increase in false positive rate.[1] (Specifically, show the effectiveness of deriving the k indices using enhanced double hashing or triple hashing, variants of double hashing that are effectively simple random number generators seeded with the two or three hash values.)

Removing an element from this simple Bloom filter is impossible because there is no way to tell which of the k bits it maps to should be cleared. Although setting any one of those k bits to zero suffices to remove the element, it would also remove any other elements that happen to map onto that bit. Since the simple algorithm provides no way to determine whether any other elements have been added that affect the bits for the element to be removed, clearing any of the bits would introduce the possibility of false negatives.

One-time removal of an element from a Bloom filter can be simulated by having a second Bloom filter that contains items that have been removed. However, false positives in the second filter become false negatives in the composite filter, which may be undesirable. In this approach re-adding a previously removed item is not possible, as one would have to remove it from the "removed" filter.

It is often the case that all the keys are available but are expensive to enumerate (for example, requiring many disk reads). When the false positive rate gets too high, the filter can be regenerated; this should be a relatively rare event.

## Space and time advantages

While risking false positives, Bloom filters have a substantial space advantage over other data structures for representing sets, such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings ( are an exception since they can share storage between elements with equal prefixes). However, Bloom filters do not store the data items at all, and a separate solution must be provided for the actual storage. Linked structures incur an additional linear space overhead for pointers. A Bloom filter with a 1% error and an optimal value of k, in contrast, requires only about 9.6 bits per element, regardless of the size of the elements. This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. The 1% false-positive rate can be reduced by a factor of ten by adding only about 4.8 bits per element.

However, if the number of potential values is small and many of them can be in the set, the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Hash tables gain a space and time advantage if they begin ignoring collisions and store only whether each bucket contains an entry; in this case, they have effectively become Bloom filters with k = 1.

Bloom filters also have the unusual property that the time needed either to add items or to check whether an item is in the set is a fixed constant, O(k), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

To understand its space efficiency, it is instructive to compare the general Bloom filter with its special case when k = 1. If k = 1, then in order to keep the false positive rate sufficiently low, a small fraction of bits should be set, which means the array must be very large and contain long runs of zeros. The information content of the array relative to its size is low. The generalized Bloom filter (k greater than 1) allows many more bits to be set while still maintaining a low false positive rate; if the parameters (k and m) are chosen well, about half of the bits will be set,[2] and these will be apparently random, minimizing redundancy and maximizing information content.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. If m is the number of bits in the array, the probability that a certain bit is not set to 1 by a certain hash function during the insertion of an element is

1-\frac{1}{m}.

If k is the number of hash functions and each has no significant correlation between each other, then the probability that the bit is not set to 1 by any of the hash functions is

\left(1-\frac{1}{m}\right)^k.

We can use the well-known identity for e−1

\lim_{m\to\infty} \left(1 - \frac{1}{m}\right)^m = \frac{1}{e}

to conclude that, for large m,

\left(1-\frac{1}{m}\right)^k = \left(\left(1-\frac{1}{m}\right)^m\right)^{k/m} \approx e^{-k/m}.

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{m}\right)^{kn} \approx e^{-kn/m};

the probability that it is 1 is therefore

1-\left(1-\frac{1}{m}\right)^{kn} \approx 1 - e^{-kn/m}.

Now test membership of an element that is not in the set. Each of the k array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is often given as

\varepsilon = \left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k.

This is not strictly correct as it assumes independence for the probabilities of each bit being set. However, assuming it is a close approximation we have that the probability of false positives decreases as m (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases.

An alternative analysis arriving at the same approximation without the assumption of independence is given by Mitzenmacher and Upfal.[3] After all n items have been added to the Bloom filter, let q be the fraction of the m bits that are set to 0. (That is, the number of bits still set to 0 is qm.) Then, when testing membership of an element not in the set, for the array position given by any of the k hash functions, the probability that the bit is found set to 1 is 1-q . So the probability that all k hash functions find their bit set to 1 is (1 - q)^k . Further, the expected value of q is the probability that a given array position is left untouched by each of the k hash functions for each of the n items, which is (as above)

E[q] = \left(1 - \frac{1}{m}\right)^{kn} .

It is possible to prove, without the independence assumption, that q is very strongly concentrated around its expected value. In particular, from the Azuma–Hoeffding inequality, they prove that[4]

\Pr(\left|q - E[q]\right| \ge \frac{\lambda}{m}) \le 2\exp(-2\lambda^2/kn)

Because of this, we can say that the exact probability of false positives is

\sum_{t} \Pr(q = t) (1 - t)^k \approx (1 - E[q])^k = \left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k

as before.

### Optimal number of hash functions

The number of hash functions, k, must be a positive integer. Putting this constraint aside, for a given m and n, the value of k that minimizes the false positive probability is

k = \frac{m}{n} \ln 2.

The required number of bits, m, given n (the number of inserted elements) and a desired false positive probability ε (and assuming the optimal value of k is used) can be computed by substituting the optimal value of k in the probability expression above:

\varepsilon = \left( 1-e^{-(\frac m n \ln 2) \frac n m} \right)^{\frac m n\ln 2}

which can be simplified to:

\ln\varepsilon = -\frac{m}{n} \left(\ln 2\right)^2.

This results in:

m=-\frac{n\ln\varepsilon}{(\ln 2)^2}

So the optimal number of bits per element is

\frac{m}{n}=-\frac{\log_2\varepsilon}{\ln 2}\approx-1.44\log_2\varepsilon

with the corresponding number of hash functions k (ignoring integrality):

k=-\frac{\ln\varepsilon}{\ln 2}=-\log_2\varepsilon.

This means that for a given false positive probability ε, the length of a Bloom filter m is proportionate to the number of elements being filtered n and the required number of hash functions only depends on the target false positive probability ε.

The formula m=-\frac{n\ln\varepsilon}{(\ln 2)^2} is approximate for three reasons. First, and of least concern, it approximates

1 - \frac{1}{m} as e^{-\frac{1}{m}} , which is a good asymptotic approximation (i.e., which holds as m →∞). Second, of more concern, it assumes that during the membership test the event that one tested bit is set to 1 is independent of the event that any other tested bit is set to 1. Third, of most concern, it assumes that k = \frac{m}{n} \ln 2 is fortuitously integral.

Goel and Gupta, however, give a rigorous upper bound that makes no approximations and requires no assumptions. They show that the false positive probability for a finite Bloom filter with m bits ( m > 1 ), n elements, and k hash functions is at most

\varepsilon \leq \left( 1-e^{-\frac{k(n+0.5)}{m-1}} \right)^k.

This bound can be interpreted as saying that the approximate formula \left( 1-e^{-\frac{kn}m} \right)^k can be applied at a penalty of at most half an extra element and at most one fewer bit.

## Approximating the number of items in a Bloom filter

showed that the number of items in a Bloom filter can be approximated with the following formula,

n^* = -\frac{m}{k} \ln \left[ 1 - \frac{X}{m} \right],

where n^* is an estimate of the number of items in the filter, m is the length (size) of the filter, k is the number of hash functions, and X is the number of bits set to one.

### The union and intersection of sets

Bloom filters are a way of compactly representing a set of items. It is common to try to compute the size of the intersection or union between two sets. Bloom filters can be used to approximate the size of the intersection and union of two sets. showed that for two Bloom filters of length m, their counts, respectively can be estimated as

n(A^*) = -\frac{m}{k} \ln \left[ 1 - \frac m \right]

and

n(B^*) = -\frac{m}{k} \ln \left[ 1 - \frac m \right].

The size of their union can be estimated as

n(A^*\cup B^*) = -\frac{m}{k} \ln \left[ 1 - \frac m \right],

where n(A \cup B) is the number of bits set to one in either of the two Bloom filters. Finally, the intersection can be estimated as

n(A^*\cap B^*) = n(A^*) + n(B^*) - n(A^* \cup B^*),

using the three formulas together.

## Interesting properties

Unlike a standard hash table using open addressing for collision resolution, a Bloom filter of a fixed size can represent a set with an arbitrarily large number of elements; adding an element never fails due to the data structure "filling up". However, the false positive rate increases steadily as elements are added until all bits in the filter are set to 1, at which point all queries yield a positive result. With open addressing hashing, false positives are never produced, but performance steadily deteriorates until it approaches linear search.

Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations, respectively. The union operation on Bloom filters is lossless in the sense that the resulting Bloom filter is the same as the Bloom filter created from scratch using the union of the two sets. The intersect operation satisfies a weaker property: the false positive probability in the resulting Bloom filter is at most the false-positive probability in one of the constituent Bloom filters, but may be larger than the false positive probability in the Bloom filter created from scratch using the intersection of the two sets.

Some kinds of superimposed code can be seen as a Bloom filter implemented with physical edge-notched cards. An example is Zatocoding, invented by Calvin Mooers in 1947, in which the set of categories associated with a piece of information is represented by notches on a card, with a random pattern of four notches for each category.

## Examples

Fruit flies use a modified version of Bloom filters to detect novelty of odors, with additional features including similarity of novel odor to that of previously experienced examples, and time elapsed since previous experience of the same odor.[5]

The servers of Akamai Technologies, a content delivery provider, use Bloom filters to prevent "one-hit-wonders" from being stored in its disk caches. One-hit-wonders are web objects requested by users just once, something that Akamai found applied to nearly three-quarters of their caching infrastructure. Using a Bloom filter to detect the second request for a web object and caching that object only on its second request prevents one-hit wonders from entering the disk cache, significantly reducing disk workload and increasing disk cache hit rates.

Google Bigtable, Apache HBase and Apache Cassandra and PostgreSQL[6] use Bloom filters to reduce the disk lookups for non-existent rows or columns. Avoiding costly disk lookups considerably increases the performance of a database query operation.[7]

The Google Chrome web browser used to use a Bloom filter to identify malicious URLs. Any URL was first checked against a local Bloom filter, and only if the Bloom filter returned a positive result was a full check of the URL performed (and the user warned, if that too returned a positive result).[8,9]

Microsoft Bing (search engine) uses multi-level hierarchical Bloom filters for its search index, BitFunnel. Bloom filters provided lower cost than the previous Bing index, which was based on inverted files.[10]

The Squid Web Proxy Cache uses Bloom filters for cache digests.

Bitcoin used Bloom filters to speed up wallet synchronization until privacy vulnerabilities with the implementation of Bloom filters were discovered.[11,12]

The Venti archival storage system uses Bloom filters to detect previously stored data.[13]

The SPIN model checker uses Bloom filters to track the reachable state space for large verification problems.[14]

The Cascading analytics framework uses Bloom filters to speed up asymmetric joins, where one of the joined data sets is significantly larger than the other (often called Bloom join in the database literature).

The Exim mail transfer agent (MTA) uses Bloom filters in its rate-limit feature.[15]

Medium uses Bloom filters to avoid recommending articles a user has previously read.[16]

Ethereum uses Bloom filters for quickly finding logs on the Ethereum blockchain.

## Alternatives

Classic Bloom filters use 1.44\log_2(1/\varepsilon) bits of space per inserted key, where \varepsilon is the false positive rate of the Bloom filter. However, the space that is strictly necessary for any data structure playing the same role as a Bloom filter is only \log_2(1/\varepsilon) per key. Hence Bloom filters use 44% more space than an equivalent optimal data structure. Instead, Pagh et al. provide an optimal-space data structure. Moreover, their data structure has constant locality of reference independent of the false positive rate, unlike Bloom filters, where a lower false positive rate \varepsilon leads to a greater number of memory accesses per query, \log(1/\varepsilon) . Also, it allows elements to be deleted without a space penalty, unlike Bloom filters. The same improved properties of optimal space usage, constant locality of reference, and the ability to delete elements are also provided by the cuckoo filter of , an open source implementation of which is available.

describe a probabilistic structure based on hash tables, hash compaction, which identify as significantly more accurate than a Bloom filter when each is configured optimally. Dillinger and Manolios, however, point out that the reasonable accuracy of any given Bloom filter over a wide range of numbers of additions makes it attractive for probabilistic enumeration of state spaces of unknown size. Hash compaction is, therefore, attractive when the number of additions can be predicted accurately; however, despite being very fast in software, hash compaction is poorly suited for hardware because of worst-case linear access time.

have studied some variants of Bloom filters that are either faster or use less space than classic Bloom filters. The basic idea of the fast variant is to locate the k hash values associated with each key into one or two blocks having the same size as processor's memory cache blocks (usually 64 bytes). This will presumably improve performance by reducing the number of potential memory cache misses. The proposed variants have however the drawback of using about 32% more space than classic Bloom filters.

The space efficient variant relies on using a single hash function that generates for each key a value in the range \left[0,n/\varepsilon\right] where \varepsilon is the requested false positive rate. The sequence of values is then sorted and compressed using Golomb coding (or some other compression technique) to occupy a space close to n\log_2(1/\varepsilon) bits. To query the Bloom filter for a given key, it will suffice to check if its corresponding value is stored in the Bloom filter. Decompressing the whole Bloom filter for each query would make this variant totally unusable. To overcome this problem the sequence of values is divided into small blocks of equal size that are compressed separately. At query time only half a block will need to be decompressed on average. Because of decompression overhead, this variant may be slower than classic Bloom filters but this may be compensated by the fact that a single hash function need to be computed.

Another alternative to classic Bloom filter is the cuckoo filter, based on space-efficient variants of cuckoo hashing. In this case, a hash table is constructed, holding neither keys nor values, but short fingerprints (small hashes) of the keys. If looking up the key finds a matching fingerprint, then key is probably in the set. One useful property of cuckoo filters is that they are updatable; entries may be dynamically added (with a small probability of failure due to the hash table being full) and removed.

describes an approach called an xor filter, where they store fingerprints in a particular type of perfect hash table, producing a filter which is more memory efficient ( 1.23\log_2(1/\varepsilon) bits per key) and faster than Bloom or cuckoo filters. (The time saving comes from the fact that a lookup requires exactly three memory accesses, which can all execute in parallel.) However, filter creation is more complex than Bloom and cuckoo filters, and it is not possible to modify the set after creation.

## Extensions and applications

There are over 60 variants of Bloom filters, many surveys of the field, and a continuing churn of applications (see e.g., Luo, et al [17]). Some of the variants differ sufficiently from the original proposal to be breaches from or forks of the original data structure and its philosophy.[17] A treatment which unifies Bloom filters with other work on random projections, compressive sensing, and locality sensitive hashing remains to be done (though see Dasgupta, et al[18] for one attempt inspired by neuroscience).

### Cache filtering

Content delivery networks deploy web caches around the world to cache and serve web content to users with greater performance and reliability. A key application of Bloom filters is their use in efficiently determining which web objects to store in these web caches. Nearly three-quarters of the URLs accessed from a typical web cache are "one-hit-wonders" that are accessed by users only once and never again. It is clearly wasteful of disk resources to store one-hit-wonders in a web cache, since they will never be accessed again. To prevent caching one-hit-wonders, a Bloom filter is used to keep track of all URLs that are accessed by users. A web object is cached only when it has been accessed at least once before, i.e., the object is cached on its second request. The use of a Bloom filter in this fashion significantly reduces the disk write workload, since one-hit-wonders are never written to the disk cache. Further, filtering out the one-hit-wonders also saves cache space on disk, increasing the cache hit rates.

### Avoiding false positives in a finite universe

Kiss et al [19] described a new construction for the Bloom filter that avoids false positives in addition to the typical non-existence of false negatives. The construction applies to a finite universe from which set elements are taken. It relies on existing non-adaptive combinatorial group testing scheme by Eppstein, Goodrich and Hirschberg. Unlike the typical Bloom filter, elements are hashed to a bit array through deterministic, fast and simple-to-calculate functions. The maximal set size for which false positives are completely avoided is a function of the universe size and is controlled by the amount of allocated memory.

### Counting Bloom filters

Counting filters provide a way to implement a delete operation on a Bloom filter without recreating the filter afresh. In a counting filter, the array positions (buckets) are extended from being a single bit to being an multibit counter. In fact, regular Bloom filters can be considered as counting filters with a bucket size of one bit. Counting filters were introduced by .

The insert operation is extended to increment the value of the buckets, and the lookup operation checks that each of the required buckets is non-zero. The delete operation then consists of decrementing the value of each of the respective buckets.

Arithmetic overflow of the buckets is a problem and the buckets should be sufficiently large to make this case rare. If it does occur then the increment and decrement operations must leave the bucket set to the maximum possible value in order to retain the properties of a Bloom filter.

The size of counters is usually 3 or 4 bits. Hence counting Bloom filters use 3 to 4 times more space than static Bloom filters. In contrast, the data structures of and also allow deletions but use less space than a static Bloom filter.

Another issue with counting filters is limited scalability. Because the counting Bloom filter table cannot be expanded, the maximal number of keys to be stored simultaneously in the filter must be known in advance. Once the designed capacity of the table is exceeded, the false positive rate will grow rapidly as more keys are inserted.

introduced a data structure based on d-left hashing that is functionally equivalent but uses approximately half as much space as counting Bloom filters. The scalability issue does not occur in this data structure. Once the designed capacity is exceeded, the keys could be reinserted in a new hash table of double size.

The space efficient variant by could also be used to implement counting filters by supporting insertions and deletions.

introduced a new general method based on variable increments that significantly improves the false positive probability of counting Bloom filters and their variants, while still supporting deletions. Unlike counting Bloom filters, at each element insertion, the hashed counters are incremented by a hashed variable increment instead of a unit increment. To query an element, the exact values of the counters are considered and not just their positiveness. If a sum represented by a counter value cannot be composed of the corresponding variable increment for the queried element, a negative answer can be returned to the query.

Kim et al. (2019) shows that false positive of Counting Bloom filter decreases from k=1 to a point defined k_{opt} , and increases from k_{opt} to positive infinity, and finds k_{opt} as a function of count threshold.[20]

### Decentralized aggregation

Bloom filters can be organized in distributed data structures to perform fully decentralized computations of aggregate functions. Decentralized aggregation makes collective measurements locally available in every node of a distributed network without involving a centralized computational entity for this purpose.

### Distributed Bloom filters

Parallel Bloom filters can be implemented to take advantage of the multiple processing elements (PEs) present in parallel shared-nothing machines. One of the main obstacles for a parallel Bloom filter is the organization and communication of the unordered data which is, in general, distributed evenly over all PEs at the initiation or at batch insertions. To order the data two approaches can be used, either resulting in a Bloom filter over all data being stored on each PE, called replicating bloom filter, or the Bloom filter over all data being split into equal parts, each PE storing one part of it.[21] For both approaches a "Single Shot" Bloom filter is used which only calculates one hash, resulting in one flipped bit per element, to reduce the communication volume.

Distributed Bloom filters are initiated by first hashing all elements on their local PE and then sorting them by their hashes locally. This can be done in linear time using e.g. Bucket sort and also allows local duplicate detection. The sorting is used to group the hashes with their assigned PE as separator to create a Bloom filter for each group. After encoding these Bloom filters using e.g. Golomb coding each bloom filter is send as packet to the PE responsible for the hash values that where inserted into it. A PE p is responsible for all hashes between the values p*(s/|\text{PE}|) and (p+1)*(s/|\text{PE}|) , where s is the total size of the Bloom filter over all data. Because each element is only hashed once and therefore only a single bit is set, to check if an element was inserted into the Bloom filter only the PE responsible for the hash value of the element needs to be operated on. Single insertion operations can also be done efficiently because the Bloom filter of only one PE has to be changed, compared to Replicating Bloom filters where every PE would have to update its Bloom filter.

By distributing the global Bloom filter over all PEs instead of storing it separately on each PE the Bloom filters size can be far larger, resulting in a larger capacity and lower false positive rate.

Distributed Bloom filters can be used to improve duplicate detection algorithms[22] by filtering out the most 'unique' elements. These can be calculated by communicating only the hashes of elements, not the elements themselves which are far larger in volume, and removing them from the set, reducing the workload for the duplicate detection algorithm used afterwards.

During the communication of the hashes the PEs search for bits that are set in more than one of the receiving packets, as this would mean that two elements had the same hash and therefore could be duplicates. If this occurs a message containing the index of the bit, which is also the hash of the element that could be a duplicate, is send to the PEs which sent a packet with the set bit. If multiple indices are send to the same PE by one sender it can be advantageous to encode the indices as well. All elements that didn't have their hash sent back are now guaranteed to not be a duplicate and won't be evaluated further, for the remaining elements a Repartitioning algorithm[23] can be used. First all the elements that had their hash value sent back are send to the PE that their hash is responsible for. Any element and its duplicate is now guaranteed to be on the same PE. In the second step each PE uses a sequential algorithm for duplicate detection on the receiving elements, which are only a fraction of the amount of starting elements. By allowing a false positive rate for the duplicates, the communication volume can be reduced further as the PEs don't have to send elements with duplicated hashes at all and instead any element with a duplicated hash can simply be marked as a duplicate. As a result, the false positive rate for duplicate detection is the same as the false positive rate of the used bloom filter.

The process of filtering out the most 'unique' elements can also be repeated multiple times by changing the hash function in each filtering step. If only a single filtering step is used it has to archive a small false positive rate, however if the filtering step is repeated once the first step can allow a higher false positive rate while the latter one has a higher one but also works on less elements as many have already been removed by the earlier filtering step. While using more than two repetitions can reduce the communication volume further if the number of duplicates in a set is small, the payoff for the additional complications is low.

Replicating Bloom filters organize their data by using a well known hypcercube algorithm for gossiping, e.g.[24] First each PE calculates the Bloom filter over all local elements and stores it. By repeating a loop where in each step i the PEs send their local Bloom filter over dimension i and merge the Bloom filter they receive over the dimension with their local Bloom filter, it is possible to double the elements each Bloom filter contains in every iteration. After sending and receiving Bloom filters over all \log |\text{PE}| dimensions each PE contains the global Bloom filter over all elements.

Replicating Bloom filters are more efficient when the number of queries is much larger than the number of elements that the Bloom filter contains, the break even point compared to Distributed Bloom filters is approximately after |\text{PE}| * |\text{Elements}| / \log_{f^\text{+}} |\text{PE}| accesses, with f^\text{+} as the false positive rate of the bloom filter.

### Data synchronization

Bloom filters can be used for approximate data synchronization as in . Counting Bloom filters can be used to approximate the number of differences between two sets and this approach is described in .

### Bloomier filters

designed a generalization of Bloom filters that could associate a value with each element that had been inserted, implementing an associative array. Like Bloom filters, these structures achieve a small space overhead by accepting a small probability of false positives. In the case of "Bloomier filters", a false positive is defined as returning a result when the key is not in the map. The map will never return the wrong value for a key that is in the map.

### Compact approximators

proposed a lattice-based generalization of Bloom filters. A compact approximator associates to each key an element of a lattice (the standard Bloom filters being the case of the Boolean two-element lattice). Instead of a bit array, they have an array of lattice elements. When adding a new association between a key and an element of the lattice, they compute the maximum of the current contents of the k array locations associated to the key with the lattice element. When reading the value associated to a key, they compute the minimum of the values found in the k locations associated to the key. The resulting value approximates from above the original value.

### Parallel Partitioned Bloom Filters

This implementation used a separate array for each hash function. This method allows for parallel hash calculations for both insertions and inquiries.[25]

### Stable Bloom filters

proposed Stable Bloom filters as a variant of Bloom filters for streaming data. The idea is that since there is no way to store the entire history of a stream (which can be infinite), Stable Bloom filters continuously evict stale information to make room for more recent elements. Since stale information is evicted, the Stable Bloom filter introduces false negatives, which do not appear in traditional Bloom filters. The authors show that a tight upper bound of false positive rates is guaranteed, and the method is superior to standard Bloom filters in terms of false positive rates and time efficiency when a small space and an acceptable false positive rate are given.

### Scalable Bloom filters

proposed a variant of Bloom filters that can adapt dynamically to the number of elements stored, while assuring a minimum false positive probability. The technique is based on sequences of standard Bloom filters with increasing capacity and tighter false positive probabilities, so as to ensure that a maximum false positive probability can be set beforehand, regardless of the number of elements to be inserted.

### Spatial Bloom filters

Spatial Bloom filters (SBF) were originally proposed by as a data structure designed to store location information, especially in the context of cryptographic protocols for location privacy. However, the main characteristic of SBFs is their ability to store multiple sets in a single data structure, which makes them suitable for a number of different application scenarios. Membership of an element to a specific set can be queried, and the false positive probability depends on the set: the first sets to be entered into the filter during construction have higher false positive probabilities than sets entered at the end. This property allows a prioritization of the sets, where sets containing more "important" elements can be preserved.

### Layered Bloom filters

A layered Bloom filter consists of multiple Bloom filter layers. Layered Bloom filters allow keeping track of how many times an item was added to the Bloom filter by checking how many layers contain the item. With a layered Bloom filter a check operation will normally return the deepest layer number the item was found in.

### Attenuated Bloom filters

An attenuated Bloom filter of depth D can be viewed as an array of D normal Bloom filters. In the context of service discovery in a network, each node stores regular and attenuated Bloom filters locally. The regular or local Bloom filter indicates which services are offered by the node itself. The attenuated filter of level i indicates which services can be found on nodes that are i-hops away from the current node. The i-th value is constructed by taking a union of local Bloom filters for nodes i-hops away from the node.

Let's take a small network shown on the graph below as an example. Say we are searching for a service A whose id hashes to bits 0,1, and 3 (pattern 11010). Let n1 node to be the starting point. First, we check whether service A is offered by n1 by checking its local filter. Since the patterns don't match, we check the attenuated Bloom filter in order to determine which node should be the next hop. We see that n2 doesn't offer service A but lies on the path to nodes that do. Hence, we move to n2 and repeat the same procedure. We quickly find that n3 offers the service, and hence the destination is located.

By using attenuated Bloom filters consisting of multiple layers, services at more than one hop distance can be discovered while avoiding saturation of the Bloom filter by attenuating (shifting out) bits set by sources further away.

### Chemical structure searching

Bloom filters are often used to search large chemical structure databases (see chemical similarity). In the simplest case, the elements added to the filter (called a fingerprint in this field) are just the atomic numbers present in the molecule, or a hash based on the atomic number of each atom and the number and type of its bonds. This case is too simple to be useful. More advanced filters also encode atom counts, larger substructure features like carboxyl groups, and graph properties like the number of rings. In hash-based fingerprints, a hash function based on atom and bond properties is used to turn a subgraph into a PRNG seed, and the first output values used to set bits in the Bloom filter.

Molecular fingerprints started in the late 1940s as way to search for chemical structures searched on punched cards. However, it wasn't until around 1990 that Daylight Chemical Information Systems, Inc. introduced a hash-based method to generate the bits, rather than use a precomputed table. Unlike the dictionary approach, the hash method can assign bits for substructures which hadn't previously been seen. In the early 1990s, the term "fingerprint" was considered different from "structural keys", but the term has since grown to encompass most molecular characteristics which can be used for a similarity comparison, including structural keys, sparse count fingerprints, and 3D fingerprints. Unlike Bloom filters, the Daylight hash method allows the number of bits assigned per feature to be a function of the feature size, but most implementations of Daylight-like fingerprints use a fixed number of bits per feature, which makes them a Bloom filter. The original Daylight fingerprints could be used for both similarity and screening purposes. Many other fingerprint types, like the popular ECFP2, can be used for similarity but not for screening because they include local environmental characteristics that introduce false negatives when used as a screen. Even if these are constructed with the same mechanism, these are not Bloom filters because they cannot be used to filter.

References:
[1] ; .
[2] , pp. 21–22
[3] , pp. 109–111, 308.
[4] , p. 308.
[5] Dasgupta, Sanjoy. (2018-12-18). A neural data structure for novelty detection. Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1814448115
[6] (2016-04-01). Bloom index contrib module. Postgresql.org. https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=9ee014fc899a28a198492b074e32b60ed8915ea9
[7] ; .
[8] Yakunin, Alex. (2010-03-25). Alex Yakunin's blog: Nice Bloom filter application. Blog.alexyakunin.com. http://blog.alexyakunin.com/2010/03/nice-bloom-filter-application.html
[9] Issue 10896048: Transition safe browsing from bloom filter to prefix set. - Code Review. Chromiumcodereview.appspot.com. https://chromiumcodereview.appspot.com/10896048/
[10] Goodwin, Bob. (2017). BitFunnel: Revisiting Signatures for Search. SIGIR. doi:10.1145/3077136.3080789
[11] (2012-10-24). BIP 0037. https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki
[12] Bloom Filter River Glossary. River Financial. https://river.com/learn/terms/b/bloom-filter/
[13] Plan 9 /sys/man/8/venti. Plan9.bell-labs.com. http://plan9.bell-labs.com/magic/man2html/8/venti
[14] Spin - Formal Verification. http://spinroot.com/
[15] Exim source code. github. https://github.com/Exim/exim/blob/master/src/src/acl.c#L2627
[16] (2015-07-15). What are Bloom filters?. Medium. https://medium.com/the-story/what-are-bloom-filters-1ec2a50c68ff#.xlkqtn1vy
[17] Luo, Lailong. (13 Apr 2018). Optimizing Bloom filter: Challenges, solutions, and comparisons.
[18] Dasgupta, Sanjoy. (2018). A neural data structure for novelty detection. Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1814448115
[19] Kiss, S. Z.. (2018). Bloom ﬁlter with a false positive free zone. IEEE Proceedings of INFOCOM. http://lendulet.tmit.bme.hu/lendulet_website/wp-content/papercite-data/pdf/kiss2018bloom.pdf
[20] Kim, Kibeom. (2019-07-11). Analysis of Counting Bloom Filters Used for Count Thresholding. Electronics. doi:10.3390/electronics8070779
[21] Sanders, Peter and Schlag, Sebastian and Müller, Ingo. (2013). Communication efficient algorithms for fundamental big data problems. 2013 IEEE International Conference on Big Data.
[22] Schlag, Sebastian. (2013). Distributed duplicate removal. Karlsruhe Institute of Technology.
[23] Shatdal, Ambuj, and Jeffrey F. Naughton. (1994). Processing aggregates in parallel database systems. University of Wisconsin-Madison Department of Computer Sciences.
[24] V. Kumar, A. Grama, A. Gupta, and G. Karypis. (1994). Introduction to Parallel Computing. Design and Analysis of Algorithms. Benjamin/Cummings.
[25] Kirsch, Adam. Less Hashing, Same Performance: Building a Better Bloom Filter. Harvard School of Engineering and Applied Sciences. https://www.eecs.harvard.edu/~michaelm/postscripts/rsa2008.pdf
````

</details>

<details><summary><b>Step 8 — final</b> (7564 words)</summary>

````text
In computing, a Bloom filter is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with the counting Bloom filter variant); the more items added, the larger the probability of false positives.

Bloom proposed the technique for applications where the amount of source data would require an impractically large amount of memory if "conventional" error-free hashing techniques were applied. He gave the example of a hyphenation algorithm for a dictionary of 500,000 words, out of which 90% follow simple hyphenation rules, but the remaining 10% require expensive disk accesses to retrieve specific hyphenation patterns. With sufficient memory, an error-free hash could be used to eliminate all unnecessary disk accesses; on the other hand, with limited memory, Bloom's technique uses a smaller hash area but still eliminates most unnecessary accesses. For example, a hash area only 18% of the size needed by an ideal error-free hash still eliminates 87% of the disk accesses.

More generally, fewer than 10 bits per element are required for a 1% false positive probability, independent of the size or number of elements in the set.

## Algorithm description

An empty Bloom filter is a bit array of m bits, all set to 0. It is equipped with k different hash functions, which map set elements to one of the m possible array positions. To be optimal, the hash functions should be uniformly distributed and independent. Typically, k is a small constant which depends on the desired false error rate ε, while m is proportional to k and the number of elements to be added.

To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To test whether an element is in the set, feed it to each of the k hash functions to get k array positions. If any of the bits at these positions is 0, the element is definitely not in the set; if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, or the bits have by chance been set to 1 during the insertion of other elements, resulting in a false positive. In a simple Bloom filter, there is no way to distinguish between the two cases, but more advanced techniques can address this problem.

The requirement of designing k different independent hash functions can be prohibitive for large k. For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields. Alternatively, one can pass k different initial values (such as 0, 1, ..., k − 1) to a hash function that takes an initial value; or add (or append) these values to the key. For larger m and/or k, independence among the hash functions can be relaxed with negligible increase in false positive rate.[1] (Specifically, show the effectiveness of deriving the k indices using enhanced double hashing

and triple hashing, variants of double hashing that are effectively simple random number generators seeded with the two or three hash values.)

Removing an element from this simple Bloom filter is impossible because there is no way to tell which of the k bits it maps to should be cleared. Although setting any one of those k bits to zero suffices to remove the element, it would also remove any other elements that happen to map onto that bit. Since the simple algorithm provides no way to determine whether any other elements have been added that affect the bits for the element to be removed, clearing any of the bits would introduce the possibility of false negatives.

One-time removal of an element from a Bloom filter can be simulated by having a second Bloom filter that contains items that have been removed. However, false positives in the second filter become false negatives in the composite filter, which may be undesirable. In this approach re-adding a previously removed item is not possible, as one would have to remove it from the "removed" filter.

It is often the case that all the keys are available but are expensive to enumerate (for example, requiring many disk reads). When the false positive rate gets too high, the filter can be regenerated; this should be a relatively rare event.

## Space and time advantages

While risking false positives, Bloom filters have a substantial space advantage over other data structures for representing sets, such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings ( are an exception since they can share storage between elements with equal prefixes). However, Bloom filters do not store the data items at all, and a separate solution must be provided for the actual storage. Linked structures incur an additional linear space overhead for pointers. A Bloom filter with a 1% error and an optimal value of k, in contrast, requires only about 9.6 bits per element, regardless of the size of the elements. This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. The 1% false-positive rate can be reduced by a factor of ten by adding only about 4.8 bits per element.

However, if the number of potential values is small and many of them can be in the set, the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Hash tables gain a space and time advantage if they begin ignoring collisions and store only whether each bucket contains an entry; in this case, they have effectively become Bloom filters with = 1.

Bloom filters also have the unusual property that the time needed either to add items or to check whether an item is in the set is a fixed constant, O(), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

To understand its space efficiency, it is instructive to compare the general Bloom filter with its special case when = 1. If = 1, then in order to keep the false positive rate sufficiently low, a small fraction of bits should be set, which means the array must be very large and contain long runs of zeros. The information content of the array relative to its size is low. The generalized Bloom filter (k greater than 1) allows many more bits to be set while still maintaining a low false positive rate; if the parameters (k and m) are chosen well, about half of the bits will be set,[2] and these will be apparently random, minimizing redundancy and maximizing information content.

## Probability of false positives

Assume that a hash function selects each array position with equal probability. If m is the number of bits in the array, the probability that a certain bit is not set to 1 by a certain hash function during the insertion of an element is

1-\frac{1}{m}.

If k is the number of hash functions and each has no significant correlation between each other, then the probability that the bit is not set to 1 by any of the hash functions is

\left(1-\frac{1}{m}\right)^k.

We can use the well-known identity for e−1

\lim_{m\to\infty} \left(1 - \frac{1}{m}\right)^m = \frac{1}{e}

to conclude that, for large m,

\left(1-\frac{1}{m}\right)^k = \left(\left(1-\frac{1}{m}\right)^m\right)^{k/m} \approx e^{-k/m}.

If we have inserted n elements, the probability that a certain bit is still 0 is

\left(1-\frac{1}{m}\right)^{kn} \approx e^{-kn/m};

the probability that it is 1 is therefore

1-\left(1-\frac{1}{m}\right)^{kn} \approx 1 - e^{-kn/m}.

Now test membership of an element that is not in the set. Each of the k array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is often given as

\varepsilon = \left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k.

This is not strictly correct as it assumes independence for the probabilities of each bit being set. However, assuming it is a close approximation we have that the probability of false positives decreases as m (the number of bits in the array) increases, and increases as n (the number of inserted elements) increases.

The true probability of a false positive, without assuming independence, is

\frac{1}{m^{k(n+1)}}\sum_{i=1}^m i^k i! {m \choose i} \left\{ {kn \atop i}\right\}

where the {braces} denote Stirling numbers of the second kind.[3]

An alternative analysis arriving at the same approximation without the assumption of independence is given by Mitzenmacher and Upfal.[4] After all n items have been added to the Bloom filter, let q be the fraction of the m bits that are set to 0. (That is, the number of bits still set to 0 is qm.) Then, when testing membership of an element not in the set, for the array position given by any of the k hash functions, the probability that the bit is found set to 1 is 1-q . So the probability that all k hash functions find their bit set to 1 is (1 - q)^k . Further, the expected value of q is the probability that a given array position is left untouched by each of the k hash functions for each of the n items, which is (as above)

E[q] = \left(1 - \frac{1}{m}\right)^{kn} .

It is possible to prove, without the independence assumption, that q is very strongly concentrated around its expected value. In particular, from the Azuma–Hoeffding inequality, they prove that[5]

\Pr(\left|q - E[q]\right| \ge \frac{\lambda}{m}) \le 2\exp(-2\lambda^2/kn)

Because of this, we can say that the exact probability of false positives is

\sum_{t} \Pr(q = t) (1 - t)^k \approx (1 - E[q])^k = \left(1-\left[1-\frac{1}{m}\right]^{kn}\right)^k \approx \left( 1-e^{-kn/m} \right)^k

as before.

### Optimal number of hash functions

The number of hash functions, k, must be a positive integer. Putting this constraint aside, for a given m and n, the value of k that minimizes the false positive probability is

k = \frac{m}{n} \ln 2.

The required number of bits, m, given n (the number of inserted elements) and a desired false positive probability ε (and assuming the optimal value of k is used) can be computed by substituting the optimal value of k in the probability expression above:

\varepsilon = \left( 1-e^{-(\frac m n \ln 2) \frac n m} \right)^{\frac m n\ln 2}=\left(\frac 1 2 \right)^{\frac m n\ln 2}

which can be simplified to:

\ln (\varepsilon) = -\frac{m}{n}\ln(2)^2.

This results in:

m=-\frac{n\ln(\varepsilon)}{\ln (2)^2}

So the optimal number of bits per element is

\frac{m}{n}=-\frac{\ln(\varepsilon)}{\ln (2)^2}\approx-2.08\ln(\varepsilon)

with the corresponding number of hash functions k (ignoring integrality):

k=-\frac{\ln (\varepsilon)}{\ln(2)}.

This means that for a given false positive probability ε, the length of a Bloom filter m is proportionate to the number of elements being filtered n and the required number of hash functions only depends on the target false positive probability ε.

The formula m=-\frac{n\ln\varepsilon}{(\ln 2)^2} is approximate for three reasons. First, and of least concern, it approximates

1 - \frac{1}{m} as e^{-\frac{1}{m}} , which is a good asymptotic approximation (i.e., which holds as m →∞). Second, of more concern, it assumes that during the membership test the event that one tested bit is set to 1 is independent of the event that any other tested bit is set to 1. Third, of most concern, it assumes that k = \frac{m}{n} \ln 2 is fortuitously integral.

Goel and Gupta, however, give a rigorous upper bound that makes no approximations and requires no assumptions. They show that the false positive probability for a finite Bloom filter with m bits ( m > 1 ), n elements, and k hash functions is at most

\varepsilon \leq \left( 1-e^{-\frac{k(n+0.5)}{m-1}} \right)^k.

This bound can be interpreted as saying that the approximate formula \left( 1-e^{-\frac{kn}m} \right)^k can be applied at a penalty of at most half an extra element and at most one less bit.

## Approximating the number of items in a Bloom filter

The number of items in a Bloom filter can be approximated with the following formula,

n^* = -\frac{m}{k} \ln \left[ 1 - \frac{X}{m} \right],

where n^* is an estimate of the number of items in the filter, m is the length (size) of the filter, k is the number of hash functions, and X is the number of bits set to one.[6]

### The union and intersection of sets

Bloom filters are a way of compactly representing a set of items. It is common to try to compute the size of the intersection or union between two sets. Bloom filters can be used to approximate the size of the intersection and union of two sets. For two Bloom filters of length m, their counts, respectively can be estimated as

n(A^*) = -\frac{m}{k} \ln \left[ 1 - \frac m \right]

and

n(B^*) = -\frac{m}{k} \ln \left[ 1 - \frac m \right].

The size of their union can be estimated as

n(A^*\cup B^*) = -\frac{m}{k} \ln \left[ 1 - \frac m \right],

where n(A \cup B) is the number of bits set to one in either of the two Bloom filters. Finally, the intersection can be estimated as

n(A^*\cap B^*) = n(A^*) + n(B^*) - n(A^* \cup B^*),

using the three formulas together.[6]

## Properties

Unlike a standard hash table using open addressing for collision resolution, a Bloom filter of a fixed size can represent a set with an arbitrarily large number of elements; adding an element never fails due to the data structure "filling up". However, the false positive rate increases steadily as elements are added until all bits in the filter are set to 1, at which point all queries yield a positive result. With open addressing hashing, false positives are never produced, but performance steadily deteriorates until it approaches linear search.

Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations, respectively. The union operation on Bloom filters is lossless in the sense that the resulting Bloom filter is the same as the Bloom filter created from scratch using the union of the two sets. The intersect operation satisfies a weaker property: the false positive probability in the resulting Bloom filter is at most the false-positive probability in one of the constituent Bloom filters, but may be larger than the false positive probability in the Bloom filter created from scratch using the intersection of the two sets.

Some kinds of superimposed code can be seen as a Bloom filter implemented with physical edge-notched cards. An example is Zatocoding, invented by Calvin Mooers in 1947, in which the set of categories associated with a piece of information is represented by notches on a card, with a random pattern of four notches for each category.

## Examples

Fruit flies use a mechanism similar to Bloom filters to detect novelty of odors, with the primary differences being stateful tests such as similarity of an odor to that of previously experienced odors or time elapsed since previous experience of the same odor.[7]

The servers of Akamai Technologies, a content delivery provider, use Bloom filters to prevent "one-hit-wonders" from being stored in its disk caches. One-hit-wonders are web objects requested by users just once, something that Akamai found applied to nearly three-quarters of their caching infrastructure. Using a Bloom filter to detect the second request for a web object and caching that object only on its second request prevents one-hit wonders from entering the disk cache, significantly reducing disk workload and increasing disk cache hit rates.

Google Bigtable, Apache HBase, Apache Cassandra, ScyllaDB and PostgreSQL[8] use Bloom filters to reduce the disk lookups for non-existent rows or columns. Avoiding costly disk lookups considerably increases the performance of a database query operation.[9]

The Google Chrome web browser previously used a Bloom filter to identify malicious URLs. Any URL was first checked against a local Bloom filter, and only if the Bloom filter returned a positive result was a full check of the URL performed (and the user warned, if that too returned a positive result).[10,11]

Mozilla Firefox uses cascading Bloom filters for Certificate Revocation[12,13] and for blocking malicious addons.[14]

Microsoft Bing (search engine) uses multi-level hierarchical Bloom filters for its search index, BitFunnel. Bloom filters provided lower cost than the previous Bing index, which was based on inverted files.[15]

The Squid Web Proxy Cache uses Bloom filters for cache digests.

Bitcoin used Bloom filters to speed up wallet synchronization until privacy vulnerabilities with the implementation of Bloom filters were discovered.[16]

The Venti archival storage system uses Bloom filters to detect previously stored data.[17]

The SPIN model checker uses Bloom filters to track the reachable state space for large verification problems.[18]

The Cascading analytics framework uses Bloom filters to speed up asymmetric joins, where one of the joined data sets is significantly larger than the other (often called Bloom join in the database literature).

The Exim mail transfer agent (MTA) uses Bloom filters in its rate-limit feature.

Medium uses Bloom filters to avoid recommending articles a user has previously read.[19]

Ethereum uses Bloom filters for quickly finding logs on the Ethereum blockchain.

Grafana Tempo uses Bloom filters to improve query performance by storing bloom filters for each backend block. These are accessed on each query to determine the blocks containing data that meets the supplied search criteria[20]

## Alternatives

Classic Bloom filters use 1.44\log_2(1/\varepsilon) bits of space per inserted key, where \varepsilon is the false positive rate of the Bloom filter. However, the space that is strictly necessary for any data structure playing the same role as a Bloom filter is only \log_2(1/\varepsilon) per key.[21] Hence Bloom filters use 44% more space than an equivalent optimal data structure.

Pagh et al. provide a data structure that uses (1 + o(1)) n \log_2 (1/\epsilon) + O(n) bits while supporting constant amortized expected-time operations. Their data structure is primarily theoretical, but it is closely related to the widely-used quotient filter, which can be parameterized to use (1 + \delta) n \log \epsilon^{-1} + 3n bits of space, for an arbitrary parameter \delta > 0 , while supporting O(\delta^{-2}) -time operations.[22] Advantages of the quotient filter, when compared to the Bloom filter, include its locality of reference and the ability to support deletions.

Another alternative to classic Bloom filter is the cuckoo filter, based on space-efficient variants of cuckoo hashing. In this case, a hash table is constructed, holding neither keys nor values, but short fingerprints (small hashes) of the keys. If looking up the key finds a matching fingerprint, then key is probably in the set. Cuckoo filters support deletions and have better locality of reference than Bloom filters.[23] Additionally, in some parameter regimes, cuckoo filters can be parameterized to offer nearly optimal space guarantees.[23]

Many alternatives to Bloom filters, including quotient filters and cuckoo filters, are based on the idea of hashing keys to random (\log n + \log \epsilon^{-1}) -bit fingerprints, and then storing those fingerprints in a compact hash table. This technique, which was first introduced by Carter et al. in 1978,[21] relies on the fact that compact hash tables can be implemented to use roughly n \log n bits less space than their non-compact counterparts. Using succinct hash tables, the space usage can be reduced to as little as n \log_2 (e/\epsilon) + o(n) bits[24] while supporting constant-time operations in a wide variety of parameter regimes.

have studied some variants of Bloom filters that are either faster or use less space than classic Bloom filters. The basic idea of the fast variant is to locate the k hash values associated with each key into one or two blocks having the same size as processor's memory cache blocks (usually 64 bytes). This will presumably improve performance by reducing the number of potential memory cache misses. The proposed variants have however the drawback of using about 32% more space than classic Bloom filters.

The space efficient variant relies on using a single hash function that generates for each key a value in the range \left[0,n/\varepsilon\right] where \varepsilon is the requested false positive rate. The sequence of values is then sorted and compressed using Golomb coding (or some other compression technique) to occupy a space close to n\log_2(1/\varepsilon) bits. To query the Bloom filter for a given key, it will suffice to check if its corresponding value is stored in the Bloom filter. Decompressing the whole Bloom filter for each query would make this variant totally unusable. To overcome this problem the sequence of values is divided into small blocks of equal size that are compressed separately. At query time only half a block will need to be decompressed on average. Because of decompression overhead, this variant may be slower than classic Bloom filters but this may be compensated by the fact that a single hash function needs to be computed.

describes an approach called an xor filter, where they store fingerprints in a particular type of perfect hash table, producing a filter which is more memory efficient ( 1.23\log_2(1/\varepsilon) bits per key) and faster than Bloom or cuckoo filters. (The time saving comes from the fact that a lookup requires exactly three memory accesses, which can all execute in parallel.) However, filter creation is more complex than Bloom and cuckoo filters, and it is not possible to modify the set after creation.

## Extensions and applications

There are over 60 variants of Bloom filters, many surveys of the field, and a continuing churn of applications (see e.g., Luo, et al [25]). Some of the variants differ sufficiently from the original proposal to be breaches from or forks of the original data structure and its philosophy.[25] A treatment which unifies Bloom filters with other work on random projections, compressive sensing, and locality sensitive hashing remains to be done (though see Dasgupta, et al[26] for one attempt inspired by neuroscience).

### Cache filtering

Content delivery networks deploy web caches around the world to cache and serve web content to users with greater performance and reliability. A key application of Bloom filters is their use in efficiently determining which web objects to store in these web caches. Nearly three-quarters of the URLs accessed from a typical web cache are "one-hit-wonders" that are accessed by users only once and never again. It is clearly wasteful of disk resources to store one-hit-wonders in a web cache, since they will never be accessed again. To prevent caching one-hit-wonders, a Bloom filter is used to keep track of all URLs that are accessed by users. A web object is cached only when it has been accessed at least once before, i.e., the object is cached on its second request. The use of a Bloom filter in this fashion significantly reduces the disk write workload, since most one-hit-wonders are not written to the disk cache. Further, filtering out the one-hit-wonders also saves cache space on disk, increasing the cache hit rates.

### Avoiding false positives in a finite universe

Kiss et al described a new construction for the Bloom filter that avoids false positives in addition to the typical non-existence of false negatives.[27] The construction applies to a finite universe from which set elements are taken. It relies on existing non-adaptive combinatorial group testing scheme by Eppstein, Goodrich and Hirschberg. Unlike the typical Bloom filter, elements are hashed to a bit array through deterministic, fast and simple-to-calculate functions. The maximal set size for which false positives are completely avoided is a function of the universe size and is controlled by the amount of allocated memory.

Alternatively, an initial Bloom filter can be constructed in the standard way and then, with a finite and tractably-enumerable domain, all false positives can be exhaustively found and then a second Bloom filter constructed from that list; false positives in the second filter are similarly handled by constructing a third, and so on. As the universe is finite and the set of false positives strictly shrinks with each step, this procedure results in a finite cascade of Bloom filters that (on this closed, finite domain) will produce only true positives and true negatives. To check for membership in the filter cascade, the initial filter is queried, and, if the result is positive, the second filter is then consulted, and so on. This construction is used in CRLite, a proposed certificate revocation status distribution mechanism for the Web PKI, and Certificate Transparency is exploited to close the set of extant certificates.[28]

### Counting Bloom filters

Counting filters provide a way to implement a delete operation on a Bloom filter without recreating the filter afresh. In a counting filter, the array positions (buckets) are extended from being a single bit to being a multibit counter. In fact, regular Bloom filters can be considered as counting filters with a bucket size of one bit. Counting filters were introduced by .

The insert operation is extended to increment the value of the buckets, and the lookup operation checks that each of the required buckets is non-zero. The delete operation then consists of decrementing the value of each of the respective buckets.

Arithmetic overflow of the buckets is a problem and the buckets should be sufficiently large to make this case rare. If it does occur then the increment and decrement operations must leave the bucket set to the maximum possible value in order to retain the properties of a Bloom filter.

The size of counters is usually 3 or 4 bits. Hence counting Bloom filters use 3 to 4 times more space than static Bloom filters. In contrast, the data structures of and also allow deletions but use less space than a static Bloom filter.

Another issue with counting filters is limited scalability. Because the counting Bloom filter table cannot be expanded, the maximal number of keys to be stored simultaneously in the filter must be known in advance. Once the designed capacity of the table is exceeded, the false positive rate will grow rapidly as more keys are inserted.

introduced a data structure based on d-left hashing that is functionally equivalent but uses approximately half as much space as counting Bloom filters. The scalability issue does not occur in this data structure. Once the designed capacity is exceeded, the keys could be reinserted in a new hash table of double size.

The space efficient variant by could also be used to implement counting filters by supporting insertions and deletions.

introduced a new general method based on variable increments that significantly improves the false positive probability of counting Bloom filters and their variants, while still supporting deletions. Unlike counting Bloom filters, at each element insertion, the hashed counters are incremented by a hashed variable increment instead of a unit increment. To query an element, the exact values of the counters are considered and not just their positiveness. If a sum represented by a counter value cannot be composed of the corresponding variable increment for the queried element, a negative answer can be returned to the query.

Kim et al. (2019) shows that false positive of Counting Bloom filter decreases from k=1 to a point defined k_{opt} , and increases from k_{opt} to positive infinity, and finds k_{opt} as a function of count threshold.[29]

### Decentralized aggregation

Bloom filters can be organized in distributed data structures to perform fully decentralized computations of aggregate functions. Decentralized aggregation makes collective measurements locally available in every node of a distributed network without involving a centralized computational entity for this purpose.

### Distributed Bloom filters

Parallel Bloom filters can be implemented to take advantage of the multiple processing elements (PEs) present in parallel shared-nothing machines. One of the main obstacles for a parallel Bloom filter is the organization and communication of the unordered data which is, in general, distributed evenly over all PEs at the initiation or at batch insertions. To order the data two approaches can be used, either resulting in a Bloom filter over all data being stored on each PE, called replicating bloom filter, or the Bloom filter over all data being split into equal parts, each PE storing one part of it.[30] For both approaches a "Single Shot" Bloom filter is used which only calculates one hash, resulting in one flipped bit per element, to reduce the communication volume.

Distributed Bloom filters are initiated by first hashing all elements on their local PE and then sorting them by their hashes locally. This can be done in linear time using e.g. Bucket sort and also allows local duplicate detection. The sorting is used to group the hashes with their assigned PE as separator to create a Bloom filter for each group. After encoding these Bloom filters using e.g. Golomb coding each bloom filter is sent as packet to the PE responsible for the hash values that where inserted into it. A PE p is responsible for all hashes between the values p*(s/|\text{PE}|) and (p+1)*(s/|\text{PE}|) , where s is the total size of the Bloom filter over all data. Because each element is only hashed once and therefore only a single bit is set, to check if an element was inserted into the Bloom filter only the PE responsible for the hash value of the element needs to be operated on. Single insertion operations can also be done efficiently because the Bloom filter of only one PE has to be changed, compared to Replicating Bloom filters where every PE would have to update its Bloom filter.

By distributing the global Bloom filter over all PEs instead of storing it separately on each PE the Bloom filters size can be far larger, resulting in a larger capacity and lower false positive rate.

Distributed Bloom filters can be used to improve duplicate detection algorithms[31] by filtering out the most 'unique' elements. These can be calculated by communicating only the hashes of elements, not the elements themselves which are far larger in volume, and removing them from the set, reducing the workload for the duplicate detection algorithm used afterwards.

During the communication of the hashes the PEs search for bits that are set in more than one of the receiving packets, as this would mean that two elements had the same hash and therefore could be duplicates. If this occurs a message containing the index of the bit, which is also the hash of the element that could be a duplicate, is sent to the PEs which sent a packet with the set bit. If multiple indices are sent to the same PE by one sender it can be advantageous to encode the indices as well. All elements that didn't have their hash sent back are now guaranteed to not be a duplicate and won't be evaluated further, for the remaining elements a Repartitioning algorithm[32] can be used. First all the elements that had their hash value sent back are sent to the PE that their hash is responsible for. Any element and its duplicate is now guaranteed to be on the same PE. In the second step each PE uses a sequential algorithm for duplicate detection on the receiving elements, which are only a fraction of the amount of starting elements. By allowing a false positive rate for the duplicates, the communication volume can be reduced further as the PEs don't have to send elements with duplicated hashes at all and instead any element with a duplicated hash can simply be marked as a duplicate. As a result, the false positive rate for duplicate detection is the same as the false positive rate of the used bloom filter.

The process of filtering out the most 'unique' elements can also be repeated multiple times by changing the hash function in each filtering step. If only a single filtering step is used it has to archive a small false positive rate, however if the filtering step is repeated once the first step can allow a higher false positive rate while the latter one has a higher one but also works on less elements as many have already been removed by the earlier filtering step. While using more than two repetitions can reduce the communication volume further if the number of duplicates in a set is small, the payoff for the additional complications is low.

Replicating Bloom filters organize their data by using a well known hypercube algorithm for gossiping, e.g.[33] First each PE calculates the Bloom filter over all local elements and stores it. By repeating a loop where in each step i the PEs send their local Bloom filter over dimension i and merge the Bloom filter they receive over the dimension with their local Bloom filter, it is possible to double the elements each Bloom filter contains in every iteration. After sending and receiving Bloom filters over all \log |\text{PE}| dimensions each PE contains the global Bloom filter over all elements.

Replicating Bloom filters are more efficient when the number of queries is much larger than the number of elements that the Bloom filter contains, the break even point compared to Distributed Bloom filters is approximately after |\text{PE}| * |\text{Elements}| / \log_{f^\text{+}} |\text{PE}| accesses, with f^\text{+} as the false positive rate of the bloom filter.

### Data synchronization

Bloom filters can be used for approximate data synchronization as in . Counting Bloom filters can be used to approximate the number of differences between two sets and this approach is described in .

### Bloom filters for streaming data

Bloom filters can be adapted to the context of streaming data. For instance, proposed Stable Bloom filters, which consist of a counting Bloom filter where insertion of a new element sets the associated counters to a value c, and then only a fixed amount s of counters are decreased by 1, hence the memory mostly contains information about recent elements (intuitively, one could assume that the lifetime of an element inside a SBF of N counters is around c \tfrac s N ). Another solution is the Aging Bloom filter, that consists of two Bloom filter each occupying half the total available memory: when one filter is full, the second filter is erased and newer elements are then added to this newly empty filter.[34]

However, it has been shown[35] that no matter the filter, after n insertions, the sum of the false positive FP and false negative FN probabilities is bounded below by FP + FN \geq 1 - \frac{1 - \left(1 - \frac {1}{L} \right)^m}{1 - \left( 1 - \frac {1}{L} \right)^{n}} where L is the amount of all possible elements (the alphabet size), m the memory size (in bits), assuming n > m . This result shows that for L big enough and n going to infinity, then the lower bound converges to FP + FN = 1 , which is the characteristic relation of a random filter. Hence, after enough insertions, and if the alphabet is too big to be stored in memory (which is assumed in the context of probabilistic filters), it is impossible for a filter to perform better than randomness. This result can be leveraged by only expecting a filter to operate on a sliding window rather than the whole stream. In this case, the exponent n in the formula above is replaced by w, which gives a formula that might deviate from 1, if w is not too small.

### Bloomier filters

designed a generalization of Bloom filters that could associate a value with each element that had been inserted, implementing an associative array. Like Bloom filters, these structures achieve a small space overhead by accepting a small probability of false positives. In the case of "Bloomier filters", a false positive is defined as returning a result when the key is not in the map. The map will never return the wrong value for a key that is in the map.

### Compact approximators

proposed a lattice-based generalization of Bloom filters. A compact approximator associates to each key an element of a lattice (the standard Bloom filters being the case of the Boolean two-element lattice). Instead of a bit array, they have an array of lattice elements. When adding a new association between a key and an element of the lattice, they compute the maximum of the current contents of the k array locations associated to the key with the lattice element. When reading the value associated to a key, they compute the minimum of the values found in the k locations associated to the key. The resulting value approximates from above the original value.

### Parallel-partitioned Bloom filters

This implementation used a separate array for each hash function. This method allows for parallel hash calculations for both insertions and inquiries.[36]

### Scalable Bloom filters

proposed a variant of Bloom filters that can adapt dynamically to the number of elements stored, while assuring a minimum false positive probability. The technique is based on sequences of standard Bloom filters with increasing capacity and tighter false positive probabilities, so as to ensure that a maximum false positive probability can be set beforehand, regardless of the number of elements to be inserted.

### Spatial Bloom filters

Spatial Bloom filters (SBF) were originally proposed by as a data structure designed to store location information, especially in the context of cryptographic protocols for location privacy. However, the main characteristic of SBFs is their ability to store multiple sets in a single data structure, which makes them suitable for a number of different application scenarios. Membership of an element to a specific set can be queried, and the false positive probability depends on the set: the first sets to be entered into the filter during construction have higher false positive probabilities than sets entered at the end. This property allows a prioritization of the sets, where sets containing more "important" elements can be preserved.

### Layered Bloom filters

A layered Bloom filter consists of multiple Bloom filter layers. Layered Bloom filters allow keeping track of how many times an item was added to the Bloom filter by checking how many layers contain the item. With a layered Bloom filter a check operation will normally return the deepest layer number the item was found in.

### Attenuated Bloom filters

An attenuated Bloom filter of depth D can be viewed as an array of D normal Bloom filters. In the context of service discovery in a network, each node stores regular and attenuated Bloom filters locally. The regular or local Bloom filter indicates which services are offered by the node itself. The attenuated filter of level i indicates which services can be found on nodes that are i-hops away from the current node. The i-th value is constructed by taking a union of local Bloom filters for nodes i-hops away from the node.

For example, consider a small network, shown on the graph below. Say we are searching for a service A whose id hashes to bits 0,1, and 3 (pattern 11010). Let n1 node to be the starting point. First, we check whether service A is offered by n1 by checking its local filter. Since the patterns don't match, we check the attenuated Bloom filter in order to determine which node should be the next hop. We see that n2 doesn't offer service A but lies on the path to nodes that do. Hence, we move to n2 and repeat the same procedure. We quickly find that n3 offers the service, and hence the destination is located.

By using attenuated Bloom filters consisting of multiple layers, services at more than one hop distance can be discovered while avoiding saturation of the Bloom filter by attenuating (shifting out) bits set by sources further away.

### Chemical structure searching

Bloom filters are often used to search large chemical structure databases (see chemical similarity). In the simplest case, the elements added to the filter (called a fingerprint in this field) are just the atomic numbers present in the molecule, or a hash based on the atomic number of each atom and the number and type of its bonds. This case is too simple to be useful. More advanced filters also encode atom counts, larger substructure features like carboxyl groups, and graph properties like the number of rings. In hash-based fingerprints, a hash function based on atom and bond properties is used to turn a subgraph into a PRNG seed, and the first output values used to set bits in the Bloom filter.

Molecular fingerprints started in the late 1940s as way to search for chemical structures searched on punched cards. However, it wasn't until around 1990 that Daylight Chemical Information Systems, Inc. introduced a hash-based method to generate the bits, rather than use a precomputed table. Unlike the dictionary approach, the hash method can assign bits for substructures which hadn't previously been seen. In the early 1990s, the term "fingerprint" was considered different from "structural keys", but the term has since grown to encompass most molecular characteristics which can be used for a similarity comparison, including structural keys, sparse count fingerprints, and 3D fingerprints. Unlike Bloom filters, the Daylight hash method allows the number of bits assigned per feature to be a function of the feature size, but most implementations of Daylight-like fingerprints use a fixed number of bits per feature, which makes them a Bloom filter. The original Daylight fingerprints could be used for both similarity and screening purposes. Many other fingerprint types, like the popular ECFP2, can be used for similarity but not for screening because they include local environmental characteristics that introduce false negatives when used as a screen. Even if these are constructed with the same mechanism, these are not Bloom filters because they cannot be used to filter.

### Works cited

. Open source implementation available on github.

. A preliminary version appeared at SIGCOMM '98.

. Prototype implementation available on github.

References:
[1] ; .
[2] , pp. 21–22
[3] Gopinathan, Kiran. (2020-07-21). Computer Aided Verification. Springer, Cham. doi:10.1007/978-3-030-53291-8_16
[4] , pp. 109–111, 308.
[5] , p. 308.
[6] Swamidass, S. Joshua. (2007). Mathematical correction for fingerprint similarity measures to improve chemical retrieval. Journal of Chemical Information and Modeling. doi:10.1021/ci600526a
[7] Dasgupta, Sanjoy. (2018-12-18). A neural data structure for novelty detection. Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1814448115
[8] (2016-04-01). Bloom index contrib module. Postgresql.org. https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=9ee014fc899a28a198492b074e32b60ed8915ea9
[9] ; .
[10] Yakunin, Alex. (2010-03-25). Alex Yakunin's blog: Nice Bloom filter application. Blog.alexyakunin.com. http://blog.alexyakunin.com/2010/03/nice-bloom-filter-application.html
[11] Issue 10896048: Transition safe browsing from bloom filter to prefix set. - Code Review. Chromiumcodereview.appspot.com. https://chromiumcodereview.appspot.com/10896048/
[12] Jones, J. C.. (2020-01-09). Introducing CRLite: All of the Web PKI's revocations, compressed. Mozilla Security Blog. https://blog.mozilla.org/security/2020/01/09/crlite-part-1-all-web-pki-revocations-compressed
[13] Jones, J. C.. (2020-01-09). The End-to-End Design of CRLite. Mozilla Security Blog. https://blog.mozilla.org/security/2020/01/09/crlite-part-2-end-to-end-design
[14] Colville, Stuart. (2020-08-24). Introducing a scalable add-ons blocklist. Mozilla Add-ons Community Blog. https://blog.mozilla.org/addons/2020/08/24/introducing-a-scalable-add-ons-blocklist
[15] Goodwin, Bob. (2017). Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval. doi:10.1145/3077136.3080789
[16] Bloom Filter River Glossary. River Financial. https://river.com/learn/terms/b/bloom-filter/
[17] Plan 9 /sys/man/8/venti. Plan9.bell-labs.com. http://plan9.bell-labs.com/magic/man2html/8/venti
[18] Spin - Formal Verification. http://spinroot.com/
[19] (2015-07-15). What are Bloom filters?. Medium. https://medium.com/the-story/what-are-bloom-filters-1ec2a50c68ff#.xlkqtn1vy
[20] Grafana Tempo Documentation - Caching. Grafana. https://grafana.com/docs/tempo/latest/operations/caching/
[21] Carter, Larry. (1978). Proceedings of the tenth annual ACM symposium on Theory of computing - STOC '78. ACM Press. doi:10.1145/800133.804332
[22] Bender, Michael A.. (July 2012). Don't thrash. Proceedings of the VLDB Endowment. doi:10.14778/2350229.2350275
[23] Even, Tomer. (March 2022). Prefix filter. Proceedings of the VLDB Endowment. doi:10.14778/3523210.3523211
[24] Bender, Michael A.. (2022-06-09). Proceedings of the 54th Annual ACM SIGACT Symposium on Theory of Computing. ACM. doi:10.1145/3519935.3519969
[25] Luo, Lailong. (13 Apr 2018). Optimizing Bloom filter: Challenges, solutions, and comparisons.
[26] Dasgupta, Sanjoy. (2018). A neural data structure for novelty detection. Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1814448115
[27] Kiss, S. Z.. (2018). Bloom filter with a false positive free zone. IEEE Proceedings of INFOCOM. http://lendulet.tmit.bme.hu/lendulet_website/wp-content/papercite-data/pdf/kiss2018bloom.pdf
[28] Larisch, James. (2017). 2017 IEEE Symposium on Security and Privacy (SP). doi:10.1109/sp.2017.17
[29] Kim, Kibeom. (2019-07-11). Analysis of Counting Bloom Filters Used for Count Thresholding. Electronics. doi:10.3390/electronics8070779
[30] (2013). 2013 IEEE International Conference on Big Data. doi:10.1109/BigData.2013.6691549
[31] Schlag, Sebastian. (2013). Distributed duplicate removal. Karlsruhe Institute of Technology.
[32] (1994). Processing aggregates in parallel database systems. University of Wisconsin-Madison Department of Computer Sciences.
[33] (1994). Introduction to Parallel Computing. Design and Analysis of Algorithms. Benjamin/Cummings.
[34] Yoon, MyungKeun. (2010). Aging Bloom Filter with Two Active Buffers for Dynamic Sets. IEEE Transactions on Knowledge and Data Engineering. doi:10.1109/TKDE.2009.136
[35] Géraud-Stewart, Rémi. (2020). Computing and Combinatorics. doi:10.1007/978-3-030-58150-3_6
[36] Kirsch, Adam. Less Hashing, Same Performance: Building a Better Bloom Filter. Harvard School of Engineering and Applied Sciences. https://www.eecs.harvard.edu/~michaelm/postscripts/rsa2008.pdf
````

</details>
