from rest_framework import serializers
from ibc.models import IBC


class IBCSerializer(serializers.ModelSerializer):

	class Meta:
		model = IBC
		exclude = ['id']