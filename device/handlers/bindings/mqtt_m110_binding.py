import asyncio

from device.handlers.tapo_client.m110 import TapoDeviceManager


class M110Binding:
    PREFIX = 'M110'

    def __init__(self):
        self.device = TapoDeviceManager()

        def on_message(device, massage: str):
            if not self.device.connected:
                asyncio.run(self.device.connect())
            print(massage)
            if massage.lower() == 'on':
                asyncio.run(self.device.turn_on())
            elif massage.lower() == 'off':
                print(1)
                asyncio.run(self.device.turn_off())

        self.on_message = on_message
