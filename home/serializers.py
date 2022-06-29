from rest_framework import serializers
from .models import Mahsoul


class MahsoulSerializer(serializers.ModelSerializer):
    discount = serializers.FloatField()

    class Meta:
        model = Mahsoul
        fields = ('name', 'price', 'old_price', 'discount')
        