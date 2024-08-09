---
title: "How we Migrated our JSON DB to a Relational DB using Apache Beam / Dataflow"
slug: how-we-migrated-our-json-db-to-a-relational-db-using-apache-beam-dataflow
speakers:
 - Lakshmanan Arumugam
topics:
 - Use case
 - Cross language
 - Python
 - Runners
 - Templates
track: Use case
room: Mariposa Grove
time_start: 2024-09-04 12:00:00
time_end: 2024-09-04 12:25:00
day: 1
gridarea: "7/2/8/3"
timeslot: 12
images:
 - /images/sessions/2024/how-we-migrated.jpg 
---

We migrated ~5 TB (~2 billion rows) of production NoSQL DB to a Postgres DB without application downtime. This involved data export from Cloud Datastore (NSQL DB), normalization (from JSON to SQL schema) and then data import into Postgres. We used two different Apache Beam pipelines in the process.

1) Exporting data from cloud datastore - for this we used Google developed dataflow template (written in java). *
2) Normalize and import into Postgres - we wrote our own custom Apache Beam pipeline that transforms every JSON row into Postgres compatible schema and batches the normalized rows for ingestion into Postgres (written in python). **

Data migration took about ~16 hrs with this approach using the beam pipeline (as opposed to our initial estimate of 5 days using other batch scripts with parallel computing) 

Advantages: 
- Time: made our migration faster 
- Repeatability and error handling: easy to rerun for records that were failed to import (and easy rerun for any new records created in datastore during the migration etc.,) 
- Managed scaling with Google Dataflow 

*pipeline 1: https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/src/main/java/com/google/cloud/teleport/templates/DatastoreToText.java 
** pipeline 2: we wrote custom beam DoFn transforms in python(+sqlalchemy) and built a pipeline to ingest data into Postgres with error handling.