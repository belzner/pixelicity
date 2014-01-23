from django.contrib import admin
from pixgame.models import Locations, UserLocs, Achievement, UserAchieve

# Register your models here.
admin.site.register(Locations)
admin.site.register(UserLocs)
admin.site.register(Achievement)
admin.site.register(UserAchieve)