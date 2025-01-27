# device/urls.py

from django.urls import path
from .views import create_noise_view, list_silenced_events_by_noise, list_devices_with_actions

urlpatterns = [
    path('create-noise/', create_noise_view, name='create_noise'),
    path(
        'noises/<int:noise_id>/silenced-events/',
        list_silenced_events_by_noise,
        name='list_silenced_events'
    ),
    path('list-devices-actions/', list_devices_with_actions, name='list_devices_actions'),
    path('create-noise/', create_noise_view, name='create_noise'),
]