from django.utils.timezone import now
from django.db import models
from Auth.models import User
import uuid


GENRE_OPTIONS = (
    ('Event','Event'),
    ('Comedy','Comedy'),
    ('CollegeEvent','CollegeEvent'),
    ('WorkShop','WorkShop'),
    ('Webinar','Webinar'),
    ('theater&art','theater&art')
)

MODE_CHOICES = (
    ('Online','Online'),
    ('Offline','Offline')
)

TICKETSTATUS_CHOICES = [('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')]

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    mode = models.CharField(choices=MODE_CHOICES,default='Offline',max_length=8)
    image = models.CharField(max_length=250,blank=True)
    venue = models.CharField(max_length=200)
    genre = models.CharField(choices=GENRE_OPTIONS,default='Event',max_length=25)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField(default=1)
    tickets_booked = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default='',null=False)
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def increase_tickets_booked(self, num_tickets):
        if not self.sold_out:
            self.tickets_booked += num_tickets
            if self.tickets_booked >= self.number_of_seats:
                self.sold_out = True
            self.save()

    def save(self,*args, **kwargs):
        if self.tickets_booked >= self.number_of_seats:
            self.sold_out = True
        name = self.name.replace(" ","-")
        self.slug = f"{str(self.genre)}-{name}"
        return super().save(*args, **kwargs)

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_tickets = models.PositiveIntegerField(default=1)
    booked_date_time = models.CharField(max_length=20,default="",blank=True)
    status = models.CharField(max_length=20, choices=TICKETSTATUS_CHOICES, default='Confirmed')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0,blank=True)
    booking_reference_code = models.CharField(max_length=20, unique=True, editable=False,blank=True)

    def __str__(self):
        return f"{self.user.username} booked {str(self.num_tickets)} tickets for {self.event.name}"
    
    def calculate_total_price(self):
        total_price = self.num_tickets * self.event.price
        return total_price

    def generate_booking_reference_code(self):
        reference_code = str(uuid.uuid4())[:16].upper()
        return reference_code
    
    def save(self,*args, **kwargs):
        self.total_price = self.calculate_total_price()
        self.booking_reference_code = self.generate_booking_reference_code()
        return super().save(*args, **kwargs)