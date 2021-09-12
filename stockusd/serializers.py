from rest_framework import serializers
from stockusd.models import StockUSD


class StockUSDSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=100)

	class Meta:
		model = StockUSD
		exclude = ['id']