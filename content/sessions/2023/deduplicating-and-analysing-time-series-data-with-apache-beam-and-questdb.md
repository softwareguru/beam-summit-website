---
title: "Deduplicating and analysing time-series data with Apache Beam and QuestDB"
slug: deduplicating-and-analysing-time-series-data-with-apache-beam-and-questdb
speakers:
 - Javier Ramirez
topics:
 - State & timers
room: Palisades
time_start: 2023-06-14 12:00:00
time_end: 2023-06-14 12:25:00
day: b
timeslot: e
timeorder: 1
language: 
live_url: 
slides: 
video: https://youtu.be/B7IjWHFhpfE
track: concurrent
tags:
---

Time series data pipelines tend to prioritise speed and freshness over completeness and integrity. In such scenarios, it is very common to ingest duplicate data, which may be fine for many analytical use cases, but is very inconvenient for others.
 
 
 
 There are many open source databases built specifically for the speed and query semantics of time series, and most of them lack automatic deduplication of events in near real-time. One such database is QuestDB, which requires a manual batch process to deduplicate ingested data.
 
 
 
 In this talk, we will see how we can successfully use Apache Beam to deduplicate streaming time series, which can then be analysed by a time series database.