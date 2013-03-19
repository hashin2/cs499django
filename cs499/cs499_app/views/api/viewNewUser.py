# Create your views here.
from django.shortcuts import render_to_response
from cs499.cs499_app.models import LoginUsers
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def new_users(request):
    state = "Fill out the information below..." 
    
    if request.POST:
    	username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = LoginUsers.objects.get(username=username) 
            state = "username unavailable. Please choose a different username"           
            direct = "newuser.html"
        except LoginUsers.DoesNotExist:
        	user = LoginUsers(username=username,password=password)
        	user.save()
        	state = "You successfully made an account! You may now login"
        	direct = "auth.html"
    else:
    	state = "Fill out the form below..."
    	direct = "newuser.html"

    return render_to_response(direct,{'state':state})