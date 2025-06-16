---
title: "Building Banking Synthetic Data for a Lakehouse with Gemma"
slug: building-banking-synthetic-data-for-a-lakehouse-with-gemma
speakers:
 - Alberto Lopez Serna
topics:
 - Emerging trends
room: Horizon Hall
time_start: 2025-07-09 10:30:00
time_end: 2025-07-09 10:55:00
track: 
day: 20252
gridarea: "5/2/6/4"
timeslot: 25
images: 

slides:
video:
draft: true
---

Building a Beam pipeline to preprocess, generate and validate Synthetic data for a Datawarehouse migration into GCP.

Why It’s New: Synthetic data generation is a hot topic, and using GenAI with Beam is a novel approach, we were inspired by https://developers.googleblog.com/en/gemma-for-streaming-ml-with-dataflow/ and decided to use Beam for preprocessing, generation and validation to scale synthetic data generation from 1 up to 3000 tables and leverage the model forkeeping primary keys referencial integrity among them.

Tech Stack: Apache Beam, TensorFlow, Google Cloud.