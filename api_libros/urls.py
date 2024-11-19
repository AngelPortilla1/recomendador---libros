from django.urls import path
from api_libros.vistas.data_libros import GetLibroList
from .vistas.views import LibroListView
from api_libros.vistas import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Otras rutas
    path('iniciar-sesion/', LoginView.as_view(template_name='iniciar_sesion.html'), name='iniciar_sesion'),
]



urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),  # Ruta base: /libros/
    path('all/', GetLibroList.as_view(), name='libros-list'),
    
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    #path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    
    path('iniciar-sesion/', LoginView.as_view(template_name='iniciar_sesion.html'), name='iniciar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]



