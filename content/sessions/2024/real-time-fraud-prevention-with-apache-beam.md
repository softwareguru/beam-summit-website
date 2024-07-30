---
title: "Real-Time Fraud Prevention with Apache Beam"
slug: real-time-fraud-prevention-with-apache-beam
speakers:
 - Hai Sadon
topics:
 - Python
 - State & timers
 - Kubernetes
 - ML
room: Mariposa Grove
time_start: 2024-09-04 16:00:00
time_end: 2024-09-04 16:25:00
---

In this session, we will explore how Apache Beam can be leveraged to create a robust real-time fraud prevention system. Drawing from real-world implementations at Transmit Security, the presentation will cover the architecture and components of our Detection and Response solution. Attendees will learn about the challenges of analyzing high volumes of data in real-time, and how we utilize a combination of data collection points, enriched data pipelines, and stateful aggregation engines.

We will discuss our transition to using Google BigTable for low-latency, high-throughput data management, highlighting its role in enhancing the system's performance. 

Additionally, the session will focus on two unique flows within our system:
1. Running machine learning models that predict fraud in real time.
2. Implementing a feedback loop that takes the results from the stream and re-ingests them back into the pipeline to continuously improve detection accuracy.