---
slot: b113
title: "Beam as a High-Performance Compute Grid"
url: /sessions/hpc-grid
speakers:
 - Peter Coyle
 - Raj Subramani
time_start: 2022-07-19 10:50:00 -0500 CDT
time_end:   2022-07-19 11:15:00 -0500 CDT
day: b
timeslot: 1
room: 204
timeorder: 3
track: case-study
live_url: https://www.crowdcast.io/e/beam-summit-2022/24
video: https://youtu.be/QoKWdOXyBw4
slides: 2022/BeamRiskEngine.pdf
---

Risk Management is a key function across all Financial Services. Often this entails heavy computer simulation exploring how financial markets could evolve.  Counterparty Credit Risk  requires particularly  extreme compute capacity given the billions of daily calculations it performs.

Increased regulatory demand (FRTB SA CVA, BCBS 239, etc.) has required further compute power. Traditionally, these simulations are broken up into small tasks and distributed in a compute grid. Map reduction techniques are then used to aggregate and calculate statistical properties.  

To respond to this pressure, HSBC initiated a programme to radically scale out our Risk Service in the Cloud with Apache Beam and managed services in the Cloud.

We would like to share our experience of using Apache Beam as the core platform for hosting both the computational calculations and the map-reduction aggregation process on one DAG.