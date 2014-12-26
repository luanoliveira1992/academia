from django.conf.urls import patterns, include, url
from django.contrib import admin
from usuarios.views import IndexView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^accounts/', include('allauth.urls')),
)