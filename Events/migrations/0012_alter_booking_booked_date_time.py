# Generated by Django 4.2.9 on 2024-02-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_alter_booking_booked_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_date_time',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]