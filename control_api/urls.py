from django.urls import path
from .views import *

app_name = 'control_api'

urlpatterns = [
    path('rooms/', RoomListAPIView.as_view()),
    path('room/<int:pk>', RoomDetailAPIView.as_view()),
    path('input-devices/', InputDeviceListAPIView.as_view()),
    path('input-device/<int:pk>', InputDeviceDetailAPIView.as_view()),
    path('output-devices/', OutputDeviceListAPIView.as_view()),
    path('output-device/<int:pk>', OutputDeviceDetailAPIView.as_view()),
]
