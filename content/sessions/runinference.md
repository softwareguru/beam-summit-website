---
id: 
title: "RunInference: Machine Learning Inferences in Beam"
url: /sessions/runinference
speakers:
 - Andy Ye
time_start: 2022-01-01T17:00:00.000Z
time_end: 2022-01-01T18:00:00.000Z
block: 
slot: 
---

Users of machine learning frameworks must currently implement their own PTransforms for predictions or inferences. Only TensorFlow makes a RunInference beam transform available, but it's not highly accessible since it's hosted in the TFX-BSL repo.
 
We are creating implementations of RunInference for two popular machine learning frameworks, scikit-learn and PyTorch. These will take advantage of both internal optimizations like shared resource models, as well as framework-specific optimizations such as vectorization. It will have a clean simple unified interface, and use types intuitive to developers for inputs and outputs (numpy for scikit-learn, Tensors for PyTorch).  
 
The eventual goal is to support this for many more ML frameworks (e.g. XGBoost, mxnet, Statsmodels, JAX, TensorRT) and remote services (e.g. Vertex AI).