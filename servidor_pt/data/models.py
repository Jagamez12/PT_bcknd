from django.db import models

# Create your models here.
from django.db import models
from enum import Enum

class TEL_ID(Enum):
    """Enum de Opciones de telefono.
        TEL = TELEFONO,
        CEL = CELULAR"""
    TEL = 'TEL'
    CEL = 'CEL'
    
    @classmethod
    def opciones(cls):
        
        return tuple((i.name, i.value) for i in cls)

class TipoIdentificacion(Enum):
    """Enum de opciones de identificacion. NIT = NIT, CC = Cedula de Ciudadania"""
    NIT = 'NIT'
    CC = 'CC'

    @classmethod
    def opciones(cls):
        
        return tuple((i.name, i.value) for i in cls)
    

class Departamento(models.Model):
    departamento = models.CharField(max_length=20, unique=True)

class Cargo(models.Model):
    cargo = models.CharField (max_length=20, unique=True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    tipoIdentificacion = models.CharField(max_length=3, choices=TipoIdentificacion.opciones())
    fechaIngreso = models.DateField()
    salarioMensual = models.DecimalField(max_digits=20, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Email(models.Model):
    
    email = models.EmailField(max_length=50, unique=True)
    usuario = models.OneToOneField(Empleado, on_delete=models.CASCADE)

class Telefono(models.Model):
    tipoIdentificacion = models.CharField(max_length=3, choices=TipoIdentificacion.opciones())
    telefono = models.IntegerField(unique=True)
    indicador = models.IntegerField()
    usuario = models.OneToOneField(Empleado, on_delete=models.CASCADE)

