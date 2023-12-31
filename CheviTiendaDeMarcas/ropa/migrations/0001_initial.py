# Generated by Django 4.2.3 on 2023-07-14 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_nombre_en_administrador', models.CharField(max_length=100)),
                ('categoria_nombre_en_pantalla', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tallas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('especificacion', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ropa.categorias')),
                ('tallas', models.ManyToManyField(to='ropa.tallas')),
            ],
        ),
        migrations.AddField(
            model_name='categorias',
            name='genero_al_que_pertenece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ropa.generos'),
        ),
    ]
