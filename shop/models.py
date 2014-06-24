from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from cms.models import CMSPlugin
from sorl.thumbnail import ImageField


class Carousel(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="", blank=True)
    image = ImageField(upload_to="carousel/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="", blank=True)
    options = models.TextField(default="", blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True, editable=True, blank=True)
    price = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name



class Feature(models.Model):
    name = models.CharField(default="", max_length=120)
    html_class = models.CharField(max_length=30, default="")
    description = models.TextField(default="")
    image = models.ImageField(upload_to="features/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name


class FeaturePlugin(CMSPlugin):
    feature1 = models.ForeignKey("shop.Feature", related_name="plugins1")
    feature2 = models.ForeignKey("shop.Feature", related_name="plugins2")
    feature3 = models.ForeignKey("shop.Feature", related_name="plugins3")

    def __unicode__(self):
        return self.feature1.name + ', ' + self.feature2.name + ', ' + self.feature3.name


class Website(models.Model):
    name = models.CharField(max_length=30, default="")
    user = models.ForeignKey(User)
    plan = models.ForeignKey(Plan)
    domain = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=2, default="")
    currency = models.CharField(max_length=3, default="EUR")
    created = models.BooleanField(default=False)
    date_add = models.DateTimeField(default=datetime.now, auto_now_add=True, blank=True)
    date_mod = models.DateTimeField(default=datetime.now, auto_now=True, blank=True)

    def __unicode__(self):
        return self.name + ' [' + self.domain + ']'


class Subscriptions(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    plan = models.ForeignKey(Plan)
    website = models.ForeignKey(Website)

