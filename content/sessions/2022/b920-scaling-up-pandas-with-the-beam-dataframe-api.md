---
slot: b920
title: "Scaling up pandas with the Beam DataFrame API"
url: /sessions/scaling-up-pandas-with-the-beam-dataframe-api
speakers:
 - Brian Hulette
time_start: 2022-07-19 17:15:00 -0500 CDT
time_end:   2022-07-19 18:05:00 -0500 CDT
day: b
timeslot: 9
room: 203
timeorder: 0
track: deep-dive
live_url: https://www.crowdcast.io/e/beam-summit-2022/42
slides: 2022/DataFrameAPI.pdf
video: https://youtu.be/b0jyPcfgdPA
---

Beam’s Python SDK is incredibly powerful due to its high scalability and advanced streaming capabilities, but its unfamiliar API has always been a barrier to adoption. Conversely, the popular Python pandas library has seen explosive growth in recent years due to its ease of use and tight integration with interactive notebook environments, but it can only process data with a single node - it cannot be used to process distributed datasets in parallel. In this talk I will demonstrate how Beam’s pandas-compatible DataFrame API provides the best of both tools. First, I will demonstrate how the API can be used to interactively build data pipelines that can be easily scaled up to process distributed datasets. Then, I will dive into the internals of the Beam DataFrame API and show how it scales up pandas to process distributed datasets.