from rest_framework import serializers
from .models import Planeta
import requests
import swapi


# Serializers define the API representation.
class PlanetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planeta
        fields = ['id', 'url', 'nome', 'clima', 'terreno']
