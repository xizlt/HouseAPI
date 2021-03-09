from rest_framework import serializers

from ad.models import Ad


class AdSerializer(serializers.ModelSerializer):
    ad_id = serializers.IntegerField(source='pk', read_only=True)
    type = serializers.StringRelatedField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ad
        fields = ["ad_id", "title", "beginning", "ending",  "text", 'type', "user"]
