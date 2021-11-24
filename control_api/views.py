from django.shortcuts import render
from rest_framework import generics
from control.models import *
from .serializers import *


class RoomListAPIView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = RoomModel.objects.all()


class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = RoomModel.objects.all()


class InputDeviceListAPIView(generics.ListCreateAPIView):
    serializer_class = InputDeviceSerializer
    queryset = InputDeviceModel.objects.all()


class InputDeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InputDeviceSerializer
    queryset = InputDeviceModel.objects.all()


class OutputDeviceListAPIView(generics.ListCreateAPIView):
    serializer_class = OutputDeviceSerializer
    queryset = OutputDeviceModel.objects.all()


class OutputDeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OutputDeviceSerializer
    queryset = OutputDeviceModel.objects.all()
