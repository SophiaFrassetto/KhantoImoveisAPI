import uuid
from django.db import models


class Property(models.Model):
    """
    Model representing a property.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=200)
    num_bathrooms = models.PositiveIntegerField()
    accept_animals = models.BooleanField()
    cleaning_price = models.DecimalField(max_digits=8, decimal_places=2)
    gest_limit = models.PositiveIntegerField()
    activate_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ad(models.Model):
    """
    Model representing an ad for a property.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    platform_name = models.CharField(max_length=50)
    platform_tax = models.DecimalField(max_digits=3, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    """
    Model representing a reservation for an ad.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)

    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
