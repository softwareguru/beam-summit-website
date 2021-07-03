---
id: b07l
title: "Multi-language Pipelines for improving usability and reducing overheads"
url: /sessions/multi-language-pipelines
speakers:
 - Chamikara Jayalath
time_start: 2021-08-05T18:00:00.000Z
time_end: 2021-08-05T18:50:00.000Z
block: b
slot: 07
summary: Apache Beam offers a novel and powerful framework named Multi-Language Pipelines that allows you to execute pipelines that employ multiple supported SDK languages.
---

Apache Beam offers a novel and powerful framework named Multi-Language Pipelines that allows you to execute pipelines that employ multiple supported SDK languages. With multi-language pipelines you can build and maintain transforms for one language but use them from all supported languages hence significantly increasing the usability of any transform that you develop. This can significantly reduce development overheads for any functionality that you hope to offer in the form of Beam transforms. Additionally, multi-language pipelines framework will allow you to reduce maintenance overhead related to Beam transforms that you develop since SDK languages other than the primary language where the transform is implemented just have to provide thin wrappers to make the transform usable. Multi-language pipelines framework is built on top of the Apache Beam portability framework and supported by Beam portable runners and Google Cloud Dataflow.