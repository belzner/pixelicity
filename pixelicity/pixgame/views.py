from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	name = ""
	if request.user.is_authenticated():
		name = request.user.first_name
	return render(request, 'index.html', {'name': name})

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