from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from app.apis.serializers import ReservationSerializer
from app.models import Reservation


class ReservationListCreateView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationRetreiveDestroyView(RetrieveDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        check_in = serializer.validated_data['check_in']
        check_out = serializer.validated_data['check_out']
        if check_in >= check_out:
            return Response({"error": "check_in must be less than check_out"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
