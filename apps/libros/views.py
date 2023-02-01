
import datetime
from django.views.generic import ListView, DetailView
from .models import Libro, Categoria
# Create your views here.


class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/lista_libros.html'
    context_object_name = 'libros'

    def get_queryset(self):
      queryset = super(ListarLibros, self).get_queryset()
      kword = self.request.GET.get('kword', '')
      f1 = self.request.GET.get('fecha1', '')
      f2 = self.request.GET.get('fecha2', '')
      
      if f1 and f2:
        date1 = datetime.datetime.strptime(f1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(f2, '%Y-%m-%d')
        queryset = Libro.objects.buscar_libros_fecha2(kword, date1, date2)
      else:
        queryset = Libro.objects.buscar_libros_categoria(1)

      return queryset

    
    def get_context_data(self, **kwargs):
        context = super(ListarLibros, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/detalle_libro.html"

