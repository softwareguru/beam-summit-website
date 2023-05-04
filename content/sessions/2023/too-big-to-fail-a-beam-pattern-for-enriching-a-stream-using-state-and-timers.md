---
title: "Too big to fail - a Beam Pattern for enriching a Stream using State and Timers"
slug: too-big-to-fail-a-beam-pattern-for-enriching-a-stream-using-state-and-timers
speakers:
 - Tobias Kaymak
 - Israel Herraiz
topics:
 - State & timers
room: Palisades
time_start: 2023-06-14 11:30:00
time_end: 2023-06-14 11:55:00
day: b
timeslot: d
timeorder: 2
language: 
live_url: 
slides: 
video: 
track: concurrent
tags:
---

Imagine you have an two unlimited stream of events, one contains IDs and their hashed counterparts for lookups, and one the full information about every object with its hashed id. Your job is to output the full information for each object with it’s clear text id. You could query a single source of truth to enrich, but you don’t want to hammer an external API for this as its typically slower than letting Beam run the show.
 
 This talk introduces a pattern as a possible solution to this problem.