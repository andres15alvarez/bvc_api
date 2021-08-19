from rest_framework import generics
from rest_framework import Response
from stockusd.models import StockUSD
from stockusd.serializers import StockUSDSerializer


class StockUSDView(generics.ListAPIView):

	serializer_class = StockUSD
	filterset_Fields = ['date_from', 'date_to']

	def get_queryset(self):
		date_from = self.request.query_params.get('date_from', '')
		date_to = self.request.query_params.get('date_to', '')
		return StockUSD.objects.filter(date__range=(date_from, date_to))

	def list(self):
		queryset = self.get_queryset()
		serializer = StockUSDSerializer(queryset, many=true)
		return Response(serializer.data)
