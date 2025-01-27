from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
import time

from device.handlers.mqtt.publisher import MQTTPublisher, PUBLISHERS
from device.models import Device, Noise


class Command(BaseCommand):
    help = 'Publishes messages for devices.'

    def handle(self, *args, **options):
        topic = "proxy"
        publisher = MQTTPublisher(topic)
        publisher.start()
        while True:
            # devices = Device.objects.filter(device_type__role__in=['publisher', 'both'])
            # print(len(devices))
            # for device in devices:
            #     prefix = f"{device.device_type.prefix}#{device.id}#"
            #     print(prefix)
            #     handler = device.device_type.publisher
            #     handler.execute(publisher, prefix)
            print("Trying to publish")
            time.sleep(1)
            noises = Noise.objects.filter(
                device__device_type__role__in=['publisher', 'both'],
                created_at__gte=datetime.now() - timedelta(seconds=2)
            )
            for noise in noises:
                print('Published noise')
                device = noise.device
                prefix = f"{device.device_type.prefix}#{device.id}#"
                handler = device.device_type.publisher
                handler.execute(publisher, prefix, noise.action.name)