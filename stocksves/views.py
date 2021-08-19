from rest_framework import generics
from stockves.models import StockVES
from stockves.serializers import StockVESSerializer


class StockVESView(generics.ListAPIView):

	queryset = StockVES.objects.all()
	serializer_class = StockVES
	filterset_Fields = ['date_from', 'date_to']
