from django.db import models
from Auth.models import User


GENRE_OPTIONS = (
    ('Event','Event'),
    ('Comedy','Comedy'),
    ('CollegeEvent','CollegeEvent'),
    ('WorkShop','WorkShop'),
    ('Webinar','Webinar'),
    ('theater&art','theater&art')
)

MODe_CHOICES = (
    ('Online','Online'),
    ('Offline','Offline')
)

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    mode = models.CharField(choices=MODe_CHOICES,default='Offline',max_length=8)
    image = models.CharField(max_length=250,blank=True)
    venue = models.CharField(max_length=200)
    genre = models.CharField(choices=GENRE_OPTIONS,default='Event',max_length=15)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField(default=1)
    tickets_booked = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default='',null=False)

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_tickets = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} booked {self.num_tickets} tickets for {self.event.name}"