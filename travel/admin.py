from django.contrib import admin
from csv import writer
from django.http import HttpResponse
from travel.models import Mission, Couch, Contact, Address

admin.site.register(Mission)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Couch)



def couch_list(request):
  response = HttpResponse()
  response['Content-Disposition'] = 'attachment; filename="couches.csv"'
  couches = Couch.objects.all()
  output = writer(response)
  output.writerow(['Contact','Phone' 'Address'])
  for couch in couches:
    output.writerow([couch.contact, couch.contact.phone ,couch.address])
  return response

admin.site.register_view('couchlist', view=couch_list)
