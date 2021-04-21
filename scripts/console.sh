#! /bin/bash -e
docker run \
    --rm \
    -it \
    cgspeck/fronius-to-influx:latest \
    /bin/bash
