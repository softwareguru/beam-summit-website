---
title: "Dealing with order in streams using Apache Beam"
slug: dealing-with-order-in-streams-using-apache-beam
speakers:
 - Israel Herraiz
topics:
 - Use case
room: Palisades
time_start: 2023-06-14 10:30:00
time_end: 2023-06-14 10:55:00
day: b
timeslot: c
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

How to get data processed in order even when the queue deliver messages unordered?
 
 
 
 One of the main problems when working with data in streaming is out of order. Data will come unordered and late. How come we apply a logic to that stream if it requires data to be ordered? Is there any solution to that?
 
 
 
 In this talk, we will see how we can solve this problem using Apache Beam, and apply any temporal logic to keyed streams, however complex it is, even if it requires recovering the order in which data was produced.