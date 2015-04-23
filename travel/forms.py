from django import forms
from travel.models import Mission, Contact
from localflavor.us.forms import USPhoneNumberField

class MissionForm(forms.ModelForm):
  description = forms.CharField(widget = forms.Textarea(attrs={'cols': 17, 'rows': 6}))
  anything_else = forms.CharField(widget = forms.Textarea(attrs={'cols': 15, 'rows': 4}), required=False)
  is_approved = forms.BooleanField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Mission
    fields = ('description','anything_else',)

class ContactForm(forms.ModelForm):
  name = forms.CharField(max_length=150)
  phone = USPhoneNumberField()
  email = forms.CharField(max_length=150)

  class Meta:
    model = Contact
    fields = ('name','phone','email',)