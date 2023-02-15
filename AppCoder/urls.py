from django.urls import path

from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('vendedores/', vendedores, name='vendedores'),
    path('distribuidores/', distribuidores, name='distribuidores'),
    path('entregas/', entregas, name='entregas'),
    path('curso-formulario/', curso_formulario, name='curso-formulario'),
    path('vendedor-formulario/', vendedor_formulario, name='vendedor-formulario'),
    path('busqueda-camada/', busqueda_camada, name='busqueda-camada'),
    path('buscar/', buscar, name='buscar'),
    
]
 