# Generated by Django 5.1 on 2024-10-31 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_clientes', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('historial', models.CharField(max_length=50)),
                ('id_inventario', models.CharField(max_length=50)),
            ],
        ),
    ]
