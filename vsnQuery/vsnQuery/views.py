from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from importVsns.models import VSNData

def index(request):
     template = loader.get_template('vsnQuery/index.html')
     context=0
     return HttpResponse(template.render(context))
	
