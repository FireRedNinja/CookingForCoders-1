from django.conf.urls import url
from cfc import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
