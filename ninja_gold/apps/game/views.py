# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from random import *
from time import localtime, strftime

# Create your views here.
def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
	if not 'log' in request.session:
		request.session['log'] = []
	return render(request, 'game/index.html')

def process(request):
	if request.POST['findGold'] == 'farm':
		gains = randint(10,20)
		request.session['gold'] += gains #randint inclusive both numbers
		request.session['log'].append("Earned " + str(gains) + " golds from the farm! " + "(" + strftime('%Y/%m/%d %I:%M %p', localtime()) + ")")
	elif request.POST['findGold'] == "cave":
		gains = randint(5,10)
		request.session['gold'] += gains
		request.session['log'].append("Earned " + str(gains) + " golds from the cave! " + "(" + strftime('%Y/%m/%d %I:%M %p', localtime()) + ")")
	elif request.POST['findGold'] == "house":
		gains = randint(2,5)
		request.session['gold'] += gains
		request.session['log'].append("Earned " + str(gains) + " golds from the house! " + "(" + strftime('%Y/%m/%d %I:%M %p', localtime()) + ")")
	elif request.POST['findGold'] == "casino":
		gains = randint(-50,50)
		request.session['gold'] += gains
		if gains >= 0:
			request.session['log'].append("Earned " + str(gains) + " golds from the casino! " + "(" + strftime('%Y/%m/%d %I:%M %p', localtime()) + ")")
		else:
			request.session['log'].append("Entered a casino and lost " + str(abs(gains)) + " golds... Ouch... " + "(" + strftime('%Y/%m/%d %I:%M %p', localtime()) + ")")

	if request.session['gold'] < 0:
		request.session['gold'] = 0
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')