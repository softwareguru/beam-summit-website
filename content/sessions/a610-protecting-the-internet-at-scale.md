---
slot: a610
title: "Protecting the Internet at Scale"
url: /sessions/protecting-the-internet-at-scale
speakers:
 - Alfredo Gimenez
time_start: 2022-07-18 15:00:00 -0500 CDT
time_end:   2022-07-18 15:50:00 -0500 CDT
day: a
timeslot: 6
room: 1
timeorder: 0
track: case-study

---

At BlueVoyant, we process billions of cyber events per second in an effort to secure the supply chains of several high-stakes Fortune 500 companies. Cyber attacks exploit the weakest links in a target company, and modern tech infrastructures are composed of more third-party dependencies than ever before. Our Third-Party Risk (3PR) product requires us to monitor, analyze, and pinpoint weaknesses throughout hundreds of thousands of third party entities, each consisting of tens to millions of assets that may be exploited. We do this by stream-processing billions of cyber events collected across the entire internet from a variety of disparate data sources and formats, using Apache Beam on Google Dataflow, in a project we call Prophet.
 
In this talk we'll discuss how we turned Prophet into a reality, focusing on four major computational challenges we overcame: indexing disparate cyber event data in a common data warehouse, ingesting billions of events per second, searching and ETL-ing petabytes of results in a distributed stream pipeline, and running advanced cyberanalytics on this data on-demand. As a result of these efforts, Prophet can identify the many points of weakness in an enormous and complex ecosystem of third-party dependencies, and our team of expert cyber analysts are able to respond to emerging cyber attacks immediately by querying Prophet for vulnerability and exploit fingerprints within petabytes of data going back over a year of history.