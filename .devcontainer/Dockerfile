# Using template from https://github.com/abetlen/llama-cpp-python/blob/main/

# Use a simple image for non-GPU devices.
# ARG IMAGE=python:3-slim-bullseye
# FROM ${IMAGE}
# ARG IMAGE

ARG VARIANT=3.9
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

# Install dependencies
# ENV DEBIAN_FRONTEND=noninteractive
# RUN apt update && apt install -y python3 python3-pip cmake curl git

# ARG NODE_VERSION=14.16.0
# ARG NODE_PACKAGE=node-v$NODE_VERSION-linux-x64
# ARG NODE_HOME=/opt/$NODE_PACKAGE

# ENV NODE_PATH $NODE_HOME/lib/node_modules
# ENV PATH $NODE_HOME/bin:$PATH

# RUN curl https://nodejs.org/dist/v$NODE_VERSION/$NODE_PACKAGE.tar.gz | tar -xzC /opt/

#RUN pip install flask
# WORKDIR /edge-api
# COPY requirements.txt ./
# RUN pip install -r requirements.txt


# We need to set the host to 0.0.0.0 to allow outside access
#ENV HOST 0.0.0.0

# RUN export LLAMA_CUBLAS=0
# RUN CMAKE_ARGS="-DLLAMA_CUBLAS=off" FORCE_CMAKE=1 pip install llama-cpp-python[server] langchain

# RUN pip3 install langchain llama-cpp-python llama-cpp-python[server] openai Flask
# RUN sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# RUN curl -L https://github.com/kubernetes/kompose/releases/download/v1.30.0/kompose-linux-amd64 -o kompose