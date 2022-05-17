---
slot: b610
title: "Streaming NLP infrastructure on Dataflow"
url: /sessions/streaming-nlp-infrastructure-on-dataflow
speakers:
 - Alex Chan
 - Angus Neilson
time_start: 2022-07-19 15:00:00 -0500 CDT
time_end:   2022-07-19 15:50:00 -0500 CDT
day: b
timeslot: 6
room: 1
timeorder: 0
track: case-study

---

Trustpilot is an e-commerce reviews platform delivering millions of new reviews to businesses each week. We are using Apache Beam on GCP Dataflow to deliver real-time streaming inferences with the latest NLP transformer models.
 
 Our talk will touch on:
 - Infrastructure setup to enable Python Beam to interface with Kafka for streaming data
 - Taking advantage of Beam's unified programming model to enable batch jobs for backfilling via BigQuery
 - Working with GPUs on Dataflow to speed up local model inference
 - MLOps: Using Dataflow as part of a continuous evaluation model monitoring setup