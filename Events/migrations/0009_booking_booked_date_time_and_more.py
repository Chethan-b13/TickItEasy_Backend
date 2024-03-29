# Generated by Django 4.2.9 on 2024-02-04 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0008_alter_event_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_reference_code',
            field=models.CharField(blank=True, editable=False, max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Confirmed', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
