#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Pull notebook image
: ${DOCKER_CONTAINER_IMAGE:="jupyter/singleuser:latest"}
export DOCKER_CONTAINER_IMAGE
docker pull "$DOCKER_CONTAINER_IMAGE"

# Build the JupyterHub image
docker-compose -f "$DIR/jupyterhub.yml" build
