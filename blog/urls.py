from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'home$', views.home),
    url(r'board$', views.board),
    url(r'cities$', views.cities),
    url(r'orgs$', views.orgs),
    ]
