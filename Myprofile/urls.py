from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView, name='Myprofile'),
    url(r'^posts/(?P<id>[0-9]+)$', views.viewpost, name='viewpost'),

]
