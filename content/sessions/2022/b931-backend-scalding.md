---
slot: b931
title: "Apache Beam backend for open source Scalding"
url: /sessions/backend-scalding
speakers:
 - Navin Viswanath
time_start: 2022-07-19 17:15:00 -0500 CDT
time_end:   2022-07-19 17:40:00 -0500 CDT
day: b
timeslot: 9
room: 202
timeorder: 1
track: trends
video: https://youtu.be/caumzQWqslQ
slides: 2022/BeamBackendScalding.pdf
---

The batch processing data pipelines at Twitter process hundreds of petabytes of data on a daily basis. These pipelines run on on-premise Hadoop clusters and use Scalding as the framework for data processing.We are currently in the midst of migrating our batch processing pipelines to the cloud. With approximately 5000 production pipelines, it becomes necessary to automate the migration of these pipelines to the cloud.

Scalding is an abstract API for expressing computations on data, and allows backend implementations to be plugged in. It currently has both a Cascading and Spark backend. In this talk, we’ll describe a new Apache Beam backend for Scalding that we are in the process of implementing at Twitter. This backend expresses the various computations in Scalding as PTransforms in Beam. With this backend, we can run Scalding pipelines on Beam in the cloud with near zero code changes, thus automating the migration of these pipelines to the cloud.

