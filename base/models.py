from django.db import models
from django.contrib.auth.models import User

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    watchlist = models.ForeignKey(Watchlist, related_name='movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.title

