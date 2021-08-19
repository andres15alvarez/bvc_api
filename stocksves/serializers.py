from rest_framework import serializers
from stockves.models import StockVES


class StockVESSerializer(serializers.ModelSerializer):

	class Meta:
		model = StockVES
		exclude = ['id']