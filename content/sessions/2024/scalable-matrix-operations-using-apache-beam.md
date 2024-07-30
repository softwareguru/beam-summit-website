---
title: "Scalable Matrix Operations using Apache Beam"
slug: scalable-matrix-operations-using-apache-beam
speakers:
 - Pramod Rao
 - Jay Jayakumar
topics:
 - Use case
 - ML
 - State & timers
 - Java
 - Architecture
room: Mariposa Grove
time_start: 2024-09-04 13:30:00
time_end: 2024-09-04 14:20:00
---

NumPy is amongst the most popular Python libraries known for their powerful capabilities in handling complex numerical computations including matrix operations which are encountered frequently in exploratory data science tasks.

This discussion will delve into an alternative approach to achieve similar outcomes at scale, using the Apache Beam and open-source linear algebra library such as EJML. This is a generalized presentation of an implemented use case for a large customer.

We will also explore strategies for making this core library developed to be used within Apache Beam further extended as a microservice, allowing other data scientists to integrate and leverage this streamlined workflow effectively.

The attendees will gain valuable insights into: 
* Converting existing logic written in NumPy/Pandas to Apache Beam
* Extend the core computations as a micro-services for serving multiple use cases
* Learnings/Challenges