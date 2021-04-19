# fronius-to-influx

Collect Fronius inverter data and save in Influxdb for Grafana. This tool collects the most basic Fronius inverter data for a most basic photovoltaic setup. If your installation is more sophisticated, then probably some extra work will be required.

## Fronius Endpoints

This tool collects data from one or many of the three endpoints below. Endpoints that can be used (adjust DeviceId accordingly):

    http://<fronius_ip>/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=3PInverterData&DeviceId=1
    http://<fronius_ip>/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=CommonInverterData&DeviceId=1
    http://<fronius_ip>/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=MinMaxInverterData&DeviceId=1

## Install Requirements

To install requirements:

```
    python3 -m venv .venv
    source ./.venv/bin/activate
    pip install -r requirements.txt
```

## Running Locally

Install [direnv](https://direnv.net/), copy `.envrc.example` to `.envrc` and modify it to suit, then run:

    python src/main.py

## Running In Docker

Modify `.envrc` as above then run:

    ./scripts/run.sh

Or:

    docker-compose up

## Mock Fronius Server

To install requirements and run:

    pip install -r requirements-dev.txt
    export FLASK_APP=json_server
    flask run

Modify `.envrc` to point to the mock server, then run:

    python src/main.py

## Grafana dashboards

Grafana dashboards from the parent repo are in the `grafana_dashboards` directory.

![Screenshot](img/screenshot.png?raw=true "Screenshot")
![Screenshot2](img/screenshot2.png?raw=true "Screenshot2")
![Screenshot3](img/screenshot3.png?raw=true "Screenshot3")
![Screenshot4](img/screenshot4.png?raw=true "Screenshot4")
