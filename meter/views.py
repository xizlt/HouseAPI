from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ad.permissions import IsOwnerOrReadOnly
from meter.models import Indication
from meter.serializers import IndicationSerializer


class IndicationViewSet(ModelViewSet):
    queryset = Indication.objects.filter()
    serializer_class = IndicationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     if self.request.user.is_authenticated:
    #         serializer.validated_data['user'] = self.request.user
    #     serializer.save()