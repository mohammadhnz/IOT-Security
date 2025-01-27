from django.db import models

from django.db import models


class DeviceType(models.Model):
    device_class = models.CharField(max_length=100)


class Action(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='actions')


class Device(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='devices')
    prefix = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100)


class Noise(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='noises')
    created_at = models.DateTimeField(auto_now_add=True)


class SilencedEvent(models.Model):
    noise = models.ForeignKey(Noise, on_delete=models.CASCADE, related_name='silenced_events')
    created_at = models.DateTimeField(auto_now_add=True)
