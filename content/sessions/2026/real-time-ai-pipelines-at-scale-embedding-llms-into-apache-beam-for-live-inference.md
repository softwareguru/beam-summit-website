---
title: "Real-Time AI Pipelines at Scale: Embedding LLMs into Apache Beam for Live Inference"
slug: real-time-ai-pipelines-at-scale-embedding-llms-into-apache-beam-for-live-inference
speakers:
 - Samir Sengupta
topics:
 - Agentic Architectures
 - Unified Data Processing with ML Integration
 - Real-time ML-Driven Data Insights
room: Hackberry
time_start: 2026-06-22 14:30:00
time_end: 2026-06-22 15:20:00
---

As AI moves from experimentation to production, the hardest challenge isn't building a model. It's getting it to run reliably on live data at scale. In this talk, I'll walk through how I architected production-grade pipelines that embed LLMs and RAG systems directly into Apache Beam, enabling real-time inference on high-velocity data streams.

We'll cover:
How to integrate HuggingFace and vLLM models into Beam transforms for low-latency inference
Designing a RAG pipeline inside Beam using vector databases (Pinecone, FAISS) for semantic search on streaming data
Handling the cost and throughput challenges of running LLMs in a pipeline (quantization, batching, GPU optimization)
Deploying the full stack on AWS Bedrock + SageMaker with Kubernetes orchestration
Real benchmark results: how we cut inference costs by 50% while improving reasoning accuracy by 35%

This isn't a toy demo. It's a battle-tested architecture handling 10M+ daily events with 99.9% uptime. Attendees will leave with concrete patterns they can apply to fraud detection, anomaly detection, semantic search, and personalized recommendation systems.