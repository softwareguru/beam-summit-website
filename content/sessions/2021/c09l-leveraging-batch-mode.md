---
id: c09l
title: "Leveraging Beam's Batch-Mode for Robust Recoveries and Late-Data Processing of Streaming Pipelines"
url: /sessions/leveraging-batch-mode
speakers:
 - Devon Peticolas
time_start: 2021-08-06T18:00:00.000Z
time_end: 2021-08-06T18:50:00.000Z
block: c
slot: 09
slides: 2021/c09-LeveragingBatch.pdf
video: https://youtu.be/g1p8PR44l90
---

This will be an application talk targeted at users or potential users of Apache Beam for real-time streaming applications. It will show how to write a Beam application deployable as both a streaming and batch job. And how to leverage that batch deployment for robust batch recoveries and late-data processing for your streaming application.

At Oden, we focus on the ingest and analysis of data from connected manufacturing equipment, context from manufacturing execution systems, and input from operators on the manufacturing factory floor. We do this with a series of streaming Beam applications that transform, enrich, and provide real-time insights from our customer’s data.

However, getting data from factories comes with a unique set of challenges such as limited ISP coverage, faulty networks, and poor connectivity. This results in incomplete, out-of-order, or highly late data regularly dumped onto our real-time pipeline. While this data is necessary for historical analysis, intermingling it with the “good” data comes at the expense of performance and stability.

To address this, Oden has created reusable patterns so that every streaming application is deployable in a batch mode that uses BigQuery and GCS in place of real-time PubSub. Each night, an Apache Airflow DAG orchestrates a batch-mode mirror of our streaming pipeline that separately processes this late and problematic data, keeping our real-time pipeline protected.

The result of this approach is a two-tier SLA for ingesting and processing our customer’s data and a significantly more efficient and resilient real-time system.