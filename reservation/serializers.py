from rest_framework import serializers

from reservation.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    res_id = serializers.IntegerField(source='pk', read_only=True)
    executed = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reservation
        fields = ["res_id", "data_begin", "data_end", "executed", "type", "user"]
