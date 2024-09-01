---
id: b01l
title: "Simple Distributed Raytracer with the Beam Go SDK"
url: /sessions/distributed-raytracer-go-sdk
speakers:
 - Robert Burke
time_start: 2021-08-05T15:00:00.000Z
time_end: 2021-08-05T15:50:00.000Z
block: b
slot: 01
summary: Demonstrate the Beam Go SDK with a raytracer as the motivating example.
slides: 2021/b01-RayTracer.pdf
video: https://youtu.be/JZcva_JPR-I
---

Demonstrate the Beam Go SDK with a raytracer as the motivating example.
Attendees will come away with a light overview of Ray Tracing, but the focus is on implementing it using Beam Go.
Includes
* Raytracing overview
* Using SplittableDoFns to divide work (and DoFn basics)
* Writing final images to GCS
* Collecting and accessing Metrics
* Debugging using the Python Portable runner and Loopback mode.
* Executing on a distributed runner.