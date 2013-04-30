from django.views.decorators.csrf import csrf_exempt
from cs499.cs499_app.models import Session, Device, MotionEvent, App
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from helpers import rest_mux, jsonify, dejsonify

#********* Purpose *********#
# Handle the POST request sent from the andriod device
# when it runs the app. The user information is retrieved from the POST
# to validate their account, then the data is parsed through and stored 
# to the databse.


# Checks if the request is a GET or POST and
# redirects to the corresponding function
@csrf_exempt
def api_request(request):
    return rest_mux(
        request,
        {
            'GET': get_request, 
            'POST': post_request,           
        })

# This function handles a GET request. Nothing is  
# implemented for this request so it just returns
def get_request(request, query_params=None, **kwargs):
	# events = MotionEvent.objects.all()
	events = Session.objects.all()
	retVal = {
		'events': [e.to_dict() for e in events]	
	};
	return HttpResponse(retVal)	

# This function handles the POST request. It parses the
# data received and stores it to the database. Each touch 
# point is stored in the MotionEvent table. If the device or 
# app information received does not currently exist in the
# database then they will be created and added. Then a session
# is created using all this information.
def post_request(request, query_params, **kwargs):
	#gets the data from the POST	
	s = request.raw_post_data
	ds = dejsonify(s)
	username = ds['username']
	password = ds['password']
	# check the users information to make sure they have a valid account
	user = authenticate(username=username, password=password)
	
	if user is not None:	
	    d = ds['Serial']
	    a = ds['appname']
	    # check if the app is in the database and add it if it is not
	    try:
	    	device = Device.objects.get(serial=d)
	    except Device.DoesNotExist:
	    	device = Device(serial = ds['Serial'], screenWidth = ds['screen width'], screenHeight = ds['screen height'], version = ds['Version'], user = user)	
	    	device.save()
	    try:	
	    	app = App.objects.get(appname=a)
	    except App.DoesNotExist:
	    	app = App(appname = ds['appname'], user = user)
	    	app.save()
		# add a session with this information
	    session = Session(user=user,device=device,app=app)
	    session.save()
	    arraySize = len(ds['Motion Events'])	
	    # get the motion event array from the POST
	    motion = ds['Motion Events']	 
	    # for each index of the array add it as a motion event in the table  
	    for i in range(0,arraySize):	   	        
	        MotionEvent(action=motion[i]['action'], deviceId=motion[i]['deviceId'], downTime=motion[i]['downTime'], edgeFlags=motion[i]['edgeFlags'], eventTime=motion[i]['eventTime'], metaState=motion[i]['metaState'], pressure=motion[i]['pressure'],size=motion[i]['size'],x=motion[i]['x'], xPrecision=motion[i]['xPrecision'], y=motion[i]['y'],yPrecision=motion[i]['yPrecision'],sessionId=session).save()            
	    return HttpResponse('added data to DB')
	else:
	    return HttpResponse('invalid request')
											
