# 7. Dijkstra's algorithm — History

`A-wiki_Dijkstras_algorithm` · [D_mix_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Dijkstra%27s_algorithm&oldid=1378301409> · License: https://creativecommons.org/licenses/by-sa/4.0/

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | prompt | 23 | 0 | 0.03 | reconstructed |
| 1 | outline | 190 | 0 | 0.24 | reconstructed |
| 2 | rough_draft | 362 | 0 | 0.70 | reconstructed |
| 3 | cited_draft | 533 | 5 | 0.92 | reconstructed |
| 4 | final | 510 | 5 | 1.00 | source |

<details><summary><b>Step 0 — prompt</b> (23 words)</summary>

````text
Write the History section of the encyclopedia article on Dijkstra's algorithm, opening with Dijkstra's own account of how he came up with it.
````

</details>

<details><summary><b>Step 1 — outline</b> (190 words)</summary>

````text
- Opening quote: Dijkstra, interview with Philip L. Frana, Communications of the ACM, 2001
  - problem: shortest way from Rotterdam to Groningen / given city to given city
  - designed in about twenty minutes; shopping in Amsterdam with young fiancée, café terrace, cup of coffee
  - published in '59, three years later; publication still readable, "quite nice"
  - designed without pencil and paper -> forced to avoid all avoidable complexities
  - became one of the cornerstones of his fame, to his amazement
- Shortest path algorithm origin
  - 1956, programmer at Mathematical Center in Amsterdam
  - wanted to demonstrate the new ARMAC computer
  - goal: problem + computer solution non-computing people could understand
  - implemented for ARMAC: slightly simplified transportation map, 64 cities in the Netherlands
  - 64 so that 6 bits enough to encode city number
- Minimum spanning tree
  - a year later: problem from hardware engineers on the institute's next computer
  - minimize wire to connect pins on machine's back panel
  - re-discovered Prim's minimal spanning tree algorithm (known earlier to Jarník, also rediscovered by Prim)
- Publication: 1959, two years after Prim, 29 years after Jarník
````

</details>

<details><summary><b>Step 2 — rough_draft</b> (362 words)</summary>

````text
> What is the shortest way to travel from Rotterdam to Groningen, in general: from given city to given city. It is the algorithm for the shortest path, which I designed in about twenty minutes. One morning I was shopping in Amsterdam with my young fiancée, and tired, we sat down on the café terrace to drink a cup of coffee and I was just thinking about whether I could do this, and I then designed the algorithm for the shortest path. As I said, it was a twenty-minute invention. In fact, it was published in '59, three years later. The publication is still readable, it is, in fact, quite nice. One of the reasons that it is so nice was that I designed it without pencil and paper. I learned later that one of the advantages of designing without pencil and paper is that you are almost forced to avoid all avoidable complexities. Eventually, that algorithm became to my great amazement, one of the cornerstones of my fame.

— Edsger Dijkstra, interview with Philip L. Frana, Communications of the ACM, 2001

Dijkstra was working as a programmer at the Mathematical Center in Amsterdam in 1956 when he thought about the shortest path problem. He wanted to show what the new ARMAC computer could do. The objective was to pick a problem, and a computer solution for it, that people who were not in computing could understand. He designed the shortest path algorithm and later implemented it for ARMAC on a transportation map of 64 cities in the Netherlands that was slightly simplified (he limited it to 64 cities so that 6 bits would be enough to encode the city number). A year after that he came across another problem, which was advanced by hardware engineers working on the next computer of the institute: how to minimize the amount of wire needed to connect the pins on the back panel of the machine. As a solution he re-discovered Prim's minimal spanning tree algorithm (which was known earlier to Jarník, and was also rediscovered by Prim). Dijkstra published the algorithm in 1959, which was two years after Prim and 29 years after Jarník.
````

</details>

<details><summary><b>Step 3 — cited_draft</b> (533 words)</summary>

````text
> What is the shortest way to travel from Rotterdam to Groningen, in general: from given city to given city. It is the algorithm for the shortest path, which I designed in about twenty minutes. One morning I was shopping in Amsterdam with my young fiancée, and tired, we sat down on the café terrace to drink a cup of coffee and I was just thinking about whether I could do this, and I then designed the algorithm for the shortest path. As I said, it was a twenty-minute invention. In fact, it was published in '59, three years later. The publication is still readable, it is, in fact, quite nice. One of the reasons that it is so nice was that I designed it without pencil and paper. I learned later that one of the advantages of designing without pencil and paper is that you are almost forced to avoid all avoidable complexities. Eventually, that algorithm became to my great amazement, one of the cornerstones of my fame.

— Edsger Dijkstra, interview with Philip L. Frana, Communications of the ACM, 2001 [1]

Dijkstra was working as a programmer at the Mathematical Center in Amsterdam in 1956 when he thought about the shortest path problem. He wanted to show what the new ARMAC computer could do. [2] The objective was to pick a problem, and a computer solution for it, that people who were not in computing could understand. He designed the shortest path algorithm and later implemented it for ARMAC on a transportation map of 64 cities in the Netherlands that was slightly simplified (he limited it to 64 cities so that 6 bits would be enough to encode the city number). [1] A year after that he came across another problem, which was advanced by hardware engineers working on the next computer of the institute: how to minimize the amount of wire needed to connect the pins on the back panel of the machine. As a solution he re-discovered Prim's minimal spanning tree algorithm (which was known earlier to Jarník, and was also rediscovered by Prim). [3,4] Dijkstra published the algorithm in 1959, which was two years after Prim and 29 years after Jarník. [5,6]

References:
[1] Frana, Phil (August 2010). "An Interview with Edsger W. Dijkstra". Communications of the ACM. 53 (8): 41– 47. doi: 10.1145/1787234.1787249. S2CID 27009702.
[2] "ARMAC". Unsung Heroes in Dutch Computing History. 2007. Archived from the original on 13 November 2013.
[3] Dijkstra, Edsger W., Reflections on "A note on two problems in connexion with graphs (PDF)
[4] Tarjan, Robert Endre (1983), Data Structures and Network Algorithms, CBMS_NSF Regional Conference Series in Applied Mathematics, vol. 44, Society for Industrial and Applied Mathematics, p. 75, The third classical minimum spanning tree algorithm was discovered by Jarník and rediscovered by Prim and Dikstra; it is commonly known as Prim's algorithm.
[5] Prim, R.C. (1957). "Shortest connection networks and some generalizations" (PDF). Bell System Technical Journal. 36 (6): 1389– 1401. Bibcode: 1957BSTJ...36.1389P. doi: 10.1002/j.1538-7305.1957.tb01515.x. Archived from the original (PDF) on 18 July 2017. Retrieved 18 July 2017.
[6] V. Jarník: O jistém problému minimálním [About a certain minimal problem], Práce Moravské Přírodovědecké Společnosti, 6, 1930, pp. 57–63. (in Czech)
````

</details>

<details><summary><b>Step 4 — final</b> (510 words)</summary>

````text
> What is the shortest way to travel from Rotterdam to Groningen, in general: from given city to given city. It is the algorithm for the shortest path, which I designed in about twenty minutes. One morning I was shopping in Amsterdam with my young fiancée, and tired, we sat down on the café terrace to drink a cup of coffee and I was just thinking about whether I could do this, and I then designed the algorithm for the shortest path. As I said, it was a twenty-minute invention. In fact, it was published in '59, three years later. The publication is still readable, it is, in fact, quite nice. One of the reasons that it is so nice was that I designed it without pencil and paper. I learned later that one of the advantages of designing without pencil and paper is that you are almost forced to avoid all avoidable complexities. Eventually, that algorithm became to my great amazement, one of the cornerstones of my fame.

— Edsger Dijkstra, in an interview with Philip L. Frana, Communications of the ACM, 2001 [1]

Dijkstra thought about the shortest path problem while working as a programmer at the Mathematical Center in Amsterdam in 1956. He wanted to demonstrate the capabilities of the new ARMAC computer. [2] His objective was to choose a problem and a computer solution that non-computing people could understand. He designed the shortest path algorithm and later implemented it for ARMAC for a slightly simplified transportation map of 64 cities in the Netherlands (he limited it to 64, so that 6 bits would be sufficient to encode the city number). [1] A year later, he came across another problem advanced by hardware engineers working on the institute's next computer: minimize the amount of wire needed to connect the pins on the machine's back panel. As a solution, he re-discovered Prim's minimal spanning tree algorithm (known earlier to Jarník, and also rediscovered by Prim). [3,4] Dijkstra published the algorithm in 1959, two years after Prim and 29 years after Jarník. [5,6]

References:
[1] Frana, Phil (August 2010). "An Interview with Edsger W. Dijkstra". Communications of the ACM. 53 (8): 41– 47. doi: 10.1145/1787234.1787249. S2CID 27009702.
[2] "ARMAC". Unsung Heroes in Dutch Computing History. 2007. Archived from the original on 13 November 2013.
[3] Dijkstra, Edsger W., Reflections on "A note on two problems in connexion with graphs (PDF)
[4] Tarjan, Robert Endre (1983), Data Structures and Network Algorithms, CBMS_NSF Regional Conference Series in Applied Mathematics, vol. 44, Society for Industrial and Applied Mathematics, p. 75, The third classical minimum spanning tree algorithm was discovered by Jarník and rediscovered by Prim and Dikstra; it is commonly known as Prim's algorithm.
[5] Prim, R.C. (1957). "Shortest connection networks and some generalizations" (PDF). Bell System Technical Journal. 36 (6): 1389– 1401. Bibcode: 1957BSTJ...36.1389P. doi: 10.1002/j.1538-7305.1957.tb01515.x. Archived from the original (PDF) on 18 July 2017. Retrieved 18 July 2017.
[6] V. Jarník: O jistém problému minimálním [About a certain minimal problem], Práce Moravské Přírodovědecké Společnosti, 6, 1930, pp. 57–63. (in Czech)
````

</details>
