from .models import Planeta
from rest_framework import viewsets
from .serializers import PlanetaSerializer


#ViewSets define the view behavior.
class PlanetaViewSet(viewsets.ModelViewSet):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer


