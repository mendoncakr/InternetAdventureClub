from django.conf.urls import patterns, include, url
from travel import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^thelist/$', views.all_missions, name='all_missions'),
    url(r'^mission/new/$', views.add_mission, name='add_mission'),
    # url(r'^thanks/$', views.thanks, name='thanks'),
)
