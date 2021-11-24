from django.contrib import admin

from .models import RoomModel, InputDeviceModel, OutputDeviceModel

admin.site.register(RoomModel)
admin.site.register(InputDeviceModel)
admin.site.register(OutputDeviceModel)
