---
title: "How to balance power and control when using Dataflow with an OLTP SQL Database"
slug: how-to-balance-power-and-control-when-using-dataflow-with-an-oltp-sql-database
speakers:
 - Florian Bastin
topics:
 - Use case
 - Runners
room: Upper Bay
time_start: 2023-06-14 14:30:00
time_end: 2023-06-14 14:55:00
day: b
timeslot: 8
timeorder: 1
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

We created a Python SDK-based Dataflow streaming pipeline for a major French retail company. When notified, the pipeline efficiently reads large CSV files from Google Cloud Storage and selects, inserts, upserts, and deletes rows from a Cloud SQL Postgres database with a controlled number of connections.
 
 The business purpose of this project is to use streaming queries in order to apply various types of transactions to an OLTP database based on CSV files.
 
 
 
 Technical description:
 
 Connecting Cloud SQL to Dataflow is not straightforward. For example, the Cloud SQL JDBC connector is limited in the kind of read and write operations it allows and other custom connectors and can be easily overflown due to the parallelism and autoscaling capabilities of Apache Beam and Dataflow. Additionally, since the number of connections for a database is limited, we developed additional features to prevent connections from being overwhelmed.
 
 
 
 Main focus:
 
 After reviewing the most common ways to control the level of parallelism and its limit (number of threads and workers...), our talk will focus on how we controlled the number of connections to Cloud SQL in a Dataflow pipeline by leveraging the beam.utils.Shared module to share connections at the worker level.
 
 We will show that by doing that and using the different flavors of reshuffle based transforms (groupIntoBatches, GroupByKey...), you can achieve a better control of your SQL connections.
 
 
 
 We also developed SDF for reading large CSV files and created a streaming pipeline for inserting CSV rows into an OLTP database. Since the connection between Dataflow and Cloud SQL is not highlighted in the Google and Beam documentation, we want to share our experience with other companies who faced similar issues at the summit.