# 7. Bogosort

`B-Bogosort` · [B_wiki_history_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Bogosort&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 888 revisions in history; 36 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 1 | 0 | 0.00 | source_title |
| 1 | revision_1 | 125 | 0 | 0.05 | enwiki rev 338239 (2002-10-05) |
| 2 | revision_2 | 273 | 0 | 0.17 | enwiki rev 11115837 (2005-03-14) |
| 3 | revision_3 | 663 | 3 | 0.33 | enwiki rev 190652200 (2008-02-11) |
| 4 | revision_4 | 633 | 5 | 0.41 | enwiki rev 435705977 (2011-06-22) |
| 5 | revision_5 | 676 | 8 | 0.48 | enwiki rev 517676390 (2012-10-14) |
| 6 | revision_6 | 496 | 6 | 0.72 | enwiki rev 1194317495 (2024-01-08) |
| 7 | revision_7 | 503 | 6 | 0.78 | enwiki rev 1281185981 (2025-03-18) |
| 8 | final | 729 | 7 | 1.00 | enwiki rev 1371942247 (2026-08-29) |

<details><summary><b>Step 0 — title</b> (1 words)</summary>

````text
Bogosort
````

</details>

<details><summary><b>Step 1 — revision_1</b> (125 words)</summary>

````text
Bogosort: According to the Jargon file, it is "the archetypal perversely awful algorithm." and it is "equivalent to repeatedly throwing a deck of cards in the air, picking them up at random, and then testing whether they are in order." C code snippet follows:

void bogo_sort (int *A)

int i, j;

srand (time(0));

while (!sorted(A))

B = make_visited (length(A));

for (i = 0; i < length(A); ++i)

j = rand () % length (A);

if (!B[j])

A[i] = A[j];

B[j]++;

int *make_visited (int k)

int i, *C = malloc (k*sizeof(int));

for (i = 0; i < k; ++i)

C[i] = 0;

return C;

int sorted (int *A)

int i;

for (i = 0; i < length(A); ++i)

if (A[i] > A[i+1])

return 0;

return 1;
````

</details>

<details><summary><b>Step 2 — revision_2</b> (273 words)</summary>

````text
According to the Jargon File, bogosort is "the archetypal perversely awful algorithm", one example of which is attempting to sort a deck of cards by repeatedly throwing the deck in the air, picking the cards up at random, and then testing whether the cards are in sorted order. It is named after the humourous term quantum bogodynamics and ultimately, the word bogus. Other names are bozo sort and blort sort.

Here is the pseudocode of the algorithm:

while not is_sorted(array)

array := random_permutation(array)

This sorting algorithm is probabilistic in nature. If all elements to be sorted are distinct, the expected complexity is O(n × n!). The exact expected running time depends on how many different element values occur, and how often each of them occurs, but for non-trivial cases the expected running time is exponential or super-exponential in n. It terminates for the same reason that the infinite monkey theorem holds; there is some probability of getting the right permutation, so given an infinite number of tries it must eventually find it.

It should be noted that with real-world pseudo-random number algorithms, which have a finite number of states and are not in any case actually random, the algorithm may never terminate for certain inputs.

Bogosort is not a stable sort.

## Implementations

### Python

import random

def is_sorted(aList):

sortedCopy = aList[:]

sortedCopy.sort()

return sortedCopy == aList

def bogosort(aList):

while not is_sorted(aList):

random.shuffle(aList)

### C++

#include <algorithm>

#include <vector>

template<class T>

void bogosort(std::vector<T>& array)

while (! is_sorted(array))

std::random_shuffle(array.begin(), array.end());

template<class T>

bool is_sorted(const std::vector<T>& array)

for (typename std::vector<T>::size_type i = 1; i < array.size(); ++i)

if (array[i] < array[i-1]) return false;

return true;
````

</details>

<details><summary><b>Step 3 — revision_3</b> (663 words)</summary>

````text
In computer science, bogosort (also random sort) is a particularly ineffective sorting algorithm. Its only use is for educational purposes, to contrast it with other more realistic algorithms. Used to sort a deck of cards, it would consist of testing the deck for order, and if not, throwing the deck in the air, picking the cards up at random, and repeating the process. It is named after the humorous term quantum bogodynamics and, ultimately, the word bogus.

## Implementation

In pseudocode

while not InOrder(deck) do Shuffle(deck);

## Running time and termination

This sorting algorithm is probabilistic in nature. If all elements to be sorted are distinct, the expected number of comparisons in the average case is asymptotically equivalent to (e-1)× n!, and the expected number of swaps in the average case equals (n-1)×n!.[1] The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons no matter how many elements there are, but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads every time.

The best case occurs if the list as given is already sorted; in this case the expected number of comparisons is n-1, and no swaps at all are carried out.[1] For dealing with a list of two elements, this places Bogosort amongst the best sorting methods: one comparison, and then either it finishes, or else there is one swap and one more comparison. If that second comparison were omitted, then the best possible sequence would be attained.

The exact expected running time depends on how many different element values occur, and how often each of them occurs, but one might expect that for non-trivial cases the expected running time is super-exponential in n since n! outgrows an for every constant a.

It terminates for the same reason that the infinite monkey theorem holds; there is some probability of getting the right permutation, so given an unbounded number of tries it must eventually be stumbled upon. For this though, the shuffle process must never repeat its pattern, which will happen if it relies upon random number generators that are not perfect, as are all pseudo-random generators.

## Related algorithms

### Bozo sort

Bozo sort is another sorting algorithm based on random numbers. If the list is not in order, it picks two items at random and swaps them, then checks to see if the list is sorted. The running time analysis of Bozo Sort is more difficult, but some estimates are found in H. Gruber's analysis of perversely awful randomized sorting algorithms.[1]

### Quantum Bogosort

An in-joke among some computer scientists is that quantum computing could be used to effectively implement a bogosort with a time complexity of O(n). It uses true quantum randomness to randomly permute the list. By the many-worlds interpretation of quantum physics, the quantum randomization spawns an infinite array of universes and some of these will be such that the single shuffle had produced the list in sorted order because the total number of distinct orderings, though large, is not infinite. The list is then tested for sortedness (requiring n-1 comparisons); should it be out of order, the computer triggers its "destroy universe" operation. Only in the surviving universes will there be observers to see that the randomization worked first time and that the list is in sorted order.

Note, however, that even here there is no free lunch -- while this algorithm is O(n) in time, permuting the list requires that we consume O(n log n) bits of quantum randomness.

References:
[1] H. Gruber, M. Holzer and O. Ruepp: Sorting the Slow Way: An Analysis of Perversely Awful Randomized Sorting Algorithms, 4th International Conference on Fun with Algorithms, Castiglioncello, Italy, 2007, Lecture Notes in Computer Science 4475, pp. 183-197.
````

</details>

<details><summary><b>Step 4 — revision_4</b> (633 words)</summary>

````text
## Overview

In computer science, bogosort (also stupid sort[1]) is a particularly ineffective sorting algorithm. Its only use is for educational purposes, to contrast it with other more realistic algorithms. If bogosort were used to sort a deck of cards, it would consist of checking if the deck were in order, and if it were not, throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. Its name comes from the word bogus.

## Description of the algorithm

Following is a description of the algorithm in pseudocode.

while not inOrder(deck) do

shuffle(deck);

## Running time and termination

This sorting algorithm is probabilistic in nature. If all elements to be sorted are distinct, the expected number of comparisons in the average case is asymptotically equivalent to (e-1) n! , and the expected number of swaps in the average case equals (n-1) n! .[2] The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons no matter how many elements there are, but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads any number of times in a row.

The best case occurs if the list as given is already sorted; in this case the expected number of comparisons is n-1 , and no swaps at all are carried out.[2]

For any collection of fixed size, the expected running time of the algorithm is finite for much the same reason that the infinite monkey theorem holds: there is some probability of getting the right permutation, so given an unbounded number of tries it will almost surely eventually be chosen. However, if a pseudorandom number generator is used in place of a random source, it may never terminate, since these exhibit long-term cyclic behavior.

## Related algorithms

### Goro sort

Goro sort is a sorting algorithm introduced in the 2011 Google Code Jam.[3] As long as the list is not in order, a subset of all elements is randomly permuted. If this subset is optimally chosen each time this is performed, the expected value of the total number of times this operation needs to be done is equal to the number of misplaced elements.

### Bozo sort

Bozo sort is another sorting algorithm based on random numbers. If the list is not in order, it picks two items at random and swaps them, then checks to see if the list is sorted. The running time analysis of Bozo Sort is more difficult, but some estimates are found in H. Gruber's analysis of perversely awful randomized sorting algorithms.[2] O(n!) is found to be the expected average case.

### Quantum bogosort

An in-joke among some computer scientists is that quantum computing could be used to effectively implement a bogosort with a time complexity of O(n). It uses true quantum randomness to randomly permute the list. The list is then inspected, and if it is not in order, the universe is destroyed. By the many-worlds interpretation of quantum physics, the quantum randomization spawns 2^N (where N is the number of random bits) universes and one of these will be such that this single shuffle had produced the list in sorted order.

References:
[1] E. S. Raymond. "bogo-sort". The New Hacker’s Dictionary. MIT Press, 1996.
[2] H. Gruber, M. Holzer and O. Ruepp: Sorting the Slow Way: An Analysis of Perversely Awful Randomized Sorting Algorithms, 4th International Conference on Fun with Algorithms, Castiglioncello, Italy, 2007, Lecture Notes in Computer Science 4475, pp. 183-197.
[3] Google Code Jam 2011, Qualification Rounds, Problem D
````

</details>

<details><summary><b>Step 5 — revision_5</b> (676 words)</summary>

````text
In computer science, bogosort[1,2] (also stupid sort[3] or slowsort[4,5]) is a particularly ineffective sorting algorithm based on the generate and test paradigm. It is not useful for sorting, but may be used for educational purposes, to contrast it with other more realistic algorithms; it has also been used as an example in logic programming.[2,4,5] If bogosort were used to sort a deck of cards, it would consist of checking if the deck were in order, and if it were not, throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. Its name comes from the word bogus.

## Description of the algorithm

Following is a description of the algorithm in pseudocode.

while not isInOrder(deck) do

shuffle(deck);

## Running time and termination

This sorting algorithm is probabilistic in nature. If all elements to be sorted are distinct, the expected number of comparisons in the average case is asymptotically equivalent to (e-1) n! , and the expected number of swaps in the average case equals (n-1) n! .[1] The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons no matter how many elements there are, but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads any number of times in a row.

The best case occurs if the list as given is already sorted; in this case the expected number of comparisons is n-1 , and no swaps at all are carried out.[1]

For any collection of fixed size, the expected running time of the algorithm is finite for much the same reason that the infinite monkey theorem holds: there is some probability of getting the right permutation, so given an unbounded number of tries it will almost surely eventually be chosen. However, if a pseudorandom number generator is used in place of a random source, it may never terminate, since these exhibit long-term cyclic behavior.

## Related algorithms

Goro sort is a sorting algorithm introduced in the 2011 Google Code Jam.[6] As long as the list is not in order, a subset of all elements is randomly permuted. If this subset is optimally chosen each time this is performed, the expected value of the total number of times this operation needs to be done is equal to the number of misplaced elements.

Bozo sort is another sorting algorithm based on random numbers. If the list is not in order, it picks two items at random and swaps them, then checks to see if the list is sorted. The running time analysis of Bozo Sort is more difficult, but some estimates are found in H. Gruber's analysis of perversely awful randomized sorting algorithms.[1] O(n!) is found to be the expected average case.

Quantum bogosort An in-joke among some computer scientists is that quantum computing could be used to effectively implement a bogosort with a time complexity of O(n). It uses true quantum randomness to randomly permute the list. The list is then inspected, and if it is not in order, the universe is destroyed. By the many-worlds interpretation of quantum physics, the quantum randomization spawns 2^N (where N is the number of random bits) universes and one of these will be such that this single shuffle had produced the list in sorted order.

References:
[1] Gruber, H.. 4th International Conference on Fun with Algorithms, Castiglioncello, Italy, 2007. Springer-Verlag. doi:10.1007/978-3-540-72914-3_17
[2] Kiselyov, Oleg. (2005). Proceedings of the Tenth ACM SIGPLAN International Conference on Functional Programming (ICFP '05). doi:10.1145/1086365.1086390
[3] E. S. Raymond. "bogo-sort". The New Hacker’s Dictionary. MIT Press, 1996.
[4] Naish, Lee. (1986). Proceedings of the Third International Conference on Logic Programming. Springer-Verlag. doi:10.1007/3-540-16492-8_111
[5] Naish, Lee. (June 1995). Pruning in logic programming. Department of Computer Science, University of Melbourne.
[6] Google Code Jam 2011, Qualification Rounds, Problem D
````

</details>

<details><summary><b>Step 6 — revision_6</b> (496 words)</summary>

````text
In computer science, bogosort[1,2] (also known as permutation sort and stupid sort[3]) is a sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not considered useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms.

Two versions of this algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted one,[2,4] and a randomized version that randomly permutes its input. An analogy for the working of the latter version is to sort a deck of cards by throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. The worst-case happen with this version if the random source is of low quality and happens to make the sorted permutation unboundedly unlikely to occur. Its name is a portmanteau of the words bogus and sort.[5]

## Description of the algorithm

The following is a description of the randomized algorithm in pseudocode:

while not sorted(deck):

shuffle(deck)

This is the code written in C.

Here is the above pseudocode rewritten in Python 3:

This code assumes that data is a simple, mutable, array-like data structure—like Python's built-in list—whose elements can be compared without issue.

## Running time and termination

If all elements to be sorted are distinct, the expected number of comparisons performed in the average case by randomized bogosort is asymptotically equivalent to (e − 1)n!, and the expected number of swaps in the average case equals (n − 1)n!.[1] The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons, no matter how many elements there are; but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads any number of times in a row.

The best case occurs if the list as given is already sorted; in this case the expected number of comparisons is n − 1, and no swaps at all are carried out.[1]

For any collection of fixed size, the expected running time of the algorithm is finite for much the same reason that the infinite monkey theorem holds: there is some probability of getting the right permutation, so given an unbounded number of tries it will almost surely eventually be chosen.

## Related algorithms

References:
[1] Gruber, H.. 4th International Conference on Fun with Algorithms, Castiglioncello, Italy, 2007. Springer-Verlag. doi:10.1007/978-3-540-72914-3_17
[2] Kiselyov, Oleg. (2005). Proceedings of the Tenth ACM SIGPLAN International Conference on Functional Programming (ICFP '05). doi:10.1145/1086365.1086390
[3] E. S. Raymond. "bogo-sort". The New Hacker’s Dictionary. MIT Press, 1996.
[4] Naish, Lee. (1986). Proceedings of the Third International Conference on Logic Programming. Springer-Verlag. doi:10.1007/3-540-16492-8_111
[5] bogosort. xlinux.nist.gov. https://xlinux.nist.gov/dads/HTML/bogosort.html
````

</details>

<details><summary><b>Step 7 — revision_7</b> (503 words)</summary>

````text
In computer science, bogosort[1,2] (also known as permutation sort and stupid sort[3]) is a sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not considered useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms. The algorithm's name is a portmanteau of the words bogus and sort.[4]

Two versions of this algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted one,[2,5] and a randomized version that randomly permutes its input and checks whether it is sorted. An analogy for the working of the latter version is to sort a deck of cards by throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. In a worst-case scenario with this version, the random source is of low quality and happens to make the sorted permutation unlikely to occur.

## Description of the algorithm

### Pseudocode

The following is a description of the randomized algorithm in pseudocode:

while deck is not sorted:

shuffle(deck)

### C

An implementation in C:

### Python

An implementation in Python:

This code assumes that data is a simple, mutable, array-like data structure—like Python's built-in list—whose elements can be compared without issue.

## Running time and termination

If all elements to be sorted are distinct, the expected number of comparisons performed in the average case by randomized bogosort is asymptotically equivalent to (e − 1)n!, and the expected number of swaps in the average case equals (n − 1)n!.[1] The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons, no matter how many elements there are; but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads any number of times in a row.

The best case occurs if the list as given is already sorted; in this case the expected number of comparisons is n − 1, and no swaps at all are carried out.[1]

For any collection of fixed size, the expected running time of the algorithm is finite for much the same reason that the infinite monkey theorem holds: there is some probability of getting the right permutation, so given an unbounded number of tries it will almost surely eventually be chosen.

## Related algorithms

References:
[1] Gruber, H.. (2007). 4th International Conference on Fun with Algorithms, Castiglioncello, Italy, 2007. Springer-Verlag. doi:10.1007/978-3-540-72914-3_17
[2] Kiselyov, Oleg. (2005). Proceedings of the Tenth ACM SIGPLAN International Conference on Functional Programming (ICFP '05). doi:10.1145/1086365.1086390
[3] E. S. Raymond. "bogo-sort". The New Hacker’s Dictionary. MIT Press, 1996.
[4] bogosort. xlinux.nist.gov. https://xlinux.nist.gov/dads/HTML/bogosort.html
[5] Naish, Lee. (1986). Proceedings of the Third International Conference on Logic Programming. Springer-Verlag. doi:10.1007/3-540-16492-8_111
````

</details>

<details><summary><b>Step 8 — final</b> (729 words)</summary>

````text
In computer science, bogosort[1,2] (also known as permutation sort and stupid sort[3]) is a sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not considered useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms. The algorithm's name is a portmanteau of the words bogus and sort.[4]

Two versions of this algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted one,[2,5] and a randomized version that randomly permutes its input and checks whether it is sorted. An analogy for the working of the latter version is to sort a deck of cards by throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. In a worst-case scenario with this version, the random source is of low quality and happens to make the sorted permutation unlikely to occur.

## Probabilistic analysis

Although Bogosort is primarily discussed as a pedagogical example of an inefficient sorting algorithm, it can also be connected to basic probability theory.

One way to analyze its expected behavior is to consider the probability of obtaining a sorted sequence after repeated random shuffles. This is analogous to the general formula for the probability of at least one success in a series of independent trials:

P(\text{at least one success}) = 1 - (P(\text{failure in one trial}))^n

Here, n represents the number of independent shuffles (trials). In the context of Bogosort, a "success" corresponds to producing a sorted permutation, while a "failure" corresponds to producing an unsorted permutation. Since only one of the n! possible permutations is sorted, the probability of success in a single trial is 1/n! . Thus, the probability of obtaining a sorted list within k shuffles is:

P(\text{sorted within } k \text{ shuffles}) = 1 - \left(1 - \tfrac{1}{n!}\right)^k

This framing highlights the extreme inefficiency of Bogosort: even for modest values of n , the probability of success remains vanishingly small unless k is astronomically large.[6,7]

## Description of the algorithm

### Pseudocode

The following is a description of the randomized algorithm in pseudocode:

function bogoSort(deck: List):

while deck is not sorted:

shuffle(deck)

### C

An implementation in C:

### Python

An implementation in Python:

This code creates a random array - random_array - in generate_random_array that would be sorted by shuffling it in bogosort. All data in the array is natural numbers from 1 - 100.

## Running time and termination

If all elements to be sorted are distinct, the expected number of comparisons performed in the average case by randomized bogosort is asymptotically equivalent to (e-1)n! , and the expected number of swaps in the average case equals (n-1)n! .[1] The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons, no matter how many elements there are; but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads any number of times in a row.

The best case occurs if the list as given is already sorted; in this case the expected number of comparisons is n - 1 , and no swaps at all are carried out.[1]

For any collection of fixed size, the expected running time of the algorithm is finite for much the same reason that the infinite monkey theorem holds: there is some probability of getting the right permutation, so given an unbounded number of tries it will almost surely eventually be chosen.

## Related algorithms

References:
[1] Gruber, H.. (2007). 4th International Conference on Fun with Algorithms, Castiglioncello, Italy, 2007. Springer-Verlag. doi:10.1007/978-3-540-72914-3_17
[2] Kiselyov, Oleg. (2005). Proceedings of the Tenth ACM SIGPLAN International Conference on Functional Programming (ICFP '05). doi:10.1145/1086365.1086390
[3] E. S. Raymond. "bogo-sort". The New Hacker’s Dictionary. MIT Press, 1996.
[4] bogosort. xlinux.nist.gov. https://xlinux.nist.gov/dads/HTML/bogosort.html
[5] Naish, Lee. (1986). Proceedings of the Third International Conference on Logic Programming. Springer-Verlag. doi:10.1007/3-540-16492-8_111
[6] Bobbitt, Zach. (2021-01-05). How to Find the Probability of "At Least One" Success. Statology. https://www.statology.org/probability-of-at-least-one-success/
[7] Major, Leslie. (2024-04-01). Calculating At Least, At Most and More Than ‘X’ Events. https://pressbooks.bccampus.ca/1130sandbox/chapter/at-most-and-at-least/
````

</details>
