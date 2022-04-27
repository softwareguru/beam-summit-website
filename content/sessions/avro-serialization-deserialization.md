---
id: 
title: "New Avro serialization and deserialization in Beam SQL"
url: /sessions/avro-serialization-deserialization
speakers:
 - Talat Uyarer
time_start: 2022-01-01T17:00:00.000Z
time_end: 2022-01-01T18:00:00.000Z
block: 
slot: 
---

At Palo Alto Networks we heavily rely on Avro, using it as the primary storage format and use Beam Row as in memory. We de/serialize billions Avro records per second. One day we realized Avro Row conversion routines consume much of CPU time. Then the story begins ....