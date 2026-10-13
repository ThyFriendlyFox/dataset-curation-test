# 7. Rust RFC: north star

`C-rfc_1728-north-star` · [full/D_mix_9step](README.md)

Source: <https://github.com/rust-lang/rfcs/blob/d2705ad64ba47e812a2b6b19d6f613fb4c14c5e0/text/1728-north-star.md> · License: MIT OR Apache-2.0 · 13 commits touching the file; 10 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | revision_1 | 3220 | 2 | 0.58 | commit 0670624136 (2016-08-22) |
| 2 | revision_2 | 3359 | 2 | 0.76 | commit 8b98bfd8f0 (2016-08-22) |
| 3 | revision_3 | 3597 | 2 | 0.85 | commit a0701a2d64 (2016-08-22) |
| 4 | revision_4 | 3719 | 0 | 0.89 | commit c3d4f6d20d (2016-08-22) |
| 5 | revision_5 | 3719 | 0 | 0.89 | commit 96a089ae1d (2016-08-23) |
| 6 | revision_6 | 3733 | 0 | 0.89 | commit 2832657eba (2016-08-23) |
| 7 | revision_7 | 3808 | 0 | 1.00 | commit 735549875c (2016-09-01) |
| 8 | final | 3808 | 0 | 1.00 | commit f17e8623ee (2025-11-28) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
north star
````

</details>

<details><summary><b>Step 1 — revision_1</b> (3220 words)</summary>

````text
# Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the language we are building toward among contributors, to make clear
the roadmap toward that vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language,
along with the story we want to be able to tell the world about Rust. Work
toward solving those problems, our short-term goals, will be decided in
quarter-long cycles by individual teams. Goals that result in stable features
will be assigned to release milestones for the purposes of reporting the project
roadmap.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress in The Rust Project toward our goals, as well as
achievements in the wider community. It will celebrate our performance and
anticipate its impact on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

# Motivation
[motivation]: #motivation

Rust is a massive system, developed by a massive team of mostly-independent
contributors. What we've achieved together already is mind-blowing: we've
created a uniquely powerful platform that solves problems that the computing
world had nearly given up on, and jumpstarted a new era in systems
programming. Now that Rust is out in the world, proving itself to be a stable
foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

For many months approaching the release of Rust 1.0 we had a clear, singular
goal: get Rust done and deliver it to the world. We knew precisely the discreet
steps necessary to get there, and although it was a tense period where the
entire future of the project was on the line, we were united in a single
mission. As The Rust Project Developers we were pumped up, and our user base -
along with the wider programming world - were excited to see what we would
deliver.

The same has not been true since. We've had a number of major goals - refactor
the compiler, enable strong IDE support, make cross-compilation easier, increase
community diversity - but it's not clear that we've been as focused on them as
needed. Even where there are clear strategic priorities in the project, they are
often under-emphasized in the way we talk about Rust, under-prioritized when we
do our own work or in our efforts to rally contributions, under-staffed by both
Mozilla and community contributors, and backburnered in favor of more present
issues. We are overwhelmed by an avalanche of promising ideas, with major RFCs
demanding attention (and languishing in the queue for months), TODO another
clause to make this sentence shine.

Compounding this problem is that we have no clear end state for our efforts, no
major deliverable to show for all our work, for the community to rally behind,
and for the user base to anticipate. To a great degree this is a result of our
own successes - we have a short, time-based release cycle where new features
drip out as they become available, and a feature integration process that places
incredible emphasis on maintaining stability. It works shockingly well! But Rust
releases are boring 😢 (admitedly some of the reason for this is that language
features have been delayed waiting on internal compiler refactoring). And -
perhaps surprisingly - our rapid release process seems to cause work to proceed
slowly: the lack of deadlines for features reduces the pressure to get them
done, and today there are many approved RFCs languishing in a half-finished
state, with no-one urgently championing their completion. The slow trickle of
features reduces opportunities to make a big public 'splash' upon release,
lessening the impact of our work.

The result is that there is a lack of direction in Rust, both real and
perceieved.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertanty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
mamnagement structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

# Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front, as a project, the most critical problems facing the language, formulated
as _problem statements_. Work toward solving those problems, _goals_, will be
planned in quarter-long cycles by individual teams. _goals_ that result in
stable features will be assigned to _release milestones_ for the purposes of
reporting the project roadmap. Along the way, teams will be expected to maintain
_tracking issues_ that communicate progress toward the project's goals.

The end-of-year retrospective is a 'rallying point'. Its primary purposes are to
create anticipation of a major event in the Rust world, to motivate (rally)
contributors behind the goals we've established to get there, and generate a big
PR-bomb where we can brag to the world about what we've done. It can be thought
of as a 'state of the union'. This is where we tell Rust's story, describe the
new best practices enabled by the new features we've delivered, celebrate those
contributors who helped achieve our goals, honestly evaluate our performance,
and look forward to the year to come.

## Summary of terminology

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together every year
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year.
- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker.
- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those contributors who contribute to achieving the project's goals
  and resolving it's problems.
- _quarterly milestone_ - All goals have estimates for completion, placed on
  quarterly milestones. Each quarter that a goal remains incomplete it must be
  re-triaged and re-estimated by the responsible team.

## The big planning cycle (problem statements and the narrative arc)

The big cycle spans one year. At the beginning of the cycle we identify areas of
Rust that need the most improvement, and at the end of the cycle is a 'rallying
point' where we deliver to the world the results of our efforts. We choose
year-long cycles because a year is enough time to accomplish relatively large
goals; and because having the rallying point occur at the same time every year
makes it easy to know when to anticipate big news from the project.

This planning effort is _problem-oriented_. In our collective experience we have
consistently seen that spending up front effort focusing on motivation - even
when we have strong ideas about the solutions - is a critical step in building
consensus. It avoids surprises and hurt feelings, and establishes a strong causal
record for explaining decisions in the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them.

TODO: How do we talk about solutions during this process? We certainly will have
lots of ideas about how these problems are going to get solved, and we can't
pretend like they don't exist.

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraph describing it in details. Examples of good problem statements
might be:

- The Rust compiler is slow
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is incomplete
- Rust compiler errors are dificult to understand
- Plugins need to be on path to stabilization
- Rust doesn't integrate well with garbage collectors
- Inability to write truly zero-cost abstractions (due to lack of
  specialization) (TODO this is awfully goal-oriented, also not a complete
  sentence)
- We would like the Rust community to be more diverse
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

## The little planning cycle (goals and tracking progress)

TODO: This is the most important part of the RFC mechanically and needs to be
clear so teams can just read it and follow the instructions.

The little cycle is where the solutions take shape and are carried out. They
last one quarter - 3 months - and are the responsibility of individual teams.

Each cycle the teams will have one week to update their set of _goals_. This
includes both creating new goals and reviewing and revising existing goals. A
goal describes a task that contributes to solving the year's problems. It may or
may not involve a concrete deliverable, and it may be in turn subdivided into
further goals.

The social process of the quarterly planning cycle is less strict, but it
should be conducted in a way that allows open feedback. It is suggested that
teams present their quarterly plan on internals.rust-lang.org at the beginning
of the week, solicit feedback, then finalize them at the end of the week.

All goals have estimated completion dates. There is no limit on the duration of
a single goal, but they are encouraged to be scoped to less than a quarter year
of work. Goals that are expected to take more than a quarter _must_ be
subdivided into smaller goals of less than a quarter, each with their own
estimates. These estimates are used to place goals onto quarterly milestones.

Not all the work items done by teams in a quarter should be considered a goal
nor should they be. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that
contributors toward quarterly goals should still be tracked as sub-tasks of
those goals, but only needs to be filed on the issue tracker and not reported
directly as goals on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary (TODO what
makes a good summary?). Goals with sub-goals and sub-tasks must list them in the
OP in a standard format.

During each planning period all goals must be triaged and updated for the
following information:

- The set of sub-goals and sub-tasks and their status
- The estimated date of completion for goals

## The retrospective (rallying point)

- Written for broad public consumption
- Detailed
- Progress toward goals
- Demonstration of new features
- Technical details
- Reinforce the project narrative
- Celebrate contributors who accomplished our goals
- Celebrate the evolution of the ecosystem
- Evaluation of performance, missed goals

TODO How is it constructed?

## Release estimation

The teams are responsible for estimating only the _timeframe_ in which they
complete their work, but possibly the single most important piece of information
desired by users is to know _in what release_ any given feature will become
available.

To reduce process burden on team members we will not require them to make
that estimate themselves, instead a single person will have the responsibility
each quarter to examine the roadmap, its goals and time estimates, and turn
those into release estimates for individual features.

The precise mechanics are to be determined.

## Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain the work items, tagged with metadata
  indicating their statuses.

Alone, this is perhaps sufficient for presenting the roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

We may additionally develop tools to present this information in a more
accessible form (for a prototype see [1]).

[1]: https://brson.github.io/rust-z

## Calendar

The timing of the events specified by this RFC is precisely specified in order
to limit bikeshedding. The activities specified here are not the focus of the
project and we need to get through them efficiently and get on with the actual
work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
RFC by the last week of September. We choose september for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; and the
development of the yearly retrospective approximately for the month of August.

## Summary of mechanics

There are four primary new mechanism introduced by this RFC

- North star RFC. Each year in September the entire project comes together
  to produce this. It is what drives the evolution of the project roadmap
  over the next year.
- `R-problem-statement` tag. The north star RFC defines problem statements that
  are filed and tagged on the issue tracker. The `R-problem-statement` issues in
  turn link to the goals that support them.
- `R-goal`. Reevaluated every quarter by the teams, with feedback from
  the wider community, these are filed on the issue tracker, tagged `R-goal` and
  linked to the `R-problem-statement` issue they support.
- End-of-year retrospective blog post. In the final month we write a detailed
  blog post that hypes up our amazing work.

For simplicity, all `R-problem-statement` and `R-goal` issues live in
rust-lang/rust, even when they primarily entail work on other code-bases.

# Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleast bikeshed. Maybe nobody actually
agrees on the project's direction.

This imposes more work on teams to organize their goals.

There is no mechanism here for presenting the roadmap.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands.

# Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap soley from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
The Rust Platform.

Another rallying point could be a long-term support release.

# Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing?  One of the
problems we have right now is that our release cycles are so predictable they
are boring. It could be more exciting to not know exactly when the cycle is
going to end, to experience the tension of struggling to cross the finish line.

How can we account for work that is not part of the planning process
described here?

How can we avoid adding new tags?

How do we address problems that are outside the scope of the standard library
and compiler itself? Would have used 'the rust platform' and related processes.

How do we motivate the improvement of rust-lang, other libraries?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'.

Likewise, 'goal' and 'retrospective' could be more colorful.

How can we work in an inspiring 'vision statement'?

Can we call the yearly RFC the 'north start RFC'? Too many concepts?

Does the yearly planning really need to be an RFC?

Likewise, _this RFC_ is currently titled 'north-star'.

What about tracking work that is not part of R-problem-statement and R-goal.  I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this does not provide an easy way to find the status of
arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (3359 words)</summary>

````text
# Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the project among contributors, to make clear the roadmap toward that
vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language
and its ecosystem, along with the story we want to be able to tell the world
about Rust. Work toward solving those problems, our short-term goals, will be
decided in quarter-long cycles by individual teams. Goals that result in stable
features will be assigned to release milestones for the purposes of reporting
the project roadmap.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress in The Rust Project toward our goals, as well as
achievements in the wider community. It will celebrate our performance and
anticipate its impact on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

# Motivation
[motivation]: #motivation

Rust is a massive project and ecosystem, developed by a massive team of
mostly-independent contributors. What we've achieved together already is
mind-blowing: we've created a uniquely powerful platform that solves problems
that the computing world had nearly given up on, and jumpstarted a new era in
systems programming. Now that Rust is out in the world, proving itself to be a
stable foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

In the run-up to the release of Rust 1.0 we had a clear, singular goal: get Rust
done and deliver it to the world. We established the discrete steps necessary
to get there, and although it was a tense period where the entire future of the
project was on the line, we were united in a single mission. As The Rust Project
Developers we were pumped up, and our user base - along with the wider
programming world - were excited to see what we would deliver.

But 1.0 is a unique event, and since then our efforts have become more diffuse
even as the scope of our ambitions widen. This shift is inevitable: **our success
post-1.0 depends on making improvements in increasingly broad and complex ways**.
The downside, of course, is that a less singular focus can make it much harder
to rally our efforts, to communicate a clear story - and ultimately, to ship.

Since 1.0, we've attempted to lay out some major goals, both through the
[discuss forum] and the [blog]. We've done pretty well in actually achieving
these goals, and in some cases - particularly [MIR] - the community has really
come together to produce amazing, focused results. But in general, there are
several problems with the status quo:

[discuss forum]: https://internals.rust-lang.org/t/priorities-after-1-0/1901
[blog]: https://blog.rust-lang.org/2015/08/14/Next-year.html
[MIR]: https://blog.rust-lang.org/2016/04/19/MIR.html

