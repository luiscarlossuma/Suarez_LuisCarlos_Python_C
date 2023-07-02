from django.db import models

class Productos(models.Model):

    nombre = models.CharField('Nombre del producto', max_length=300, default='Sin nombrar')
    descripcion = models.CharField('Descripcion', max_length=300, default='Descripcion')
    precio = models.FloatField('Precio', max_length=300, default=None)
    fec_reg = models.DateField('Fecha de registro', auto_now_add=False)
    estatus = models.BooleanField('Estatus', default=None)

    def _str_(self):
        return self.nombre
