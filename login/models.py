from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class UserComplaint(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    complaint = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Null")
    Mobile_number = models.IntegerField(max_length=10)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location
