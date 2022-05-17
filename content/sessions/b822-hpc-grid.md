---
slot: b822
title: "Beam as a High-Performance Compute Grid"
url: /sessions/hpc-grid
speakers:
 - Peter Coyle
 - Raj Subramani
time_start: 2022-07-19 16:45:00 -0500 CDT
time_end:   2022-07-19 17:10:00 -0500 CDT
day: b
timeslot: 8
room: 2
timeorder: 2
track: case-study

---

Risk Management is a key function across all Financial Services. Often this entails heavy computer simulation exploring how financial markets could evolve.  Counterparty Credit Risk  requires particularly  extreme compute capacity given the billions of daily calculations it performs.

Increased regulatory demand (FRTB SA CVA, BCBS 239, etc.) has required further compute power. Traditionally, these simulations are broken up into small tasks and distributed in a compute grid. Map reduction techniques are then used to aggregate and calculate statistical properties.  

To respond to this pressure, HSBC initiated a programme to radically scale out our Risk Service in the Cloud with Apache Beam and managed services in the Cloud.

We would like to share our experience of using Apache Beam as the core platform for hosting both the computational calculations and the map-reduction aggregation process on one DAG.