from rest_framework import serializers
from ibc.models import IBC


class IBCSerializer(serializers.ModelSerializer):

	class Meta:
		model = IBC
		exclude = ['id']


class IBCRangeSerializer(serializers.Serializer):
	date_from = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
	date_to = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
