import os
import random
import time

from paho.mqtt import client as mqtt_client
from paho.mqtt.enums import CallbackAPIVersion

from bindings.mqtt_water_binding import WaterSensorBinding

os.environ.setdefault('MQTT_USERNAME', 'mqtt_user')
os.environ.setdefault('MQTT_PASSWORD', '123456')
os.environ.setdefault('MQTT_BROKER', 'localhost')
os.environ.setdefault('MQTT_PORT', '1883')

PUBLISHERS = [
    WaterSensorBinding()
]

class MQTTPublisher:
    def __init__(self, topic):
        self.broker = os.environ.get('MQTT_BROKER')
        self.port = int(os.environ.get('MQTT_PORT'))
        self.topic = topic
        self.client_id = f'publisher-{random.randint(0, 1000)}'
        self.client = self.connect_mqtt()

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc, etc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print(f"Failed to connect, return code {rc}")
            print(userdata)
            print(flags)
            print(rc)
            print(etc)

        client = mqtt_client.Client(client_id=self.client_id, callback_api_version=CallbackAPIVersion.VERSION2)
        client.on_connect = on_connect

        # Read username and password from environment variables
        username = os.environ.get('MQTT_USERNAME')
        password = os.environ.get('MQTT_PASSWORD')
        if username is not None and password is not None:
            client.username_pw_set(username, password)
        else:
            print("MQTT_USERNAME or MQTT_PASSWORD environment variables not set")

        client.connect(self.broker, self.port)
        return client

    def publish(self, msg):
        result = self.client.publish(self.topic, msg , retain=True)
        status = result[0]
        if status == mqtt_client.MQTT_ERR_SUCCESS:
            print(f"Sent `{msg}` to topic `{self.topic}`")
        else:
            print(f"Failed to send message to topic `{self.topic}`")

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()


def main():
    topic = "proxy"

    publisher = MQTTPublisher(topic)
    publisher.start()
    while True:
        for pb in PUBLISHERS:
            pb.execute(publisher)


if __name__ == '__main__':
    main()