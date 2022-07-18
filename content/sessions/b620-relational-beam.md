---
slot: b620
title: "Relational Beam: Process columns, not rows!"
url: /sessions/relational-beam
speakers:
 - Andrew Pilloud
 - Brian Hulette

time_start: 2022-07-19 15:00:00 -0500 CDT
time_end:   2022-07-19 15:50:00 -0500 CDT
day: b
timeslot: 6
room: 203
timeorder: 0
track: deep-dive

---

Last year we kicked off relational work with a vision of automatically optimizing your pipeline. Now we have a panel of contributors who are working towards this goal! We will demo the new optimizer in Java core, showing how we can automatically prune columns from IOs. Then we will discuss our upcoming work to make vectorized execution a reality through native columnar support in Python and Java. Finally we will discuss usage best practices around using Schemas, Dataframes, and SQL to ensure you can benefit from these changes.