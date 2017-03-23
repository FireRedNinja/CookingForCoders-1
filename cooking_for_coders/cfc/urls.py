from django.conf.urls import url
from cfc import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_title_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^recipe/(?P<recipe_id>[\w\-]+)/$', views.recipe, name='recipe'),
    url(r'^splash/$', views.splash, name='splash'),
    url(r'^profile/$', views.profile, name='profile'),


]
