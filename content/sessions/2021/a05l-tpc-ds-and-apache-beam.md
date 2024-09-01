---
id: a05l
title: "TPC-DS and Apache Beam - the time has come!"
url: /sessions/tpc-ds-and-apache-beam
speakers:
 - Alexey Romanenko
 - Ismael Mejía
time_start: 2021-08-04T17:00:00.000Z
time_end: 2021-08-04T17:45:00.000Z
block: a
slot: 05
summary: TPC-DS is the de-facto SQL-based benchmark framework used to measure database systems and Big Data processing frameworks. Beam introduced an early TPC-DS implementation last year but so far we have not started to use it to measure the state of the performance of Beam.
slides: 2021/a05-TPCDS.pdf
video: https://youtu.be/LVpAD79VQzI

---

TPC-DS is the de-facto SQL-based benchmark framework used to measure database systems and Big Data processing frameworks. Beam introduced an early TPC-DS implementation last year but so far we have not started to use it to measure the state of the performance of Beam.

In this talk we will introduce TPC-DS and how it works in general. We will present the different ways of running the TPC-DS benchmark on Beam via Beam SQL and “classical” Beam Java SDK, the issues that we have found trying to run TPC-DS on Beam and the current status of the project.

Also, we are going to discuss some issues related to Beam SQL, several performance optimisations, the challenges of fair benchmarking on distributed processing systems and how we expect to integrate TPC-DS with Beam’s CI tests to track regressions and improvements in the future.