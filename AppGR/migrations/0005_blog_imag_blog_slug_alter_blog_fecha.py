# Generated by Django 4.1 on 2022-10-27 01:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGR', '0004_alter_avatar_imagen_alter_avatar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imag',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
    ]
