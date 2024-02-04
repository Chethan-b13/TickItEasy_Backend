from django.utils.text import slugify
from rest_framework import generics,permissions
from .models import Event, Booking
from Auth.models import User
from .serializer import EventSerializer,BookingTicketSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


@swagger_auto_schema(request_body=EventSerializer)
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
        name = self.request.data.get('name')
        slug = slugify(name)
        serializer.save(organizer=self.request.user,slug=slug)


@swagger_auto_schema(request_body=EventSerializer)
class EventDetails(generics.RetrieveAPIView):
    lookup_field='slug'
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


########### Permission #################
class IsCustomerUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.role == "Customer"

@swagger_auto_schema(request_body=BookingTicketSerializer)
class BookTickets(generics.ListCreateAPIView):
    serializer_class = BookingTicketSerializer
    permission_classes = [permissions.IsAuthenticated,IsCustomerUser]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        ticket = serializer.save(user=self.request.user)
        event = ticket.event
        event.increase_tickets_booked(ticket.num_tickets)
