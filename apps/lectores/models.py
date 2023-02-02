from django.db import models
from apps.libros.models import Libro

# Create your models here.

class Lector(models.Model):
  """Model definition for Lector."""

  # TODO: Define fields here
  nombres = models.CharField(
    max_length=50
  )

  apellidos = models.CharField(
    max_length=50
  )

  nacionalidad = models.CharField(
    max_length=30
  )

  edad = models.PositiveIntegerField()

  class Meta:
    """Meta definition for Lector."""

    verbose_name = 'Lector'
    verbose_name_plural = 'Lectores'

  def __str__(self):
    """Unicode representation of Lector."""
    return (f'{self.nombres} {self.apellidos}')


class Prestamo(models.Model):
  """Model definition for Prestamo."""

  # TODO: Define fields here
  libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
  lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
  fecha_prestamo = models.DateField('Fecha de prestamo', auto_now=False, auto_now_add=False, blank=False)
  fecha_devolucion = models.DateField('Fecha de devolución', auto_now=False, auto_now_add=False, blank=True)
  devuelto = models.BooleanField()

  class Meta:
    """Meta definition for Prestamo."""

    verbose_name = 'Prestamo'
    verbose_name_plural = 'Prestamos'

  def __str__(self):
    """Unicode representation of Prestamo."""
    return (f'{self.libro.titulo}')


