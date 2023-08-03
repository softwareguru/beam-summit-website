---
title: "Optimizing Machine Learning Workloads on Dataflow"
slug: optimizing-machine-learning-workloads-on-dataflow
speakers:
 - Alex Chan
topics:
 - ML
 - Runners
room: Horizon
time_start: 2023-06-14 15:00:00
time_end: 2023-06-14 15:25:00
day: b
timeslot: i
timeorder: 1
language: 
live_url: 
slides: 
video: https://youtu.be/ayrisg-6YyM
track: concurrent
tags:
---

Trustpilot is is a community-driven platform that hosts reviews of businesses from across the world. It helps people by providing authentic reviews of products and services.
 
 As a reviews platform, Trustpilot handles large volumes of data, particularly text from many languages, making it an ideal use case for machine learning. We use Apache Beam on GCP Dataflow for batch and streaming machine learning workloads. 
 
 
 
 In this talk, we would like to share our experiences optimizing the running of machine learning workloads on Dataflow including:
 
 ‣ Granular resource specification with Dataflow Prime to significantly lower inference costs 
 
 ‣ Making use of Beam's RunInference API for loading models
 
 ‣ Running multiple large models in a pipeline by GPU sharing with NVIDIA MPS
 
 ‣ Accelerating matrix operations in Beam pipelines with the JAX array computation library