from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
]
