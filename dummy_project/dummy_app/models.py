from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Trying to write API for react native frontend


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    photo = models.ImageField(upload_to="food/photos/", null=True, blank=True)
    menu = models.TextField()
    tags = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    # writer = models.ForeignKey(User)

    def __str__(self):
        return self.name


# # geolocation and year need to be done later on
# class NasaData(models.Model):
#     name = models.CharField(max_length=20)
#     id = models.IntegerField()
#     nametype = models.CharField(max_length=10)
#     recclass = models.CharField(max_length=10)
#     mass = models.IntegerField()
#     fall = models.CharField(max_length=10)
#     reclat = models.FloatField()
#     reclong = models.FloatField()
