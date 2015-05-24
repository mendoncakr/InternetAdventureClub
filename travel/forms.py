from django import forms
from travel.models import Mission, Contact, Address, Couch
from localflavor.us.forms import USPhoneNumberField

SOLO_CHOICES = [(True, 'I want Daniel to do this mission'), (False, 'I want Daniel to help me with this mission')]


class MissionForm(forms.ModelForm):
  description = forms.CharField(widget = forms.Textarea(attrs={'cols': 10, 'rows': 4}))
  anything_else = forms.CharField(widget = forms.Textarea(attrs={'cols': 10, 'rows': 2, 'placeholder':'Anything else?'}), required=False)
  is_approved = forms.BooleanField(widget=forms.HiddenInput(), required=False)
  solo_mission = forms.ChoiceField(widget=forms.RadioSelect, choices=SOLO_CHOICES, required=True)

  class Meta:
    model = Mission
    fields = ('description','anything_else','solo_mission')

class ContactForm(forms.ModelForm):
  name = forms.CharField(max_length=150)
  phone = USPhoneNumberField()
  email = forms.CharField(max_length=150)
  willing_to_be_on_camera = forms.BooleanField(widget=forms.CheckboxInput, required=False)

  class Meta:
    model = Contact
    fields = ('name','phone','email', 'willing_to_be_on_camera')


class AddressForm(forms.ModelForm):
  city = forms.CharField(required=True)
  street = forms.CharField(required=False)

  class Meta:
    model = Address
    fields = ('street','city','state',)

class CouchForm(forms.ModelForm):
  class Meta:
    model = Couch