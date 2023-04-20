---
title: "Multi-language pipelines: a unique Beam feature that will make your team more efficient"
slug: multi-language-pipelines-a-unique-beam-feature-that-will-make-your-team-more-efficient
speakers:
 - Chamikara Jayalath
topics:
 - Cross language
room: Upper Bay
time_start: 2023-06-13 11:00:00
time_end: 2023-06-13 11:50:00
---

Apache Beam offers a unique feature named multi-language pipelines. This feature allows you to use any Beam transform from any Beam pipeline irrespective of the language SDKs the transform or the pipeline is developed in. This allows Beam users to completely isolate development of transforms from development of pipelines. Think of an organization with development teams working on features built using different languages. Now each team can focus on developing transforms for the feature in their preferred language. After transforms are developed, they can be used by any team inside or outside the organization in Beam pipelines developed using any Beam SDK language. Teams no longer have to develop the same feature in different languages or compromise on the features based on the library support of the pipeline SDK. This allows development teams to be more efficient and allows organizations to significantly reduce the financial overheads related to feature development and maintenance. In this talk, we’ll deep dive into how Apache Beam’s multi-language pipelines are executed and look closely at some example multi-language pipelines.