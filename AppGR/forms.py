from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppGR.models import Avatar 

class SombrasForm(forms.Form):
    codigo = forms.IntegerField()
    color = forms.CharField(max_length=100)
    tipo = forms.CharField(max_length=100)

class BaseForm(forms.Form):
    codigo = forms.IntegerField()
    tono = forms.CharField(max_length=100)
    cobertura = forms.CharField(max_length=100)

class BrochasForm(forms.Form):
    numero = forms.IntegerField()
    clase = forms.CharField(max_length=100)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    