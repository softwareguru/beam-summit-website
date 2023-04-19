---
title: "Running Beam Multi Language Pipeline on Flink Cluster on Kubernetes"
slug: running-beam-multi-language-pipeline-on-flink-cluster-on-kubernetes
speakers:
 - Lydian Lee
topics:
 - Runners
 - Kubernetes
 - Cross language
room: Upper Bay
time_start: 2023-06-14 11:30:00
time_end: 2023-06-14 11:55:00
---

The mission of Affirm is to provide honest financial products and services that empower consumers to spend and save responsibly. To achieve this goal, we need to have event-sourced data interfaces to allow pseudo real time event processing and aggregation. Affirm uses Apache Beam to deliver streaming applications written in Python, and to re-use existing Python business logic in streaming pipelines. However there are challenges in properly configuring across-language pipeline to run Python on theJava KafkaIO library, largely due to lack of examples and documentation. In this blog post, we would like to share how Affirm configures our Apache Beam pipelines to run on a kubernetes-powered Apache Flink cluster. Hopefully we can help other teams bridge the gap on setting up their streaming infra.