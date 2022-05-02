---
id: 
title: "Oops, I wrote a Portable Beam Runner in Go"
url: /sessions/portable-go-beam-runner
speakers:
 - Robert Burke
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

Like all the SDKs, the Apache Beam Go SDK has a direct runner, for simple testing. However, unlike Python and Java, it has languished, not covering all parts of the model supported by the SDK. Worse, it doesn't even use the FnAPI!

This dive into the runner side of Beam will cover how I wrote my own testing oriented replacement for the Go Direct runner, and how it can become useful for Java, Python, and future SDKs.