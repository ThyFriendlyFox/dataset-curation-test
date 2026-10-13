# 6. ENIAC — Development and design

`A-wiki_ENIAC` · [D_mix_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=ENIAC&oldid=1378744539> · License: https://creativecommons.org/licenses/by-sa/4.0/

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | prompt | 36 | 0 | 0.01 | reconstructed |
| 1 | outline | 607 | 0 | 0.30 | reconstructed |
| 2 | rough_draft | 1234 | 0 | 0.66 | reconstructed |
| 3 | cited_draft | 1639 | 19 | 0.82 | reconstructed |
| 4 | final | 1643 | 19 | 1.00 | source |

<details><summary><b>Step 0 — prompt</b> (36 words)</summary>

````text
Write the "Development and design" section of an encyclopedia article on ENIAC: who funded and built it and when, the people involved, how the machine was organized, and subsections on its components, operation times and reliability.
````

</details>

<details><summary><b>Step 1 — outline</b> (607 words)</summary>

````text
Development and design
- funding: US Army Ordnance Corps, Research and Development Command, Maj. Gen. Gladeon M. Barnes; ~$487,000 (= $7,000,000 in 2024)
- June 1941: firing tables for Army Ordnance Department computed by graduate students (Friden calculators, differential analyzer), supervised by John Mauchly
- Mauchly explores electronics to speed up; not electronics expert -> partners with research associate J. Presper Eckert
- Aug 1942: Mauchly proposes fully electronic calculating machine for the tables
- Army Ordnance accepts: six-month research contract to University of Pennsylvania, $61,700
- construction contract June 5, 1943; secret work starts following month, Moore School of Electrical Engineering, code name "Project PX", John Grist Brainerd principal investigator
- Herman Goldstine persuaded Army to fund, assigned to oversee
- assembly June 1944; Sept 1944 Eckert and Mauchly complete conception
- construction complete May 1945, testing at Moore School
- Nov 1945: first confidential report (Eckert, Mauchly, Brainerd, Goldstine) - how it functioned, how programmed
- 1946: Mauchly and Eckert resign, form Eckert–Mauchly Computer Corporation
- design engineers: Robert F. Shaw (function tables), Jeffrey Chuan Chu (divider/square-rooter), Thomas Kite Sharpless (master programmer), Frank Mural (master programmer), Arthur Burks (multiplier), Harry Huskey (reader/printer), Jack Davis (accumulators)
- programmers: Jean Jennings, Marlyn Wescoff, Ruth Lichterman, Betty Snyder, Frances Bilas, Kay McNulty
- design: large modular, panels w/ different functions; 20 accumulators (add/subtract, hold ten-digit decimal number)
- general-purpose buses ("trays"); panels send/receive, compute, save answers, trigger next op, no moving parts -> speed
- branching on sign of result -> versatility
## Components
- by end of operation (1955): 18,000 vacuum tubes, 7,200 crystal diodes, 6,000 relays, 70,000 resistors, 10,000 capacitors, ~5,000,000 hand-soldered joints
- >30 short tons (27 t); ~10 ft (3 m) tall, 3 ft (1 m) deep, 100 ft (30 m) long; 300 sq ft (28 m 2); 150 kW
- IBM card reader in, IBM card punch out; offline printing via IBM accounting machine (IBM 405)
- no memory system originally; punch cards as external memory; 1953 100-word magnetic-core memory by Burroughs Corporation
- ten-position ring counters; 36 vacuum tubes per digit, 10 dual triodes = flip-flops; arithmetic by counting pulses, carry on wrap-around (digit wheels of mechanical adding machine)
- 20 ten-digit signed accumulators, ten's complement, 5,000 add/subtract per second with a source (accumulator, constant transmitter); parallel -> higher peak
- carry wiring for double precision, not three or more (carry circuit timing)
- multiplier unit w/ 4 accumulators: up to 385 mult/s; divider/square-rooter w/ 5 accumulators: up to 40 div/s or 3 sqrt/s
- other nine units: initiating unit, cycling unit, master programmer, reader, printer, constant transmitter, three function tables
## Operation times
- Rojas and Hashagen (or Wilkes) give somewhat different times
- basic cycle 200 microseconds (20 cycles of 100 kHz clock), 5,000 cycles/s; per cycle write, read, or add/subtract
- multiply 10-digit by d -digit: d +4 cycles -> 14 cycles, 2,800 microseconds, 357/s; faster with fewer digits
- division / square root: 13(d +1) cycles -> up to 143 cycles, 28,600 microseconds, 35/s; Wilkes 1956:20: 10-digit quotient division 6 milliseconds
- ~500 FLOPS; as of 2026 supercomputers petascale (10 15 FLOPS) and exascale (10 18 FLOPS)
## Reliability
- common octal-base radio tubes; accumulators 6SN7 flip-flops; 6L7s, 6SJ7s, 6SA7s, 6AC7s logic; 6L6s, 6V6s line drivers between rack assemblies
- several tubes burned out almost daily -> nonfunctional ~half the time; high-reliability tubes only from 1948
- most failures in warm-up / cool-down (thermal stress on heaters, cathodes)
- reduced to one tube every two days; Eckert 1989 interview quote (fail every two days, locate within 15 minutes)
- 1954: longest run without failure 116 hours (~five days)
````

</details>

<details><summary><b>Step 2 — rough_draft</b> (1234 words)</summary>

````text
The United States Army Ordnance Corps, Research and Development Command, which was led by Major General Gladeon M. Barnes, paid for ENIAC's design and construction, and it cost about $487,000 (equivalent to $7,000,000 in 2024). In June 1941 graduate students were computing firing tables for artillery for the United States Army Ordnance Department, using Friden calculators and differential analyzer, and John Mauchly was supervising them. Mauchly started to explore using electronics to make these calculations faster. He was not an electronics expert, so he partnered with a research associate, J. Presper Eckert, to draft an electronic computer that could work a lot faster. In August 1942 Mauchly proposed a fully electronic calculating machine to calculate these tables. The U.S. Army Ordnance accepted the plan and gave the University of Pennsylvania a six-month research contract for $61,700. The construction contract was signed on June 5, 1943, and the next month secret work on the computer started at the University of Pennsylvania's Moore School of Electrical Engineering under the code name "Project PX", and John Grist Brainerd was the principal investigator. Herman Goldstine persuaded the Army to fund the project and they assigned him to oversee it. Assembly of the computer started in June 1944. In September 1944 Eckert and Mauchly completed their conception of the computer. Construction was finished in May 1945 and then testing started at the Moore School. In November 1945 Eckert, Mauchly, John Brainerd, and Herman Goldstine issued the first confidential report on the computer, which describes how it worked and how it was programmed. In 1946 Mauchly and Eckert resigned from the University of Pennsylvania and formed the Eckert–Mauchly Computer Corporation.

Mauchly and Eckert had a team of design engineers helping them, which included Robert F. Shaw (function tables), Jeffrey Chuan Chu (divider/square-rooter), Thomas Kite Sharpless (master programmer), Frank Mural (master programmer), Arthur Burks (multiplier), Harry Huskey (reader/printer) and Jack Davis (accumulators). Most of the ENIAC programming was done by several female mathematicians: Jean Jennings, Marlyn Wescoff, Ruth Lichterman, Betty Snyder, Frances Bilas, and Kay McNulty.

ENIAC was a big modular computer made of individual panels that did different functions. Twenty of the modules were accumulators, which could add and subtract and also hold a ten-digit decimal number in memory. Numbers were passed between the units over several general-purpose buses (at the time they were called trays). The panels of ENIAC could send and receive numbers, compute, save answers, and trigger the next operation, and they did all of this without any moving parts, which made the calculation very fast. It could also branch, meaning trigger different operations depending on the sign of a computed result, and this was essential to its versatility.

## Components

When it stopped operating in 1955, ENIAC had 18,000 vacuum tubes, 7,200 crystal diodes, 6,000 relays, 70,000 resistors, 10,000 capacitors, and about 5,000,000 hand-soldered joints. It weighed more than 30 short tons (27 t), and was roughly 10 ft (3 m) tall, 3 ft (1 m) deep, and 100 ft (30 m) long, it took up 300 sq ft (28 m 2) and it used 150 kW of electricity. Input could come from an IBM card reader and output went to an IBM card punch. The cards could be used to make printed output offline with an IBM accounting machine, like the IBM 405. ENIAC did not originally have a memory system, but the punch cards could be used for external memory storage. In 1953 a 100-word magnetic-core memory that was built by the Burroughs Corporation was added to ENIAC.

To store digits ENIAC used ten-position ring counters. Each digit needed 36 vacuum tubes, and 10 of them were the dual triodes that made up the flip-flops of the ring counter. Arithmetic was done by "counting" pulses with the ring counters and generating carry pulses when a counter "wrapped around". The idea was to emulate electronically how the digit wheels of a mechanical adding machine work.

ENIAC had 20 ten-digit signed accumulators. They used ten's complement representation and could do 5,000 simple addition or subtraction operations per second between any of them and a source (e.g., another accumulator or a constant transmitter). Several accumulators could be connected to run at the same time, so because of parallel operation the peak speed was potentially much higher.

The carry of one accumulator could be wired into another accumulator to do arithmetic with double the precision, but the timing of the accumulator carry circuit prevented wiring three or more together for even higher precision. ENIAC used four of the accumulators, controlled by a special multiplier unit, to do up to 385 multiplication operations per second, and five of the accumulators were controlled by a special divider/square-rooter unit to do up to 40 division operations per second or three square root operations per second.

The other nine units of ENIAC were the initiating unit (which started and stopped the machine), the cycling unit (which synchronized the other units), the master programmer (which controlled loop sequencing), the reader (which controlled an IBM punch-card reader), the printer (which controlled an IBM card punch), the constant transmitter, and three function tables.

## Operation times

There are more details about operation times in the references by Rojas and Hashagen (or Wilkes), and they are a bit different from the times given above.

The basic machine cycle was 200 microseconds (20 cycles of the 100 kHz clock in the cycling unit), which is 5,000 cycles per second for operations on the 10-digit numbers. In one cycle ENIAC could write a number to a register, read a number from a register, or add/subtract two numbers.

Multiplying a 10-digit number by a d -digit number (for d up to 10) took d +4 cycles, so multiplying a 10-digit number by a 10-digit number took 14 cycles, or 2,800 microseconds, which is a rate of 357 per second. If one of the numbers had fewer than 10 digits, it was faster.

Division and square roots took 13(d +1) cycles, where d is how many digits are in the result (the quotient or square root). So a division or a square root took up to 143 cycles, or 28,600 microseconds, which is a rate of 35 per second. (Wilkes 1956:20 says that a division with a 10-digit quotient needed 6 milliseconds.) If the result had less than ten digits it was obtained faster.

ENIAC could process about 500 FLOPS. As of 2026, supercomputers operate at petascale (10 15 FLOPS) and exascale (10 18 FLOPS) speeds.

## Reliability

ENIAC used the common octal-base radio tubes of the time. The decimal accumulators were made of 6SN7 flip-flops, and 6L7s, 6SJ7s, 6SA7s and 6AC7s were used for logic functions. Many 6L6s and 6V6s were used as line drivers to drive pulses through the cables between rack assemblies.

Almost every day several tubes burned out, so ENIAC was not working about half the time. Special high-reliability tubes were not available until 1948. However most of the failures happened during warm-up and cool-down, when the tube heaters and cathodes were under the most thermal stress. Engineers got ENIAC's tube failures down to a more acceptable rate of one tube every two days. In a 1989 interview Eckert said, "We had a tube fail about every two days and we could locate the problem within 15 minutes." In 1954, the longest continuous time it operated without a failure was 116 hours, close to five days.
````

</details>

<details><summary><b>Step 3 — cited_draft</b> (1639 words)</summary>

````text
The United States Army Ordnance Corps, Research and Development Command, which was led by Major General Gladeon M. Barnes, paid for ENIAC's design and construction, and it cost about $487,000 (equivalent to $7,000,000 in 2024). [1] In June 1941 graduate students were computing firing tables for artillery for the United States Army Ordnance Department, using Friden calculators and differential analyzer, and John Mauchly was supervising them. Mauchly started to explore using electronics to make these calculations faster. He was not an electronics expert, so he partnered with a research associate, J. Presper Eckert, to draft an electronic computer that could work a lot faster. In August 1942 Mauchly proposed a fully electronic calculating machine to calculate these tables. [2,3,4] The U.S. Army Ordnance accepted the plan and gave the University of Pennsylvania a six-month research contract for $61,700. [5] The construction contract was signed on June 5, 1943, and the next month secret work on the computer started at the University of Pennsylvania's Moore School of Electrical Engineering [6] under the code name "Project PX", and John Grist Brainerd was the principal investigator. Herman Goldstine persuaded the Army to fund the project and they assigned him to oversee it. [7] Assembly of the computer started in June 1944. [5] In September 1944 Eckert and Mauchly completed their conception of the computer. [8] Construction was finished in May 1945 and then testing started at the Moore School. In November 1945 Eckert, Mauchly, John Brainerd, and Herman Goldstine issued the first confidential report on the computer, which describes how it worked and how it was programmed. [3] In 1946 Mauchly and Eckert resigned from the University of Pennsylvania and formed the Eckert–Mauchly Computer Corporation.

Mauchly and Eckert had a team of design engineers helping them, which included Robert F. Shaw (function tables), Jeffrey Chuan Chu (divider/square-rooter), Thomas Kite Sharpless (master programmer), Frank Mural (master programmer), Arthur Burks (multiplier), Harry Huskey (reader/printer) and Jack Davis (accumulators). [9] Most of the ENIAC programming was done by several female mathematicians: Jean Jennings, Marlyn Wescoff, Ruth Lichterman, Betty Snyder, Frances Bilas, and Kay McNulty.

ENIAC was a big modular computer made of individual panels that did different functions. Twenty of the modules were accumulators, which could add and subtract and also hold a ten-digit decimal number in memory. Numbers were passed between the units over several general-purpose buses (at the time they were called trays). The panels of ENIAC could send and receive numbers, compute, save answers, and trigger the next operation, and they did all of this without any moving parts, which made the calculation very fast. It could also branch, meaning trigger different operations depending on the sign of a computed result, and this was essential to its versatility.

## Components

When it stopped operating in 1955, ENIAC had 18,000 vacuum tubes, 7,200 crystal diodes, 6,000 relays, 70,000 resistors, 10,000 capacitors, and about 5,000,000 hand-soldered joints. It weighed more than 30 short tons (27 t), and was roughly 10 ft (3 m) tall, 3 ft (1 m) deep, and 100 ft (30 m) long, it took up 300 sq ft (28 m 2) and it used 150 kW of electricity. [10,11] Input could come from an IBM card reader and output went to an IBM card punch. The cards could be used to make printed output offline with an IBM accounting machine, like the IBM 405. ENIAC did not originally have a memory system, but the punch cards could be used for external memory storage. [12] In 1953 a 100-word magnetic-core memory that was built by the Burroughs Corporation was added to ENIAC. [13]

To store digits ENIAC used ten-position ring counters. Each digit needed 36 vacuum tubes, and 10 of them were the dual triodes that made up the flip-flops of the ring counter. Arithmetic was done by "counting" pulses with the ring counters and generating carry pulses when a counter "wrapped around". The idea was to emulate electronically how the digit wheels of a mechanical adding machine work. [14]

ENIAC had 20 ten-digit signed accumulators. They used ten's complement representation and could do 5,000 simple addition or subtraction operations per second between any of them and a source (e.g., another accumulator or a constant transmitter). Several accumulators could be connected to run at the same time, so because of parallel operation the peak speed was potentially much higher. [15]

The carry of one accumulator could be wired into another accumulator to do arithmetic with double the precision, but the timing of the accumulator carry circuit prevented wiring three or more together for even higher precision. ENIAC used four of the accumulators, controlled by a special multiplier unit, to do up to 385 multiplication operations per second, and five of the accumulators were controlled by a special divider/square-rooter unit to do up to 40 division operations per second or three square root operations per second.

The other nine units of ENIAC were the initiating unit (which started and stopped the machine), the cycling unit (which synchronized the other units), the master programmer (which controlled loop sequencing), the reader (which controlled an IBM punch-card reader), the printer (which controlled an IBM card punch), the constant transmitter, and three function tables.

## Operation times

There are more details about operation times in the references by Rojas and Hashagen (or Wilkes) [17], and they are a bit different from the times given above.

The basic machine cycle was 200 microseconds (20 cycles of the 100 kHz clock in the cycling unit), which is 5,000 cycles per second for operations on the 10-digit numbers. In one cycle ENIAC could write a number to a register, read a number from a register, or add/subtract two numbers.

Multiplying a 10-digit number by a d -digit number (for d up to 10) took d +4 cycles, so multiplying a 10-digit number by a 10-digit number took 14 cycles, or 2,800 microseconds, which is a rate of 357 per second. If one of the numbers had fewer than 10 digits, it was faster.

Division and square roots took 13(d +1) cycles, where d is how many digits are in the result (the quotient or square root). So a division or a square root took up to 143 cycles, or 28,600 microseconds, which is a rate of 35 per second. (Wilkes 1956:20 [17] says that a division with a 10-digit quotient needed 6 milliseconds.) If the result had less than ten digits it was obtained faster.

ENIAC could process about 500 FLOPS. [18] As of 2026, supercomputers operate at petascale (10 15 FLOPS) and exascale (10 18 FLOPS) speeds.

## Reliability

ENIAC used the common octal-base radio tubes of the time. The decimal accumulators were made of 6SN7 flip-flops, and 6L7s, 6SJ7s, 6SA7s and 6AC7s were used for logic functions. [19] Many 6L6s and 6V6s were used as line drivers to drive pulses through the cables between rack assemblies.

Almost every day several tubes burned out, so ENIAC was not working about half the time. Special high-reliability tubes were not available until 1948. However most of the failures happened during warm-up and cool-down, when the tube heaters and cathodes were under the most thermal stress. Engineers got ENIAC's tube failures down to a more acceptable rate of one tube every two days. In a 1989 interview Eckert said, "We had a tube fail about every two days and we could locate the problem within 15 minutes." [20] In 1954, the longest continuous time it operated without a failure was 116 hours, close to five days.

References:
[1] Dalakov, Georgi. "ENIAC". History of Computers. Georgi Dalakov. Archived from the original on January 3, 2020. Retrieved May 23, 2016.
[2] "ENIAC - CHM Revolution". Computer History Museum. Retrieved November 9, 2024.
[3] "Key Events in the Development of the ENIAC". History of Information. Retrieved November 29, 2024.
[4] "Description of the ENIAC and comments on electronic digital computing machines" (PDF). Moore School of Electrical Engineering, University of Pennsylvania. November 30, 1945. Retrieved December 25, 2025.
[5] Computer History Museum (August 15, 2008). UNIVAC - Information Age: Then and Now. YouTube. Retrieved November 6, 2024.
[6] Goldstine & Goldstine 1946
[7] Gayle Ronan Sims (June 22, 2004). "Herman Heine Goldstine". The Philadelphia Inquirer. Archived from the original on November 30, 2015. Retrieved April 15, 2017 – via www.princeton.edu.
[8] "Key Developments Concerning the ENIAC Patent". History of Information. Retrieved November 29, 2024.
[9] "ENIAC on Trial". USHistory.org. Independence Hall Association. Archived from the original on August 12, 2019. Retrieved November 9, 2020.
[10] "ENIAC". The Free Dictionary. Retrieved March 29, 2015.
[11] Weik, Martin H. (December 1955). Ballistic Research Laboratories Report No. 971: A Survey of Domestic Electronic Digital Computing Systems. Aberdeen Proving Ground, MD: United States Department of Commerce Office of Technical Services. p. 41. Retrieved March 29, 2015.
[12] "ENIAC in Action: What it Was and How it Worked". ENIAC: Celebrating Penn Engineering History. University of Pennsylvania. Retrieved May 17, 2016.
[13] Martin, Jason (December 17, 1998). "Past and Future Developments in Memory Design". Past and Future Developments in Memory Design. University of Maryland. Retrieved May 17, 2016.
[14] Peddie, Jon (June 13, 2013). The History of Visual Magic in Computers: How Beautiful Images are Made in CAD, 3D, VR and AR. Springer Science & Business Media. ISBN 978-1-4471-4932-3.
[15] Igarashi, Yoshihide; Altman, Tom; Funada, Mariko; Kamiyama, Barbara (May 27, 2014). Computing: A Historical and Technical Perspective. CRC Press. ISBN 978-1-4822-2741-3.
[17] Wilkes, M. V. (1956). Automatic Digital Computers. New York: John Wiley & Sons. QA76.W5 1956.
[18] "The incredible evolution of supercomputers' powers, from 1946 to today". Popular Science. March 18, 2019. Retrieved February 8, 2022.
[19] Burks 1947, pp. 756–767
[20] Randall, Alexander 5th (February 14, 2006). "A lost interview with ENIAC co-inventor J. Presper Eckert". Computer World. Archived from the original on June 5, 2013. Retrieved March 29, 2015.
````

</details>

<details><summary><b>Step 4 — final</b> (1643 words)</summary>

````text
ENIAC's design and construction was financed by the United States Army Ordnance Corps, Research and Development Command, led by Major General Gladeon M. Barnes, at a cost of about $487,000, equivalent to $7,000,000 in 2024. [1] In June 1941 firing tables for artillery were being computed for the United States Army Ordnance Department by graduate students using Friden calculators and differential analyzer, under the supervision of John Mauchly. Mauchly began exploring the use of electronics to speed up these calculations. He was not an electronics expert, and he partnered with research associate J. Presper Eckert to draft an electronic computer that could work much faster. In August 1942 Mauchly proposed a fully electronic calculating machine to calculate these tables. [2,3,4] The U.S. Army Ordnance accepted their plan, giving the University of Pennsylvania a six-month research contract for $61,700. [5] The construction contract was signed on June 5, 1943, and secret work on the computer began at the University of Pennsylvania 's Moore School of Electrical Engineering [6] the following month, under the code name "Project PX", with John Grist Brainerd as principal investigator. Herman Goldstine persuaded the Army to fund the project and they assigned him to oversee it. [7] Assembly of the computer began in June 1944. [5] In September of that year, Eckert and Mauchly completed their conception of the computer. [8] Construction was complete in May 1945 and testing began at the Moore School. In November of that year, Eckert, Mauchly, John Brainerd, and Herman Goldstine issued the first confidential report on the computer, which describes how it functioned and the methods by which it was programmed. [3] In 1946, Mauchly and Eckert resigned from the University of Pennsylvania and formed the Eckert–Mauchly Computer Corporation.

The team of design engineers assisting Mauchly and Eckert included Robert F. Shaw (function tables), Jeffrey Chuan Chu (divider/square-rooter), Thomas Kite Sharpless (master programmer), Frank Mural (master programmer), Arthur Burks (multiplier), Harry Huskey (reader/printer) and Jack Davis (accumulators). [9] Several female mathematicians performed the bulk of the ENIAC programming: Jean Jennings, Marlyn Wescoff, Ruth Lichterman, Betty Snyder, Frances Bilas, and Kay McNulty.

ENIAC was a large, modular computer, composed of individual panels to perform different functions. Twenty of these modules were accumulators that could not only add and subtract, but hold a ten-digit decimal number in memory. Numbers were passed between these units across several general-purpose buses (called trays at the time). ENIAC's panels could send and receive numbers, compute, save answers, and trigger the next operation, all without any moving parts, allowing for great speed of calculation. It could also branch, or trigger different operations depending on the sign of a computed result, which was essential to its versatility.

## Components

By the end of its operation in 1955, ENIAC contained 18,000 vacuum tubes, 7,200 crystal diodes, 6,000 relays, 70,000 resistors, 10,000 capacitors, and approximately 5,000,000 hand-soldered joints. It weighed more than 30 short tons (27 t), was roughly 10 ft (3 m) tall, 3 ft (1 m) deep, and 100 ft (30 m) long, occupied 300 sq ft (28 m 2) and consumed 150 kW of electricity. [10,11] Input was possible from an IBM card reader and an IBM card punch was used for output. These cards could be used to produce printed output offline using an IBM accounting machine, such as the IBM 405. While ENIAC originally had no memory system, these punch cards could be used for external memory storage. [12] In 1953, a 100- word magnetic-core memory built by the Burroughs Corporation was added to ENIAC. [13]

ENIAC used ten-position ring counters to store digits; each digit required 36 vacuum tubes, 10 of which were the dual triodes making up the flip-flops of the ring counter. Arithmetic was performed by "counting" pulses with the ring counters and generating carry pulses if the counter "wrapped around", the idea being to electronically emulate the operation of the digit wheels of a mechanical adding machine. [14]

ENIAC had 20 ten-digit signed accumulators, which used ten's complement representation and could perform 5,000 simple addition or subtraction operations between any of them and a source (e.g., another accumulator or a constant transmitter) per second. It was possible to connect several accumulators to run simultaneously, so the peak speed of operation was potentially much higher, due to parallel operation. [15]

It was possible to wire the carry of one accumulator into another accumulator to perform arithmetic with double the precision, but the accumulator carry circuit timing prevented the wiring of three or more for even higher precision. ENIAC used four of the accumulators (controlled by a special multiplier unit) to perform up to 385 multiplication operations per second; five of the accumulators were controlled by a special divider/square-rooter unit to perform up to 40 division operations per second or three square root operations per second.

The other nine units in ENIAC were the initiating unit (started and stopped the machine), the cycling unit (used for synchronizing the other units), the master programmer (controlled loop sequencing), the reader (controlled an IBM punch-card reader), the printer (controlled an IBM card punch), the constant transmitter, and three function tables.

## Operation times

The references by Rojas and Hashagen (or Wilkes) [17] give more details about the times for operations, which differ somewhat from those stated above.

The basic machine cycle was 200 microseconds (20 cycles of the 100 kHz clock in the cycling unit), or 5,000 cycles per second for operations on the 10-digit numbers. In one of these cycles, ENIAC could write a number to a register, read a number from a register, or add/subtract two numbers.

A multiplication of a 10-digit number by a d -digit number (for d up to 10) took d +4 cycles, so the multiplication of a 10-digit number by 10-digit number took 14 cycles, or 2,800 microseconds—a rate of 357 per second. If one of the numbers had fewer than 10 digits, the operation was faster.

Division and square roots took 13(d +1) cycles, where d is the number of digits in the result (quotient or square root). So a division or square root took up to 143 cycles, or 28,600 microseconds—a rate of 35 per second. (Wilkes 1956:20 [17] states that a division with a 10-digit quotient required 6 milliseconds.) If the result had fewer than ten digits, it was obtained faster.

ENIAC was able to process about 500 FLOPS. [18] As of 2026, supercomputers operate at petascale (10 15 FLOPS) and exascale (10 18 FLOPS) speeds.

## Reliability

ENIAC used common octal-base radio tubes of the day; the decimal accumulators were made of 6SN7 flip-flops, while 6L7s, 6SJ7s, 6SA7s and 6AC7s were used in logic functions. [19] Numerous 6L6s and 6V6s served as line drivers to drive pulses through cables between rack assemblies.

Several tubes burned out almost every day, leaving ENIAC nonfunctional about half the time. Special high-reliability tubes were not available until 1948. Most of these failures, however, occurred during the warm-up and cool-down periods, when the tube heaters and cathodes were under the most thermal stress. Engineers reduced ENIAC's tube failures to the more acceptable rate of one tube every two days. According to an interview in 1989 with Eckert, "We had a tube fail about every two days and we could locate the problem within 15 minutes." [20] In 1954, the longest continuous period of operation without a failure was 116 hours—close to five days.

References:
[1] Dalakov, Georgi. "ENIAC". History of Computers. Georgi Dalakov. Archived from the original on January 3, 2020. Retrieved May 23, 2016.
[2] "ENIAC - CHM Revolution". Computer History Museum. Retrieved November 9, 2024.
[3] "Key Events in the Development of the ENIAC". History of Information. Retrieved November 29, 2024.
[4] "Description of the ENIAC and comments on electronic digital computing machines" (PDF). Moore School of Electrical Engineering, University of Pennsylvania. November 30, 1945. Retrieved December 25, 2025.
[5] Computer History Museum (August 15, 2008). UNIVAC - Information Age: Then and Now. YouTube. Retrieved November 6, 2024.
[6] Goldstine & Goldstine 1946
[7] Gayle Ronan Sims (June 22, 2004). "Herman Heine Goldstine". The Philadelphia Inquirer. Archived from the original on November 30, 2015. Retrieved April 15, 2017 – via www.princeton.edu.
[8] "Key Developments Concerning the ENIAC Patent". History of Information. Retrieved November 29, 2024.
[9] "ENIAC on Trial". USHistory.org. Independence Hall Association. Archived from the original on August 12, 2019. Retrieved November 9, 2020.
[10] "ENIAC". The Free Dictionary. Retrieved March 29, 2015.
[11] Weik, Martin H. (December 1955). Ballistic Research Laboratories Report No. 971: A Survey of Domestic Electronic Digital Computing Systems. Aberdeen Proving Ground, MD: United States Department of Commerce Office of Technical Services. p. 41. Retrieved March 29, 2015.
[12] "ENIAC in Action: What it Was and How it Worked". ENIAC: Celebrating Penn Engineering History. University of Pennsylvania. Retrieved May 17, 2016.
[13] Martin, Jason (December 17, 1998). "Past and Future Developments in Memory Design". Past and Future Developments in Memory Design. University of Maryland. Retrieved May 17, 2016.
[14] Peddie, Jon (June 13, 2013). The History of Visual Magic in Computers: How Beautiful Images are Made in CAD, 3D, VR and AR. Springer Science & Business Media. ISBN 978-1-4471-4932-3.
[15] Igarashi, Yoshihide; Altman, Tom; Funada, Mariko; Kamiyama, Barbara (May 27, 2014). Computing: A Historical and Technical Perspective. CRC Press. ISBN 978-1-4822-2741-3.
[16] The original photo can be seen in the article: Rose, Allen (April 1946). "Lightning Strikes Mathematics". Popular Science: 83– 86. Retrieved March 29, 2015.
[17] Wilkes, M. V. (1956). Automatic Digital Computers. New York: John Wiley & Sons. QA76.W5 1956.
[18] "The incredible evolution of supercomputers' powers, from 1946 to today". Popular Science. March 18, 2019. Retrieved February 8, 2022.
[19] Burks 1947, pp. 756–767
[20] Randall, Alexander 5th (February 14, 2006). "A lost interview with ENIAC co-inventor J. Presper Eckert". Computer World. Archived from the original on June 5, 2013. Retrieved March 29, 2015.
````

</details>
