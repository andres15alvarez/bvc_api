"""IBC Views."""
from rest_framework import generics, status
from rest_framework.response import Response
from ibc.models import IBC
from ibc.serializers import IBCSerializer


class IBCView(generics.ListAPIView):
	"""List View to get all records of IBC daily given a date range.

		Query Params:
			date_from (str): String format YYYY-MM-DD to date (2021-01-01)
			date_to (str): String format YYYY-MM-DD to date (2021-01-01)

	"""

	def get_queryset(self):
		date_from = self.request.query_params.get('date_from')
		date_to = self.request.query_params.get('date_to')
		if date_from and date_to:
			return IBC.objects.filter(date__range=(date_from, date_to))
		raise Exception('query params null')

	def list(self, *args, **kwargs):
		try:
			queryset = self.get_queryset()
			serializer = IBCSerializer(queryset, many=True)
			return Response({'data': serializer.data}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
