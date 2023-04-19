---
id: c05s
title: "Scalable Predictions of Deep Learning models with Apache Beam"
url: /sessions/scalable-predictions
speakers:
 - Jo Pu
 - Hannes Hapke
time_start: 2021-08-06T16:30:00.000Z
time_end: 2021-08-06T16:55:00.000Z
block: c
slot: 05
slides: 
video: https://youtu.be/EjGAQt8tgr8
---

With the rise of deep learning applications, so do the questions of how to integrate larger machine learning models (e.g. transformer models) in Apache Beam data pipelines. At Digits, we took a deep dive into optimal integrations of our deep learning models to be consumed efficiently with Apache Beam and Google Cloud’s Dataflow.

In this presentation, we will walk the audience through how we evaluated the various options for serving Deep Learning models on Beam with Dataflow, the architecture of our production model pipelines, and some lessons we learned while optimizing inference performance and maximizing pipeline throughput. The resulting architecture leads to scalability, interoperability, and increased engineering productivity.

Bringing machine learning models into production can look daunting. We’ll highlight why Apache Beam is the perfect companion for deployed machine learning models and hope to share our own experiences to ease your future deployments and integrations of deep learning applications.