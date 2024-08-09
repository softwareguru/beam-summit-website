---
title: "Beam SDKs Don't Have to Look the Same"
slug: beam-sdks-don-t-have-to-look-the-same
speakers:
 - Robert Burke
topics:
 - Architecture
 - Go
room: Walker Canyon
time_start: 2024-09-05 11:00:00
time_end: 2024-09-05 11:25:00
day: 20242
gridarea: "4/3/5/4"
timeslot: 40
images:
 - /images/sessions/2024/beam-sdks.jpg 
---

Do we even need PCollections? Or ProcessElements? Can we have the language fully typecheck the pipeline for us at compile time? Can we do that in Go?

Since Beam was designed, programming languages have continued to evolve and change, so why can't our SDKs? We've now got ample experience with the Apache Beam Go SDK, but the language it was designed for is now very different. 

This short talk will compare the current Go SDK with an experimental implementation that takes better advantage of the current strengths of Go, and its approach to generic type parameters, and more.