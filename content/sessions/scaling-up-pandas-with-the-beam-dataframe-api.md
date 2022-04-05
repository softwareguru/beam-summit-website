---
id: 
title: "Scaling up pandas with the Beam DataFrame API"
url: /sessions/scaling-up-pandas-with-the-beam-dataframe-api
speakers:
 - Brian Hulette
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

Beam’s Python SDK is incredibly powerful due to its high scalability and advanced streaming capabilities, but its unfamiliar API has always been a barrier to adoption. Conversely, the popular Python pandas library has seen explosive growth in recent years due to its ease of use and tight integration with interactive notebook environments, but it can only process data with a single node - it cannot be used to process distributed datasets in parallel. In this talk I will demonstrate how Beam’s pandas-compatible DataFrame API provides the best of both tools. First, I will demonstrate how the API can be used to interactively build data pipelines that can be easily scaled up to process distributed datasets. Then, I will dive into the internals of the Beam DataFrame API and show how it scales up pandas to process distributed datasets.