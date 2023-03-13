from django.db import models
from Auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField(default=1)
    tickets_booked = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_tickets = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} booked {self.num_tickets} tickets for {self.event.name}"