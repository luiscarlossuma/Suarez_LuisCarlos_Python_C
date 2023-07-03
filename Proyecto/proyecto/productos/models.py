from django.db import models
from django.utils import timezone

class Productos(models.Model):

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    nombre = models.CharField('Nombre del producto', max_length=300, blank=False, default='Sin nombrar')
    descripcion = models.CharField('Descripcion', max_length=300, blank=False, default='Descripcion')
    precio = models.FloatField('Precio', max_length=300,blank=False, default=0)
    fec_reg = models.DateField('Fecha de registro', auto_now_add=False, blank=False, default=timezone.now)
    estatus = models.BooleanField('Estatus', default=True)

    def _str_(self):
        return self.nombre
