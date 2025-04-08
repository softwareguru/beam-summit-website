---
title: "Many Data Formats, One Data Lake"
slug: many-data-formats-one-data-lake
speakers:
 - Peter Wagener
time_start: 2025-07-08 09:10:00
time_end: 2024-07-08 10:05:00
room: 
track: 
 - Connecting disparate systems with modern data architectures
day: 
timeslot: 
gridarea: 
images: 

slides:
video: 
---

Apache Beam has the flexibility to handle a wide variety of different types of text-based data: CSV, Avro, Parquet, Iceberg, ... they can all be inputs and / or outputs for your data processing projects. The question quickly becomes, which do you choose?

Our answer is a bit surprising: All of them. If you can define the schema appropriately within the pipelines, you can use the file format that makes the most sense for each use case.

In this talk, learn how we have leveraged Avro as our schema definition language and implemented a small Beam library that allows us to consume a variety of formats (APIs, CSV, Avro, Parquet, etc.) and output it to almost any other format. We use this to blend census data from APIs with proprietary customer data CSVs, data from for-profit data providers via Parquet, and other inputs into a single data lake.

When choosing output formats, no single choice will ever be perfect for every user. We choose how to output the results based on who will be using the data:

- Teams with very little technical background? Probably CSV.
- Other data pipelines? Probably Avro.
- Data Lakehouse Systems? Probably Parquet.
- Bleeding-Edge Technical Users? Probably Iceberg.

The Avro schema is the pivot point for all these to be trustworthy. The trick is in ensuring the processing code has minimal knowledge about the file formats on either end... until it has to. Only in the very beginning and at the very end does it truly care.

This talk will detail our motivations and give a code-level deep dive into how you can build a similar system for your own data lake users.