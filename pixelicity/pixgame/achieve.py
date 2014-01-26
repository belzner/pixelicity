from django.contrib.auth.models import User
from pixgame.models import UserAchieve, Achievement, UserLocs, Locations

def checkAch(a, req, user):
	ua = UserAchieve.objects.get(user=user)
	if req:
		if a not in ua.achievements.all():
			ua.achievements.add(a)
			return a.compName
	return None

def parseAch(a, req, user, new):
	ach = checkAch(a, req, user)
	if ach:
		new.append(ach)
	return new

def collectAch(user, userLoc):
	newAch = []
	numResi = len(userLoc.locations.filter(locType="residential"))
	numRest = len(userLoc.locations.filter(locType="restaurant"))

	a = Achievement.objects.get(compName='getstart')
	req = numResi >= 1
	newAch = parseAch(a, req, user, newAch)

	a = Achievement.objects.get(compName='firstfood')
	req = numRest >= 1
	newAch = parseAch(a, req, user, newAch)

	a = Achievement.objects.get(compName='hundredfood')
	req = numRest >= 100
	newAch = parseAch(a, req, user, newAch)

	if len(newAch) > 0:
		return newAch[0]
	else:
		return False