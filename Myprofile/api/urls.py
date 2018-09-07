from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name='list'),
    url(r'^create$', views.CreatePostAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', views.PostUpdateAPIView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete$', views.PostDeleteAPIView.as_view(), name='delete'),

]
