---
slot: b511
title: "Unified Streaming and Batch Pipelines at LinkedIn using Beam"
url: /sessions/unified-stream-and-batch-pipelines-at-linkedin-using-beam
speakers:
 - Shangjin Zhang
 - Yuhong Cheng
time_start: 2022-07-19 14:00:00 -0500 CDT
time_end:   2022-07-19 14:25:00 -0500 CDT
day: b
timeslot: 5
room: 204
timeorder: 1
track: case-study
video: https://youtu.be/rBfwjbrMJTE
slides: 2022/UnifiedStreaming-LinkedIn.pdf
---

Many use cases at LinkedIn require real-time processing and periodic backfilling of data. Running a single codebase for both needs is an emerging requirement. In this talk, we will share how we leverage Apache Beam to unify Samza stream and Spark batch processing. We will present the first unified production use case Standardization. By leveraging Beam on Spark for its backfilling, we reduced the backfilling time by 93% while only using 50% of resources. We will also go through the challenges of running unified pipelines, lessons we have learned, and future roadmap at Linkedin.