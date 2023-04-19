---
id: a09s
title: "Deduplication: Where Beam Fits In"
url: /sessions/deduplication
speakers:
 - Jeff Klukas
time_start: 2021-08-04T20:00:00.000Z
time_end: 2021-08-04T20:25:00.000Z
block: a
slot: 09
slides: a09-Deduplication.pdf
video: https://youtu.be/9OfJKDs3h40
---

This session will start with a brief overview of the problem of duplicate records and the different options available for handling them. We'll then explore two concrete approaches to deduplication within a Beam streaming pipeline implemented in Mozilla's open source codebase [0] for ingesting telemetry data from Firefox clients.

We'll compare the robustness, performance, and operational experience of using the deduplication built in to PubsubIO vs. storing IDs in an external Redis cluster and why Mozilla switched from one approach to the other.

Finally, we'll compare streaming deduplication to a much stronger end-to-end guarantee that Mozilla achieves via nightly scheduled queries [1] to serve historical analysis use cases.

* [0] https://github.com/mozilla/gcp-ingestion/tree/main/ingestion-beam
* [1] https://github.com/mozilla/bigquery-etl/blob/main/bigquery_etl/copy_deduplicate.py