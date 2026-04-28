---
title: "The Agent-Driven Pipeline: Real-Time Data Validation & Modeling using Apache Beam, MCP, and GenAI"
slug: the-agent-driven-pipeline-real-time-data-validation-modeling-using-apache-beam-mcp-and-genai
speakers:
 - Jay Jayakumar
 - Pablo Costamagna
topics:
 - Agentic Architectures
 - Unified Data Processing with ML Integration
 - Ecosystem and Community with Modern Data Tools
room: Hackberry
time_start: 2026-06-23 13:45:00
time_end: 2026-06-23 14:35:00
---

Data pipelines need reliable quality checks, but hardcoded validation rules struggle to keep up with changing business needs. This session shows how to simplify data quality by using an AI agent to figure out the rules, and Apache Beam to do the heavy lifting of actually checking the data.

We will walk through a practical setup where an AI Data Validation Agent takes the lead. Using tools like Retrieval-Augmented Generation (RAG) and the Model Context Protocol (MCP), the agent reads your live data catalogs and governance rules to understand exactly what your data should look like today.

But the agent doesn't process the data itself. Instead, it automatically triggers Apache Beam (Dataflow) to run these custom checks. The agent translates the business rules into logic specifically built for Apache Beam, allowing Beam to do what it does best: process huge amounts of data efficiently.

What You Will See:

Smart Triggering: How an AI agent figures out what needs checking and automatically spins up Apache Beam pipelines exactly when they are needed.

Building Beam-Ready Rules: How the agent translates everyday business rules and data catalog metadata into SQL and validation steps that plug right into your Apache Beam workflow.

Distributed Execution: How Apache Beam takes the handoff from the agent, using its distributed processing power to check massive datasets for errors and schema changes quickly and reliably.