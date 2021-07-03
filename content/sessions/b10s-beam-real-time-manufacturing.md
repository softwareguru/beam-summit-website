---
id: b10s
title: "Using Beam for Real-time Manufacturing Data Analysis"
url: /sessions/beam-real-time-manufacturing
speakers:
 - Jeswanth Yadagani
time_start: 2021-08-05T20:30:00.000Z
time_end: 2021-08-05T20:55:00.000Z
block: b
slot: 10
---


This is an application talk targeted at users of Apache Beam to illustrate how a combination of stateless, stateful, and windowed streaming transformations can be used to support arbitrarily complex real-time analysis of manufacturing time-series data.

At Oden, we are focused on the ingest and analysis of data from connected manufacturing equipment, context from manufacturing execution systems, and input from operators on the manufacturing factory floor. We run several real-time analytics using ML models deployed on Apache Beam to provide access to patterns, alerts, and process optimization insights to end-users. As part of this, we leverage Apache Beam’s features to perform stateless, windowed, and stateful calculations, transform and contextualize manufacturing tag values into meaningful metrics that speak about a process, and extract features that are input to the ML models.

In this talk, we present how we realize an “Algebra of Streaming Metric Calculations” on real-time data using a combination of stateless, stateful, and windowed operations, and how these calculations are leveraged to provide insights into the manufacturing process. This includes:

Allowing users to define arbitrary logic (as Javascript functions) that can be applied to any metric, a combination of metrics, or a window of metrics., and implementing these calculations using an embedded JS interpreter within Beam ParDos.
Translating complex rules for alerting, extracted from ML models, into such combinations of calculations, and auto-populating them to realize predictive alerting.
Using Apache Beam to capture stateful context that combines process metadata with streaming measurements in real-time and allows us to reduce false positives in our real-time alerts and increase their process relevance.
We will describe the underlying manufacturing processes, our implementation and architecture, and sample results on how this brings value to our customers. We will also describe generalizable patterns from our work that can be applied to other application contexts.
