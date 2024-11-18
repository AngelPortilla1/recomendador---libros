from django.urls import path
from api_libros.vistas.data_libros import GetLibroList
from .vistas.views import LibroListView
from api_libros.vistas import views


urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),  # Ruta base: /libros/
    path('all/', GetLibroList.as_view(), name='libros-list'),
    
    
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    
]
