from django import forms
from travel.models import Mission, Contact, Address
from localflavor.us.forms import USPhoneNumberField

class MissionForm(forms.ModelForm):
  description = forms.CharField(widget = forms.Textarea(attrs={'cols': 17, 'rows': 5}))
  anything_else = forms.CharField(widget = forms.Textarea(attrs={'cols': 15, 'rows': 5}), required=False)
  is_approved = forms.BooleanField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Mission
    fields = ('description','anything_else',)

class ContactForm(forms.ModelForm):
  name = forms.CharField(max_length=150)
  phone = USPhoneNumberField()
  email = forms.CharField(max_length=150)
  willing_to_be_on_camera = forms.BooleanField(widget=forms.CheckboxInput, required=False)

  class Meta:
    model = Contact
    fields = ('name','phone','email', 'willing_to_be_on_camera')

class AddressForm(forms.ModelForm):
  class Meta:
    model = Address
    fields = ('street','city','state',)