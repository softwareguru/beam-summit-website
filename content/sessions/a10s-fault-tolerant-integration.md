---
id: a10s
title: "Fault Tolerant Integration of Apache Beam With Relational Database"
url: /sessions/fault-tolerant-integration
speakers:
 - Savitha Jayasankar
time_start: 2021-08-04T20:30:00.000Z
time_end: 2021-08-04T20:55:00.000Z
block: a
slot: 10
summary: We will share a use case at Niantic where we used Postgres as a time-series database to store metrics information from Apache Beam workflows.
---

Prometheus is an industry-wide used monitoring system and time series database. Prometheus cannot be used as a metrics reporting system for outputs of a non-real-time Apache Beam pipeline as the metric denotes a player activity when occurred in the past, and Prometheus does not have a feature to accept timestamp as input. Niantic's goal was to process the batched data pipelines and produce timestamped player activity metrics without data loss and millisecond accuracy. The solution that worked in Niantic was using Postgres as a time-series database to store metrics information from Apache Beam workflows.

In this session, Savitha (Software Engineer, Niantic) and Piaw (Senior Staff Software Engineer, Niantic) will share how they solved the problem using a novel Apache Beam pipeline design pattern that allows workflow pipelines to do most of the data processing, allowing metrics ingestion into Postgres at low cost, low latency, and large scale, along with optimal execution time.The design combines all the elements in each window of the input using a combining function that can happen in parallel with a fanout parameter. This ensures optimal CPU utilization and workflow execution time. This customized implementation is another approach of divide-and-conquer applied to distributed data processing.