---
title: "Throttling Detection and Reactive Worker Downscaling"
slug: throttling-detection-and-reactive-worker-downscaling
speakers:
 - Yi Hu
topics:
 - IO
 - Runners
room: Hamina (MP4)
time_start: 2024-09-04 14:30:00
time_end: 2024-09-04 14:55:00
day: 1
gridarea: "10/4/11/5"
timeslot: 23
images:
 - /images/sessions/2024/throttling.jpg 
---

Rate limiting and draining quota is a common issue for a data processing pipeline running at scale. Overprovision of the worker pool when the external resource is throttled not only increases the cost but also puts additional pressure onto the resources. This talk introduces the recent improvements on tackling this issue, from tracking throttled states in a Beam pipeline to taking actions on these signals from the runner (particularly Dataflow) side. Finally, it explores options on how users can onboard their custom IO connectors for throttling detection features.