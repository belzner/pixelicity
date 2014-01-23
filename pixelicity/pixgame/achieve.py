from django.contrib.auth.models import User
from pixgame.models import UserAchieve, Achievement

def checkAchieve(a, req, user):
	ua = UserAchieve.objects.get(user=user)
	if req:
		if a not in ua.achievements.all():
			ua.achievements.add(a)
			return True
	return False