from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

class Sombras(models.Model):
    codigo=models.IntegerField()
    color=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo}, {self.color}, {self.tipo}'

class Base(models.Model):
    codigo=models.IntegerField()
    tono=models.CharField(max_length=100)
    cobertura=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo}, {self.tono}, {self.cobertura}'

class Brochas(models.Model):
    numero=models.IntegerField()
    clase=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.numero}, {self.clase}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    imagen = models.ImageField(upload_to='avatares', null = True)

    def __str__(self):
        return f"Imagen de: {self.user}"

class Blog(models.Model):
    titulo = models.CharField('Título', max_length=200, blank = False, null = False)
    subtitulo = models.CharField('Subtítulo', max_length=200, blank = False, null = False)
    fecha = models.DateField('Fecha', blank = False, null = False)
    autor = models.CharField('Autor', max_length=200, blank = False, null = False)
    contenido = RichTextField('Contenido', blank = False, null = False)
    imag = RichTextUploadingField('Imagen', null = True)
    slug = models.SlugField(default='', blank = True)
    
    def save(self):
        self.slug = slugify(self.titulo)
        super(Blog, self).save()

    def __str__(self):
        return '%s' % self.titulo

