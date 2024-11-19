from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView
from ..modelos.models import Libro
from ..serializers import LibroSerializer

class LibroListView(ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
""" 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..user_serializers import UsuarioSerializer

class CrearUsuarioAPIView(View):
    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response(
                {
                    "message": "Usuario creado exitosamente",
                    "user_id": usuario.id,
                    "email": usuario.email,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

Usuario = get_user_model()

def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f"Usuario '{usuario.username}' creado exitosamente.")
            return redirect('iniciar_sesion')  # Redirige a la página de inicio
        else:
            messages.error(request, "Hubo un error al crear el usuario. Revisa los datos.")
    else:
        form = UserCreationForm()

    return render(request, 'crear_usuario.html', {'form': form})

"""


"""
from django.shortcuts import render, redirect
from ..forms import RegistroUsuarioForm
from django.contrib import messages

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Guarda el usuario
                messages.success(request, "Usuario registrado exitosamente.")
                return redirect('iniciar_sesion')  # Redirige al login
            except Exception as e:
                messages.error(request, f"Error al registrar el usuario: {str(e)}")
        else:
            # Captura los errores del formulario
            for field, error in form.errors.items():
                messages.error(request, f"{field}: {error}")
    else:
        form = RegistroUsuarioForm()

    return render(request, 'crear_usuario.html', {'form': form})
"""








#AQUIII -----------------------------------------------------------



""" 
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

Usuario = get_user_model()

def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f"Usuario '{usuario.username}' creado exitosamente.")
            return redirect('iniciar_sesion')  # Redirige a la página de inicio
        else:
            messages.error(request, "Hubo un error al crear el usuario. Revisa los datos.")
    else:
        form = UserCreationForm()

    return render(request, 'crear_usuario.html', {'form': form})
"""

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
import json

Usuario = get_user_model()

@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        try:
            # Parsear los datos del JSON enviado
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')  # Email opcional

            # Validar que se enviaron los datos necesarios
            if not username or not password:
                return JsonResponse({'error': 'El nombre de usuario y la contraseña son obligatorios.'}, status=400)

            # Verificar si el usuario ya existe
            if Usuario.objects.filter(username=username).exists():
                return JsonResponse({'error': f"El usuario '{username}' ya existe."}, status=400)

            # Crear el usuario
            usuario = Usuario.objects.create(
                username=username,
                email=email,
                password=make_password(password)  # Encripta la contraseña
            )

            return JsonResponse({'message': f"Usuario '{usuario.username}' creado exitosamente."}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)

    return JsonResponse({'error': 'Método no permitido. Usa POST.'}, status=405)

def perfil(request):
    return render(request, 'perfil.html', {'usuario': request.user})

