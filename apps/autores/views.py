from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor

# Create your views here.

class ListAutores(ListView):
    model = Autor
    template_name = "autores/lista_autores.html"
    context_object_name = 'autores'

    def get_queryset(self):
        queryset = super(ListAutores, self).get_queryset()
        kword = self.request.GET.get('kword', '')
        queryset = Autor.objects.buscar_autores(kword)
        return queryset

    

