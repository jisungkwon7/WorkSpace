from django.conf.urls import url
from apptwo import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^$', views.help,name='help'),
]
