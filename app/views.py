from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def fun(request):
	data = student.objects.all().values()#query set
	context = {'data':data} 
	return render( request,'home.html',context)
