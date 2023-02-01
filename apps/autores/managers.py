from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
  """ Managers para el módelo autor """

  def listar_autores(self):
    return self.all()

# OR
  def buscar_autores(self, kword):
    autores = self.filter(
      Q(nombres__icontains = kword) | Q(apellidos__icontains = kword)
    )
    return autores

# OR con EXCLUDE
  def buscar_autores_excepto_35_65(self, kword):
    autores = self.filter(
      Q(nombres__icontains = kword) | Q(apellidos__icontains = kword)
    ).exclude(
      Q(edad = 35) | Q(edad = 65)
    )
    return autores

# <= Y AND - lt < - gt >
  def buscar_autores_mayores_a_39(self, kword):
    autores = self.filter(
      Q(edad__gt = 39) & Q(edad__lt = 100)
    ).order_by('apellidos')
    return autores
