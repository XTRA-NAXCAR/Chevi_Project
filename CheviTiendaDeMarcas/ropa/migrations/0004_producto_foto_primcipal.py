# Generated by Django 4.2.3 on 2023-07-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0003_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Foto_Primcipal',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
