---
title: "Meeting Security Requirements for Apache Beam Pipelines on Google Cloud"
slug: meeting-security-requirements-for-apache-beam-pipelines-on-google-cloud
speakers:
 - Lorenzo Caggioni
topics:
 - Architecture
room: Palisades
time_start: 2023-06-13 14:30:00
time_end: 2023-06-13 14:55:00
day: a
timeslot: h
timeorder: 0
language: 
live_url: 
slides: 2023/Lorenzo-SecurityRequirements.pdf
video: https://youtu.be/CW94rCjDYpE
track: concurrent
tags:
---

When running Apache Beam pipelines in an enterprise environment, it is important to be able to meet a variety of security requirements. These requirements may include:
 
  - Role separation and least privileges: Identities should only be able to access the data and resources that they need to perform their job.
 
 - Private resources: Data and resources should be stored and processed in a private environment that is not accessible to the public.
 
  - Encryption of customer data: Customer data should be encrypted at rest using a customer managed encryption key.
 
 
 
 In this talk we will identify a reference architecture to accomplish all such requirements on a Google Cloud Platform environment.