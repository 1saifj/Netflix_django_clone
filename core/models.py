from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)


MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=100)
    age_limit = models.CharField(max_length=10, choices = AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    created = models.DatetimeField(auto_now_add=True)
    discription = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    age_limit = models.CharField(max_length=10, choices = AGE_CHOICES)

class Video(models.Model): 
    title = models.CharField(max_length=225, null = True, blank = True)
    file = models.FileField(upload_to='movies/', blank=True, null=True)