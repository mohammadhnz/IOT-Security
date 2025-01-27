from django.contrib import admin

# Register your models here.
# device/admin.py

from django.contrib import admin
from .models import DeviceType, Action, Device, Noise, SilencedEvent

@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_class')

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device_type')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_type')

@admin.register(Noise)
class NoiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'created_at')

@admin.register(SilencedEvent)
class SilencedEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'noise', 'created_at')
