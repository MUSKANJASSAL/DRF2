from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer

# Create your views here.
# how to get objects in the database

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


