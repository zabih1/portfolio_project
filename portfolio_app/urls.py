from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('send-message/', views.send_message, name='send_message'),
]