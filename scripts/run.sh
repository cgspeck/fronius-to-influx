#! /bin/bash -e
docker run \
    --rm \
    -t \
    -e INVERTER_ENDPOINT \
    -e INFLUXDB_BUCKET \
    -e INFLUXDB_V2_TOKEN \
    -e INFLUXDB_V2_URL \
    -e INFLUXDB_V2_ORG \
    -e INFLUXDB_V2_SSL_CA_CERT \
    cgspeck/fronius-to-influx:latest

