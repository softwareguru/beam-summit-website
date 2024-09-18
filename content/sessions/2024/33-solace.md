---
title: "The SolaceIO connector: how was it made and why"
slug: solace
speakers:
 - Matt Mays
topics:
 - Splittable DoFn
 - IO

room: Bonsai
time_start: 2024-09-04 16:00:00
time_end: 2024-09-04 16:25:00
day: 20241
gridarea: "13/5/14/6"
timeslot: 33
images:
 - /images/sessions/2024/solace.png
---

Together with Solace, we have developed a new native streaming connector for Solace, a popular messaging platform used in manufacturing, finance and many other industries.

Solace has different APIs for different purposes (moving data around, managing queues, etc), that can be leveraged together to create a Beam connector with accurate and timely backlog and watermark estimations.

The connector has been developed by Solace and Google, in collaboration with a customer, this connector is an example of cross-industry collaboration for the benefit of all Apache Beam users.

In this talk we explain how Solace works, how we made it work with Beam with high throughput and low latency, and what lessons can be learnt for the design of complex streaming connectors for Beam.
