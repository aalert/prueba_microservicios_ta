import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

url = "influx"
org = "tecnoandina"
username = "admin"
password = "admin"

client = influxdb_client.InfluxDBClient(
    url=url,
    username=username,
    password=password,
    org=org
)


def write_to_influxdb(data):
    bucket = "system"
    measurement = "dispositivos"

    write_api = client.write_api(write_options=SYNCHRONOUS)

    point = influxdb_client.Point(measurement).\
        tag("version", data["version"]).\
        field("temperatura", data["temperatura"]).time(data["time"])

    write_api.write(bucket=bucket, record=point)
