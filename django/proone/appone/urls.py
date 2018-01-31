from django.conf.urls import url
from appone import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^$', views.IamAppOne,name='IamAppOne'),
]
