from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from app.apis.serializers import AdSerializer
from app.models import Ad


class AdRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdListCreateView(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
