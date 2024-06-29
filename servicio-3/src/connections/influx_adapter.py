import influxdb_client

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


def read_devices_from_system(absolute_time=None, version=None):
    bucket = "system"
    measurement = "dispositivos"

    query_api = client.query_api()

    query = (
        f"from(bucket: \"{bucket}\")"
        f"|> filter(fn: (r) => r._measurement == \"{measurement}\")"
        f"|> filter(fn: (r) => r.version == \"{version}\")"
    )

    if isinstance(absolute_time, tuple) and absolute_time:
        query += f"|> range(start: {filter_abs_time_string(absolute_time, is_start=True)})"

    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_field(), record.get_value()))

    print(results)
    return results


def filter_abs_time_string(absolute_time: tuple, is_start=False) -> str:
    minutes, hours, days = absolute_time
    result = ""
    symbol = ""

    if is_start:
        symbol = "-"

    if minutes:
        result += f"{symbol}{minutes}m"
    if hours:
        result += f"{symbol}{hours}h"
    if days:
        result += f"{symbol}{days}d"

    return result