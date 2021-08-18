---
id: b11s
title: "Lessons learned from using Dataflow for local ML batch inference"
url: /sessions/lessons-learned-dataflow-ml-batch-inference
speakers:
 - Ramtin Rassoli
time_start: 2021-08-05T21:00:00.000Z
time_end: 2021-08-05T21:25:00.000Z
block: b
slot: 11
slides: 
video: https://youtu.be/7yOsiMOgAHY
---

At BenchSci, we mine the world’s biological research papers with the aim of extracting information that will accelerate future pharmaceutical research programs by enabling more reproducible experiments. Machine Learning and specifically our in-house Deep Learning models play an important role in extracting these key pieces of information and organizing the knowledge into a meaningful and easy-to-use structure.

While we have the luxury of processing this information in batch, the size and number of our models along with the size of the input data eventually outgrew our on-premise model serving infrastructure. So we decided to migrate our MLOps pipelines to our cloud environment where we can scale our operations with minimal infrastructure management overhead. Dataflow, which is already a core component of our solution architecture, recently added support for custom containers and GPUs. This made extending our current use-case to accommodate our model serving as well, considerably easier. For ML inference we implemented our batch processes locally in Beam and used Dataflow to load our ML models into memory directly inside the worker nodes.

In comparison to remote inference options (e.g. GCP AI Platform), using Apache Beam for local batch inference provides a straightforward yet effective pattern to streamline our MLOps operations and seamlessly re-use the same framework, tools, and CI/CD we already have for our data processing pipelines. In sharing this use case we hope to provide others with a set of expectations about the benefits and work involved when dealing with local inference on Beam and Dataflow.