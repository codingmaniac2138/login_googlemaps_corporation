# -*- coding: utf-8 -*-
from .models import UserComplaint
from django.contrib import admin

class UserComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'complaint', 'location', 'Mobile_number', 'pub_date')

admin.site.register(UserComplaint, UserComplaintAdmin)