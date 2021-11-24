from rest_framework import serializers
from control.models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RoomModel


class InputDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = InputDeviceModel


class OutputDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OutputDeviceModel
