---
title: "Case study: Using statefulDofns to process late arriving data"
slug: case-study-using-statefuldofns-to-process-late-arriving-data
speakers:
 - Amruta Deshmukh
topics:
 - Use case
room: Palisades
time_start: 2023-06-14 14:30:00
time_end: 2023-06-14 14:55:00
day: b
timeslot: h
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

We needed to process two different types of files arriving in the same bucket but there was no way of knowing if both files had arrived in real time. So we used two separate beam pipelines and StatefulDoFns to wait until the all the files are received and processed.