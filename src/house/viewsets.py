from rest_framework import viewsets
from .models import House
from .serializers import HouseSerializer
from .permissions import IsHouseManagerOrNot

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    permission_classes = [IsHouseManagerOrNot,]
    serializer_class = HouseSerializer

