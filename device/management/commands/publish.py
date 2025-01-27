from django.core.management.base import BaseCommand
import time

from device.handlers.mqtt.publisher import MQTTPublisher, PUBLISHERS


class Command(BaseCommand):
    help = 'Publishes messages for devices.'

    def handle(self, *args, **options):
        topic = "proxy"
        publisher = MQTTPublisher(topic)
        publisher.start()
        while True:
            for pb in PUBLISHERS:
                pb.execute(publisher)
            time.sleep(1)