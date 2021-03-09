from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from ad.permissions import IsOwnerOrReadOnly
from application.models import Application
from application.serializers import ApplicationSerializer


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.validated_data['user'] = self.request.user
        serializer.save()