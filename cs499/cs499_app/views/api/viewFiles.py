# Create your views here.
from django.shortcuts import render_to_response
from cs499.cs499_app.models import UserFiles, LoginUsers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import MySQLdb

@csrf_exempt
def user_files(request):
    state = "User's files" 
    direct = "files.html"
	try:
		userfiles = UserFiles.objects.all().order_by('numFiles')
		filename = ','.join([f.filename for f in uesrfiles])
		
	except UserFiles.DoesNotExist:
		state = "You do not currently have any files"
		direct = "files.html"

	return render_to_response(direct,{'state':state, 'filename':userfiles})    