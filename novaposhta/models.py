from django.db import models


class NovaCity(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)


class NovaOffice(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(NovaCity)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
