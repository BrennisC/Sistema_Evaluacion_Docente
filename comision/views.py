from rest_framework import viewsets
from .models import Comision, MiembroComision
from .serializers import ComisionSerializer, MiembroComisionSerializer

# Create your views here.

class ComisionViewSet(viewsets.ModelViewSet):
    queryset = Comision.objects.all()
    serializer_class = ComisionSerializer


class MiembroComisionViewSet(viewsets.ModelViewSet):
    queryset = MiembroComision.objects.all()
    serializer_class = MiembroComisionSerializer