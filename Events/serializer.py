from rest_framework import serializers
from .models import Event, Booking

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {'organizer': {'required': False}}


class BookingTicketSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name')
    start_time = serializers.CharField(source='event.start_time')
    mode = serializers.CharField(source='event.mode')
    venue = serializers.CharField(source='event.venue')

    class Meta:
        model = Booking
        fields = '__all__'
        extra_fields = ['event_name', 'start_time', 'mode', 'venue']
        extra_kwargs = {'user': {'required': False}}