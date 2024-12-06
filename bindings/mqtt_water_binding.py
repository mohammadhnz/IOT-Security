import asyncio
from random import randint
from time import sleep

from mqtt.publisher import MQTTPublisher


class WaterSensorBinding:
    def __init__(self, topic):
        self.publisher = MQTTPublisher(topic)
        self.publisher.start()

    def run(self):
        while True:
            if randint(1, 10) % 3 == 0:
                self.publisher.publish('wet')
                print('wet')
            else:
                self.publisher.publish('dry')
                print('dry')
            sleep(10)


WaterSensorBinding('water').run()
