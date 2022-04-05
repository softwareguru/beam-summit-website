---
id: 
title: "Optimizing a Dataflow pipeline for cost efficiency: lessons learned at Orange"
url: /sessions/optimizing-cost-efficiency
speakers:
 - Jérémie Gomez
 - Thomas Sauvagnat
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

This session would be co-presented between a customer (Orange, french telco) and myself following a work we did together (PSO engagement between Google and Orange).
 
 It would go like this: 
 - The use case: what are we trying to do with this project (in particular, it's a project that collects all logs from internet boxes)
 - Configuration (tuning vCPUs, number of threads, enabling or disabling streaming engine)
 - Autoscaling (give some info about helping the autoscaler to behave correctly, and iteratively choose a good number of initial and max workers)
 - Writing to BigQuery: talking about the BQ Storage Write API and the BQ Load API in the context of Dataflow
 - Profiling and improving the code (basically profiling and best practices)
 
 This would be told as a story and every time we would say if each step made us gain on the cost/performance side or not.
 
 I am hesitating between 25mn and 50mn, but I believe 40mn with 10mn questions could be good. Do you think this would be a case study or a deep dive? I'm leaning towards case study.