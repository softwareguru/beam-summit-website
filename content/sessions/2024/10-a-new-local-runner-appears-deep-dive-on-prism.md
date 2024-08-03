---
title: "A New Local Runner Appears: Deep dive on Prism"
slug: a-new-local-runner-appears-deep-dive-on-prism
speakers:
 - Robert Burke
topics:
 - Runners
 - Go
 - Testing
 - Cross language
room: Hamina (MP4)
time_start: 2024-09-04 11:30:00
time_end: 2024-09-04 12:20:00
day: 1
gridarea: "4/4/6/5"
timeslot: 10
images:
 - /images/sessions/2024/new-local-runner.jpg 
---

Prism is a local portable Beam Runner intended to assist end user and SDK developers alike, by providing a common platform for all existing and new Beam SDKs.

Beam is unique among data processing systems in how it divides the user facing SDK from the execution engine. Jobs can be authored in one SDK and executed on Flink, Spark, or on cloud services, like Dataflow. But these external systems can make prototyping, testing, and debugging complicated. 

Prism is written Go to be a small, local runner built using Beam Portability first, to better emulate how jobs of any SDK execute on those larger systems. Further, Prism serves as a model runner for all SDKs for a robust local experience.

This talk will go into how runners execute pipelines, and the design and implementation of Prism for the goals of testing and configurability. Knowledge of Go is encouraged, but not required.