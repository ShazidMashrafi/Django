from django.db import models
from django.urls import reverse
# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First name",)
    last_name = models.CharField(max_length=50, verbose_name="Last name",)
    instrument = models.CharField(max_length=50, verbose_name="Instrument",)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('First_app:musician_details', kwargs={'pk':self.pk})

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_list')  # models.Cascade If an album is here it won't let that musician to be deleted
    name = models.CharField(max_length=100, verbose_name="Album name",)
    release_date = models.DateField()
    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Average"),
        (4, "Good"),
        (5, "Excellent")
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name + ", Rating: " + str(self.num_stars)