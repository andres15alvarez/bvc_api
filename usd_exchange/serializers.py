from rest_framework import serializers
from usd_exchange.models import USDExchange


class USDExchangeSerializer(serializers.ModelSerializer):

	class Meta:
		model = USDExchange
		exclude = ['id']