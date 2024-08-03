---
title: "How Beam ML Optimizes Serving Large Models"
slug: how-beam-ml-optimizes-serving-large-models
speakers:
 - Danny McCormick
topics:
 - ML
room: Mariposa Grove
time_start: 2024-09-04 14:30:00
time_end: 2024-09-04 14:55:00
day: 1
gridarea: "8/2/9/3"
timeslot: 21
images:
 - /images/sessions/2024/how-beam-ml-optimizes.jpg 
---

Serving ML models at scale is increasingly important, and Beam's RunInference transform is a great tool to do this. At the same time, models are getting larger and larger, and it can be hard to fit them into your CPU or GPU.

This talk will explore some of the mechanisms that Beam has put in place for large model management so that it can serve your models efficiently without requiring any additional work from the pipeline author. Attendees can expect to come away with an understanding of how Beam loads and serves models, how it optimizes its serving architecture for different model sizes/footprints, and how they can use Beam to serve their models (large or small).