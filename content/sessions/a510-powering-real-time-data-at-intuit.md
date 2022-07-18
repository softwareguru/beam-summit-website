---
slot: a510
title: "Powering Real-time Data at Intuit: A Look at Golden Signals powered by Beam"
url: /sessions/powering-real-time-data-at-intuit
speakers:
 - Omkar Deshpande
 - Dunja Panic
 - Nick Hwang
 - Nagaraja Tantry
time_start: 2022-07-18 14:00:00 -0500 CDT
time_end:   2022-07-18 14:50:00 -0500 CDT
day: a
timeslot: 5
room: 204
timeorder: 0
track: case-study

---

The Stream Processing Platform powers real-time data applications at Intuit using the Apache Beam framework. The platform makes it easy for an engineer to access, transform, and publish streaming data with turn-key solutions to debug and deploy their streaming applications on a managed platform in a manner that is compliant with and leverage Intuit central capabilities. Since launch 3 years ago, the platform has grown to over 150 pipelines in production and handled at peak ~17.3 billion events and 82 TB of data. Most of our pipelines use Kafka as source, with Apache Flink as our stream processing runner of choice for executing the Beam pipelines.
 
In this talk, we will discuss how we’ve built an internal, self-serve stream processing platform with Apache Beam SDK, running on Kubernetes. Specifically, we will highlight our stream processing platform’s benefits and tech stack where Apache Beam serves as a critical technology in how we do real time data processing at Intuit. 
  
We will highlight one streaming use case that generates golden signals for all the services behind Intuit API gateway to provide visibility into the business critical systems. We will provide a high-level design overview as well as dive deep into key technical aspects related to the pipeline, such as triggers, error recovery, side inputs, and late data handling