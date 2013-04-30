# Create your views here.
from django.shortcuts import render_to_response
from cs499.cs499_app.models import Session, Device, MotionEvent, App 
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from helpers import rest_mux, jsonify, dejsonify


#********* Purpose *********#
# This file contains the functions for handling the logging in, 
# logging out, viewing sessions, viewing individual session data,
# viewing heatmap view of a session, adding a device or app and
# deleting a session


# Login user and if valid allow them to view their sessions.
# Uses the built in Django User class to authenticate a users account
def login_view(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check that the user entered correct username 
        # and password and has a valid account
        user = authenticate(username=username, password=password)        
        # if user is valid then log them in
        if user is not None:
            if user.is_active:
                login(request,user)
                return  HttpResponseRedirect('session')
            else:
                return render_to_response('register.html',c)
        # if user is not valid
        else:
            return render_to_response('login.html',c)
    # GET request to get to the login page
    else:
        return render_to_response('login.html',c)


# Logout user when they are finished viewing their sessions
# using built in functions of the Django User class
def logout_view(request):
    logout(request)
    return render_to_response('logout.html')


# Creates new account for user when they register
def register(request):
    c = {}
    c.update(csrf(request))
    # POST request called when 'register account' button pressed
    if request.POST:
        # get the information entered by the user
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('last_name')
        # check that the username and password entered  
        # does not already exist in  the database
        user = authenticate(username=username, password=password)
        # if username/password are available then add new user to database
        if user is None:
            u = User(username=username)
            u.set_password(password)
            u.save()   
            # redirect to the login page after successfully creating the users account
            return HttpResponseRedirect('/login/')
        # stay on register page if invalid data entered
        else:
            print("Invalid infomation entered") 
            return render_to_response('register.html',c) 
    # GET request to get to the register page
    else:       
        return render_to_response('register.html',c)   
  

# Gets the ID number for the session requested by the user
@login_required
def session_view(request): 
    # user must be logged in to view thier sessions
    if not request.user.is_authenticated():
        return render(request,'login.html')         
    else:    
        # get the users sessions 
        events = Session.objects.all().filter(user=request.user.id)
        # get the id numbers of the sessions
        idNum = Session.objects.values('id')        
        # return the sessions, id numbers, and user to display
        return render_to_response('session.html', {'data':events, 'id':idNum, 'user':request.user})   


# Displays motion events for the requested session.
# The displayed data can be saved by the user to replay in their app
@login_required
def display_session(request, offset, query_params=None):
    # get the id number of the session the user wants to view
    try:
        offset = int(offset)        
    except ValueError:
        raise Http404() 

    # retreived the session and all its motion events
    s = Session.objects.all().filter(id=offset)   
    events = MotionEvent.objects.all().filter(sessionId=s)
    retVal = {
        'Motion Events': [e.to_dict() for e in events] 
    }   
    return HttpResponse(jsonify(retVal, query_params), mimetype="application/json")


# Gets the motion events of the request session from 
# the database to display in the heatmap view
@login_required
def display_heatmap(request, offset, query_params=None):
    # the session id number chosen
    try:
        offset = int(offset)        
    except ValueError:
        raise Http404() 

    s = Session.objects.get(id=offset)    
    events = MotionEvent.objects.all().filter(sessionId=s)
    size = len(events)
    # formats the motion event data into a json object to use
    # to generate the heatmap display
    retVal = {
        'data': [d.to_heatmap() for d in events] 
    }   
    motion = jsonify(retVal, query_params)
      
    return render_to_response('heatmap.html',{'retVal':retVal, 'session':s, 'motion':motion, 'events':events, 'size':size})


# Allows users to add additional apps to the account manually through the website
@login_required
def manageApps(request):
    state="Enter the App name"
    c = {}
    c.update(csrf(request))
    if request.POST:
        # get the app name entered by the user
        appname = request.POST.get('appname')
        # add the app and the associated user to the database
        app = App(appname=appname, user=request.user)
        app.save()
        # displays so that the user knows the were successful in adding the app
        state = "App was successfully added"
        return render_to_response('app.html',{"state":state},context_instance=RequestContext(request))
    else:                
        return render_to_response('app.html',{"state":state},context_instance=RequestContext(request))        

#Allows user to add additional devices to their account
@login_required
def manageDevices(request):
    state= "Enter your device information."    
    c = {}
    c.update(csrf(request))
    if request.POST:
        # get the device info entered
        serial = request.POST.get('serial')
        version = request.POST.get('version')
        screenWidth = request.POST.get('screenWidth')
        screenHeight = request.POST.get('screenHeight')
        # add a deivce with the entered info to the database
        device = Device(serial=serial,version=version,screenWidth=screenWidth,screenHeight=screenHeight,user=request.user)
        device.save()
        #displays so the user knows the device successfully added
        state = "Device was successfully added"
        return render_to_response('device.html',{"state":state},context_instance=RequestContext(request))
    else:                
        return render_to_response('device.html',{"state":state},context_instance=RequestContext(request))

# displays the heatmap page
def heatmap_view(request):
    return render_to_response('heatmap.html')


#View the Apps currently in the system
@login_required
def viewapps(request): 
    if not request.user.is_authenticated():
        return render(request,'login.html')         
    else:                 
        apps = App.objects.all()      
        return render_to_response('viewapps.html', {'apps':apps, 'user':request.user})   

#View the Devices currently in the system
@login_required
def viewdevices(request): 
    if not request.user.is_authenticated():
        return render(request,'login.html')         
    else:                 
        devices = Device.objects.all()      
        return render_to_response('viewdevices.html', {'devices':devices, 'user':request.user})           

# Allows users to delete sessions they no longer want
@login_required
def delete_session(request, offset): 
    try:
        offset = int(offset)        
    except ValueError:
        raise Http404() 

    s = Session.objects.all().filter(id=offset)   
    s.delete()

    events = Session.objects.all().filter(user=request.user.id)
    idNum = Session.objects.values('id')        
    return render_to_response('session.html', {'data':events, 'id':idNum, 'user':request.user})         
