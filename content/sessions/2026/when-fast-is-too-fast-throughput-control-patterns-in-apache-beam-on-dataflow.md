---
title: "When Fast Is Too Fast: Throughput Control Patterns in Apache Beam on Dataflow"
slug: when-fast-is-too-fast-throughput-control-patterns-in-apache-beam-on-dataflow
speakers:
 - Josi Aranda
topics:
 - Scalability and Performance with Optimized Storage
room: Hackberry
time_start: 2026-06-23 13:15:00
time_end: 2026-06-23 13:45:00
---

Apache Beam and Google Cloud Dataflow are optimized for parallelism and autoscaling. In practice, that’s often exactly what we want, until it isn’t.

What happens when your streaming pipeline suddenly scales from 5 to 50 workers and overwhelms a downstream REST API? Or a legacy service enforces strict QPS limits? Beam provides powerful primitives for windowing, batching, and scaling — but it does not offer first-class global throughput control.

This talk explores advanced throughput control patterns specifically in the context of Apache Beam running on Google Cloud Dataflow.
