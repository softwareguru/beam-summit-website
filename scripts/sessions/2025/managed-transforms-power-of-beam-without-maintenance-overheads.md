---
title: "Managed transforms - power of Beam without maintenance overheads"
slug: managed-transforms-power-of-beam-without-maintenance-overheads
speakers:
 - Chamikara Jayalath
topics:
 - Real-time data applications
 - Scalability & Performance
 - Unified Data Processing
room: Palisades
time_start: 2025-07-08 11:45:00
time_end: 2025-07-08 12:10:00
---

Apache Beam offers a number of powerful transforms including a set of highly scalable I/O connectors. Usually, you have to regularly keep upgrading Beam to get critical fixes related to such transforms. With the recent addition of Java and Python managed APIs, Beam allows runners to fully manage supported transforms. Google Cloud Dataflow uses this API to manage and automatically upgrade widely used Beam I/O connectors. This allows you to focus on the business logic of your batch and streaming pipelines without worrying about associated maintenance overheads.