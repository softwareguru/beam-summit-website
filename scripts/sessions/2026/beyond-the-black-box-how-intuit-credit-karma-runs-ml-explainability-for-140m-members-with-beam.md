---
title: "Beyond the Black Box: How Intuit Credit Karma Runs ML Explainability for 140M Members with Beam"
slug: beyond-the-black-box-how-intuit-credit-karma-runs-ml-explainability-for-140m-members-with-beam
speakers:
 - Raj Katakam
 - Pallav Anand
topics:
 - Scalability and Performance with Optimized Storage
 - Unified Data Processing with ML Integration
 - Ecosystem and Community with Modern Data Tools
room: Pitch Pine
time_start: 2026-06-22 14:00:00
time_end: 2026-06-22 14:30:00
---

Everyone talks about explainable AI. Almost no one runs it at scale in production.

The dirty secret of ML explainability is that it's easy in a notebook and brutally hard in the real world. Feature attribution libraries are compute-intensive and don't parallelize out of the box. Models retrain and refresh continuously, making it impossible to guarantee that an explanation matches the model that actually made the prediction. Raw feature attributions are cryptic to everyone except the data scientist who built the model — but business stakeholders and end users all need to understand them in terms meaningful to them. And at the scale of billions of predictions a day across 140 million members, none of the off-the-shelf approaches hold up.

At Intuit Credit Karma, we built and operate a production ML explainability platform on Apache Beam and Dataflow — and we'll show you exactly how. Beam's unified programming model gave us the horizontal scalability to run attribution computation across massive prediction volumes without blowing up cost or latency. Its flexible I/O and pipeline composition patterns let us stitch together a three-stage architecture: feature log preparation, distributed attribution generation grouped by model version, and downstream delivery with correctness guardrails — all orchestrated on a daily cadence.

We'll walk through the real engineering decisions: how we used Apache Beam pipelines to group predictions by model version and load the corresponding model dynamically — ensuring explanations always reflect the exact model that made each prediction even as models refresh continuously in production; how we aggregated feature-level attributions into human-readable reason codes configurable for any audience; and how we designed the pipeline to be privacy-preserving by construction, with no sensitive data leaking through intermediate stages.

We'll also be honest about where Beam shines for this use case and where the rough edges are — including version compatibility with ML attribution libraries, managing model artifacts in distributed workers, and cost tradeoffs vs. managed explainability services.

Whether you're building explainability infrastructure, running large-scale batch ML pipelines, or just trying to understand what Apache Beam can do beyond ETL — this talk will show you what production explainability looks like when you build it the right way, at real scale.