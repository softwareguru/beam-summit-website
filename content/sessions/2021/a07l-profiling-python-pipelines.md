---
id: a07l
title: "Profiling Apache Beam Python pipelines"
url: /sessions/profiling-python-pipelines
speakers:
 - Israel Herraiz
time_start: 2021-08-04T18:00:00.000Z
time_end: 2021-08-04T18:45:00.000Z
block: a
slot: 07
summary: In this talk, we will explore how to profile Apache Beam Python pipelines to identify potential bottlenecks in our code.
slides: 2021/a07-Profiling.pdf
video: https://youtu.be/K2M0uo-DfOg
---

Often the first version of our Apache Beam pipelines do not perform as well as we would like, and sometimes it is not so obvious to find the places where we could optimize performance; sometimes it will be a function parsing JSON, some others the bottleneck will be a external source or sink, or we have a very hot key and we are trying to group by key. In this talk, we will explore how to profile Apache Beam Python pipelines to identify potential bottlenecks in our code.