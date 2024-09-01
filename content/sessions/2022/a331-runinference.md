---
slot: a331
title: "RunInference: Machine Learning Inferences in Beam"
url: /sessions/runinference
speakers:
 - Andy Ye
time_start: 2022-07-18 12:00:00 -0500 CDT
time_end:   2022-07-18 12:25:00 -0500 CDT
day: a
timeslot: 3
room: 202
timeorder: 1
track: trends
slides: 2022/RunInference.pdf
video: https://youtu.be/Ru36d_upOt8
---

Users of machine learning frameworks must currently implement their own PTransforms for predictions or inferences. Only TensorFlow makes a RunInference beam transform available, but it's not highly accessible since it's hosted in the TFX-BSL repo.
 
We are creating implementations of RunInference for two popular machine learning frameworks, scikit-learn and PyTorch. These will take advantage of both internal optimizations like shared resource models, as well as framework-specific optimizations such as vectorization. It will have a clean simple unified interface, and use types intuitive to developers for inputs and outputs (numpy for scikit-learn, Tensors for PyTorch).  
 
The eventual goal is to support this for many more ML frameworks (e.g. XGBoost, mxnet, Statsmodels, JAX, TensorRT) and remote services (e.g. Vertex AI).

Link to notebook: https://colab.research.google.com/drive/10iPQTCmaLJL4_OohS00R9Wmor6d57JkS