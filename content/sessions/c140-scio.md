---
slot: c140
title: Scio in-depth workshop
url: /sessions/scio-track
speakers:
 - Michel Davit
 - Israel Herraiz
 - Claire McGinty
 - Annica Ivert
 - Austin Bennett
time_start: 2022-07-20 9:00:00 -0500 CDT
time_end: 2022-07-20 12:00:00 -0500 CDT

day: c
timeslot: 1
room: 202
timeorder: 0
track: workshop
session_type: workshop
summary: "This workshop encompasses several talks and a workshop around Scio, which is the open source Scala API for Apache Beam."

---

This workshop encompasses several talks and a workshop around Scio, which is the open source Scala API for Apache Beam.

Sessions:

1. #### Scio & Scala to enhance the Beam experience
   Introduction to Scio and how it leverages some features of the scala programming language.

2. #### A hands-on workshop for Scio
   We will work through a series of kata-like exercises for Scio, where we progressively reveal new concepts and SDK utilities, and build up our knowledge of how to use Scio in our applications.

3. #### Algorithms for Join optimizations in Scio
   Joining large datasets is one of the main tasks when working with Beam and Scio. Joins are a big source of runtime and cost for these sorts of pipelines, as they cause most PCollection data to be serialized and transferred over to new workers. This talk studies how Scio can save you time and money with clever join strategies and approximate algorithms.

4. #### How to optimize cost and runtime when doing rollup aggregations in Scio
   We will explain the use case and algorithm behind the rollupAndCount aggregation, that is part of the scio-extra package. When creating a dataset with rollup dimensions, there is a potentially huge fan-out transform before the aggregation step that can incur large costs in shuffle. It is possible to reduce this fan-out drastically by rethinking the problem. This talk will go into some backstory of the use case we had at Spotify and explain how we developed the algorithm behind rollupAndCount to solve this problem more efficiently.
