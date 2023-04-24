---
title: "Simplifying Speech-to-Text Processing with Apache Beam and Redis"
slug: simplifying-speech-to-text-processing-with-apache-beam-and-redis
speakers:
 - Pramod Rao
 - Prateek Sheel
topics:
 - Use case
 - Architecture
room: Palisades
time_start: 2023-06-13 15:30:00
time_end: 2023-06-13 15:55:00
day: a
timeslot: j
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

Abstract:
 
 
 
 Processing speech-to-text data streams can be complex, particularly when it comes to sequencing and event deduplication. Beam runners offer stateful processing backends to address these challenges, but such backends can introduce additional complexities and tie the implementation to a specific runner.
 
 
 
 In this session, we present our design journey to solve a complex speech-to-text processing problem in Apache Beam by leveraging Redis, a simple and efficient external persistent state. Redis provides data types that can handle ordering and deduplication, and offers automatic state management through TTL. By using Redis, we were able to simplify our pipeline code and free it from the constraints of runner-specific stateful mechanisms.
 
 
 
 We will walk through our design iteration process showcasing how we were able to use Redis along with Apache Beam to meet the complex business requirements of a large telecom enterprise. Our approach can serve as a blueprint for other organizations looking to simplify their speech-to-text processing pipelines.