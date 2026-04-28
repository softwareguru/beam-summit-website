---
title: "The Apache Lakehouse Ecosystem and Apache Beam's Role in It"
slug: the-apache-lakehouse-ecosystem-and-apache-beam-s-role-in-it
speakers:
 - JB Onofré
topics:
 - Ecosystem and Community with Modern Data Tools
room: Pitch Pine
time_start: 2026-06-22 11:00:00
time_end: 2026-06-22 11:30:00
---

The modern data landscape has converged on the lakehouse architecture — a paradigm that unifies the scalability of data lakes with the governance and performance of traditional data warehouses. Open table formats such as Apache Iceberg, Apache Hudi, and Delta Lake now serve as the foundation for this ecosystem, enabling ACID transactions, schema evolution, and time-travel queries directly on cloud object storage.

Yet as organizations adopt these formats at scale, a critical question emerges: how do data teams move data into and across these tables in a portable, reliable, and runtime-agnostic way?
This talk explores where Apache Beam fits into the lakehouse picture. We will examine how Beam's unified programming model and runner abstraction make it a natural choice for lakehouse ingestion and transformation pipelines — whether targeting Apache Iceberg via the managed I/O connector, streaming CDC events into Hudi, or orchestrating multi-table workflows across batch and streaming workloads in a single pipeline.
Attendees will come away with a clear mental model of the lakehouse ecosystem's key components, an understanding of the trade-offs between format choices, and practical insight into how Apache Beam's portability layer complements — rather than competes with — engines like Apache Flink and Apache Spark in a modern data platform.