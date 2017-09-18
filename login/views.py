from __future__ import unicode_literals
from .form import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import UserComplaint
import datetime, json
import googlemaps
import csv
#key to access google api
api_key = "AIzaSyBb3ERZRNTtb-Rp0FpWsTu7VQmU6OjD5lM"
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
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "lllllllllllllllllllllllllllllllllllllllllllll"
        print "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", varr
        
        data_update = UserComplaint(user=request.user, complaint=varr["complaint"], location=varr["location"], Mobile_number=varr["mobile_number"], pub_date=date_time )
        data_update.save()
        message= "complain has been submitted"
        return render(request, 'login/profile.html', {'msg':message})

    return render(request, 'login/profile.html', {})


def display_location(request):
    print "inside"
    data = UserComplaint.objects.all()
    loc_list =[]
    details_list = []
    for i in data:
        print i.user
        # print i.location
    # print loc_list
    
        gmaps = googlemaps.Client(key=api_key)
        address = i.location
        lat_lng = gmaps.geocode(address)
        # print lat_lng
        loc_list.append([i.location,lat_lng[0]['geometry']['location']['lat'], lat_lng[0]['geometry']['location']['lng']
        ])
        details_list.append([i.Mobile_number, i.complaint, str(i.pub_date)])
    # print loc_list
    print details_list

    test = loc_list

    return render_to_response('login/location.html', {"test":json.dumps(test),"listt":json.dumps(details_list) } )