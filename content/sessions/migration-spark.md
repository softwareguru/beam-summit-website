---
id: 
title: "Migration Spark to Apache Beam/Dataflow and hexagonal architecture + DDD"
url: /sessions/migration-spark
speakers:
 - Mazlum Tosun
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

In my previous customer, we did a code migration from Spark/Dataproc et Apache Beam/Dataflow.



I proposed an hexagonal architecture + Domain driven design with Apache Beam, in order to isolate to business code (bounded context/domain) and technical code (infrastucture).



This architecture is used with code decoupling and dependency injection.

I used Dagger2 and i am going to explain why :)



The purpose is showing a Beam project with this architecture and explain why it's interesting.



One example with Beam Java and another with Kotlin will be shown. The Kotlin version uses dataclasses and extensions to have a more concise and expressive code.



I also use this architecture in my actual customer in prod.