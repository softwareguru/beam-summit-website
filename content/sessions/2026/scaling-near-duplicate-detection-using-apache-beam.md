---
title: "Scaling near-duplicate detection using Apache Beam"
slug: scaling-near-duplicate-detection-using-apache-beam
speakers:
 - Pablo Rodriguez Defino
topics:
 - Unified Data Processing with ML Integration
room: Pitch Pine
time_start: 2026-06-22 16:15:00
time_end: 2026-06-22 16:45:00
---

Abstract
Deduplicating trillion-token corpora is a critical requirement for modern LLM pre-training, yet it remains a significant engineering bottleneck. Traditional approaches often rely on fragmented pipelines—massive batch jobs for historical cleaning paired with separate, lightweight scripts for real-time ingestion. This fragmentation leads to logic drift, where signatures generated in the stream may not align with batch history, creating inconsistencies that are difficult to debug.

This session presents a fully native Apache Beam implementation of the MinHash Locality-Sensitive Hashing (LSH) algorithm. We demonstrate a Unified Architecture that uses a single Java codebase to handle both large-scale "Batch Bootstrapping" and low-latency streaming workflows.

Key Technical Takeaways:

Multi-Level Parallelism: Decomposing MinHash LSH into document-level, element-level, and global-level parallel transforms within Beam.

Unified State: Implementing an external "Global Memory" using high-throughput state stores to bridge the gap between processing modes.

Hardware Density: Offloading compute-intensive hashing to TPUs via Dataflow to drastically reduce the cost-per-token processed.

Reusable Components: Deploying low-latency membership inference to prevent "corpus poisoning" during live web crawls by reusing identical batch logic.

We will conclude with a live demonstration using the Common Crawl dataset, showcasing the pipeline's ability to intercept near-duplicate documents in real-time with zero logic drift.