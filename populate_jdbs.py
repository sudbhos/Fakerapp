import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakerproj.settings')
import django
django.setup()
from fakerapp.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=""+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdata=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager',"Team Lead","software developer"))
        feleigibility=fake.random_element(elements=("BE","MTECH","ME","BCA","MCA"))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()

        Hydrabad_job = Hydrabad.objects.get_or_create(data=fdata, company=fcompany, title=ftitle, eligibility=feleigibility,
                                                 address=faddress, email=femail, phonenumber=fphonenumber)

        Nagpur_job = Mumbai.objects.get_or_create(data=fdata, company=fcompany, title=ftitle, eligibility=feleigibility,
                                                 address=faddress, email=femail, phonenumber=fphonenumber)

        Mumbai_job = Nagpurjob.objects.get_or_create(data=fdata, company=fcompany, title=ftitle, eligibility=feleigibility,
                                                 address=faddress, email=femail, phonenumber=fphonenumber)

        pune_job=Punejob.objects.get_or_create(data=fdata,company=fcompany,title=ftitle,eligibility=feleigibility,address=faddress,email=femail,phonenumber=fphonenumber)
populate(30)