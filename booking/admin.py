from django.contrib import admin
from booking.models import Booking, Seat, Train, TrainSchedule

admin.site.register(Train)
admin.site.register(TrainSchedule)
admin.site.register(Booking)
admin.site.register(Seat)
