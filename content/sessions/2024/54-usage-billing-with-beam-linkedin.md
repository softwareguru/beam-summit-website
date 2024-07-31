---
title: "Usage Billing with BEAM @ LinkedIn"
slug: usage-billing-with-beam-linkedin
speakers:
 - Narayanan Venkiteswaran
 - Bella Le
 - Vinay Chander
topics:
 - Use case
 - Runners
 - Architecture
room: Hamina (MP4)
time_start: 2024-09-05 13:30:00
time_end: 2024-09-05 13:55:00
day: 2
timeslot: 6
---

Usage Billing is a billing concept where charges are based on consumption. At LinkedIn, the Usage Billing system processes large volume of consumptions particularly for Ads and Jobs use cases. In this presentation, we will discuss how the team rearchitected the existing usage platform to adopt a more streaming-oriented approach using Apache Beam and Samza Runner. The new system can aggregate usage data across various dimensions and supports multiple rules to handle different aggregation windows. It also includes change data capture and correction events to ensure the high level of accuracy required when handling customers' money.