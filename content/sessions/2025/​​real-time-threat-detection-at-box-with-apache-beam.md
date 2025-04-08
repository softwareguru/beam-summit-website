---
title: "​​​​Real-time Threat Detection at Box with Apache Beam"
slug: ​​real-time-threat-detection-at-box-with-apache-beam
speakers:
 - Abhishek Mishra
time_start: 2025-07-08 09:10:00
time_end: 2024-07-08 10:05:00
room: 
track: 
 - Real-time data applications
 - Emerging trends
 - Scalability & Performance
day: 
timeslot: 
gridarea: 
images: 

slides:
video: 
---

Box faces a constant barrage of sophisticated cybersecurity threats. This session dives into how Box leverages the Apache Beam Python SDK, combined with cutting-edge machine learning techniques, to build a real-time threat detection system. We'll explore the unique challenges of processing high-volume, real-time data streams to identify and mitigate threats before they can impact our customers. The presentation will focus on:

- The architecture of our Beam-based unified threat detection pipeline, highlighting the integration of machine learning models.
- How we utilize a transformer-like structure for time-series analysis in ransomware detection. This includes discussing the advantages of transformers for capturing long-range dependencies and contextual information in sequential data (e.g., system logs, network traffic).
- Specific real-time data challenges encountered at Box's scale (e.g., data velocity, variety, veracity, late-arriving data, schema evolution) and how they impact model training and inference.
- Practical techniques and Beam patterns used to address these challenges (e.g., windowing, triggering, state management, handling out-of-order data), ensuring data is prepared effectively for the machine learning model.
- Lessons learned and best practices for building robust, real-time threat detection systems with Apache Beam and transformer-based models.
- How the Python SDK of Apache Beam facilitated the integration of machine learning components into the streaming pipeline, specially the effective utilization of RunInference within the Beam pipeline to serve the transformer-based model and perform real-time predictions.
- Future directions for enhancing our threat detection capabilities, including exploring other advanced machine-learning architectures.