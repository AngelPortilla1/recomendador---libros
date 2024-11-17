from django.shortcuts import render
from rest_framework.generics import ListAPIView
from ..modelos.models import Libro
from ..serializers import LibroSerializer

class LibroListView(ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
