from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
]