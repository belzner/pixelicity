#from django.utils import simplejson
import json
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pixgame.models import Locations, UserLocs, UserAchieve, Achievement
from pixgame.achieve import checkAch, parseAch, collectAch

# Create your views here.
def index(request):
	name = ""
	un = ""
	locations = []
	allLocs = []
	achievements = []
	allAch = []
	stats = []
	new = False
	if request.user.is_authenticated():
		name = request.user.first_name
		un = request.user.username
		userLoc = UserLocs.objects.get(user=request.user)
		locations = userLoc.locations.all()
		allLocs = Locations.objects.all().exclude(locType="residential")
		newAch = []
		numResi = len(userLoc.locations.filter(locType="residential"))
		numRest = len(userLoc.locations.filter(locType="restaurant"))
		numShop = len(userLoc.locations.filter(locType="shopping"))
		newAch = collectAch(request.user, userLoc)
		if newAch:
			new = True
		userAch = UserAchieve.objects.get(user=request.user)
		achievements = userAch.achievements.all()
		allAch = Achievement.objects.all()
		stats = [len(locations), numResi, numRest, len(achievements), request.user.date_joined, numShop]
	return render(request, 'index.html', {'name': name, 'username': un, 'locations': locations, 'allLocs': allLocs, 'achievements': achievements, 'new': new, 'allAch': allAch, 'stats': stats})

def about(request):
	name = ""
	un = ""
	if request.user.is_authenticated():
		name = request.user.first_name
		un = request.user.username
	return render(request, 'about.html', {'name': name, 'username': un})

def help(request):
	name = ""
	un = ""
	if request.user.is_authenticated():
		name = request.user.first_name
		un = request.user.username
	return render(request, 'help.html', {'name': name, 'username': un})

def achievements(request):
	if request.user.is_authenticated():
		name = request.user.first_name
		un = request.user.username
		userAch = UserAchieve.objects.get(user=request.user)
		achievements = userAch.achievements.all()
		allAch = Achievement.objects.all()
		return render(request, 'achievements.html', {'name': name, 'username': un, 'achievements': achievements, 'allAch': allAch})
	else:
		return redirect('index')

def error(request):
	return redirect('index')

def userlogin(request):
	un = request.POST['username']
	pw = request.POST['password']
	user = authenticate(username=un, password=pw)
	if user is not None:
		if user.is_active:
			login(request, user)
	return redirect(request.META.get('HTTP_REFERER', 'index'))

def userlogout(request):
	logout(request)
	return redirect(request.META.get('HTTP_REFERER', 'index'))

def userreg(request):
	un = request.POST['username']
	pw = request.POST['password']
	em = request.POST['email']
	fn = request.POST['first']
	ln = request.POST['last']
	if un and pw and em:
		user = User.objects.create_user(un, em, pw)
		user.first_name = fn
		user.last_name = ln
		user.save()
		userLoc = UserLocs(user=user)
		userLoc.save()
		userAch = UserAchieve(user=user)
		userAch.save()
		user = authenticate(username=un, password=pw)
		if user is not None:
			if user.is_active:
				login(request, user)
		return redirect('index')
	else:
		if not un:
			messages.error(request, "Please enter a username.")
		if not pw:
			messages.error(request, "Please enter a password.")
		if not em:
			messages.error(request, "Please enter an email address.")
	return redirect(request.META.get('HTTP_REFERER', 'index'))


def addloc(request):
	ul = UserLocs.objects.get(user=request.user)
	numAch = len(UserAchieve.objects.get(user=request.user).achievements.all())
	numResi = len(ul.locations.filter(locType="residential"))
	numRest = len(ul.locations.filter(locType="restaurant"))
	results = {'success': False, 'id': 0, 'newAch': False, 'numAch': numAch, 'numResi': numResi, 'numRest': numRest}
	if request.user.is_authenticated():
		if request.method == u'GET':
			GET = request.GET
			if GET.has_key(u'li'):
				li = int(GET[u'li'])
				loc = Locations.objects.get(locId=li)
				ul.locations.add(loc)
				ul.save()
				newAch = collectAch(request.user, ul)
				numAch = len(UserAchieve.objects.get(user=request.user).achievements.all())
				numResi = len(ul.locations.filter(locType="residential"))
				numRest = len(ul.locations.filter(locType="restaurant"))
				numShop = len(ul.locations.filter(locType="shopping"))
				results = {'success': True, 'id': li, 'newAch': newAch, 'numAch': numAch, 'numResi': numResi, 'numRest': numRest, 'numShop': numShop}
	jsonRes = json.dumps(results)
	return HttpResponse(jsonRes, mimetype='application/json')

def addhome(request):
	#results = {'success': False, 'newAch': False}
	results = {'success': False}
	if request.user.is_authenticated():
		if request.method == u'GET':
			GET = request.GET
			if GET.has_key(u'lat') and GET.has_key(u'lng'):
				lat = GET[u'lat']
				lng = GET[u'lng']
				l = Locations(locId=1, locName=request.user.first_name+"'s Home", centerLat=lat, centerLng=lng, locType="residential", locImage="loc-res.png")
				l.save()
				ul = UserLocs.objects.get(user=request.user)
				ul.locations.add(l)
				ul.save()
				#newAch = collectAch(request.user, ul)
				#results = {'success': True, 'newAch': newAch}
				results = {'success': True}
	jsonRes = json.dumps(results)
	return HttpResponse(jsonRes, mimetype='application/json')