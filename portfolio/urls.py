
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',portfolio,name='Home'),
    path('contact/',Contacts,name='contact')
]