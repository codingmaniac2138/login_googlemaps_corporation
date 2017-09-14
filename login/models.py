from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfilename(models.Model):
    name = models.OneToOneField(User, primary_key=True)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=20)
    skill = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Message(models.Model):
    user = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.user
