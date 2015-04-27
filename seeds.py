import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generique_project.settings')

import django
django.setup()


from travel.models import Mission, Contact, Address
from faker import Faker
fake = Faker()

def seed():
  address = Address(city='Brooklyn', street='778 Lincoln Place', state='NY', zip=11216)
  address.save()

  kenneth = Contact(name='kenneth mendonca', email='mendonca.kr@Gmail.com', phone=9099640670, address=address)
  kenneth.save()

  for num in range(0,100):
    mission =  Mission(description=fake.sentence(),
                      anything_else=fake.sentence(),
                      address = address,
                      contact = kenneth
                      )
    mission.save()

if __name__ == '__main__':
  print("Seeding Travel database....")
  seed()