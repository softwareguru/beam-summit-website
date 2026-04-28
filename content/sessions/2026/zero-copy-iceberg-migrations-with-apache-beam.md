---
title: "Zero-Copy Iceberg Migrations with Apache Beam"
slug: zero-copy-iceberg-migrations-with-apache-beam
speakers:
 - Ahmed Abualsaud
topics:
 - Emerging Trends (AI/ML and Lakehouse Architectures)
room: Pitch Pine
time_start: 2026-06-23 11:00:00
time_end: 2026-06-23 11:30:00
---

Traditionally, converting a Parquet-based data lake to Iceberg required a hidden tax of rewriting every single data file. For organizations managing petabyte-scale datasets, this compute overhead and the associated cloud bill are often dealbreakers.

This talk introduces a more efficient path using Apache Beam’s new AddFiles feature to perform zero-copy migrations, registering existing Parquet files directly into an Iceberg table without moving a single byte.

In this session, we’ll explore:
- A practical framework for modernizing your lakehouse with minimal compute overhead.
- Live demos showcasing (1) the Batch approach for migrating historical data and (2) the Streaming approach for registering incoming files in real-time
- A decision matrix for choosing between tradition rewrites and zero-copy registration