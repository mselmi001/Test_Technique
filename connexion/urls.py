from django.conf.urls import include, url

from connexion.views import *
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', LoginView.as_view()),
    url(r'^home$', views.home, name='home'),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^connexion/$', login_required(TemplateView.as_view(template_name='connexion/index.html'))),
]
