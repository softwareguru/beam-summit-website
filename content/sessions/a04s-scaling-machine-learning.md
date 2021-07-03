---
id: a04s
title: "Scaling machine learning to millions of users with Apache Beam"
url: /sessions/scaling-machine-learning
speakers:
 - Tatiana Al-Chueyr Martins
time_start: 2021-08-04T16:30:00.000Z
time_end: 2021-08-04T16:55:00.000Z
block: a
slot: 04
---

Apache Beam is a critical technology in delivering millions of personalised recommendations to the BBC audience daily. The journey to adopt the technology, however, wasn't the smoothest. The objective of this talk is to save others time and money.

This talk will discuss:
* Why Beam
* First pipeline which allowed us to go from a machine learning prototype to production
* Issues faced with the first approach
* Solutions embraced to handle problems
* Current pipeline design and cost gains

This talk will focus on using the Python SDK and the Dataflow runner.

The solutions covered will include simplifying and splitting the original problem, pipeline configuration and using features such as shared memory.