---
title: "A Beginners Guide to Avro and Beam Schemas Without Smashing Your Keyboard"
slug: a-beginners-guide-to-avro-and-beam-schemas-without-smashing-your-keyboard
speakers:
 - Devon Peticolas
topics:
 - Architecture
room: Horizon
time_start: 2023-06-13 12:00:00
time_end: 2023-06-13 12:50:00
day: a
timeslot: e
timeorder: 0
language: 
live_url: 
slides: 2023/Devon-AvroSchemas.pdf
video: https://youtu.be/lvAdyEm9chI
track: concurrent
tags:
---

This beginner-friendly talk will cover everything I wish I had known when I started writing batch and streaming Beam jobs that use Avro-Schema-encoded data and Beam-Schema-aware PCollections.
 
Apache Avro is a popular data serialization format that uses schemas for cross-language serializing and deserializing data. Apache Beam provides a type system for records called “Schemas,” which allows for cross-language type sharing, easy type conversion, and an easy way to share PTransforms between types. Using an Avro Schema for external data sources and Beam Schemas for the internal PCollections is a powerful combination plagued with beginner-unfriendly nuanced differences.
 
In this talk, we will cover:
 
 - How we use Avro for our Streaming and Batch data sources and how Avro enables powerful workflows with PubSub, Google Cloud Storage, and BigQuery.
 
 - How we manage internal and external representations of our data types with Beam Schemas and help us write simpler jobs that share more code.
 
 - How using Avro and Beam Schemas in conjunction allows us to seamlessly deploy every job as either streaming or batch at the flip of a Pipeline Option and how you can do the same.
 
 - How Oden migrated from JSON to Avro and reduced our Pubsub and Dataflow costs by over 50%.