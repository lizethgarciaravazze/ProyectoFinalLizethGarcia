from pickle import FALSE
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from AppGR.models import Sombras, Base, Brochas, Avatar, Blog
from django.template import loader
from AppGR.forms import SombrasForm, BaseForm, BrochasForm, UserRegisterForm, UserUpdateForm, AvatarForm, BlogForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.

def inicio(request):

      return render(request, "inicio.html", {"avatar": obtenerAvatar(request)})

def about(request):
      return render(request, "about.html", {"avatar": obtenerAvatar(request)})

def sombras(request):
      sombras = Sombras.objects.all()
      return render(request, "sombras.html", {'sombras': sombras, "avatar": obtenerAvatar(request)})


def base(request):
      base = Base.objects.all()
      return render(request, "base.html", {'base': base, "avatar": obtenerAvatar(request)})


def brochas(request):
      brochas = Brochas.objects.all()
      return render(request, "brochas.html", {'brochas': brochas, "avatar": obtenerAvatar(request)})


@login_required
def sombras_formulario(request):
      if request.method == 'POST':
            formulario= SombrasForm(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  sombras = Sombras(codigo=data['codigo'], color=data['color'], tipo=data['tipo']  )
                  sombras.save()
                  return render(request, "inicio.html", {"exitoso": True, "avatar": obtenerAvatar(request)})
      else:  
            formulario= SombrasForm()  
      return render(request, "form_sombras.html", {"formulario": formulario, "avatar": obtenerAvatar(request)})


@login_required 
def busqueda_sombras(request):
      return render(request, "form_busqueda_sombras.html", {"avatar": obtenerAvatar(request)})


@login_required 
def buscar_sombras(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            sombras = Sombras.objects.filter(codigo__icontains=codigo)
            return render(request, "sombras.html", {'sombras': sombras, "avatar": obtenerAvatar(request)})
      else:
            return render(request, "sombras.html", {'sombras': [], "avatar": obtenerAvatar(request)})

@login_required 
def base_formulario(request):
      if request.method == 'POST':
            formulario1= BaseForm(request.POST)

            if formulario1.is_valid():
                  data = formulario1.cleaned_data
                  base = Base(codigo=data['codigo'], tono=data['tono'], cobertura=data['cobertura']  )
                  base.save()
                  return render(request, "inicio.html", {"exitoso": True, "avatar": obtenerAvatar(request)})
      else:  
            formulario1= BaseForm() 
      return render(request, "form_base.html", {"formulario": formulario1, "avatar": obtenerAvatar(request)})

@login_required 
def busqueda_base(request):
            return render(request, "form_busqueda_base.html", {"avatar": obtenerAvatar(request)})

@login_required 
def buscar_base(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            base = Base.objects.filter(codigo__icontains=codigo)
            return render(request, "base.html", {'base': base, "avatar": obtenerAvatar(request)})
      else:
            return render(request, "base.html", {'base': [], "avatar": obtenerAvatar(request)})

@login_required 
def brochas_formulario(request):
      if request.method == 'POST':
            formulario2= BrochasForm(request.POST)

            if formulario2.is_valid():
                  data = formulario2.cleaned_data
                  brochas = Brochas(numero=data['numero'], clase=data['clase'] )
                  brochas.save()
                  return render(request, "inicio.html", {"exitoso": True, "avatar": obtenerAvatar(request)})
      else:  
            formulario2= BrochasForm()  
      return render(request, "form_brochas.html", {"formulario": formulario2, "avatar": obtenerAvatar(request)})

@login_required 
def busqueda_brochas(request):
            return render(request, "form_busqueda_brochas.html", {"avatar": obtenerAvatar(request)})

@login_required 
def buscar_brochas(request):
      if request.GET["numero"]:
            numero = request.GET["numero"]
            brochas = Brochas.objects.filter(numero__icontains=numero)
            return render(request, "brochas.html", {'brochas': brochas, "avatar": obtenerAvatar(request)})
      else:
            return render(request, "brochas.html", {'brochas': [], "avatar": obtenerAvatar(request)})

@login_required
def eliminar_sombra(request, id):
    sombra = Sombras.objects.get(id=id)
    sombra.delete()
    sombra = Sombras.objects.all()
    return render(request, "sombras.html", {'sombras': sombras, "avatar": obtenerAvatar(request)})

@login_required
def editar_sombra(request, id):
    sombra = Sombras.objects.get(id=id)

    if request.method == 'POST':
        formulario = SombrasForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            sombra.codigo = data['codigo']
            sombra.color = data['color']
            sombra.tipo = data['tipo']
            sombra.save()
            sombra= Sombras.objects.all()
            return render(request, "sombras.html", {'sombras': sombras, "avatar": obtenerAvatar(request)})
    else:  
      formulario=SombrasForm(initial={"codigo":sombra.codigo, "color":sombra.color, "tipo":sombra.tipo})
      return render(request, "form_sombras.html", {"formulario": formulario, "avatar": obtenerAvatar(request)})

@login_required
def eliminar_base(request, id):
    bases = Base.objects.get(id=id)
    bases.delete()
    bases = Base.objects.all()
    return render(request, "base.html", {'base': base, "avatar": obtenerAvatar(request)})

@login_required
def editar_base(request, id):
    bases = Base.objects.get(id=id)

    if request.method == 'POST':
        formulario = BaseForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            bases.codigo = data['codigo']
            bases.tono = data['tono']
            bases.cobertura = data['cobertura']
            bases.save()
            bases= Base.objects.all()
            return render(request, "base.html", {'base': bases, "avatar": obtenerAvatar(request)})
    else:  
      formulario=BaseForm(initial={"codigo":bases.codigo, "tono":bases.tono, "cobertura":bases.cobertura})
      return render(request, "form_base.html", {"formulario": formulario, "avatar": obtenerAvatar(request)})


@login_required
def eliminar_brocha(request, id):
    brocha = Brochas.objects.get(id=id)
    brocha.delete()
    brocha = Brochas.objects.all()
    return render(request, "brochas.html", {'brochas': brochas, "avatar": obtenerAvatar(request)})

@login_required
def editar_brocha(request, id):
    brocha = Brochas.objects.get(id=id)

    if request.method == 'POST':
        formulario = BrochasForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            brocha.numero = data['numero']
            brocha.clase = data['clase']
            brocha.save()
            brocha= Sombras.objects.all()
            return render(request, "brochas.html", {'brochas': brochas, "avatar": obtenerAvatar(request)})
    else:  
      formulario=BrochasForm(initial={"numero":brocha.numero, "clase":brocha.clase})
      return render(request, "form_brochas.html", {"formulario": formulario, "avatar": obtenerAvatar(request)})


class CustomLogoutView(LogoutView):
      template_name = 'logout.html'
      next_page = reverse_lazy('login')


def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, "inicio.html", {"mensaje": f"Usuario {username} creado correctamente:"})

            else:
                  return render(request, "register.html", {"formulario":form,"mensaje": "Registro inválido"})

      else:
            form=UserRegisterForm()
            return render(request, "register.html", {"formulario":form})


def login_request(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                  usu = form.cleaned_data.get('username')
                  clave = form.cleaned_data.get('password')
                  usuario = authenticate(username=usu, password=clave)

                  if usuario is not None:
                        login(request, usuario) 
                        return render(request, "inicio.html", {"mensaje":f"Bienvenido a nuestra tienda de maquillaje {usuario}"})                        
                  else:
                        return render(request, "login.html", {"formulario":form, "mensaje":"Error, los datos ingresados son incorrectos"})
            else:
                  return render(request, "login.html", {"formulario":form, "mensaje": "Error, los datos ingresados son incorrectos"})
      else:
            form = AuthenticationForm()
            return render(request, "login.html", {'formulario':form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
      model = User
      form_class = UserUpdateForm    
      success_url = reverse_lazy('inicio')
      template_name = "form_perfil.html"
      
      def get_object(self, queryset=None):
          return self.request.user 


def agregarAvatar(request):
      if request.method == 'POST':     
            formulario = AvatarForm(request.POST, request.FILES)  
            if formulario.is_valid():
                  avatarViejo=Avatar.objects.filter(user=request.user.id)
                  if(len(avatarViejo)>0):
                        avatarViejo[0].delete()
                  avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, 'inicio.html', {'usuario':request.user, 'mensaje':'Avatar Agregardo Exitosamente!', "imagen":avatar.imagen.url})
            else:
                  return render(request, 'agregarAvatar.html', {'formulario':formulario, 'mensaje':'Formulario inválido'})
      else:
            formulario = AvatarForm()
            return render(request, "agregarAvatar.html", {"formulario":formulario, "usuario":request.user})

def obtenerAvatar(request):
      lista=Avatar.objects.filter(user=request.user.id)
      if len(lista)!=0:
            imagen=lista[0].imagen.url
      else:
            imagen="/media/avatares/avatarpordefecto.jpg"
      return imagen

def blog(request):
      blog = Blog.objects.all()
      return render(request, "blog.html", {'blog': blog, "avatar": obtenerAvatar(request)})

@login_required
def blog_formulario(request):
      if request.method == 'POST':
            formulario= BlogForm(request.POST)

            if formulario.is_valid():
                  blog = formulario.save(commit=FALSE)
                  blog.save()
                  return redirect ('/')
      else:  
            formulario= BlogForm()  
      return render(request, "form_blog.html", {"formulario": formulario, "avatar": obtenerAvatar(request)})

@login_required
def edit_blog(request, blog_id=None):
      item = get_object_or_404(Blog, id=blog_id)
      formulario = BlogForm(request.POST or None, instance=item)
      if formulario.is_valid():
            formulario.save()
            return redirect('/')
      return render(request, "form_blog.html", {'formulario': formulario, "avatar": obtenerAvatar(request)})