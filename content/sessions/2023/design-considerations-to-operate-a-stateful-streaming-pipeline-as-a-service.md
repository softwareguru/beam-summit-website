---
title: "Design considerations to operate a stateful streaming pipeline as a service"
slug: design-considerations-to-operate-a-stateful-streaming-pipeline-as-a-service
speakers:
 - Israel Herraiz
 - Bhupinder Sindhwani
topics:
 - Operations
 - Use case
room: Palisades
time_start: 2023-06-14 12:30:00
time_end: 2023-06-14 12:55:00
---

Businesses are looking to harness the power of real-time data with streaming analytics and more often or not that involves computing stateful transformations out of the raw data stream. When the business logic to be applied in streaming is complex and does not use time-based aggregations, it is difficult to use windows, and it is easy to start by leveraging external stores to simplify the streaming pipeline implementation, however this is an anti-pattern that eventually causes latency and troubleshooting issues. 
 
 
 
 Furthermore, efficiently operating a streaming pipeline requires adoption of SRE principles (e.g. defining specific SLOs and error budget) to monitor the pipeline as a service and avoid alert fatigue. This session will walk you through an example use-case to demonstrate how you can leverage Apache Beam state and timers APIs for complex event processing in streaming and incorporate the SRE principles to design and operate a stateful streaming pipeline as a service.