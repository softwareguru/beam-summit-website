---
title: "Developing (experimental) Rust SDKs and a Beam engine for IoT devices"
slug: developing-experimental-rust-sdks-beam-engine-iot
aliases: 
 - introducing-springql-as-a-rust-based-beam-engine-for-iot-devices
speakers:
 - Sho Nakatani
topics:
 - Use case
room: Horizon
time_start: 2023-06-13 16:15:00
time_end: 2023-06-13 16:40:00
day: a
timeslot: l
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

SpringQL (https://github.com/SpringQL/SpringQL) is a single-node stream processor designed specifically for IoT devices. It is written in Rust, which allows it to keep applications small and fast, avoiding the need for large language runtimes or garbage collections. In this talk, we propose making SpringQL as a Beam engine, and discuss the work that we are doing to change SpringQL's API from incomplete streaming SQL to the Beam Model.
 
 
 
 To achieve this, we are using an experimental Rust SDK (https://github.com/apache/beam/issues/21089), which we are also contributing to and improving. We will share our progress and discuss any challenges we have faced in the process. While we may not have a fully functioning SpringQL as a Beam engine by the time of the presentation, we will share our plans for future work and discuss the potential benefits of using Rust for Beam on IoT devices.