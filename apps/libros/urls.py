from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('libros/', views.ListarLibros.as_view(), name='libros'),
    path('libros/detalle/<int:pk>/', views.LibroDetailView.as_view(), name='detalle'),
]
