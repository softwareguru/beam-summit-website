---
id: b12s
title: "Autoscaling your transforms with auto-sharded GroupIntoBatches"
url: /sessions/autoscaling-transforms
speakers:
 - Pablo Estrada
time_start: 2021-08-05T21:30:00.000Z
time_end: 2021-08-05T21:55:00.000Z
block: b
slot: 12
---

Big data systems have implemented the ability to scale up from the cluster perspective: Add more workers, and parallelize further.

An issue with this is that many transforms still work with a fixed number of shards that can't scale up or down with the cluster.

We recently added this capability to Cloud Dataflow, and we want to share our experiments and what we learned from this - and how you can take advantage of it.