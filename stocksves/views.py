from rest_framework import generics
from stockves.models import StockVES
from stockves.serializers import StockVESSerializer


class StockVESView(generics.ListAPIView):

	serializer_class = StockVES
	filterset_Fields = ['date_from', 'date_to']

	def get_queryset(self):
		date_from = self.request.query_params.get('date_from', '')
		date_to = self.request.query_params.get('date_to', '')
		return StockVES.objects.filter(date__range=(date_from, date_to))

	def list(self):
		queryset = self.get_queryset()
		serializer = StockVESSerializer(queryset, many=true)
		return Response(serializer.data)
