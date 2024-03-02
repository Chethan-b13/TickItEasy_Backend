from rest_framework import serializers
from .models import Event, Booking

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {'organizer': {'required': False}}


class HomeDataSerializer(serializers.ModelSerializer):
    class Meta:
            model = Event
            fields = [
                "id",
                "name",
                "description",
                "start_time",
                "end_time",
                "mode",
                "image",
                "venue",
                "genre",
                "number_of_seats",
                "price",
                "slug",
            ]

class BookingTicketSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name', required=False)
    start_time = serializers.CharField(source='event.start_time', required=False)
    mode = serializers.CharField(source='event.mode', required=False)
    venue = serializers.CharField(source='event.venue', required=False)

    class Meta:
        model = Booking
        fields = '__all__'
        extra_fields = ['event_name', 'start_time', 'mode', 'venue']
        extra_kwargs = {'user': {'required': False}}