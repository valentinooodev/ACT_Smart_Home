from django.shortcuts import render
from django.http import HttpResponse
from .models import RoomModel, DeviceModel


def index(request):
    rooms = RoomModel.objects.all()
    lamps = DeviceModel.objects.filter(type='lamp')
    fans = DeviceModel.objects.filter(type='fan')
    humidity = DeviceModel.objects.filter(type='humidity')
    temperature = DeviceModel.objects.filter(type='temperature')
    return render(request, 'control/index.html', {
        'rooms': rooms,
        'lamps': lamps,
        'fans': fans,
        'humidity': humidity,
        'temperature': temperature,
    })
