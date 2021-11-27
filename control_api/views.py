from django.shortcuts import render
from rest_framework import generics
from control.models import *
from .serializers import *
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    MQTT_TOPIC = [("sensor/temperature", 0),
                  ("sensor/humidity", 0),
                  ("homeassistant/switch1", 0)]
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    client.publish('test', 'hello')


client = mqtt.Client()


class RoomListAPIView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = RoomModel.objects.all()


class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = RoomModel.objects.all()


class DeviceListAPIView(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    queryset = DeviceModel.objects.all()


class DeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    queryset = DeviceModel.objects.all()
