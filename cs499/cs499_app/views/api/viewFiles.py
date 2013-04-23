# # Create your views here.
# from django.shortcuts import render_to_response
# from cs499.cs499_app.models import UserFiles, LoginUsers
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# # import MySQLdb

# from helpers import rest_mux, jsonify, dejsonify

# @csrf_exempt
# def user_files(request):
#     return rest_mux(
#         request,
#         {
#             'GET': __user_files,            
#         })

# def __user_files(request, query_params=None, **kwargs):
# 	# events = MotionEvent.objects.all()
# 	events = UserFiles.objects.all()
# 	# retVal = {
# 	# 	'Files': [e.to_dict() for e in events],		

# 	# };
# 	results = []
# 	for e in events:
# 		results.append(e.to_dict())



# 	# filename = jsonify(retVal, query_params)
# 	# files = "<tr><td><b> %s </b></td><td>" %filename
# 	# return HttpResponse(jsonify(retVal, query_params), mimetype="application/json")
# 	# return render_to_response('files.html', jsonify(retVal, query_params)) 	
	
# 	# from django.template import Context, Template
# 	# f = Template("File: {{html}}")
# 	# c = Context({"html": files})
# 	# f.render(jsonify(retVal, query_params));

# 	# return render_to_response('files.html',{'data' :retVal.iteritems()})
# 	return render_to_response('files.html',{'data' :results})

# def viewSessions(request, query_params=None, **kwargs):
# 	events = MotionEvent.objects.all()
# 	retVal = {
# 		'events': [e.to_dict() for e in events]	
# 	};

