---
id: 
title: "Vega: Scaling MLOps Pipelines at Credit Karma using Apache Beam and Dataflow"
url: /sessions/vega-mlops
speakers:
 - Debasish Das
 - Vishnu Venkataraman
time_start: 2022-01-01T17:00:00.000Z.000Z
time_end: 2022-01-01T18:00:00.000Z.000Z
block: 
slot: 
---

At Credit Karma, we enable financial progress for more than 100 million of our members by recommending them personalized financial products when they interact with our application. In this talk we are introducing our machine learning platform that uses Apache Beam and Google Dataflow to build interactive and production MLOps pipelines to serve relevant financial products to Credit Karma users.



Vega, Credit Karma’s Machine Learning Platform, uses Bigquery, Apache Beam, Distributed Tensorflow and Airflow for building MLOps pipelines. Apache Beam with Dataflow Runner is used in Vega for scalable feature transformations, model chaining, batch scoring of Tensorflow and PMML models, model analysis and online model monitoring.



In this session we will walk you through the various scalable Apache Beam jobs that we use for training, deploying, monitoring and refreshing the models for our recommendation system. Overall, our MLOps pipelines leveraging Apache Beam have improved the efficiency of ML Engineering. Using our pipelines we deploy more than 500 Tensorflow and Tree models every week to production.