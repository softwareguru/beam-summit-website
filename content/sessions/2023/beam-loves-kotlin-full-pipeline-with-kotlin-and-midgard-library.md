---
title: "Beam loves Kotlin: full pipeline with Kotlin and Midgard library"
slug: beam-loves-kotlin-full-pipeline-with-kotlin-and-midgard-library
speakers:
 - Mazlum Tosun
topics:
 - Cross language
room: Upper Bay
time_start: 2023-06-13 16:45:00
time_end: 2023-06-13 17:35:00
day: a
timeslot: m
timeorder: 0
language: 
live_url: 
slides: 2023/Mazlum-KotlinMidgard.pdf
video: https://youtu.be/iFHfY8ocUrU
track: concurrent
tags:
---

The goal of this talk is to show a real-world and full Beam pipeline with Kotlin and Midgard library.

This library was created recently to help Beam and Kotlin communities to have a more concise/expressive code and a more functional programming style.

Kotlin is a great language and we love using it with Beam, we proposed this combination at my last customer and the code is beautiful.

We will first show the pipeline with Beam Java.

We will then show the same pipeline with Kotlin and Midgard with live coding in some parts of the pipeline.

This example will contain many operators (map, flatMap, and filters), the use of Beam DoFn lifecycle, and side input.

In the end, we will explain the strategy behind Midgard based on Kotlin extensions, to be very near to the native Beam Java SDK and have the possibility to mix very easily Midgard code with native code.