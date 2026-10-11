# 6. Turing machine — History

`A-wiki_Turing_machine` · [A_reconstructed_9step](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Turing_machine&oldid=1373616450> · License: https://creativecommons.org/licenses/by-sa/4.0/

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | prompt | 41 | 0 | 0.01 | reconstructed |
| 1 | skeleton_outline | 43 | 0 | 0.03 | reconstructed |
| 2 | detailed_outline | 894 | 0 | 0.37 | reconstructed |
| 3 | partial_draft | 1309 | 0 | 0.61 | reconstructed |
| 4 | rough_draft | 1952 | 0 | 0.88 | reconstructed |
| 5 | draft_citation_needed | 1960 | 0 | 0.87 | reconstructed |
| 6 | cited_draft | 2027 | 4 | 0.90 | reconstructed |
| 7 | revised_draft | 1982 | 4 | 0.98 | reconstructed |
| 8 | final | 1984 | 4 | 1.00 | source |

<details><summary><b>Step 0 — prompt</b> (41 words)</summary>

````text
Write the History section of the Wikipedia article on the Turing machine: the background in earlier calculating machines and Hilbert's decision problem, how Turing came to his machine, and what happened to the idea afterwards in computer science and complexity theory.
````

</details>

<details><summary><b>Step 1 — skeleton_outline</b> (43 words)</summary>

````text
## Historical background: computational machinery (Babbage, Gandy)
## The Entscheidungsproblem: Hilbert's tenth question and the race to answer it
## Alan Turing's a-machine
## 1937–1970: digital computers and the birth of computer science
## 1970–present: the Turing machine as a model of computation
````

</details>

<details><summary><b>Step 2 — detailed_outline</b> (894 words)</summary>

````text
## Historical background: computational machinery
- Robin Gandy (1919–1995): student of Alan Turing (1912–1954), lifelong friend
- Gandy traces "calculating machine" back to Charles Babbage (circa 1834); proposes "Babbage's Thesis"
  - [quote: Babbage's Thesis, italics in Babbage as cited by Gandy]
- Gandy's analysis of the analytical engine: five operations (cf. p. 52–53)
  - arithmetic +, −, × ("proper" subtraction: x − y = 0 if y ≥ x)
  - any sequence of operations is an operation
  - iteration (repeat operation P n times)
  - conditional iteration (repeat P n times, conditional on "success" of test T)
  - conditional transfer (conditional "goto")
- Gandy: functions calculable by (1), (2), (4) = exactly the Turing computable ones
- other "universal calculating machines": Percy Ludgate (1909), Leonardo Torres Quevedo (1914), Maurice d'Ocagne (1922), Louis Couffignal (1933), Vannevar Bush (1936), Howard Aiken (1937)
  - [quote: Gandy — emphasis on fixed arithmetic sequences; conditional iteration/transfer not recognized]

## The Entscheidungsproblem (the "decision problem"): Hilbert's tenth question of 1900
- David Hilbert's problems, 1900; an aspect of #10 floating about for almost 30 years before framed precisely
  - [quote: Hilbert's original No. 10 + the Entscheidungsproblem; translation in Dershowitz and Gurevich, 2008]
- 1922: H. Behmann on the "most general form" of the Entscheidungsproblem
  - [quotes via Gandy: definite prescription, finite steps; equivalent to deciding which propositions are true; would give a procedure for solving many/all problems]
- 1928 international congress of mathematicians: Hilbert's questions made precise — complete? consistent? decidable?
  - first two answered 1930 by Kurt Gödel, at the same meeting as Hilbert's retirement speech (chagrin)
  - third (Entscheidungsproblem) waits until mid-1930s
- needs precise definition of "definite general applicable prescription" (Church: "effective calculability"); none in 1928
- next 6–7 years:
  - Emil Post: worker moving room to room, writing/erasing marks per list of instructions
  - Church + students Stephen Kleene, J. B. Rosser: lambda-calculus, Gödel's recursion theory (1934)
- Church's paper (15 April 1936): Entscheidungsproblem "undecidable"; beat Turing by almost a year (Turing submitted 28 May 1936, published January 1937)
- Post: brief paper, fall 1936 -> Turing has priority over Post
- Church referees Turing's paper; Turing studies Church's, adds Appendix sketching proof that lambda-calculus and his machines compute same functions
  - [quote: Hodges — Church's result weaker; Turing's more direct, from first principles]
- Post only proposed a definition, criticised Church's, proved nothing

## Alan Turing's a-machine
- spring 1935: Turing, young Master's student, King's College, Cambridge, takes on the challenge
- stimulated by lectures of logician M. H. A. Newman (Gödel's work, Entscheidungsproblem, "mechanical")
  - [quote: Newman's 1955 obituary of Turing, via Gandy — "Something that can be done by a machine"]
  - [quote: Gandy — undecidability as goal from the start? 'main idea' in Grantchester meadows, summer 1935]
- Gandy: Newman's statement "misleading"; not shared by all
- lifelong interest in machines: typewriters as a boy, Mrs. Turing's typewriter, "mechanical" (Hodges p. 96)
- at Princeton (PhD): Boolean-logic multiplier (see below)
- PhD thesis "Systems of Logic Based on Ordinals": definition of "a computable function"
  - [quote: Turing (1939, p. 166) — purely mechanical process; three definitions equivalent]
- 1936: invents "a-machine" (automatic machine)
- paper submitted 31 May 1936 to London Mathematical Society (Proceedings); published early 1937; offprints February 1937
- term "Turing machine" coined later by Church (doctoral advisor) in a review
- two questions answered in the negative:
  - machine deciding whether any arbitrary machine on its tape is "circular" (freezes / fails to continue)?
  - machine deciding whether any arbitrary machine on its tape ever prints a given symbol?
- simple device, arbitrary computations -> properties of computation in general; uncomputability of Entscheidungsproblem
- back in UK: jointly responsible for breaking German "Enigma" codes; ACE (Automatic Computing Engine)
  - Hodges p. 318: ACE roots in his own universal machine, not EDVAC
- Kleene (1952) names "Turing's Thesis"; arguments continue on origin and nature
- what Turing did prove: "On Computable Numbers, with an Application to the Entscheidungsproblem" (1937)
  - [quote: Turing — no general process for whether formula U of functional calculus K is provable; The Undecidable, p. 145]
- second proof: "Does this machine ever print 0" is "undecidable"

## 1937–1970: The "digital computer", the birth of "computer science"
- 1937, Princeton: digital (Boolean-logic) multiplier from scratch, own electromechanical relays (Hodges p. 138)
  - Hodges p. 138: logical design of a Turing machine in relay-operated switches
- earnest work elsewhere: Konrad Zuse (1938), Germany; Howard Aiken, George Stibitz (1937), US; used by Axis and Allied militaries in WWII (Hodges p. 298–299)
- early–mid 1950s: Hao Wang, Marvin Minsky reduce TM to simpler form (precursor of Martin Davis's Post–Turing machine); Europeans reduce electronic computer to theoretical object equivalent to TM
- late 1950s/early 1960s: Melzak and Lambek (1961), Minsky (1961), Shepherdson and Sturgis (1961) -> counter machine
- Elgot and Robinson (1964), Hartmanis (1971), Cook and Reckhow (1973) -> register machine, random-access machine
- all basically multi-tape TMs with arithmetic-like instruction set

## 1970–present: as a model of computation
- counter, register, random-access machines + their sire the TM: models of choice in theory of computation
- computational complexity theory uses the TM
  - [quote: Van Emde Boas (1990) — off-line multitape TM and RAM (Cook and Reckhow) dominant in machine-based complexity theory]
  - [quote: Van Emde Boas (1990) — RAM takes the role in analysis of algorithms]
````

</details>

<details><summary><b>Step 3 — partial_draft</b> (1309 words)</summary>

````text
## Historical background: computational machinery

Robin Gandy (1919–1995) was a student of Alan Turing (1912–1954), and also his lifelong friend. Gandy traces the idea of a "calculating machine" back to Charles Babbage (circa 1834), and he actually proposes something he calls "Babbage's Thesis":

> That the whole of development and operations of analysis are now capable of being executed by machinery.

— (italics in Babbage as cited by Gandy)

Gandy analyses Babbage's analytical engine and describes the following five operations that it has (cf. p. 52–53):

- The arithmetic functions +, −, ×, where − is "proper" subtraction: x − y = 0 if y ≥ x.
- Any sequence of operations is an operation.
- Iteration of an operation (repeating an operation P n times).
- Conditional iteration (repeating an operation P n times, conditional on the "success" of test T).
- Conditional transfer (i.e., a conditional "goto").

According to Gandy, "the functions which can be calculated by (1), (2), and (4) are precisely those which are Turing computable." He also cites other proposals for "universal calculating machines", which include the ones by Percy Ludgate (1909), Leonardo Torres Quevedo (1914), Maurice d'Ocagne (1922), Louis Couffignal (1933), Vannevar Bush (1936) and Howard Aiken (1937). But about these he says:

> … the emphasis is on programming a fixed iterable sequence of arithmetical operations. The fundamental importance of conditional iteration and conditional transfer for a general theory of calculating machines is not recognized…

— Gandy

## The Entscheidungsproblem (the "decision problem"): Hilbert's tenth question of 1900

The famous mathematician David Hilbert posed his problems in 1900, and one aspect of problem #10 had been floating around for almost 30 years before it got framed precisely. This is Hilbert's original expression for No. 10:

> 10. Determination of the solvability of a Diophantine equation. Given a Diophantine equation with any number of unknown quantities and with rational integral coefficients: To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers. The Entscheidungsproblem [decision problem for first-order logic ] is solved when we know a procedure that allows for any given logical expression to decide by finitely many operations its validity or satisfiability... The Entscheidungsproblem must be considered the main problem of mathematical logic.

— quoted, with this translation and the original German, in Dershowitz and Gurevich, 2008

By 1922 this notion of "Entscheidungsproblem" had developed a bit, and H. Behmann stated that

> ... most general form of the Entscheidungsproblem [is] as follows:

> A quite definite generally applicable prescription is required which will allow one to decide in a finite number of steps the truth or falsity of a given purely logical assertion...

— Gandy quoting Behmann

> Behmann remarks that... the general problem is equivalent to the problem of deciding which mathematical propositions are true.

— ibid.

> If one were able to solve the Entscheidungsproblem then one would have a "procedure for solving many (or even all) mathematical problems".

— ibid.

At the 1928 international congress of mathematicians, Hilbert "made his questions quite precise. First, was mathematics complete... Second, was mathematics consistent... And thirdly, was mathematics decidable ?" Kurt Gödel answered the first two questions in 1930, at the very same meeting where Hilbert gave his retirement speech (much to the chagrin of Hilbert). The third one, the Entscheidungsproblem, had to wait until the mid-1930s.

The problem was that to answer it you first needed a precise definition of "definite general applicable prescription", which the Princeton professor Alonzo Church would come to call "effective calculability", and in 1928 there was no such definition. Over the next 6–7 years Emil Post developed his definition, which was a worker moving from room to room writing and erasing marks per a list of instructions. Church and his two students Stephen Kleene and J. B. Rosser also developed one, by using Church's lambda-calculus and Gödel's recursion theory (1934). Church's paper was published 15 April 1936 and it showed that the Entscheidungsproblem was indeed "undecidable", and it beat Turing to the punch by almost a year (Turing's paper was submitted 28 May 1936 and published January 1937). Meanwhile Emil Post submitted a brief paper in the fall of 1936, so Turing at least had priority over Post. Church refereed Turing's paper, and while he did, Turing had time to study Church's paper and add an Appendix where he sketched a proof that Church's lambda-calculus and his own machines would compute the same functions.

> But what Church had done was something rather different, and in a certain sense weaker.... the Turing construction was more direct, and provided an argument from first principles, closing the gap in Church's demonstration.

— Hodges

Post had only proposed a definition of calculability and criticised Church's "definition", but he had not proved anything.

## Alan Turing's a-machine
- spring 1935: Turing, young Master's student, King's College, Cambridge, takes on the challenge
- stimulated by lectures of logician M. H. A. Newman (Gödel's work, Entscheidungsproblem, "mechanical")
  - [quote: Newman's 1955 obituary of Turing, via Gandy — "Something that can be done by a machine"]
  - [quote: Gandy — undecidability as goal from the start? 'main idea' in Grantchester meadows, summer 1935]
- Gandy: Newman's statement "misleading"; not shared by all
- lifelong interest in machines: typewriters as a boy, Mrs. Turing's typewriter, "mechanical" (Hodges p. 96)
- at Princeton (PhD): Boolean-logic multiplier (see below)
- PhD thesis "Systems of Logic Based on Ordinals": definition of "a computable function"
  - [quote: Turing (1939, p. 166) — purely mechanical process; three definitions equivalent]
- 1936: invents "a-machine" (automatic machine)
- paper submitted 31 May 1936 to London Mathematical Society (Proceedings); published early 1937; offprints February 1937
- term "Turing machine" coined later by Church (doctoral advisor) in a review
- two questions answered in the negative:
  - machine deciding whether any arbitrary machine on its tape is "circular" (freezes / fails to continue)?
  - machine deciding whether any arbitrary machine on its tape ever prints a given symbol?
- simple device, arbitrary computations -> properties of computation in general; uncomputability of Entscheidungsproblem
- back in UK: jointly responsible for breaking German "Enigma" codes; ACE (Automatic Computing Engine)
  - Hodges p. 318: ACE roots in his own universal machine, not EDVAC
- Kleene (1952) names "Turing's Thesis"; arguments continue on origin and nature
- what Turing did prove: "On Computable Numbers, with an Application to the Entscheidungsproblem" (1937)
  - [quote: Turing — no general process for whether formula U of functional calculus K is provable; The Undecidable, p. 145]
- second proof: "Does this machine ever print 0" is "undecidable"

## 1937–1970: The "digital computer", the birth of "computer science"
- 1937, Princeton: digital (Boolean-logic) multiplier from scratch, own electromechanical relays (Hodges p. 138)
  - Hodges p. 138: logical design of a Turing machine in relay-operated switches
- earnest work elsewhere: Konrad Zuse (1938), Germany; Howard Aiken, George Stibitz (1937), US; used by Axis and Allied militaries in WWII (Hodges p. 298–299)
- early–mid 1950s: Hao Wang, Marvin Minsky reduce TM to simpler form (precursor of Martin Davis's Post–Turing machine); Europeans reduce electronic computer to theoretical object equivalent to TM
- late 1950s/early 1960s: Melzak and Lambek (1961), Minsky (1961), Shepherdson and Sturgis (1961) -> counter machine
- Elgot and Robinson (1964), Hartmanis (1971), Cook and Reckhow (1973) -> register machine, random-access machine
- all basically multi-tape TMs with arithmetic-like instruction set

## 1970–present: as a model of computation
- counter, register, random-access machines + their sire the TM: models of choice in theory of computation
- computational complexity theory uses the TM
  - [quote: Van Emde Boas (1990) — off-line multitape TM and RAM (Cook and Reckhow) dominant in machine-based complexity theory]
  - [quote: Van Emde Boas (1990) — RAM takes the role in analysis of algorithms]
````

</details>

<details><summary><b>Step 4 — rough_draft</b> (1952 words)</summary>

````text
## Historical background: computational machinery

Robin Gandy (1919–1995) was a student of Alan Turing (1912–1954), and also his lifelong friend. Gandy traces the idea of a "calculating machine" back to Charles Babbage (circa 1834), and he actually proposes something he calls "Babbage's Thesis":

> That the whole of development and operations of analysis are now capable of being executed by machinery.

— (italics in Babbage as cited by Gandy)

Gandy analyses Babbage's analytical engine and describes the following five operations that it has (cf. p. 52–53):

- The arithmetic functions +, −, ×, where − is "proper" subtraction: x − y = 0 if y ≥ x.
- Any sequence of operations is an operation.
- Iteration of an operation (repeating an operation P n times).
- Conditional iteration (repeating an operation P n times, conditional on the "success" of test T).
- Conditional transfer (i.e., a conditional "goto").

According to Gandy, "the functions which can be calculated by (1), (2), and (4) are precisely those which are Turing computable." He also cites other proposals for "universal calculating machines", which include the ones by Percy Ludgate (1909), Leonardo Torres Quevedo (1914), Maurice d'Ocagne (1922), Louis Couffignal (1933), Vannevar Bush (1936) and Howard Aiken (1937). But about these he says:

> … the emphasis is on programming a fixed iterable sequence of arithmetical operations. The fundamental importance of conditional iteration and conditional transfer for a general theory of calculating machines is not recognized…

— Gandy

## The Entscheidungsproblem (the "decision problem"): Hilbert's tenth question of 1900

The famous mathematician David Hilbert posed his problems in 1900, and one aspect of problem #10 had been floating around for almost 30 years before it got framed precisely. This is Hilbert's original expression for No. 10:

> 10. Determination of the solvability of a Diophantine equation. Given a Diophantine equation with any number of unknown quantities and with rational integral coefficients: To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers. The Entscheidungsproblem [decision problem for first-order logic ] is solved when we know a procedure that allows for any given logical expression to decide by finitely many operations its validity or satisfiability... The Entscheidungsproblem must be considered the main problem of mathematical logic.

— quoted, with this translation and the original German, in Dershowitz and Gurevich, 2008

By 1922 this notion of "Entscheidungsproblem" had developed a bit, and H. Behmann stated that

> ... most general form of the Entscheidungsproblem [is] as follows:

> A quite definite generally applicable prescription is required which will allow one to decide in a finite number of steps the truth or falsity of a given purely logical assertion...

— Gandy quoting Behmann

> Behmann remarks that... the general problem is equivalent to the problem of deciding which mathematical propositions are true.

— ibid.

> If one were able to solve the Entscheidungsproblem then one would have a "procedure for solving many (or even all) mathematical problems".

— ibid.

At the 1928 international congress of mathematicians, Hilbert "made his questions quite precise. First, was mathematics complete... Second, was mathematics consistent... And thirdly, was mathematics decidable ?" Kurt Gödel answered the first two questions in 1930, at the very same meeting where Hilbert gave his retirement speech (much to the chagrin of Hilbert). The third one, the Entscheidungsproblem, had to wait until the mid-1930s.

The problem was that to answer it you first needed a precise definition of "definite general applicable prescription", which the Princeton professor Alonzo Church would come to call "effective calculability", and in 1928 there was no such definition. Over the next 6–7 years Emil Post developed his definition, which was a worker moving from room to room writing and erasing marks per a list of instructions. Church and his two students Stephen Kleene and J. B. Rosser also developed one, by using Church's lambda-calculus and Gödel's recursion theory (1934). Church's paper was published 15 April 1936 and it showed that the Entscheidungsproblem was indeed "undecidable", and it beat Turing to the punch by almost a year (Turing's paper was submitted 28 May 1936 and published January 1937). Meanwhile Emil Post submitted a brief paper in the fall of 1936, so Turing at least had priority over Post. Church refereed Turing's paper, and while he did, Turing had time to study Church's paper and add an Appendix where he sketched a proof that Church's lambda-calculus and his own machines would compute the same functions.

> But what Church had done was something rather different, and in a certain sense weaker.... the Turing construction was more direct, and provided an argument from first principles, closing the gap in Church's demonstration.

— Hodges

Post had only proposed a definition of calculability and criticised Church's "definition", but he had not proved anything.

## Alan Turing's a-machine

In the spring of 1935 Turing, who was then a young Master's student at King's College, Cambridge, took on the challenge. He had been stimulated by the lectures of the logician M. H. A. Newman "and learned from them of Gödel's work and the Entscheidungsproblem... Newman used the word 'mechanical'...". In his obituary of Turing 1955 Newman writes:

> To the question 'what is a "mechanical" process?' Turing returned the characteristic answer 'Something that can be done by a machine' and he embarked on the highly congenial task of analysing the general notion of a computing machine.

— Gandy

Gandy also states that:

> I suppose, but do not know, that Turing, right from the start of his work, had as his goal a proof of the undecidability of the Entscheidungsproblem. He told me that the 'main idea' of the paper came to him when he was lying in Grantchester meadows in the summer of 1935. The 'main idea' might have either been his analysis of computation or his realization that there was a universal machine, and so a diagonal argument to prove unsolvability.

— ibid.

Gandy believed that Newman's statement above is "misleading", but not everyone shares this opinion. Turing had a lifelong interest in machines: "Alan had dreamt of inventing typewriters as a boy; [his mother] Mrs. Turing had a typewriter; and he could well have begun by asking himself what was meant by calling a typewriter 'mechanical'" (Hodges p. 96). When he was at Princeton doing his PhD, Turing built a Boolean-logic multiplier (see below). His PhD thesis is titled "Systems of Logic Based on Ordinals", and it contains this definition of "a computable function":

> It was stated above that 'a function is effectively calculable if its values can be found by some purely mechanical process'. We may take this statement literally, understanding by a purely mechanical process one which could be carried out by a machine. It is possible to give a mathematical description, in a certain normal form, of the structures of these machines. The development of these ideas leads to the author's definition of a computable function, and to an identification of computability with effective calculability. It is not difficult, though somewhat laborious, to prove that these three definitions [the 3rd is the λ-calculus] are equivalent.

— Turing (1939, p. 166)

Turing invented the "a-machine" (automatic machine) in 1936. He submitted his paper to the London Mathematical Society for its Proceedings on 31 May 1936, but it was published in early 1937, and offprints were available in February 1937. The term "Turing machine" was coined later by Turing's doctoral advisor, Alonzo Church, in a review. Using this model Turing could answer two questions in the negative:

- Does a machine exist that can determine whether any arbitrary machine on its tape is "circular" (e.g., freezes, or fails to continue its computational task)?
- Does a machine exist that can determine whether any arbitrary machine on its tape ever prints a given symbol?

So by giving a mathematical description of a very simple device that can do arbitrary computations, he was able to prove properties of computation in general, and in particular the uncomputability of the Entscheidungsproblem ('decision problem').

After Turing returned to the UK he ultimately became jointly responsible for breaking the German secret codes that were created by encryption machines called "The Enigma". He also got involved in the design of the ACE (Automatic Computing Engine): "[Turing's] ACE proposal was effectively self-contained, and its roots lay not in the EDVAC [the USA's initiative], but in his own universal machine" (Hodges p. 318). There are still arguments about the origin and nature of what Kleene (1952) named Turing's Thesis. But what Turing did prove with his computational-machine model is in his paper "On Computable Numbers, with an Application to the Entscheidungsproblem" (1937):

> [that] the Hilbert Entscheidungsproblem can have no solution... I propose, therefore to show that there can be no general process for determining whether a given formula U of the functional calculus K is provable, i.e. that there can be no machine which, supplied with any one U of these formulae, will eventually say whether U is provable.

— from Turing's paper as reprinted in The Undecidable, p. 145

Turing's example (his second proof) is this: if one asks for a general procedure to tell us "Does this machine ever print 0", the question is "undecidable".

## 1937–1970: The "digital computer", the birth of "computer science"

In 1937, while he was at Princeton working on his PhD thesis, Turing built a digital (Boolean-logic) multiplier from scratch, and he made his own electromechanical relays for it (Hodges p. 138). "Alan's task was to embody the logical design of a Turing machine in a network of relay-operated switches..." (Hodges p. 138). Turing might have just been curious and experimenting at first, but quite-earnest work in the same direction was going on in Germany by Konrad Zuse (1938) and in the United States by Howard Aiken and George Stibitz (1937). The fruits of their labors were used by both the Axis and the Allied militaries in World War II (cf. Hodges p. 298–299).

In the early to mid-1950s Hao Wang and Marvin Minsky reduced the Turing machine to a simpler form, which was a precursor to the Post–Turing machine of Martin Davis. At the same time European researchers were reducing the new-fangled electronic computer to a computer-like theoretical object that is equivalent to what is now being called a "Turing machine". In the late 1950s and early 1960s, the coincidentally parallel developments of Melzak and Lambek (1961), Minsky (1961), and Shepherdson and Sturgis (1961) took the European work further and reduced the Turing machine to a more friendly, computer-like abstract model which is called the counter machine. Elgot and Robinson (1964), Hartmanis (1971), and Cook and Reckhow (1973) took this work even further with the register machine and random-access machine models. But basically all of these are just multi-tape Turing machines with an arithmetic-like instruction set.

## 1970–present: as a model of computation

Today the counter, register and random-access machines, and also their sire the Turing machine, are still the models of choice for theorists who investigate questions in the theory of computation. In particular computational complexity theory uses the Turing machine:

> Depending on the objects one likes to manipulate in the computations (numbers like nonnegative integers or alphanumeric strings), two models have obtained a dominant position in machine-based complexity theory:

> the off-line multitape Turing machine..., which represents the standard model for string-oriented computation, and the random access machine (RAM) as introduced by Cook and Reckhow..., which models the idealised Von Neumann-style computer.

— Van Emde Boas (1990)

> Only in the related area of analysis of algorithms this role is taken over by the RAM model.

— Van Emde Boas (1990)
````

</details>

<details><summary><b>Step 5 — draft_citation_needed</b> (1960 words)</summary>

````text
## Historical background: computational machinery

Robin Gandy (1919–1995) was a student of Alan Turing (1912–1954), and also his lifelong friend. Gandy traces the idea of a "calculating machine" back to Charles Babbage (circa 1834), and he actually proposes something he calls "Babbage's Thesis":

> That the whole of development and operations of analysis are now capable of being executed by machinery.

— (italics in Babbage as cited by Gandy)

Gandy analyses Babbage's analytical engine and describes the following five operations that it has (cf. p. 52–53):

- The arithmetic functions +, −, ×, where − is "proper" subtraction: x − y = 0 if y ≥ x.
- Any sequence of operations is an operation.
- Iteration of an operation (repeating an operation P n times).
- Conditional iteration (repeating an operation P n times, conditional on the "success" of test T).
- Conditional transfer (i.e., a conditional "goto").

According to Gandy, "the functions which can be calculated by (1), (2), and (4) are precisely those which are Turing computable." He also cites other proposals for "universal calculating machines", which include the ones by Percy Ludgate (1909), Leonardo Torres Quevedo (1914), Maurice d'Ocagne (1922), Louis Couffignal (1933), Vannevar Bush (1936) and Howard Aiken (1937). But about these he says:

> … the emphasis is on programming a fixed iterable sequence of arithmetical operations. The fundamental importance of conditional iteration and conditional transfer for a general theory of calculating machines is not recognized…

— Gandy

## The Entscheidungsproblem (the "decision problem"): Hilbert's tenth question of 1900

The famous mathematician David Hilbert posed his problems in 1900, and one aspect of problem #10 had been floating around for almost 30 years before it got framed precisely. This is Hilbert's original expression for No. 10:

> 10. Determination of the solvability of a Diophantine equation. Given a Diophantine equation with any number of unknown quantities and with rational integral coefficients: To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers. The Entscheidungsproblem [decision problem for first-order logic ] is solved when we know a procedure that allows for any given logical expression to decide by finitely many operations its validity or satisfiability... The Entscheidungsproblem must be considered the main problem of mathematical logic.

— quoted, with this translation and the original German, in Dershowitz and Gurevich, 2008

By 1922 this notion of "Entscheidungsproblem" had developed a bit, and H. Behmann stated that

> ... most general form of the Entscheidungsproblem [is] as follows:

> A quite definite generally applicable prescription is required which will allow one to decide in a finite number of steps the truth or falsity of a given purely logical assertion...

— Gandy quoting Behmann

> Behmann remarks that... the general problem is equivalent to the problem of deciding which mathematical propositions are true.

— ibid.

> If one were able to solve the Entscheidungsproblem then one would have a "procedure for solving many (or even all) mathematical problems".

— ibid.

At the 1928 international congress of mathematicians, Hilbert "made his questions quite precise. First, was mathematics complete... Second, was mathematics consistent... And thirdly, was mathematics decidable ?" Kurt Gödel answered the first two questions in 1930, at the very same meeting where Hilbert gave his retirement speech (much to the chagrin of Hilbert). The third one, the Entscheidungsproblem, had to wait until the mid-1930s.

The problem was that to answer it you first needed a precise definition of "definite general applicable prescription", which the Princeton professor Alonzo Church would come to call "effective calculability", and in 1928 there was no such definition. Over the next 6–7 years Emil Post developed his definition, which was a worker moving from room to room writing and erasing marks per a list of instructions. Church and his two students Stephen Kleene and J. B. Rosser also developed one, by using Church's lambda-calculus and Gödel's recursion theory (1934). Church's paper was published 15 April 1936 and it showed that the Entscheidungsproblem was indeed "undecidable" [citation needed], and it beat Turing to the punch by almost a year (Turing's paper was submitted 28 May 1936 and published January 1937). Meanwhile Emil Post submitted a brief paper in the fall of 1936, so Turing at least had priority over Post. Church refereed Turing's paper, and while he did, Turing had time to study Church's paper and add an Appendix where he sketched a proof that Church's lambda-calculus and his own machines would compute the same functions.

> But what Church had done was something rather different, and in a certain sense weaker.... the Turing construction was more direct, and provided an argument from first principles, closing the gap in Church's demonstration.

— Hodges

Post had only proposed a definition of calculability and criticised Church's "definition", but he had not proved anything.

## Alan Turing's a-machine

In the spring of 1935 Turing, who was then a young Master's student at King's College, Cambridge, took on the challenge. He had been stimulated by the lectures of the logician M. H. A. Newman "and learned from them of Gödel's work and the Entscheidungsproblem... Newman used the word 'mechanical'...". In his obituary of Turing 1955 Newman writes:

> To the question 'what is a "mechanical" process?' Turing returned the characteristic answer 'Something that can be done by a machine' and he embarked on the highly congenial task of analysing the general notion of a computing machine.

— Gandy

Gandy also states that:

> I suppose, but do not know, that Turing, right from the start of his work, had as his goal a proof of the undecidability of the Entscheidungsproblem. He told me that the 'main idea' of the paper came to him when he was lying in Grantchester meadows in the summer of 1935. The 'main idea' might have either been his analysis of computation or his realization that there was a universal machine, and so a diagonal argument to prove unsolvability.

— ibid.

Gandy believed that Newman's statement above is "misleading", but not everyone shares this opinion. Turing had a lifelong interest in machines: "Alan had dreamt of inventing typewriters as a boy; [his mother] Mrs. Turing had a typewriter; and he could well have begun by asking himself what was meant by calling a typewriter 'mechanical'" (Hodges p. 96). When he was at Princeton doing his PhD, Turing built a Boolean-logic multiplier (see below). His PhD thesis is titled "Systems of Logic Based on Ordinals", and it contains this definition of "a computable function":

> It was stated above that 'a function is effectively calculable if its values can be found by some purely mechanical process'. We may take this statement literally, understanding by a purely mechanical process one which could be carried out by a machine. It is possible to give a mathematical description, in a certain normal form, of the structures of these machines. The development of these ideas leads to the author's definition of a computable function, and to an identification of computability with effective calculability. It is not difficult, though somewhat laborious, to prove that these three definitions [the 3rd is the λ-calculus] are equivalent.

— Turing (1939, p. 166)

Turing invented the "a-machine" (automatic machine) in 1936. He submitted his paper to the London Mathematical Society for its Proceedings on 31 May 1936, but it was published in early 1937, and offprints were available in February 1937. The term "Turing machine" was coined later by Turing's doctoral advisor, Alonzo Church, in a review. [citation needed] Using this model Turing could answer two questions in the negative:

- Does a machine exist that can determine whether any arbitrary machine on its tape is "circular" (e.g., freezes, or fails to continue its computational task)?
- Does a machine exist that can determine whether any arbitrary machine on its tape ever prints a given symbol? [citation needed]

So by giving a mathematical description of a very simple device that can do arbitrary computations, he was able to prove properties of computation in general, and in particular the uncomputability of the Entscheidungsproblem ('decision problem'). [citation needed]

After Turing returned to the UK he ultimately became jointly responsible for breaking the German secret codes that were created by encryption machines called "The Enigma". He also got involved in the design of the ACE (Automatic Computing Engine): "[Turing's] ACE proposal was effectively self-contained, and its roots lay not in the EDVAC [the USA's initiative], but in his own universal machine" (Hodges p. 318). There are still arguments about the origin and nature of what Kleene (1952) named Turing's Thesis. But what Turing did prove with his computational-machine model is in his paper "On Computable Numbers, with an Application to the Entscheidungsproblem" (1937):

> [that] the Hilbert Entscheidungsproblem can have no solution... I propose, therefore to show that there can be no general process for determining whether a given formula U of the functional calculus K is provable, i.e. that there can be no machine which, supplied with any one U of these formulae, will eventually say whether U is provable.

— from Turing's paper as reprinted in The Undecidable, p. 145

Turing's example (his second proof) is this: if one asks for a general procedure to tell us "Does this machine ever print 0", the question is "undecidable".

## 1937–1970: The "digital computer", the birth of "computer science"

In 1937, while he was at Princeton working on his PhD thesis, Turing built a digital (Boolean-logic) multiplier from scratch, and he made his own electromechanical relays for it (Hodges p. 138). "Alan's task was to embody the logical design of a Turing machine in a network of relay-operated switches..." (Hodges p. 138). Turing might have just been curious and experimenting at first, but quite-earnest work in the same direction was going on in Germany by Konrad Zuse (1938) and in the United States by Howard Aiken and George Stibitz (1937). The fruits of their labors were used by both the Axis and the Allied militaries in World War II (cf. Hodges p. 298–299).

In the early to mid-1950s Hao Wang and Marvin Minsky reduced the Turing machine to a simpler form, which was a precursor to the Post–Turing machine of Martin Davis. At the same time European researchers were reducing the new-fangled electronic computer to a computer-like theoretical object that is equivalent to what is now being called a "Turing machine". In the late 1950s and early 1960s, the coincidentally parallel developments of Melzak and Lambek (1961), Minsky (1961), and Shepherdson and Sturgis (1961) took the European work further and reduced the Turing machine to a more friendly, computer-like abstract model which is called the counter machine. Elgot and Robinson (1964), Hartmanis (1971), and Cook and Reckhow (1973) took this work even further with the register machine and random-access machine models. But basically all of these are just multi-tape Turing machines with an arithmetic-like instruction set.

## 1970–present: as a model of computation

Today the counter, register and random-access machines, and also their sire the Turing machine, are still the models of choice for theorists who investigate questions in the theory of computation. In particular computational complexity theory uses the Turing machine:

> Depending on the objects one likes to manipulate in the computations (numbers like nonnegative integers or alphanumeric strings), two models have obtained a dominant position in machine-based complexity theory:

> the off-line multitape Turing machine..., which represents the standard model for string-oriented computation, and the random access machine (RAM) as introduced by Cook and Reckhow..., which models the idealised Von Neumann-style computer.

— Van Emde Boas (1990)

> Only in the related area of analysis of algorithms this role is taken over by the RAM model.

— Van Emde Boas (1990)
````

</details>

<details><summary><b>Step 6 — cited_draft</b> (2027 words)</summary>

````text
## Historical background: computational machinery

Robin Gandy (1919–1995) was a student of Alan Turing (1912–1954), and also his lifelong friend. Gandy traces the idea of a "calculating machine" back to Charles Babbage (circa 1834), and he actually proposes something he calls "Babbage's Thesis":

> That the whole of development and operations of analysis are now capable of being executed by machinery.

— (italics in Babbage as cited by Gandy)

Gandy analyses Babbage's analytical engine and describes the following five operations that it has (cf. p. 52–53):

- The arithmetic functions +, −, ×, where − is "proper" subtraction: x − y = 0 if y ≥ x.
- Any sequence of operations is an operation.
- Iteration of an operation (repeating an operation P n times).
- Conditional iteration (repeating an operation P n times, conditional on the "success" of test T).
- Conditional transfer (i.e., a conditional "goto").

According to Gandy, "the functions which can be calculated by (1), (2), and (4) are precisely those which are Turing computable." He also cites other proposals for "universal calculating machines", which include the ones by Percy Ludgate (1909), Leonardo Torres Quevedo (1914), Maurice d'Ocagne (1922), Louis Couffignal (1933), Vannevar Bush (1936) and Howard Aiken (1937). But about these he says:

> … the emphasis is on programming a fixed iterable sequence of arithmetical operations. The fundamental importance of conditional iteration and conditional transfer for a general theory of calculating machines is not recognized…

— Gandy

## The Entscheidungsproblem (the "decision problem"): Hilbert's tenth question of 1900

The famous mathematician David Hilbert posed his problems in 1900, and one aspect of problem #10 had been floating around for almost 30 years before it got framed precisely. This is Hilbert's original expression for No. 10:

> 10. Determination of the solvability of a Diophantine equation. Given a Diophantine equation with any number of unknown quantities and with rational integral coefficients: To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers. The Entscheidungsproblem [decision problem for first-order logic ] is solved when we know a procedure that allows for any given logical expression to decide by finitely many operations its validity or satisfiability... The Entscheidungsproblem must be considered the main problem of mathematical logic.

— quoted, with this translation and the original German, in Dershowitz and Gurevich, 2008

By 1922 this notion of "Entscheidungsproblem" had developed a bit, and H. Behmann stated that

> ... most general form of the Entscheidungsproblem [is] as follows:

> A quite definite generally applicable prescription is required which will allow one to decide in a finite number of steps the truth or falsity of a given purely logical assertion...

— Gandy quoting Behmann

> Behmann remarks that... the general problem is equivalent to the problem of deciding which mathematical propositions are true.

— ibid.

> If one were able to solve the Entscheidungsproblem then one would have a "procedure for solving many (or even all) mathematical problems".

— ibid.

At the 1928 international congress of mathematicians, Hilbert "made his questions quite precise. First, was mathematics complete... Second, was mathematics consistent... And thirdly, was mathematics decidable ?" Kurt Gödel answered the first two questions in 1930, at the very same meeting where Hilbert gave his retirement speech (much to the chagrin of Hilbert). The third one, the Entscheidungsproblem, had to wait until the mid-1930s.

The problem was that to answer it you first needed a precise definition of "definite general applicable prescription", which the Princeton professor Alonzo Church would come to call "effective calculability", and in 1928 there was no such definition. Over the next 6–7 years Emil Post developed his definition, which was a worker moving from room to room writing and erasing marks per a list of instructions. Church and his two students Stephen Kleene and J. B. Rosser also developed one, by using Church's lambda-calculus and Gödel's recursion theory (1934). Church's paper was published 15 April 1936 and it showed that the Entscheidungsproblem was indeed "undecidable" [1], and it beat Turing to the punch by almost a year (Turing's paper was submitted 28 May 1936 and published January 1937). Meanwhile Emil Post submitted a brief paper in the fall of 1936, so Turing at least had priority over Post. Church refereed Turing's paper, and while he did, Turing had time to study Church's paper and add an Appendix where he sketched a proof that Church's lambda-calculus and his own machines would compute the same functions.

> But what Church had done was something rather different, and in a certain sense weaker.... the Turing construction was more direct, and provided an argument from first principles, closing the gap in Church's demonstration.

— Hodges

Post had only proposed a definition of calculability and criticised Church's "definition", but he had not proved anything.

## Alan Turing's a-machine

In the spring of 1935 Turing, who was then a young Master's student at King's College, Cambridge, took on the challenge. He had been stimulated by the lectures of the logician M. H. A. Newman "and learned from them of Gödel's work and the Entscheidungsproblem... Newman used the word 'mechanical'...". In his obituary of Turing 1955 Newman writes:

> To the question 'what is a "mechanical" process?' Turing returned the characteristic answer 'Something that can be done by a machine' and he embarked on the highly congenial task of analysing the general notion of a computing machine.

— Gandy

Gandy also states that:

> I suppose, but do not know, that Turing, right from the start of his work, had as his goal a proof of the undecidability of the Entscheidungsproblem. He told me that the 'main idea' of the paper came to him when he was lying in Grantchester meadows in the summer of 1935. The 'main idea' might have either been his analysis of computation or his realization that there was a universal machine, and so a diagonal argument to prove unsolvability.

— ibid.

Gandy believed that Newman's statement above is "misleading", but not everyone shares this opinion. Turing had a lifelong interest in machines: "Alan had dreamt of inventing typewriters as a boy; [his mother] Mrs. Turing had a typewriter; and he could well have begun by asking himself what was meant by calling a typewriter 'mechanical'" (Hodges p. 96). When he was at Princeton doing his PhD, Turing built a Boolean-logic multiplier (see below). His PhD thesis is titled "Systems of Logic Based on Ordinals", and it contains this definition of "a computable function":

> It was stated above that 'a function is effectively calculable if its values can be found by some purely mechanical process'. We may take this statement literally, understanding by a purely mechanical process one which could be carried out by a machine. It is possible to give a mathematical description, in a certain normal form, of the structures of these machines. The development of these ideas leads to the author's definition of a computable function, and to an identification of computability with effective calculability. It is not difficult, though somewhat laborious, to prove that these three definitions [the 3rd is the λ-calculus] are equivalent.

— Turing (1939, p. 166)

Turing invented the "a-machine" (automatic machine) in 1936. He submitted his paper to the London Mathematical Society for its Proceedings on 31 May 1936, but it was published in early 1937, and offprints were available in February 1937. The term "Turing machine" was coined later by Turing's doctoral advisor, Alonzo Church, in a review. [2] Using this model Turing could answer two questions in the negative:

- Does a machine exist that can determine whether any arbitrary machine on its tape is "circular" (e.g., freezes, or fails to continue its computational task)?
- Does a machine exist that can determine whether any arbitrary machine on its tape ever prints a given symbol? [3]

So by giving a mathematical description of a very simple device that can do arbitrary computations, he was able to prove properties of computation in general, and in particular the uncomputability of the Entscheidungsproblem ('decision problem'). [4]

After Turing returned to the UK he ultimately became jointly responsible for breaking the German secret codes that were created by encryption machines called "The Enigma". He also got involved in the design of the ACE (Automatic Computing Engine): "[Turing's] ACE proposal was effectively self-contained, and its roots lay not in the EDVAC [the USA's initiative], but in his own universal machine" (Hodges p. 318). There are still arguments about the origin and nature of what Kleene (1952) named Turing's Thesis. But what Turing did prove with his computational-machine model is in his paper "On Computable Numbers, with an Application to the Entscheidungsproblem" (1937):

> [that] the Hilbert Entscheidungsproblem can have no solution... I propose, therefore to show that there can be no general process for determining whether a given formula U of the functional calculus K is provable, i.e. that there can be no machine which, supplied with any one U of these formulae, will eventually say whether U is provable.

— from Turing's paper as reprinted in The Undecidable, p. 145

Turing's example (his second proof) is this: if one asks for a general procedure to tell us "Does this machine ever print 0", the question is "undecidable".

## 1937–1970: The "digital computer", the birth of "computer science"

In 1937, while he was at Princeton working on his PhD thesis, Turing built a digital (Boolean-logic) multiplier from scratch, and he made his own electromechanical relays for it (Hodges p. 138). "Alan's task was to embody the logical design of a Turing machine in a network of relay-operated switches..." (Hodges p. 138). Turing might have just been curious and experimenting at first, but quite-earnest work in the same direction was going on in Germany by Konrad Zuse (1938) and in the United States by Howard Aiken and George Stibitz (1937). The fruits of their labors were used by both the Axis and the Allied militaries in World War II (cf. Hodges p. 298–299).

In the early to mid-1950s Hao Wang and Marvin Minsky reduced the Turing machine to a simpler form, which was a precursor to the Post–Turing machine of Martin Davis. At the same time European researchers were reducing the new-fangled electronic computer to a computer-like theoretical object that is equivalent to what is now being called a "Turing machine". In the late 1950s and early 1960s, the coincidentally parallel developments of Melzak and Lambek (1961), Minsky (1961), and Shepherdson and Sturgis (1961) took the European work further and reduced the Turing machine to a more friendly, computer-like abstract model which is called the counter machine. Elgot and Robinson (1964), Hartmanis (1971), and Cook and Reckhow (1973) took this work even further with the register machine and random-access machine models. But basically all of these are just multi-tape Turing machines with an arithmetic-like instruction set.

## 1970–present: as a model of computation

Today the counter, register and random-access machines, and also their sire the Turing machine, are still the models of choice for theorists who investigate questions in the theory of computation. In particular computational complexity theory uses the Turing machine:

> Depending on the objects one likes to manipulate in the computations (numbers like nonnegative integers or alphanumeric strings), two models have obtained a dominant position in machine-based complexity theory:

> the off-line multitape Turing machine..., which represents the standard model for string-oriented computation, and the random access machine (RAM) as introduced by Cook and Reckhow..., which models the idealised Von Neumann-style computer.

— Van Emde Boas (1990)

> Only in the related area of analysis of algorithms this role is taken over by the RAM model.

— Van Emde Boas (1990)

References:
[1] The narrower question posed in Hilbert's tenth problem, about Diophantine equations, remained unresolved until 1970, when the relationship between recursively enumerable sets and Diophantine sets was finally laid bare.
[2] See note in forward Tyler & Emderton (2019) harvtxt error: no target: CITEREFTylerEmderton2019 (help).
[3] Turing 1936 in Davis (2004, pp. 132–134); Turing's definition of "circular" is found on page 119.
[4] Turing 1936 in Davis (2004, p. 145)
````

</details>

<details><summary><b>Step 7 — revised_draft</b> (1982 words)</summary>

````text
## Historical background: computational machinery

Robin Gandy (1919–1995)—a student of Alan Turing (1912–1954), and his lifelong friend—traces the notion of "calculating machine" back to Charles Babbage (circa 1834) and proposes what he calls "Babbage's Thesis":

> That the whole of development and operations of analysis are now capable of being executed by machinery.

— (italics in Babbage as cited by Gandy)

Gandy's analysis of Babbage's analytical engine describes these five operations (cf. p. 52–53):

- The arithmetic functions +, −, ×, where − indicates "proper" subtraction: x − y = 0 if y ≥ x.

- Any sequence of operations is an operation.

- Iteration of an operation (repeating n times an operation P).

- Conditional iteration (repeating n times an operation P conditional on the "success" of test T).

- Conditional transfer (i.e., conditional " goto ").

Gandy states that "the functions which can be calculated by (1), (2), and (4) are precisely those which are Turing computable." He also cites other proposals for "universal calculating machines" including those of Percy Ludgate (1909), Leonardo Torres Quevedo (1914), Maurice d'Ocagne (1922), Louis Couffignal (1933), Vannevar Bush (1936) and Howard Aiken (1937). However:

> … the emphasis is on programming a fixed iterable sequence of arithmetical operations. The fundamental importance of conditional iteration and conditional transfer for a general theory of calculating machines is not recognized…

— Gandy

## The Entscheidungsproblem (the "decision problem"): Hilbert's tenth question of 1900

Of the problems posed by the famous mathematician David Hilbert in 1900, an aspect of problem #10 had been floating around for almost 30 years before it was framed precisely. Hilbert's original expression for No. 10 is as follows:

> 10. Determination of the solvability of a Diophantine equation. Given a Diophantine equation with any number of unknown quantities and with rational integral coefficients: To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers. The Entscheidungsproblem [decision problem for first-order logic ] is solved when we know a procedure that allows for any given logical expression to decide by finitely many operations its validity or satisfiability... The Entscheidungsproblem must be considered the main problem of mathematical logic.

— quoted, with this translation and the original German, in Dershowitz and Gurevich, 2008

By 1922, this notion of " Entscheidungsproblem " had developed somewhat, and H. Behmann stated that

> ... most general form of the Entscheidungsproblem [is] as follows:

> A quite definite generally applicable prescription is required which will allow one to decide in a finite number of steps the truth or falsity of a given purely logical assertion...

— Gandy quoting Behmann

> Behmann remarks that... the general problem is equivalent to the problem of deciding which mathematical propositions are true.

— ibid.

> If one were able to solve the Entscheidungsproblem then one would have a "procedure for solving many (or even all) mathematical problems".

— ibid.

At the 1928 international congress of mathematicians, Hilbert "made his questions quite precise. First, was mathematics complete... Second, was mathematics consistent... And thirdly, was mathematics decidable ?" The first two questions were answered in 1930 by Kurt Gödel at the very same meeting where Hilbert delivered his retirement speech (much to the chagrin of Hilbert); the third—the Entscheidungsproblem —had to wait until the mid-1930s.

The problem was that answering it first required a precise definition of "definite general applicable prescription", which Princeton professor Alonzo Church would come to call " effective calculability ", and in 1928 no such definition existed. Over the next 6–7 years Emil Post developed his definition of a worker moving from room to room writing and erasing marks per a list of instructions, as did Church and his two students Stephen Kleene and J. B. Rosser by use of Church's lambda-calculus and Gödel's recursion theory (1934). Church's paper (published 15 April 1936) showed that the Entscheidungsproblem was indeed "undecidable" [1] and beat Turing to the punch by almost a year (Turing's paper submitted 28 May 1936, published January 1937). Meanwhile, Emil Post submitted a brief paper in the fall of 1936, so Turing at least had priority over Post. While Church refereed Turing's paper, Turing had time to study Church's paper and add an Appendix where he sketched a proof that Church's lambda-calculus and his machines would compute the same functions.

> But what Church had done was something rather different, and in a certain sense weaker.... the Turing construction was more direct, and provided an argument from first principles, closing the gap in Church's demonstration.

— Hodges

Post had only proposed a definition of calculability and criticised Church's "definition", but had not proved anything.

## Alan Turing's a-machine

In the spring of 1935, Turing as a young Master's student at King's College, Cambridge, took on the challenge; he had been stimulated by the lectures of the logician M. H. A. Newman "and learned from them of Gödel's work and the Entscheidungsproblem... Newman used the word 'mechanical'... In his obituary of Turing 1955 Newman writes:

> To the question 'what is a "mechanical" process?' Turing returned the characteristic answer 'Something that can be done by a machine' and he embarked on the highly congenial task of analysing the general notion of a computing machine.

— Gandy

Gandy states that:

> I suppose, but do not know, that Turing, right from the start of his work, had as his goal a proof of the undecidability of the Entscheidungsproblem. He told me that the 'main idea' of the paper came to him when he was lying in Grantchester meadows in the summer of 1935. The 'main idea' might have either been his analysis of computation or his realization that there was a universal machine, and so a diagonal argument to prove unsolvability.

— ibid.

Gandy believed that Newman's statement above is "misleading", but this opinion is not shared by all. Turing had a lifelong interest in machines: "Alan had dreamt of inventing typewriters as a boy; [his mother] Mrs. Turing had a typewriter; and he could well have begun by asking himself what was meant by calling a typewriter 'mechanical'" (Hodges p. 96). While he was at Princeton pursuing his PhD, Turing built a Boolean-logic multiplier (see below). His PhD thesis, titled " Systems of Logic Based on Ordinals ", contains the following definition of "a computable function":

> It was stated above that 'a function is effectively calculable if its values can be found by some purely mechanical process'. We may take this statement literally, understanding by a purely mechanical process one which could be carried out by a machine. It is possible to give a mathematical description, in a certain normal form, of the structures of these machines. The development of these ideas leads to the author's definition of a computable function, and to an identification of computability with effective calculability. It is not difficult, though somewhat laborious, to prove that these three definitions [the 3rd is the λ-calculus] are equivalent.

— Turing (1939, p. 166)

Alan Turing invented the "a-machine" (automatic machine) in 1936. Turing submitted his paper to the London Mathematical Society for its Proceedings on 31 May 1936, but it was published in early 1937 and offprints were available in February 1937. It was Turing's doctoral advisor, Alonzo Church, who later coined the term "Turing machine" in a review. [2] Using this model, Turing was able to answer two questions in the negative:

- Does a machine exist that can determine whether any arbitrary machine on its tape is "circular" (e.g., freezes, or fails to continue its computational task)?

- Does a machine exist that can determine whether any arbitrary machine on its tape ever prints a given symbol? [3]

So by providing a mathematical description of a very simple device capable of arbitrary computations, he was able to prove properties of computation in general—and in particular, the uncomputability of the Entscheidungsproblem ('decision problem'). [4]

When Turing returned to the UK he ultimately became jointly responsible for breaking the German secret codes created by encryption machines called "The Enigma"; he was also involved in the design of the ACE (Automatic Computing Engine), "[Turing's] ACE proposal was effectively self-contained, and its roots lay not in the EDVAC [the USA's initiative], but in his own universal machine" (Hodges p. 318). Arguments still continue about the origin and nature of what has been named by Kleene (1952) Turing's Thesis. But what Turing did prove with his computational-machine model appears in his paper " On Computable Numbers, with an Application to the Entscheidungsproblem " (1937):

> [that] the Hilbert Entscheidungsproblem can have no solution... I propose, therefore to show that there can be no general process for determining whether a given formula U of the functional calculus K is provable, i.e. that there can be no machine which, supplied with any one U of these formulae, will eventually say whether U is provable.

— from Turing's paper as reprinted in The Undecidable, p. 145

Turing's example (his second proof): if one asks for a general procedure to tell us: "Does this machine ever print 0", the question is "undecidable".

## 1937–1970: The "digital computer", the birth of "computer science"

In 1937, while at Princeton working on his PhD thesis, Turing built a digital (Boolean-logic) multiplier from scratch, making his own electromechanical relays (Hodges p. 138). "Alan's task was to embody the logical design of a Turing machine in a network of relay-operated switches..." (Hodges p. 138). Turing might have been just initially curious and experimenting, but quite-earnest work in the same direction was going on in Germany by Konrad Zuse (1938), and in the United States by Howard Aiken and George Stibitz (1937); the fruits of their labors were used by both the Axis and Allied militaries in World War II (cf. Hodges p. 298–299). In the early to mid-1950s Hao Wang and Marvin Minsky reduced the Turing machine to a simpler form (a precursor to the Post–Turing machine of Martin Davis); at the same time European researchers were reducing the new-fangled electronic computer to a computer-like theoretical object equivalent to what is now being called a "Turing machine". In the late 1950s and early 1960s, the coincidentally parallel developments of Melzak and Lambek (1961), Minsky (1961), and Shepherdson and Sturgis (1961) took the European work further and reduced the Turing machine to a more friendly, computer-like abstract model called the counter machine; Elgot and Robinson (1964), Hartmanis (1971), Cook and Reckhow (1973) carried this work even further with the register machine and random-access machine models—but basically all are just multi-tape Turing machines with an arithmetic-like instruction set.

## 1970–present: as a model of computation

Today the counter, register and random-access machines, along with their sire the Turing machine, continue to be the models of choice for theorists investigating questions in the theory of computation. In particular, computational complexity theory uses the Turing machine:

> Depending on the objects one likes to manipulate in the computations (numbers like nonnegative integers or alphanumeric strings), two models have obtained a dominant position in machine-based complexity theory:

> the off-line multitape Turing machine..., which represents the standard model for string-oriented computation, and the random access machine (RAM) as introduced by Cook and Reckhow..., which models the idealised Von Neumann-style computer.

— Van Emde Boas (1990)

> Only in the related area of analysis of algorithms this role is taken over by the RAM model.

— Van Emde Boas (1990)

References:
[1] The narrower question posed in Hilbert's tenth problem, about Diophantine equations, remained unresolved until 1970, when the relationship between recursively enumerable sets and Diophantine sets was finally laid bare.
[2] See note in forward Tyler & Emderton (2019) harvtxt error: no target: CITEREFTylerEmderton2019 (help).
[3] Turing 1936 in Davis (2004, pp. 132–134); Turing's definition of "circular" is found on page 119.
[4] Turing 1936 in Davis (2004, p. 145)
````

</details>

<details><summary><b>Step 8 — final</b> (1984 words)</summary>

````text
## Historical background: computational machinery

Robin Gandy (1919–1995)—a student of Alan Turing (1912–1954), and his lifelong friend—traces the lineage of the notion of "calculating machine" back to Charles Babbage (circa 1834) and actually proposes "Babbage's Thesis":

> That the whole of development and operations of analysis are now capable of being executed by machinery.

— (italics in Babbage as cited by Gandy)

Gandy's analysis of Babbage's analytical engine describes the following five operations (cf. p. 52–53):

- The arithmetic functions +, −, ×, where − indicates "proper" subtraction: x − y = 0 if y ≥ x.

- Any sequence of operations is an operation.

- Iteration of an operation (repeating n times an operation P).

- Conditional iteration (repeating n times an operation P conditional on the "success" of test T).

- Conditional transfer (i.e., conditional " goto ").

Gandy states that "the functions which can be calculated by (1), (2), and (4) are precisely those which are Turing computable." He cites other proposals for "universal calculating machines" including those of Percy Ludgate (1909), Leonardo Torres Quevedo (1914), Maurice d'Ocagne (1922), Louis Couffignal (1933), Vannevar Bush (1936), Howard Aiken (1937). However:

> … the emphasis is on programming a fixed iterable sequence of arithmetical operations. The fundamental importance of conditional iteration and conditional transfer for a general theory of calculating machines is not recognized…

— Gandy

## The Entscheidungsproblem (the "decision problem"): Hilbert's tenth question of 1900

With regard to Hilbert's problems posed by the famous mathematician David Hilbert in 1900, an aspect of problem #10 had been floating about for almost 30 years before it was framed precisely. Hilbert's original expression for No. 10 is as follows:

> 10. Determination of the solvability of a Diophantine equation. Given a Diophantine equation with any number of unknown quantities and with rational integral coefficients: To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers. The Entscheidungsproblem [decision problem for first-order logic ] is solved when we know a procedure that allows for any given logical expression to decide by finitely many operations its validity or satisfiability... The Entscheidungsproblem must be considered the main problem of mathematical logic.

— quoted, with this translation and the original German, in Dershowitz and Gurevich, 2008

By 1922, this notion of " Entscheidungsproblem " had developed a bit, and H. Behmann stated that

> ... most general form of the Entscheidungsproblem [is] as follows:

> A quite definite generally applicable prescription is required which will allow one to decide in a finite number of steps the truth or falsity of a given purely logical assertion...

— Gandy quoting Behmann

> Behmann remarks that... the general problem is equivalent to the problem of deciding which mathematical propositions are true.

— ibid.

> If one were able to solve the Entscheidungsproblem then one would have a "procedure for solving many (or even all) mathematical problems".

— ibid.

By the 1928 international congress of mathematicians, Hilbert "made his questions quite precise. First, was mathematics complete... Second, was mathematics consistent... And thirdly, was mathematics decidable ?" The first two questions were answered in 1930 by Kurt Gödel at the very same meeting where Hilbert delivered his retirement speech (much to the chagrin of Hilbert); the third—the Entscheidungsproblem —had to wait until the mid-1930s.

The problem was that an answer first required a precise definition of "definite general applicable prescription", which Princeton professor Alonzo Church would come to call " effective calculability ", and in 1928 no such definition existed. But over the next 6–7 years Emil Post developed his definition of a worker moving from room to room writing and erasing marks per a list of instructions, as did Church and his two students Stephen Kleene and J. B. Rosser by use of Church's lambda-calculus and Gödel's recursion theory (1934). Church's paper (published 15 April 1936) showed that the Entscheidungsproblem was indeed "undecidable" [1] and beat Turing to the punch by almost a year (Turing's paper submitted 28 May 1936, published January 1937). In the meantime, Emil Post submitted a brief paper in the fall of 1936, so Turing at least had priority over Post. While Church refereed Turing's paper, Turing had time to study Church's paper and add an Appendix where he sketched a proof that Church's lambda-calculus and his machines would compute the same functions.

> But what Church had done was something rather different, and in a certain sense weaker.... the Turing construction was more direct, and provided an argument from first principles, closing the gap in Church's demonstration.

— Hodges

Post had only proposed a definition of calculability and criticised Church's "definition", but had proved nothing.

## Alan Turing's a-machine

In the spring of 1935, Turing as a young Master's student at King's College, Cambridge, took on the challenge; he had been stimulated by the lectures of the logician M. H. A. Newman "and learned from them of Gödel's work and the Entscheidungsproblem... Newman used the word 'mechanical'... In his obituary of Turing 1955 Newman writes:

> To the question 'what is a "mechanical" process?' Turing returned the characteristic answer 'Something that can be done by a machine' and he embarked on the highly congenial task of analysing the general notion of a computing machine.

— Gandy

Gandy states that:

> I suppose, but do not know, that Turing, right from the start of his work, had as his goal a proof of the undecidability of the Entscheidungsproblem. He told me that the 'main idea' of the paper came to him when he was lying in Grantchester meadows in the summer of 1935. The 'main idea' might have either been his analysis of computation or his realization that there was a universal machine, and so a diagonal argument to prove unsolvability.

— ibid.

While Gandy believed that Newman's statement above is "misleading", this opinion is not shared by all. Turing had a lifelong interest in machines: "Alan had dreamt of inventing typewriters as a boy; [his mother] Mrs. Turing had a typewriter; and he could well have begun by asking himself what was meant by calling a typewriter 'mechanical'" (Hodges p. 96). While at Princeton pursuing his PhD, Turing built a Boolean-logic multiplier (see below). His PhD thesis, titled " Systems of Logic Based on Ordinals ", contains the following definition of "a computable function":

> It was stated above that 'a function is effectively calculable if its values can be found by some purely mechanical process'. We may take this statement literally, understanding by a purely mechanical process one which could be carried out by a machine. It is possible to give a mathematical description, in a certain normal form, of the structures of these machines. The development of these ideas leads to the author's definition of a computable function, and to an identification of computability with effective calculability. It is not difficult, though somewhat laborious, to prove that these three definitions [the 3rd is the λ-calculus] are equivalent.

— Turing (1939, p. 166)

Alan Turing invented the "a-machine" (automatic machine) in 1936. Turing submitted his paper on 31 May 1936 to the London Mathematical Society for its Proceedings, but it was published in early 1937 and offprints were available in February 1937. It was Turing's doctoral advisor, Alonzo Church, who later coined the term "Turing machine" in a review. [2] With this model, Turing was able to answer two questions in the negative:

- Does a machine exist that can determine whether any arbitrary machine on its tape is "circular" (e.g., freezes, or fails to continue its computational task)?

- Does a machine exist that can determine whether any arbitrary machine on its tape ever prints a given symbol? [3]

Thus by providing a mathematical description of a very simple device capable of arbitrary computations, he was able to prove properties of computation in general—and in particular, the uncomputability of the Entscheidungsproblem ('decision problem'). [4]

When Turing returned to the UK he ultimately became jointly responsible for breaking the German secret codes created by encryption machines called "The Enigma"; he also became involved in the design of the ACE (Automatic Computing Engine), "[Turing's] ACE proposal was effectively self-contained, and its roots lay not in the EDVAC [the USA's initiative], but in his own universal machine" (Hodges p. 318). Arguments still continue concerning the origin and nature of what has been named by Kleene (1952) Turing's Thesis. But what Turing did prove with his computational-machine model appears in his paper " On Computable Numbers, with an Application to the Entscheidungsproblem " (1937):

> [that] the Hilbert Entscheidungsproblem can have no solution... I propose, therefore to show that there can be no general process for determining whether a given formula U of the functional calculus K is provable, i.e. that there can be no machine which, supplied with any one U of these formulae, will eventually say whether U is provable.

— from Turing's paper as reprinted in The Undecidable, p. 145

Turing's example (his second proof): If one is to ask for a general procedure to tell us: "Does this machine ever print 0", the question is "undecidable".

## 1937–1970: The "digital computer", the birth of "computer science"

In 1937, while at Princeton working on his PhD thesis, Turing built a digital (Boolean-logic) multiplier from scratch, making his own electromechanical relays (Hodges p. 138). "Alan's task was to embody the logical design of a Turing machine in a network of relay-operated switches..." (Hodges p. 138). While Turing might have been just initially curious and experimenting, quite-earnest work in the same direction was going in Germany by Konrad Zuse (1938), and in the United States by Howard Aiken and George Stibitz (1937); the fruits of their labors were used by both the Axis and Allied militaries in World War II (cf. Hodges p. 298–299). In the early to mid-1950s Hao Wang and Marvin Minsky reduced the Turing machine to a simpler form (a precursor to the Post–Turing machine of Martin Davis); simultaneously European researchers were reducing the new-fangled electronic computer to a computer-like theoretical object equivalent to what is now being called a "Turing machine". In the late 1950s and early 1960s, the coincidentally parallel developments of Melzak and Lambek (1961), Minsky (1961), and Shepherdson and Sturgis (1961) carried the European work further and reduced the Turing machine to a more friendly, computer-like abstract model called the counter machine; Elgot and Robinson (1964), Hartmanis (1971), Cook and Reckhow (1973) carried this work even further with the register machine and random-access machine models—but basically all are just multi-tape Turing machines with an arithmetic-like instruction set.

## 1970–present: as a model of computation

Today, the counter, register and random-access machines and their sire the Turing machine continue to be the models of choice for theorists investigating questions in the theory of computation. In particular, computational complexity theory makes use of the Turing machine:

> Depending on the objects one likes to manipulate in the computations (numbers like nonnegative integers or alphanumeric strings), two models have obtained a dominant position in machine-based complexity theory:

> the off-line multitape Turing machine..., which represents the standard model for string-oriented computation, and the random access machine (RAM) as introduced by Cook and Reckhow..., which models the idealised Von Neumann-style computer.

— Van Emde Boas (1990)

> Only in the related area of analysis of algorithms this role is taken over by the RAM model.

— Van Emde Boas (1990)

References:
[1] The narrower question posed in Hilbert's tenth problem, about Diophantine equations, remained unresolved until 1970, when the relationship between recursively enumerable sets and Diophantine sets was finally laid bare.
[2] See note in forward Tyler & Emderton (2019) harvtxt error: no target: CITEREFTylerEmderton2019 (help).
[3] Turing 1936 in Davis (2004, pp. 132–134); Turing's definition of "circular" is found on page 119.
[4] Turing 1936 in Davis (2004, p. 145)
````

</details>
