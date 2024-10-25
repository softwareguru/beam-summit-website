---
title: "Workshop: Step by step development of a streaming pipeline in Python"
slug: workshop-step-by-step-development-of-a-streaming-pipeline-in-python
speakers:
 - Israel Herraiz
 - Anthony Lazzaro
topics:
 - Python
room: C
time_start: 2023-07-18 15:30:00
time_end: 2023-07-20 17:30:00
day: a
timeslot: b
timeorder: 1
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:   

---

In this workshop we will develop a streaming pipeline, showing how to get data in JSON format and parse it (using Beam schemas), how to aggregate it and write it in batches to Avro files.
 
 
 
 We will apply complex analytics to the stream, calculating properties of a session for different users, grouping together events of the same session by using windowing. 
 
 
 
 As a bonus point, we will explore how to use the parameters of a DoFn to inspect the properties of the window, adding information about the window and the trigger, to understand the concepts of windowing, triggering and accumulation mode.