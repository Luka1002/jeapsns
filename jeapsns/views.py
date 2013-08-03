#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from jeapsns.models import sns
from jeapsns.forms import SnsForm
import datetime
import os

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext 
from django.contrib.auth.forms import *


def register(request):
	form = UserCreationForm()
	if request.method == 'GET':
		return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/hello")
		return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

def delete(request):
	if 'id' in request.GET:
		n = sns.objects.get(id=int(request.GET['id']))
		n.delete()
	return redirect('/hello')
		

def index_temp_file(request,id):
	id = int(id)
	if id == 0:
		l1 = sns.objects.all()
	else:
		l1 = sns.objects.filter(id=id)

        return render_to_response('index_temp_file.html',{'l1':l1})

from django.template import Template,Context

def index_temp(request,input_name):
	t = Template('My name is{{ name }}.')
	c = Context({'name':input_name})
	return HttpResponse(t.render(c))


def hello(request):
	if  request.method == 'POST':
		a = sns()
		for n in request.POST.keys():
			if hasattr(a,n):
				setattr(a,n,request.POST[n])
		#a = sns(**request.POST)
		print a.content
		a.save()
	f = SnsForm()
	l1 = sns.objects.all()
	#print a.save()
	return render_to_response('hello.html',{'l1':l1,'f':f},context_instance=RequestContext(request))

'''
def current_time(request,s):
	#s = datetime.date.today()
	#s = str(s)
	#s.split('-')
	#return HttpResponse(s)
'''
def current_time(request,p):

	s = datetime.date.today()
	if p == 'y':
	  s1 = s.year
	if p == 'm':
	  s1 = s.month
	if p == 'd':
	  s1 = s.day
	return HttpResponse(s1)

def system_info(request,q):
	if q == 'c':
		s1 = os.getcwd()
	return HttpResponse(s1)
		
