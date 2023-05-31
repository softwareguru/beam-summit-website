---
title: "Managed Stream Processing through Apache Beam at LinkedIn"
slug: managed-stream-processing-through-apache-beam-at-linkedin
speakers:
 - Bingfeng Xia
 - Prateek Maheshwari
 - Xinyu Liu
topics:
 - Runners
 - Use case
room: Horizon
time_start: 2023-06-13 12:00:00
time_end: 2023-06-13 12:50:00
day: a
timeslot: e
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

Managed Beam is LinkedIn's initiative to offer a fully managed stream processing platform via Apache Beam. This platform enables LinkedIn engineers to quickly build and easily run sophisticated streaming applications, without requiring costly infrastructure expertise. At LinkedIn, our stream infrastructure, which combines Apache Beam and Apache Samza, processes over 4 trillion events daily across more than 10,000 pipelines, powering critical services and platforms, including machine learning, notifications, tracking, and anti-abuse.
 
 
 
 In this talk, we will share the key innovations of the fully managed Beam platform, which include:
 
 
 
 1) Workflow Components: reusable and language-neutral building blocks built by Beam JDKs with Protobuf interface, allowing users to compose fully managed workflows, such as source, sink, filter, projection, and aggregation etc.
 
 
 
 2) Compute Isolation: the isolation between user logic and infra framework in build, deploy, and runtime enables both to evolve and operate independently, such as seamless framework upgrade for Beam applications with UDFs. We have achieved this through runtime process-level separation via the Beam Portability Framework.
 
 
 
 3) Auto Sizing: automatically tunes Beam application resources (e.g., CPU, memory, and disk) to optimize for stability and cost efficiency.
 
 
 
 4) Auto Triaging: automatically detects and classifies application and platform health issues. It determines whether an issue is caused by the platform (e.g., noisy neighbors) or the user (e.g., processing exceptions or timeouts).