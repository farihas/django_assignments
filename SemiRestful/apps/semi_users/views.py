# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
from datetime import datetime

# index method - displays homepage with all users via /users 
def index(request):
   users = {
      "users": User.objects.all()
     }
   return render(request, "semi_users/index.html", users)

# new method - displays add new user form page via /users/new
def new(request):
   return render(request, "semi_users/new.html")

# show method - displays selected user via /users/<id>
def show(request, id):

   user = {
      "user" : User.objects.get(id=id)
   }   
   return render(request, "semi_users/show.html", user)

# edit method - displays a form allowing editing of a given user record via /users/<id>/edit
def edit(request, id):
   user = {
      "user": User.objects.get(id=id)
   }
   # redirects to /users/<id>/update on update user form submission
   return render(request, "semi_users/edit.html", user)

# create method - creates new user record using posted form info via /users/create
def create(request):
   errors = User.objects.validate(request.POST)
   if len(errors):
      for error in errors.iteritems():
         messages.error(request, error)
         print {{ error }}

      return redirect("/users/edit")
     
   user = User.objects.create(
      first_name = request.POST["first_name"],
      last_name = request.POST["last_name"],
      email = request.POST["email"],
   )
   id = user.id
   # redirects to /users/<id> on successful new user form submission
   return redirect("/users/{}".format(id))

# update method - processes updates to the user record via /users/<id>/update(request, "users/{{ user.id }}/update")
def update(request, id):
   errors = User.objects.validate(request.POST)
   if len(errors):
      for error in errors:
         messages.error(request, error)

      return redirect("/users/edit.html")

   user = User.objects.get(id=id)
   user.first_name = request.POST["first_name"]
   user.last_name = request.POST["last_name"]
   user.email = request.POST["email"]
   user.save()
   # redirects to /users/<id> on update user form submission
   return redirect("/users/{}".format(id))

# destroy method - deletes a given user via /users/<id>/destroy
def destroy(request, id):
   user = User.objects.get(id=id)
   user.delete() 
   # redirects to /users homepage on deletion
   return redirect("/users")
