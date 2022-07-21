"""USD Exchange rate Views."""
from rest_framework import generics, status
from rest_framework.response import Response
from apps.exchange.models import ExchangeRate
from apps.exchange.serializers import ExchangeRateSerializer, ExchangeRateRangeSerializer


class ExchangeRateView(generics.ListAPIView):
	"""List View to get all records of usd exchange rate daily given a date range.

		Query Params:
			date_from (str): String format YYYY-MM-DD to date (2021-01-01)
			date_to (str): String format YYYY-MM-DD to date (2021-01-01)

	"""

	def list(self, *args, **kwargs):
		serializer = ExchangeRateRangeSerializer(data=self.request.query_params)
		serializer.is_valid(raise_exception=True)
		date_from = serializer.validated_data["date_from"]
		date_to = serializer.validated_data["date_to"]
		queryset = ExchangeRate.objects.filter(date__range=(date_from, date_to))
		serializer = ExchangeRateSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
