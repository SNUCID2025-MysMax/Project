FROM ollama/ollama:0.1.37
SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get -y install python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install ollama
RUN pip install sentence-transformers
RUN pip install fastai
RUN pip install uvicorn
RUN pip install fastapi
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    libcurl4-openssl-dev

RUN pip install unsloth torch transformers datasets trl huggingface_hub

WORKDIR /app

