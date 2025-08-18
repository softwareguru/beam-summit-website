---
title: "Integration of Batch and Streaming data processing with Apache Beam"
slug: integration-of-batch-and-streaming-data-processing-with-apache-beam
speakers:
 - Yoichi Nagai
topics:
 - Real-time data applications
 - Unified Data Processing
room: Online
time_start: 2025-07-30 15:00:00
time_end: 2025-07-30 15:30:00
track: 
day: 20253
gridarea: "1/2/2/3"
timeslot: 6
images: 

slides: 
video: https://youtu.be/lkIR4oYstKI

---

Mercari utilizes Apache Beam for batch and streaming processing for various purposes, such as transferring data to CRM and providing incentives to users.
To avoid having to develop similar data pipelines in different departments within the company, Mercari Pipeline has been developed and released as OSS as a tool that allows users to build pipelines by simply defining the processing via JSON or YAML.
(https://github.com/mercari/pipeline)

In this session, we will introduce an example of utilizing the features of Apache Beam, which allows Batch and Streaming processes to share the same code, to divert time-series aggregate values generated and verified by Batch to Streaming processes.

* Integration of multiple data sources
* Aggregate computation with window function using State API
* Aggregate computation with window function utilizing external data store (Bigtable) and CDC
* Inference with ONNX model
* Configuration management by Batch and Streaming difference