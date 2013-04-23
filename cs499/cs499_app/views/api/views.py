# Create your views here.
from django.shortcuts import render_to_response
from cs499.cs499_app.models import Session, Device, MotionEvent
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from helpers import rest_mux, jsonify, dejsonify


#Login user and if valid allow them to view their sessions
def login_view(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)        
        if user is not None:
            if user.is_active:
                login(request,user)
                return  HttpResponseRedirect('session')
            else:
                return render_to_response('register.html',c)
        else:
            return render_to_response('login.html',c)
    else:
        return render_to_response('login.html',c)


#Logout user when they are finished viewing their sessions
def logout_view(request):
    logout(request)
    return render_to_response('logout.html')


#Creates new account for user when they register
def register(request):
    c = {}
    c.update(csrf(request))

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('last_name')
        user = authenticate(username=username, password=password)
        if user is None:
            u = User(username=username)
            u.set_password(password)
            u.save()   
            return HttpResponseRedirect('/login/')
        else:
            print("Invalid infomation entered") 
            return render_to_response('register.html',c) 
    else:       
        return render_to_response('register.html',c)   


#Allows users to add additional apps to the account
def manageAccount(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        password = request.POST.get('password')
        return render_to_response('account',c)             
    else:       
        return render_to_response('account',c)          	  


#Gets the session ID for the session requested by the user
@login_required
def session_view(request): 
    if not request.user.is_authenticated():
        return render(request,'login.html')         
    else:          
        events = Session.objects.all().filter(user=request.user.id)
        idNum = Session.objects.values('id')        
        return render_to_response('session.html', {'data':events, 'id':idNum, 'user':request.user})   


#Displays motion events for the requests session
@login_required
def display_session(request, offset, query_params=None):
    try:
        offset = int(offset)        
    except ValueError:
        raise Http404() 

    s = Session.objects.all().filter(id=offset)   
    events = MotionEvent.objects.all().filter(sessionId=s)
    sz = len(events)
    for i in range(0,sz):
        retVal = {
            'events': [e.to_dict() for e in events] 
        };
    return HttpResponse(retVal)
    # return HttpResponse(jsonify(retVal, query_params), mimetype="application/json")