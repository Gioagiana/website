
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home_success/', views.home_success, name='home_success'),


]