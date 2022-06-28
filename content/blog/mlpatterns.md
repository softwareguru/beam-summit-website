---
title: "Machine learning design patterns: between Beam and a hard place"
date: 2022-06-27T16:15:00-05:00
description: ""
url: /sessions/mlpatterns/
# post thumb
image : "/images/blog/lak-lakshmanan.png"
images : ["/images/blog/lak-lakshmanan.png"]
# author
author: "Beam Summit Team"
weight: 4
---

In a recent book entitled Machine Learning Design Patterns, we captured best practices and solutions to recurring problems in machine learning. Many of these design patterns are best implemented using Beam. The obvious example is the Transform design pattern, which allows you to replicate arbitrary operations from the training graph in the serving graph while keeping both training and serving code efficient and maintainable. Indeed, the tf.transform package makes this easy.

In this talk, I discuss the patterns where Beam is commonly used (Transform, Batch Serving, Windowed Inference, Feature Store) as well as cases where Beam would be useful but rarely used (Hashed Feature, Continuous Model Evaluation, Bridged Schema, among others).

What capabilities of Beam make Beam such a good fit in ML? What can the Beam community to foster more uptake?
