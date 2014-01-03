#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from django.db import models


class Empleado (models.Model):

    def nomcompleto(self):
        return self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno

    nombre = models.CharField ('Nombre del Empleado:',max_length = 50)
    apellido_paterno = models.CharField ('Apellido Paterno:',max_length=50)
    apellido_materno = models.CharField ('Apellido Materno:',max_length=50)
    cargo = models.CharField ('Cargo Actual:',max_length=1000)
    observaciones = models.CharField('Observaciones:',max_length=1000)
    fecha_ingreso = models.DateField ('Fecha de Ingreso:')
    fecha_fin = models.DateField ('Fecha de Vencimiento:')
    vencido = models.BooleanField(default=True)