- We have not systematically tracked or communicated our progression through the
  completion of these goals, making it difficult for even the most immersed
  community members to know where things stand, and making it difficult for
  *anyone* to know how or where to get involved. A symptom is that questions
  like "When is MIR landing?" or "What are the blockers for `?` stabilizing"
  become extremely frequently-asked. **We should provide an at-a-glance view
  what Rust's current strategic priorities are and how they are progressing.**

- We are overwhelmed by an avalanche of promising ideas, with major RFCs
  demanding attention (and languishing in the queue for months) while subteams
  focus on their strategic goals. This state of affairs produces needless
  friction and loss of momentum. **We should agree on and disseminate our
  priorities, so we can all be pulling in roughly the same direction**.

- We do not have any single point of release, like 1.0, that gathers together a
  large body of community work into a single, polished product. Instead, we have
  a rapid release process, which is a huge boon for
  [stability without stagnation] but can paradoxically reduce pressure to ship
  in a timely fashion. **We should find a balance, retaining rapid release but
  establishing some focal point around which to rally the community, polish a
  product, and establish a clear public narrative**.

[stability without stagnation]: http://blog.rust-lang.org/2014/10/30/Stability.html

All told, there's a lot of room to do better in establishing, communicating, and
driving the vision for Rust.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertanty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
mamnagement structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

# Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front the most critical problems facing the project, formulated as _problem
statements_. Work toward solving those problems, _goals_, will be planned in
quarter-long cycles by individual teams. _Goals_ that result in stable features
will be assigned to _release milestones_ for the purposes of reporting the
project roadmap. Along the way, teams will be expected to maintain _tracking
issues_ that communicate progress toward the project's goals.

The end-of-year retrospective is a 'rallying point'. Its primary purposes are to
create anticipation of a major event in the Rust world, to motivate (rally)
contributors behind the goals we've established to get there, and generate a big
PR-bomb where we can brag to the world about what we've done. It can be thought
of as a 'state of the union'. This is where we tell Rust's story, describe the
new best practices enabled by the new features we've delivered, celebrate those
contributors who helped achieve our goals, honestly evaluate our performance,
and look forward to the year to come.

## Summary of terminology

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together every year
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year.

- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker.

- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those contributors who contribute to achieving the project's goals
  and resolving it's problems.

- _quarterly milestone_ - All goals have estimates for completion, placed on
  quarterly milestones. Each quarter that a goal remains incomplete it must be
  re-triaged and re-estimated by the responsible team.

## The big planning cycle (problem statements and the narrative arc)

The big cycle spans one year. At the beginning of the cycle we identify areas of
Rust that need the most improvement, and at the end of the cycle is a 'rallying
point' where we deliver to the world the results of our efforts. We choose
year-long cycles because a year is enough time to accomplish relatively large
goals; and because having the rallying point occur at the same time every year
makes it easy to know when to anticipate big news from the project. (Being
calendar-based avoids the temptation to slip or produce feature-based releases,
instead providing a fixed point of accountability for shipping.)

This planning effort is _problem-oriented_. Focusing on "why" may seem like an
obvious thing to do, but in practice it's very easy to become enamored of
particular technical ideas and lose sight of the larger context. By codifying a
top-level focus on motivation, we ensure we are focusing on the right problems
and keeping an open mind on how to solve them. Consensus on the problem space
then frames the debate on solutions, helping to avoid surprises and hurt
feelings, and establishing a strong causal record for explaining decisions in
the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them. They should be informed in part by inputs
like [the survey] and [production user outreach], as well as an open discussion
process. And while the end-product is problem-focused, the discussion is likely
to touch on possible solutions as well. We shouldn't blindly commit to solving a
problem without some sense for the plausibility of a solution in terms of both
design and resources.

[the survey]: https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html
[production user outreach]: https://internals.rust-lang.org/t/production-user-research-summary/2530

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraphs describing it (and its importance!) in detail. Examples of
good problem statements might be:

- The Rust compiler is too slow for a tight edit-compile-test cycle
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is very primitive
- Rust compiler errors are dificult to understand
- Rust plugins have no clear path to stabilization
- Rust doesn't integrate well with garbage collectors
- Rust's trait system doesn't fully support zero-cost abstractions
- The Rust community is insufficiently diverse
- Rust needs more training materials
- Rust's CI infrastructure is unstable
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

## The little planning cycle (goals and tracking progress)

The little cycle is where the solutions take shape and are carried out. They
last one quarter - 3 months - and are the responsibility of individual teams.

Each cycle the teams will have one week to update their set of _goals_. This
includes both creating new goals and reviewing and revising existing goals. A
goal describes a task that contributes to solving the year's problems. It may or
may not involve a concrete deliverable, and it may be in turn subdivided into
further goals.

The social process of the quarterly planning cycle is less strict, but it
should be conducted in a way that allows open feedback. It is suggested that
teams present their quarterly plan on internals.rust-lang.org at the beginning
of the week, solicit feedback, then finalize them at the end of the week.

All goals have estimated completion dates. There is no limit on the duration of
a single goal, but they are encouraged to be scoped to less than a quarter year
of work. Goals that are expected to take more than a quarter _must_ be
subdivided into smaller goals of less than a quarter, each with their own
estimates. These estimates are used to place goals onto quarterly milestones.

Not all the work items done by teams in a quarter should be considered a goal
nor should they be. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that
contribute toward quarterly goals should still be tracked as sub-tasks of
those goals, but only needs to be filed on the issue tracker and not reported
directly as goals on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary with a
_deliverable_ that is as crisply stated as possible. Goals with sub-goals and
sub-tasks must list them in the OP in a standard format.

During each planning period all goals must be triaged and updated for the
following information:

- The set of sub-goals and sub-tasks and their status
- The estimated date of completion for goals

## The retrospective (rallying point)

- Written for broad public consumption
- Detailed
- Progress toward goals
- Demonstration of new features
- Technical details
- Reinforce the project narrative
- Celebrate contributors who accomplished our goals
- Celebrate the evolution of the ecosystem
- Evaluation of performance, missed goals

TODO How is it constructed?

## Release estimation

The teams are responsible for estimating only the _timeframe_ in which they
complete their work, but possibly the single most important piece of information
desired by users is to know _in what release_ any given feature will become
available.

To reduce process burden on team members we will not require them to make
that estimate themselves, instead a single person will have the responsibility
each quarter to examine the roadmap, its goals and time estimates, and turn
those into release estimates for individual features.

The precise mechanics are to be determined.

## Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain the work items, tagged with metadata
  indicating their statuses.

Alone, this is perhaps sufficient for presenting the roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

We may additionally develop tools to present this information in a more
accessible form (for a prototype see [1]).

[1]: https://brson.github.io/rust-z

## Calendar

The timing of the events specified by this RFC is precisely specified in order
to limit bikeshedding. The activities specified here are not the focus of the
project and we need to get through them efficiently and get on with the actual
work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
RFC by the last week of September. We choose september for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; and the
development of the yearly retrospective approximately for the month of August.

## Summary of mechanics

There are four primary new mechanism introduced by this RFC

- North star RFC. Each year in September the entire project comes together
  to produce this. It is what drives the evolution of the project roadmap
  over the next year.
- `R-problem-statement` tag. The north star RFC defines problem statements that
  are filed and tagged on the issue tracker. The `R-problem-statement` issues in
  turn link to the goals that support them.
- `R-goal`. Reevaluated every quarter by the teams, with feedback from
  the wider community, these are filed on the issue tracker, tagged `R-goal` and
  linked to the `R-problem-statement` issue they support.
- End-of-year retrospective blog post. In the final month we write a detailed
  blog post that hypes up our amazing work.

For simplicity, all `R-problem-statement` and `R-goal` issues live in
rust-lang/rust, even when they primarily entail work on other code-bases.

# Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleast bikeshed. Maybe nobody actually
agrees on the project's direction.

This imposes more work on teams to organize their goals.

There is no mechanism here for presenting the roadmap.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands.

# Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap soley from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
The Rust Platform.

Another rallying point could be a long-term support release.

# Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing?  One of the
problems we have right now is that our release cycles are so predictable they
are boring. It could be more exciting to not know exactly when the cycle is
going to end, to experience the tension of struggling to cross the finish line.

How can we account for work that is not part of the planning process
described here?

How can we avoid adding new tags?

How do we address problems that are outside the scope of the standard library
and compiler itself? Would have used 'the rust platform' and related processes.

How do we motivate the improvement of rust-lang, other libraries?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'.

Likewise, 'goal' and 'retrospective' could be more colorful.

How can we work in an inspiring 'vision statement'?

Can we call the yearly RFC the 'north start RFC'? Too many concepts?

Does the yearly planning really need to be an RFC?

Likewise, _this RFC_ is currently titled 'north-star'.

What about tracking work that is not part of R-problem-statement and R-goal.  I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this does not provide an easy way to find the status of
arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (3597 words)</summary>

````text
# Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the project among contributors, to make clear the roadmap toward that
vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language
and its ecosystem, along with the story we want to be able to tell the world
about Rust. Work toward solving those problems, our short-term goals, will be
decided in quarter-long cycles by individual teams. For the purposes of
reporting the project roadmap, goals will be assigned to quartely milestones,
and where these goals result in stable features the Rust version in which they
become stable will be estimated as well.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress toward our goals, as well as the achievements of
the wider community. It will evaluate our performance and anticipate its impact
on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

# Motivation
[motivation]: #motivation

Rust is a massive project and ecosystem, developed by a massive team of
mostly-independent contributors. What we've achieved together already is
mind-blowing: we've created a uniquely powerful platform that solves problems
that the computing world had nearly given up on, and jumpstarted a new era in
systems programming. Now that Rust is out in the world, proving itself to be a
stable foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

In the run-up to the release of Rust 1.0 we had a clear, singular goal: get Rust
done and deliver it to the world. We established the discrete steps necessary
to get there, and although it was a tense period where the entire future of the
project was on the line, we were united in a single mission. As The Rust Project
Developers we were pumped up, and our user base - along with the wider
programming world - were excited to see what we would deliver.

But 1.0 is a unique event, and since then our efforts have become more diffuse
even as the scope of our ambitions widen. This shift is inevitable: **our success
post-1.0 depends on making improvements in increasingly broad and complex ways**.
The downside, of course, is that a less singular focus can make it much harder
to rally our efforts, to communicate a clear story - and ultimately, to ship.

Since 1.0, we've attempted to lay out some major goals, both through the
[internals forum] and the [blog]. We've done pretty well in actually achieving
these goals, and in some cases - particularly [MIR] - the community has really
come together to produce amazing, focused results. But in general, there are
several problems with the status quo:

[internals forum]: https://internals.rust-lang.org/t/priorities-after-1-0/1901
[blog]: https://blog.rust-lang.org/2015/08/14/Next-year.html
[MIR]: https://blog.rust-lang.org/2016/04/19/MIR.html

- We have not systematically tracked or communicated our progression through the
  completion of these goals, making it difficult for even the most immersed
  community members to know where things stand, and making it difficult for
  *anyone* to know how or where to get involved. A symptom is that questions
  like "When is MIR landing?" or "What are the blockers for `?` stabilizing"
  become extremely frequently-asked. **We should provide an at-a-glance view
  what Rust's current strategic priorities are and how they are progressing.**

- We are overwhelmed by an avalanche of promising ideas, with major RFCs
  demanding attention (and languishing in the queue for months) while subteams
  focus on their strategic goals. This state of affairs produces needless
  friction and loss of momentum. **We should agree on and disseminate our
  priorities, so we can all be pulling in roughly the same direction**.

- We do not have any single point of release, like 1.0, that gathers together a
  large body of community work into a single, polished product. Instead, we have
  a rapid release process, which results in a [remarkably stable and reliable
  product][s] but can paradoxically reduce pressure to ship new features in a
  timely fashion. **We should find a balance, retaining rapid release but
  establishing some focal point around which to rally the community, polish a
  product, and establish a clear public narrative**.

[s]: http://blog.rust-lang.org/2014/10/30/Stability.html

All told, there's a lot of room to do better in establishing, communicating, and
driving the vision for Rust.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertanty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
mamnagement structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

# Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front the most critical problems facing the project, formulated as _problem
statements_. Work toward solving those problems, _goals_, will be planned in
quarter-long cycles by individual teams. For the purposes of reporting the
project roadmap, goals will be assigned to _quartely milestones_, and where
these goals result in stable features the Rust version in which they become
stable will be estimated as well. Along the way, teams will be expected to
maintain _tracking issues_ that communicate progress toward the project's goals.

At the end of the year we will deliver a public facing retrospective, which is
intended as a 'rallying point'. Its primary purposes are to create anticipation
of a major event in the Rust world, to motivate (rally) contributors behind the
goals we've established to get there, and generate a big PR-bomb where we can
brag to the world about what we've done. It can be thought of as a 'state of the
union'. This is where we tell Rust's story, describe the new best practices
enabled by the new features we've delivered, celebrate those contributors who
helped achieve our goals, honestly evaluate our performance, and look forward to
the year to come.

## Summary of terminology

Key terminology used in this RFC:

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together, every year,
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year, and are
  captured in the yearly "north star RFC", and tagged `R-problem-statement`
  on the issue tracker.

- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker. They are
  tagged `R-goal`.

- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those who contribute to achieving the project's goals and
  resolving it's problems.

- _quarterly milestone_ - All goals have estimates for completion, placed on
  quarterly milestones. Each quarter that a goal remains incomplete it must be
  re-triaged and re-estimated by the responsible team.

## The big planning cycle (problem statements and the north star RFC)

The big cycle spans one year. At the beginning of the cycle we identify areas of
Rust that need the most improvement, and at the end of the cycle is a 'rallying
point' where we deliver to the world the results of our efforts. We choose
year-long cycles because a year is enough time to accomplish relatively large
goals; and because having the rallying point occur at the same time every year
makes it easy to know when to anticipate big news from the project. Being
calendar-based avoids the temptation to slip or produce feature-based releases,
instead providing a fixed point of accountability for shipping.

This planning effort is _problem-oriented_. Focusing on "why" may seem like an
obvious thing to do, but in practice it's very easy to become enamored of
particular technical ideas and lose sight of the larger context. By codifying a
top-level focus on motivation, we ensure we are focusing on the right problems
and keeping an open mind on how to solve them. Consensus on the problem space
then frames the debate on solutions, helping to avoid surprises and hurt
feelings, and establishing a strong causal record for explaining decisions in
the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them. They should be informed in part by inputs
like [the survey] and [production user outreach], as well as an open discussion
process. And while the end-product is problem-focused, the discussion is likely
to touch on possible solutions as well. We shouldn't blindly commit to solving a
problem without some sense for the plausibility of a solution in terms of both
design and resources.

[the survey]: https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html
[production user outreach]: https://internals.rust-lang.org/t/production-user-research-summary/2530

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraphs describing it (and its importance!) in detail. Examples of
good problem statements might be:

- The Rust compiler is too slow for a tight edit-compile-test cycle
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is very primitive
- Rust compiler errors are dificult to understand
- Rust plugins have no clear path to stabilization
- Rust doesn't integrate well with garbage collectors
- Rust's trait system doesn't fully support zero-cost abstractions
- The Rust community is insufficiently diverse
- Rust needs more training materials
- Rust's CI infrastructure is unstable
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

## The little planning cycle (goals and tracking progress)

The little cycle is where the solutions take shape and are carried out. They
last one quarter - 3 months - and are the responsibility of individual teams.

Each cycle the teams will have one week to update their set of _goals_. This
includes both creating new goals and reviewing and revising existing goals. A
goal describes a task that contributes to solving the year's problems. It may or
may not involve a concrete deliverable, and it may be in turn subdivided into
further goals.

The social process of the quarterly planning cycle is less strict, but it
should be conducted in a way that allows open feedback. It is suggested that
teams present their quarterly plan on internals.rust-lang.org at the beginning
of the week, solicit feedback, then finalize them at the end of the week.

All goals have estimated completion dates. There is no limit on the duration of
a single goal, but they are encouraged to be scoped to less than a quarter year
of work. Goals that are expected to take more than a quarter _must_ be
subdivided into smaller goals of less than a quarter, each with their own
estimates. These estimates are used to place goals onto quarterly milestones.

Not all the work items done by teams in a quarter should be considered a goal
nor should they be. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that
contributes toward quarterly goals should still be tracked as sub-tasks of
those goals, but only needs to be filed on the issue tracker and not reported
directly as goals on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary with an
end-result or deliverable that is as crisply stated as possible. Goals with
sub-goals and sub-tasks must list them in the OP in a standard format.

During each planning period all goals must be triaged and updated for the
following information:

- The set of sub-goals and sub-tasks and their status
- The estimated date of completion

## The retrospective (rallying point)

The retrospective is an opportunity to showcase the best of Rust and its
community to the world.

It is a report covering all the Rust activity of the past year. It is written
for a broad audience: contributors, users and non-users alike. It reviews each
of the problems we tackled this year and the goals we achieved toward solving
them, and it highlights important work in the broader community and
ecosystem. For both these things the retrospective provides technical detail, as
though it were primary documentation; this is where we show our best side to the
world. It explains new features in depth, with clear prose and plentiful
examples, and it connects them all thematically, as a demonstration of how to
write cutting-edge Rust code.

While we are always lavish with our praise of contributors, the retrospective is
the best opportunity to celebrate specific individuals and their contributions
toward the strategic interests of the project, as defined way back at the
beginning of the year.

Finally, the retrospective is an opportunity to evaluate our performance. Did we
make progress toward solving the problems we set out to solve? Did we outright
solve any of them? Where did we fail to meet our goals and how might we do
better next year?

Since the retrospective must be a high-quality document, and cover a lot of
material, it is expected to require significant planning, editing and revision.
The details of how this will work are to be determined.

## Release estimation

The teams are responsible for estimating only the _timeframe_ in which they
complete their work, but possibly the single most important piece of information
desired by users is to know _in what release_ any given feature will become
available.

To reduce process burden on team members we will not require them to make
that estimate themselves, instead a single person will have the responsibility
each quarter to examine the roadmap, its goals and time estimates, and turn
those into release estimates for individual features.

The precise mechanics are to be determined.

## Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain the work items, tagged with metadata
  indicating their statuses.

Alone, this is perhaps sufficient for presenting the roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

We may additionally develop tools to present this information in a more
accessible form (for a prototype see [1]).

[1]: https://brson.github.io/rust-z

Again, the details are to be determined.

## Calendar

The timing of the events specified by this RFC is precisely specified in order
to limit bikeshedding. The activities specified here are not the focus of the
project and we need to get through them efficiently and get on with the actual
work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
RFC by the last week of September. We choose september for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; likewise,
the planning for each subsequent quarter at the beginning of the calendar
quarter; and the development of the yearly retrospective approximately for the
month of August.

## References

