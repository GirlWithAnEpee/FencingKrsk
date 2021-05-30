from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^coaches$', views.coaches, name='coaches'),
    url(r'^awards$', views.awards, name='awards'),
    url(r'^rasp60$', views.rasp60, name='rasp60'),
    url(r'^raspM$', views.raspM, name='raspM'),
    url(r'^raspES$', views.raspES, name='raspES'),
    url(r'^fencers/$', views.FencerListView.as_view(), name='fencers'),
    url(r'^fencer/(?P<pk>\d+)$', views.FencerDetailView.as_view(), name='fencer-detail'),
    url(r'^competitions/$', views.CompetitionListView.as_view(), name='competitions'),
    url(r'^competition/(?P<pk>\d+)$', views.CompetitionDetailView.as_view(), name='competition-detail'),
    url(r'^results/$', views.ResultListView.as_view(), name='results'),
]