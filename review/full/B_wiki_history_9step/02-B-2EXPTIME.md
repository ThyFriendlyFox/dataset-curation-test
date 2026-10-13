# 2. 2-EXPTIME

`B-2EXPTIME` · [full/B_wiki_history_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=2-EXPTIME&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 50 revisions in history; 25 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 1 | 0 | 0.00 | source_title |
| 1 | revision_1 | 254 | 2 | 0.50 | enwiki rev 133080897 (2007-05-24) |
| 2 | revision_2 | 269 | 2 | 0.53 | enwiki rev 230969452 (2008-08-10) |
| 3 | revision_3 | 270 | 2 | 0.56 | enwiki rev 992532734 (2020-12-05) |
| 4 | revision_4 | 479 | 7 | 0.77 | enwiki rev 1064778788 (2022-01-10) |
| 5 | revision_5 | 508 | 8 | 0.82 | enwiki rev 1281104436 (2025-03-18) |
| 6 | revision_6 | 610 | 11 | 0.89 | enwiki rev 1281107252 (2025-03-18) |
| 7 | revision_7 | 659 | 12 | 0.95 | enwiki rev 1281118849 (2025-03-18) |
| 8 | final | 689 | 13 | 1.00 | enwiki rev 1378637420 (2026-10-05) |

<details><summary><b>Step 0 — title</b> (1 words)</summary>

````text
2-EXPTIME
````

</details>

<details><summary><b>Step 1 — revision_1</b> (254 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP) is the set of all decision problems solvable by a deterministic Turing machine in O(2(2p(n))) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mbox{EXPTIME} = \bigcup_{k \in \mathbb{N} } \mbox{ DTIME } \left( 2^{ 2^{n^k} } \right) .

We know

P \subseteq NP \subseteq PSPACE \subseteq EXPTIME \subseteq NEXPTIME \subseteq EXPSPACE

\subseteq 2-EXPTIME.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE \subseteq 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply-exponential time bound 2^{2^{2^n}} . This can be generalized to higher and higher time bounds.

## 2-EXPTIME-complete problems

Generalizations of many fully observable games are EXPTIME-complete.

These games can be viewed as particular instance of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists.

A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete [2].

References:
[1] Papadimitriou (1994), section 20.1, corollary 3, page 495.
[2] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (269 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP) is the set of all decision problems solvable by a deterministic Turing machine in O(22p(n)) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mbox{2-EXPTIME} = \bigcup_{k \in \mathbb{N} } \mbox{ DTIME } \left( 2^{ 2^{n^k} } \right) .

We know

P \subseteq NP \subseteq PSPACE \subseteq EXPTIME \subseteq NEXPTIME \subseteq EXPSPACE \subseteq 2-EXPTIME \subseteq ELEMENTARY.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE \subseteq 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply-exponential time bound 2^{2^{2^{n^k}}} . This can be generalized to higher and higher time bounds.

## 2-EXPTIME-complete problems

Generalizations of many fully observable games are EXPTIME-complete. These games can be viewed as particular instance of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists.

A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete.[2]

References:
[1] Christos Papadimitriou, Computational Complexity (1994), ISBN 9780201530827. Section 20.1, corollary 3, page 495.
[2] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability. Proceedings of International Conference on Automated Planning and Scheduling.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (270 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP) is the set of all decision problems solvable by a deterministic Turing machine in O(22p(n)) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mathsf{2\mbox{-}EXPTIME} = \bigcup_{k \in \mathbb{N} } \mathsf{ DTIME } \left( 2^{ 2^{n^k} } \right) .

We know

P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ NEXPTIME ⊆ EXPSPACE ⊆ 2-EXPTIME ⊆ ELEMENTARY.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE ⊆ 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply exponential time bound 2^{2^{2^{n^k}}} . This can be generalized to higher and higher time bounds.

## 2-EXPTIME-complete problems

Generalizations of many fully observable games are EXPTIME-complete. These games can be viewed as particular instance of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists.

A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete.[2]

References:
[1] Christos Papadimitriou, Computational Complexity (1994), . Section 20.1, corollary 3, page 495.
[2] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability. Proceedings of International Conference on Automated Planning and Scheduling. http://www.informatik.uni-freiburg.de/~ki/papers/Rintanen03compl.pdf
````

</details>

<details><summary><b>Step 4 — revision_4</b> (479 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP) is the set of all decision problems solvable by a deterministic Turing machine in O(22p(n)) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mathsf{2\mbox{-}EXPTIME} = \bigcup_{k \in \mathbb{N} } \mathsf{ DTIME } \left( 2^{ 2^{n^k} } \right) .

We know

P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ NEXPTIME ⊆ EXPSPACE ⊆ 2-EXPTIME ⊆ ELEMENTARY.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE ⊆ 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply exponential time bound 2^{2^{2^{n^k}}} . This can be generalized to higher and higher time bounds.

## Examples

Examples of algorithms that require at least 2-EXPTIME include:

Each decision procedure for Presburger arithmetic provably requires at least doubly exponential time [2]

Computing a Gröbner basis over a field. In the worst case, a Gröbner basis may have a number of elements which is doubly exponential in the number of variables. On the other hand, the worst-case complexity of Gröbner basis algorithms is doubly exponential in the number of variables as well as in the entry size.[3]

Finding a complete set of associative-commutative unifiers [4]

Satisfying CTL+ (which is, in fact, 2-EXPTIME-complete) [5]

Quantifier elimination on real closed fields takes doubly exponential time (see Cylindrical algebraic decomposition).

Calculating the complement of a regular expression[6]

## 2-EXPTIME-complete problems

Generalizations of many fully observable games are EXPTIME-complete. These games can be viewed as particular instances of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists. A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete.[7]

References:
[1] Christos Papadimitriou, Computational Complexity (1994), . Section 20.1, corollary 3, page 495.
[2] Fischer, M. J., and Michael O. Rabin, 1974, ""Super-Exponential Complexity of Presburger Arithmetic. " Proceedings of the SIAM-AMS Symposium in Applied Mathematics Vol. 7: 27–41
[3] Dubé, Thomas W.. (August 1990). The Structure of Polynomial Ideals and Gröbner Bases. SIAM Journal on Computing. doi:10.1137/0219053
[4] Kapur, Deepak. (1992). Proc. 7th IEEE Symp. Logic in Computer Science (LICS 1992). doi:10.1109/LICS.1992.185515
[5] Johannsen, Jan. (2003). Proceedings of the 30th International Colloquium on Automata, Languages and Programming (ICALP 2003). Springer-Verlag. doi:10.1007/3-540-45061-0_60
[6] Gruber, Hermann. (2008). Finite Automata, Digraph Connectivity, and Regular Expression Size. doi:10.1007/978-3-540-70583-3_4
[7] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability. Proceedings of International Conference on Automated Planning and Scheduling. http://www.informatik.uni-freiburg.de/~ki/papers/Rintanen03compl.pdf
````

</details>

<details><summary><b>Step 5 — revision_5</b> (508 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP) is the set of all decision problems solvable by a deterministic Turing machine in O(22p(n)) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mathsf{2\mbox{-}EXPTIME} = \bigcup_{k \in \mathbb{N} } \mathsf{ DTIME } \left( 2^{ 2^{n^k} } \right) .

We know

P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ NEXPTIME ⊆ EXPSPACE ⊆ 2-EXPTIME ⊆ ELEMENTARY.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE ⊆ 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply exponential time bound 2^{2^{2^{n^k}}} . This can be generalized to higher and higher time bounds.

## Examples

Examples of algorithms that require at least 2-EXPTIME include:

Each decision procedure for Presburger arithmetic provably requires at least doubly exponential time[2]

Computing a Gröbner basis over a field. In the worst case, a Gröbner basis may have a number of elements which is doubly exponential in the number of variables. On the other hand, the worst-case complexity of Gröbner basis algorithms is doubly exponential in the number of variables as well as in the entry size.[3]

Finding a complete set of associative-commutative unifiers[4]

Quantifier elimination on real closed fields takes doubly exponential time (see Cylindrical algebraic decomposition).

Calculating the complement of a regular expression[5]

## 2-EXPTIME-complete problems

### Logic

The satisfiability problem for CTL+ is 2-EXPTIME-complete[6]. The satisfiability problem of ATL* (alternating-time temporal logic) is 2-EXPTIME-complete[7].

### Games

Generalizations of many fully observable games are EXPTIME-complete. These games can be viewed as particular instances of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists.

### Planning

A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete.[8]

References:
[1] Christos Papadimitriou, Computational Complexity (1994), . Section 20.1, corollary 3, page 495.
[2] Fischer, M. J., and Michael O. Rabin, 1974, ""Super-Exponential Complexity of Presburger Arithmetic. " Proceedings of the SIAM-AMS Symposium in Applied Mathematics Vol. 7: 27–41
[3] Dubé, Thomas W.. (August 1990). The Structure of Polynomial Ideals and Gröbner Bases. SIAM Journal on Computing. doi:10.1137/0219053
[4] Kapur, Deepak. (1992). [1992] Proceedings of the Seventh Annual IEEE Symposium on Logic in Computer Science. doi:10.1109/LICS.1992.185515
[5] Gruber, Hermann. (2008). Finite Automata, Digraph Connectivity, and Regular Expression Size. doi:10.1007/978-3-540-70583-3_4
[6] Johannsen, Jan. (2003). Proceedings of the 30th International Colloquium on Automata, Languages and Programming (ICALP 2003). Springer-Verlag. doi:10.1007/3-540-45061-0_60
[7] Schewe, Sven. (2008). ATL* Satisfiability Is 2EXPTIME-Complete. Automata, Languages and Programming. doi:10.1007/978-3-540-70583-3_31
[8] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability. Proceedings of International Conference on Automated Planning and Scheduling. http://www.informatik.uni-freiburg.de/~ki/papers/Rintanen03compl.pdf
````

</details>

<details><summary><b>Step 6 — revision_6</b> (610 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP) is the set of all decision problems solvable by a deterministic Turing machine in O(22p(n)) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mathsf{2\mbox{-}EXPTIME} = \bigcup_{k \in \mathbb{N} } \mathsf{ DTIME } \left( 2^{ 2^{n^k} } \right) .

## Comparison with other complexity classes

We know

P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ NEXPTIME ⊆ EXPSPACE ⊆ 2-EXPTIME ⊆ ELEMENTARY.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE ⊆ 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply exponential time bound 2^{2^{2^{n^k}}} . This can be generalized to higher and higher time bounds.

## Examples

Examples of algorithms that require at least 2-EXPTIME include:

Each decision procedure for Presburger arithmetic provably requires at least doubly exponential time[2]

Computing a Gröbner basis over a field. In the worst case, a Gröbner basis may have a number of elements which is doubly exponential in the number of variables. On the other hand, the worst-case complexity of Gröbner basis algorithms is doubly exponential in the number of variables as well as in the entry size.[3]

Finding a complete set of associative-commutative unifiers[4]

Quantifier elimination on real closed fields takes doubly exponential time (see Cylindrical algebraic decomposition).

Calculating the complement of a regular expression[5]

## 2-EXPTIME-complete problems

### Logic

The satisfiability problem for CTL+ (Computation tree logic) is 2-EXPTIME-complete[6]. The satisfiability problem of ATL* (alternating-time temporal logic) is 2-EXPTIME-complete[7].

Implicational Relevance Logic is 2-EXPTIME-complete[8].

The satisfiability problem for propositional dynamic logic with intersection (IPDL) is 2-EXPTIME-complete[9].

### Games

Generalizations of many fully observable games are EXPTIME-complete. These games can be viewed as particular instances of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists.

### Planning

A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete.[10]

### Synthesis

LTL (linear temporal logic) synthesis (deciding whether a reactive module satisfying an LTL specification) is 2EXPTIME-complete[11].

References:
[1] Christos Papadimitriou, Computational Complexity (1994), . Section 20.1, corollary 3, page 495.
[2] Fischer, M. J., and Michael O. Rabin, 1974, ""Super-Exponential Complexity of Presburger Arithmetic. " Proceedings of the SIAM-AMS Symposium in Applied Mathematics Vol. 7: 27–41
[3] Dubé, Thomas W.. (August 1990). The Structure of Polynomial Ideals and Gröbner Bases. SIAM Journal on Computing. doi:10.1137/0219053
[4] Kapur, Deepak. (1992). [1992] Proceedings of the Seventh Annual IEEE Symposium on Logic in Computer Science. doi:10.1109/LICS.1992.185515
[5] Gruber, Hermann. (2008). Finite Automata, Digraph Connectivity, and Regular Expression Size. doi:10.1007/978-3-540-70583-3_4
[6] Johannsen, Jan. (2003). Proceedings of the 30th International Colloquium on Automata, Languages and Programming (ICALP 2003). Springer-Verlag. doi:10.1007/3-540-45061-0_60
[7] Schewe, Sven. (2008). ATL* Satisfiability Is 2EXPTIME-Complete. Automata, Languages and Programming. doi:10.1007/978-3-540-70583-3_31
[8] Schmitz, Sylvain. (2016). Implicational Relevance Logic Is 2-Exptime-Complete. The Journal of Symbolic Logic. https://www.jstor.org/stable/43864316
[9] Lange, Martin. (2005). 2-Exptime Lower Bounds for Propositional Dynamic Logics with Intersection. The Journal of Symbolic Logic. https://www.jstor.org/stable/27588414
[10] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability. Proceedings of International Conference on Automated Planning and Scheduling. http://www.informatik.uni-freiburg.de/~ki/papers/Rintanen03compl.pdf
[11] Pnueli, A.. (1989-01-03). On the synthesis of a reactive module. Proceedings of the 16th ACM SIGPLAN-SIGACT symposium on Principles of programming languages. doi:10.1145/75277.75293
````

</details>

<details><summary><b>Step 7 — revision_7</b> (659 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP, sometimes also written 2EXPTIME) is the set of all decision problems solvable by a deterministic Turing machine in O(22p(n)) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mathsf{2\mbox{-}EXPTIME} = \bigcup_{k \in \mathbb{N} } \mathsf{ DTIME } \left( 2^{ 2^{n^k} } \right) .

## Comparison with other complexity classes

We know

P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ NEXPTIME ⊆ EXPSPACE ⊆ 2-EXPTIME ⊆ ELEMENTARY.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE ⊆ 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply exponential time bound 2^{2^{2^{n^k}}} . This can be generalized to higher and higher time bounds.

## Examples

Examples of algorithms that require at least double-exponential time include:

Each decision procedure for Presburger arithmetic provably requires at least doubly exponential time[2]

Computing a Gröbner basis over a field. In the worst case, a Gröbner basis may have a number of elements which is doubly exponential in the number of variables. On the other hand, the worst-case complexity of Gröbner basis algorithms is doubly exponential in the number of variables as well as in the entry size.[3]

Finding a complete set of associative-commutative unifiers[4]

Quantifier elimination on real closed fields takes doubly exponential time (see Cylindrical algebraic decomposition). Thus, deciding whether a first-order formula over the real numbers is in 2-EXPTIME. But it was shown to be EXPSPACE and was conjectured to be EXPSPACE-complete in 1986.[5]

Calculating the complement of a regular expression[6]

## 2-EXPTIME-complete problems

### Logic

The satisfiability problem for CTL+ (Computation tree logic) is 2-EXPTIME-complete[7]. The satisfiability problem of ATL* (alternating-time temporal logic) is 2-EXPTIME-complete[8].

Implicational Relevance Logic is 2-EXPTIME-complete[9].

The satisfiability problem for propositional dynamic logic with intersection (IPDL) is 2-EXPTIME-complete[10].

### Planning

Generalizations of many fully observable games are EXPTIME-complete. These games can be viewed as particular instances of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists. A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete.[11]

### Synthesis

LTL (linear temporal logic) synthesis (deciding whether a reactive module satisfying an LTL specification) is 2EXPTIME-complete[12].

References:
[1] Christos Papadimitriou, Computational Complexity (1994), . Section 20.1, corollary 3, page 495.
[2] Fischer, M. J., and Michael O. Rabin, 1974, ""Super-Exponential Complexity of Presburger Arithmetic. " Proceedings of the SIAM-AMS Symposium in Applied Mathematics Vol. 7: 27–41
[3] Dubé, Thomas W.. (August 1990). The Structure of Polynomial Ideals and Gröbner Bases. SIAM Journal on Computing. doi:10.1137/0219053
[4] Kapur, Deepak. (1992). [1992] Proceedings of the Seventh Annual IEEE Symposium on Logic in Computer Science. doi:10.1109/LICS.1992.185515
[5] Ben-Or, Michael. (1986-04-01). The complexity of elementary algebra and geometry. Journal of Computer and System Sciences. doi:10.1016/0022-0000(86)90029-2
[6] Gruber, Hermann. (2008). Finite Automata, Digraph Connectivity, and Regular Expression Size. doi:10.1007/978-3-540-70583-3_4
[7] Johannsen, Jan. (2003). Proceedings of the 30th International Colloquium on Automata, Languages and Programming (ICALP 2003). Springer-Verlag. doi:10.1007/3-540-45061-0_60
[8] Schewe, Sven. (2008). ATL* Satisfiability Is 2EXPTIME-Complete. Automata, Languages and Programming. doi:10.1007/978-3-540-70583-3_31
[9] Schmitz, Sylvain. (2016). Implicational Relevance Logic Is 2-Exptime-Complete. The Journal of Symbolic Logic. https://www.jstor.org/stable/43864316
[10] Lange, Martin. (2005). 2-Exptime Lower Bounds for Propositional Dynamic Logics with Intersection. The Journal of Symbolic Logic. https://www.jstor.org/stable/27588414
[11] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability. Proceedings of International Conference on Automated Planning and Scheduling. http://www.informatik.uni-freiburg.de/~ki/papers/Rintanen03compl.pdf
[12] Pnueli, A.. (1989-01-03). On the synthesis of a reactive module. Proceedings of the 16th ACM SIGPLAN-SIGACT symposium on Principles of programming languages. doi:10.1145/75277.75293
````

</details>

<details><summary><b>Step 8 — final</b> (689 words)</summary>

````text
In computational complexity theory, the complexity class 2-EXPTIME (sometimes called 2-EXP, sometimes also written 2EXPTIME) is the set of all decision problems solvable by a deterministic Turing machine in O(22p(n)) time, where p(n) is a polynomial function of n.

In terms of DTIME,

\mathsf{2\mbox{-}EXPTIME} = \bigcup_{k \in \mathbb{N} } \mathsf{ DTIME } \left( 2^{ 2^{n^k} } \right) .

## Comparison with other complexity classes

We know

P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ NEXPTIME ⊆ EXPSPACE ⊆ 2-EXPTIME ⊆ ELEMENTARY.

2-EXPTIME can also be reformulated as the space class AEXPSPACE, the problems that can be solved by an alternating Turing machine in exponential space. This is one way to see that EXPSPACE ⊆ 2-EXPTIME, since an alternating Turing machine is at least as powerful as a deterministic Turing machine.[1]

2-EXPTIME is one class in a hierarchy of complexity classes with increasingly higher time bounds. The class 3-EXPTIME is defined similarly to 2-EXPTIME but with a triply exponential time bound 2^{2^{2^{n^k}}} . This can be generalized to higher and higher time bounds.

## Examples

Examples of algorithms that require at least double-exponential time include:

Each decision procedure for Presburger arithmetic provably requires at least doubly exponential time[2]

Computing a Gröbner basis over a field. In the worst case, a Gröbner basis may have a number of elements which is doubly exponential in the number of variables. On the other hand, the worst-case complexity of Gröbner basis algorithms is doubly exponential in the number of variables as well as in the entry size.[3]

Finding a complete set of associative-commutative unifiers[4]

Quantifier elimination on real closed fields takes doubly exponential time (see Cylindrical algebraic decomposition). Thus, deciding whether a first-order formula over the real numbers is in 2-EXPTIME. But it was shown to be EXPSPACE and was conjectured to be EXPSPACE-complete in 1986.[5]

Calculating the complement of a regular expression[6]

## 2-EXPTIME-complete problems

### Logic

The satisfiability problem for CTL+ (computation tree logic) is 2-EXPTIME-complete.[7] The satisfiability problem of ATL* (alternating-time temporal logic) is 2-EXPTIME-complete.[8]

Implicational Relevance Logic is 2-EXPTIME-complete.[9]

The satisfiability problem for propositional dynamic logic with intersection (IPDL) is 2-EXPTIME-complete.[10]

### Planning

Generalizations of many fully observable games are EXPTIME-complete. These games can be viewed as particular instances of a class of transition systems defined in terms of a set of state variables and actions/events that change the values of the state variables, together with the question of whether a winning strategy exists. A generalization of this class of fully observable problems to partially observable problems lifts the complexity from EXPTIME-complete to 2-EXPTIME-complete.[11]

### Synthesis

LTL (linear temporal logic) synthesis (deciding whether a reactive module satisfying an LTL specification) is 2-EXPTIME-complete.[12] Best-effort synthesis for an LTL specification is also 2-EXPTIME-complete.[13]

References:
[1] Christos Papadimitriou, Computational Complexity (1994), . Section 20.1, corollary 3, page 495.
[2] Fischer, M. J., and Michael O. Rabin, 1974, ""Super-Exponential Complexity of Presburger Arithmetic. " Proceedings of the SIAM-AMS Symposium in Applied Mathematics Vol. 7: 27–41
[3] Dubé, Thomas W.. (August 1990). The Structure of Polynomial Ideals and Gröbner Bases. SIAM Journal on Computing. doi:10.1137/0219053
[4] Kapur, Deepak. (1992). [1992] Proceedings of the Seventh Annual IEEE Symposium on Logic in Computer Science. doi:10.1109/LICS.1992.185515
[5] Ben-Or, Michael. (1986-04-01). The complexity of elementary algebra and geometry. Journal of Computer and System Sciences. doi:10.1016/0022-0000(86)90029-2
[6] Gruber, Hermann. (2008). Finite Automata, Digraph Connectivity, and Regular Expression Size. doi:10.1007/978-3-540-70583-3_4
[7] Johannsen, Jan. (2003). Proceedings of the 30th International Colloquium on Automata, Languages and Programming (ICALP 2003). Springer-Verlag. doi:10.1007/3-540-45061-0_60
[8] Schewe, Sven. (2008). Automata, Languages and Programming. Springer. doi:10.1007/978-3-540-70583-3_31
[9] Schmitz, Sylvain. (2016). Implicational Relevance Logic Is 2-Exptime-Complete. The Journal of Symbolic Logic. doi:10.1017/jsl.2015.7
[10] Lange, Martin. (2005). 2-Exptime Lower Bounds for Propositional Dynamic Logics with Intersection. The Journal of Symbolic Logic. doi:10.2178/jsl/1129642115
[11] Jussi Rintanen. (2004). Complexity of Planning with Partial Observability. Proceedings of International Conference on Automated Planning and Scheduling. http://www.informatik.uni-freiburg.de/~ki/papers/Rintanen03compl.pdf
[12] Pnueli, A.. (1989-01-03). Proceedings of the 16th ACM SIGPLAN-SIGACT symposium on Principles of programming languages - POPL '89. Association for Computing Machinery. doi:10.1145/75277.75293
[13] Aminof, Benjamin. (2021). Best-Effort Synthesis: Doing Your Best Is Not Harder Than Giving Up. Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21). doi:10.24963/ijcai.2021/243
````

</details>
