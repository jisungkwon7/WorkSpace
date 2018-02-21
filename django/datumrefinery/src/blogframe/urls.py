from django.conf.urls import url
from blogframe import views

urlpatterns = [
    url(r'^aboutview/$',views.AboutView.as_view(),name='aboutview'),
]
