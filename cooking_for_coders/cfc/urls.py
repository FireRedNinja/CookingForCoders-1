from django.conf.urls import url
from cfc import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),


    # url(r'^recipe/$', views.recipe, name='recipe'),
    # url(r'^splash/$', views.splash, name='splash'),
    # url(r'^profile/$', views.profile, name='profile'),


]
