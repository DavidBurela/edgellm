# Using template from https://github.com/abetlen/llama-cpp-python/blob/main/Dockerfile.cuda

# Specify your CUDA version
ARG CUDA_IMAGE="nvidia/cuda:12.0.1-devel-ubuntu22.04"
FROM ${CUDA_IMAGE}

# Install dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y python3 python3-pip cmake curl git

# We need to set the host to 0.0.0.0 to allow outside access
ENV HOST 0.0.0.0

RUN export LLAMA_CUBLAS=1
RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python[server] langchain

