---
title: "From Binary to Breach Detection: Normalizing OT and Mixed Logs for SecOps with Apache Beam"
slug: from-binary-to-breach-detection-normalizing-ot-and-mixed-logs-for-secops-with-apache-beam
speakers:
 - Canburak Tümer
topics:
 - Ecosystem and Community with Modern Data Tools
room: Hackberry
time_start: 2026-06-23 14:40:00
time_end: 2026-06-23 15:10:00
---

Modern Security Operations Centers (SOCs) face a massive data problem: the "Data Wall." As IT, OT, and IoT environments converge, security teams are forced to ingest a chaotic mix of structured, unstructured, and even proprietary binary logs (such as S7 or Modbus) into their SIEM platforms. Traditional ingestion tools often fail when faced with the need for real-time normalization, massive scale, and complex data transformation.

In this session, we will explore how Apache Beam serves as the critical "bridge" in this ecosystem, enabling the transformation of disparate manufacturing and enterprise logs into a standardized Unified Data Model (UDM). Drawing from real-world implementations using Google Cloud Dataflow and SecOps (Chronicle), we will dive into:

Handling the "Mixed Stream" Challenge: How to use Beam to demultiplex and route mixed log types from a single Kafka or Pub/Sub source.

Decoding the Undecodable: Patterns for processing proprietary binary protocols and industrial equipment logs at scale.

Architecting for Reliability: Implementing Dead Letter Queues (DLQs) and rejected message sinks to ensure zero data loss during ingestion.

The Ingestion Decision Tree: A comparison of ingestion methods (API vs. GCS vs. Pub/Sub) and how to choose the right sink for your security requirements.

Attendees will leave with a blueprint for building resilient, scalable security data pipelines that turn raw industrial signals into actionable security intelligence.