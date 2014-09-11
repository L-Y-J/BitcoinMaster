from django.conf.urls import patterns, include, url

from django.contrib import admin
from BitcoinTradeMaster import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BitcoinTradeMaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'calculate.views.indexView'),
    url(r'^onLoad/', 'calculate.views.onLoad'),
    url(r'^calculate/', 'calculate.views.calculate'),
    url(r'^jslib/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
)
