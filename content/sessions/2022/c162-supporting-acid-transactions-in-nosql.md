---
slot: c162
title: "Supporting ACID transactions in a NoSQL database with Apache Beam"
url: /sessions/supporting-acid-transactions-in-nosql
speakers:
 - Jan Lukavský
time_start: 2022-07-20 9:30:00 -0500 CDT
time_end:   2022-07-20 9:55:00 -0500 CDT
day: c
timeslot: 1
room: 201 (remote)
timeorder: 2
track: trends
video: https://youtu.be/1TuUejyFT2g
---

In this session we will see how we can use Apache Beam to enhance a generic eventually consistent NoSQL database (e.g. Apache Cassandra) by ACID transactions. We will see how we can use gRPC with splittable DoFn to create an RPC streaming source of requests into Apache Beam Pipeline and then how we can process these requests inside the Pipeline ensuring the requests are applied atomically, consistently, independently and durably despite the data being backed by an eventually consistent data store. The session will use a simplified scenario of banking transactions as a motivating example.