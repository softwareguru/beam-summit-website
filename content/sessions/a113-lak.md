---
slot: a113
title: "Machine learning design patterns: between Beam and a hard place"
url: /sessions/mlpatterns
speakers:
 - Lak Lakshmanan
time_start: 2022-07-18 10:25:00 -0500 CDT
time_end:   2022-07-18 10:50:00 -0500 CDT
day: a
timeslot: 1
room: 204
timeorder: 3
track: keynote

---

In a recent book entitled Machine Learning Design Patterns, we captured best practices and solutions to recurring problems in machine learning. Many of these design patterns are best implemented using Beam. The obvious example is the Transform design pattern, which allows you to replicate arbitrary operations from the training graph in the serving graph while keeping both training and serving code efficient and maintainable. Indeed, the tf.transform package makes this easy. 

In this talk, I discuss the patterns where Beam is commonly used (Transform, Batch Serving, Windowed Inference, Feature Store) as well as cases where Beam would be useful but rarely used (Hashed Feature, Continuous Model Evaluation, Bridged Schema, among others). 

What capabilities of Beam make Beam such a good fit in ML? What can the Beam community to foster more uptake?