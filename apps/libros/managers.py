from django.db import models
from django.db.models import Q, Count

class LibroManager(models.Manager):
  """ Managers para el módelo autor """

  def listar_libros(self):
    return self.all()

# KWORD Y RANGO DE FECHAS
  def buscar_libros_fecha(self, kword):
    libros = self.filter(
      Q(titulo__icontains = kword) & Q(fecha_lanzamiento__range = ('2000-01-01', '2022-12-01'))
    )
    return libros

  def buscar_libros_fecha2(self, kword, fecha1, fecha2):
    libros = self.filter(
      Q(titulo__icontains = kword) & Q(fecha_lanzamiento__range = (fecha1, fecha2))
    )
    return libros

# BUSCAR POR FK
  def buscar_libros_categoria(self, id_categoria):
    libros = self.filter(
      categoria__id = id_categoria
    )
    return libros
  
# AGREGAR M2N
  def agregar_autor_libro(self, libro_id, autor_id):
    libro = self.get(id=libro_id)
    libro.autores.add(autor_id)
    return libro

  def libro_num_prestamos(self):
    resultado = self.aggregate(
      num_prestamos = Count('libro_prestamo')
    )
    return resultado

class CategoriaManager(models.Manager):

  def categoria_por_autor(self, id_autor):
    
    return self.filter(
      categoria_libro__autores__id = id_autor
    ).distinct()

  def libros_por_categoria(self):
    resultado = self.annotate(
      num_libros = Count('categoria_libro')
    )
    return resultado