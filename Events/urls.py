from django.urls import path
from .views import CreateEvent,EventDetails



urlpatterns = [
   path('',CreateEvent.as_view(),name='event-list-create'),
   path('<slug:slug>/',EventDetails.as_view(),name='event-details')
]