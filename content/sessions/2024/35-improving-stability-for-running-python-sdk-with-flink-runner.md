---
title: "Improving Stability for Running Python SDK with Flink Runner"
slug: improving-stability-for-running-python-sdk-with-flink-runner
speakers:
 - Lydian Lee
topics:
 - Kubernetes
 - Python
 - Architecture
room: Walker Canyon
time_start: 2024-09-04 16:30:00
time_end: 2024-09-04 16:55:00
day: 20241
gridarea: "14/3/15/4"
timeslot: 35

images:
 - /images/sessions/2024/improving-stability.png
slides: 2024/ImprovingstabilityforrunningPythonSDKwithflinkrunner.pdf
video: 
---

In this session, we will explore our journey to improve the stability of our Flink application using the Python Beam SDK runner, with a particular focus on memory tuning. Our initial setup faced significant challenges, including frequent task manager disconnections and ambiguous error logs, often hinting at out-of-memory (OOM) issues. Despite no clear indicators of high memory usage, the instability worsened after transitioning from the Lyft K8s operator to the Apache Flink operator. 

Key points include: 
- Initial Setup Challenges: Both the Python worker harness and the Flink task manager running in the same container, leading to frequent disconnections.
- Diagnosing the Problem: Despite no high overall memory usage, the task manager frequently reported being unavailable, suggesting potential OOM issues.
- Operator Differences: The Lyft K8s operator reserved 20% of memory for the system, while the Apache Flink operator allocated all memory to taskmanager.memory.process.size, causing OOM on the Python worker harness due to lack of reserved system memory.
- Solution Implementation: Separating the Python worker harness into a separate container and using external to connect to Python, resulting in enhanced stability.
- Additional Benefits: Improved resource utilization and flexibility by assigning specific memory requests and limits to the sidecar container running Python.