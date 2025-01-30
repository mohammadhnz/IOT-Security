from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Device, Action
from .models import Noise, SilencedEvent
from .serializers import SilencedEventSerializer
from .models import DeviceType


@api_view(['POST'])
def create_noise_view(request):
    device_id = request.data.get('device_id')
    action_name = request.data.get('action_name')

    if not device_id or not action_name:
        return Response({"error": "Missing device_id or action_name"}, status=status.HTTP_400_BAD_REQUEST)

    device = get_object_or_404(Device, pk=device_id)
    action = get_object_or_404(Action, name=action_name, device_type=device.device_type)

    noise = Noise.objects.create(device=device, action=action)

    return Response({"noise_id": noise.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_silenced_events_by_noise(request, noise_id):
    noise = get_object_or_404(Noise, pk=noise_id)
    silenced_events = SilencedEvent.objects.filter(noise=noise)
    serializer = SilencedEventSerializer(silenced_events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_devices_with_actions(request):
    device_types = DeviceType.objects.all()
    data = []
    for dt in device_types:
        data.append({
            'device_type_class': dt.device_class,
            'devices': [dev.id for dev in dt.devices.all()],
            'actions': [action.name for action in dt.actions.all()],
        })
    return Response(data)
