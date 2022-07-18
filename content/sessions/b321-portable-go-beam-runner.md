---
slot: b321
title: "Oops, I wrote a Portable Beam Runner in Go"
url: /sessions/portable-go-beam-runner
speakers:
 - Robert Burke
time_start: 2022-07-19 12:00:00 -0500 CDT
time_end:   2022-07-19 12:25:00 -0500 CDT
day: b
timeslot: 3
room: 203
timeorder: 1
track: deep-dive

---

Like all the SDKs, the Apache Beam Go SDK has a direct runner, for simple testing. However, unlike Python and Java, it has languished, not covering all parts of the model supported by the SDK. Worse, it doesn't even use the FnAPI!

This dive into the runner side of Beam will cover how I wrote my own testing oriented replacement for the Go Direct runner, and how it can become useful for Java, Python, and future SDKs.