# Create your views here.
from django.shortcuts import render_to_response
from cs499.cs499_app.models import LoginUsers
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def login_users(request):
    state = "Please log in below..."
    username = password = ''
    direct = 'auth.html'

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = LoginUsers.objects.get(username=username)            
            if user.password == password:         
                    state = "You're successfully logged in!"
                    direct = 'files.html'
            else:
                state = "Incorrect password!"
                direct = 'auth.html'
        except LoginUsers.DoesNotExist:
            direct = 'auth.html'   
            state = "Incorrect username!" 
    else:
        direct = 'auth.html'   
        state = "Enter you information below"         

    return render_to_response(direct,{'state':state, 'username': username})    