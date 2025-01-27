from rest_framework import serializers

from .models import SilencedEvent

class SilencedEventSerializer(serializers.ModelSerializer):
    device_id = serializers.IntegerField(source='noise.device.id', read_only=True)
    device_type_class = serializers.CharField(source='noise.device.device_type.device_class', read_only=True)
    action_name = serializers.CharField(source='action.name', read_only=True)

    class Meta:
        model = SilencedEvent
        fields = [
            'id',
            'noise',
            'device_id',
            'device_type_class',
            'action_name',
            'created_at'
        ]