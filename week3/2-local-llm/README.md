# Module 2: Running a Local LLM with Docker
In this module, we run a local Large Language Model using Docker and Ollama. A simple Python program sends a prompt to the local model and prints the response.
## Goal
By the end of this module, you will be able to:
- run an LLM locally using Docker
- start multiple containers using Docker Compose
- call a local LLM from a Python program
## Project Files
```text
module-2-local-llm/
|-- app.py
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- README.md

Requirements

Before starting, make sure you have:

* Docker Desktop installed
* Docker Desktop open and running
* the course repository cloned to your computer

How This Project Works

This module uses two containers:

ollama container      -> runs the local LLM service
python-app container  -> runs the Python script that calls the LLM

The Python app sends a request to Ollama using:

http://ollama:11434

Inside Docker Compose, ollama is the service name of the Ollama container.

Run the Project

From inside the module-2-local-llm folder, run:

docker compose up --build

The first time you run this command, Docker may need to:

1. download the Ollama Docker image
2. build the Python app image
3. download the selected LLM model

This may take a few minutes depending on your internet connection and computer.

Expected Output

You should see output similar to this:

Waiting for Ollama to start...
Ollama is running.
Pulling model: llama3.2:1b
Model is ready.
Prompt:
Explain Docker in one short paragraph for a beginner.
LLM response:
Docker is a tool that lets developers package applications...

The exact LLM response may be different. That is normal.

Stop the Containers

To stop the running containers, press:

CTRL + C

Then run:

docker compose down

Run Again

After the model has been downloaded once, it should not need to download again every time.

To run the project again:

docker compose up --build

Important Notes

This project uses the model:

llama3.2:1b

This is a smaller model and is better for student laptops.

The model is stored in a Docker volume named:

ollama_data

This allows Docker to keep the downloaded model even after the containers are stopped.

Troubleshooting

Docker command not found

Make sure Docker Desktop is installed and your terminal has been restarted.

Docker is not running

Open Docker Desktop and wait until it says Docker is running.

Model not found

If you see an error like:

model not found

run:

docker compose down
docker compose up --build

The Python script should pull the model before using it.

Port already in use

If port 11434 is already being used, stop any other Ollama instance running on your computer, then try again:

docker compose down
docker compose up --build

Summary

In this module, Docker Compose starts an Ollama container and a Python container. The Python container sends a prompt to the local LLM and prints the response.

The workflow is:

Start Docker Compose
        |
        v
Run Ollama container
        |
        v
Run Python container
        |
        v
Python sends prompt to local LLM
        |
        v
LLM returns response
:::