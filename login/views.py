from __future__ import unicode_literals
from .form import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import UserProfilename, Message
from datetime import datetime
import csv

#home page of the website
def index_view(request):
        return render(request, "login/index.html", {})

#login page 
def login_view(request):
    print "inside login view"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print username, password, "username and password"
        user = authenticate(username=username, password=password)
        form = User(request.POST)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                return render(request, 'login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/login.html', {'error_message': 'Enter correct username or password'})
    return render(request, "login/login.html", {})

#registration page
@csrf_exempt
def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data.get('email')
        usern = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        authenticate(username=user.username, password=password)
        user.is_active = False
        user.save()
        return render(request, "login/index.html", {"title": title, "username": usern})

    context = {
        "form": form,
        "title": title
    }
    return render(request, "login/registration.html", context)

#logout user from his profile to the homePage
def logout_view(request):
    logout(request)
    return render(request, "login/index.html", {})


#profile page for the users
def profile_view(request):
   

    return render(request, 'login/profile.html', {})

#upload csv and read in construction
# def upload_csv(request):
#     print "xcvxcvxcvxcvxvxv"

#     if request.POST and request.FILES:
#         print "sdffffffffffffffffffffffffffffffffffff"
#         csvfile = request.FILES['csv_file']
#         dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
#         csvfile.open()
#         reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
#         print reader
#         return render(request, 'login/profile.html', {'profile': reader})
