# Generated by Django 4.2.9 on 2024-02-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0012_alter_booking_booked_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_reference_code',
            field=models.CharField(blank=True, editable=False, max_length=20, unique=True),
        ),
    ]
