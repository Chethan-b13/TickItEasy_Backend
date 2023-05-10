from django.contrib import admin
from .models import Event,Booking
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'image','organizer','mode','tickets_booked','price')
    list_editable  = ('tickets_booked','image','price','organizer','mode')
    list_filter = ('mode', 'genre')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Event,EventAdmin)
admin.site.register(Booking)