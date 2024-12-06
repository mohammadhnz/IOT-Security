import asyncio

from mqtt.subscriber import MQTTSubscriber
from tapo_client.m110 import TapoDeviceManager


class M110Binding:
    def __init__(self, topic):
        self.device = TapoDeviceManager()

        def on_message(massage: str):
            if not self.device.connected:
                asyncio.run(self.device.connect())
            print(massage)
            if massage.lower() == 'on':
                asyncio.run(self.device.turn_on())
            elif massage.lower() == 'off':
                print(1)
                asyncio.run(self.device.turn_off())

        self.subscriber = MQTTSubscriber(topic, on_message=on_message)

    def run(self):
        self.subscriber.run()


binding = M110Binding('Plug')
binding.device.turn_off()
binding.run()
