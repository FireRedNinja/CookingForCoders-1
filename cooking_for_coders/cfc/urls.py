from django.conf.urls import url
from cfc import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_title_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^recipe/(?P<recipe_id>[\w\-]+)/$', views.recipe, name='recipe'),
    url(r'^splash/$', views.splash, name='splash'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^recipe/(?P<recipe_id>[\w\-]+)/recipeStore/$', views.recipeStore, name='recipe_store'),
    url(r'^add_rating/$', views.add_rating, name='add_rating'),


]
