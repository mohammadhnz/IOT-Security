import asyncio
from random import randint
from time import sleep


class WaterSensorBinding:
    def execute(self, publisher, prefix):
        if randint(1, 4) % 3 < 2:
            publisher.publish(prefix + 'wet')
            print(prefix + 'wet')
        else:
            publisher.publish(prefix + 'dry')
            print(prefix + 'dry')
        sleep(2)
