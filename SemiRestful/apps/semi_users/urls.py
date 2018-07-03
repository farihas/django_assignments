# semi_users App's urls

from django.conf.urls import url
from . import views 

urlpatterns = [
   # /users - displays homepage with all users via index method
   url(r'^$', views.index), 

   # /users/new - displays add new user form page via new method
   url(r'^new$', views.new),

   # /users/<id> - displays selected user via show method
   url(r'^(?P<id>\d+)$', views.show),

   # /users/<id>/edit - displays a form allowing editing of a given user record
   url(r'^(?P<id>\d+)/edit$', views.edit),

   # /users/create - creates new user record using posted form info via create method
   url(r'^create$', views.create),

   # /users/update - processes updates to the user record via update method
   url(r'^update$', views.update),

   # /users/<id>/destroy - deletes a given user via the destroy method
   url(r'^(?P<id>\d+)/destroy$', views.destroy),

]
