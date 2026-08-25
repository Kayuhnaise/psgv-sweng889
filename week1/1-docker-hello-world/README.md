# Module 1: Hello World with Python and Docker

In this module, we run a simple Python program inside a Docker container.

## Files

```text
app.py
Dockerfile
```

## What this project does

The Python file prints:

```text
Hello world from Python inside Docker!
```

## Build the Docker image

Run this command from inside the `module-1-hello-world` folder:

```bash
docker build -t sweng889-module1 .
```

## Run the container

```bash
docker run --name module1-hello sweng889-module1
```

You should see:

```text
Hello world from Python inside Docker!
```

## If you want to run it again

The container name `module1-hello` can only be used once. Remove the old container first:

```bash
docker rm module1-hello
```

Then run it again:

```bash
docker run --name module1-hello sweng889-module1
```

## Alternative: run without naming the container

```bash
docker run sweng889-module1
```

Docker will automatically create a random container name.