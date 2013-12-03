from rest_framework import viewsets
from serializers import TiendaSerializer, CadenaSerializer
from app.apps.demo.models import Tienda, Cadena

class TiendaViewSet(viewsets.ModelViewSet):
	queryset = Tienda.objects.all()
	serializer_class = TiendaSerializer

class CadenaViewSet(viewsets.ModelViewSet):
	queryset = Cadena.objects.all()
	serializer_class = CadenaSerializer