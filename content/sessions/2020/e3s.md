---
id: e3s
title: "Snorkel Beambell - Real-time Weak Supervision on Apache Beam"
url: /sessions/snorkell-beambell
speakers:
  - Suneel Marthi

time_start: 2020-08-28T16:50:00.000Z
time_end:   2020-08-28T17:10:00.000Z
day_num: 5
---

The advent of Deep Learning models has led to a massive growth of real-world machine learning. Deep Learning allows Machine Learning Practitioners to get the state-of-the-art score on benchmarks without any hand-engineered features. These Deep Learning models rely on massive hand-labeled training datasets which is a bottleneck in developing and modifying machine learning models.

Most large scale Machine Learning systems today like Google’s DryBell use some form of Weak Supervision to construct lower quality, large scale training datasets that can be used to continuously retrain and deploy models in a real-world scenario.

The challenge with continuous retraining is that one needs to maintain prior state (e.g., the learning functions in case of Weak Supervision or a pre-trained model like BERT or Word2Vec for Transfer Learning) that is shared across multiple streams, while continuously updating the model. Apache Beam’s Stateful Stream processing capabilities are a perfect match here including support for scalable Weak Supervision.

Prior work on using Beam’s State coupled with Flink’s dynamic processing capabilities to store and update word embeddings for real-time Online Topic Modeling of text has been presented at Flink Forward Berlin 2018. Similar streaming pipelines would also work for real-time model updates using Weak Supervision and Transfer Learning. In this talk, we’ll be looking at a framework - Snorkel BeamBell - a framework leveraging Stanford’s Snorkel library for Weak Supervision and Apache Beam for large scale Weak Supervision Learning for online labeling of large amounts of data that can continuously learn new classification models based on Stateful Learning Functions and user feedback.
