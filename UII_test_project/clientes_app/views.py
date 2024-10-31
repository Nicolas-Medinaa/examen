from django.shortcuts import render
from .models import Clientes
# Create your views here.
def listadoClientes(request):
    Losclientes=Clientes.objects.all()
    return render(request,"GestionarClientes.html",{"misclientes":Losclientes})