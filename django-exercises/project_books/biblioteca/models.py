from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validar_año_publicacion(valor):
    if valor < 1500 or valor > 2024:
        raise ValidationError(
            _('El año de publicación debe estar entre 1500 y el año actual.'),
            params={'value': valor},
        )

class Libro(models.Model):
    titulo = models.CharField(max_length=100, help_text='Ingrese el título del libro')
    autor = models.CharField(max_length=50, help_text='Ingrese el nombre del autor')
    resumen = models.TextField()
    año_publicacion = models.IntegerField(validators=[validar_año_publicacion])
    
    def __str__(self):
        return self.titulo