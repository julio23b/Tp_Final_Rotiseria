# Generated by Django 4.2.7 on 2023-12-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotiseria_app', '0002_alter_formulario_rotiseria_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre')),
                ('Plato', models.CharField(max_length=20, verbose_name='Plato')),
                ('Cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('fecha', models.DateField(max_length=20, verbose_name='Fecha')),
            ],
            options={
                'db_table': 'pedido_table',
            },
        ),
        migrations.DeleteModel(
            name='Formulario_rotiseria',
        ),
    ]
