---
id: b02r
title: "Ingesting and Processing Level 3 Order Book Streams"
url: /sessions/ingesting-processing-book-streams
speakers:
 - Daniel Tyreus
time_start: 2021-08-05T15:50:00.000Z
time_end: 2021-08-05T16:00:00.000Z
block: b
slot: 02
summary: Use case of Beam to ingest and process billions of order book messages for cryptocurrency.
slides: 2021/b02-Ingesting.pdf
video: https://youtu.be/5337vr4-6lo
---

Financial exchanges maintain a real-time list of orders for buyers and sellers of instruments such as equities and cryptocurrencies. The most detailed view of an order book consists of every unique order at every price level. As the order book changes, exchanges emit messages that we can store and analyze at a later time. At Cambrian we are using Beam and GCP PubSub to ingest and process billions of order book messages per week. We use the processed data to back test and tune our trading algorithms.
