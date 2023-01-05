from django.db import models


class Property(models.Model):
    """
    Model representing a property.
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    accept_animals = models.BooleanField()
    cleaning_price = models.DecimalField(max_digits=8, decimal_places=2)
    gest_limit = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Platform(models.Model):
    """
    Model representing a platform.
    """
    name = models.CharField(max_length=200)
    tax = models.DecimalField(max_digits=3, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ad(models.Model):
    """
    Model representing an ad for a property.
    """
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    platform = models.ForeignObject(Platform, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    """
    Model representing a reservation for an ad.
    """
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
