---
title: "From taming energy market data to hyperparameter hunting at scale: leveraging Apache Beam & BigQuery"
slug: from-taming-energy-market-data-to-hyperparameter-hunting-at-scale-leveraging-apache-beam-bigquery
speakers:
 - Nicholas Bonfanti
 - Matteo Pacciani
topics:
 - Scalability & Performance
 - Unified Data Processing
room: The Bandshell
time_start: 2025-07-08 11:45:00
time_end: 2025-07-08 12:10:00
track: 
day: 20251
gridarea: "7/2/8/4"
timeslot: 7
images: 

slides: 2025/from-taming-energy-market-data.pdf
video: https://youtu.be/WJgpQAP1Jfk
---

This session explores how Apache Beam handles the end-to-end workflow for Italian energy market analytics, including forecasting electricity demand, natural gas demand, and renewable generation.

We'll demonstrate its power as a robust ETL tool for parsing and processing diverse data sources, using Google BigQuery as the central data warehouse. These sources range from millions of XML files detailing point-of-delivery (POD) electricity demand to ECMWF-generated GRIB meteorological files, among others.

Building on this foundation, the session covers Beam's role in scalable machine learning, detailing its use for distributed Bayesian hyperparameter searches over thousands of models, efficient retraining with optimized parameters over newly-parsed data, and large-scale distributed inference.