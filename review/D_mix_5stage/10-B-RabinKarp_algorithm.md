# 10. Rabin–Karp algorithm

`B-RabinKarp_algorithm` · [D_mix_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Rabin–Karp_algorithm&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 376 revisions in history; 29 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | earliest_version | 945 | 0 | 0.33 | enwiki rev 3759466 (2004-05-28) |
| 2 | early_revision | 1393 | 0 | 0.52 | enwiki rev 547494729 (2013-03-28) |
| 3 | late_revision | 1535 | 0 | 0.73 | enwiki rev 918045073 (2019-09-26) |
| 4 | final | 1601 | 0 | 1.00 | enwiki rev 1373719006 (2026-09-07) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Rabin–Karp algorithm
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (945 words)</summary>

````text
Rabin-Karp algorithm is a string searching algorithm that seeks a patter, i.e. a substring, within a text by using hashing. It is not widely used for single pattern matching, but is of considerable theoretical importance and is very effective for multiple pattern matching. Historically, it predates the very popular Knuth-Morris-Pratt algorithm. For text of length n and pattern of length m, its average and best case running time is proportional to n, but the worst case scenario is proportional to n*m, which is one of the reasons why it is not widely used.

## Shifting substrings search and competing algorithms

The basic problem the algorithm addresses is finding a pattern (fixed substring) of length m within a text of length n, for example "sun" in "Hello sunshine in this vale of tears." By way of comparison of the algorithms, a naive brute force string searching algorithm involves aligning the first character of the pattern with the first character of the text and checking if the pattern matches the initial substring of equivalent length. If it does not match, the pattern is shifted right by 1 and the procedure is repeated, for a worst case running time of m*n. Knuth-Morris-Pratt-algorithm is an elegant elaboration on this naive algorithm that uses precomputed data to skip forward not by 1 character, but by as many as possible for the search to succeed.

## Use of hashing for shifting substring search

Rabin-Karp algorithm takes a very different approach. Rather than pursuing more sophisticated skipping, it seeks to speed up the testing of equality of the pattern to the substrings in the text by using hashing. Hashing a string means computing a numerical value from the value of its characters using some standard hash function (a very primitive one could involve multiplying the ASCII values of all of its characters together). Rabin-Karp exploits the fact that if 2 strings are equal, their hash values are also equal. Note that the converse of this statement is not valid, although good hash functions seek to reduce the number of such hash collisions. Rabin-Karp computes hash value of the pattern, and then goes through the text computing hash values of all of its substrings and checking whether or not the pattern's hash is equal to the substring hash, and advancing by 1 character every time. If the two numbers are indeed discovered to be equal, then the algorithm has to verify that the two string really are equal, rather than this being a fluke of the hashing scheme. It does so using regular string comparison. It is this verification that in the worst case can drag down algorithm performance down to the level of the naive string search. This general approach is sometimes referred to as the use of a virtual hash table.

## Hash function used

The key to Rabin-Karp performance is the efficient computation of hash values of the successive substrings of the text. Rabin-Karp achieves this by treating every substring as a number in some base, the base being usually a big prime. For example, if the substring is "hi" and the base is 101, the hash value would be 104 * 101^1 + 105 * 101^0 = 10609 (ASCII of 'h' is 104 and of 'i' is 105). Technically, this algorithm is only similar to the true number in a non-decimal system representation, since for example we could have the "base" less than one of the "digits". See hash function for much more detailed discussion. The essential benefit achieved by such representation is that is is possible to compute the hash value of the next substring from the previous one by doing only a finite number of operations, independent of the substrings' length. For example, if we have text "abracadabra" and we are searching for a pattern of length 3, we can compute the hash of "bra" from the hash for "abr" (the previous substring) by subtracting the number added for the first 'a' of "abr", i.e. 97 * 101^2 (97 is ASCII for 'a' and 101 is the base we are using) and adding that for the last a of "bra", i.e. 97 * 101^0 = 97. If the substrings in question are long, this algorithm achieves great savings compared with many other hashing schemes. Theoretically, there exist other algorithms that could provide convenient recompution, e.g. multiplying together ASCII values of all characters so that shifting substring would only entail dividing by the first character and multiplying by the last. The limitation, however, is the limitations of the size of integer data type and the necessity of using modular arithmetic to scale down the hash results, for which see hash function article. Hence the number in arbitrary base hash function is the preferred one in Rabin-Karp.

## Rabin-Karp and multiple pattern search

Rabin-Karp is inferior to Knuth-Morris-Pratt algorithm, Boyer-Moore algorithm and other faster single pattern string search algorithms because of its slow worst case behavior. However, Rabin-Karp is an algorithm of choice for multiple pattern search. That is, if we want to find any of a large number, say k, fixed length patterns in a text, a variant Rabin-Karp that uses a hash table to check whether the hash of a given string belongs to a set of hash values of patterns we are looking for. Other algorithms can search for a single pattern in time order n, hence they will search for k patterns in time order n*k. The variant Rabin-Karp will still work in time order n in the best and average case because a hash table allows to check whether or not substring hash equals any of the pattern hashes in order of 1 time.
````

</details>

<details><summary><b>Step 2 — early_revision</b> (1393 words)</summary>

````text
In computer science, the Rabin–Karp algorithm is a string searching algorithm created by Michael O. Rabin and Richard M. Karp in 1987 that uses hashing to find any one of a set of pattern strings in a text. For text of length n and p patterns of combined length m, its average and best case running time is O(n+m) in space O(p), but its worst-case time is O(nm). In contrast, the Aho–Corasick string matching algorithm has asymptotic worst-time complexity O(n+m) in space O(m).

A practical application of Rabin–Karp is detecting plagiarism. Given source material, Rabin–Karp can rapidly search through a paper for instances of sentences from the source material, ignoring details such as case and punctuation. Because of the abundance of the sought strings, single-string searching algorithms are impractical.

## Shifting substrings search and competing algorithms

A brute-force substring search algorithm checks all possible positions:

1 function NaiveSearch(string s[1..n], string sub[1..m])

2 for i from 1 to n-m+1

3 for j from 1 to m

4 if s[i+j-1] ≠ sub[j]

5 jump to next iteration of outer loop

6 return i

7 return not found

This algorithm works well in many practical cases, but can exhibit relatively long running times on certain examples, such as searching for a string of 10,000 "a"s followed by a "b" in a string of 10 million "a"s, in which case it exhibits its worst-case O(mn) time.

The Knuth–Morris–Pratt algorithm reduces this to O(n) time using precomputation to examine each text character only once; the Boyer–Moore algorithm skips forward not by 1 character, but by as many as possible for the search to succeed, effectively decreasing the number of times we iterate through the outer loop, so that the number of characters examined can be as small as n/m in the best case. The Rabin–Karp algorithm focuses instead on speeding up lines 3-6.

## Use of hashing for shifting substring search

Rather than pursuing more sophisticated skipping, the Rabin–Karp algorithm seeks to speed up the testing of equality of the pattern to the substrings in the text by using a hash function. A hash function is a function which converts every string into a numeric value, called its hash value; for example, we might have hash("hello")=5. Rabin–Karp exploits the fact that if two strings are equal, their hash values are also equal. Thus, it would seem all we have to do is compute the hash value of the substring we're searching for, and then look for a substring with the same hash value.

However, there are two problems with this. First, because there are so many different strings, to keep the hash values small we have to assign some strings the same number. This means that if the hash values match, the strings might not match; we have to verify that they do, which can take a long time for long substrings. Luckily, a good hash function promises us that on most reasonable inputs, this won't happen too often, which keeps the average search time good.

The algorithm is as shown:

1 function RabinKarp(string s[1..n], string sub[1..m])

2 hsub := hash(sub[1..m]); hs := hash(s[1..m])

3 for i from 1 to n-m+1

4 if hs = hsub

5 if s[i..i+m-1] = sub

6 return i

7 hs := hash(s[i+1..i+m])

8 return not found

Lines 2, 5, and 7 each require O(m) time. However, line 2 is only executed once, and line 5 is only executed if the hash values match, which is unlikely to happen more than a few times. Line 4 is executed n times, but only requires constant time. So the only problem is line 7.

If we naively recompute the hash value for the substring s[i+1..i+m], this would require O(m) time, and since this is done on each loop, the algorithm would require O(mn) time, the same as the most naive algorithms. The trick to solving this is to note that the variable hs already contains the hash value of s[i..i+m-1]. If we can use this to compute the next hash value in constant time, then our problem will be solved.

We do this using what is called a rolling hash. A rolling hash is a hash function specially designed to enable this operation. One simple example is adding up the values of each character in the substring. Then, we can use this formula to compute the next hash value in constant time:

s[i+1..i+m] = s[i..i+m-1] - s[i] + s[i+m]

This simple function works, but will result in statement 5 being executed more often than other more sophisticated rolling hash functions such as those discussed in the next section.

Notice that if we're very unlucky, or have a very bad hash function such as a constant function, line 5 might very well be executed n times, on every iteration of the loop. Because it requires O(m) time, the whole algorithm then takes a worst-case O(mn) time.

## Hash function used

The key to Rabin–Karp performance is the efficient computation of hash values of the successive substrings of the text. One popular and effective rolling hash function treats every substring as a number in some base, the base being usually a large prime. For example, if the substring is "hi" and the base is 101, the hash value would be 104 × 1011 + 105 × 1010 = 10609 (ASCII of 'h' is 104 and of 'i' is 105).

Technically, this algorithm is only similar to the true number in a non-decimal system representation, since for example we could have the "base" less than one of the "digits". See hash function for a much more detailed discussion. The essential benefit achieved by such representation is that it is possible to compute the hash value of the next substring from the previous one by doing only a constant number of operations, independent of the substrings' lengths.

For example, if we have text "abracadabra" and we are searching for a pattern of length 3, we can compute the hash of "bra" from the hash for "abr" (the previous substring) by subtracting the number added for the first 'a' of "abr", i.e. 97 × 1012 (97 is ASCII for 'a' and 101 is the base we are using), multiplying by the base and adding for the last a of "bra", i.e. 97 × 1010 = 97. If the substrings in question are long, this algorithm achieves great savings compared with many other hashing schemes.

Theoretically, there exist other algorithms that could provide convenient recomputation, e.g. multiplying together ASCII values of all characters so that shifting substring would only entail dividing by the first character and multiplying by the last. The limitation, however, is the limited size of the integer data type and the necessity of using modular arithmetic to scale down the hash results, for which see hash function article; meanwhile, those naive hash functions that would not produce large numbers quickly, like just adding ASCII values, are likely to cause many hash collisions and hence slow down the algorithm. Hence the described hash function is typically the preferred one in Rabin–Karp.

## Rabin–Karp and multiple pattern search

Rabin–Karp is inferior for single pattern searching to Knuth–Morris–Pratt algorithm, Boyer–Moore string search algorithm and other faster single pattern string searching algorithms because of its slow worst case behavior. However, Rabin–Karp is an algorithm of choice for multiple pattern search.

That is, if we want to find any of a large number, say k, fixed length patterns in a text, we can create a simple variant of Rabin–Karp that uses a Bloom filter or a set data structure to check whether the hash of a given string belongs to a set of hash values of patterns we are looking for:

function RabinKarpSet(string s[1..n], set of string subs, m):

set hsubs := emptySet

for each sub in subs

insert hash(sub[1..m]) into hsubs

hs := hash(s[1..m])

for i from 1 to n-m+1

if hs ∈ hsubs and s[i..i+m-1] ∈ subs

return i

hs := hash(s[i+1..i+m])

return not found

We assume all the substrings have a fixed length m.

A naïve way to search for k patterns is to repeat a

single-pattern search taking O(n) time, totalling in O(n k) time. In contrast, the variant Rabin–Karp above can find all k patterns in O(n+k) time in expectation, because a hash table checks whether a substring hash equals any of the pattern hashes in O(1) time.
````

</details>

<details><summary><b>Step 3 — late_revision</b> (1535 words)</summary>

````text
In computer science, the Rabin–Karp algorithm or Karp–Rabin algorithm is a string-searching algorithm created by that uses hashing to find any one of a set of pattern strings in a text. For text of length n and p patterns of combined length m, its average and best case running time is O(n+m) in space O(p), but its worst-case time is O(nm). In contrast, the Aho–Corasick string-matching algorithm has asymptotic worst-time complexity O(n+m) in space O(m). See also the Knuth-Morris-Pratt algorithm.

A practical application of the algorithm is detecting plagiarism. Given source material, the algorithm can rapidly search through a paper for instances of sentences from the source material, ignoring details such as case and punctuation. Because of the abundance of the sought strings, single-string searching algorithms are impractical.

## Shifting substrings search and competing algorithms

A brute-force substring search algorithm checks all possible positions:

This algorithm works well in many practical cases, but can exhibit relatively long running times in certain examples, such as searching for a pattern string of 10,000 "a"s followed by a single "b" in a search string of 10 million "a"s, in which case it exhibits its worst-case O(mn) time.

The Knuth–Morris–Pratt algorithm reduces this to O(n) time using precomputation to examine each text character only once; the Boyer–Moore algorithm skips forward not by 1 character, but by as many as possible for the search to succeed, effectively decreasing the number of times we iterate through the outer loop, so that the number of characters examined can be as small as n/m in the best case. The Rabin–Karp algorithm focuses instead on speeding up lines 3-5.

## Use of hashing for shifting substring search

Rather than pursuing more sophisticated skipping, the Rabin–Karp algorithm seeks to speed up the testing of equality of the pattern to the substrings in the text by using a hash function. A hash function is a function which converts every string into a numeric value, called its hash value; for example, we might have hash("hello")=5. The algorithm exploits the fact that if two strings are equal, their hash values are also equal. Thus, string matching is reduced (almost) to computing the hash value of the search pattern and then looking for substrings of the input string with that hash value.

However, there are two problems with this approach. First, because there are so many different strings and so few hash values, some differing strings will have the same hash value. If the hash values match, the pattern and the substring may not match; consequently, the potential match of search pattern and the substring must be confirmed by comparing them; that comparison can take a long time for long substrings. Luckily, a good hash function on reasonable strings usually does not have many collisions, so the expected search time will be acceptable.

The algorithm is as shown:

Lines 2, 4, and 6 each require O(m) time. However, line 2 is only executed once, and line 6 is only executed if the hash values match, which is unlikely to happen more than a few times. Line 5 is executed O(n) times, but each comparison only requires constant time, so its impact is O(n). The issue is line 4.

Naively computing the hash value for the substring s[i+1..i+m] requires O(m) time because each character is examined. Since the hash computation is done on each loop, the algorithm with a naïve hash computation requires O(mn) time, the same complexity as a straightforward string matching algorithms. For speed, the hash must be computed in constant time. The trick is the variable hs already contains the previous hash value of s[i..i+m-1]. If that value can be used to compute the next hash value in constant time, then computing successive hash values will be fast.

The trick can be exploited using a rolling hash. A rolling hash is a hash function specially designed to enable this operation. A trivial (but not very good) rolling hash function just adds the values of each character in the substring. This rolling hash formula can compute the next hash value from the previous value in constant time:

This simple function works, but will result in statement 5 being executed more often than other more sophisticated rolling hash functions such as those discussed in the next section.

Good performance requires good hashing function for the encountered data. If the hashing is poor (such as producing the same hash value for every input), then line 5 would be executed O(n) times (i.e. on every iteration of the loop). Because character-by-character comparison of strings with length m takes O(m) time, the whole algorithm then takes a worst-case O(mn) time.

## Hash function used

The key to the Rabin–Karp algorithm's performance is the efficient computation of hash values of the successive substrings of the text. The Rabin fingerprint is a popular and effective rolling hash function. The hash function described here is not a Rabin fingerprint, but it works equally well. It treats every substring as a number in some base, the base being usually the size of the character set.

For example, if the substring is "hi", the base is 256, and prime modulus is 101, then the hash value would be

(ASCII of 'h' is 104 and of 'i' is 105)

'%' is 'mod' or modulo, or remainder after integer division, operator

Technically, this algorithm is only similar to the true number in a non-decimal system representation, since for example we could have the "base" less than one of the "digits". See hash function for a much more detailed discussion. The essential benefit achieved by using a rolling hash such as the Rabin fingerprint is that it is possible to compute the hash value of the next substring from the previous one by doing only a constant number of operations, independent of the substrings' lengths.

For example, if we have text "abracadabra" and we are searching for a pattern of length 3, the hash of the first substring, "abr", using 256 as the base, and 101 as the prime modulus is:

// ASCII a = 97, b = 98, r = 114.

hash("abr") = [ ( [ ( [ (97 × 256) % 101 + 98 ] % 101 ) × 256 ] % 101 ) + 114 ] % 101 = 4

We can then compute the hash of the next substring, "bra", from the hash of "abr" by subtracting the number added for the first 'a' of "abr", i.e. 97 × 2562, multiplying by the base and adding for the last a of "bra", i.e. 97 × 2560. Like so:

// old hash -ve avoider old 'a' left base offset base shift new 'a''' prime modulus

hash("bra") = [ ( 4 + 101 - 97 * [(256%101)*256] % 101 ) * 256 + 97 ] % 101 = 30

the last '* 256' is the shift of the subtracted hash to the left

although ((256%101)*256)%101 is the same as 2562 % 101, to avoid overflowing integer maximums when the pattern string is longer (e.g. 'Rabin-Karp' is 10 characters, 2569 is the offset without modulation ), the pattern length base offset is pre-calculated in a loop, modulating the result each iteration

If we are matching the search string "bra", using similar calculation of hash("abr"),

hash'("bra") = [ ( [ ( [ ( 98 × 256) %101 + 114] % 101 ) × 256 ] % 101) + 97 ] % 101 = 30

If the substrings in question are long, this algorithm achieves great savings compared with many other hashing schemes.

Theoretically, there exist other algorithms that could provide convenient recomputation, e.g. multiplying together ASCII values of all characters so that shifting substring would only entail dividing the previous hash by the first character value, then multiplying by the new last character's value. The limitation, however, is the limited size of the integer data type and the necessity of using modular arithmetic to scale down the hash results, (see hash function article). Meanwhile, naive hash functions do not produce large numbers quickly, but, just like adding ASCII values, are likely to cause many hash collisions and hence slow down the algorithm. Hence the described hash function is typically the preferred one in the Rabin–Karp algorithm.

## Multiple pattern search

The Rabin–Karp algorithm is inferior for single pattern searching to Knuth–Morris–Pratt algorithm, Boyer–Moore string search algorithm and other faster single pattern string searching algorithms because of its slow worst case behavior. However, it is an algorithm of choice for multiple pattern search.

To find any of a large number, say k, fixed length patterns in a text, a simple variant of the Rabin–Karp algorithm uses a Bloom filter or a set data structure to check whether the hash of a given string belongs to a set of hash values of patterns we are looking for:

We assume all the substrings have a fixed length m.

A naïve way to search for k patterns is to repeat a single-pattern search taking O(n+m) time, totaling in O((n+m)k) time. In contrast, the above algorithm above can find all k patterns in O(n+km) expected time, assuming that a hash table check works in O(1) expected time. A deterministic O(n+km'') solution is the Aho–Corasick algorithm.
````

</details>

<details><summary><b>Step 4 — final</b> (1601 words)</summary>

````text
In computer science, the Rabin–Karp algorithm or Karp–Rabin algorithm is a string-searching algorithm created by that uses hashing to find an exact match of a pattern string in a text. It uses a rolling hash to quickly filter out positions of the text that cannot match the pattern, and then checks for a match at the remaining positions. Generalizations of the same idea can be used to find more than one match of a single pattern, or to find matches for more than one pattern.

To find a single match of a single pattern, the expected time of the algorithm is linear in the combined length of the pattern and text,

although its worst-case time complexity is the product of the two lengths. To find multiple matches, the expected time is linear in the input lengths, plus the combined length of all the matches, which could be greater than linear. In contrast, the Aho–Corasick algorithm can find all matches of multiple patterns in worst-case time and space linear in the input length and the number of matches (instead of the total length of the matches).

A practical application of the algorithm is detecting plagiarism. Given source material, the algorithm can rapidly search through a paper for instances of sentences from the source material, ignoring details such as case and punctuation. Because of the abundance of the sought strings, single-string searching algorithms are impractical.

## Overview

A naive string matching algorithm compares the given pattern against all positions in the given text. Each comparison takes time proportional to the length of the pattern,

and the number of positions is proportional to the length of the text. Therefore, the worst-case time for such a method is proportional to the product of the two lengths.

In many practical cases, this time can be significantly reduced by cutting short the comparison at each position as soon as a mismatch is found, but this idea cannot guarantee any speedup.

Several string-matching algorithms, including the Knuth–Morris–Pratt algorithm and the Boyer–Moore string-search algorithm, reduce the worst-case time for string matching by extracting more information from each mismatch, allowing them to skip over positions of the text that are guaranteed not to match the pattern. The Rabin–Karp algorithm instead achieves its speedup by using a hash function to quickly perform an approximate check for each position, and then only performing an exact comparison at the positions that pass this approximate check.

A hash function is a function which converts every string into a numeric value, called its hash value; for example, we might have hash("hello")=5. If two strings are equal, their hash values are also equal. For a well-designed hash function, the inverse is true, in an approximate sense: strings that are unequal are very unlikely to have equal hash values. The Rabin–Karp algorithm proceeds by computing, at each position of the text, the hash value of a string starting at that position with the same length as the pattern. If this hash value equals the hash value of the pattern, it performs a full comparison at that position.

In order for this to work well, the hash function should be selected randomly from a family of hash functions that are unlikely to produce many false positives, that is, positions of the text which have the same hash value as the pattern but do not actually match the pattern. These positions contribute to the running time of the algorithm unnecessarily, without producing a match. Additionally, the hash function used should be a rolling hash, a hash function whose value can be quickly updated from each position of the text to the next. Recomputing the hash function from scratch at each position would be too slow.

## The algorithm

The algorithm is as shown:

Lines 2, 4, and 6 each require O(m) time. However, line 2 is only executed once, and line 6 is only executed if the hash values match, which is unlikely to happen more than a few times. Line 5 is executed O(n) times, but each comparison only requires constant time, so its impact is O(n). The issue is line 4.

Naively computing the hash value for the substring s[i+1..i+m] requires O(m) time because each character is examined. Since the hash computation is done on each loop, the algorithm with a naive hash computation requires O(mn) time, the same complexity as a straightforward string matching algorithm. For speed, the hash must be computed in constant time. The trick is the variable hs already contains the previous hash value of s[i..i+m-1]. If that value can be used to compute the next hash value in constant time, then computing successive hash values will be fast.

The trick can be exploited using a rolling hash. A rolling hash is a hash function specially designed to enable this operation. A trivial (but not very good) rolling hash function just adds the values of each character in the substring. This rolling hash formula can compute the next hash value from the previous value in constant time:

This simple function works, but will result in statement 5 being executed more often than other more sophisticated rolling hash functions such as those discussed in the next section.

Good performance requires a good hashing function for the encountered data. If the hashing is poor (such as producing the same hash value for every input), then line 6 would be executed O(n) times (i.e. on every iteration of the loop). Because character-by-character comparison of strings with length m takes O(m) time, the whole algorithm then takes a worst-case O(mn) time.

## Hash function used

The key to the Rabin–Karp algorithm's performance is the efficient computation of hash values of the successive substrings of the text. The Rabin fingerprint is a popular and effective rolling hash function. The hash function described here is not a Rabin fingerprint, but it works equally well. It treats every substring as a number in some base, the base being usually the size of the character set.

For example, if the substring is "hi", the base is 256, and prime modulus is 101, then the hash value would be

(ASCII of 'h' is 104 and of 'i' is 105)

Technically, this algorithm is only similar to the true number in a non-decimal system representation, since for example we could have the "base" less than one of the "digits". See hash function for a much more detailed discussion. The essential benefit achieved by using a rolling hash such as the Rabin fingerprint is that it is possible to compute the hash value of the next substring from the previous one by doing only a constant number of operations, independent of the substrings' lengths.

For example, if we have text "abracadabra" and we are searching for a pattern of length 3, the hash of the first substring, "abr", using 256 as the base, and 101 as the prime modulus is:

// ASCII a = 97, b = 98, r = 114.

hash("abr") = [ ( [ ( [ (97 × 256) % 101 + 98 ] % 101 ) × 256 ] % 101 ) + 114 ] % 101 = 4

We can then compute the hash of the next substring, "bra", from the hash of "abr" by subtracting the number added for the first 'a' of "abr", i.e. 97 × 2562, multiplying by the base and adding for the last a of "bra", i.e. 97 × 2560. Like so:

{{pre|style=font-size:95%|1=

// old hash (-ve avoider) old 'a' left base offset base shift new 'a''' prime modulus

hash("bra") = [ ( 4 + 101 - 97 * [(256%101)*256] % 101 ) * 256 + 97 ] % 101 = 30

If we are matching the search string "bra", using similar calculation of hash("abr"),

hash'("bra") = [ ( [ ( [ ( 98 × 256) %101 + 114] % 101 ) × 256 ] % 101) + 97 ] % 101 = 30

If the substrings in question are long, this algorithm achieves great savings compared with many other hashing schemes.

Theoretically, there exist other algorithms that could provide convenient recomputation, e.g. multiplying together ASCII values of all characters so that shifting substring would only entail dividing the previous hash by the first character value, then multiplying by the new last character's value. The limitation, however, is the limited size of the integer data type and the necessity of using modular arithmetic to scale down the hash results. Meanwhile, naive hash functions do not produce large numbers quickly, but, just like adding ASCII values, are likely to cause many hash collisions and hence slow down the algorithm. Hence the described hash function is typically the preferred one in the Rabin–Karp algorithm.

## Multiple pattern search

The Rabin–Karp algorithm is inferior for single pattern searching to Knuth–Morris–Pratt algorithm, Boyer–Moore string-search algorithm and other faster single pattern string searching algorithms because of its slow worst case behavior. However, it is a useful algorithm for multiple pattern search.

To find any of a large number, say k, fixed length patterns in a text, a simple variant of the Rabin–Karp algorithm uses a Bloom filter or a set data structure to check whether the hash of a given string belongs to a set of hash values of patterns we are looking for:

We assume all the substrings have a fixed length m.

A naïve way to search for k patterns is to repeat a single-pattern search taking O(n+m) time, totaling in O((n+m)k) time. In contrast, the above algorithm can find all k patterns in O(n+km'') expected time, assuming that a hash table check works in O(1) expected time.
````

</details>
