---
title: "See the Full Picture: Integrating Beam/Dataflow into Your Distributed Traces"
slug: see-the-full-picture-integrating-beam-dataflow-into-your-distributed-traces
speakers:
 - Radek Stankiewicz
 - Steven van Rossum
 - Kenneth Knowles
topics:
 - Connecting disparate systems with modern data architectures
time_start: 2025-07-08 12:15:00
time_end: 2024-07-08 12:40:00
room: Palisades
track: 
day: 20251
gridarea: "8/4/9/6"
timeslot: 10
images: 

slides:
video: 
---

Achieving holistic observability often hits a wall at asynchronous batch or streaming systems. While OpenTelemetry provides standards for tracing, integrating systems like Apache Beam/Dataflow requires specific considerations. This presentation details the successful integration of Beam pipelines with OpenTelemetry's tracing APIs. We'll explore the mechanisms for context propagation across Beam's distributed workers and stages, enabling pipelines to join traces initiated by upstream services. Discover how spans generated within the Dataflow runner can be exported and visualized alongside the rest of your application traces in Google Cloud Trace, finally delivering the "full picture" of your system's behavior, including its data processing components.