# NVIDIA GTC 2023

## Developer Breakout

### Accelerating Enterprise Workflows With Triton Server and DALI

_[SE52140]_

## Overview

NVIDIA Data Loading Library (DALI) is a collection of highly optimized building blocks and an execution engine that accelerates the data pipeline for computer vision and audio deep learning applications.

Input and augmentation pipelines provided by Deep Learning frameworks fit typically into one of two categories:

- fast, but inflexible - written in C++, they are exposed as a single monolithic Python object with very specific set and ordering of operations it provides
- slow, but flexible - set of building blocks written in either C++ or Python, that can be used to compose arbitrary data pipelines that end up being slow. One of the biggest overheads for this type of data pipelines is Global Interpreter Lock (GIL) in Python. This forces developers to use multiprocessing, complicating the design of efficient input pipelines.

DALI stands out by providing both performance and flexibility of accelerating different data pipelines. It achieves that by exposing optimized building blocks which are executed using simple and efficient engine, and enabling offloading of operations to GPU (thus enabling scaling to multi-GPU systems).

It is a single library, that can be easily integrated into different deep learning training and inference applications.

DALI offers ease-of-use and flexibility across GPU enabled systems with direct framework plugins, multiple input data formats, and configurable graphs. DALI can help achieve overall speedup on deep learning workflows that are bottlenecked on I/O pipelines due to the limitations of CPU cycles. Typically, systems with high GPU to CPU ratio are constrained on the host CPU, thereby under-utilizing the available GPU compute capabilities. DALI significantly accelerates input processing on such dense GPU configurations to achieve the overall throughput.
