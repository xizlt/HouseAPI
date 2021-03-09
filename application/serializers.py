from rest_framework import serializers

from application.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    app_id = serializers.IntegerField(source='pk', read_only=True)
    executed = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = ["app_id", "title", "due_data", "executed",  "mark", "type", "user"]
