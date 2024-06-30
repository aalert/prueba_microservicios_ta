import socket

import influxdb_client
from connections.schemas import Device

url = "influx"
org = "tecnoandina"
username = "admin"
password = "influxadmin"
port = 8086

url = f"http://{socket.gethostbyname(url)}:{port}"

client = influxdb_client.InfluxDBClient(
    url=url,
    username=username,
    password=password,
    org=org
)


def read_devices_from_system(absolute_time=None, version=None):
    bucket = "system"
    measurement = "dispositivos"

    query_api = client.query_api()

    query = (
        f"from(bucket: \"{bucket}\") "
        "RANGE_PLACEHOLDER "
        f"|> filter(fn: (r) => r._measurement == \"{measurement}\")"
        f"|> filter(fn: (r) => r.version == \"{version}\")"
    )

    range = ""
    if isinstance(absolute_time, tuple) and absolute_time:
        clean_absolute_time = filter_abs_time_string(absolute_time, is_start=True)

        for each_time in clean_absolute_time:
            range += f"|> range(start: {each_time}) "

    query = query.replace("RANGE_PLACEHOLDER", range)

    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append(
                Device(
                    version=record.values.get("version"),
                    time=record.get_time(),
                    value=record.get_value()
                )
            )
            #results.append((record.get_field(), record.get_value()))

    return results


def filter_abs_time_string(absolute_time: tuple, is_start=False) -> str:
    minutes, hours, days = absolute_time
    result = []
    symbol = ""

    if is_start:
        symbol = "-"

    if minutes:
        result.append(f"{symbol}{minutes}")
    if hours:
        result.append(f"{symbol}{hours}")
    if days:
        result.append(f"{symbol}{days}")

    return result