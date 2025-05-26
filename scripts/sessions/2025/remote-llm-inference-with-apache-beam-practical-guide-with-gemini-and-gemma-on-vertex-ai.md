---
title: "Remote LLM Inference with Apache Beam: Practical Guide with Gemini and Gemma on Vertex AI"
slug: remote-llm-inference-with-apache-beam-practical-guide-with-gemini-and-gemma-on-vertex-ai
speakers:
 - Taka Shinagawa
topics:
 - Emerging trends
room: Palisades
time_start: 2025-07-08 12:45:00
time_end: 2025-07-08 13:10:00
---

Large Language Models offer powerful capabilities for data transformation, but reliably integrating them at scale into Apache Beam data pipelines presents challenges. Deploying powerful, large models (e.g., Gemma 27B, Llama 70B, DeepSeek R1) directly onto Beam workers via the RunInference API is often infeasible due to resource constraints, multi-GPU complexity, cost, and lack of serving optimizations. Furthermore, many frontier models like Gemini are only available via APIs. Therefore, this session focuses on effective Remote LLM inference integration with Apache Beam.

This practical session guides you through implementing LLM pipelines using Python and Apache Beam's RequestResponseIO feature. It will demonstrate building robust callers for remote endpoints, using the native Gemini API and Vertex AI Prediction API (hosting Gemma) as concrete examples. Learn essential performance tuning techniques crucial for managing latency, throughput, and reliability in these I/O-bound pipelines. Finally, discover compelling use cases and examples for building intelligent, scalable data processing solutions with Gemini and Gemma models.