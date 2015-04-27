from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, PhoneNumberField
from django.db import models

# Create your models here.
class Mission(models.Model):
  description = models.TextField()
  anything_else = models.TextField()
  longitude = models.FloatField(default=0.0)
  latitude = models.FloatField(default=0.0)

  is_approved = models.BooleanField(default=False)
  is_current = models.BooleanField(default=False)
  address = models.ForeignKey('Address')
  contact = models.ForeignKey('Contact')

  def __str__(self):
    return self.description

  def city_state(self):
    return self.address.city.title() + ", " + self.address.state.upper()


class Address(models.Model):
  city = models.CharField(max_length=200)
  street = models.CharField(max_length=200)
  state = USStateField(choices=STATE_CHOICES)
  zip = models.CharField(max_length=33, blank=True)

  def __str__(self):
    return self.city + ", " + self.state


class Contact(models.Model):
  name = models.CharField(max_length=150)
  phone = PhoneNumberField(unique=True)
  email = models.CharField(max_length=150)
  address = models.ForeignKey('Address', null=True, blank=True)

  def __str__(self):
    return self.name


class Couch(models.Model):
  address = models.ForeignKey('Address')
  contact = models.ForeignKey('Contact')
