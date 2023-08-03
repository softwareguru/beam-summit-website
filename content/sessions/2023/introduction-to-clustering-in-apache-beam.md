---
title: "Introduction to Clustering in Apache Beam"
slug: introduction-to-clustering-in-apache-beam
speakers:
 - Jasper Van den Bossche
topics:
 - 
room: A
time_start: 2023-07-18 16:00:00
time_end: 2023-07-18 16:25:00
day: a
timeslot: b
timeorder: 2
language: 
live_url: 
slides: 2023/Jasper-Clustering.pdf
video: https://youtu.be/rRPJZrgQFUI
track: concurrent
tags:
---

A common way to train a machine learning model to classify data is to show the model a lot of examples together with a label. In the real world, you often don't have labeled data because labeling is a labor intensive and costly job or simply because it's really hard for humans to label the data. When working with unlabeled data, clustering/cluster analysis is a commonly used technique to group similar data together. It is used to solve a variety of problems in many different fields ranging from bioinformatics to detect cancer cells all the way up the financial world where it is used to detect fraudulent transactions in a banking system.
 
 
 
 One of the biggest challenges when putting such machine learning applications into production is managing all the different steps, such as: data ingestion to data cleaning, scaling infrastructure, etc.. However, Apache Beam is capable of all of these steps and makes it possible to easily build scalable machine learning workflows.
 
 
 
 In this session we'll focus on the Online Clustering Transform. We'll start the session with a small introduction on clustering for non-machine learning experts where we'll explain how the algorithms work and what the difference is between online and offline clustering. We will then explain how Clustering Transform works behind the scenes.
 
 
 
 Finally we will take a look at example use, where we will put the clustering transform at work. We will get a streaming pipeline that does anomaly detection on sensor data so that such defects can be detected.