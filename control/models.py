from django.db import models
from django.contrib.auth.models import User


class RoomModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'room'
        verbose_name_plural = 'Rooms'


class InputDeviceModel(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    data = models.CharField(max_length=255)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='input_device_model')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'input_device'
        verbose_name_plural = 'Input Devices'


class OutputDeviceModel(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='output_device_model')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'output_device'
        verbose_name_plural = 'Output Devices'

