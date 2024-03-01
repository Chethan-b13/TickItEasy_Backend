import os
import django
from django.utils import timezone
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TickItEasy.settings')  # Replace 'your_project.settings' with your actual project's settings
django.setup()

from Events.models import Event  # Replace 'your_app' with the actual name of your Django app
from Auth.models import User
fake = Faker()

def create_fake_event(organizer):
    return Event.objects.create(
        name=fake.name(),
        description=fake.paragraphs(nb=3),
        start_time=timezone.make_aware(fake.future_datetime()),
        end_time=timezone.make_aware(fake.future_datetime()),
        mode=random.choice(['Offline', 'Online']),  # Assuming MODE_CHOICES contains 'Offline' and 'Online'
        image=f"https://picsum.photos/id/{fake.random_int(min=10, max=1000)}/450/300",
        venue=fake.country(),
        genre=random.choice(['Event', 'Concert', 'Conference']),  # Assuming GENRE_OPTIONS contains relevant genres
        organizer=random.choice(organizer),
        number_of_seats=fake.random_int(min=100, max=350),
        tickets_booked=fake.random_int(min=0, max=99),  # Adjust as needed
        price=fake.random_int(min=0, max=8000),  # Adjust as needed
    )

def populate_events(num_events=10):
    users = []
    for user in User.objects.all():
        users.append(user)

    for i in range(num_events):
        try:
            create_fake_event(users)
            print(i)
        except Exception as ex:
            print("error",ex,i)

if __name__ == "__main__":
    populate_events()
    print("Events populated successfully!")