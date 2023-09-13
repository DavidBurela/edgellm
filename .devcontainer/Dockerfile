# Using template from https://github.com/abetlen/llama-cpp-python/blob/main/

# Use a simple image for non-GPU devices.
# ARG IMAGE=python:3-slim-bullseye
# FROM ${IMAGE}
# ARG IMAGE

ARG VARIANT=3.9
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}


# Install dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y python3 python3-pip cmake curl git

# We need to set the host to 0.0.0.0 to allow outside access
ENV HOST 0.0.0.0

RUN export LLAMA_CUBLAS=0
RUN CMAKE_ARGS="-DLLAMA_CUBLAS=off" FORCE_CMAKE=1 pip install llama-cpp-python[server] langchain

RUN pip3 install langchain llama-cpp-python llama-cpp-python[server] openai Flask