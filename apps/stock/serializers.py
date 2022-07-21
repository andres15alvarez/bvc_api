from rest_framework import serializers
from apps.stock.models import Stock


class StockSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=100)

	class Meta:
		model = Stock
		exclude = ['id']
