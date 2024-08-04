---
title: "Streaming Modes & Vertical Scaling for Cost Effectiveness to Customers"
slug: streaming-modes-vertical-scaling-for-cost-effectiveness-to-customers
speakers:
 - Sharan Teja Malyala
topics:
 - Runners
 - Use case
room: Hamina (MP4)
time_start: 2024-09-05 12:00:00
time_end: 2024-09-05 12:25:00
day: 2
gridarea: "6/4/7/5"
timeslot: 49
images:
 - /images/sessions/2024/streaming-modes.jpg 
---

This talk will explain three capabilities of Dataflow that may help customers save costs:
1. Streaming modes. Recently, Dataflow introduced a new mode "At least once" for streaming jobs which may help customers who do not have "exactly once" requirement save some costs.
2. Vertical scaling that prevents job failures from OOM's. How Dataflow's vertical scaling recovers from OOM situations and prevents job failures.
3. Dynamic Thread Scaling. Dataflow tries to maximize the worker utilisation with this feature and avoids using up more workers. 