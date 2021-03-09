from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ad.permissions import IsOwnerOrReadOnly
from reservation.models import Reservation
from reservation.serializers import ReservationSerializer


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.filter()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.validated_data['user'] = self.request.user
        serializer.save()

