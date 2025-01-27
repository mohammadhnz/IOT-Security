import asyncio
from random import randint
from time import sleep


class WaterSensorBinding:
     def execute(self, publisher, prefix, action):
        publisher.publish(prefix + action)
        sleep(2)
