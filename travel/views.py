from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from travel.models import Mission, Contact, Address, Couch
from travel.forms import MissionForm, ContactForm, AddressForm, CouchForm

# Create your views here.
def index(request):
  return render(request, 'travel/index.html')

def thanks(request):
  return render(request, 'travel/thanks.html')

def add_mission(request):
  if request.method == 'POST':
    mission_form, contact_form, address_form = MissionForm(request.POST), ContactForm(request.POST), AddressForm(request.POST)
    if mission_form.is_valid() and contact_form.is_valid() and address_form.is_valid():
      mission = Mission(description=request.POST['description'], anything_else=request.POST['anything_else'])
      contact = Contact.objects.get_or_create(phone=request.POST['phone'])
      address = Address.objects.get_or_create(street=request.POST['street'])

      #If contact found
      if contact[1] == False: 
        contact = contact[0]
      else:
        contact = contact[0]
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.save()

      #If address found
      if address[1] == False:
        address = address[0]
      else:
        address = address[0]
        address.city = request.POST['city']
        address.state = request.POST['state']
        address.save()

      mission.contact = contact
      mission.address = address

      # Save coords for mission
      coords = mission.geolocate()
      mission.latitude, mission.longitude = coords[0], coords[1]
      mission.save()
      messages.add_message(request, messages.INFO, 'Thanks! Your mission will be added to the list as soon as Chris spell checks it!')
      return redirect('all_missions')
    else:
      print(mission_form.errors)
      print(contact_form.errors)
      return HttpResponse('Form Errors!!')
  else:
    mission_form, contact_form,address_form = MissionForm(), ContactForm(), AddressForm()
    context_dict = {'mission_form' : mission_form,'contact_form' : contact_form,'address_form' : address_form}
    return render(request, 'travel/register.html', context_dict)

def all_missions(request):
  context_dict = {}
  context_dict['missions'] = Mission.objects.filter(is_approved=True)
  return render(request, 'travel/the_list.html', context_dict)

def add_couch(request):
  if request.method == "POST":
    contact_form, address_form = ContactForm(request.POST), AddressForm(request.POST)
    if contact_form.is_valid() and address_form.is_valid():
      contact = Contact.objects.get_or_create(phone=request.POST['phone'])
      address = Address(city=request.POST['city'], street=request.POST['street'], state=request.POST['state'])
      address.save()
      if contact[1] == False: 
        contact = contact[0]
      else:
        contact = contact[0]
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.address = address
        contact.save()
      couch = Couch()
      couch.address = address
      couch.contact =  contact
      couch.save()
      messages.add_message(request, messages.INFO, 'Thanks for the offer! We\'ll let you know if we\'re nearby.')
      return redirect('all_missions')
  else:
    mission_form, contact_form,address_form = MissionForm(), ContactForm(), AddressForm()
    context_dict = {'mission_form' : mission_form,'contact_form' : contact_form,'address_form' : address_form}
    return render(request, 'travel/new_couch.html', context_dict)





