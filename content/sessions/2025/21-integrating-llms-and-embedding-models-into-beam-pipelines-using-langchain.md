---
title: "Integrating LLMs and Embedding models into Beam pipelines using langchain"
slug: integrating-llms-and-embedding-models-into-beam-pipelines-using-langchain
speakers:
 - Ganesh Sivakumar
time_start: 2025-07-08 16:45:00
time_end: 2025-07-08 17:10:00
room: Horizon Hall
track:
topics: 
 - Emerging trends
 - Unified Data Processing
 - Ecosystem & Community
day: 20251
gridarea: "16/2/17/4"
timeslot: 21
images: 

slides:
video: 
---

Large language models (LLMs) have transformed how we process and generate text. In this session, I'll talk about Langchain-Beam, an open-source library that integrates LLMs and embedding models into Apache Beam pipelines as transform using LangChain.

We will explore how Langchain-Beam transform performs remote LLM inference with OpenAi and Anthropic models. Provide data processing logic as prompt and use the models to transform the data based on the prompt. Use embedding models to generate vector embeddings for text in pipeline and Learn about real-world use cases Like,

1. Embedding generation pipelines to update LLM application's knowledge base - Loading data from source, generating text embeddings using openai's models and writing it to vector database. 
2. Perform NLP based tasks like summarization and classification in beam pipeline using models from various models providers and with open source models using ollama. 

Repository : https://github.com/Ganeshsivakumar/langchain-beam