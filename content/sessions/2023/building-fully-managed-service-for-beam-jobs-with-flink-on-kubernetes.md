---
title: "Building Fully Managed Service for Beam Jobs with Flink on Kubernetes"
slug: building-fully-managed-service-for-beam-jobs-with-flink-on-kubernetes
speakers:
 - Talat Uyarer
 - Rishabh Kedia
topics:
 - Kubernetes
 - Use case
 - Architecture
room: Upper Bay
time_start: 2023-06-14 11:00:00
time_end: 2023-06-14 11:25:00
day: b
timeslot: 4
timeorder: 1
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

At Palo Alto Networks, We are using Beam on Dataflow for 10K+ jobs. Beam has good abstraction run on multiple runner. For multi Cloud Provider use case We developed a fully managed stream processing platform on Flink running on K8s to power thousands of stream processing pipelines in production without changing our business code. This platform is the backbone for other infra systems like Real Time Analytics and Log processing to handle 10 Million rps.
 
 
 
 We have provided a rich authoring and testing environment which allows users to create, test, and deploy their streaming jobs in a self-serve fashion within minutes with Dataflow. Now we provide similar functionality by building Beam Flink based platform on Kubernetes.
 
 
 
 So Users can focus on their business logic, leaving the Beam platform to take care of management aspects such as resource provisioning, auto-scaling, job monitoring, alerting, failure recovery and much more on multi cloud platform.
 
 
 
 In this talk, we will introduce the overall platform architecture, highlight the unique value propositions that it brings to stream processing at Palo Alto Networks and share the experiences and lessons we have learned while creating Beam Kubernetes based platform