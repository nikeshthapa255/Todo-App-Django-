from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Jobs

# Create your views here.

def show(request):
	return HttpResponse('<bold>TODO APP</bold><a href="/">home</a>')
	#return render(request,'todo/home.html')

def addjobs(request):
	new_job=Jobs(name=request.POST['name'],description=request.POST['description'])
	new_job.save()
	return HttpResponseRedirect('/')

def default1(request):
	return render(request,'todo/home.html',
		{'job':Jobs.objects.all()})

def deletejob(request,jobid):
	new_job=Jobs.objects.get(id=jobid)
	new_job.delete()
	return HttpResponseRedirect('/')