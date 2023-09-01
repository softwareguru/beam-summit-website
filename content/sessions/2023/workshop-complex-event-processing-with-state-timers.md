---
title: "Workshop: Complex event processing with state & timers"
slug: workshop-complex-event-processing-with-state-timers
speakers:
 - Israel Herraiz
 - Miren Esnaola
topics:
 - 
room: Palisades
time_start: 2023-06-15 10:45:00
time_end: 2023-06-15 12:15:00
day: c
timeslot: 2
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:

---

Beam does not have a dedicated complex event processing module, but this can be overcome using state & timers.
 
 
 
 In this workshop, we will show an example of how to reconstruct sessions from a stream of data, processing the data in order and identifying sessions not based on temporal properties but on a deep inspection of the messages being processed. We will be using the NY taxi dataset to calculate metrics such as speed, distances (polyline distance based on all intermediate points followed by the taxi), and apply complex patterns such as filtering taxi messages and sessions that fulfil certain criteria (minimum and maximum velocity, minimum and maximum distance, etc).
 
 
 
 We will be using Python for the workshop. To follow this workshop, you will need a Python local development environment.