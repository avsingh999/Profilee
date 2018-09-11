from django.conf.urls import url
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    url(r'^$', views.HomeView, name='Myprofile'),
    url(r'^(?P<id>[0-9]+)$', views.likepost, name='likepost'),
    url(r'^posts/(?P<id>[0-9]+)$', views.viewpost, name='viewpost'),
    url(r'^posts/(?P<id>[0-9]+)/comment$', views.commentpost, name='commentpost'),

]
