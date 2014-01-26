#from django.utils import simplejson
import json
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pixgame.models import Locations, UserLocs, UserAchieve, Achievement
from pixgame.achieve import checkAch, parseAch, collectAch

# Create your views here.
def index(request):
	name = ""
	locations = []
	allLocs = []
	achievements = []
	allAch = []
	stats = []
	new = False
	if request.user.is_authenticated():
		name = request.user.first_name
		userLoc = UserLocs.objects.get(user=request.user)
		locations = userLoc.locations.all()
		allLocs = Locations.objects.all().exclude(locType="residential")
		newAch = []
		numResi = len(userLoc.locations.filter(locType="residential"))
		numRest = len(userLoc.locations.filter(locType="restaurant"))
		newAch = collectAch(request.user, userLoc)
		if newAch:
			new = True
		userAch = UserAchieve.objects.get(user=request.user)
		achievements = userAch.achievements.all()
		allAch = Achievement.objects.all()
		stats = [len(locations), numResi, numRest, len(achievements), request.user.date_joined]
	return render(request, 'index.html', {'name': name, 'locations': locations, 'allLocs': allLocs, 'achievements': achievements, 'new': new, 'allAch': allAch, 'stats': stats})

def about(request):
	name = ""
	if request.user.is_authenticated():
		name = request.user.first_name
	return render(request, 'about.html', {'name': name})

def help(request):
	name = ""
	if request.user.is_authenticated():
		name = request.user.first_name
	return render(request, 'help.html', {'name': name})

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
				results = {'success': True, 'id': li, 'newAch': newAch, 'numAch': numAch, 'numResi': numResi, 'numRest': numRest}
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