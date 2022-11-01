from django.urls import path

from AppGR import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    path('sombras/', views.sombras, name="sombras"),
    path('base/', views.base, name="base"),
    path('brochas/', views.brochas, name="brochas"),
    path('sombras_formulario/', views.sombras_formulario, name="sombras_formulario"),
    path('form_busqueda_sombras/', views.busqueda_sombras, name="form_busqueda_sombras"),
    path('busqueda_sombras/', views.buscar_sombras, name="busqueda_sombras"),
    path('base_formulario/', views.base_formulario, name="base_formulario"),
    path('form_busqueda_base/', views.busqueda_base, name="form_busqueda_base"),
    path('busqueda_base/', views.buscar_base, name="busqueda_base"),
    path('brochas_formulario/', views.brochas_formulario, name="brochas_formulario"),
    path('form_busqueda_brochas/', views.busqueda_brochas, name="form_busqueda_brochas"),
    path('busqueda_brochas/', views.buscar_brochas, name="busqueda_brochas"),
    path('eliminar_sombra/<id>/', views.eliminar_sombra, name="eliminar_sombra"),
    path('editar_sombra/<id>/', views.editar_sombra, name="editar_sombra"),
    path('eliminar_base/<id>/', views.eliminar_base, name="eliminar_base"),
    path('editar_base/<id>/', views.editar_base, name="editar_base"),
    path('eliminar_brocha/<id>/', views.eliminar_brocha, name="eliminar_brocha"),
    path('editar_brocha/<id>/', views.editar_brocha, name="editar_brocha"),
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar_perfil/', views.ProfileUpdateView.as_view(), name='editar_perfil'),
    path('agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
    path('blog/', views.blog, name='blog'),
    path('blog_formulario/', views.blog_formulario, name='blog_formulario'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    
]