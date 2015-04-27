from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from travel.models import Mission, Contact, Address
from travel.forms import MissionForm, ContactForm, AddressForm

# Create your views here.
def index(request):
  return render(request, 'travel/index.html')

def add_mission(request):
  if request.method == 'POST':
    mission_form, contact_form, address_form = MissionForm(request.POST), ContactForm(request.POST), AddressForm(request.POST)
    if mission_form.is_valid() and contact_form.is_valid() and address_form.is_valid():
      mission = Mission(description=request.POST['description'], anything_else=request.POST['anything_else'])
      contact = Contact.objects.get_or_create(phone=request.POST['phone'], address=None)
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
      mission.save()
    else:
      # Let's render form errors to bootstrap
      print(mission_form.errors)
      print(contact_form.errors)
      return HttpResponse('Form Errors!!')
  else:
    mission_form, contact_form,address_form = MissionForm(), ContactForm(), AddressForm()
    context_dict = {'mission_form' : mission_form,
                    'contact_form' : contact_form,
                    'address_form' : address_form}
    return render(request, 'travel/register.html', context_dict)
  return redirect('home')

def all_missions(request):
  context_dict = {}
  context_dict['missions'] = Mission.objects.all()
  return render(request, 'travel/the_list.html', context_dict)