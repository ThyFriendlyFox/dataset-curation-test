# 7. Halting problem — History

`A-wiki_Halting_problem` · [A_reconstructed_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Halting_problem&oldid=1378690130> · License: https://creativecommons.org/licenses/by-sa/4.0/

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | prompt | 39 | 0 | 0.03 | reconstructed |
| 1 | skeleton_outline | 66 | 0 | 0.05 | reconstructed |
| 2 | detailed_outline | 438 | 0 | 0.29 | reconstructed |
| 3 | partial_draft | 504 | 0 | 0.42 | reconstructed |
| 4 | rough_draft | 991 | 0 | 0.79 | reconstructed |
| 5 | draft_citation_needed | 1009 | 0 | 0.78 | reconstructed |
| 6 | cited_draft | 1125 | 9 | 0.86 | reconstructed |
| 7 | revised_draft | 1081 | 9 | 0.95 | reconstructed |
| 8 | final | 1101 | 9 | 1.00 | source |

<details><summary><b>Step 0 — prompt</b> (39 words)</summary>

````text
Write the History section of the encyclopedia article on the halting problem: a short intro, a timeline of the events leading up to it from Hilbert onward, and a subsection on where the term "halting problem" actually comes from.
````

</details>

<details><summary><b>Step 1 — skeleton_outline</b> (66 words)</summary>

````text
- Intro: Church's and Turing's proofs, halting problem emerges later
## Timeline
- Hilbert's problems and the 1928 questions
- Post, Gödel, Church in the early 1930s
- Turing's 1936 paper and the equivalence of definitions
- Kleene's formulations and Davis's first use of the term
## Origin of the halting problem
- Misattribution to Turing; who really coined the term
- Halting vs. printing problems
````

</details>

<details><summary><b>Step 2 — detailed_outline</b> (438 words)</summary>

````text
- Intro
  - Church: proof of undecidability of a problem in lambda calculus, April 1936
  - Turing's proof later, January 1937
  - many other undecidable problems since; halting problem emerged in 1950s
## Timeline
- 1900: Hilbert, "23 questions" (Hilbert's problems), Second International Congress of Mathematicians, Paris
  - [quote: the second problem = consistency of Peano axioms]
- 1920–1921: Emil Post, halting problem for tag systems, candidate for unsolvability
  - unsolvability established much later, by Marvin Minsky
- 1928: Hilbert recasts 'Second Problem', Bologna International Congress
  - three questions: complete? consistent? decidable?
  - third = Entscheidungsproblem (Decision Problem)
- 1930: Gödel announces proof answering first two of the 1928 questions
  - [quote: Hilbert's reaction; Gödel didn't think it contradicted Hilbert's formalism]
- 1931: Gödel publishes "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I"
- 19 April 1935: Church, "An Unsolvable Problem of Elementary Number Theory"
  - effectively calculable = general recursive functions = lambda-definable functions
  - halting problem for lambda calculus (does a lambda-expression have a normal form) not effectively calculable
- 1936: Church, first proof Entscheidungsproblem unsolvable, via recursive functions
- 7 October 1936: Post's "Finite Combinatory Processes. Formulation I" received
  - instruction "(C) Stop"; [quote: "type 1" process]
- May 1936 – January 1937: Turing, On Computable Numbers With an Application to the Entscheidungsproblem
  - to press May 1936, in print January 1937
  - three problems undecidable: "satisfaction", "printing", Entscheidungsproblem
  - differs from Church: computation by machine
  - one of the "first examples of decision problems proved unsolvable"
- 1939: J. Barkley Rosser, essential equivalence of "effective method" (Gödel, Church, Turing)
- 1943: Kleene paper, [quote: procedure that necessarily terminates, 'Yes' or 'No']
- 1952: Kleene, halting problem for Turing machines, machines that "eventually stop"
  - [quote: Kleene 1952]
- 1952: Martin Davis uses 'halting problem' in lectures, Control Systems Laboratory, University of Illinois
  - likely first use of the term
## Origin of the halting problem
- papers/textbooks credit Turing's 1936 paper -> not correct
  - Turing never used "halt"/"halting" in published works
- literature search 1936–1958: first published use = Rogers (1957)
  - but Rogers had draft of Davis (1958); Davis intro [quote: "some novelty in the arrangement"]
  - so terminology attributed to Davis; letter: using it since 1952
- [quote: Davis's book, definition + Theorem 2.2 + printing problem]
- precursor: Kleene 1952, differs only in wording [quote]
- halting problem Turing equivalent to Davis's printing problem and Turing's 1936 printing problem
  - Turing equivalence loose; machines print but don't halt, halt but don't print
  - different issues, conceptual and technical differences
  - Davis being modest [quote: Davis on Turing]
````

</details>

<details><summary><b>Step 3 — partial_draft</b> (504 words)</summary>

````text
In April 1936 Alonzo Church published a proof that a problem in the lambda calculus was undecidable. Turing's proof came later, in January 1937. Since then many other undecidable problems have been described, and the halting problem is one of them; it emerged in the 1950s.

## Timeline

- 1900: David Hilbert poses his "23 questions", which are now known as Hilbert's problems, at the Second International Congress of Mathematicians in Paris. [quote: the second problem was proving the consistency of the Peano axioms]

- 1920–1921: Emil Post looks at the halting problem for tag systems and thinks it is a candidate for unsolvability. It was not shown to be unsolvable until much later, by Marvin Minsky.

- 1928: At the Bologna International Congress Hilbert recasts his 'Second Problem'. He posed three questions: #1 was mathematics complete, #2 was mathematics consistent, #3 was mathematics decidable. The third question is the Entscheidungsproblem (Decision Problem).

- 1930: Kurt Gödel announces a proof that answers the first two of Hilbert's 1928 questions. [quote: Hilbert angry and frustrated at first; Gödel felt his work did not contradict Hilbert's formalism]

- 1931: Gödel publishes "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I".

- 19 April 1935: Alonzo Church publishes "An Unsolvable Problem of Elementary Number Theory". In it he proposes that the intuitive notion of an effectively calculable function can be formalized by the general recursive functions, or equivalently by the lambda-definable functions. He proves that the halting problem for lambda calculus (whether a given lambda-expression has a normal form) is not effectively calculable.

- 1936: Church publishes the first proof that the Entscheidungsproblem is unsolvable, using recursive functions as the notion of calculation.

- 7 October 1936: Post's paper "Finite Combinatory Processes. Formulation I" received; adds instruction "(C) Stop"; [quote: "type 1" process]
- May 1936 – January 1937: Turing, On Computable Numbers With an Application to the Entscheidungsproblem; press May 1936, print January 1937
  - three undecidable problems: "satisfaction", "printing", Entscheidungsproblem
  - differs from Church: computation by machine; "first examples of decision problems proved unsolvable"
- 1939: Rosser, essential equivalence of "effective method" of Gödel, Church, Turing
- 1943: Kleene, [quote: procedure necessarily terminates, 'Yes' or 'No']
- 1952: Kleene, unsolvability of halting problem for Turing machines, machines that "eventually stop" [quote]
- 1952: Davis uses 'halting problem' in lectures at Control Systems Laboratory, University of Illinois; likely first use

## Origin of the halting problem
- many papers/textbooks credit Turing 1936 -> not correct; Turing never used "halt"/"halting" in published works
- search of literature 1936–1958: first published use Rogers (1957); Rogers had draft of Davis (1958); Davis's intro [quote: "some novelty in the arrangement and treatment of topics"] -> term attributed to Davis
- Davis letter: referring to halting problem since 1952
- [quote: Davis's book usage]
- Kleene 1952 as possible precursor, differs only in wording [quote]
- Turing equivalent to Davis's printing problem and Turing's 1936 printing problem; equivalence loose; print-but-not-halt and halt-but-not-print machines; different issues
- Davis modest [quote]
````

</details>

<details><summary><b>Step 4 — rough_draft</b> (991 words)</summary>

````text
In April 1936 Alonzo Church published a proof that a problem in the lambda calculus was undecidable. Turing's proof was published later than that, in January 1937. Since then a lot of other undecidable problems have been described, and one of them is the halting problem, which emerged in the 1950s.

## Timeline

- 1900: David Hilbert poses his "23 questions" at the Second International Congress of Mathematicians in Paris. These are now known as Hilbert's problems. "Of these, the second was that of proving the consistency of the ' Peano axioms ' on which, as he had shown, the rigour of mathematics depended".

- 1920–1921: Emil Post looks at the halting problem for tag systems and he regards it as a candidate for unsolvability. Its unsolvability was not established until much later, and it was Marvin Minsky who did it.

- 1928: Hilbert recasts his 'Second Problem' at the Bologna International Congress. He posed three questions, which were: #1: Was mathematics complete? #2: Was mathematics consistent? #3: Was mathematics decidable? The third question is the one that is known as the Entscheidungsproblem (Decision Problem).

- 1930: Kurt Gödel announces a proof which answers the first two of Hilbert's 1928 questions. "At first he [Hilbert] was only angry and frustrated, but then he began to try to deal constructively with the problem... Gödel himself felt—and expressed the thought in his paper—that his work did not contradict Hilbert's formalistic point of view".

- 1931: Gödel publishes "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I".

- 19 April 1935: Alonzo Church publishes "An Unsolvable Problem of Elementary Number Theory". The paper proposes that the intuitive notion of an effectively calculable function can be formalized by the general recursive functions, or equivalently by the lambda-definable functions. He proves that the halting problem for lambda calculus is not effectively calculable, i.e. whether a given lambda-expression has a normal form.

- 1936: Church publishes the first proof that the Entscheidungsproblem is unsolvable, and he uses a notion of calculation by recursive functions to do it.

- 7 October 1936: Emil Post's paper "Finite Combinatory Processes. Formulation I" is received. Post adds an instruction "(C) Stop" to his "process". He called such a process "type 1... if the process it determines terminates for each specific problem."

- May 1936 – January 1937: Alan Turing's paper On Computable Numbers With an Application to the Entscheidungsproblem goes to press in May 1936 and it reaches print in January 1937. In the paper Turing proves three problems undecidable, which are the "satisfaction" problem, the "printing" problem, and the Entscheidungsproblem. The difference between Turing's proof and Church's proof is that Turing introduces the notion of computation by machine. This is one of the "first examples of decision problems proved unsolvable".

- 1939: J. Barkley Rosser observes that the "effective method" defined by Gödel, Church, and Turing are essentially equivalent.

- 1943: Stephen Kleene states in a paper that "In setting up a complete algorithmic theory, what we do is describe a procedure... which procedure necessarily terminates and in such manner that from the outcome we can read a definite answer, 'Yes' or 'No,' to the question, 'Is the predicate value true?'."

- 1952: Kleene includes a discussion of the unsolvability of the halting problem for Turing machines. He reformulates it in terms of machines that "eventually stop", i.e. halt: "...there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops."

- 1952: Martin Davis uses the term 'halting problem' in a series of lectures at the Control Systems Laboratory at the University of Illinois in 1952. This is likely the first such use of the term.

## Origin of the halting problem

Many papers and textbooks say that the definition and proof of undecidability of the halting problem is in Turing's 1936 paper. But this is not correct. Turing did not use the terms "halt" or "halting" in any of his published works, and this includes his 1936 paper. If you search the academic literature from 1936 to 1958, the first published material that uses the term "halting problem" is Rogers (1957). However, Rogers says that he had a draft of Davis (1958) available to him, and in the introduction Martin Davis states that "the expert will perhaps find some novelty in the arrangement and treatment of topics", so the terminology must be attributed to Davis. Davis stated in a letter that he had been referring to the halting problem since 1952. This is how Davis's book uses it:

> "[...] we wish to determine whether or not [a Turing machine] Z, if placed in a given initial state, will eventually halt. We call this problem the halting problem for Z. [...]

> Theorem 2.2 There exists a Turing machine whose halting problem is recursively unsolvable.

> A related problem is the printing problem for a simple Turing machine Z with respect to a symbol S i ".

Kleene's 1952 statement is a possible precursor to Davis's formulation, and it only differs in wording:

> there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops.

The halting problem is Turing equivalent to Davis's printing problem ("does a Turing machine starting from a given state ever print a given symbol?"), and it is also Turing equivalent to the printing problem in Turing's 1936 paper ("does a Turing machine starting from a blank tape ever print a given symbol?"). But Turing equivalence is rather loose and it does not mean the two problems are the same. Some machines print but do not halt, and some halt but do not print. The printing problem and the halting problem address different issues and they have important conceptual and technical differences. So Davis was just being modest when he said:

> It might also be mentioned that the unsolvability of essentially these problems was first obtained by Turing.
````

</details>

<details><summary><b>Step 5 — draft_citation_needed</b> (1009 words)</summary>

````text
In April 1936 Alonzo Church published a proof that a problem in the lambda calculus was undecidable. Turing's proof was published later than that, in January 1937. Since then a lot of other undecidable problems have been described, and one of them is the halting problem, which emerged in the 1950s.

## Timeline

- 1900: David Hilbert poses his "23 questions" at the Second International Congress of Mathematicians in Paris. These are now known as Hilbert's problems. "Of these, the second was that of proving the consistency of the ' Peano axioms ' on which, as he had shown, the rigour of mathematics depended". [citation needed]

- 1920–1921: Emil Post looks at the halting problem for tag systems and he regards it as a candidate for unsolvability. [citation needed] Its unsolvability was not established until much later, and it was Marvin Minsky who did it.

- 1928: Hilbert recasts his 'Second Problem' at the Bologna International Congress. He posed three questions, which were: #1: Was mathematics complete? #2: Was mathematics consistent? #3: Was mathematics decidable? The third question is the one that is known as the Entscheidungsproblem (Decision Problem).

- 1930: Kurt Gödel announces a proof which answers the first two of Hilbert's 1928 questions. "At first he [Hilbert] was only angry and frustrated, but then he began to try to deal constructively with the problem... Gödel himself felt—and expressed the thought in his paper—that his work did not contradict Hilbert's formalistic point of view".

- 1931: Gödel publishes "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I". [citation needed]

- 19 April 1935: Alonzo Church publishes "An Unsolvable Problem of Elementary Number Theory". The paper proposes that the intuitive notion of an effectively calculable function can be formalized by the general recursive functions, or equivalently by the lambda-definable functions. He proves that the halting problem for lambda calculus is not effectively calculable, i.e. whether a given lambda-expression has a normal form.

- 1936: Church publishes the first proof that the Entscheidungsproblem is unsolvable, and he uses a notion of calculation by recursive functions to do it. [citation needed]

- 7 October 1936: Emil Post's paper "Finite Combinatory Processes. Formulation I" is received. Post adds an instruction "(C) Stop" to his "process". He called such a process "type 1... if the process it determines terminates for each specific problem."

- May 1936 – January 1937: Alan Turing's paper On Computable Numbers With an Application to the Entscheidungsproblem goes to press in May 1936 and it reaches print in January 1937. [citation needed] In the paper Turing proves three problems undecidable, which are the "satisfaction" problem, the "printing" problem, and the Entscheidungsproblem. The difference between Turing's proof and Church's proof is that Turing introduces the notion of computation by machine. This is one of the "first examples of decision problems proved unsolvable".

- 1939: J. Barkley Rosser observes that the "effective method" defined by Gödel, Church, and Turing are essentially equivalent. [citation needed]

- 1943: Stephen Kleene states in a paper that "In setting up a complete algorithmic theory, what we do is describe a procedure... which procedure necessarily terminates and in such manner that from the outcome we can read a definite answer, 'Yes' or 'No,' to the question, 'Is the predicate value true?'."

- 1952: Kleene includes a discussion of the unsolvability of the halting problem for Turing machines. He reformulates it in terms of machines that "eventually stop", i.e. halt: "...there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops."

- 1952: Martin Davis uses the term 'halting problem' in a series of lectures at the Control Systems Laboratory at the University of Illinois in 1952. This is likely the first such use of the term. [citation needed]

## Origin of the halting problem

Many papers and textbooks say that the definition and proof of undecidability of the halting problem is in Turing's 1936 paper. But this is not correct. Turing did not use the terms "halt" or "halting" in any of his published works, and this includes his 1936 paper. [citation needed] If you search the academic literature from 1936 to 1958, the first published material that uses the term "halting problem" is Rogers (1957). However, Rogers says that he had a draft of Davis (1958) available to him, and in the introduction Martin Davis states that "the expert will perhaps find some novelty in the arrangement and treatment of topics", so the terminology must be attributed to Davis. Davis stated in a letter that he had been referring to the halting problem since 1952. [citation needed] This is how Davis's book uses it:

> "[...] we wish to determine whether or not [a Turing machine] Z, if placed in a given initial state, will eventually halt. We call this problem the halting problem for Z. [...]

> Theorem 2.2 There exists a Turing machine whose halting problem is recursively unsolvable.

> A related problem is the printing problem for a simple Turing machine Z with respect to a symbol S i ".

Kleene's 1952 statement is a possible precursor to Davis's formulation, and it only differs in wording:

> there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops.

The halting problem is Turing equivalent to Davis's printing problem ("does a Turing machine starting from a given state ever print a given symbol?"), and it is also Turing equivalent to the printing problem in Turing's 1936 paper ("does a Turing machine starting from a blank tape ever print a given symbol?"). But Turing equivalence is rather loose and it does not mean the two problems are the same. Some machines print but do not halt, and some halt but do not print. The printing problem and the halting problem address different issues and they have important conceptual and technical differences. So Davis was just being modest when he said:

> It might also be mentioned that the unsolvability of essentially these problems was first obtained by Turing.
````

</details>

<details><summary><b>Step 6 — cited_draft</b> (1125 words)</summary>

````text
In April 1936 Alonzo Church published a proof that a problem in the lambda calculus was undecidable. Turing's proof was published later than that, in January 1937. Since then a lot of other undecidable problems have been described, and one of them is the halting problem, which emerged in the 1950s.

## Timeline

- 1900: David Hilbert poses his "23 questions" at the Second International Congress of Mathematicians in Paris. These are now known as Hilbert's problems. "Of these, the second was that of proving the consistency of the ' Peano axioms ' on which, as he had shown, the rigour of mathematics depended". [1]

- 1920–1921: Emil Post looks at the halting problem for tag systems and he regards it as a candidate for unsolvability. [2] Its unsolvability was not established until much later, and it was Marvin Minsky who did it.

- 1928: Hilbert recasts his 'Second Problem' at the Bologna International Congress. He posed three questions, which were: #1: Was mathematics complete? #2: Was mathematics consistent? #3: Was mathematics decidable? The third question is the one that is known as the Entscheidungsproblem (Decision Problem).

- 1930: Kurt Gödel announces a proof which answers the first two of Hilbert's 1928 questions. "At first he [Hilbert] was only angry and frustrated, but then he began to try to deal constructively with the problem... Gödel himself felt—and expressed the thought in his paper—that his work did not contradict Hilbert's formalistic point of view".

- 1931: Gödel publishes "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I". [3]

- 19 April 1935: Alonzo Church publishes "An Unsolvable Problem of Elementary Number Theory". The paper proposes that the intuitive notion of an effectively calculable function can be formalized by the general recursive functions, or equivalently by the lambda-definable functions. He proves that the halting problem for lambda calculus is not effectively calculable, i.e. whether a given lambda-expression has a normal form.

- 1936: Church publishes the first proof that the Entscheidungsproblem is unsolvable, and he uses a notion of calculation by recursive functions to do it. [4]

- 7 October 1936: Emil Post's paper "Finite Combinatory Processes. Formulation I" is received. Post adds an instruction "(C) Stop" to his "process". He called such a process "type 1... if the process it determines terminates for each specific problem."

- May 1936 – January 1937: Alan Turing's paper On Computable Numbers With an Application to the Entscheidungsproblem goes to press in May 1936 and it reaches print in January 1937. [5] In the paper Turing proves three problems undecidable, which are the "satisfaction" problem, the "printing" problem, and the Entscheidungsproblem. The difference between Turing's proof and Church's proof is that Turing introduces the notion of computation by machine. This is one of the "first examples of decision problems proved unsolvable".

- 1939: J. Barkley Rosser observes that the "effective method" defined by Gödel, Church, and Turing are essentially equivalent. [6]

- 1943: Stephen Kleene states in a paper that "In setting up a complete algorithmic theory, what we do is describe a procedure... which procedure necessarily terminates and in such manner that from the outcome we can read a definite answer, 'Yes' or 'No,' to the question, 'Is the predicate value true?'."

- 1952: Kleene includes a discussion of the unsolvability of the halting problem for Turing machines. He reformulates it in terms of machines that "eventually stop", i.e. halt: "...there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops."

- 1952: Martin Davis uses the term 'halting problem' in a series of lectures at the Control Systems Laboratory at the University of Illinois in 1952. This is likely the first such use of the term. [7]

## Origin of the halting problem

Many papers and textbooks say that the definition and proof of undecidability of the halting problem is in Turing's 1936 paper. But this is not correct. Turing did not use the terms "halt" or "halting" in any of his published works, and this includes his 1936 paper. [8] If you search the academic literature from 1936 to 1958, the first published material that uses the term "halting problem" is Rogers (1957). However, Rogers says that he had a draft of Davis (1958) available to him, and in the introduction Martin Davis states that "the expert will perhaps find some novelty in the arrangement and treatment of topics", so the terminology must be attributed to Davis. Davis stated in a letter that he had been referring to the halting problem since 1952. [7] This is how Davis's book uses it:

> "[...] we wish to determine whether or not [a Turing machine] Z, if placed in a given initial state, will eventually halt. We call this problem the halting problem for Z. [...]

> Theorem 2.2 There exists a Turing machine whose halting problem is recursively unsolvable.

> A related problem is the printing problem for a simple Turing machine Z with respect to a symbol S i ".

Kleene's 1952 statement is a possible precursor to Davis's formulation, and it only differs in wording:

> there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops.

The halting problem is Turing equivalent to Davis's printing problem ("does a Turing machine starting from a given state ever print a given symbol?"), and it is also Turing equivalent to the printing problem in Turing's 1936 paper ("does a Turing machine starting from a blank tape ever print a given symbol?"). But Turing equivalence is rather loose and it does not mean the two problems are the same. Some machines print but do not halt, and some halt but do not print. The printing problem and the halting problem address different issues and they have important conceptual and technical differences. So Davis was just being modest when he said:

> It might also be mentioned that the unsolvability of essentially these problems was first obtained by Turing.

References:
[1] Hodges 1983, p. 83; Davis' commentary in Davis 1965, p. 108
[2] Absolutely unsolvable problems and relatively undecidable propositions – account of an anticipation, reprinted in Davis 1965, pp. 340–433
[3] reprinted in Davis 1965, p. 5ff
[4] A Note on the Entscheidungsproblem, reprinted in Davis 1965, p. 110
[5] reprinted in Davis 1965, p. 115
[6] Rosser, "Informal Exposition of Proofs of Gödel's Theorem and Church's Theorem", reprinted in Davis 1965, p. 223
[7] letter from Davis to Copeland, 12 December 2001, Footnote 61 in Copeland 2004, p. 40
[8] Textual search of Turing's collected works: Good (1992), Gandy & Yates (2001), Ince (1992), Saunders (1992). Similarly Hodges (1983) does not have the word "halting" or words "halting problem" in his index.
````

</details>

<details><summary><b>Step 7 — revised_draft</b> (1081 words)</summary>

````text
In April 1936, Alonzo Church published his proof of the undecidability of a problem in the lambda calculus. Turing's proof was published later, in January 1937. Since then, many other undecidable problems have been described, among them the halting problem, which emerged in the 1950s.

## Timeline

- 1900: David Hilbert poses his "23 questions" (now known as Hilbert's problems) at the Second International Congress of Mathematicians in Paris. "Of these, the second was that of proving the consistency of the ' Peano axioms ' on which, as he had shown, the rigour of mathematics depended". [1]

- 1920–1921: Emil Post explores the halting problem for tag systems, regarding it as a candidate for unsolvability. [2] Its unsolvability was only established much later, by Marvin Minsky.

- 1928: Hilbert recasts his 'Second Problem' at the Bologna International Congress. He posed three questions: #1: Was mathematics complete? #2: Was mathematics consistent? #3: Was mathematics decidable? The third question is known as the Entscheidungsproblem (Decision Problem).

- 1930: Kurt Gödel announces a proof as an answer to the first two of Hilbert's 1928 questions. "At first he [Hilbert] was only angry and frustrated, but then he began to try to deal constructively with the problem... Gödel himself felt—and expressed the thought in his paper—that his work did not contradict Hilbert's formalistic point of view".

- 1931: Gödel publishes "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I". [3]

- 19 April 1935: Alonzo Church publishes "An Unsolvable Problem of Elementary Number Theory", which proposes that the intuitive notion of an effectively calculable function can be formalized by the general recursive functions or equivalently by the lambda-definable functions. He proves that the halting problem for lambda calculus (i.e., whether a given lambda-expression has a normal form) is not effectively calculable.

- 1936: Church publishes the first proof that the Entscheidungsproblem is unsolvable, using a notion of calculation by recursive functions. [4]

- 7 October 1936: Emil Post's paper "Finite Combinatory Processes. Formulation I" is received. Post adds to his "process" an instruction "(C) Stop". He called such a process "type 1... if the process it determines terminates for each specific problem."

- May 1936 – January 1937: Alan Turing's paper On Computable Numbers With an Application to the Entscheidungsproblem goes to press in May 1936 and reaches print in January 1937. [5] Turing proves three problems undecidable: the "satisfaction" problem, the "printing" problem, and the Entscheidungsproblem. Turing's proof differs from Church's in that it introduces the notion of computation by machine. This is one of the "first examples of decision problems proved unsolvable".

- 1939: J. Barkley Rosser observes the essential equivalence of the "effective method" defined by Gödel, Church, and Turing. [6]

- 1943: In a paper, Stephen Kleene states that "In setting up a complete algorithmic theory, what we do is describe a procedure... which procedure necessarily terminates and in such manner that from the outcome we can read a definite answer, 'Yes' or 'No,' to the question, 'Is the predicate value true?'."

- 1952: Kleene includes a discussion of the unsolvability of the halting problem for Turing machines and reformulates it in terms of machines that "eventually stop", i.e. halt: "...there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops."

- 1952: Martin Davis uses the term 'halting problem' in a series of lectures at the Control Systems Laboratory at the University of Illinois in 1952. This is likely the first such use of the term. [7]

## Origin of the halting problem

Many papers and textbooks attribute the definition and proof of undecidability of the halting problem to Turing's 1936 paper. This, however, is not correct. Turing did not use the terms "halt" or "halting" in any of his published works, including his 1936 paper. [8] A search of the academic literature from 1936 to 1958 shows that the first published material using the term "halting problem" was Rogers (1957). However, Rogers says he had a draft of Davis (1958) available to him, and Martin Davis states in the introduction that "the expert will perhaps find some novelty in the arrangement and treatment of topics", so the terminology must be attributed to Davis. Davis stated in a letter that he had been referring to the halting problem since 1952. [7] Davis's book uses the term as follows:

> "[...] we wish to determine whether or not [a Turing machine] Z, if placed in a given initial state, will eventually halt. We call this problem the halting problem for Z. [...]

> Theorem 2.2 There exists a Turing machine whose halting problem is recursively unsolvable.

> A related problem is the printing problem for a simple Turing machine Z with respect to a symbol S i ".

A possible precursor to Davis's formulation is Kleene's 1952 statement, which differs only in wording:

> there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops.

The halting problem is Turing equivalent both to Davis's printing problem ("does a Turing machine starting from a given state ever print a given symbol?") and to the printing problem considered in Turing's 1936 paper ("does a Turing machine starting from a blank tape ever print a given symbol?"). However, Turing equivalence is rather loose and does not mean that the two problems are the same: there are machines which print but do not halt, and machines which halt but do not print. The printing and halting problems address different issues and exhibit important conceptual and technical differences. Davis was thus simply being modest when he said:

> It might also be mentioned that the unsolvability of essentially these problems was first obtained by Turing.

References:
[1] Hodges 1983, p. 83; Davis' commentary in Davis 1965, p. 108
[2] Absolutely unsolvable problems and relatively undecidable propositions – account of an anticipation, reprinted in Davis 1965, pp. 340–433
[3] reprinted in Davis 1965, p. 5ff
[4] A Note on the Entscheidungsproblem, reprinted in Davis 1965, p. 110
[5] reprinted in Davis 1965, p. 115
[6] Rosser, "Informal Exposition of Proofs of Gödel's Theorem and Church's Theorem", reprinted in Davis 1965, p. 223
[7] letter from Davis to Copeland, 12 December 2001, Footnote 61 in Copeland 2004, p. 40
[8] Textual search of Turing's collected works: Good (1992), Gandy & Yates (2001), Ince (1992), Saunders (1992). Similarly Hodges (1983) does not have the word "halting" or words "halting problem" in his index.
````

</details>

<details><summary><b>Step 8 — final</b> (1101 words)</summary>

````text
In April 1936, Alonzo Church published his proof of the undecidability of a problem in the lambda calculus. Turing's proof was published later, in January 1937. Since then, many other undecidable problems have been described, including the halting problem which emerged in the 1950s.

## Timeline

- 1900 (1900): David Hilbert poses his "23 questions" (now known as Hilbert's problems) at the Second International Congress of Mathematicians in Paris. "Of these, the second was that of proving the consistency of the ' Peano axioms ' on which, as he had shown, the rigour of mathematics depended". [1]

- 1920 (1920) –1921 (1921): Emil Post explores the halting problem for tag systems, regarding it as a candidate for unsolvability. [2] Its unsolvability was not established until much later, by Marvin Minsky.

- 1928 (1928): Hilbert recasts his 'Second Problem' at the Bologna International Congress. He posed three questions: i.e. #1: Was mathematics complete ? #2: Was mathematics consistent ? #3: Was mathematics decidable ? The third question is known as the Entscheidungsproblem (Decision Problem).

- 1930 (1930): Kurt Gödel announces a proof as an answer to the first two of Hilbert's 1928 questions. "At first he [Hilbert] was only angry and frustrated, but then he began to try to deal constructively with the problem... Gödel himself felt—and expressed the thought in his paper—that his work did not contradict Hilbert's formalistic point of view".

- 1931 (1931): Gödel publishes "On Formally Undecidable Propositions of Principia Mathematica and Related Systems I". [3]

- 19 April 1935 (1935-04-19): Alonzo Church publishes "An Unsolvable Problem of Elementary Number Theory", which proposes that the intuitive notion of an effectively calculable function can be formalized by the general recursive functions or equivalently by the lambda-definable functions. He proves that the halting problem for lambda calculus (i.e., whether a given lambda-expression has a normal form) is not effectively calculable.

- 1936 (1936): Church publishes the first proof that the Entscheidungsproblem is unsolvable, using a notion of calculation by recursive functions. [4]

- 7 October 1936 (1936-10-07): Emil Post 's paper "Finite Combinatory Processes. Formulation I" is received. Post adds to his "process" an instruction "(C) Stop". He called such a process "type 1... if the process it determines terminates for each specific problem."

- May 1936 (1936-05) – January 1937 (1937-01): Alan Turing 's paper On Computable Numbers With an Application to the Entscheidungsproblem goes to press in May 1936 and reaches print in January 1937. [5] Turing proves three problems undecidable: the "satisfaction" problem, the "printing" problem, and the Entscheidungsproblem. Turing's proof differs from Church's by introducing the notion of computation by machine. This is one of the "first examples of decision problems proved unsolvable".

- 1939 (1939): J. Barkley Rosser observes the essential equivalence of "effective method" defined by Gödel, Church, and Turing. [6]

- 1943 (1943): In a paper, Stephen Kleene states that "In setting up a complete algorithmic theory, what we do is describe a procedure... which procedure necessarily terminates and in such manner that from the outcome we can read a definite answer, 'Yes' or 'No,' to the question, 'Is the predicate value true?'."

- 1952 (1952): Kleene includes a discussion of the unsolvability of the halting problem for Turing machines and reformulates it in terms of machines that "eventually stop", i.e. halt: "...there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops."

- 1952 (1952): Martin Davis uses the term 'halting problem' in a series of lectures at the Control Systems Laboratory at the University of Illinois in 1952. It is likely that this is the first such use of the term. [7]

## Origin of the halting problem

Many papers and textbooks refer the definition and proof of undecidability of the halting problem to Turing's 1936 paper. However, this is not correct. Turing did not use the terms "halt" or "halting" in any of his published works, including his 1936 paper. [8] A search of the academic literature from 1936 to 1958 showed that the first published material using the term "halting problem" was Rogers (1957). However, Rogers says he had a draft of Davis (1958) available to him, and Martin Davis states in the introduction that "the expert will perhaps find some novelty in the arrangement and treatment of topics", so the terminology must be attributed to Davis. Davis stated in a letter that he had been referring to the halting problem since 1952. [7] The usage in Davis's book is as follows:

> "[...] we wish to determine whether or not [a Turing machine] Z, if placed in a given initial state, will eventually halt. We call this problem the halting problem for Z. [...]

> Theorem 2.2 There exists a Turing machine whose halting problem is recursively unsolvable.

> A related problem is the printing problem for a simple Turing machine Z with respect to a symbol S i ".

A possible precursor to Davis's formulation is Kleene's 1952 statement, which differs only in wording:

> there is no algorithm for deciding whether any given machine, when started from any given situation, eventually stops.

The halting problem is Turing equivalent to both Davis's printing problem ("does a Turing machine starting from a given state ever print a given symbol?") and to the printing problem considered in Turing's 1936 paper ("does a Turing machine starting from a blank tape ever print a given symbol?"). However, Turing equivalence is rather loose and does not mean that the two problems are the same. There are machines which print but do not halt, and halt but not print. The printing and halting problems address different issues and exhibit important conceptual and technical differences. Thus, Davis was simply being modest when he said:

> It might also be mentioned that the unsolvability of essentially these problems was first obtained by Turing.

References:
[1] Hodges 1983, p. 83; Davis' commentary in Davis 1965, p. 108
[2] Absolutely unsolvable problems and relatively undecidable propositions – account of an anticipation, reprinted in Davis 1965, pp. 340–433
[3] reprinted in Davis 1965, p. 5ff
[4] A Note on the Entscheidungsproblem, reprinted in Davis 1965, p. 110
[5] reprinted in Davis 1965, p. 115
[6] Rosser, "Informal Exposition of Proofs of Gödel's Theorem and Church's Theorem", reprinted in Davis 1965, p. 223
[7] letter from Davis to Copeland, 12 December 2001, Footnote 61 in Copeland 2004, p. 40
[8] Textual search of Turing's collected works: Good (1992), Gandy & Yates (2001), Ince (1992), Saunders (1992). Similarly Hodges (1983) does not have the word "halting" or words "halting problem" in his index.
````

</details>
