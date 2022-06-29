from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.functions import Cast
from django.db.models import F, FloatField
from .serializers import MahsoulSerializer
from .models import Mahsoul


class MahsoulView(APIView):
    def post(self, request):
        ser_data = MahsoulSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response({'message': 'ok'})
        return  Response({'message': 'error'})

    def get(self, request):
        products = Mahsoul.objects.all().annotate(discount = Cast(F('old_price') - F('price'), FloatField())/Cast(F('old_price') / 100, FloatField()))
        ser_data = MahsoulSerializer(products, many=True)
        return Response(ser_data.data)

class MahsoulRetrieveView(APIView):
    def get(self, request, value):
        products = Mahsoul.objects.annotate(discount = Cast(F('old_price') - F('price'), FloatField())/Cast(F('old_price') / 100, FloatField()))
        filter = products.filter(discount=value)
        ser_data = MahsoulSerializer(filter, many=True)
        return Response(ser_data.data)
