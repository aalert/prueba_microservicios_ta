import json
from datetime import datetime
from random import randint, uniform
from time import sleep

import paho.mqtt.publish as publish


def main():
    while True:
        random_data = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "value": uniform(0, 1000),
            "version": randint(0, 1)
        }

        print(f"sending: {random_data}")

        publish.single(
            "challenge/dispositivo/rx",
            json.dumps(random_data),
            hostname="mosquitto"
        )

        sleep(60)


if __name__ == "__main__":
    main()
