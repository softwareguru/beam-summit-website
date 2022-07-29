---
slot: b512
title: "Detecting Change-Points in Real-Time with Apache Beam"
url: /sessions/detecting-change-points-in-real-time
speakers:
 - Devon Peticolas
time_start: 2022-07-19 14:30:00 -0500 CDT
time_end:   2022-07-19 14:55:00 -0500 CDT
day: b
timeslot: 5
room: 204
timeorder: 2
track: deep-dive
live_url: https://www.crowdcast.io/e/beam-summit-2022/32
slides: Apache Beam Summit - Detecting Change Points.pdf
video:
---

Apache Beam provides an expressive and powerful toolset for transformation over bounded and unbounded (streaming) data. One common but not obvious transformation that Oden has needed to implement is Change-Point Detection.
 
Change-Point Detection is at the heart of many of Oden's real-time features to its manufacturing clients. For example, many clients need to track when their factory’s production lines stop running in order to root-cause issues and improve capacity.
 
Oden continuously streams sampled real-world properties of the machines used in those lines, such as motor-speed, and uses change-detection to differentiate periods where the line was “stopped,” “ramping up,” or “running.” This problem is complicated by the need to “smooth out” flapping stoppages and by sparse, late, and out-of-order data caused by network outages.
  
In this talk, we'll cover different methods of change-point detection in bounded and unbounded PCollections using Beam Windows and State, how to implement "smoothing" of change-points to limit their frequency, and the implications of event sparsity, lateness, and order on these methods.