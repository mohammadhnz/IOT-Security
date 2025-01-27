import os
import random

from paho.mqtt import client as mqtt_client
from paho.mqtt.enums import CallbackAPIVersion

from bindings.mqtt_m110_binding import M110Binding

os.environ.setdefault('MQTT_USERNAME', 'mqtt_user')
os.environ.setdefault('MQTT_PASSWORD', '123456')
os.environ.setdefault('MQTT_BROKER', 'localhost')
os.environ.setdefault('MQTT_PORT', '1883')

SUBSCRIBERS = {
    M110Binding.PREFIX: M110Binding()
}


class MQTTSubscriber:
    def __init__(self, topic, on_message=None):
        self.broker = os.environ.get('MQTT_BROKER')
        self.port = int(os.environ.get('MQTT_PORT'))
        self.topic = topic
        self.client_id = f'subscriber-{random.randint(0, 1000)}'
        self.client = self.connect_mqtt()
        self.on_message = on_message

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc, etc):
            if rc == 0:
                print("Connected to MQTT Broker!")
                # Subscribe to the topic upon successful connection
                self.subscribe()
            else:
                print(f"Failed to connect, return code {rc}")

        # Create MQTT client instance with callback API version 2
        self.client = mqtt_client.Client(
            client_id=self.client_id,
            # Remove callback_api_version if not necessary; it's optional
            callback_api_version=CallbackAPIVersion.VERSION2
        )

        # Read username and password from environment variables
        username = os.environ.get('MQTT_USERNAME')
        password = os.environ.get('MQTT_PASSWORD')
        if username is not None and password is not None:
            self.client.username_pw_set(username, password)
        else:
            print("MQTT_USERNAME or MQTT_PASSWORD environment variables not set")

        self.client.on_connect = on_connect

        self.client.connect(self.broker, self.port)
        return self.client

    def subscribe(self):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            massage = msg.payload.decode()
            for prefix, subscriber in SUBSCRIBERS.items():
                if massage.startswith(prefix):
                    subscriber.on_message(massage.split("#")[1])

        self.client.subscribe(self.topic)
        self.client.on_message = on_message

    def run(self):
        # Start the network loop to process network traffic and callbacks
        self.client.loop_forever()


def main():
    topic = "proxy-sub"

    subscriber = MQTTSubscriber(topic)
    subscriber.run()


if __name__ == '__main__':
    main()
