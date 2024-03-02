from django.utils.text import slugify
from rest_framework import generics,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Booking
from Auth.models import User
from .serializer import EventSerializer,BookingTicketSerializer,HomeDataSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


@swagger_auto_schema(request_body=EventSerializer)
class CreateEvent(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

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


@swagger_auto_schema(request_body=HomeDataSerializer)
class EventDetails(generics.RetrieveAPIView):
    lookup_field='slug'
    queryset = Event.objects.all()
    serializer_class = HomeDataSerializer
    permission_classes = [permissions.IsAuthenticated]


@swagger_auto_schema(request_body=EventSerializer)
class AllEvents(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class HomePageData(APIView):
    def get(self, request, *args, **kwargs):
        try:
            carousel_data = Event.objects.all().order_by('-tickets_booked')[:5]
            top_events = Event.objects.all().order_by('-tickets_booked')[5:10]

            carousel_serializer = HomeDataSerializer(carousel_data, many=True)
            top_events_serializer = HomeDataSerializer(top_events, many=True)

            response_data = {
                "carousel_data": carousel_serializer.data,
                "top_events": top_events_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
