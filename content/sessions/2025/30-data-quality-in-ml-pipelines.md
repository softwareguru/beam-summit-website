---
title: "Data Quality in ML Pipelines"
slug: data-quality-in-ml-pipelines
speakers:
 - Pritam Dodeja
time_start: 2025-07-09 11:30:00
time_end: 2025-07-09 11:55:00
room: Star Leaved Gum
track:
topics: 
 - Scalability & Performance
 - Unified Data Processing
day: 20252
gridarea: "7/4/8/6"
timeslot: 30
images: 

slides:
video: 
---


You know what somebody should do? Somebody should invent a way for data processing systems to talk to each other. All these different formats, batching, streaming, analytics, machine learning. It's way too much.

What? Somebody already did this? When? 2016? What? That's crazy! When's the paper from? 2015? Ridiculous! (Technical paper at the end).

That technology is Apache Beam and in this year's summit I will show how to manage data quality in ML pipelines. In this talk, I'm going to demonstrate a few beam powered tfx components. These components do the following things:

Take an arbitrary python function, and apply it at scale to tensors using apache beam. This is, in a sense, at the confluence of data preparation and operations on tensors that happens in mlops at scale. It doesn't add to the tensor graph, but provides a way to spot bad data (among other things). It potentially adds a bit to the picture at https://www.tensorflow.org/tfx

Another one filters data. So you have some indicator for data quality. Apply the filter. Cleaner data on the other side. You don't need to know any of the complexity of scaling etc., just provide a simple python function.

And what connects the two? A JSONSampler. This is the third component. It takes these (partially) opaque protocol buffers, and provides easy to interact with jsonl versions that come from the same population. This way, you can actually see the data that's flowing through your pipelines, not just statistical distributions of that data. In the JSONSampler, you can also specify a sampling percentage and your data is delivered to you, with all of the transformation, scale, metadata management handled for you. All powered by Apache Beam.

Here's the dataflow paper: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43864.pdf
 
And here's the tfx paper: https://arxiv.org/pdf/2010.02013

If you find any of these things interesting, come to my talk!