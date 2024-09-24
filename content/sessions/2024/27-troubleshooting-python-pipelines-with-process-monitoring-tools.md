---
title: "Troubleshooting Python pipelines with process monitoring tools."
slug: troubleshooting-python-pipelines-with-process-monitoring-tools
speakers:
 - Valentyn Tymofieiev
track: Best practices
room: Hamina (MP4)
time_start: 2024-09-04 15:00:00
time_end: 2024-09-04 15:25:00
day: 20241
gridarea: "11/4/12/5"
timeslot: 27
images:
 - /images/sessions/2024/troubleshooting-python.png
slides: 2024/TroubleshootingPythonpipelineswithprocessmonitoringtools.pdf
video: 
---

In an ideal scenario, a data processing pipeline performs without issues. When a runtime processing error occurs, normally Beam surfaces the error to the runner. However in some cases, the process running the user code might run out of memory, get stuck or crash. This can prevent it from reporting the error, leaving the user unaware of the failure's root cause. In this talk, I'll discuss troubleshooting techniques for these situations. The techniques I cover can also be applied for debugging other Python applications.