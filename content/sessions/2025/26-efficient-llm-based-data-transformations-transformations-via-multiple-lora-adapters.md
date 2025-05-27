---
title: "Efficient LLM-Based Data Transformations Transformations via Multiple LoRA Adapters"
slug: efficient-llm-based-data-transformations-transformations-via-multiple-lora-adapters
speakers:
 - Jasper Van den Bossche
topics:
 - Real-time data applications
 - Scalability & Performance
room: Palisades
time_start: 2025-07-09 10:30:00
time_end: 2025-07-09 10:55:00
track: 
day: 20252
gridarea: "5/4/6/6"
timeslot: 26
images: 

slides:
video:
---

LLM-based data transformations are very powerful for processing unstructured data, organizations often struggle to deploy these tools at scale, particularly when tailoring them to specific custom use cases. This talk will explore how to efficiently serve multiple LoRA (Low-Rank Adaptation) adapters on a single base model, enabling task-specific transformations within Apache Beam pipelines and addressing the scalability challenges head-on.
LoRA adapters enable efficient fine-tuning of large language models by updating only a subset of parameters, making it possible to tailor models for specific tasks without the computational overhead of full fine-tuning. This approach is particularly valuable when working with private data or deploying cost-effective models.
We will explore how inference servers like vLLM and NVIDIA NIM can dynamically swap LoRA adapters in real-time, optimizing resource utilization while seamlessly integrating with Apache Beam for batch and streaming data processing. This integration ensures scalable, cost-effective, and adaptable workflows for various data sources.
We'll demonstrate this approach through a real-world implementation where we process different document types using custom LoRA adapters for each—from invoices to legal contracts—achieving specialized extraction capabilities while maintaining a single model infrastructure.
The talk will cover: (1) an overview of LoRA adapters and their efficiency benefits, (2) configuring inference servers for dynamic adapter swapping, and (3) implementing a complete Apache Beam pipeline for production-ready unstructured data processing.