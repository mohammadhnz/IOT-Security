from django.core.management.base import BaseCommand
import time

from device.handlers.mqtt.publisher import MQTTPublisher, PUBLISHERS
from device.models import Device


class Command(BaseCommand):
    help = 'Publishes messages for devices.'

    def handle(self, *args, **options):
        topic = "proxy"
        publisher = MQTTPublisher(topic)
        publisher.start()
        while True:
            devices = Device.objects.filter(device_type__role__in=['publisher', 'both'])
            print(len(devices))
            for device in devices:
                prefix = f"{device.device_type.prefix}#{device.id}#"
                print(prefix)
                handler = device.device_type.publisher
                handler.execute(publisher, prefix)
            time.sleep(1)