from django.conf.urls import patterns, include, url
from django.contrib import admin

# Enable admin area
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'supercluster.views.home', name='home'),
    url(r'^$', include('game.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
