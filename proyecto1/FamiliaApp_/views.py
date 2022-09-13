from django.shortcuts import render
from django.http import HttpResponse
from FamiliaApp_.models import Familia
from django.template import loader


def familia(self):

    familia1 = Familia(nombre = "Edith", edad = 46, fecha_nac = "1975-1-16")

    familia1.save()

    familia2 = Familia(nombre = "Bruno", edad = 17, fecha_nac = "2005-8-28")

    familia2.save()

    familia3 = Familia(nombre = "Valeria", edad = 30, fecha_nac = "1992-7-1")

    familia3.save()


    diccionario = {
        "name1": familia1.nombre, "age1": familia1.edad, "birth1": familia1.fecha_nac,
        "name2": familia2.nombre, "age2": familia2.edad, "birth2": familia2.fecha_nac,
        "name3": familia3.nombre, "age3": familia3.edad, "birth3": familia3.fecha_nac
        }

    
    plantilla = loader.get_template("Familiares.html")

    document = plantilla.render(diccionario)

    return HttpResponse(document)