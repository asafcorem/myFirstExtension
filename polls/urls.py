from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<pk>[0-9]+)/posts_display/$', views.IndexView.as_view(), name='posts_display'),
    url(r'^1/clean_data_bases/$', views.clean_data_bases, name='clean_data_bases'),
    url(r'^([0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<user_id>[0-9]+)/saving/$', views.saving, name='saving'),
    url(r'^([0-9]+)/fsdssd/$', views.start_scan, name='start_scan'),
    url(r'^([0-9]+)/$', views.DetailView.as_view(), name='detail'),

#     url(r'^homepage/$', views.DetailView.as_view(), name='asdfsa'),
]