---
title: "How Beam serves models with vLLM"
slug: how-beam-serves-models-with-vllm
speakers:
 - Danny McCormick
time_start: 2025-07-08 16:15:00
time_end: 2025-07-08 16:40:00
room: Horizon Hall
track:
topics: 
 - Emerging trends
 - Scalability & Performance
day: 20251
gridarea: "15/2/16/4"
timeslot: 19
images: 

slides:
video: 
---

Serving ML models at scale is increasingly important, and Beam's RunInference transform is a great tool to do this. At the same time, models are getting larger and larger, and it can be hard to fit them into your CPU or GPU and to serve them efficiently. In particular, serving large language models efficiently has grown in importance and difficulty as models have continued to grow.

vLLM is an open-source library specifically designed for high-throughput and low-latency LLM inference. It optimizes the serving of LLMs by employing several specialized techniques, including continuous batching.

This talk will explore how Beam integrated vLLM so that a Beam pipeline can spin up a vLLM server in the middle of its execution and run inference locally. Attendees can expect to come away with an understanding of how vLLM works, how Beam loads and serves models with or without vLLM, and how they can use Beam to serve their models (large or small).