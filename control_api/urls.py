from django.urls import path
from .views import *

app_name = 'control_api'

urlpatterns = [
    path('rooms/', RoomListAPIView.as_view()),
    path('room/<int:pk>', RoomDetailAPIView.as_view()),
    path('devices/', DeviceListAPIView.as_view()),
    path('device/<int:pk>', DeviceDetailAPIView.as_view()),
]
