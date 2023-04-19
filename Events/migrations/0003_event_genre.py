# Generated by Django 4.1.7 on 2023-04-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='genre',
            field=models.CharField(choices=[('Event', 'Event'), ('Comedy', 'Comedy'), ('CollegeEvent', 'CollegeEvent'), ('WorkShops', 'WorkShops'), ('Webinar', 'Webinar'), ('theater&art', 'theater&art')], default='Event', max_length=15),
        ),
    ]
