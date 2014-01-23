from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pixgame.models import Locations, UserLocs, UserAchieve, Achievement
from pixgame.achieve import checkAchieve

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
		a = Achievement.objects.get(compName='getstart')
		req = numResi >= 1
		newAch.append(checkAchieve(a, req, request.user))
		a = Achievement.objects.get(compName='firstfood')
		req = numRest >= 1
		newAch.append(checkAchieve(a, req, request.user))
		a = Achievement.objects.get(compName='hundredfood')
		req = numRest >= 100
		newAch.append(checkAchieve(a, req, request.user))
		userAch = UserAchieve.objects.get(user=request.user)
		if True in newAch:
			new = True
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
	results = {'success': False, 'id': 0}
	if request.user.is_authenticated():
		if request.method == u'GET':
			GET = request.GET
			if GET.has_key(u'li'):
				li = int(GET[u'li'])
				loc = Locations.objects.get(locId=li)
				ul = UserLocs.objects.get(user=request.user)
				ul.locations.add(loc)
				ul.save()
				results = {'success': True, 'id': li}
	json = simplejson.dumps(results)
	return HttpResponse(json, mimetype='application/json')

def addhome(request):
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
				results = {'success': True}
	json = simplejson.dumps(results)
	return HttpResponse(json, mimetype='application/json')