#!/usr/bin/env bash

podman-compose down
podman ps -aq | xargs -I {} podman rm {}
podman image ls -aq | xargs -I {} podman rmi {} --force
podman volume rm rcos_io_pg_data
podman-compose build
podman-compose up -d