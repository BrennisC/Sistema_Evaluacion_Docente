from rest_framework import viewsets
from .models import Docente
from .serializers import DocenteSerializer
# Create your views here.


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer