import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from app.models import Property, Ad, Reservation
from app.apis.serializers import PropertySerializer, AdSerializer, ReservationSerializer


class PropertyViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.property_data = {
            'name': 'Casa na Cidade',
            'num_bathrooms': 3,
            'accept_animals': True,
            'cleaning_price': 155.00,
            'gest_limit': 12,
            'activate_date': '2023-01-01T00:00:00Z'
        }
        self.response = self.client.post(
            '/api/properties/',
            self.property_data,
            format='json'
        )

    def test_api_can_create_a_property(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_property(self):
        property = Property.objects.get()
        response = self.client.get(
            f'/api/properties/{property.id}/',
            format='json'
        )
        serializer = PropertySerializer(property)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_property(self):
        property = Property.objects.get()

        new_property_data = {
            'name': 'Casa atualizada',
            'num_bathrooms': 4,
            'accept_animals': False,
            'cleaning_price': 200.0,
            'gest_limit': 8,
            'activate_date': '2022-12-30T00:00:00Z'
        }
        response = self.client.put(reverse('property-detail', kwargs={'pk': property.pk}), new_property_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        property.refresh_from_db()
        self.assertEqual(property.name, 'Casa atualizada')
        self.assertEqual(property.num_bathrooms, 4)
        self.assertFalse(property.accept_animals)
        self.assertEqual(property.cleaning_price, 200.0)
        self.assertEqual(property.gest_limit, 8)
        self.assertEqual(property.activate_date, datetime.datetime(2022, 12, 30, 0, 0, tzinfo=datetime.timezone.utc))

    def test_api_can_delete_property(self):
        property = Property.objects.first()
        url = reverse('property-detail', kwargs={'pk': property.id})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Property.objects.count(), 0)

    def test_api_can_list_property(self):
        Property.objects.create(
            name = 'Apartamento na Cidade',
            num_bathrooms = 2,
            accept_animals = True,
            cleaning_price = 200.00,
            gest_limit = 4,
            activate_date = datetime.date(2023, 1, 1)
        )
        response = self.client.get('/api/properties/')

        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_api_can_detail_property(self):
        property_data = {
            'name': 'Casa na Cidade',
            'num_bathrooms': 3,
            'accept_animals': True,
            'cleaning_price': 155.00,
            'gest_limit': 12,
            'activate_date': '2023-01-01T00:00:00Z'
        }

        serializer = PropertySerializer(data=property_data)
        if serializer.is_valid():
            serializer.save()
        else:
            self.fail(serializer.errors)

        response = self.client.get(reverse("property-detail", kwargs={"pk": serializer.data["id"]}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], serializer.data["id"])
        self.assertEqual(response.data, serializer.data)


class AdViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.property = Property.objects.create(
            name = 'Apartamento na Cidade',
            num_bathrooms = 2,
            accept_animals = True,
            cleaning_price = 200.00,
            gest_limit = 4,
            activate_date = datetime.date(2023, 1, 1)
        )

        self.ad_data = {
            'property': self.property.id,
            'platform_name': 'AirBnB',
            'platform_tax': 1.0
        }

        self.response = self.client.post(
            '/api/ads/',
            self.ad_data,
            format='json'
        )

    def test_api_can_create_a_ad(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_ad(self):
        ad = Ad.objects.get()
        response = self.client.get(
            f'/api/ads/{ad.id}/',
            format='json'
        )
        serializer = AdSerializer(ad)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_ad(self):
        ad = Ad.objects.get()

        new_ad_data = {
            'property': self.property.id,
            'platform_name': 'AirBnB',
            'platform_tax': 12.00
        }

        response = self.client.put(reverse('ad-detail', kwargs={'pk': ad.pk}), new_ad_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        ad.refresh_from_db()
        self.assertEqual(ad.property, self.property)
        self.assertEqual(ad.platform_name, 'AirBnB')
        self.assertEqual(ad.platform_tax, 12.00)

    def test_api_can_list_ad(self):
        Ad.objects.create(
            property=self.property,
            platform_name='TripAdvisor',
            platform_tax=20.00,
        )
        response = self.client.get('/api/ads/')

        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_api_can_detail_ad(self):
        ad_data = {
            'property': self.property.id,
            'platform_name': 'AirBnB',
            'platform_tax': 1.0
        }

        serializer = AdSerializer(data=ad_data)
        if serializer.is_valid():
            serializer.save()
        else:
            self.fail(serializer.errors)

        response = self.client.get(reverse("ad-detail", kwargs={"pk": serializer.data["id"]}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], serializer.data["id"])
        self.assertEqual(response.data, serializer.data)


class ReservationViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.property = Property.objects.create(
            name = 'Apartamento na Cidade',
            num_bathrooms = 2,
            accept_animals = True,
            cleaning_price = 200.00,
            gest_limit = 4,
            activate_date = datetime.date(2023, 1, 1)
        )

        self.ad = Ad.objects.create(
            property=self.property,
            platform_name='TripAdvisor',
            platform_tax=20.00,
        )

        self.reservation_data = {
            "ad": self.ad.id,
            "check_in": datetime.date(2023, 1, 1),
            "check_out": datetime.date(2023, 1, 2),
            "guests": 2,
            "comment": "Beautiful",
            "total_price": 102.30,
        }

        self.response = self.client.post(
            '/api/reservations/',
            self.reservation_data,
            format='json'
        )

    def test_api_can_create_a_reservation(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_reservation(self):
        reservation = Reservation.objects.get()
        response = self.client.get(
            f'/api/reservations/{reservation.id}/',
            format='json'
        )
        serializer = ReservationSerializer(reservation)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_reservation(self):
        reservation = Reservation.objects.first()
        url = reverse('reservation-detail', kwargs={'pk': reservation.id})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reservation.objects.count(), 0)

    def test_api_can_list_reservation(self):
        Reservation.objects.create(
            ad = self.ad,
            check_in = datetime.date(2023, 1, 1),
            check_out = datetime.date(2023, 1, 2),
            guests = 2,
            comment= "Beautiful",
            total_price = 102.30,
        )
        response = self.client.get('/api/reservations/')

        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_api_can_detail_reservation(self):
        reservation_data = {
            "ad": self.ad.id,
            "check_in": datetime.date(2023, 1, 1),
            "check_out": datetime.date(2023, 1, 2),
            "guests": 2,
            "comment": "Beautiful",
            "total_price": 102.30,
        }

        serializer = ReservationSerializer(data=reservation_data)
        if serializer.is_valid():
            serializer.save()
        else:
            self.fail(serializer.errors)

        response = self.client.get(reverse("reservation-detail", kwargs={"pk": serializer.data["id"]}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], serializer.data["id"])
        self.assertEqual(response.data, serializer.data)
