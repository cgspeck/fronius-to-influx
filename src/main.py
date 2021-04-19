from fronius_to_influx import FroniusToInflux
from influxdb_client import InfluxDBClient
from astral import LocationInfo
from os import environ

import pytz

COLLECT_COMMON_INVERTER_DATA = (
    environ.get("COLLECT_COMMON_INVERTER_DATA", "true") == "true"
)

COLLECT_3P_INVERTER_DATA = environ.get("COLLECT_3P_INVERTER_DATA", "false") == "true"
COLLECT_MINMAX_INVERTER_DATA = (
    environ.get("COLLECT_MINMAX_INVERTER_DATA", "false") == "true"
)

INVERTER_ENDPOINT = environ["INVERTER_ENDPOINT"]

INFLUXDB_BUCKET = environ.get("INFLUXDB_BUCKET", "fronius")

IGNORE_SUN_DOWN = environ.get("IGNORE_SUN_DOWN", "false") == "true"

LOCATION_CITY = environ["LOCATION_CITY"]
LOCATION_REGION = environ["LOCATION_REGION"]
LOCATION_TIMEZONE = environ["LOCATION_TIMEZONE"]
LOCATION_LAT = float(environ["LOCATION_LAT"])
LOCATION_LNG = float(environ["LOCATION_LNG"])

client = InfluxDBClient.from_env_properties()

location_info = LocationInfo(
    LOCATION_CITY, LOCATION_REGION, LOCATION_TIMEZONE, LOCATION_LAT, LOCATION_LNG
)
tz = pytz.timezone(LOCATION_TIMEZONE)
print(f"Location: {location_info}")
print(f"Timezone: {tz}")
endpoints = []

if COLLECT_MINMAX_INVERTER_DATA:
    print("Collecting MinMax Inverter Data")
    endpoints.append(
        f"http://{INVERTER_ENDPOINT}/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=MinMaxInverterData&DeviceId=1",
    )

if COLLECT_3P_INVERTER_DATA:
    print("Collecting 3P Inverter data")
    endpoints.append(
        f"http://{INVERTER_ENDPOINT}/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=3PInverterData&DeviceId=1"
    )

if COLLECT_COMMON_INVERTER_DATA:
    print("Collecting Common Inverter data")
    endpoints.append(
        f"http://{INVERTER_ENDPOINT}/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=CommonInverterData&DeviceId=1"
    )

z = FroniusToInflux(
    client,
    location_info,
    endpoints,
    tz,
    INFLUXDB_BUCKET,
    ignore_sundown=IGNORE_SUN_DOWN,
)
print("starting...")
z.run()
