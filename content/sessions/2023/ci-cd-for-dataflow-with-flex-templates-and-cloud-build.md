---
title: "CI CD for Dataflow with Flex Templates and Cloud Build"
slug: ci-cd-for-dataflow-with-flex-templates-and-cloud-build
speakers:
 - Mazlum Tosun
topics:
 - 
room: Palisades
time_start: 2023-06-14 15:00:00
time_end: 2023-06-14 15:50:00
day: b
timeslot: i
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

The goal of this talk is showing a full example with a CI CD pipeline for Dataflow jobs.

The jobs will be based on Flex Template that is a way to standardize the deployment of Dataflow jobs and we are going to show a full example with Java and Python SDKs.

The CI CD will be orchestrated with Cloud Build based on a Github repository :
- Launch unit tests on push to the Github repository
- Manual job to deploy the Dataflow job with Flex Template
- Manual job to run the Dataflow job and template

In an extra and optional part, we will show the Dataflow Flex Template deployment with Dagger IO and Go.

Dagger is a tool that allows to write CI CD Pipeline As Code.