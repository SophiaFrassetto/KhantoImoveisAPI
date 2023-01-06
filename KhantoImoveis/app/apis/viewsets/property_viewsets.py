from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.apis.serializers import PropertySerializer
from app.models import Property


class PropertyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyListCreateView(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
