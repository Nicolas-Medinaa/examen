from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_clientes=models.CharField(primary_key=True,max_length=6)
    nombres=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    historial=models.CharField(max_length=50)
    id_inventario=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombres
