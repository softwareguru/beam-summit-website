---
title: "Mapping Data to FHIR with Apache Beam"
slug: mapping-data-to-fhir-with-apache-beam
speakers:
 - Alex Fragotsis
topics:
 - Architecture
 - Use case
 - Templates
 - Python
room: Horizon
time_start: 2023-06-13 14:30:00
time_end: 2023-06-13 14:55:00
---

A common use case across various teams at League is to to map regular data into its FHIR format (Fast Healthcare Interoperability Resources). This is not straightforward as it requires an understanding of the FHIR format, the original data source, as well as the mapping pipeline in Dataflow itself, owned by the data platform team. As a result, this causes a bottleneck on a single team, leading to inefficient and repeated work. 
 
 
 
 While the data comes from many different sources, the use case of mapping a certain data format into FHIR is actually quite a repeated pattern regardless of whether it is required in real-time or batch, or where the data the source of the data is. The solution: 
 
 We developed a reusable self-serve system based on Apache Beam to make it easier for other teams develop and deploy their own mappers easily using Python UDFs. Now with minimal guidance from the data platform team, any team can write their own mapper and deploy a batch OR real-time dataflow job, without needing the dataflow/infra knowledge. The job template handles everything from the reading of the data from the source (PubSub, BigQuery, GCS) and the writing to the destination (Cloud Healthcare API), including error handling and alerting.