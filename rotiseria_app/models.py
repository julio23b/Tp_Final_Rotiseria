from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.

class Pedido(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre', null=False)
    plato = models.CharField(max_length=20, verbose_name='Plato')
    cantidad = models.IntegerField(verbose_name='Cantidad', null=False, default=0)
    fecha = models.DateField(verbose_name='Fecha',default=timezone.now)

    class Meta:
        db_table = "pedido_table"

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Plato: {self.plato}, La cantidad es: {self.cantidad}" 
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self._meta.get_fields()]
    
    def clean(self):
        super().clean()
        if self.cantidad < 0:
            raise ValidationError({'cantidad': 'La cantidad no puede ser un número negativo.'})
    

