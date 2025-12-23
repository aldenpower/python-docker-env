This project is a learning-oriented Docker project designed to explore how [ENTRYPOINT](https://docs.docker.com/reference/dockerfile/#entrypoint), [CMD](https://docs.docker.com/reference/dockerfile/#cmd), and docker-compose commands interact when running Python scripts and Python packages.

## Motivation

Docker is a fantastic tool and can be used for a number of purposes. At one point i still had difficulty understanding and clearly explaining how a container actually decides what to run. Concepts like ENTRYPOINT, CMD, command overrides, and execution context are often not clear. The goal is not application complexity, but mastery of container basic execution flow.

## [Dockerfile explained](Dockerfile)

- Minimal base image (python:3.12-slim)
- PYTHONPATH=/app allows imports without installing the code as a package
- User defined python install dependencies using requirements.txt file
- Dependencies can be listed by the user using [requirements.txt](requirements.txt) file
- ENTRYPOINT ["python"] makes the container behave like the Python CLI

## [docker-compose.yml explained](docker-compose.yaml)

- command: "logger.py" becomes an argument to ENTRYPOINT
- Final executed command inside the container:

```bash
python logger.py
```
- tty and stdin_open allow interactive usage (docker exec -it)

## Running the project

> I'm assuming you've already installed [Docker](https://docs.docker.com/engine/install/)!

Run the default script:

```bash
docker compose up
```
Try the default python package editing the [compose file](docker-compose.yaml)

```yml
command: "-m package"
```
then:

```bash
docker compose up
```
