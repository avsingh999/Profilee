from django.conf.urls import  url
from . import views
# from django.contrib.auth.views import login

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
        url(r'^$', views.home),
        
        url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name="login"),
        url(r'^logout/$', LogoutView.as_view(template_name='accounts/home.html'), name="logout"),
        url(r'^register/$', views.register, name="register"),
        # url(r'^/$')

]

# urlpatterns = [
    # url(r'^$', views.home),
#     url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
# ]