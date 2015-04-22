from django.http import HttpResponse
from django.shortcuts import render
from travel.models import Mission, Contact
from travel.forms import MissionForm, ContactForm

# Create your views here.
def index(request):
  mission_form = MissionForm()
  contact_form = ContactForm()
  context_dict = {'mission_form' : mission_form,
                  'contact_form' : contact_form}
  return render(request, 'travel/index.html', context_dict)


def add_mission(request):
  if request.method == 'POST':
    mission_form = MissionForm(request.POST)
    contact_form = ContactForm(request.POST)
    if mission_form.is_valid() and contact_form.is_valid():
      contact = Contact(name=request.POST['name'], 
                        phone=request.POST['phone'], 
                        email=request.POST['email'])
      contact.save()
      mission = Mission(description=request.POST['description'],
                        anything_else=request.POST['anything_else'])
      mission.contact_id = contact.id
      mission.save()
    else:
      print(mission_form.errors)
      print(contact_form.errors)
      return HttpResponse('Form Errors!!')
  else:
    return HttpResponse('Broken Form Brah')
  return index(request)