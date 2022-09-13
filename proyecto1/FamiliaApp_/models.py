from django.db import models
from datetime import date
import datetime

class Familia(models.Model):

    nombre = models.CharField(max_length=40)

    edad = models.IntegerField()

    fecha_nac = models.DateField()