from django.urls import path
from app.apis.viewsets import (
    PropertyListCreateView,
    PropertyRetrieveUpdateDestroyView,
    AdListCreateView,
    AdRetrieveUpdateView,
    ReservationListCreateView,
    ReservationRetreiveDestroyView,
)

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='properties'),
    path('properties/<pk>/', PropertyRetrieveUpdateDestroyView.as_view(), name='property-detail'),

    path('ads/', AdListCreateView.as_view(), name='ads'),
    path('ads/<pk>/', AdRetrieveUpdateView.as_view(), name='ad-detail'),

    path('reservations/', ReservationListCreateView.as_view(), name='reservations'),
    path('reservations/<pk>/', ReservationRetreiveDestroyView.as_view(), name='reservation-detail'),
]