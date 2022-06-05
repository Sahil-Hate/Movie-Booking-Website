from django.contrib import admin
from .models import Movie,MovieCast,Screen,Seat
from movie.models import Booking
# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieCast)
admin.site.register(Screen)
admin.site.register(Seat)
admin.site.register(Booking)