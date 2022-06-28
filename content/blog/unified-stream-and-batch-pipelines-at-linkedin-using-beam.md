---
title: "Unified Streaming and Batch Pipelines at LinkedIn using Beam"
date: 2022-06-27T16:37:04-05:00
url: /sessions/unified-stream-and-batch-pipelines-at-linkedin-using-beam/
description: ""
# post thumb
image : "/images/blog/Shangjin Zhang,  Yuhong Cheng.png"
images : ["/images/blog/Shangjin Zhang,  Yuhong Cheng.png"]
# author
author: "Beam Summit Team"
weight: 3
---

Many use cases at LinkedIn require real-time processing and periodic backfilling of data. Running a single codebase for both needs is an emerging requirement. In this talk, we will share how we leverage Apache Beam to unify Samza stream and Spark batch processing. We will present the first unified production use case Standardization. By leveraging Beam on Spark for its backfilling, we reduced the backfilling time by 93% while only using 50% of resources. We will also go through the challenges of running unified pipelines, lessons we have learned, and future roadmap at Linkedin.