---
title: "ML model updates with side inputs in Dataflow streaming pipelines"
slug: ml-model-updates-with-side-inputs-in-dataflow-streaming-pipelines
speakers:
 - Anand Inguva
topics:
 - ML
 - Runners
room: Horizon
time_start: 2023-06-14 15:30:00
time_end: 2023-06-14 15:55:00
day: b
timeslot: i
timeorder: 2
language: 
live_url: 
slides: 2023/Anand-AutoModelRefresh.pdf
video: https://youtu.be/g5rvWd-ZizY
track: concurrent
tags:
---

In this session, we would go over a live demo of how user can update their Machine learning model in a Dataflow streaming pipeline without updating/stopping their beam pipeline as mentioned at https://cloud.google.com/dataflow/docs/guides/updating-a-pipeline using Apache Beam side inputs.
 
 
 
 A side input containing model path[1] can be passed to the RunInference transform. Initially, when there is no side input to the main input, RunInference will use the default model path defined by the ModelHandler. Once the side input is updated with a latest path, Beam RunInference will continue to use the updated model for performing inferences on examples. 
 
 
 
 [1] https://github.com/apache/beam/blob/36486447e4d07af5076830ca1e331a6b61f14986/sdks/python/apache_beam/ml/inference/base.py#L332