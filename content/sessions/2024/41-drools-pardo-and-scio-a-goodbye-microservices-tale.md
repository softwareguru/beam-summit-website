---
title: "Drools ParDo and SCIO: a goodbye microservices tale"
slug: drools-pardo-and-scio-a-goodbye-microservices-tale
speakers:
 - Alberto López Serna
topics:
 - Architecture
 - Scala
 - Use case
 - Kubernetes
 - Splittable DoFn
 - Java
room: Hamina (MP4)
time_start: 2024-09-05 11:00:00
time_end: 2024-09-05 11:25:00
day: 2
timeslot: 2
---

A successful re-engineering in banking with a Drools ParDo using a KieContainer (JBoss) in Dataflow has been used to process business rules.jar, merging several Spring microservices into Dataflow. This design, with another Dataflow app and the pattern adopted in "Avoid HTTP requests duplicates in Apache Beam with SCIO, a custom BaseAsyncDoFn and State and Timers" has allowed to get tid off all microservices and infrastructure thanks to Apache Beam and Dataflow.