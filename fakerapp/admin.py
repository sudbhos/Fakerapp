from django.contrib import admin
from .models import Punejob,Nagpurjob,Mumbai,Hydrabad
# Register your models here.

class Puneadmin(admin.ModelAdmin):
    list_display = ["data","company","title","eligibility","address","email","phonenumber"]

class Nagpuradmin(admin.ModelAdmin):
    list_display = ["data","company","title","eligibility","address","email","phonenumber"]

class Mumbaiadmin(admin.ModelAdmin):
    list_display = ["data","company","title","eligibility","address","email","phonenumber"]

class Hydrabadadmin(admin.ModelAdmin):
    list_display = ["data","company","title","eligibility","address","email","phonenumber"]

admin.site.register(Punejob,Puneadmin)

admin.site.register(Mumbai,Mumbaiadmin)

admin.site.register(Nagpurjob,Nagpuradmin)

admin.site.register(Hydrabad,Hydrabadadmin)