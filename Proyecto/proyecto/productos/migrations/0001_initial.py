# Generated by Django 4.2.2 on 2023-07-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Sin nombrar', max_length=300, verbose_name='Nombre del producto')),
                ('descripcion', models.CharField(default='Descripcion', max_length=300, verbose_name='Descripcion')),
                ('precio', models.FloatField(default=None, max_length=300, verbose_name='Precio')),
                ('fec_reg', models.DateField(verbose_name='Fecha de registro')),
                ('estatus', models.BooleanField(default=None, verbose_name='Estatus')),
            ],
        ),
    ]
