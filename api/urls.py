from django.urls import path
from api.views import *

urlpatterns = [
    path('register-time-slot', RegisterTimeSlot.as_view(), name='register-time-slot'),
    path('get-time-slot', GetTimeSlots.as_view(), name='get-time-slot'),
]