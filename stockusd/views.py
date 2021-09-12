"""Stock on USD Views."""
from rest_framework import generics, status
from rest_framework.response import Response
from stockusd.models import StockUSD
from stockusd.serializers import StockUSDSerializer


class StockUSDView(generics.ListAPIView):
	"""List View to get all records of transactions daily given a date range and/or
		a company code.

		Query Params:
			company_code (str): Optional company code (RST)
			date_from (str): String format YYYY-MM-DD to date (2021-01-01)
			date_to (str): String format YYYY-MM-DD to date (2021-01-01)

	"""

	def get_queryset(self):
		company_code = self.request.query_params.get('company_code', '')
		date_from = self.request.query_params.get('date_from')
		date_to = self.request.query_params.get('date_to')
		if date_from and date_to:
			return StockUSD.objects.filter(
				date__range=(date_from, date_to), 
				code=company_code
			)
		raise Exception('query params null')

	def list(self, *args, **kwargs):
		try:
			queryset = self.get_queryset()
			serializer = StockUSDSerializer(queryset, many=True)
			return Response({'data': serializer.data}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
