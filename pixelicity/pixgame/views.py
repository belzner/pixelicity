from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pixgame.models import Locations, UserLocs

# Create your views here.
def index(request):
	name = ""
	locations = []
	allLocs = []
	if request.user.is_authenticated():
		name = request.user.first_name
		userLoc = UserLocs.objects.get(user=request.user)
		locations = userLoc.locations.all()
		allLocs = Locations.objects.all()
	return render(request, 'index.html', {'name': name, 'locations': locations, 'allLocs': allLocs})

def about(request):
	name = ""
	if request.user.is_authenticated():
		name = request.user.first_name
	return render(request, 'about.html', {'name': name})

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