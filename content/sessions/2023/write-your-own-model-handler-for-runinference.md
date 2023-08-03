---
title: "Write your own model handler for RunInference!"
slug: write-your-own-model-handler-for-runinference
speakers:
 - Ritesh Ghorse
topics:
 - ML
 - Python
room: Horizon
time_start: 2023-06-14 14:00:00
time_end: 2023-06-14 14:25:00
day: b
timeslot: g
timeorder: 1
language: 
live_url: 
slides: 
video: https://youtu.be/kw7UFr-I_I4
track: concurrent
tags:
---

This talk will cover how to write a custom model handler for RunInference transform in Python SDK. Currently, we support Sklearn, PyTorch, Tensorflow, Onxx, and XGBoost model handlers. But there are situations when developers would like to write their own because of different input types they are using, any new framework, custom options, etc. I'll talk about the bits and pieces of writing a new model handler and explain the key components by using a Tensorflow model handler as an example.