from rest_framework import serializers
from app.apps.demo.models import Tienda, Cadena

class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('url', 'nombre','direccion','cadena',)

class CadenaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cadena
        fields = ('url', 'nombre',)