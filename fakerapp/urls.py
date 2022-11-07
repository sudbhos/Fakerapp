
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage,name="home"),
    path('punejob', views.punejob,name="punejob"),
    path('mumbaijob', views.mumbaijob,name="mumbaijob"),
    path('nagpurjob', views.nagpurjob,name="nagpurjob"),
    path('hydrabadjob', views.hydrabadjob,name="hydrabadjob"),

]
