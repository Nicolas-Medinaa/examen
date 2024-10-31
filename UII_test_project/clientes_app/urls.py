from django.urls import path
from clientes_app import views
urlpatterns = [
    path("",views.listadoClientes,name="listadoClientes")
]