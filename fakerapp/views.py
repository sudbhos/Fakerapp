from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'testapp/home.html')
def punejob(request):
    obj1=Punejob.objects.all()
    my_dict={"obj1":obj1}
    return render(request,'testapp/pune.html',context=my_dict)
def nagpurjob(request):
    obj=Nagpurjob.objects.all()
    my_dict2={"obj":obj}
    return render(request,'testapp/nagpur.html',context=my_dict2)
def mumbaijob(request):
    obj2=Mumbai.objects.all()
    omy_dict3={"obj2":obj2}
    return render(request,'testapp/mumbai.html',context=omy_dict3)
def hydrabadjob(request):
    ob=Hydrabad.objects.all()
    my_d={"ob":ob}
    return render(request,'testapp/hydrabad.html',context=my_d)