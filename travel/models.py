from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, PhoneNumberField
from django.db import models
from django.utils.encoding import smart_str

import requests, simplejson

# Create your models here.
class Mission(models.Model):
  description = models.TextField()
  anything_else = models.TextField()
  longitude = models.FloatField(default=0.0)
  latitude = models.FloatField(default=0.0)
  is_approved = models.BooleanField(default=False)
  is_current = models.BooleanField(default=False)
  # is_completed = models.BooleanField(default=False)
  address = models.ForeignKey('Address')
  contact = models.ForeignKey('Contact')

  def __str__(self):
    return self.description

  def city_state(self):
    return self.address.city.title() + ", " + self.address.state.upper()

  def geolocate(self):
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false'.format(self.address.full())
    response = requests.get(url)
    if response.status_code == 200:
       lat = float(response.json()['results'][0]['geometry']['location']['lat'])
       lng = float(response.json()['results'][0]['geometry']['location']['lng'])
       return [lat, lng]
    else:
      return HttpResponse('Please try again, we could not geolocate your address')

class Address(models.Model):
  city = models.CharField(max_length=200)
  street = models.CharField(max_length=200)
  state = USStateField(choices=STATE_CHOICES)
  zip = models.CharField(max_length=33, blank=True)

  def __str__(self):
    return self.city + ", " + self.state

  def full(self):
    return self.street + ", " +self.city + ", " + self.state + ", " + self.zip

class Contact(models.Model):
  name = models.CharField(max_length=150)
  phone = PhoneNumberField(unique=True)
  email = models.CharField(max_length=150)
  address = models.ForeignKey('Address', null=True, blank=True)
  willing_to_be_on_camera = models.BooleanField(default=False)

  def __str__(self):
    return self.name


class Couch(models.Model):
  address = models.ForeignKey('Address')
  contact = models.ForeignKey('Contact')
