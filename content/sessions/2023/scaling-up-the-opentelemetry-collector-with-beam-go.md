---
title: "Scaling up the OpenTelemetry Collector with Beam Go"
slug: scaling-up-the-opentelemetry-collector-with-beam-go
speakers:
 - Alex Van Boxel
topics:
 - Go
room: Upper Bay
time_start: 2023-06-13 15:30:00
time_end: 2023-06-13 15:55:00
day: a
timeslot: j
timeorder: 0
language: 
live_url: 
slides: 
video: https://youtu.be/2PVxlaaZMzk
track: concurrent
tags:
---

The OpenTelemetry Collector is a remarkable piece of software. It has a lot of parallels with a Beam pipeline, but it's focused on processing and converting telemetry data. Due to its focus, it's not designed to be run in batch and has limited functionality for parallelism.
 
 
 
 The ability to run the same pipelines in "batch" would undoubtedly be valuable for processing historical data now that the Telemetry Query Language is becoming more mature. If we succeed in making the Collector run with the Beam SDK, the need to create a dedicated pipeline will disappear.
 
 
 
 We will go through the steps, successes, and failures of making a "Go" program, like the OpenTelemetry Collector, and adapt it to work with the Apache Beam Go SDK.