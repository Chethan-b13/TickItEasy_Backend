from django.shortcuts import get_object_or_404 

from rest_framework import generics,permissions,response
from .models import Event
from .serializer import EventSerializer
# Create your views here.
class CreateEvent(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-tickets_booked')
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)



class EventDetails(generics.RetrieveAPIView):
    lookup_field='slug'
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
