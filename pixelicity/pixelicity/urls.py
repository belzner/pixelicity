from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from pixgame import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pixelicity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^admin', include(admin.site.urls)),
    url(r'^login', views.userlogin, name='login'),
    url(r'^logout', views.userlogout, name='logout'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
