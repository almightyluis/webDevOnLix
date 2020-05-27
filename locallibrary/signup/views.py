from django.shortcuts import render
from django.http import HttpResponse


import datetime

# To return a render of a template To-Do
#1 .Render template first


#def current_datetime(request):
#    now = datetime.datetime.now()
#   html = "<html><body>It is now %s.</body></html>" % now
#   return HttpResponse(html)


#def index(request):
#    return HttpResponse("Hello, world. You're at the signup index!")


#Create template Folder
# example.html 
	# def returnView(request){ return render( request, '')}


def create_view(request):
	return render(request, 'design.html')