from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=30)

class Gasera(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    logo = models.ImageField(blank=True,null=True)

class Unidad(models.Model):
    idGasera = models.ForeignKey(Gasera, on_delete=models.CASCADE)
    identificador = models.IntegerField()
    placas = models.CharField(max_length=10)
    modelo =  models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    anio = models.IntegerField()

class PedidosXEmpleado(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pedido(models.Model):
    idGasera = models.ForeignKey(Gasera, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idUnidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    idPedidosXEmpleado = models.ForeignKey(PedidosXEmpleado, on_delete=models.CASCADE)


class DetallesPedido(models.Model):
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)

"""
class Administrador(models.Model):
    idGasera = models.ForeignKey(Gasera, on_delete=models.CASCADE)

class Empleado(models.Model):
    idGasera = models.ForeignKey(Gasera, on_delete=models.CASCADE)
    """
