from django_filters import rest_framework as filters
from property.models import House


class HouseAreaFilter(filters.FilterSet):
    min_area = filters.NumberFilter(field_name="area", lookup_expr="gte")
    max_area = filters.NumberFilter(field_name="area", lookup_expr="lte")

    class Meta:
        model = House
        fields = ['area']
