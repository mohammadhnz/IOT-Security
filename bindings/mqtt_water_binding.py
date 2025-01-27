import asyncio
from random import randint
from time import sleep


class WaterSensorBinding:
    PREFIX = 'wx'

    def execute(self, publisher):
        if randint(1, 4) % 3 < 2:
            publisher.publish(self.PREFIX + "#" + 'wet')
            print('wx#wet')
        else:
            publisher.publish(self.PREFIX + "#" + 'dry')
            print('wx#dry')
        sleep(2)
