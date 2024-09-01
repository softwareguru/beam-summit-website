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
slides: 2021/a08-AWS.pdf
video: https://youtu.be/KmvAc0F8zNM
---


In this workshop, you explore an end to end example that combines batch and streaming aspects in one uniform Beam pipeline.
You start off with building a Beam pipeline to analyse taxi trip events. You deploy the the pipeline to Amazon Kinesis Data Analytics for Apache Flink to analyse incoming events in a streaming fashion. You also implement archival of the streaming data to Amazon S3 for long term storage. Finally, you extend the Beam pipeline by adding new metrics to the generated output. After applying the changed to the streaming pipeline, you reprocess the archived data in a batch fashion to backfill dashboards with the newly added metrics.

In case you were not able to attend live you can run this workshop on your own at https://streaming-analytics.workshop.aws/beam-on-kda

