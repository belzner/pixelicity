from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pixgame.models import Locations, UserLocs

# Create your views here.
def index(request):
	name = ""
	locations = []
	if request.user.is_authenticated():
		name = request.user.first_name
		userLoc = UserLocs.objects.get(user=request.user)
		locations = userLoc.locations.all()
	return render(request, 'index.html', {'name': name, 'locations': locations})

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
	return redirect('index')

def userlogout(request):
	logout(request)
	return redirect('index')

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