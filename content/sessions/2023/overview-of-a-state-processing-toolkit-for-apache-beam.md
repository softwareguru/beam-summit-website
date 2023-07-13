---
title: "Overview of a State Processing Toolkit for Apache Beam"
slug: overview-of-a-state-processing-toolkit-for-apache-beam
speakers:
 - Harish Nagu Sana
 - Antonio Si
 - Prema devi Kuppuswamy
topics:
 - State & timers
 - Use case
room: Palisades
time_start: 2023-06-14 11:00:00
time_end: 2023-06-14 11:25:00
day: b
timeslot: d
timeorder: 1
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
draft: false
---

Internal states managed by a stateful Beam pipeline are often a black box to pipeline developers. There are various use cases in which the ability to maneuver states would be helpful. At a high level, there are two alternatives one can maneuver the states. One may want to expose the states to some external storage or one may want to kickstart a pipeline with the data from external data sources. In this talk, we would share why, at Intuit, we believe the ability to inspect states and the ability to kickstart a pipeline with some initial states from an external source would be useful. We would share the challenges that we faced and how we address the problems in our State Processing toolkit.