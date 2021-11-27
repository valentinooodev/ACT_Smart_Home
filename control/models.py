from django.db import models
from django.contrib.auth.models import User


class RoomModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'room'
        verbose_name_plural = 'Rooms'


class DeviceModel(models.Model):
    choices = (
        ('lamp', 'Lamp'),
        ('fan', 'Fan'),
        ('humidity', 'Humidity'),
        ('temperature', 'Temperature'),
    )
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False, null=True)
    type = models.CharField(max_length=15, choices=choices)
    data = models.CharField(max_length=255, null=True)
    info = models.TextField()
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='device_model')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'devices '
        verbose_name_plural = 'Devices'

