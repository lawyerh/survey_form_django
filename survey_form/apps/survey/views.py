# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html')

def results(request):
	return render(request, 'results.html')

def process(request):
	try:
		request.session['count'] += 1
	except: 
		request.session['count'] = 0

	request.session['name'] = request.POST['name']
	request.session['favorite_city'] = request.POST['favorite_city']
	request.session['fav_language'] = request.POST['fav_language']
	request.session['comments'] = request.POST['comments']
	return redirect('/results')
def goback(request):
	return redirect('/')