---
title: "Per Entity Training Pipelines in Apache Beam"
slug: per-entity-training-pipelines-in-apache-beam
speakers:
 - Jasper Van den Bossche
topics:
 - ML
room: Horizon
time_start: 2023-06-14 11:00:00
time_end: 2023-06-14 11:50:00
day: b
timeslot: d
timeorder: 0
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

When building a machine learning application, engineers often make a trade-off between training a single model or one model per entity. Imagine you're building a chatbot for an online retailer that sells to customers around the world that speak many different languages. You could opt for a single multilingual model or you could train a model for English, Spanish, French, etc.. Another example could be quality inspection using different kinds of sensors. You could build a model that takes all sensory data or you could build a model that predicts defects using the data of a single sensor. This concept is called per entity training and has a few advantages:
 
 
 
 Smaller models are easier to train, cheaper to run and it is easier to detect and fix problems with the model or the data it is trained on. However one of the big challenges when working with per entity training is managing all steps involved. These steps may include: Data ingestion from different sources, processing data in various formats and varying quality, inference of the different models or post processing the results such that they can be presented to the end user in such a way that is easy to understand.
 
 
 
 Apache Beam can serve as an excellent system to keep track of all of these steps. In this session we will take a deep dive into per entity training using Apache Beam. We will go step by step over an example where we analyze the incomes of individuals living in different parts of the US. In this conference, You will gain an understanding of how data is processed from different sources, how the different models are trained and how this workflow can easily scale.