from django.urls import path
from .views import CreateEvent,EventDetails,BookTickets, HomePageData



urlpatterns = [
   path('',CreateEvent.as_view(),name='event-list-create'),
   path('home-page-data',HomePageData.as_view(),name='event-homepage'),
   path('',CreateEvent.as_view(),name='event-list-create'),
   path('book-ticket',BookTickets.as_view(),name='ticket-booking'),
   path('<slug:slug>/',EventDetails.as_view(),name='event-details')
]