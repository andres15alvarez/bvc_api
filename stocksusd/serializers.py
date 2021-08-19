from rest_framework import serializers
from stockusd.models import StockUSD


class StockUSDSerializer(serializers.ModelSerializer):

	class Meta:
		model = StockUSD
		exclude = ['id']