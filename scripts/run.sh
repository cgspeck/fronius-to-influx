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
    -e COLLECT_COMMON_INVERTER_DATA \
    -e COLLECT_3P_INVERTER_DATA \
    -e COLLECT_MINMAX_INVERTER_DATA \
    -e IGNORE_SUN_DOWN \
    -e LOCATION_CITY \
    -e LOCATION_REGION \
    -e LOCATION_TIMEZONE \
    -e LOCATION_LAT \
    -e LOCATION_LNG \
    cgspeck/fronius-to-influx:latest

