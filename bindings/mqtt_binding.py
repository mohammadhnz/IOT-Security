from mqtt.subscriber import MQTTSubscriber
from tapo_client.m110 import TapoDeviceManager


class M110Binding:
    def __init__(self, topic):
        self.device = TapoDeviceManager()

        async def on_message(client, userdata, msg):
            if msg=='On':
                await self.device.turn_on()
            elif msg=='Off':
                await self.device.turn_off()

        self.subscriber = MQTTSubscriber(topic, on_message=on_message)

    def run(self):
        self.subscriber.run()


M110Binding('Plug').run()