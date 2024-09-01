---
slot: a910
title: "New Avro serialization and deserialization in Beam SQL"
url: /sessions/avro-serialization-deserialization
speakers:
 - Talat Uyarer
time_start: 2022-07-18 17:15:00 -0500 CDT
time_end:   2022-07-18 18:05:00 -0500 CDT
day: a
timeslot: 9
room: 204
timeorder: 0
track: trends 
slides: 2022/AvroSerialization.pdf
video: https://youtu.be/njMx0dIyLjw
---

At Palo Alto Networks we heavily rely on Avro, using it as the primary storage format and use Beam Row as in memory. We de/serialize billions Avro records per second. One day we realized Avro Row conversion routines consume much of CPU time. Then the story begins ....