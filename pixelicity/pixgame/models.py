from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Locations(models.Model):
	centerLat = models.DecimalField(max_digits=10, decimal_places=5)
	centerLng = models.DecimalField(max_digits=10, decimal_places=5)
	locName = models.CharField(max_length=80)
	locType = models.CharField(max_length=20)
	locImage = models.CharField(max_length=40)
	locId = models.IntegerField()

	def __unicode__(self):
		return self.locName

class UserLocs(models.Model):
	user = models.OneToOneField(User)
	locations = models.ManyToManyField(Locations)

	def __unicode__(self):
		return self.user.username

class Achievement(models.Model):
	compName = models.CharField(max_length=20)
	humanName = models.CharField(max_length=80)
	hint = models.TextField()
	image = models.CharField(max_length=40)
	how = models.TextField()

	def __unicode__(self):
		return self.humanName

class UserAchieve(models.Model):
	user = models.OneToOneField(User)
	achievements = models.ManyToManyField(Achievement)

	def __unicode__(self):
		return self.user.username

class Character(models.Model):
	name = models.CharField(max_length=20)
	intro = models.TextField()
	achieve = models.ForeignKey(Achievement)
	locType = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField()
	image = models.CharField(max_length=40)
	character = models.ForeignKey(Character)

	def __unicode__(self):
		return self.name

class Collection(models.Model):
	user = models.OneToOneField(User)
	characters = models.ManyToManyField(Character)
	items = models.ManyToManyField(Item)

	def __unicode__(self):
		return self.user.username
