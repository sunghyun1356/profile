from django.urls import path
from . import views

urlpatterns =[

    path('', views.homepage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
    path('resume', views.resume, name='resume'),
    path('contactor', views.contactor, name='contactor'),


]