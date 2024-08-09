---
title: "Multi-Modal LLM Data Processing with Apache Beam"
slug: multi-modal-llm-data-processing-with-apache-beam
speakers:
 - Konstantin Buschmeier
 - Jasper Van den Bossche
topics:
 - ML
 - Python
track: ML & AI
room: Mariposa Grove
time_start: 2024-09-04 15:00:00
time_end: 2024-09-04 15:25:00
day: 20241
gridarea: "11/2/12/3"
timeslot: 25
images:
 - /images/sessions/2024/multi-modal-llm.jpg 
---

Large language models are well known for their performance on generation tasks like summarization but they also excel at many classical tasks like classification, named-entity recognition, or information extraction. Multi-modal LLMs similarly achieve state of the art performance on document understanding. This makes them vital for modern data processing pipelines.

Apache Beam is a powerful framework to define and execute batch and streaming data processing pipelines. Recent releases introduced many tools to facilitate machine learning workflows like ML Transforms, RunInference, and Enrichment transform.

In this talk we will introduce an application that combines Beam’s ML capabilities and LLMs to extract product requests from various document types of customer emails to facilitate the automatic fulfillment of orders.