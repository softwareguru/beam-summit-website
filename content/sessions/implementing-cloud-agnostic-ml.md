---
id: 
title: "Implementing Cloud Agnostic Machine Learning Workflows with Apache Beam on Kubernetes"
url: /sessions/implementing-cloud-agnostic-ml
speakers:
 - charles adetiloye
 - Alexander Lerma
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

The need for a highly efficient data processing workflow is fast becoming a necessity in every organization implementing and deploying Machine Learning models at scale. In most cases, ML teams leverage the managed service solutions already in place by the cloud infrastructure provider they choose. While this approach is good enough for most teams to get going, the long-term cost of keeping the platform running may be prohibitively higher over time.
 
As an alternative, we run our ML pipeline tasks as Apache Beam jobs orchestrated with Argo on Kubernetes. Using Kubernetes gives us a clean abstraction of the underlying compute resources and enables us to declaratively configure Apache Beam job runners for either streaming or batch workloads on any Cloud or OnPrem compute infrastructure.
 
In this talk, we will discuss how we have implemented a continuous integration and deployment environment stack to containerize and deploy Argo workflows for running our beam job on Kubernetes. We will go through the challenges we encountered and lessons learned with recommended best practices to consider for any MLOps team considering this approach