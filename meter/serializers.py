from rest_framework import serializers

from meter.models import Indication


class IndicationSerializer(serializers.ModelSerializer):
    ind_id = serializers.IntegerField(source='pk', read_only=True)
    created = serializers.StringRelatedField(read_only=True)
    meter = serializers.StringRelatedField()

    class Meta:
        model = Indication
        fields = ["ind_id", "meter", "value", "created"]
