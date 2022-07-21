"""USD Exchange rate Views."""
from rest_framework import generics, status
from rest_framework.response import Response
from apps.exchange.models import ExchangeRate
from apps.exchange.serializers import ExchangeRateSerializer


class ExchangeRateView(generics.ListAPIView):
	"""List View to get all records of usd exchange rate daily given a date range.

		Query Params:
			date_from (str): String format YYYY-MM-DD to date (2021-01-01)
			date_to (str): String format YYYY-MM-DD to date (2021-01-01)

	"""

	def get_queryset(self):
		date_from = self.request.query_params.get('date_from')
		date_to = self.request.query_params.get('date_to')
		if date_from and date_to:
			return ExchangeRate.objects.filter(date__range=(date_from, date_to))
		raise Exception('query params null')

	def list(self, *args, **kwargs):
		try:
			queryset = self.get_queryset()
			serializer = ExchangeRateSerializer(queryset, many=True)
			return Response({'data': serializer.data}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
