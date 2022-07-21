from rest_framework import serializers
from apps.exchange.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):

	class Meta:
		model = ExchangeRate
		exclude = ['id']


class ExchangeRateRangeSerializer(serializers.Serializer):
	date_from = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
	date_to = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
