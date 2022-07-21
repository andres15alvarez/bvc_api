"""IBC Views."""
from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from apps.ibc.models import IBC
from apps.ibc.serializers import IBCSerializer, IBCRangeSerializer


class IBCView(generics.ListAPIView):
	"""List View to get all records of IBC daily given a date range.

		Query Params:
			date_from (str): String format YYYY-MM-DD to date (2021-01-01)
			date_to (str): String format YYYY-MM-DD to date (2021-01-01)

	"""

	def list(self, *args, **kwargs):
		serializer = IBCRangeSerializer(data=self.request.query_params)
		serializer.is_valid(raise_exception=True)
		date_from = serializer.validated_data["date_from"]
		date_to = serializer.validated_data["date_to"]
		serializer = IBCSerializer(IBC.objects.filter(date__range=(date_from, date_to)), many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
