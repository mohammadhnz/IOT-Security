from django.core.management.base import BaseCommand

from device.handlers.mqtt.subscriber import MQTTSubscriber


class Command(BaseCommand):
    help = 'Subscribe topics to handle messages'

    def handle(self, *args, **options):
        topic = "proxy-sub"

        subscriber = MQTTSubscriber(topic)
        subscriber.run()
