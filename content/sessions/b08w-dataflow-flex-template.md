---
id: b08w
title: "Workshop: Create your first Dataflow Flex template and set up a CI/CD pipeline for it on Cloud Build"
url: /sessions/dataflow-flex-template
speakers:
 - Miren Esnaola
time_start: 2021-08-05T18:00:00.000Z
time_end: 2021-08-05T20:00:00.000Z
block: b
slot: 08
summary: In-depth workshop where we will explain how to use Flex templates for testing and CI/CD of Beam data pipelines. This workshop requires additional registration and has limited capacity. See details.
slides: 
video:
---

**Participation in this workshop requires additional registration and has limited capacity. If you are interested, please [register here](https://us02web.zoom.us/webinar/register/WN_bBFM33DNQTKsB9BDP9upJw)**


This will be a 2h workshop with the following format:

1. Introduction to Flex Templates, covering the following topics

- What are Flex templates?
- How do you create a Flex template?
- How do you run a Flex template?

2. Introduction to Apache Beam testing

- Transform testing
- End-to-end testing

3. Developing and testing your first Flex template in Python

Given a DAG with the steps to include in a simple pipeline we will develop a Flex template to run it including all the required transform, unit tests for them and end-to-end tests for the pipeline.

4. Setting up a CI/CD pipeline on Cloud Build

Once the Flex template is ready, tests included, we will create the build file for Cloud Build with all the required steps for our CI/CD pipeline and set up a trigger to a build every time the code is updated.