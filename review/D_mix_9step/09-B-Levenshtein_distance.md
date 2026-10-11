# 9. Levenshtein distance

`B-Levenshtein_distance` · [D_mix_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Levenshtein_distance&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 1157 revisions in history; 37 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | revision_1 | 346 | 0 | 0.06 | enwiki rev 1987917 (2003-12-18) |
| 2 | revision_2 | 1181 | 0 | 0.07 | enwiki rev 20359155 (2005-08-05) |
| 3 | revision_3 | 1221 | 6 | 0.08 | enwiki rev 265482140 (2009-01-21) |
| 4 | revision_4 | 1721 | 9 | 0.13 | enwiki rev 600148435 (2014-03-18) |
| 5 | revision_5 | 1173 | 4 | 0.14 | enwiki rev 687838920 (2015-10-28) |
| 6 | revision_6 | 1553 | 13 | 0.15 | enwiki rev 1055332013 (2021-11-15) |
| 7 | revision_7 | 1765 | 14 | 0.17 | enwiki rev 1334176829 (2026-01-22) |
| 8 | final | 1977 | 32 | 1.00 | enwiki rev 1375547008 (2026-09-18) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Levenshtein distance
````

</details>

<details><summary><b>Step 1 — revision_1</b> (346 words)</summary>

````text
In information theory, the Levenshtein distance or edit distance between two strings is given by the minimum number of operations needed to transform one string into the other, where an operation is an insertion, deletion, or substitution.

A commonly-used algorithm for computing the Levenshtein distance involves the use of an (n + 1) × (m + 1) matrix, where n and m are the lengths of the two strings. Here is pseudocode for it:

Note that the algorithm can easily be adapted to use considerably less space, O(m) instead of O(mn), since it only requires that the previous row and current row be stored at any one time. This particular algorithm parallelizes poorly.

The invariant is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. This invariant holds since:

It is initially true on row and column 0 because s[1..i] can be transformed into the empty string t[1..0] by simply dropping all i characters. Similarly, we can transform s[1..0] to t[1..j] by simply adding all j characters.

The minimum is taken over three distances, each of which is feasible:

If we can transform s[1..i] to t[1..j-1] in k operations, then we can simply add t[j] afterwards to get t[1..j] in k+1 operations.

If we can transform s[1..i-1] to t[1..j] in k operations, then we can do the same operations on s[1..i] and then remove s[i] at the end in k+1 operations.

If we can transform s[1..i-1] to t[1..j-1] in k operations, we can do the same to s[1..i] and then do a substitution of t[j] for s[i] at the end if necessary, requiring k+cost operations.

The operations required to transform s[1..n] into t[1..m] is of course the number required to transform all of s into all of t, and so d[n,m] holds our result.

This proof fails to validate that the number placed in d[i,j] is in fact minimal; this is more difficult to show.

When both strings are the same length and only substitutions are expected to occur, a simpler metric like the Hamming distance is more efficient.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (1181 words)</summary>

````text
In information theory, the Levenshtein distance or edit distance between two strings is given by the minimum number of operations needed to transform one string into the other, where an operation is an insertion, deletion, or substitution. It is named after the Russian scientist Vladimir Levenshtein, who considered this distance in 1965. It is useful in applications that need to determine how similar two strings are, such as spell checkers.

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since these three edits change one into the other, and there is no way to do it with less than three edits:

kitten

sitten (substitution of 's' for 'k')

sittin (substitution of 'e' for 'i')

sitting (insert 'g' at the end)

It can be considered a generalization of the Hamming distance, which is used for strings of the same length and only considers substitution edits. There are also further generalizations of the Levenshtein distance that consider, for example, exchanging two characters as an operation.

## The algorithm

A commonly-used bottom-up dynamic programming algorithm for computing the Levenshtein distance involves the use of an (n + 1) × (m + 1) matrix, where n and m are the lengths of the two strings. Here is pseudocode for a function LevenshteinDistance that takes two strings, str1 of length lenStr1, and str2 of length lenStr2, and computes the Levenshtein distance between them:

int LevenshteinDistance(char str1[1..lenStr1], char str2[1..lenStr2])

// d is a table with lenStr1+1 rows and lenStr2+1 columns

declare int d[0..lenStr1, 0..lenStr2]

// i and j are used to iterate over str1 and str2

declare int i, j, cost

for i from 0 to lenStr1

d[i, 0] := i

for j from 0 to lenStr2

d[0, j] := j

for i from 1 to lenStr1

for j from 1 to lenStr2

if str1[i] = str2[j] then cost := 0

else cost := 1

d[i, j] := minimum(

d[i-1, j ] + 1, // deletion

d[i , j-1] + 1, // insertion

d[i-1, j-1] + cost // substitution

return d[lenStr1, lenStr2]

The invariant maintained throughout the algorithm is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. At the end, the bottom-right element of the array contains the answer.

### Possible improvements

Possible improvements to this algorithm include:

We can adapt the algorithm to use less space, O(m) instead of O(mn), since it only requires that the previous row and current row be stored at any one time.

We can store the number of insertions, deletions, and substitutions separately, or even the positions at which they occur, which is always j.

We can give different penalty costs to insertion, deletion and substitution.

The initialization of d[i,0] can be moved inside the main outer loop.

This algorithm parallelizes poorly, due to a large number of data dependencies. However, all the costs can be computed in parallel, and the algorithm can be adapted to perform the minimum function in phases to eliminate dependencies.

### Proof of correctness

As mentioned earlier, the invariant is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. This invariant holds since:

It is initially true on row and column 0 because s[1..i] can be transformed into the empty string t[1..0] by simply dropping all i characters. Similarly, we can transform s[1..0] to t[1..j] by simply adding all j characters.

The minimum is taken over three distances, each of which is feasible:

If we can transform s[1..i] to t[1..j-1] in k operations, then we can simply add t[j] afterwards to get t[1..j] in k+1 operations.

If we can transform s[1..i-1] to t[1..j] in k operations, then we can do the same operations on s[1..i] and then remove the original s[i] at the end in k+1 operations.

If we can transform s[1..i-1] to t[1..j-1] in k operations, we can do the same to s[1..i] and then do a substitution of t[j] for the original s[i] at the end if necessary, requiring k+cost operations.

The operations required to transform s[1..n] into t[1..m] is of course the number required to transform all of s into all of t, and so d[n,m] holds our result.

This proof fails to validate that the number placed in d[i,j] is in fact minimal; this is more difficult to show, and involves an argument by contradiction in which we assume d[i,j] is smaller than the minimum of the three, and use this to show one of the three is not minimal.

## Upper and lower bounds

The Levenshtein distance has several simple upper and lower bounds that are useful in applications which compute many of them and compare them. These include:

It is always at least the difference of the sizes of the two strings.

It is at most the length of the longer string.

It is zero if and only if the strings are identical.

If the strings are the same size, the Hamming distance is an upper bound on the Levenshtein distance.

If the strings are called s and t, the number of characters (not counting duplicates) found in s but not in t is a lower bound.

## Sample implementations

### Emacs Lisp

Implementation available from the EmacsWiki.

(defun levenshtein-distance (str1 str2)

"Return the edit distance between strings STR1 and STR2."

(if (not (stringp str1))

(error "Argument was not a string: %s" str1))

(if (not (stringp str2))

(error "Argument was not a string: %s" str2))

(let* ((make-table (function (lambda (columns rows init)

(make-vector rows (make-vector columns init)))))

(tref (function (lambda (table x y)

(aref (aref table y) x))))

(tset (function (lambda (table x y object)

(let ((row (copy-sequence (aref table y))))

(aset row x object)

(aset table y row) object))))

(length-str1 (length str1))

(length-str2 (length str2))

(d (funcall make-table (1+ length-str1) (1+ length-str2) 0)))

(let ((i 0) (j 0))

(while (<= i length-str1)

(funcall tset d i 0 i)

(setq i (1+ i)))

(while (<= j length-str2)

(funcall tset d 0 j j)

(setq j (1+ j))))

(let ((i 1))

(while (<= i length-str1)

(let ((j 1))

(while (<= j length-str2)

(let* ((cost (if (equal (aref str1 (1- i)) (aref str2 (1- j)))

(deletion (1+ (funcall tref d (1- i) j)))

(insertion (1+ (funcall tref d i (1- j))))

(substitution (+ (funcall tref d (1- i) (1- j)) cost)))

(funcall tset d i j (min insertion deletion substitution)))

(setq j (1+ j))))

(setq i (1+ i))))

(funcall tref d length-str1 length-str2)))

### Haskell

Because Haskell automatically memoizes results of previous calls, it is particularly suited to a simple recursive implementation:

editDistance :: String->String->Int

editDistance [] [] = 0

editDistance s [] = length s

editDistance [] t = length t

editDistance (s:ss) (t:ts) = minimum [ (if s == t then 0 else 1) + editDistance ss ts,

1 + editDistance ss (t:ts),

1 + editDistance (s:ss) ts ]

### Java

Implemented as an entirely static class.

### Python

Written by Magnus Lie Hetland.

### Common Lisp

A fast Common Lisp version of the Python code above.

### Scheme

Uses srfi-25 and srfi-42

A functional implementation is by Rares Vernica

### Visual FoxPro
````

</details>

<details><summary><b>Step 3 — revision_3</b> (1221 words)</summary>

````text
In information theory and computer science, the Levenshtein distance is a metric for measuring the amount of difference between two sequences (i.e., the so called edit distance). The Levenshtein distance between two strings is given by the minimum number of operations needed to transform one string into the other, where an operation is an insertion, deletion, or substitution of a single character. A generalization of the Levenshtein distance (Damerau–Levenshtein distance) allows the transposition of two characters as an operation.

The metric is named after Vladimir Levenshtein, who considered this distance in 1965.[1]

It is often used in applications that need to determine how similar, or different, two strings are, such as spell checkers.

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following three edits change one into the other, and there is no way to do it with fewer than three edits:

kitten → sitten (substitution of 's' for 'k')

sitten → sittin (substitution of 'i' for 'e')

sittin → sitting (insert 'g' at the end).

It can be considered a generalization of the Hamming distance, which is used for strings of the same length and only considers substitution edits.

## The algorithm

A commonly-used bottom-up dynamic programming algorithm for computing the Levenshtein distance involves the use of an (n + 1) × (m + 1) matrix, where n and m are the lengths of the two strings. This algorithm is based on the Wagner-Fischer algorithm for edit distance. Here is pseudocode for a function LevenshteinDistance that takes two strings, s of length m, and t of length n, and computes the Levenshtein distance between them:

int LevenshteinDistance(char s[1..m], char t[1..n])

// d is a table with m+1 rows and n+1 columns

declare int d[0..m, 0..n]

for i from 0 to m

d[i, 0] := i

for j from 0 to n

d[0, j] := j

for i from 1 to m

for j from 1 to n

if s[i] = t[j] then cost := 0

else cost := 1

d[i, j] := minimum(

d[i-1, j] + 1, // deletion

d[i, j-1] + 1, // insertion

d[i-1, j-1] + cost // substitution

return d[m, n]

Two examples of the resulting matrix (the minimum steps to be taken are highlighted):

The invariant maintained throughout the algorithm is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. At the end, the bottom-right element of the array contains the answer.

This algorithm is essentially part of a solution to the Longest common subsequence problem (LCS), in the particular case of 2 input lists.

With a minor modification, the same algorithm can also be used in approximate string matching for finding a substring of a text which best matches a given pattern.

### Proof of correctness

As mentioned earlier, the invariant is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. This invariant holds since:

It is initially true on row and column 0 because s[1..i] can be transformed into the empty string t[1..0] by simply dropping all i characters. Similarly, we can transform s[1..0] to t[1..j] by simply adding all j characters.

The minimum is taken over three distances, each of which is feasible:

If we can transform s[1..i] to t[1..j-1] in k operations, then we can simply add t[j] afterwards to get t[1..j] in k+1 operations.

If we can transform s[1..i-1] to t[1..j] in k operations, then we can do the same operations on s[1..i] and then remove the original s[i] at the end in k+1 operations.

If we can transform s[1..i-1] to t[1..j-1] in k operations, we can do the same to s[1..i] and then do a substitution of t[j] for the original s[i] at the end if necessary, requiring k+cost operations.

The operations required to transform s[1..n] into t[1..m] is of course the number required to transform all of s into all of t, and so d[n,m] holds our result.

This proof fails to validate that the number placed in d[i,j] is in fact minimal; this is more difficult to show, and involves an argument by contradiction in which we assume d[i,j] is smaller than the minimum of the three, and use this to show one of the three is not minimal.

### Possible improvements

Possible improvements to this algorithm include:

We can adapt the algorithm to use less space, O(m) instead of O(mn), since it only requires that the previous row and current row be stored at any one time.

We can store the number of insertions, deletions, and substitutions separately, or even the positions at which they occur, which is always j.

We can normalize the distance to the interval [0,1].

If we are only interested in the distance if it is smaller than a threshold k, then it suffices to compute a diagonal stripe of width 2k+1 in the matrix. In this way, the algorithm can be run in O(kl) time, where l is the length of the shortest string.[2]

We can give different penalty costs to insertion, deletion and substitution. We can also give penalty costs that depend on which characters are inserted, deleted or substituted.

The initialization of d[i,0] can be moved inside the main outer loop.

By initializing the first row of the matrix with 0, the algorithm can be used for fuzzy string search of a string in a text [3]. This modification gives the end-position of matching substrings of the text. To determine the start-position of the matching substrings, the number of insertions and deletions can be stored separately and used to compute the start-position from the end-position.[4]

This algorithm parallelizes poorly, due to a large number of data dependencies. However, all the cost values can be computed in parallel, and the algorithm can be adapted to perform the minimum function in phases to eliminate dependencies.

By examining diagonals instead of rows, and by using lazy evaluation, we can find the Levenshtein distance in O(m (1 + d)) time (where d is the Levenshtein distance), which is much faster than the regular dynamic programming algorithm if the distance is small. [5]

### Upper and lower bounds

The Levenshtein distance has several simple upper and lower bounds that are useful in applications which compute many of them and compare them. These include:

It is always at least the difference of the sizes of the two strings.

It is at most the length of the longer string.

It is zero if and only if the strings are identical.

If the strings are the same size, the Hamming distance is an upper bound on the Levenshtein distance.

References:
[1] В.И. Левенштейн (1965) Двоичные коды с исправлением выпадений, вставок и замещений символов. Доклады Академий Наук СССР 163.4:845–848. Appeared in English as: V. I. Levenshtein, Binary codes capable of correcting deletions, insertions, and reversals. Soviet Physics Doklady 10 (1966):707–710.
[2] Dan Gusfield. Algorithms on strings, trees, and sequences: computer science and computational biology. Cambridge University Press, New York, NY, USA, 1997.
[3] Gonzalo Navarro. A guided tour to approximate string matching. ACM Computing Surveys, 33(1):31–88, 2001.
[4] Bruno Woltzenlogel Paleo. An approximate gazetteer for GATE based on levenshtein distance. Student Section of the European Summer School in Logic, Language and Information (ESSLLI), 2007.
[5] L. Allison, Lazy Dynamic-Programming can be Eager. Inf. Proc. Letters 43(4) pp207-212, Sept' 1992 http://www.csse.monash.edu.au/~lloyd/tildeStrings/Alignment/92.IPL.html
````

</details>

<details><summary><b>Step 4 — revision_4</b> (1721 words)</summary>

````text
In information theory and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (i.e. insertions, deletions or substitutions) required to change one word into the other. The phrase edit distance is often used to refer specifically to Levenshtein distance. It is named after Vladimir Levenshtein, who considered this distance in 1965.[1] It is closely related to pairwise string alignments.

## Definition

Mathematically, the Levenshtein distance between two strings a, b is given by \operatorname{lev}_{a,b}(|a|,|b|) where

\qquad\operatorname{lev}_{a,b}(i,j) = \begin{cases}

\max(i,j) & \text{ if} \min(i,j)=0, \\

\min \begin{cases}

\operatorname{lev}_{a,b}(i-1,j) + 1 \\

\operatorname{lev}_{a,b}(i,j-1) + 1 \\

\operatorname{lev}_{a,b}(i-1,j-1) + 1_{(a_i \neq b_j)}

\end{cases} & \text{ otherwise.}

\end{cases}

where 1_{(a_i \neq b_j)} is the indicator function equal to 0 when a_i = b_j and 1 otherwise.

Note that the first element in the minimum corresponds to deletion (from a to b ), the second to insertion and the third to match or mismatch, depending on whether the respective symbols are the same.

### Example

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following three edits change one into the other, and there is no way to do it with fewer than three edits:

kitten → sitten (substitution of "s" for "k")

sitten → sittin (substitution of "i" for "e")

sittin → sitting (insertion of "g" at the end).

### Upper and lower bounds

The Levenshtein distance has several simple upper and lower bounds. These include:

It is always at least the difference of the sizes of the two strings.

It is at most the length of the longer string.

It is zero if and only if the strings are equal.

If the strings are the same size, the Hamming distance is an upper bound on the Levenshtein distance.

The Levenshtein distance between two strings is no greater than the sum of their Levenshtein distances from a third string (triangle inequality).

## Applications

In approximate string matching, the objective is to find matches for short strings in many longer texts, in situations where a small number of differences is to be expected. The short strings could come from a dictionary, for instance. Here, one of the strings is typically short, while the other is arbitrarily long. This has a wide range of applications, for instance, spell checkers, correction systems for optical character recognition, and software to assist natural language translation based on translation memory.

The Levenshtein distance can also be computed between two longer strings, but the cost to compute it, which is roughly proportional to the product of the two string lengths, makes this impractical. Thus, when used to aid in fuzzy string searching in applications such as record linkage, the compared strings are usually short to help improve speed of comparisons.

## Relationship with other edit distance metrics

There are other popular measures of edit distance, which are calculated using a different set of allowable edit operations. For instance,

the Damerau–Levenshtein distance allows insertion, deletion, substitution, and the transposition of two adjacent characters;

the longest common subsequence metric allows only insertion and deletion, not substitution;

the Hamming distance allows only substitution, hence, it only applies to strings of the same length.

Edit distance is usually defined as a parameterizable metric calculated with a specific set of allowed edit operations, and each operation is assigned a cost (possibly infinite). This is further generalized by DNA sequence alignment algorithms such as the Smith–Waterman algorithm, which make an operation's cost depend on where it is applied.

## Computing Levenshtein distance

### Recursive

A straightforward recursive implementation LevenshteinDistance function takes two strings, s and t, and returns the Levenshtein distance between them:

Unfortunately, the straightforward recursive implementation is very inefficient because it recomputes the Levenshtein distance of the same substrings many times. A better method would never repeat the same distance calculation.

For example, the Levenshtein distance of all possible prefixes might be stored in an array d[][] where d[i][j] is the distance between the first i characters of string s and the first j characters of string t. The table is easy to construct one row at a time starting with row 0. When the entire table has been built, the desired distance is d[len_s][len_t]. While this technique is significantly faster, it will consume len_s * len_t more memory than the straightforward recursive implementation.

### Iterative with full matrix

Note: This section uses 1-based strings instead of 0-based strings

Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

This algorithm, an example of bottom-up dynamic programming, is discussed, with variants, in the 1974 article The String-to-string correction problem by Robert A. Wagner and Michael J. Fischer.[2]

A straightforward implementation, as pseudocode for a function LevenshteinDistance that takes two strings, s of length m, and t of length n, and returns the Levenshtein distance between them:

Note that this implementation does not fit the definition precisely: it always prefers matches, even if insertions or deletions provided a better score. This is equivalent; it can be shown that for every optimal alignment (which induces the Levenshtein distance) there is another optimal alignment that prefers matches in the sense of this implementation.[3]

Two examples of the resulting matrix (hovering over a number reveals the operation performed to get that number):

The invariant maintained throughout the algorithm is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. At the end, the bottom-right element of the array contains the answer.

### Proof of correctness

As mentioned earlier, the invariant is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. This invariant holds since:

It is initially true on row and column 0 because s[1..i] can be transformed into the empty string t[1..0] by simply dropping all i characters. Similarly, we can transform s[1..0] to t[1..j] by simply adding all j characters.

If s[i] = t[j], and we can transform s[1..i-1] to t[1..j-1] in k operations, then we can do the same to s[1..i] and just leave the last character alone, giving k operations.

Otherwise, the distance is the minimum of the three possible ways to do the transformation:

If we can transform s[1..i] to t[1..j-1] in k operations, then we can simply add t[j] afterwards to get t[1..j] in k+1 operations (insertion).

If we can transform s[1..i-1] to t[1..j] in k operations, then we can remove s[i] and then do the same transformation, for a total of k+1 operations (deletion).

If we can transform s[1..i-1] to t[1..j-1] in k operations, then we can do the same to s[1..i], and exchange the original s[i] for t[j] afterwards, for a total of k+1 operations (substitution).

The operations required to transform s[1..n] into t[1..m] is of course the number required to transform all of s into all of t, and so d[n,m] holds our result.

This proof fails to validate that the number placed in d[i,j] is in fact minimal; this is more difficult to show, and involves an argument by contradiction in which we assume d[i,j] is smaller than the minimum of the three, and use this to show one of the three is not minimal.

### Possible modifications

Possible modifications to this algorithm include:

We can adapt the algorithm to use less space, O(min(n,m)) instead of O(mn), since it only requires that the previous row and current row be stored at any one time.

We can store the number of insertions, deletions, and substitutions separately, or even the positions at which they occur, which is always j.

We can normalize the distance to the interval [0,1].

If we are only interested in the distance if it is smaller than a threshold k, then it suffices to compute a diagonal stripe of width 2k+1 in the matrix. In this way, the algorithm can be run in O(kl) time, where l is the length of the shortest string.[4]

We can give different penalty costs to insertion, deletion and substitution. We can also give penalty costs that depend on which characters are inserted, deleted or substituted.

By initializing the first row of the matrix with 0, the algorithm can be used for fuzzy string search of a string in a text.[5] This modification gives the end-position of matching substrings of the text. To determine the start-position of the matching substrings, the number of insertions and deletions can be stored separately and used to compute the start-position from the end-position.[6]

This algorithm parallelizes poorly, due to a large number of data dependencies. However, all the cost values can be computed in parallel, and the algorithm can be adapted to perform the minimum function in phases to eliminate dependencies.

By examining diagonals instead of rows, and by using lazy evaluation, we can find the Levenshtein distance in O(m (1 + d)) time (where d is the Levenshtein distance), which is much faster than the regular dynamic programming algorithm if the distance is small.[7]

### Iterative with two matrix rows

It turns out that only two rows of the table are needed for the construction: the previous row and the current row (the one being calculated).

The Levenshtein distance may be calculated iteratively using the following algorithm:[8]

References:
[1] Влади́мир И. Левенштейн. (1965). Двоичные коды с исправлением выпадений, вставок и замещений символов. Доклады Академий Наук СCCP.
[2] Wagner, Robert A.. (1974). The String-to-String Correction Problem. Journal of the ACM. doi:10.1145/321796.321811
[3] Micro-optimisation for edit distance computation: is it valid?
[4] Gusfield, Dan. (1997). Algorithms on strings, trees, and sequences: computer science and computational biology. Cambridge University Press.
[5] Navarro, Gonzalo. (March 2001). A guided tour to approximate string matching. ACM Computing Surveys. doi:10.1145/375360.375365
[6] Bruno Woltzenlogel Paleo. An approximate gazetteer for GATE based on levenshtein distance. Student Section of the European Summer School in Logic, Language and Information (ESSLLI), 2007.
[7] Allison, L.. (September 1992). Lazy Dynamic-Programming can be Eager. Inf. Proc. Letters. doi:10.1016/0020-0190(92)90202-7
[8] Hjelmqvist, Sten. (26 Mar 2012). Fast, memory efficient Levenshtein algorithm. http://www.codeproject.com/Articles/13525/Fast-memory-efficient-Levenshtein-algorithm
````

</details>

<details><summary><b>Step 5 — revision_5</b> (1173 words)</summary>

````text
In information theory and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (i.e. insertions, deletions or substitutions) required to change one word into the other. It is named after Vladimir Levenshtein, who considered this distance in 1965.[1]

Levenshtein distance may also be referred to as edit distance, although that may also denote a larger family of distance metrics. It is closely related to pairwise string alignments.

## Definition

Mathematically, the Levenshtein distance between two strings a, b (of length |a| and |b| respectively) is given by \operatorname{lev}_{a,b}(|a|,|b|) where

\qquad\operatorname{lev}_{a,b}(i,j) = \begin{cases}

\max(i,j) & \text{ if} \min(i,j)=0, \\

\min \begin{cases}

\operatorname{lev}_{a,b}(i-1,j) + 1 \\

\operatorname{lev}_{a,b}(i,j-1) + 1 \\

\operatorname{lev}_{a,b}(i-1,j-1) + 1_{(a_i \neq b_j)}

\end{cases} & \text{ otherwise.}

\end{cases}

where 1_{(a_i \neq b_j)} is the indicator function equal to 0 when a_i = b_j and equal to 1 otherwise, and \operatorname{lev}_{a,b}(i,j) is the distance between the first i characters of a and the first j characters of b .

Note that the first element in the minimum corresponds to deletion (from a to b ), the second to insertion and the third to match or mismatch, depending on whether the respective symbols are the same.

### Example

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following three edits change one into the other, and there is no way to do it with fewer than three edits:

kitten → sitten (substitution of "s" for "k")

sitten → sittin (substitution of "i" for "e")

sittin → sitting (insertion of "g" at the end).

### Upper and lower bounds

The Levenshtein distance has several simple upper and lower bounds. These include:

It is always at least the difference of the sizes of the two strings.

It is at most the length of the longer string.

It is zero if and only if the strings are equal.

If the strings are the same size, the Hamming distance is an upper bound on the Levenshtein distance.

The Levenshtein distance between two strings is no greater than the sum of their Levenshtein distances from a third string (triangle inequality).

An example where the Levenshtein distance between two strings of the same length is strictly less than the Hamming distance is given by the pair "flaw" and "lawn". Here the Levenshtein distance equals 2 (delete "f" from the front; insert "n" at the end). The Hamming distance is 4.

## Applications

In approximate string matching, the objective is to find matches for short strings in many longer texts, in situations where a small number of differences is to be expected. The short strings could come from a dictionary, for instance. Here, one of the strings is typically short, while the other is arbitrarily long. This has a wide range of applications, for instance, spell checkers, correction systems for optical character recognition, and software to assist natural language translation based on translation memory.

The Levenshtein distance can also be computed between two longer strings, but the cost to compute it, which is roughly proportional to the product of the two string lengths, makes this impractical. Thus, when used to aid in fuzzy string searching in applications such as record linkage, the compared strings are usually short to help improve speed of comparisons.

## Relationship with other edit distance metrics

There are other popular measures of edit distance, which are calculated using a different set of allowable edit operations. For instance,

the Damerau–Levenshtein distance allows insertion, deletion, substitution, and the transposition of two adjacent characters;

the longest common subsequence metric allows only insertion and deletion, not substitution;

the Hamming distance allows only substitution, hence, it only applies to strings of the same length.

Edit distance is usually defined as a parameterizable metric calculated with a specific set of allowed edit operations, and each operation is assigned a cost (possibly infinite). This is further generalized by DNA sequence alignment algorithms such as the Smith–Waterman algorithm, which make an operation's cost depend on where it is applied.

## Computing Levenshtein distance

### Recursive

This is a straightforward, but inefficient, recursive C/C++ implementation of a LevenshteinDistance function that takes two strings, s and t, together with their lengths, and returns the Levenshtein distance between them:

This recursive implementation is straightforward, but very inefficient, because it recomputes the Levenshtein distance of the same substrings many times.

A more efficient method would never repeat the same distance calculation. For example, the Levenshtein distance of all possible prefixes might be stored in an array d[][] where d[i][j] is the distance between the first i characters of string s and the first j characters of string t. The table is easy to construct one row at a time starting with row 0. When the entire table has been built, the desired distance is d[len_s][len_t]. While this technique is significantly faster, it will consume len_s * len_t more memory than the straightforward recursive implementation.

### Iterative with full matrix

Note: This section uses 1-based strings instead of 0-based strings

Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

This algorithm, an example of bottom-up dynamic programming, is discussed, with variants, in the 1974 article The String-to-string correction problem by Robert A. Wagner and Michael J. Fischer.[2]

This is a straightforward pseudocode implementation for a function LevenshteinDistance that takes two strings, s of length m, and t of length n, and returns the Levenshtein distance between them:

Note that this implementation does not fit the definition precisely: it always prefers matches, even if insertions or deletions provided a better score. This is equivalent; it can be shown that for every optimal alignment (which induces the Levenshtein distance) there is another optimal alignment that prefers matches in the sense of this implementation.[3]

Two examples of the resulting matrix (hovering over a number reveals the operation performed to get that number):

The invariant maintained throughout the algorithm is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of d[i,j] operations. At the end, the bottom-right element of the array contains the answer.

### Iterative with two matrix rows

It turns out that only two rows of the table are needed for the construction if one does not want to reconstruct the edited input strings (the previous row and the current row being calculated).

The Levenshtein distance may be calculated iteratively using the following algorithm (C# implematation):[4]

References:
[1] Влади́мир И. Левенштейн. (1965). Доклады Академий Наук СCCP.
[2] Wagner, Robert A.. (1974). The String-to-String Correction Problem. Journal of the ACM. doi:10.1145/321796.321811
[3] Micro-optimisation for edit distance computation: is it valid?
[4] Hjelmqvist, Sten. (26 Mar 2012). Fast, memory efficient Levenshtein algorithm. http://www.codeproject.com/Articles/13525/Fast-memory-efficient-Levenshtein-algorithm
````

</details>

<details><summary><b>Step 6 — revision_6</b> (1553 words)</summary>

````text
In information theory, linguistics, and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. It is named after the Soviet mathematician Vladimir Levenshtein, who considered this distance in 1965.[1]

Levenshtein distance may also be referred to as edit distance, although that term may also denote a larger family of distance metrics known collectively as edit distance.[2] It is closely related to pairwise string alignments.

## Definition

The Levenshtein distance between two strings a, b (of length |a| and |b| respectively) is given by \operatorname{lev}(a, b) where

\operatorname{lev}(a, b) = \begin{cases}

|a| & \text{ if } |b| = 0, \\

|b| & \text{ if } |a| = 0, \\

\operatorname{lev}\big(\operatorname{tail}(a),\operatorname{tail}(b)\big) & \text{ if } a[0] = b[0] \\

1 + \min \begin{cases}

\operatorname{lev}\big(\operatorname{tail}(a), b\big) \\

\operatorname{lev}\big(a, \operatorname{tail}(b)\big) \\

\operatorname{lev}\big(\operatorname{tail}(a), \operatorname{tail}(b)\big) \\

\end{cases} & \text{ otherwise,}

\end{cases}

where the \operatorname{tail} of some string x is a string of all but the first character of x , and x[n] is the n th character of the string x , counting from 0.

Note that the first element in the minimum corresponds to deletion (from a to b ), the second to insertion and the third to replacement.

This definition corresponds directly to the naive recursive implementation.

### Example

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following 3 edits change one into the other, and there is no way to do it with fewer than 3 edits:

kitten → sitten (substitution of "s" for "k"),

sitten → sittin (substitution of "i" for "e"),

sittin → sitting (insertion of "g" at the end).

### Upper and lower bounds

The Levenshtein distance has several simple upper and lower bounds. These include:

It is at least the difference of the sizes of the two strings.

It is at most the length of the longer string.

It is zero if and only if the strings are equal.

If the strings have the same size, the Hamming distance is an upper bound on the Levenshtein distance. The Hamming distance is the number of positions at which the corresponding symbols in the two strings are different.

The Levenshtein distance between two strings is no greater than the sum of their Levenshtein distances from a third string (triangle inequality).

An example where the Levenshtein distance between two strings of the same length is strictly less than the Hamming distance is given by the pair "flaw" and "lawn". Here the Levenshtein distance equals 2 (delete "f" from the front; insert "n" at the end). The Hamming distance is 4.

## Applications

In approximate string matching, the objective is to find matches for short strings in many longer texts, in situations where a small number of differences is to be expected. The short strings could come from a dictionary, for instance. Here, one of the strings is typically short, while the other is arbitrarily long. This has a wide range of applications, for instance, spell checkers, correction systems for optical character recognition, and software to assist natural-language translation based on translation memory.

The Levenshtein distance can also be computed between two longer strings, but the cost to compute it, which is roughly proportional to the product of the two string lengths, makes this impractical. Thus, when used to aid in fuzzy string searching in applications such as record linkage, the compared strings are usually short to help improve speed of comparisons.

In linguistics, the Levenshtein distance is used as a metric to quantify the linguistic distance, or how different two languages are from one another.[3] It is related to mutual intelligibility: the higher the linguistic distance, the lower the mutual intelligibility, and the lower the linguistic distance, the higher the mutual intelligibility.

## Relationship with other edit distance metrics

There are other popular measures of edit distance, which are calculated using a different set of allowable edit operations. For instance,

the Damerau–Levenshtein distance allows the transposition of two adjacent characters alongside insertion, deletion, substitution;

the longest common subsequence (LCS) distance allows only insertion and deletion, not substitution;

the Hamming distance allows only substitution, hence, it only applies to strings of the same length.

the Jaro distance allows only transposition.

Edit distance is usually defined as a parameterizable metric calculated with a specific set of allowed edit operations, and each operation is assigned a cost (possibly infinite). This is further generalized by DNA sequence alignment algorithms such as the Smith–Waterman algorithm, which make an operation's cost depend on where it is applied.

## Computing Levenshtein distance

### Recursive

This is a straightforward, but inefficient, recursive Haskell implementation of a lDistance function that takes two strings, s and t, together with their lengths, and returns the Levenshtein distance between them:

This implementation is very inefficient because it recomputes the Levenshtein distance of the same substrings many times.

A more efficient method would never repeat the same distance calculation. For example, the Levenshtein distance of all possible prefixes might be stored in an array M , where M[i][j] is the distance between the last i characters of string s and the last j characters of string t. The table is easy to construct one row at a time starting with row 0. When the entire table has been built, the desired distance is in the table in the last row and column, representing the distance between all of the characters in s and all the characters in t.

### Iterative with full matrix

(Note: This section uses 1-based strings instead of 0-based strings.)

Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

This algorithm, an example of bottom-up dynamic programming, is discussed, with variants, in the 1974 article The String-to-string correction problem by Robert A. Wagner and Michael J. Fischer.[4]

This is a straightforward pseudocode implementation for a function LevenshteinDistance that takes two strings, s of length m, and t of length n, and returns the Levenshtein distance between them:

Two examples of the resulting matrix (hovering over a tagged number reveals the operation performed to get that number):

The invariant maintained throughout the algorithm is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of operations. At the end, the bottom-right element of the array contains the answer.

### Iterative with two matrix rows

It turns out that only two rows of the table the previous row and the current row being calculated are needed for the construction, if one does not want to reconstruct the edited input strings.

The Levenshtein distance may be calculated iteratively using the following algorithm:[5]

This two-row variant is suboptimal: the amount of memory required may be reduced to one row and one (index) word of overhead, for better cache locality.[6]

Hirschberg's algorithm combines this method with divide and conquer. It can compute the optimal edit sequence, and not just the edit distance, in the same asymptotic time and space bounds.[7]

### Adaptive variant

The dynamic variant is not the ideal implementation. An adaptive approach may reduce the amount of memory required and, in the best case, may reduce the time complexity to linear in the length of the shortest string, and, in the worst case, no more than quadratic in the length of the shortest string. The idea is that one can use efficient library functions (std::mismatch) to check for common prefixes and suffixes and only dive into the DP part on mismatch.[6]

### Automata

Levenshtein automata efficiently determine whether a string has an edit distance lower than a given constant from a given string.[8]

### Approximation

The Levenshtein distance between two strings of length n can be approximated to within a factor

(\log n)^{O(1/\varepsilon)},

where ε > 0 is a free parameter to be tuned, in time O(n1 + ε).[9]

### Computational complexity

It has been shown that the Levenshtein distance of two strings of length n cannot be computed in time O(n2 − ε) for any ε greater than zero unless the strong exponential time hypothesis is false.[10]

References:
[1] В. И. Левенштейн. (1965). Доклады Академии Наук СССР. http://mi.mathnet.ru/dan31411
[2] Navarro, Gonzalo. (2001). A guided tour to approximate string matching. ACM Computing Surveys. doi:10.1145/375360.375365
[3] (2007). Receptive multilingualism: linguistic analyses, language policies, and didactic concepts. John Benjamins Publishing Company. https://books.google.com/books?id=8gIEN068J3gC&q=Levenshtein
[4] Wagner, Robert A.. (1974). The String-to-String Correction Problem. Journal of the ACM. doi:10.1145/321796.321811
[5] Hjelmqvist, Sten. (26 Mar 2012). Fast, memory efficient Levenshtein algorithm. http://www.codeproject.com/Articles/13525/Fast-memory-efficient-Levenshtein-algorithm
[6] Clearer / Iosifovich: Blazingly fast levenshtein distance function. https://bitbucket.org/clearer/iosifovich/
[7] Hirschberg, D. S.. (1975). A linear space algorithm for computing maximal common subsequences. Communications of the ACM. doi:10.1145/360825.360861
[8] Schulz, Klaus U.. (2002). Fast String Correction with Levenshtein-Automata. International Journal of Document Analysis and Recognition. doi:10.1007/s10032-002-0082-8
[9] Andoni, Alexandr. (2010). Polylogarithmic approximation for edit distance and the asymmetric query complexity.
[10] Backurs, Arturs. (2015). Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false).
````

</details>

<details><summary><b>Step 7 — revision_7</b> (1765 words)</summary>

````text
In information theory, linguistics, and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. The Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. It is named after Soviet mathematician Vladimir Levenshtein, who defined the metric in 1965.[1]

Levenshtein distance may also be referred to as edit distance, although that term may also denote a larger family of distance metrics.[2] It is closely related to pairwise string alignments.

## Definition

The Levenshtein distance between two strings a, b (of length |a| and |b| respectively) is given by \operatorname{lev}(a, b) where

\operatorname{lev}(a, b) = \begin{cases}

|a| & \text{ if } |b| = 0, \\

|b| & \text{ if } |a| = 0, \\

\operatorname{lev}\big(\operatorname{tail}(a),\operatorname{tail}(b)\big) & \text{ if } \operatorname{head}(a)= \operatorname{head}(b), \\

1 + \min \begin{cases}

\operatorname{lev}\big(\operatorname{tail}(a), b\big) \\

\operatorname{lev}\big(a, \operatorname{tail}(b)\big) \\

\operatorname{lev}\big(\operatorname{tail}(a), \operatorname{tail}(b)\big) \\

\end{cases} & \text{ otherwise}

\end{cases}

where the \operatorname{tail} of some string x is a string of all but the first character of x (i.e. \operatorname{tail}(x_0x_1 \dots x_n)=x_1x_2 \dots x_n ), and \operatorname{head}(x) is the first character of x (i.e. \operatorname{head}(x_0x_1 \dots x_n)=x_0 ). Either the notation x[n] or x_n is used to refer to the n th character of the string x , counting from 0, thus \operatorname{head}(x)=x_0=x[0] .

The first element in the minimum corresponds to deletion (from a to b ), the second to insertion and the third to replacement.

This definition corresponds directly to the naive recursive implementation.

### Example

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following 3 edits change one into the other, and there is no way to do it with fewer than 3 edits:

kitten → sitten (substitution of "s" for "k"),

sitten → sittin (substitution of "i" for "e"),

sittin → sitting (insertion of "g" at the end).

A simple example of a deletion can be seen with "uninformed" and "uniformed" which have a distance of 1:

uninformed → uniformed (deletion of "n").

### Upper and lower bounds

The Levenshtein distance has several simple upper and lower bounds. These include:

It is at least the absolute value of the difference of the sizes of the two strings.

It is at most the length of the longer string.

It is zero if and only if the strings are equal.

If the strings have the same size, the Hamming distance is an upper bound on the Levenshtein distance. The Hamming distance is the number of positions at which the corresponding symbols in the two strings are different.

The Levenshtein distance between two strings is no greater than the sum of their Levenshtein distances from a third string (triangle inequality).

An example where the Levenshtein distance between two strings of the same length is strictly less than the Hamming distance is given by the pair "flaw" and "lawn". Here the Levenshtein distance equals 2 (delete "f" from the front; insert "n" at the end). The Hamming distance is 4.

## Applications

In approximate string matching, the objective is to find matches for short strings in many longer texts, in situations where a small number of differences is to be expected. The short strings could come from a dictionary, for instance. Here, one of the strings is typically short, while the other is arbitrarily long. This has a wide range of applications, for instance, spell checkers, correction systems for optical character recognition, and software to assist natural-language translation based on translation memory.

The Levenshtein distance can also be computed between two longer strings, but the cost to compute it, which is roughly proportional to the product of the two string lengths, makes this impractical. Thus, when used to aid in fuzzy string searching in applications such as record linkage, the compared strings are usually short to help improve speed of comparisons.

In linguistics, the Levenshtein distance is used as a metric to quantify the linguistic distance, or how different two languages are from one another.[3] It is related to mutual intelligibility: the higher the linguistic distance, the lower the mutual intelligibility, and the lower the linguistic distance, the higher the mutual intelligibility.

The Levenshtein distance can be used to quantify the performance of listeners during speech-identification tests, for various applications such as speech audiometry. In this context, Levenshtein distances are calculated to quantify the distance between the stimuli that were presented to the listener and the sequence of phonemes that were identified. The cost associated with phoneme substitutions can either be fixed or depend on the number of phonological features that differ between the two substituted phonemes.[4]

In bioinformatics, the Levenshtein distance and similar algorithms measure the difference between biological sequences, such as those of DNA and protein. The edits in the algorithm correspond to genetic mutations: an insertion, deletion, or substitution of a nucleotide (in DNA) or an amino acid (in protein). A lower distance between two sequences can indicate a closer evolutionary or functional relationship.[5]

## Relationship with other edit distance metrics

There are other popular measures of edit distance, which are calculated using a different set of allowable edit operations. For instance:

the Damerau–Levenshtein distance allows the transposition of two adjacent characters alongside insertion, deletion, substitution;

the longest common subsequence (LCS) distance allows only insertion and deletion, not substitution;

the Hamming distance allows only substitution, hence, it only applies to strings of the same length.

the Jaro distance allows only transposition.

Edit distance is usually defined as a parameterizable metric calculated with a specific set of allowed edit operations, and each operation is assigned a cost (possibly infinite). This is further generalized by DNA sequence alignment algorithms such as the Smith–Waterman algorithm, which make an operation's cost depend on where it is applied.

## Computation

### Recursive

This is a straightforward, but inefficient, recursive Haskell implementation of a lDistance function that takes two strings, s and t, together with their lengths, and returns the Levenshtein distance between them:

This implementation is very inefficient because it recomputes the Levenshtein distance of the same substrings many times.

A more efficient method would never repeat the same distance calculation. For example, the Levenshtein distance of all possible suffixes might be stored in an array M , where M[i][j] is the distance between the last i characters of string s and the last j characters of string t. The table is easy to construct one row at a time starting with row 0. When the entire table has been built, the desired distance is in the table in the last row and column, representing the distance between all of the characters in s and all the characters in t.

### Iterative with full matrix

This section uses 1-based strings rather than 0-based strings. If m is a matrix, m[i,j] is the ith row and the jth column of the matrix, with the first row having index 0 and the first column having index 0.

Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

This algorithm, an example of bottom-up dynamic programming, is discussed, with variants, in the 1974 article The String-to-string correction problem by Robert A. Wagner and Michael J. Fischer.[6]

This is a straightforward pseudocode implementation for a function LevenshteinDistance that takes two strings, s of length m, and t of length n, and returns the Levenshtein distance between them:

Two examples of the resulting matrix (hovering over a tagged number reveals the operation performed to get that number):

The invariant maintained throughout the algorithm is that we can transform the initial segment s[1..i] into t[1..j] using a minimum of operations. At the end, the bottom-right element of the array contains the answer.

### Iterative with two matrix rows

It turns out that only two rows of the table the previous row and the current row being calculated are needed for the construction, if one does not want to reconstruct the edited input strings.

The Levenshtein distance may be calculated iteratively using the following algorithm:[7]

Hirschberg's algorithm combines this method with divide and conquer. It can compute the optimal edit sequence, and not just the edit distance, in the same asymptotic time and space bounds.[8]

### Automata

Levenshtein automata efficiently determine whether a string has an edit distance lower than a given constant from a given string.[9]

### Approximation

The Levenshtein distance between two strings of length n can be approximated to within a factor

(\log n)^{O(1/\varepsilon)},

where ε > 0 is a free parameter to be tuned, in time O(n1 + ε).[10]. Ten years later, researchers discovered an algorithm with the same running time but an approximation factor of f(1/ε), for some function f depending only on ε [11].

### Computational complexity

It has been shown that the Levenshtein distance of two strings of length n cannot be computed in time O(n2 − ε) for any ε greater than zero unless the strong exponential time hypothesis is false.[12]

Another (unconditional) lower bound on the complexity of this problem is \Omega(mn) in a model where the only query on symbols of the strings is comparison of two symbols.[13]

References:
[1] В. И. Левенштейн. (1965). Доклады Академии Наук СССР. http://mi.mathnet.ru/dan31411
[2] Navarro, Gonzalo. (2001). A guided tour to approximate string matching. ACM Computing Surveys. doi:10.1145/375360.375365
[3] (2007-01-01). Receptive multilingualism: linguistic analyses, language policies, and didactic concepts. John Benjamins Publishing Company. https://books.google.com/books?id=8gIEN068J3gC&q=Levenshtein
[4] Fontan, L.. (2016). Using Phonologically Weighted Levenshtein Distances for the Prediction of Microscopic Intelligibility.
[5] Berger, Bonnie. (June 2021). Levenshtein Distance, Sequence Comparison and Biological Database Search. IEEE Transactions on Information Theory. doi:10.1109/TIT.2020.2996543
[6] Wagner, Robert A.. (1974). The String-to-String Correction Problem. Journal of the ACM. doi:10.1145/321796.321811
[7] Hjelmqvist, Sten. (26 Mar 2012). Fast, memory efficient Levenshtein algorithm. http://www.codeproject.com/Articles/13525/Fast-memory-efficient-Levenshtein-algorithm
[8] Hirschberg, D. S.. (1975). A linear space algorithm for computing maximal common subsequences. Communications of the ACM. doi:10.1145/360825.360861
[9] Schulz, Klaus U.. (2002). Fast String Correction with Levenshtein-Automata. International Journal of Document Analysis and Recognition. doi:10.1007/s10032-002-0082-8
[10] Andoni, Alexandr. (2010). Polylogarithmic approximation for edit distance and the asymmetric query complexity.
[11] Andoni, A. (2020). Edit distance in near-linear time: It's a constant factor.
[12] Backurs, Arturs. (2015). Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false).
[13] Wong, C. K.. (1976). Bounds for the string editing problem. Journal of the ACM. doi:10.1145/321921.321923
````

</details>

<details><summary><b>Step 8 — final</b> (1977 words)</summary>

````text
In information theory, linguistics, and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. For two strings, it is the minimum number of single-symbol edits—insertions, deletions, or substitutions—required to transform one string into the other. Each edit has unit cost in the classical definition.[1]

The distance is named after Soviet mathematician Vladimir Levenshtein, who introduced it in 1965 in the context of error-correcting codes.[1] Levenshtein distance is a particular form of edit distance; the latter term is also used for broader models in which the set of allowed operations or their costs differ.[2] It is closely related to sequence alignment.

## Definition

Let a=a_1a_2\dots a_m and b=b_1b_2\dots b_n be two strings. Define D(i,j) as the Levenshtein distance between the prefixes a_1\dots a_i and b_1\dots b_j .

The boundary conditions are

D(i,0)=i,\qquad D(0,j)=j.

For i>0 and j>0 ,

D(i,j)=\min

\begin{cases}

D(i-1,j)+1,\\

D(i,j-1)+1,\\

D(i-1,j-1)+\delta(a_i,b_j),

\end{cases}

where

\delta(a_i,b_j)=

\begin{cases}

0,& a_i=b_j,\\

1,& a_i\ne b_j.

\end{cases}

The three alternatives correspond, respectively, to deleting a_i , inserting b_j , and either matching or substituting the final symbols of the two prefixes.[3]

The Levenshtein distance between the full strings is D(m,n) .

### Example

The Levenshtein distance between kitten and sitting is 3. One optimal edit script is:

kitten → sitten (substitute s for k);

sitten → sittin (substitute i for e);

sittin → sitting (insert g at the end).

A simple deletion example is uninformed → uniformed, which has distance 1.

## Properties and bounds

With unit insertion, deletion, and substitution costs, Levenshtein distance is a metric: it is non-negative, is zero if and only if the two strings are equal, is symmetric, and satisfies the triangle inequality.[2]

For strings of lengths m and n ,

|m-n|\leq \operatorname{lev}(a,b)\leq \max(m,n).

The lower bound follows because a single insertion or deletion changes the string length by only one. The upper bound can be achieved by substituting symbols in the common-length prefix and then inserting or deleting the remainder.

If the two strings have the same length, their Hamming distance is an upper bound on their Levenshtein distance:

\operatorname{lev}(a,b)\leq d_H(a,b).

For example, flaw and lawn have Hamming distance 4 but Levenshtein distance 2: delete f from the beginning and insert n at the end.

If substitutions are disallowed and only insertions and deletions are permitted, the resulting edit distance between strings of lengths m and n is

m+n-2L,

where L is the length of a longest common subsequence. This formula does not apply unchanged to classical Levenshtein distance because a substitution has cost 1 rather than the cost 2 of a deletion followed by an insertion.[3]

## Applications

### Approximate string matching and spelling correction

Levenshtein distance is a basic model in approximate string matching, where strings are allowed to differ by a small number of edits. Applications include spell checkers, correction of optical character recognition output, and approximate lookup in textual databases.[2]

For large collections, systems commonly combine edit-distance computation with filtering, indexing, q-grams, or automata so that the full distance need not be evaluated against every possible candidate.[2]

### Record linkage

In record linkage and deduplication, edit distances can be used as features for comparing names, addresses, and other text fields that may contain spelling variation or transcription errors. In practice, candidate-generation or blocking steps are usually used before detailed pairwise comparison.

### Linguistics and speech

In quantitative linguistics, Levenshtein distance is often applied to phonetic or phonological transcriptions and then aggregated or normalized across comparable items, rather than treating a single raw word pair as a direct measure of the distance between entire languages. It has been used extensively in dialectometry to quantify pronunciation differences between language varieties.[4]

Weighted versions can assign lower or higher costs to phoneme substitutions according to phonological features, for example in speech-identification studies.[5]

### Bioinformatics

Edit distance and sequence alignment are closely related in bioinformatics. Insertions, deletions, and substitutions provide a simple model of differences between biological sequences, although practical sequence-alignment methods generally use richer scoring systems and gap penalties than unit-cost Levenshtein distance.[6]

## Relationship to other string distances

Levenshtein distance is one member of a broader family of edit-distance models.[2]

The Damerau–Levenshtein distance additionally allows a transposition of two adjacent symbols.

The longest-common-subsequence distance allows only insertions and deletions.

The Hamming distance allows only substitutions and therefore applies directly only to strings of equal length.

More general edit-distance models may assign different costs to different operations. Such a weighted edit distance is not automatically a metric for arbitrary cost functions; metric properties depend on the conditions imposed on those costs.[2]

Other string-comparison measures, such as Jaro and Jaro–Winkler similarity, use different matching models rather than a minimum-cost script of insertions, deletions, and substitutions.[7]

Sequence-alignment algorithms such as Needleman–Wunsch and Smith–Waterman solve closely related dynamic-programming problems, but typically optimize alignment scores with application-specific substitution scores and gap penalties rather than classical unit edit costs.[6]

## Computation

### Dynamic programming

The standard dynamic-programming algorithm stores the distances between prefixes of the two input strings. It is commonly associated with Wagner and Fischer's 1974 formulation of the string-to-string correction problem.[3]

The invariant is that d[i,j] is the minimum number of edits needed to transform the first i symbols of s into the first j symbols of t.

The full matrix takes \Theta(mn) time and \Theta(mn) space.[3]

### Memory reduction and edit-script reconstruction

If only the numerical distance is required, each row depends only on the previous row and the current row. By storing the shorter dimension as the row width, the working memory can therefore be reduced to O(\min(m,n)) .[8]

If an optimal edit script is also required, it can be recovered by tracing predecessors through the full matrix. There may be several distinct optimal scripts with the same distance. Divide-and-conquer techniques based on Hirschberg's algorithm can recover an optimal alignment using linear space.[9]

### Distance-sensitive and threshold algorithms

When the true edit distance s is small compared with the input lengths, an exact algorithm need not evaluate the entire dynamic-programming matrix. Ukkonen developed exact threshold and distance-sensitive algorithms whose running time depends on s . One of the algorithms in his 1985 paper runs in O(s\min(m,n)) time; for the unit-cost case, the distance alone can be obtained with space O(\min(s,m,n)) .[8]

These are exact algorithms: the word “approximate” in approximate string matching refers to allowing differences between strings, not to approximating the numerical edit distance.

### Bit-parallel computation

For approximate pattern matching, Gene Myers proposed a bit-vector algorithm in 1999 that packs many dynamic-programming states into machine-word bits, allowing multiple state updates to be performed in parallel with bitwise operations.[10]

This should not be confused with Myers's 1986 O(ND) difference algorithm or the O(NP) sequence-comparison algorithm of Wu, Manber, Myers, and Miller. Those algorithms use shortest edit scripts consisting of insertions and deletions; under that model a substitution is equivalent to a deletion followed by an insertion and therefore costs 2, rather than the unit substitution cost of classical Levenshtein distance.[11]

### Automata

A Levenshtein automaton for a fixed pattern and threshold k recognizes exactly the strings whose Levenshtein distance from the pattern is at most k .[12]

### Approximation

For two strings of length n , Andoni, Krauthgamer, and Onak gave an algorithm running in n^{1+\varepsilon} time with approximation factor (\log n)^{O(1/\varepsilon)} , for every fixed \varepsilon>0 .[13] In 2020, Andoni and Nosatzki obtained a constant-factor approximation in n^{1+\varepsilon} time for every fixed \varepsilon>0 .[14]

### Computational complexity

For equal-length strings of length n , Backurs and Indyk showed in 2015 that an exact algorithm running in O(n^{2-\varepsilon}) time for any constant \varepsilon>0 would falsify the strong exponential time hypothesis (SETH). This is a conditional lower bound rather than an unconditional proof that quadratic time is necessary in all computational models.[15]

An older unconditional lower bound of \Omega(mn) applies in a comparison model in which the only queries allowed on input symbols are equality comparisons.[16]

## Unicode and the unit of comparison

The mathematical definition of Levenshtein distance is over sequences of symbols; it does not itself specify what a “character” in software must be. For Unicode text, an implementation may operate on encoded bytes, code units, Unicode code points, or user-perceived characters represented by extended grapheme clusters. Different choices can produce different distance values.

Unicode Standard Annex #29 defines extended grapheme clusters as an algorithmic approximation to user-perceived characters.[17]

In addition, canonically equivalent Unicode text can be represented by different sequences of code points. Unicode Standard Annex #15 defines normalization forms such as NFC and NFD for canonical equivalence.[18] Consequently, implementations that compare Unicode text should specify both the sequence unit being compared and any normalization performed before the distance is calculated.

## History

Levenshtein's 1965 paper introduced the edit metric in coding theory but did not present the matrix algorithm now commonly used to compute it.[1] Dynamic-programming methods for sequence comparison were developed independently in several areas in the late 1960s and 1970s; Wagner and Fischer's 1974 string-to-string correction formulation became a standard presentation of the quadratic dynamic program.[3,6]

Later work developed linear-space reconstruction, distance-sensitive algorithms, bit-parallel methods, Levenshtein automata, approximation algorithms, and conditional lower bounds on exact computation.[8,10,15]

References:
[1] V. I. Levenshtein, “Binary codes capable of correcting deletions, insertions, and reversals”, Doklady Akademii Nauk SSSR, vol. 163, no. 4, 1965, pp. 845–848. English translation in Soviet Physics Doklady, vol. 10, no. 8, 1966, pp. 707–710. Math-Net.
[2] Gonzalo Navarro, “A guided tour to approximate string matching”, ACM Computing Surveys, vol. 33, no. 1, 2001, pp. 31–88, doi:10.1145/375360.375365.
[3] Robert A. Wagner and Michael J. Fischer, “The String-to-String Correction Problem”, Journal of the ACM, vol. 21, no. 1, 1974, pp. 168–173, doi:10.1145/321796.321811.
[4] Wilbert J. Heeringa, Measuring Dialect Pronunciation Differences using Levenshtein Distance, PhD thesis, University of Groningen, 2004. University of Groningen.
[5] Lionel Fontan, Isabelle Ferrané, Jérôme Farinas, Julien Pinquier, and Xavier Aumont, “Using Phonologically Weighted Levenshtein Distances for the Prediction of Microscopic Intelligibility”, Interspeech 2016, pp. 650–654, doi:10.21437/Interspeech.2016-431.
[6] Bonnie Berger, Michael S. Waterman, and Yun William Yu, “Levenshtein Distance, Sequence Comparison and Biological Database Search”, IEEE Transactions on Information Theory, vol. 67, no. 6, 2021, pp. 3287–3294, doi:10.1109/TIT.2020.2996543.
[7] Matthew A. Jaro, “Advances in Record-Linkage Methodology as Applied to Matching the 1985 Census of Tampa, Florida”, Journal of the American Statistical Association, vol. 84, no. 406, 1989, pp. 414–420, doi:10.1080/01621459.1989.10478785.
[8] Esko Ukkonen, “Algorithms for approximate string matching”, Information and Control, vol. 64, nos. 1–3, 1985, pp. 100–118, doi:10.1016/S0019-9958(85)80046-2.
[9] Daniel S. Hirschberg, “A linear space algorithm for computing maximal common subsequences”, Communications of the ACM, vol. 18, no. 6, 1975, pp. 341–343, doi:10.1145/360825.360861.
[10] Gene Myers, “A fast bit-vector algorithm for approximate string matching based on dynamic programming”, Journal of the ACM, vol. 46, no. 3, 1999, pp. 395–415, doi:10.1145/316542.316550.
[11] Sun Wu, Udi Manber, Gene Myers, and Webb Miller, “An O(NP) sequence comparison algorithm”, Information Processing Letters, vol. 35, no. 6, 1990, pp. 317–323, doi:10.1016/0020-0190(90)90035-V.
[12] Klaus U. Schulz and Stoyan Mihov, “Fast String Correction with Levenshtein-Automata”, International Journal on Document Analysis and Recognition, vol. 5, no. 1, 2002, pp. 67–85, doi:10.1007/s10032-002-0082-8.
[13] Alexandr Andoni, Robert Krauthgamer, and Krzysztof Onak, “Polylogarithmic Approximation for Edit Distance and the Asymmetric Query Complexity”, 51st IEEE Symposium on Foundations of Computer Science, 2010, pp. 377–386, doi:10.1109/FOCS.2010.43.
[14] Alexandr Andoni and Negev Shekel Nosatzki, “Edit Distance in Near-Linear Time: It's a Constant Factor”, IEEE Symposium on Foundations of Computer Science, 2020, pp. 990–1001, doi:10.1109/FOCS46700.2020.00096.
[15] Arturs Backurs and Piotr Indyk, “Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)”, Proceedings of the 47th Annual ACM Symposium on Theory of Computing, 2015, pp. 51–58, doi:10.1145/2746539.2746612.
[16] C. K. Wong and Ashok K. Chandra, “Bounds for the string editing problem”, Journal of the ACM, vol. 23, no. 1, 1976, pp. 13–16, doi:10.1145/321921.321923.
[17] Unicode Consortium, “Unicode Standard Annex #29: Unicode Text Segmentation”. unicode.org.
[18] Unicode Consortium, “Unicode Standard Annex #15: Unicode Normalization Forms”. unicode.org.
````

</details>
