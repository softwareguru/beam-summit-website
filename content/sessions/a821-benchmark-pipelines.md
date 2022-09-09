---
slot: a821
title: "How to benchmark your Beam pipelines for cost optimization and capacity planning"
url: /sessions/benchmark-pipelines
speakers:
 - Roy Arsan
time_start: 2022-07-18 16:15:00 -0500 CDT
time_end:   2022-07-18 16:40:00 -0500 CDT
day: a
timeslot: 8
room: 203
timeorder: 1
track: deep-dive
live_url: https://www.crowdcast.io/e/beam-summit-2022/17
video: https://youtu.be/U58C07t6cf4
slides: BenchmarkCapacityPlanning.pdf
---

Are your deployed Beam pipelines properly sized to meet your SLOs? Currently there’s no standard way of benchmarking your Dataflow pipelines to measure expected output rate or utilization, which are required for capacity planning and cost optimization. This talk is to present a methodology and a toolset to benchmark performance (event latency and throughput) of a custom Beam pipeline using Dataflow as runner. Results would be synthesized into prescriptive sizing guidelines to achieve best performance/cost ratio. Presented methodology can also be used to monitor and avoid pipeline performance regressions as part of your pipeline development and CI/CD process.

