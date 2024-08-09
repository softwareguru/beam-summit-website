---
title: "Transitioning Uber Michelangelo's Batch Prediction from Apache Spark to Ray"
slug: transitioning-uber-michelangelo-s-batch-prediction-from-apache-spark-to-ray
speakers:
 - Baojun Liu
track: Use case
room: Mariposa Grove
time_start: 2024-09-04 11:30:00
time_end: 2024-09-04 11:55:00
day: 20241
gridarea: "6/2/7/3"
timeslot: 8
images:
 - /images/sessions/2024/transitioning-uber.jpg 
---

Michelangelo is Uber's centralized machine learning platform, designed to manage ML pipelines and their associated data processing. As the demand for batch predictions grows, the need for a flexible and efficient processing framework becomes imperative. This presentation explores Uber Michelangelo’s batch prediction processes, focusing on data processing, model prediction, and the transition from Spark to Ray.

At Michelangelo, data preparation and feature transformation are traditionally handled using Spark data transforms. The model prediction step involves a user-defined function within a Spark pipeline model. While Spark has been the backbone for our batch processing needs due to its robustness and ease of use, it has shown limitations in handling the complex machine learning tasks that Uber is increasingly deploying, such as natural language processing and Generative AI. These workloads often require GPUs to meet latency and throughput requirements, which Spark struggles to support efficiently.

Ray, an emerging distributed computing framework, offers better resource utilization, simpler parallelism, and more straightforward scalability. By leveraging Ray for batch processing, we can support large language model batch predictions reliably, efficiently, and scalably. We are also transitioning other machine learning batch prediction tasks to Ray for both data processing and model prediction. In this new setup, data processing is integrated as part of the model using native transformer techniques, allowing deployment on GPUs.

With Ray, we have developed a robust pipeline for batch prediction. Currently, streaming data is handled with separate pipelines. We are actively exploring the unification of these pipelines using open-source libraries. Apache Beam ML provides an opportunity to unify batch and streaming data processing pipelines.