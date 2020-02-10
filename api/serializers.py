from rest_framework import serializers
from property.models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = [
            'title',
            'link',
            'address',
            'area',
        ]


