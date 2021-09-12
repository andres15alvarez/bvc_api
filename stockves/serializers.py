from rest_framework import serializers
from stockves.models import StockVES


class StockVESSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=100)

	class Meta:
		model = StockVES
		exclude = ['id']