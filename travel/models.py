from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, PhoneNumberField
# from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Mission(models.Model):
  description = models.TextField()
  anything_else = models.TextField()
  is_approved = models.BooleanField(default=False)
  contact = models.ForeignKey('Contact')

  def __str__(self):
    return self.description

class Couch(models.Model):
  address = models.ForeignKey('Address')
  contact = models.ForeignKey('Contact')

class Address(models.Model):
  street = models.CharField(max_length=200)
  state = USStateField(choices=STATE_CHOICES)
  zip = models.CharField(max_length=33, blank=True)  
  country = models.CharField(max_length=150, blank=True) 
  contact = models.ForeignKey('Contact')

class Contact(models.Model):
  name = models.CharField(max_length=150)
  phone = PhoneNumberField(unique=True)
  email = models.CharField(max_length=150)

  def __str__(self):
    return self.name
