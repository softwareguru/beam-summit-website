---
id: e2s
title: "Using Cross-Language pipeline to run Python 3 code with Java SDK"
url: /sessions/cross-language-pipeline-python-java
speakers:
  - Alexey Romanenko
time_start: 2020-08-28T16:30:00.000Z
time_end:   2020-08-28T16:50:00.000Z
day_num: 5
---

There are many reasons why we would need to execute Python code in Java SDK pipelines and vice versa (e.g. Machine Learning libraries, IO connectors, user’s Python code, etc) and several different ways to do that. WIth the End of Life of Python 2 started this year, it’s getting more challenging since not all old solutions still work well for Python 3. One of the potential options for this could be using a Cross-Language pipeline and Portable Runner in Apache Beam.

In this talk I’m going to tell about what the cross-language pipelines in Beam are, how to create a mixed Java/Python pipeline, how to set up and run it, what kind of requirements and pitfalls we can expect in this case. Also, I’ll show a demo of a use case where we need to execute a custom user’s Python 3 code in the middle of Java SDK pipeline and run it with Portable Spark Runner.