- [Refining RFCs part 1: Roadmap]
  (https://internals.rust-lang.org/t/refining-rfcs-part-1-roadmap/3656),
  the internals.rust-lang.org thread that spawned this RFC.
- [Post-1.0 priorities thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/priorities-after-1-0/1901).
- [Post-1.0 blog post on project direction]
  (https://blog.rust-lang.org/2015/08/14/Next-year.html).
- [Blog post on MIR]
  (https://blog.rust-lang.org/2016/04/19/MIR.html),
  a large success in strategic community collaboration.
- ["Stability without stagnation"]
  (http://blog.rust-lang.org/2014/10/30/Stability.html),
  outlining Rust's philosophy on rapid iteration while maintaining strong
  stability guarantees.
- [The 2016 state of Rust survey]
  (https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html),
  which indicates promising directions for future work.
- [Production user outreach thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/production-user-research-summary/2530),
  another strong indicator of Rust's needs.
- [rust-z]
  (https://brson.github.io/rust-z),
  a prototype tool to organize the roadmap.

# Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleastant bikeshed. Maybe nobody
actually agrees on the project's direction.

This imposes more work on teams to organize their goals.

There is no mechanism here for presenting the roadmap.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands.

# Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap soley from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
The Rust Platform.

Another rallying point could be a long-term support release.

# Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing?  One of the
problems we have right now is that our release cycles are so predictable they
are boring. It could be more exciting to not know exactly when the cycle is
going to end, to experience the tension of struggling to cross the finish line.

How can we account for work that is not part of the planning process
described here?

How can we avoid adding new tags?

How do we address problems that are outside the scope of the standard library
and compiler itself? Would have used 'the rust platform' and related processes.

How do we motivate the improvement of rust-lang, other libraries?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'.

Likewise, 'goal' and 'retrospective' could be more colorful.

How can we work in an inspiring 'vision statement'?

Can we call the yearly RFC the 'north start RFC'? Too many concepts?

Does the yearly planning really need to be an RFC?

Likewise, _this RFC_ is currently titled 'north-star'.

What about tracking work that is not part of R-problem-statement and R-goal.  I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this does not provide an easy way to find the status of
arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>

<details><summary><b>Step 4 — revision_4</b> (3719 words)</summary>

````text
# Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the project among contributors, to make clear the roadmap toward that
vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language
and its ecosystem, along with the story we want to be able to tell the world
about Rust. Work toward solving those problems, our short-term goals, will be
decided in quarter-long cycles by individual teams. For the purposes of
reporting the project roadmap, goals will be assigned to quartely milestones,
and where these goals result in stable features the Rust version in which they
become stable will be estimated as well.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress toward our goals, as well as the achievements of
the wider community. It will evaluate our performance and anticipate its impact
on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

# Motivation
[motivation]: #motivation

Rust is a massive project and ecosystem, developed by a massive team of
mostly-independent contributors. What we've achieved together already is
mind-blowing: we've created a uniquely powerful platform that solves problems
that the computing world had nearly given up on, and jumpstarted a new era in
systems programming. Now that Rust is out in the world, proving itself to be a
stable foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

In the run-up to the release of Rust 1.0 we had a clear, singular goal: get Rust
done and deliver it to the world. We established the discrete steps necessary
to get there, and although it was a tense period where the entire future of the
project was on the line, we were united in a single mission. As The Rust Project
Developers we were pumped up, and our user base - along with the wider
programming world - were excited to see what we would deliver.

But 1.0 is a unique event, and since then our efforts have become more diffuse
even as the scope of our ambitions widen. This shift is inevitable: **our success
post-1.0 depends on making improvements in increasingly broad and complex ways**.
The downside, of course, is that a less singular focus can make it much harder
to rally our efforts, to communicate a clear story - and ultimately, to ship.

Since 1.0, we've attempted to lay out some major goals, both through the
[internals forum] and the [blog]. We've done pretty well in actually achieving
these goals, and in some cases - particularly [MIR] - the community has really
come together to produce amazing, focused results. But in general, there are
several problems with the status quo:

[internals forum]: https://internals.rust-lang.org/t/priorities-after-1-0/1901
[blog]: https://blog.rust-lang.org/2015/08/14/Next-year.html
[MIR]: https://blog.rust-lang.org/2016/04/19/MIR.html

- We have not systematically tracked or communicated our progression through the
  completion of these goals, making it difficult for even the most immersed
  community members to know where things stand, and making it difficult for
  *anyone* to know how or where to get involved. A symptom is that questions
  like "When is MIR landing?" or "What are the blockers for `?` stabilizing"
  become extremely frequently-asked. **We should provide an at-a-glance view
  what Rust's current strategic priorities are and how they are progressing.**

- We are overwhelmed by an avalanche of promising ideas, with major RFCs
  demanding attention (and languishing in the queue for months) while subteams
  focus on their strategic goals. This state of affairs produces needless
  friction and loss of momentum. **We should agree on and disseminate our
  priorities, so we can all be pulling in roughly the same direction**.

- We do not have any single point of release, like 1.0, that gathers together a
  large body of community work into a single, polished product. Instead, we have
  a rapid release process, which results in a [remarkably stable and reliable
  product][s] but can paradoxically reduce pressure to ship new features in a
  timely fashion. **We should find a balance, retaining rapid release but
  establishing some focal point around which to rally the community, polish a
  product, and establish a clear public narrative**.

[s]: http://blog.rust-lang.org/2014/10/30/Stability.html

All told, there's a lot of room to do better in establishing, communicating, and
driving the vision for Rust.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertanty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
mamnagement structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

# Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front the most critical problems facing the project, formulated as _problem
statements_. Work toward solving those problems, _goals_, will be planned in
quarter-long cycles by individual teams. For the purposes of reporting the
project roadmap, goals will be assigned to _quartely milestones_, and where
these goals result in stable features the Rust version in which they become
stable will be estimated as well. Along the way, teams will be expected to
maintain _tracking issues_ that communicate progress toward the project's goals.

At the end of the year we will deliver a public facing retrospective, which is
intended as a 'rallying point'. Its primary purposes are to create anticipation
of a major event in the Rust world, to motivate (rally) contributors behind the
goals we've established to get there, and generate a big PR-bomb where we can
brag to the world about what we've done. It can be thought of as a 'state of the
union'. This is where we tell Rust's story, describe the new best practices
enabled by the new features we've delivered, celebrate those contributors who
helped achieve our goals, honestly evaluate our performance, and look forward to
the year to come.

## Summary of terminology

Key terminology used in this RFC:

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together, every year,
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year, and are
  captured in the yearly "north star RFC", and tagged `R-problem-statement`
  on the issue tracker.

- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker. They are
  tagged `R-goal`.

- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those who contribute to achieving the project's goals and
  resolving it's problems.

- _quarterly milestone_ - All goals have estimates for completion, placed on
  quarterly milestones. Each quarter that a goal remains incomplete it must be
  re-triaged and re-estimated by the responsible team.

## The big planning cycle (problem statements and the north star RFC)

The big cycle spans one year. At the beginning of the cycle we identify areas of
Rust that need the most improvement, and at the end of the cycle is a 'rallying
point' where we deliver to the world the results of our efforts. We choose
year-long cycles because a year is enough time to accomplish relatively large
goals; and because having the rallying point occur at the same time every year
makes it easy to know when to anticipate big news from the project. Being
calendar-based avoids the temptation to slip or produce feature-based releases,
instead providing a fixed point of accountability for shipping.

This planning effort is _problem-oriented_. Focusing on "why" may seem like an
obvious thing to do, but in practice it's very easy to become enamored of
particular technical ideas and lose sight of the larger context. By codifying a
top-level focus on motivation, we ensure we are focusing on the right problems
and keeping an open mind on how to solve them. Consensus on the problem space
then frames the debate on solutions, helping to avoid surprises and hurt
feelings, and establishing a strong causal record for explaining decisions in
the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them. They should be informed in part by inputs
like [the survey] and [production user outreach], as well as an open discussion
process. And while the end-product is problem-focused, the discussion is likely
to touch on possible solutions as well. We shouldn't blindly commit to solving a
problem without some sense for the plausibility of a solution in terms of both
design and resources.

[the survey]: https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html
[production user outreach]: https://internals.rust-lang.org/t/production-user-research-summary/2530

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraphs describing it (and its importance!) in detail. Examples of
good problem statements might be:

- The Rust compiler is too slow for a tight edit-compile-test cycle
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is very primitive
- Rust compiler errors are dificult to understand
- Rust plugins have no clear path to stabilization
- Rust doesn't integrate well with garbage collectors
- Rust's trait system doesn't fully support zero-cost abstractions
- The Rust community is insufficiently diverse
- Rust needs more training materials
- Rust's CI infrastructure is unstable
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

## The little planning cycle (goals and tracking progress)

The little cycle is where the solutions take shape and are carried out. They
last one quarter - 3 months - and are the responsibility of individual teams.

Each cycle the teams will have one week to update their set of _goals_. This
includes both creating new goals and reviewing and revising existing goals. A
goal describes a task that contributes to solving the year's problems. It may or
may not involve a concrete deliverable, and it may be in turn subdivided into
further goals.

The social process of the quarterly planning cycle is less strict, but it
should be conducted in a way that allows open feedback. It is suggested that
teams present their quarterly plan on internals.rust-lang.org at the beginning
of the week, solicit feedback, then finalize them at the end of the week.

All goals have estimated completion dates. There is no limit on the duration of
a single goal, but they are encouraged to be scoped to less than a quarter year
of work. Goals that are expected to take more than a quarter _must_ be
subdivided into smaller goals of less than a quarter, each with their own
estimates. These estimates are used to place goals onto quarterly milestones.

Not all the work items done by teams in a quarter should be considered a goal
nor should they be. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that
contributes toward quarterly goals should still be tracked as sub-tasks of
those goals, but only needs to be filed on the issue tracker and not reported
directly as goals on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary with an
end-result or deliverable that is as crisply stated as possible. Goals with
sub-goals and sub-tasks must list them in the OP in a standard format.

During each planning period all goals must be triaged and updated for the
following information:

- The set of sub-goals and sub-tasks and their status
- The estimated date of completion

## The retrospective (rallying point)

The retrospective is an opportunity to showcase the best of Rust and its
community to the world.

It is a report covering all the Rust activity of the past year. It is written
for a broad audience: contributors, users and non-users alike. It reviews each
of the problems we tackled this year and the goals we achieved toward solving
them, and it highlights important work in the broader community and
ecosystem. For both these things the retrospective provides technical detail, as
though it were primary documentation; this is where we show our best side to the
world. It explains new features in depth, with clear prose and plentiful
examples, and it connects them all thematically, as a demonstration of how to
write cutting-edge Rust code.

While we are always lavish with our praise of contributors, the retrospective is
the best opportunity to celebrate specific individuals and their contributions
toward the strategic interests of the project, as defined way back at the
beginning of the year.

Finally, the retrospective is an opportunity to evaluate our performance. Did we
make progress toward solving the problems we set out to solve? Did we outright
solve any of them? Where did we fail to meet our goals and how might we do
better next year?

Since the retrospective must be a high-quality document, and cover a lot of
material, it is expected to require significant planning, editing and revision.
The details of how this will work are to be determined.

## Release estimation

The teams are responsible for estimating only the _timeframe_ in which they
complete their work, but possibly the single most important piece of information
desired by users is to know _in what release_ any given feature will become
available.

To reduce process burden on team members we will not require them to make that
estimate themselves; the teams will work purely in terms of quarterly
milestones. Instead, we will have a separate process to map the goals and time
estimates into release estimates for individual features - a process that is
likely automatable.

The precise mechanics are to be determined.

## Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain a hierarchy of work items, tagged with
  metadata indicating their statuses.

Alone, these provide the *raw data* for a roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

However, for the process to be a success, we need to present the roadmap in a
way that is prominent, succinct, and layered with progressive detail. There is a
lot of opportunity for design here; an early prototype of one possible view is
available [here].

[here]: https://brson.github.io/rust-z

Again, the details are to be determined.

## Calendar

The timing of the events specified by this RFC is precisely specified in order
to set clear expectations and accountability, and to avoid process slippage. The
activities specified here are not the focus of the project and we need to get
through them efficiently and get on with the actual work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
RFC by the last week of September. We choose september for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions. By contrast,
starting with Q1 of the calendar year is problematic due to the holiday season.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; likewise,
the planning for each subsequent quarter at the beginning of the calendar
quarter; and the development of the yearly retrospective approximately for the
month of August.

The survey and other forms of outreach and data gathering should be timed to fit
well into the overall calendar.

## References

- [Refining RFCs part 1: Roadmap]
  (https://internals.rust-lang.org/t/refining-rfcs-part-1-roadmap/3656),
  the internals.rust-lang.org thread that spawned this RFC.
- [Post-1.0 priorities thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/priorities-after-1-0/1901).
- [Post-1.0 blog post on project direction]
  (https://blog.rust-lang.org/2015/08/14/Next-year.html).
- [Blog post on MIR]
  (https://blog.rust-lang.org/2016/04/19/MIR.html),
  a large success in strategic community collaboration.
- ["Stability without stagnation"]
  (http://blog.rust-lang.org/2014/10/30/Stability.html),
  outlining Rust's philosophy on rapid iteration while maintaining strong
  stability guarantees.
- [The 2016 state of Rust survey]
  (https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html),
  which indicates promising directions for future work.
- [Production user outreach thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/production-user-research-summary/2530),
  another strong indicator of Rust's needs.
- [rust-z]
  (https://brson.github.io/rust-z),
  a prototype tool to organize the roadmap.

# Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleasant bikeshed, because it
simultaneously raises the stakes of discussion while moving away from concrete
proposals. That said, the *problem* orientation should help facilitate
discussion, and in any case it's vital to be explicit about our values and
prioritization.

While part of the aim of this proposal is to increase the effectiveness of our
team, it also imposes some amount of additional work on everyone. Hopefully the
benefits will outweigh the costs.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands. This is
the piece of the proposal that will probably need the most follow-up work.

# Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap soley from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) idea.

Another rallying point could be a long-term support release.

# Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing? One of the
problems we have right now is that our release cycles are so predictable they
are almost boring. It could be more exciting to not know exactly when the cycle
is going to end, to experience the tension of struggling to cross the finish
line.

How can we account for work that is not part of the planning process
described here?

How do we address problems that are outside the scope of the standard library
and compiler itself? (See
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) for
an alternative aimed at this goal.)

How do we motivate the improvement of rust-lang crates and other libraries? Are
they part of the planning process? The retrospective?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'. Likewise, 'goal' and 'retrospective' could
be more colorful.

Can we call the yearly RFC the 'north start RFC'? Too many concepts?

What about tracking work that is not part of R-problem-statement and R-goal? I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this proposal does not provide an easy way to find the
status of arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>

<details><summary><b>Step 5 — revision_5</b> (3719 words)</summary>

````text
# Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the project among contributors, to make clear the roadmap toward that
vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language
and its ecosystem, along with the story we want to be able to tell the world
about Rust. Work toward solving those problems, our short-term goals, will be
decided in quarter-long cycles by individual teams. For the purposes of
reporting the project roadmap, goals will be assigned to quarterly milestones,
and where these goals result in stable features the Rust version in which they
become stable will be estimated as well.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress toward our goals, as well as the achievements of
the wider community. It will evaluate our performance and anticipate its impact
on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

# Motivation
[motivation]: #motivation

Rust is a massive project and ecosystem, developed by a massive team of
mostly-independent contributors. What we've achieved together already is
mind-blowing: we've created a uniquely powerful platform that solves problems
that the computing world had nearly given up on, and jumpstarted a new era in
systems programming. Now that Rust is out in the world, proving itself to be a
stable foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

In the run-up to the release of Rust 1.0 we had a clear, singular goal: get Rust
done and deliver it to the world. We established the discrete steps necessary
to get there, and although it was a tense period where the entire future of the
project was on the line, we were united in a single mission. As The Rust Project
Developers we were pumped up, and our user base - along with the wider
programming world - were excited to see what we would deliver.

But 1.0 is a unique event, and since then our efforts have become more diffuse
even as the scope of our ambitions widen. This shift is inevitable: **our success
post-1.0 depends on making improvements in increasingly broad and complex ways**.
The downside, of course, is that a less singular focus can make it much harder
to rally our efforts, to communicate a clear story - and ultimately, to ship.

Since 1.0, we've attempted to lay out some major goals, both through the
[internals forum] and the [blog]. We've done pretty well in actually achieving
these goals, and in some cases - particularly [MIR] - the community has really
come together to produce amazing, focused results. But in general, there are
several problems with the status quo:

[internals forum]: https://internals.rust-lang.org/t/priorities-after-1-0/1901
[blog]: https://blog.rust-lang.org/2015/08/14/Next-year.html
[MIR]: https://blog.rust-lang.org/2016/04/19/MIR.html

- We have not systematically tracked or communicated our progression through the
  completion of these goals, making it difficult for even the most immersed
  community members to know where things stand, and making it difficult for
  *anyone* to know how or where to get involved. A symptom is that questions
  like "When is MIR landing?" or "What are the blockers for `?` stabilizing"
  become extremely frequently-asked. **We should provide an at-a-glance view
  what Rust's current strategic priorities are and how they are progressing.**

- We are overwhelmed by an avalanche of promising ideas, with major RFCs
  demanding attention (and languishing in the queue for months) while subteams
  focus on their strategic goals. This state of affairs produces needless
  friction and loss of momentum. **We should agree on and disseminate our
  priorities, so we can all be pulling in roughly the same direction**.

- We do not have any single point of release, like 1.0, that gathers together a
  large body of community work into a single, polished product. Instead, we have
  a rapid release process, which results in a [remarkably stable and reliable
  product][s] but can paradoxically reduce pressure to ship new features in a
  timely fashion. **We should find a balance, retaining rapid release but
  establishing some focal point around which to rally the community, polish a
  product, and establish a clear public narrative**.

[s]: http://blog.rust-lang.org/2014/10/30/Stability.html

All told, there's a lot of room to do better in establishing, communicating, and
driving the vision for Rust.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertainty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
management structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

# Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front the most critical problems facing the project, formulated as _problem
statements_. Work toward solving those problems, _goals_, will be planned in
quarter-long cycles by individual teams. For the purposes of reporting the
project roadmap, goals will be assigned to _quarterly milestones_, and where
these goals result in stable features the Rust version in which they become
stable will be estimated as well. Along the way, teams will be expected to
maintain _tracking issues_ that communicate progress toward the project's goals.

At the end of the year we will deliver a public facing retrospective, which is
intended as a 'rallying point'. Its primary purposes are to create anticipation
of a major event in the Rust world, to motivate (rally) contributors behind the
goals we've established to get there, and generate a big PR-bomb where we can
brag to the world about what we've done. It can be thought of as a 'state of the
union'. This is where we tell Rust's story, describe the new best practices
enabled by the new features we've delivered, celebrate those contributors who
helped achieve our goals, honestly evaluate our performance, and look forward to
the year to come.

## Summary of terminology

Key terminology used in this RFC:

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together, every year,
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year, and are
  captured in the yearly "north star RFC", and tagged `R-problem-statement`
  on the issue tracker.

- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker. They are
  tagged `R-goal`.

- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those who contribute to achieving the project's goals and
  resolving it's problems.

- _quarterly milestone_ - All goals have estimates for completion, placed on
  quarterly milestones. Each quarter that a goal remains incomplete it must be
  re-triaged and re-estimated by the responsible team.

## The big planning cycle (problem statements and the north star RFC)

The big cycle spans one year. At the beginning of the cycle we identify areas of
Rust that need the most improvement, and at the end of the cycle is a 'rallying
point' where we deliver to the world the results of our efforts. We choose
year-long cycles because a year is enough time to accomplish relatively large
goals; and because having the rallying point occur at the same time every year
makes it easy to know when to anticipate big news from the project. Being
calendar-based avoids the temptation to slip or produce feature-based releases,
instead providing a fixed point of accountability for shipping.

This planning effort is _problem-oriented_. Focusing on "why" may seem like an
obvious thing to do, but in practice it's very easy to become enamored of
particular technical ideas and lose sight of the larger context. By codifying a
top-level focus on motivation, we ensure we are focusing on the right problems
and keeping an open mind on how to solve them. Consensus on the problem space
then frames the debate on solutions, helping to avoid surprises and hurt
feelings, and establishing a strong causal record for explaining decisions in
the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them. They should be informed in part by inputs
like [the survey] and [production user outreach], as well as an open discussion
process. And while the end-product is problem-focused, the discussion is likely
to touch on possible solutions as well. We shouldn't blindly commit to solving a
problem without some sense for the plausibility of a solution in terms of both
design and resources.

[the survey]: https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html
[production user outreach]: https://internals.rust-lang.org/t/production-user-research-summary/2530

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraphs describing it (and its importance!) in detail. Examples of
good problem statements might be:

- The Rust compiler is too slow for a tight edit-compile-test cycle
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is very primitive
- Rust compiler errors are difficult to understand
- Rust plugins have no clear path to stabilization
- Rust doesn't integrate well with garbage collectors
- Rust's trait system doesn't fully support zero-cost abstractions
- The Rust community is insufficiently diverse
- Rust needs more training materials
- Rust's CI infrastructure is unstable
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

## The little planning cycle (goals and tracking progress)

The little cycle is where the solutions take shape and are carried out. They
last one quarter - 3 months - and are the responsibility of individual teams.

Each cycle the teams will have one week to update their set of _goals_. This
includes both creating new goals and reviewing and revising existing goals. A
goal describes a task that contributes to solving the year's problems. It may or
may not involve a concrete deliverable, and it may be in turn subdivided into
further goals.

The social process of the quarterly planning cycle is less strict, but it
should be conducted in a way that allows open feedback. It is suggested that
teams present their quarterly plan on internals.rust-lang.org at the beginning
of the week, solicit feedback, then finalize them at the end of the week.

All goals have estimated completion dates. There is no limit on the duration of
a single goal, but they are encouraged to be scoped to less than a quarter year
of work. Goals that are expected to take more than a quarter _must_ be
subdivided into smaller goals of less than a quarter, each with their own
estimates. These estimates are used to place goals onto quarterly milestones.

Not all the work items done by teams in a quarter should be considered a goal
nor should they be. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that
contributes toward quarterly goals should still be tracked as sub-tasks of
those goals, but only needs to be filed on the issue tracker and not reported
directly as goals on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary with an
end-result or deliverable that is as crisply stated as possible. Goals with
sub-goals and sub-tasks must list them in the OP in a standard format.

During each planning period all goals must be triaged and updated for the
following information:

- The set of sub-goals and sub-tasks and their status
- The estimated date of completion

## The retrospective (rallying point)

The retrospective is an opportunity to showcase the best of Rust and its
community to the world.

It is a report covering all the Rust activity of the past year. It is written
for a broad audience: contributors, users and non-users alike. It reviews each
of the problems we tackled this year and the goals we achieved toward solving
them, and it highlights important work in the broader community and
ecosystem. For both these things the retrospective provides technical detail, as
though it were primary documentation; this is where we show our best side to the
world. It explains new features in depth, with clear prose and plentiful
examples, and it connects them all thematically, as a demonstration of how to
write cutting-edge Rust code.

While we are always lavish with our praise of contributors, the retrospective is
the best opportunity to celebrate specific individuals and their contributions
toward the strategic interests of the project, as defined way back at the
beginning of the year.

Finally, the retrospective is an opportunity to evaluate our performance. Did we
make progress toward solving the problems we set out to solve? Did we outright
solve any of them? Where did we fail to meet our goals and how might we do
better next year?

Since the retrospective must be a high-quality document, and cover a lot of
material, it is expected to require significant planning, editing and revision.
The details of how this will work are to be determined.

## Release estimation

The teams are responsible for estimating only the _timeframe_ in which they
complete their work, but possibly the single most important piece of information
desired by users is to know _in what release_ any given feature will become
available.

To reduce process burden on team members we will not require them to make that
estimate themselves; the teams will work purely in terms of quarterly
milestones. Instead, we will have a separate process to map the goals and time
estimates into release estimates for individual features - a process that is
likely automatable.

The precise mechanics are to be determined.

## Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain a hierarchy of work items, tagged with
  metadata indicating their statuses.

Alone, these provide the *raw data* for a roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

However, for the process to be a success, we need to present the roadmap in a
way that is prominent, succinct, and layered with progressive detail. There is a
lot of opportunity for design here; an early prototype of one possible view is
available [here].

[here]: https://brson.github.io/rust-z

Again, the details are to be determined.

## Calendar

The timing of the events specified by this RFC is precisely specified in order
to set clear expectations and accountability, and to avoid process slippage. The
activities specified here are not the focus of the project and we need to get
through them efficiently and get on with the actual work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
FCP by the last week of September. We choose September for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions. By contrast,
starting with Q1 of the calendar year is problematic due to the holiday season.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; likewise,
the planning for each subsequent quarter at the beginning of the calendar
quarter; and the development of the yearly retrospective approximately for the
month of August.

The survey and other forms of outreach and data gathering should be timed to fit
well into the overall calendar.

## References

- [Refining RFCs part 1: Roadmap]
  (https://internals.rust-lang.org/t/refining-rfcs-part-1-roadmap/3656),
  the internals.rust-lang.org thread that spawned this RFC.
- [Post-1.0 priorities thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/priorities-after-1-0/1901).
- [Post-1.0 blog post on project direction]
  (https://blog.rust-lang.org/2015/08/14/Next-year.html).
- [Blog post on MIR]
  (https://blog.rust-lang.org/2016/04/19/MIR.html),
  a large success in strategic community collaboration.
- ["Stability without stagnation"]
  (http://blog.rust-lang.org/2014/10/30/Stability.html),
  outlining Rust's philosophy on rapid iteration while maintaining strong
  stability guarantees.
- [The 2016 state of Rust survey]
  (https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html),
  which indicates promising directions for future work.
- [Production user outreach thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/production-user-research-summary/2530),
  another strong indicator of Rust's needs.
- [rust-z]
  (https://brson.github.io/rust-z),
  a prototype tool to organize the roadmap.

# Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleasant bikeshed, because it
simultaneously raises the stakes of discussion while moving away from concrete
proposals. That said, the *problem* orientation should help facilitate
discussion, and in any case it's vital to be explicit about our values and
prioritization.

While part of the aim of this proposal is to increase the effectiveness of our
team, it also imposes some amount of additional work on everyone. Hopefully the
benefits will outweigh the costs.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands. This is
the piece of the proposal that will probably need the most follow-up work.

# Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap solely from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) idea.

Another rallying point could be a long-term support release.

# Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing? One of the
problems we have right now is that our release cycles are so predictable they
are almost boring. It could be more exciting to not know exactly when the cycle
is going to end, to experience the tension of struggling to cross the finish
line.

How can we account for work that is not part of the planning process
described here?

How do we address problems that are outside the scope of the standard library
and compiler itself? (See
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) for
an alternative aimed at this goal.)

How do we motivate the improvement of rust-lang crates and other libraries? Are
they part of the planning process? The retrospective?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'. Likewise, 'goal' and 'retrospective' could
be more colorful.

Can we call the yearly RFC the 'north star RFC'? Too many concepts?

What about tracking work that is not part of R-problem-statement and R-goal? I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this proposal does not provide an easy way to find the
status of arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>

<details><summary><b>Step 6 — revision_6</b> (3733 words)</summary>

````text
# Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the project among contributors, to make clear the roadmap toward that
vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language
and its ecosystem, along with the story we want to be able to tell the world
about Rust. Work toward solving those problems, our short-term goals, will be
decided in quarter-long cycles by individual teams. For the purposes of
reporting the project roadmap, goals will be assigned to quarterly milestones,
and where these goals result in stable features the Rust version in which they
become stable will be estimated as well.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress toward our goals, as well as the achievements of
the wider community. It will evaluate our performance and anticipate its impact
on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

# Motivation
[motivation]: #motivation

Rust is a massive project and ecosystem, developed by a massive team of
mostly-independent contributors. What we've achieved together already is
mind-blowing: we've created a uniquely powerful platform that solves problems
that the computing world had nearly given up on, and jumpstarted a new era in
systems programming. Now that Rust is out in the world, proving itself to be a
stable foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

In the run-up to the release of Rust 1.0 we had a clear, singular goal: get Rust
done and deliver it to the world. We established the discrete steps necessary
to get there, and although it was a tense period where the entire future of the
project was on the line, we were united in a single mission. As The Rust Project
Developers we were pumped up, and our user base - along with the wider
programming world - were excited to see what we would deliver.

But 1.0 is a unique event, and since then our efforts have become more diffuse
even as the scope of our ambitions widen. This shift is inevitable: **our success
post-1.0 depends on making improvements in increasingly broad and complex ways**.
The downside, of course, is that a less singular focus can make it much harder
to rally our efforts, to communicate a clear story - and ultimately, to ship.

Since 1.0, we've attempted to lay out some major goals, both through the
[internals forum] and the [blog]. We've done pretty well in actually achieving
these goals, and in some cases - particularly [MIR] - the community has really
come together to produce amazing, focused results. But in general, there are
several problems with the status quo:

[internals forum]: https://internals.rust-lang.org/t/priorities-after-1-0/1901
[blog]: https://blog.rust-lang.org/2015/08/14/Next-year.html
[MIR]: https://blog.rust-lang.org/2016/04/19/MIR.html

- We have not systematically tracked or communicated our progression through the
  completion of these goals, making it difficult for even the most immersed
  community members to know where things stand, and making it difficult for
  *anyone* to know how or where to get involved. A symptom is that questions
  like "When is MIR landing?" or "What are the blockers for `?` stabilizing"
  become extremely frequently-asked. **We should provide an at-a-glance view
  what Rust's current strategic priorities are and how they are progressing.**

- We are overwhelmed by an avalanche of promising ideas, with major RFCs
  demanding attention (and languishing in the queue for months) while subteams
  focus on their strategic goals. This state of affairs produces needless
  friction and loss of momentum. **We should agree on and disseminate our
  priorities, so we can all be pulling in roughly the same direction**.

- We do not have any single point of release, like 1.0, that gathers together a
  large body of community work into a single, polished product. Instead, we have
  a rapid release process, which results in a [remarkably stable and reliable
  product][s] but can paradoxically reduce pressure to ship new features in a
  timely fashion. **We should find a balance, retaining rapid release but
  establishing some focal point around which to rally the community, polish a
  product, and establish a clear public narrative**.

[s]: http://blog.rust-lang.org/2014/10/30/Stability.html

All told, there's a lot of room to do better in establishing, communicating, and
driving the vision for Rust.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertainty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
management structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

# Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front the most critical problems facing the project, formulated as _problem
statements_. Work toward solving those problems, _goals_, will be planned in
quarter-long cycles by individual teams. For the purposes of reporting the
project roadmap, goals will be assigned to _quarterly milestones_, and where
these goals result in stable features the Rust version in which they become
stable will be estimated as well. Along the way, teams will be expected to
maintain _tracking issues_ that communicate progress toward the project's goals.

At the end of the year we will deliver a public facing retrospective, which is
intended as a 'rallying point'. Its primary purposes are to create anticipation
of a major event in the Rust world, to motivate (rally) contributors behind the
goals we've established to get there, and generate a big PR-bomb where we can
brag to the world about what we've done. It can be thought of as a 'state of the
union'. This is where we tell Rust's story, describe the new best practices
enabled by the new features we've delivered, celebrate those contributors who
helped achieve our goals, honestly evaluate our performance, and look forward to
the year to come.

## Summary of terminology

Key terminology used in this RFC:

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together, every year,
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year, and are
  captured in the yearly "north star RFC", and tagged `R-problem-statement`
  on the issue tracker.

- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker. They are
  tagged `R-goal`.

- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those who contribute to achieving the project's goals and
  resolving it's problems.

- _quarterly milestone_ - All goals have estimates for completion, placed on
  quarterly milestones. Each quarter that a goal remains incomplete it must be
  re-triaged and re-estimated by the responsible team.

## The big planning cycle (problem statements and the north star RFC)

The big cycle spans one year. At the beginning of the cycle we identify areas of
Rust that need the most improvement, and at the end of the cycle is a 'rallying
point' where we deliver to the world the results of our efforts. We choose
year-long cycles because a year is enough time to accomplish relatively large
goals; and because having the rallying point occur at the same time every year
makes it easy to know when to anticipate big news from the project. Being
calendar-based avoids the temptation to slip or produce feature-based releases,
instead providing a fixed point of accountability for shipping.

This planning effort is _problem-oriented_. Focusing on "how" may seem like an
obvious thing to do, but in practice it's very easy to become enamored of
particular technical ideas and lose sight of the larger context. By codifying a
top-level focus on motivation, we ensure we are focusing on the right problems
and keeping an open mind on how to solve them. Consensus on the problem space
then frames the debate on solutions, helping to avoid surprises and hurt
feelings, and establishing a strong causal record for explaining decisions in
the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them. They should be informed in part by inputs
like [the survey] and [production user outreach], as well as an open discussion
process. And while the end-product is problem-focused, the discussion is likely
to touch on possible solutions as well. We shouldn't blindly commit to solving a
problem without some sense for the plausibility of a solution in terms of both
design and resources.

[the survey]: https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html
[production user outreach]: https://internals.rust-lang.org/t/production-user-research-summary/2530

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraphs describing it (and its importance!) in detail. Examples of
good problem statements might be:

- The Rust compiler is too slow for a tight edit-compile-test cycle
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is very primitive
- Rust compiler errors are difficult to understand
- Rust plugins have no clear path to stabilization
- Rust doesn't integrate well with garbage collectors
- Rust's trait system doesn't fully support zero-cost abstractions
- The Rust community is insufficiently diverse
- Rust needs more training materials
- Rust's CI infrastructure is unstable
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

## The little planning cycle (goals and tracking progress)

The little cycle is where the solutions take shape and are carried out. They
last one quarter - 3 months - and are the responsibility of individual teams.

Each cycle the teams will have one week to update their set of _goals_. This
includes both creating new goals and reviewing and revising existing goals. A
goal describes a task that contributes to solving the year's problems. It may or
may not involve a concrete deliverable, and it may be in turn subdivided into
further goals.

The social process of the quarterly planning cycle is less strict, but it
should be conducted in a way that allows open feedback. It is suggested that
teams present their quarterly plan on internals.rust-lang.org at the beginning
of the week, solicit feedback, then finalize them at the end of the week.

All goals have estimated completion dates. There is no limit on the duration of
a single goal, but they are encouraged to be scoped to less than a quarter year
of work. Goals that are expected to take more than a quarter _must_ be
subdivided into smaller goals of less than a quarter, each with their own
estimates. These estimates are used to place goals onto quarterly milestones.

Not all the work items done by teams in a quarter should be considered a goal
nor should they be. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that
contributes toward quarterly goals should still be tracked as sub-tasks of
those goals, but only needs to be filed on the issue tracker and not reported
directly as goals on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary with an
end-result or deliverable that is as crisply stated as possible. Goals with
sub-goals and sub-tasks must list them in the OP in a standard format.

During each planning period all goals must be triaged and updated for the
following information:

- The set of sub-goals and sub-tasks and their status
- The estimated date of completion

## The retrospective (rallying point)

The retrospective is an opportunity to showcase the best of Rust and its
community to the world.

It is a report covering all the Rust activity of the past year. It is written
for a broad audience: contributors, users and non-users alike. It reviews each
of the problems we tackled this year and the goals we achieved toward solving
them, and it highlights important work in the broader community and
ecosystem. For both these things the retrospective provides technical detail, as
though it were primary documentation; this is where we show our best side to the
world. It explains new features in depth, with clear prose and plentiful
examples, and it connects them all thematically, as a demonstration of how to
write cutting-edge Rust code.

While we are always lavish with our praise of contributors, the retrospective is
the best opportunity to celebrate specific individuals and their contributions
toward the strategic interests of the project, as defined way back at the
beginning of the year.

Finally, the retrospective is an opportunity to evaluate our performance. Did we
make progress toward solving the problems we set out to solve? Did we outright
solve any of them? Where did we fail to meet our goals and how might we do
better next year?

Since the retrospective must be a high-quality document, and cover a lot of
material, it is expected to require significant planning, editing and revision.
The details of how this will work are to be determined.

## Release estimation

The teams are responsible for estimating only the _timeframe_ in which they
complete their work, but possibly the single most important piece of information
desired by users is to know _in what release_ any given feature will become
available.

To reduce process burden on team members we will not require them to make that
estimate themselves; the teams will work purely in terms of quarterly
milestones. Instead, we will have a separate process to map the goals and time
estimates into release estimates for individual features - a process that is
likely automatable.

The precise mechanics are to be determined.

## Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain a hierarchy of work items, tagged with
  metadata indicating their statuses.

Alone, these provide the *raw data* for a roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

However, for the process to be a success, we need to present the roadmap in a
way that is prominent, succinct, and layered with progressive detail. There is a
lot of opportunity for design here; an early prototype of one possible view is
available [here].

[here]: https://brson.github.io/rust-z

Again, the details are to be determined.

## Calendar

The timing of the events specified by this RFC is precisely specified in order
to set clear expectations and accountability, and to avoid process slippage. The
activities specified here are not the focus of the project and we need to get
through them efficiently and get on with the actual work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
FCP by the last week of September. We choose September for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions. By contrast,
starting with Q1 of the calendar year is problematic due to the holiday season.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; likewise,
the planning for each subsequent quarter at the beginning of the calendar
quarter; and the development of the yearly retrospective approximately for the
month of August.

The survey and other forms of outreach and data gathering should be timed to fit
well into the overall calendar.

## References

- [Refining RFCs part 1: Roadmap]
  (https://internals.rust-lang.org/t/refining-rfcs-part-1-roadmap/3656),
  the internals.rust-lang.org thread that spawned this RFC.
- [Post-1.0 priorities thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/priorities-after-1-0/1901).
- [Post-1.0 blog post on project direction]
  (https://blog.rust-lang.org/2015/08/14/Next-year.html).
- [Blog post on MIR]
  (https://blog.rust-lang.org/2016/04/19/MIR.html),
  a large success in strategic community collaboration.
- ["Stability without stagnation"]
  (http://blog.rust-lang.org/2014/10/30/Stability.html),
  outlining Rust's philosophy on rapid iteration while maintaining strong
  stability guarantees.
- [The 2016 state of Rust survey]
  (https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html),
  which indicates promising directions for future work.
- [Production user outreach thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/production-user-research-summary/2530),
  another strong indicator of Rust's needs.
- [rust-z]
  (https://brson.github.io/rust-z),
  a prototype tool to organize the roadmap.

# Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleasant bikeshed, because it
simultaneously raises the stakes of discussion while moving away from concrete
proposals. That said, the *problem* orientation should help facilitate
discussion, and in any case it's vital to be explicit about our values and
prioritization.

While part of the aim of this proposal is to increase the effectiveness of our
team, it also imposes some amount of additional work on everyone. Hopefully the
benefits will outweigh the costs.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands. This is
the piece of the proposal that will probably need the most follow-up work.

# Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap solely from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) idea.

Another rallying point could be a long-term support release.

# Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Are 1 year cycles too long? What happens if important problems come up
mid-cycle?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing? One of the
problems we have right now is that our release cycles are so predictable they
are almost boring. It could be more exciting to not know exactly when the cycle
is going to end, to experience the tension of struggling to cross the finish
line.

How can we account for work that is not part of the planning process
described here?

How do we address problems that are outside the scope of the standard library
and compiler itself? (See
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) for
an alternative aimed at this goal.)

How do we motivate the improvement of rust-lang crates and other libraries? Are
they part of the planning process? The retrospective?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'. Likewise, 'goal' and 'retrospective' could
be more colorful.

Can we call the yearly RFC the 'north star RFC'? Too many concepts?

What about tracking work that is not part of R-problem-statement and R-goal? I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this proposal does not provide an easy way to find the
status of arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>

<details><summary><b>Step 7 — revision_7</b> (3808 words)</summary>

````text
# Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the project among contributors, to make clear the roadmap toward that
vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language
and its ecosystem, along with the story we want to be able to tell the world
about Rust. Work toward solving those problems, our short-term goals, will be
decided by the individual teams, as they see fit, and regularly re-triaged. For
the purposes of reporting the project roadmap, goals will be assigned to release
cycle milestones.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress toward our goals, as well as the achievements of
the wider community. It will evaluate our performance and anticipate its impact
on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

# Motivation
[motivation]: #motivation

Rust is a massive project and ecosystem, developed by a massive team of
mostly-independent contributors. What we've achieved together already is
mind-blowing: we've created a uniquely powerful platform that solves problems
that the computing world had nearly given up on, and jumpstarted a new era in
systems programming. Now that Rust is out in the world, proving itself to be a
stable foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

In the run-up to the release of Rust 1.0 we had a clear, singular goal: get Rust
done and deliver it to the world. We established the discrete steps necessary
to get there, and although it was a tense period where the entire future of the
project was on the line, we were united in a single mission. As The Rust Project
Developers we were pumped up, and our user base - along with the wider
programming world - were excited to see what we would deliver.

But 1.0 is a unique event, and since then our efforts have become more diffuse
even as the scope of our ambitions widen. This shift is inevitable: **our success
post-1.0 depends on making improvements in increasingly broad and complex ways**.
The downside, of course, is that a less singular focus can make it much harder
to rally our efforts, to communicate a clear story - and ultimately, to ship.

Since 1.0, we've attempted to lay out some major goals, both through the
[internals forum] and the [blog]. We've done pretty well in actually achieving
these goals, and in some cases - particularly [MIR] - the community has really
come together to produce amazing, focused results. But in general, there are
several problems with the status quo:

[internals forum]: https://internals.rust-lang.org/t/priorities-after-1-0/1901
[blog]: https://blog.rust-lang.org/2015/08/14/Next-year.html
[MIR]: https://blog.rust-lang.org/2016/04/19/MIR.html

- We have not systematically tracked or communicated our progression through the
  completion of these goals, making it difficult for even the most immersed
  community members to know where things stand, and making it difficult for
  *anyone* to know how or where to get involved. A symptom is that questions
  like "When is MIR landing?" or "What are the blockers for `?` stabilizing"
  become extremely frequently-asked. **We should provide an at-a-glance view
  what Rust's current strategic priorities are and how they are progressing.**

- We are overwhelmed by an avalanche of promising ideas, with major RFCs
  demanding attention (and languishing in the queue for months) while subteams
  focus on their strategic goals. This state of affairs produces needless
  friction and loss of momentum. **We should agree on and disseminate our
  priorities, so we can all be pulling in roughly the same direction**.

- We do not have any single point of release, like 1.0, that gathers together a
  large body of community work into a single, polished product. Instead, we have
  a rapid release process, which results in a [remarkably stable and reliable
  product][s] but can paradoxically reduce pressure to ship new features in a
  timely fashion. **We should find a balance, retaining rapid release but
  establishing some focal point around which to rally the community, polish a
  product, and establish a clear public narrative**.

[s]: http://blog.rust-lang.org/2014/10/30/Stability.html

All told, there's a lot of room to do better in establishing, communicating, and
driving the vision for Rust.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertainty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
management structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

# Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front the most critical problems facing the project, formulated as _problem
statements_. Work toward solving those problems, _goals_, will be planned as
part of the release cycles by individual teams. For the purposes of reporting
the project roadmap, goals will be assigned to _release cycle milestones_, which
represent the primary work performed each release cycle. Along the way, teams
will be expected to maintain _tracking issues_ that communicate progress toward
the project's goals.

At the end of the year we will deliver a public facing retrospective, which is
intended as a 'rallying point'. Its primary purposes are to create anticipation
of a major event in the Rust world, to motivate (rally) contributors behind the
goals we've established to get there, and generate a big PR-bomb where we can
brag to the world about what we've done. It can be thought of as a 'state of the
union'. This is where we tell Rust's story, describe the new best practices
enabled by the new features we've delivered, celebrate those contributors who
helped achieve our goals, honestly evaluate our performance, and look forward to
the year to come.

## Summary of terminology

Key terminology used in this RFC:

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together, every year,
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year, and are
  captured in the yearly "north star RFC", and tagged `R-problem-statement`
  on the issue tracker.

- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker. They are
  tagged `R-goal`.

- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those who contribute to achieving the project's goals and
  resolving it's problems.

- _release cycle milestone_ - All goals have estimates for completion, placed on
  milestones that correspond to the 6 week release cycle. These milestones are
  timed to corrspond to a release cycle, but don't represent a specific
  release. That is, work toward the current nightly, the current beta, or even
  that doesn't directly impact a specific release, all goes into the release
  cycle milestone corresponding to the time period in which the work is
  completed.

## Problem statements and the north star RFC

The full planning cycle spans one year. At the beginning of the cycle we
identify areas of Rust that need the most improvement, and at the end of the
cycle is a 'rallying point' where we deliver to the world the results of our
efforts. We choose year-long cycles because a year is enough time to accomplish
relatively large goals; and because having the rallying point occur at the same
time every year makes it easy to know when to anticipate big news from the
project. Being calendar-based avoids the temptation to slip or produce
feature-based releases, instead providing a fixed point of accountability for
shipping.

This planning effort is _problem-oriented_. Focusing on "how" may seem like an
obvious thing to do, but in practice it's very easy to become enamored of
particular technical ideas and lose sight of the larger context. By codifying a
top-level focus on motivation, we ensure we are focusing on the right problems
and keeping an open mind on how to solve them. Consensus on the problem space
then frames the debate on solutions, helping to avoid surprises and hurt
feelings, and establishing a strong causal record for explaining decisions in
the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them. They should be informed in part by inputs
like [the survey] and [production user outreach], as well as an open discussion
process. And while the end-product is problem-focused, the discussion is likely
to touch on possible solutions as well. We shouldn't blindly commit to solving a
problem without some sense for the plausibility of a solution in terms of both
design and resources.

[the survey]: https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html
[production user outreach]: https://internals.rust-lang.org/t/production-user-research-summary/2530

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraphs describing it (and its importance!) in detail. Examples of
good problem statements might be:

- The Rust compiler is too slow for a tight edit-compile-test cycle
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is very primitive
- Rust compiler errors are difficult to understand
- Rust plugins have no clear path to stabilization
- Rust doesn't integrate well with garbage collectors
- Rust's trait system doesn't fully support zero-cost abstractions
- The Rust community is insufficiently diverse
- Rust needs more training materials
- Rust's CI infrastructure is unstable
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

Like other RFCs, the north star RFC is not immutable, and if new motivations
arise during the year, it may be amended, even to the extent of adding
additional problem statements; though it is not appropriate for the project
to continually rehash the RFC.

## Goal setting and tracking progress

During the regular 6-week release cycles is where the solutions take shape and
are carried out. Each cycle teams are expected to set concrete _goals_ that work
toward solving the project's stated problems; and to review and revise their
previous goals. The exact forum and mechanism for doing this evaluation and
goal-setting is left to the individual teams, and to future experimentation,
but the end result is that each release cycle each team will document their
goals and progress in a standard format.

A goal describes a task that contributes to solving the year's problems. It may
or may not involve a concrete deliverable, and it may be in turn subdivided into
further goals. Not all the work items done by teams in a quarter should be
considered a goal. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that contributes
toward quarterly goals should still be tracked as sub-tasks of those goals, but
only needs to be filed on the issue tracker and not reported directly as goals
on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary with an
end-result or deliverable that is as crisply stated as possible. Goals with
sub-goals and sub-tasks must list them in the OP in a standard format.

During each cycle all `R-goal` and `R-unstable` issues assigned to each team
must be triaged and updated for the following information:

- The set of sub-goals and sub-tasks and their status
- The release cycle milestone

Goals that will be likely completed in this cycle or the next should be assigned
to the appropriate milestone. Some goals may be expected to be completed in
the distant future, and these do not need to be assigned a milestone.

The release cycle milestone corresponds to a six week period of time and
contains the work done during that time. It does not correspend to a specific
release, nor do the goals assigned to it need to result in a stable feature
landing in any specific release.

Release cycle milestones serve multiple purposes, not just tracking of the goals
defined in this RFC: `R-goal` tracking, tracking of stabilization of
`R-unstable` and `R-RFC-approved` features, tracking of critical bug fixes.

Though the release cycle milestones are time-oriented and are not strictly tied
to a single upcoming release, from the set of assigned `R-unstable` issues one
can derive the new features landing in upcoming releases.

During the last week of every release cycle each team will write a brief
report summarizing their goal progress for the cycle. Some project member
will compile all the team reports and post them to internals.rust-lang.org.
In addition to providing visibility into progress, these will be sources
to draw from for the subsequent release announcements.

## The retrospective (rallying point)

The retrospective is an opportunity to showcase the best of Rust and its
community to the world.

It is a report covering all the Rust activity of the past year. It is written
for a broad audience: contributors, users and non-users alike. It reviews each
of the problems we tackled this year and the goals we achieved toward solving
them, and it highlights important work in the broader community and
ecosystem. For both these things the retrospective provides technical detail, as
though it were primary documentation; this is where we show our best side to the
world. It explains new features in depth, with clear prose and plentiful
examples, and it connects them all thematically, as a demonstration of how to
write cutting-edge Rust code.

While we are always lavish with our praise of contributors, the retrospective is
the best opportunity to celebrate specific individuals and their contributions
toward the strategic interests of the project, as defined way back at the
beginning of the year.

Finally, the retrospective is an opportunity to evaluate our performance. Did we
make progress toward solving the problems we set out to solve? Did we outright
solve any of them? Where did we fail to meet our goals and how might we do
better next year?

Since the retrospective must be a high-quality document, and cover a lot of
material, it is expected to require significant planning, editing and revision.
The details of how this will work are to be determined.

## Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain a hierarchy of work items, tagged with
  metadata indicating their statuses.

Alone, these provide the *raw data* for a roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

However, for the process to be a success, we need to present the roadmap in a
way that is prominent, succinct, and layered with progressive detail. There is a
lot of opportunity for design here; an early prototype of one possible view is
available [here].

[here]: https://brson.github.io/rust-z

Again, the details are to be determined.

## Calendar

The timing of the events specified by this RFC is precisely specified in order
to set clear expectations and accountability, and to avoid process slippage. The
activities specified here are not the focus of the project and we need to get
through them efficiently and get on with the actual work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
FCP by the last week of September. We choose September for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions. By contrast,
starting with Q1 of the calendar year is problematic due to the holiday season.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; likewise,
the planning for each subsequent quarter at the beginning of the calendar
quarter; and the development of the yearly retrospective approximately for the
month of August.

The survey and other forms of outreach and data gathering should be timed to fit
well into the overall calendar.

## References

- [Refining RFCs part 1: Roadmap]
  (https://internals.rust-lang.org/t/refining-rfcs-part-1-roadmap/3656),
  the internals.rust-lang.org thread that spawned this RFC.
- [Post-1.0 priorities thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/priorities-after-1-0/1901).
- [Post-1.0 blog post on project direction]
  (https://blog.rust-lang.org/2015/08/14/Next-year.html).
- [Blog post on MIR]
  (https://blog.rust-lang.org/2016/04/19/MIR.html),
  a large success in strategic community collaboration.
- ["Stability without stagnation"]
  (http://blog.rust-lang.org/2014/10/30/Stability.html),
  outlining Rust's philosophy on rapid iteration while maintaining strong
  stability guarantees.
- [The 2016 state of Rust survey]
  (https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html),
  which indicates promising directions for future work.
- [Production user outreach thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/production-user-research-summary/2530),
  another strong indicator of Rust's needs.
- [rust-z]
  (https://brson.github.io/rust-z),
  a prototype tool to organize the roadmap.

# Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleasant bikeshed, because it
simultaneously raises the stakes of discussion while moving away from concrete
proposals. That said, the *problem* orientation should help facilitate
discussion, and in any case it's vital to be explicit about our values and
prioritization.

While part of the aim of this proposal is to increase the effectiveness of our
team, it also imposes some amount of additional work on everyone. Hopefully the
benefits will outweigh the costs.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands. This is
the piece of the proposal that will probably need the most follow-up work.

# Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap solely from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) idea.

Another rallying point could be a long-term support release.

# Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Are 1 year cycles too long? What happens if important problems come up
mid-cycle?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing? One of the
problems we have right now is that our release cycles are so predictable they
are almost boring. It could be more exciting to not know exactly when the cycle
is going to end, to experience the tension of struggling to cross the finish
line.

How can we account for work that is not part of the planning process
described here?

How do we address problems that are outside the scope of the standard library
and compiler itself? (See
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) for
an alternative aimed at this goal.)

How do we motivate the improvement of rust-lang crates and other libraries? Are
they part of the planning process? The retrospective?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'. Likewise, 'goal' and 'retrospective' could
be more colorful.

Can we call the yearly RFC the 'north star RFC'? Too many concepts?

What about tracking work that is not part of R-problem-statement and R-goal? I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this proposal does not provide an easy way to find the
status of arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>

<details><summary><b>Step 8 — final</b> (3808 words)</summary>

````text
## Summary
[summary]: #summary

A refinement of the Rust planning and reporting process, to establish a shared
vision of the project among contributors, to make clear the roadmap toward that
vision, and to celebrate our achievements.

Rust's roadmap will be established in year-long cycles, where we identify up
front - together, as a project - the most critical problems facing the language
and its ecosystem, along with the story we want to be able to tell the world
about Rust. Work toward solving those problems, our short-term goals, will be
decided by the individual teams, as they see fit, and regularly re-triaged. For
the purposes of reporting the project roadmap, goals will be assigned to release
cycle milestones.

At the end of the year we will deliver a public facing retrospective, describing
the goals we achieved and how to use the new features in detail. It will
celebrate the year's progress toward our goals, as well as the achievements of
the wider community. It will evaluate our performance and anticipate its impact
on the coming year.

The primary outcome for these changes to the process are that we will have a
consistent way to:

- Decide our project-wide goals through consensus.
- Advertise our goals as a published roadmap.
- Celebrate our achievements with an informative publicity-bomb.

## Motivation
[motivation]: #motivation

Rust is a massive project and ecosystem, developed by a massive team of
mostly-independent contributors. What we've achieved together already is
mind-blowing: we've created a uniquely powerful platform that solves problems
that the computing world had nearly given up on, and jumpstarted a new era in
systems programming. Now that Rust is out in the world, proving itself to be a
stable foundation for building the next generation of computing systems, the
possibilities open to us are nearly endless.

And that's a big problem.

In the run-up to the release of Rust 1.0 we had a clear, singular goal: get Rust
done and deliver it to the world. We established the discrete steps necessary
to get there, and although it was a tense period where the entire future of the
project was on the line, we were united in a single mission. As The Rust Project
Developers we were pumped up, and our user base - along with the wider
programming world - were excited to see what we would deliver.

But 1.0 is a unique event, and since then our efforts have become more diffuse
even as the scope of our ambitions widen. This shift is inevitable: **our success
post-1.0 depends on making improvements in increasingly broad and complex ways**.
The downside, of course, is that a less singular focus can make it much harder
to rally our efforts, to communicate a clear story - and ultimately, to ship.

Since 1.0, we've attempted to lay out some major goals, both through the
[internals forum] and the [blog]. We've done pretty well in actually achieving
these goals, and in some cases - particularly [MIR] - the community has really
come together to produce amazing, focused results. But in general, there are
several problems with the status quo:

[internals forum]: https://internals.rust-lang.org/t/priorities-after-1-0/1901
[blog]: https://blog.rust-lang.org/2015/08/14/Next-year.html
[MIR]: https://blog.rust-lang.org/2016/04/19/MIR.html

- We have not systematically tracked or communicated our progression through the
  completion of these goals, making it difficult for even the most immersed
  community members to know where things stand, and making it difficult for
  *anyone* to know how or where to get involved. A symptom is that questions
  like "When is MIR landing?" or "What are the blockers for `?` stabilizing"
  become extremely frequently-asked. **We should provide an at-a-glance view
  what Rust's current strategic priorities are and how they are progressing.**

- We are overwhelmed by an avalanche of promising ideas, with major RFCs
  demanding attention (and languishing in the queue for months) while subteams
  focus on their strategic goals. This state of affairs produces needless
  friction and loss of momentum. **We should agree on and disseminate our
  priorities, so we can all be pulling in roughly the same direction**.

- We do not have any single point of release, like 1.0, that gathers together a
  large body of community work into a single, polished product. Instead, we have
  a rapid release process, which results in a [remarkably stable and reliable
  product][s] but can paradoxically reduce pressure to ship new features in a
  timely fashion. **We should find a balance, retaining rapid release but
  establishing some focal point around which to rally the community, polish a
  product, and establish a clear public narrative**.

[s]: http://blog.rust-lang.org/2014/10/30/Stability.html

All told, there's a lot of room to do better in establishing, communicating, and
driving the vision for Rust.

This RFC proposes changes to the way The Rust Project plans its work,
communicates and monitors its progress, directs contributors to focus on the
strategic priorities of the project, and finally, delivers the results of its
effort to the world.

The changes proposed here are intended to work with the particular strengths of
our project - community development, collaboration, distributed teams, loose
management structure, constant change and uncertainty. It should introduce
minimal additional burden on Rust team members, who are already heavily
overtasked. The proposal does not attempt to solve all problems of project
management in Rust, nor to fit the Rust process into any particular project
management structure. Let's make a few incremental improvements that will have
the greatest impact, and that we can accomplish without disruptive changes to
the way we work today.

## Detailed design
[design]: #detailed-design

Rust's roadmap will be established in year-long cycles, where we identify up
front the most critical problems facing the project, formulated as _problem
statements_. Work toward solving those problems, _goals_, will be planned as
part of the release cycles by individual teams. For the purposes of reporting
the project roadmap, goals will be assigned to _release cycle milestones_, which
represent the primary work performed each release cycle. Along the way, teams
will be expected to maintain _tracking issues_ that communicate progress toward
the project's goals.

At the end of the year we will deliver a public facing retrospective, which is
intended as a 'rallying point'. Its primary purposes are to create anticipation
of a major event in the Rust world, to motivate (rally) contributors behind the
goals we've established to get there, and generate a big PR-bomb where we can
brag to the world about what we've done. It can be thought of as a 'state of the
union'. This is where we tell Rust's story, describe the new best practices
enabled by the new features we've delivered, celebrate those contributors who
helped achieve our goals, honestly evaluate our performance, and look forward to
the year to come.

### Summary of terminology

Key terminology used in this RFC:

- _problem statement_ - A description of a major issue facing Rust, possibly
  spanning multiple teams and disciplines. We decide these together, every year,
  so that everybody understands the direction the project is taking. These are
  used as the broad basis for decision making throughout the year, and are
  captured in the yearly "north star RFC", and tagged `R-problem-statement`
  on the issue tracker.

- _goal_ - These are set by individual teams quarterly, in service of solving
  the problems identified by the project. They have estimated deadlines, and
  those that result in stable features have estimated release numbers. Goals may
  be subdivided into further discrete tasks on the issue tracker. They are
  tagged `R-goal`.

- _retrospective_ - At the end of the year we deliver a retrospective report. It
  presents the result of work toward each of our goals in a way that serves to
  reinforce the year's narrative. These are written for public consumption,
  showing off new features, surfacing interesting technical details, and
  celebrating those who contribute to achieving the project's goals and
  resolving it's problems.

- _release cycle milestone_ - All goals have estimates for completion, placed on
  milestones that correspond to the 6 week release cycle. These milestones are
  timed to correspond to a release cycle, but don't represent a specific
  release. That is, work toward the current nightly, the current beta, or even
  that doesn't directly impact a specific release, all goes into the release
  cycle milestone corresponding to the time period in which the work is
  completed.

### Problem statements and the north star RFC

The full planning cycle spans one year. At the beginning of the cycle we
identify areas of Rust that need the most improvement, and at the end of the
cycle is a 'rallying point' where we deliver to the world the results of our
efforts. We choose year-long cycles because a year is enough time to accomplish
relatively large goals; and because having the rallying point occur at the same
time every year makes it easy to know when to anticipate big news from the
project. Being calendar-based avoids the temptation to slip or produce
feature-based releases, instead providing a fixed point of accountability for
shipping.

This planning effort is _problem-oriented_. Focusing on "how" may seem like an
obvious thing to do, but in practice it's very easy to become enamored of
particular technical ideas and lose sight of the larger context. By codifying a
top-level focus on motivation, we ensure we are focusing on the right problems
and keeping an open mind on how to solve them. Consensus on the problem space
then frames the debate on solutions, helping to avoid surprises and hurt
feelings, and establishing a strong causal record for explaining decisions in
the future.

At the beginning of the cycle we spend no more than one month deciding on a
small set of _problem statements_ for the project, for the year. The number
needs to be small enough to present to the community managably, while also
sufficiently motivating the primary work of all the teams for the year. 8-10 is
a reasonable guideline. This planning takes place via the RFC process and is
open to the entire community. The result of the process is the yearly 'north
star RFC'.

The problem statements established here determine the strategic direction of the
project. They identify critical areas where the project is lacking and represent
a public commitment to fixing them. They should be informed in part by inputs
like [the survey] and [production user outreach], as well as an open discussion
process. And while the end-product is problem-focused, the discussion is likely
to touch on possible solutions as well. We shouldn't blindly commit to solving a
problem without some sense for the plausibility of a solution in terms of both
design and resources.

[the survey]: https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html
[production user outreach]: https://internals.rust-lang.org/t/production-user-research-summary/2530

Problem statements consist of a single sentence summarizing the problem, and one
or more paragraphs describing it (and its importance!) in detail. Examples of
good problem statements might be:

- The Rust compiler is too slow for a tight edit-compile-test cycle
- Rust lacks world-class IDE support
- The Rust story for asynchronous I/O is very primitive
- Rust compiler errors are difficult to understand
- Rust plugins have no clear path to stabilization
- Rust doesn't integrate well with garbage collectors
- Rust's trait system doesn't fully support zero-cost abstractions
- The Rust community is insufficiently diverse
- Rust needs more training materials
- Rust's CI infrastructure is unstable
- It's too hard to obtain Rust for the platforms people want to target

During the actual process each of these would be accompanied by a paragraph or
more of justification.

We strictly limit the planning phase to one month in order to keep the
discussion focused and to avoid unrestrained bikeshedding. The activities
specified here are not the focus of the project and we need to get through them
efficiently and get on with the actual work.

The core team is responsible for initiating the process, either on the internals
forum or directly on the RFC repository, and the core team is responsible for
merging the final RFC, thus it will be their responsibility to ensure that the
discussion drives to a reasonable conclusion in time for the deadline.

Once the year's problem statements are decided, a metabug is created for each on
the rust-lang/rust issue tracker and tagged `R-problem-statement`. In the OP of
each metabug the teams are responsible for maintaining a list of their goals,
linking to tracking issues.

Like other RFCs, the north star RFC is not immutable, and if new motivations
arise during the year, it may be amended, even to the extent of adding
additional problem statements; though it is not appropriate for the project
to continually rehash the RFC.

### Goal setting and tracking progress

During the regular 6-week release cycles is where the solutions take shape and
are carried out. Each cycle teams are expected to set concrete _goals_ that work
toward solving the project's stated problems; and to review and revise their
previous goals. The exact forum and mechanism for doing this evaluation and
goal-setting is left to the individual teams, and to future experimentation,
but the end result is that each release cycle each team will document their
goals and progress in a standard format.

A goal describes a task that contributes to solving the year's problems. It may
or may not involve a concrete deliverable, and it may be in turn subdivided into
further goals. Not all the work items done by teams in a quarter should be
considered a goal. Goals only need to be granular enough to demonstrate
consistent progress toward solving the project's problems. Work that contributes
toward quarterly goals should still be tracked as sub-tasks of those goals, but
only needs to be filed on the issue tracker and not reported directly as goals
on the roadmap.

For each goal the teams will create an issue on the issue tracker tagged with
`R-goal`. Each goal must be described in a single sentence summary with an
end-result or deliverable that is as crisply stated as possible. Goals with
sub-goals and sub-tasks must list them in the OP in a standard format.

During each cycle all `R-goal` and `R-unstable` issues assigned to each team
must be triaged and updated for the following information:

- The set of sub-goals and sub-tasks and their status
- The release cycle milestone

Goals that will be likely completed in this cycle or the next should be assigned
to the appropriate milestone. Some goals may be expected to be completed in
the distant future, and these do not need to be assigned a milestone.

The release cycle milestone corresponds to a six week period of time and
contains the work done during that time. It does not correspond to a specific
release, nor do the goals assigned to it need to result in a stable feature
landing in any specific release.

Release cycle milestones serve multiple purposes, not just tracking of the goals
defined in this RFC: `R-goal` tracking, tracking of stabilization of
`R-unstable` and `R-RFC-approved` features, tracking of critical bug fixes.

Though the release cycle milestones are time-oriented and are not strictly tied
to a single upcoming release, from the set of assigned `R-unstable` issues one
can derive the new features landing in upcoming releases.

During the last week of every release cycle each team will write a brief
report summarizing their goal progress for the cycle. Some project member
will compile all the team reports and post them to internals.rust-lang.org.
In addition to providing visibility into progress, these will be sources
to draw from for the subsequent release announcements.

### The retrospective (rallying point)

The retrospective is an opportunity to showcase the best of Rust and its
community to the world.

It is a report covering all the Rust activity of the past year. It is written
for a broad audience: contributors, users and non-users alike. It reviews each
of the problems we tackled this year and the goals we achieved toward solving
them, and it highlights important work in the broader community and
ecosystem. For both these things the retrospective provides technical detail, as
though it were primary documentation; this is where we show our best side to the
world. It explains new features in depth, with clear prose and plentiful
examples, and it connects them all thematically, as a demonstration of how to
write cutting-edge Rust code.

While we are always lavish with our praise of contributors, the retrospective is
the best opportunity to celebrate specific individuals and their contributions
toward the strategic interests of the project, as defined way back at the
beginning of the year.

Finally, the retrospective is an opportunity to evaluate our performance. Did we
make progress toward solving the problems we set out to solve? Did we outright
solve any of them? Where did we fail to meet our goals and how might we do
better next year?

Since the retrospective must be a high-quality document, and cover a lot of
material, it is expected to require significant planning, editing and revision.
The details of how this will work are to be determined.

### Presenting the roadmap

As a result of this process the Rust roadmap for the year is encoded in three
main ways, that evolve over the year:

- The north-star RFC, which contains the problem statements collected in one
  place
- The R-problem-statement issues, which contain the individual problem
  statements, each linking to supporting goals
- The R-goal issues, which contain a hierarchy of work items, tagged with
  metadata indicating their statuses.

Alone, these provide the *raw data* for a roadmap. A user could run a
GitHub query for all `R-problem-statement` issues, and by digging through them
get a reasonably accurate picture of the roadmap.

However, for the process to be a success, we need to present the roadmap in a
way that is prominent, succinct, and layered with progressive detail. There is a
lot of opportunity for design here; an early prototype of one possible view is
available [here].

[here]: https://brson.github.io/rust-z

Again, the details are to be determined.

### Calendar

The timing of the events specified by this RFC is precisely specified in order
to set clear expectations and accountability, and to avoid process slippage. The
activities specified here are not the focus of the project and we need to get
through them efficiently and get on with the actual work.

The north star RFC development happens during the month of September, starting
September 1 and ending by October 1. This means that an RFC must be ready for
FCP by the last week of September. We choose September for two reasons: it is
the final month of a calendar quarter, allowing the beginning of the years work
to commence at the beginning of calendar Q4; we choose Q4 because it is the
traditional conference season and allows us opportunities to talk publicly about
both our previous years progress as well as next years ambitions. By contrast,
starting with Q1 of the calendar year is problematic due to the holiday season.

Following from the September planning month, the quarterly planning cycles take
place for exactly one week at the beginning of the calendar quarter; likewise,
the planning for each subsequent quarter at the beginning of the calendar
quarter; and the development of the yearly retrospective approximately for the
month of August.

The survey and other forms of outreach and data gathering should be timed to fit
well into the overall calendar.

### References

- [Refining RFCs part 1: Roadmap]
  (https://internals.rust-lang.org/t/refining-rfcs-part-1-roadmap/3656),
  the internals.rust-lang.org thread that spawned this RFC.
- [Post-1.0 priorities thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/priorities-after-1-0/1901).
- [Post-1.0 blog post on project direction]
  (https://blog.rust-lang.org/2015/08/14/Next-year.html).
- [Blog post on MIR]
  (https://blog.rust-lang.org/2016/04/19/MIR.html),
  a large success in strategic community collaboration.
- ["Stability without stagnation"]
  (http://blog.rust-lang.org/2014/10/30/Stability.html),
  outlining Rust's philosophy on rapid iteration while maintaining strong
  stability guarantees.
- [The 2016 state of Rust survey]
  (https://blog.rust-lang.org/2016/06/30/State-of-Rust-Survey-2016.html),
  which indicates promising directions for future work.
- [Production user outreach thread on internals.rust-lang.org]
  (https://internals.rust-lang.org/t/production-user-research-summary/2530),
  another strong indicator of Rust's needs.
- [rust-z]
  (https://brson.github.io/rust-z),
  a prototype tool to organize the roadmap.

## Drawbacks
[drawbacks]: #drawbacks

The yearly north star RFC could be an unpleasant bikeshed, because it
simultaneously raises the stakes of discussion while moving away from concrete
proposals. That said, the *problem* orientation should help facilitate
discussion, and in any case it's vital to be explicit about our values and
prioritization.

While part of the aim of this proposal is to increase the effectiveness of our
team, it also imposes some amount of additional work on everyone. Hopefully the
benefits will outweigh the costs.

The end-of-year retrospective will require significant effort. It's not clear
who will be motivated to do it, and at the level of quality it demands. This is
the piece of the proposal that will probably need the most follow-up work.

## Alternatives
[alternatives]: #alternatives

Instead of imposing further process structure on teams we might attempt to
derive a roadmap solely from the data they are currently producing.

To serve the purposes of a 'rallying point', a high-profile deliverable, we
might release a software product instead of the retrospective. A larger-scope
product than the existing rustc+cargo pair could accomplish this, i.e.
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) idea.

Another rallying point could be a long-term support release.

## Unresolved questions
[unresolved]: #unresolved-questions

Are 1 year cycles long enough?

Are 1 year cycles too long? What happens if important problems come up
mid-cycle?

Does the yearly report serve the purpose of building anticipation, motivation,
and creating a compelling PR-bomb?

Is a consistent time-frame for the big cycle really the right thing? One of the
problems we have right now is that our release cycles are so predictable they
are almost boring. It could be more exciting to not know exactly when the cycle
is going to end, to experience the tension of struggling to cross the finish
line.

How can we account for work that is not part of the planning process
described here?

How do we address problems that are outside the scope of the standard library
and compiler itself? (See
[The Rust Platform](http://aturon.github.io/blog/2016/07/27/rust-platform/) for
an alternative aimed at this goal.)

How do we motivate the improvement of rust-lang crates and other libraries? Are
they part of the planning process? The retrospective?

'Problem statement' is not inspiring terminology. We don't want to our roadmap
to be front-loaded with 'problems'. Likewise, 'goal' and 'retrospective' could
be more colorful.

Can we call the yearly RFC the 'north star RFC'? Too many concepts?

What about tracking work that is not part of R-problem-statement and R-goal? I
originally wanted to track all features in a roadmap, but this does not account
for anything that has not been explicitly identified as supporting the
roadmap. As formulated this proposal does not provide an easy way to find the
status of arbitrary features in the RFC pipeline.

How do we present the roadmap? Communicating what the project is working on and
toward is one of the _primary goals_ of this RFC and the solution it proposes is
minimal - read the R-problem-statement issues.
````

</details>
