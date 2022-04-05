---
id: 
title: "Relational Beam: Process columns, not rows!"
url: /sessions/relational-beam
speakers:
 - Andrew Pilloud
 - Brian Hulette
 - Kyle Weaver
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

Last year we kicked off relational work with a vision of automatically optimizing your pipeline. Now we have a panel of contributors who are working towards this goal! We will demo the new optimizer in Java core, showing how we can automatically prune columns from IOs. Then we will discuss our upcoming work to make vectorized execution a reality through native columnar support in Python and Java. Finally we will discuss usage best practices around using Schemas, Dataframes, and SQL to ensure you can benefit from these changes.