---
slot: b630
title: "Error handling with Apache Beam and Asgarde library"
url: /sessions/error-handling-asgarde
speakers:
 - Mazlum Tosun
time_start: 2022-07-19 15:00:00 -0500 CDT
time_end:   2022-07-19 15:50:00 -0500 CDT
day: b
timeslot: 6
room: 202
timeorder: 0
track: community

---

I created a library for error handling with Apache Beam Java and Kotlin. Asgarde allows error handling with less code and more concise/expressive code. The purpose is showing Beam native error handling, and the same with Asgarde Java.

I will also show Asgarde Kotlin with even more concise code and a more functional style.

https://github.com/tosun-si/asgarde/

The example with Asgarde will store the bad sink in a Bigquery table (DLQ).

We used Asgarde in production code at my actual big customer  (L'Oréal/ France).

It was very important for us to treat errors and not break our jobs in this case.
