from django.views.decorators.csrf import csrf_exempt
from cs499.cs499_app.models import Session, Device, MotionEvent
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from helpers import rest_mux, jsonify, dejsonify


@csrf_exempt
def hello_world(request):
    return rest_mux(
        request,
        {
            'GET': __hello_world, 
            'POST': __create__,           
        })

def __hello_world(request, query_params=None, **kwargs):
	# events = MotionEvent.objects.all()
	events = UserFiles.objects.all()
	retVal = {
		'events': [e.to_dict() for e in events]	
	};
	return HttpResponse(retVal)
	# return HttpResponse(jsonify(retVal, query_params), mimetype="application/json")

def __create__(request, query_params, **kwargs):	
	s = request.raw_post_data
	ds = dejsonify(s)
	username = ds['username']
	password = ds['password']
	user = authenticate(username=username, password=password)
	
	if user is not None:	
	    session = Session(user=user)
	    session.save()
	    arraySize = len(ds['Motion Events'])	
	    motion = ds['Motion Events']
	    t = 0
	    for i in range(0,arraySize):	   	        
	        MotionEvent(action=motion[i]['action'], deviceId=motion[i]['deviceId'], downTime=motion[i]['downTime'], edgeFlags=motion[i]['edgeFlags'], eventTime=motion[i]['eventTime'], metaState=motion[i]['metaState'], pressure=motion[i]['pressure'],size=motion[i]['size'],x=motion[i]['x'], xPrecision=motion[i]['xPrecision'], y=motion[i]['y'],yPrecision=motion[i]['yPrecision'],sessionId=session).save()            
	    return HttpResponse(t)
	else:
	    return HttpResponse(t)
											
