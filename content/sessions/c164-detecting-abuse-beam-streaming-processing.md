---
slot: c164
title: "Effective detecting and preventing abuse on LinkedIn with Beam streaming processing"
url: /sessions/detecting-abuse-beam-streaming-processing
speakers:
 - Rui Han
time_start: 2022-07-20 11:00:00 -0500 CDT
time_end:   2022-07-20 11:25:00 -0500 CDT
day: c
timeslot: 1
room: 6
timeorder: 4
track: case-study
draft: true
---

The anti-abuse team at Linkedin builds data infrastructure that generates offline datasets. Data is essential to our abuse defense mechanisms such as machine learning models or rule-based anti-abuse systems. Due to the adversarial nature of the problem, the defenses generated from the offline datasets need to be updated frequently in order to detect and prevent abuse activities that are rapidly changing and evading. The paradigm shift to Beam streaming data processing opened a new door to the team and empowered us to defeat sophisticated abusers quickly and accurately. In this talk, we will discuss the use case of defending automated scraping abuse with the Beam model. We will share what the anti-abuse challenges are with the offline dataset, how Beam helps to solve the problems, and how we benefit from the adaptation of Beam’s programming model and framework in our anti-abuse defense.