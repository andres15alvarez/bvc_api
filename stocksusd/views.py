from rest_framework import generics
from stockusd.models import StockUSD
from stockusd.serializers import StockUSDSerializer


class StockUSDView(generics.ListAPIView):

	queryset = StockUSD.objects.all()
	serializer_class = StockUSD
	filterset_Fields = ['date_from', 'date_to']
