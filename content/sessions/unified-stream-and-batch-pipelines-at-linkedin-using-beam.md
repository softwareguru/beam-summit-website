---
id: 
title: "Unified Stream and Batch Pipelines at LinkedIn using Beam"
url: /sessions/unified-stream-and-batch-pipelines-at-linkedin-using-beam
speakers:
 - Shangjin Zhang
 - Yuhong Cheng
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

Many use cases at LinkedIn require real-time processing and periodic backfilling of data. Running a single codebase for both needs is an emerging requirement. In this talk, we will share how we leverage Apache Beam to unify Samza stream and Spark batch processing. We will present the first unified production use case Standardization. By leveraging Beam on Spark for its backfilling, we reduced the backfilling time by 93% while only using 50% of resources. We will also go through the challenges of running unified pipelines, lessons we have learned, and future roadmap at Linkedin.