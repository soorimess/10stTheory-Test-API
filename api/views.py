from rest_framework import generics
from .serializers import HouseSerializer
from property.models import House
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HouseAreaFilter
from rest_framework import permissions


class HouseCreate(generics.CreateAPIView):
    serializer_class = HouseSerializer


class HouseAreaListView(generics.ListAPIView):
    serializer_class = HouseSerializer
    filterset_class = HouseAreaFilter
    queryset = House.objects.all()
    filter_backends = (DjangoFilterBackend,)

    # def get_queryset(self):
    #     min_area = self.kwargs['min']
    #     max_area = self.kwargs['max']
    #     queryset = House.objects.filter(area__range=(min_area, max_area))
    #     return queryset



