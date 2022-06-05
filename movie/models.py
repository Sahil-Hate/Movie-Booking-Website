from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    release_date = models.DateField()
    category = models.CharField(max_length=5)
    rating = models.FloatField()
    genre = models.CharField(max_length=255)
    duration = models.CharField(max_length=10)
    synopsis = models.TextField()
    image = models.ImageField()
    url = models.URLField()
    background_image = models.ImageField()
    show_time = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    


class MovieCast(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return str(self.movie) + " - " + self.name

class Screen(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return "Screen " + str(self.number)   

class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    seat_identity = models.CharField(max_length=5)

    def __str__(self):
        return str(self.screen) + " - " + self.seat_identity 


class Booking(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.customer) + " - " + str(self.seat) + " - " + str(self.movie)
