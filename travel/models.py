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
  is_completed = models.BooleanField(default=False)
  youtube_url = models.CharField(max_length=250)
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

  def __str__(self):
    return self.street + ", " +self.city + ", " + self.state

  def full(self):
    return self.street + ", " +self.city + ", " + self.state 

class Contact(models.Model):
  name = models.CharField(max_length=150)
  phone = PhoneNumberField(unique=True)
  email = models.CharField(max_length=150)
  address = models.ForeignKey('Address', null=True, blank=True)
  willing_to_be_on_camera = models.BooleanField(default=False)

  def __str__(self):
    return self.name + ":   " + self.address.__str__()

class Couch(models.Model):
  address = models.ForeignKey('Address')
  contact = models.ForeignKey('Contact')

  def __str__(self):
    return None


# choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]
