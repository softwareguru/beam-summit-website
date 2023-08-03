---
title: "Parallelizing Skewed Hbase Regions using Splittable Dofn"
slug: parallelizing-skewed-hbase-regions-using-splittable-dofn
speakers:
 - Prathap Reddy
topics:
 - Splittable DoFn
room: Palisades
time_start: 2023-06-14 14:00:00
time_end: 2023-06-14 14:25:00
day: b
timeslot: g
timeorder: 0
language: 
live_url: 
slides: 
video: https://youtu.be/30usg0deSTI
track: concurrent
tags:
---

During HBase to Cloud BigTable Migrations, HBase snapshots will be imported to Cloud Bigtable. Each Snapshot contains several HBase regions and certain HBase regions can be quite large due to skewed data. 
 
 
 
 In this presentation along with code snippets and benchmark test results, we showcase how to parallelize a skewed HBase Regions using Splittable DoFn and reduce pipeline runtime.