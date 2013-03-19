from cs499.cs499_app.models import MotionEvent
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from helpers import rest_mux, jsonify, dejsonify

@csrf_exempt
def hello_world(request):
    return rest_mux(
        request,
        {
            'GET': __hello_world,            
        })

def __hello_world(request, query_params=None, **kwargs):
	events = MotionEvent.objects.all()
	retVal = {
		'events': [e.to_dict() for e in events]	
	};

	return HttpResponse(jsonify(retVal, query_params), mimetype="application/json")