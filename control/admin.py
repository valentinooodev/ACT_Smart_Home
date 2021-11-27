from django.contrib import admin

from .models import RoomModel, DeviceModel

admin.site.register(RoomModel)


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'type', 'data', 'info', 'room')


