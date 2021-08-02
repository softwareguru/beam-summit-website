---
id: a08w
title: "Workshop: Build a Unified Batch and Streaming Pipeline with Apache Beam on AWS"
url: /sessions/build-beam-pipeline-aws
speakers:
 - Gandhi Swaminathan
 - Steffen Hausmann
time_start: 2021-08-04T18:00:00.000Z
time_end: 2021-08-04T20:00:00.000Z
block: a
slot: 08
summary: In this workshop, you explore an end to end example that combines batch and streaming aspects in one uniform Beam pipeline. Check out the prerrequisites and additional registration.
---

**Participation in this workshop requires additional registration and has limited capacity. If you are interested, please [register here](https://us02web.zoom.us/webinar/register/WN_3zNJOuDVQhGKxU-yg2Sbkg)**

In this workshop, you explore an end to end example that combines batch and streaming aspects in one uniform Beam pipeline.

You start off with building a Beam pipeline to analyse taxi trip events. You deploy the the pipeline to Amazon Kinesis Data Analytics for Apache Flink to analyse incoming events in a streaming fashion. You also implement archival of the streaming data to Amazon S3 for long term storage. Finally, you extend the Beam pipeline by adding new metrics to the generated output. After applying the changed to the streaming pipeline, you reprocess the archived data in a batch fashion to backfill dashboards with the newly added metrics.

Join us to learn how to leverage Beam’s expressive programming model to unify batch and streaming. You will also understand how to combine different AWS services to create Apache Beam based batch and streaming architectures in a fully managed environment on AWS.

Prerequisites

* You’ll implement the Beam pipeline with Java. Some rudimentary knowledge of Java or a similar language is useful.
* You do NOT need an AWS account, we will create accounts for you and distribute credentials before the workshop.