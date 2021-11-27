from rest_framework import serializers
from control.models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RoomModel


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DeviceModel

