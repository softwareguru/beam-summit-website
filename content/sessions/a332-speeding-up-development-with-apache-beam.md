---
slot: a332
title: "Speeding up development with Apache Beam (Adobe Experience Platform)"
url: /sessions/speeding-up-development-with-apache-beam
speakers:
 - Constantin Scacun
 - Alexander Falca
time_start: 2022-07-18 12:30:00 -0500 CDT
time_end:   2022-07-18 12:55:00 -0500 CDT
day: a
timeslot: 3
room: 3
timeorder: 2
track: case-study

---

At the core of Adobe Experience Platform (AEP), there is a large Apache Kafka deployment: 20+ data centers, 300+ billion messages a day. We use it to import/export data for external customers and integrate internal solutions. Processing those events involves lots of boilerplate code and practices: understanding the streaming platform, optimizing for throughput, instrumenting metrics, deploying the service, alerting, and monitoring.
 
Out of these requirements, we built a team to construct and be responsible for the infrastructure where Apache Beam jobs would run. Today, this allows AEP teams to quickly get their projects to a "Production Ready" state by decoupling the runtime (Beam, Flink, Kubernetes) from business logic, simplifying Production support (failure tolerance, scaling, and observability), and allowing customization by adding business logic in the form of user provided compiled and packaged code.
  
We achieved the following KPIs for the organization: 
 1. little time and effort to launch a Beam pipeline across multiple data centers 
 2. no code written for simple pipelines (expressed fully via a JSON-based DSL) 
 3. low count of use cases not satisfied by the streaming service mentioned above