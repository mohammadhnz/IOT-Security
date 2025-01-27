from django.db import models

from django.db import models

from device.handlers.bindings.mqtt_m110_binding import M110Binding
from device.handlers.bindings.mqtt_water_binding import WaterSensorBinding

IMPLEMENTED_DEVICE_TYPES = {
    'M110Binding': M110Binding(),
    'WaterSensorBinding': WaterSensorBinding()
}


class DeviceType(models.Model):
    device_class = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    ROLE_CHOICES = [
        ('publisher', 'Publisher'),
        ('subscriber', 'Subscriber'),
        ('both', 'Both'),
    ]
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='subscriber'
    )

    @property
    def subscriber(self):
        assert self.role in ['subscriber', 'both']
        return IMPLEMENTED_DEVICE_TYPES.get(self.device_class)

    @property
    def publisher(self):
        assert self.role in ['publisher', 'both']
        return IMPLEMENTED_DEVICE_TYPES.get(self.device_class)


class Action(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='actions')


class Device(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='devices')


class Noise(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='noises')
    created_at = models.DateTimeField(auto_now_add=True)


class SilencedEvent(models.Model):
    noise = models.ForeignKey(Noise, on_delete=models.CASCADE, related_name='silenced_events')
    created_at = models.DateTimeField(auto_now_add=True)
