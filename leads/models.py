from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Lead(models.Model):

    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    #agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)
    #agent = models.ForeignKey("Agent", on_delete=models.SET_DEFAULT, default=None)

    #phoned = models.BooleanField(default=false)
    #source = models.CharField(choices=SOURCE_CHOICES, max_length=200)
    #profile_picture = models.ImageField(blank=True null=True)
    #special_files = model.FileField(blank=True null=True)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
