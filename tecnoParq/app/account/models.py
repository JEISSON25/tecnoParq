from django.db import models
from model_utils.models import TimeStampedModel



class Account(TimeStampedModel):

    identify = models.BigIntegerField('Cedula')
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    username = models.CharField('Nombre de usuario', max_length=100)
    password = models.CharField('Contraseña', max_length=100)
    pricehour = models.IntegerField('Número de horas', max_length=100)

    def __str__(self):
        return f"{self.identify} {self.last_name}, {self.name}"


class Input_Output(TimeStampedModel):
    
    class Meta:
        verbose_name = "Ingresos"
        verbose_name_plural = "Egresos"

    account = models.ForeignKey(
        Account,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    date_in = models.DateField('Fecha de entrada',blank=True, null=True)
    time_in = models.TimeField('Hora de entrada',blank=True, null=True)
    date_out = models.DateField('Fecha de salida', blank=True, null=True)
    time_out = models.TimeField('Hora de salida', blank=True, null=True)

