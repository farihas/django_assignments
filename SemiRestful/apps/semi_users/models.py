# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from time import gmtime, strftime

# Create your models here.
class UserManager(models.Manager):
   def validate(self, posted):
      errors = {}
 
      if len(posted["first_name"]) < 3 or len(posted["last_name"]) < 3:
         errors["first_name", "last_name"] = "Name should be more than 2 characters."
      if not (posted["first_name"]).isalpha() or not (posted["last_name"]).isalpha():
         errors["first_name", "last_name"] = "Name cannot contain any numbers."
      if not EMAIL_REGEX.match(posted["email"]):
         errors["email"] = "Please enter a valid email."

      return errors
      # todo:
      # if (request.POST["email"]) == existing email:
      #    errors["email"] = "Email already registered." 


class User(models.Model):
   first_name = models.CharField(max_length = 100)
   last_name = models.CharField(max_length = 100)
   email = models.CharField(max_length = 100)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   # connecting an instance of UserManager to our User model
   objects = UserManager()
   def __repr__(self):
      return "<User object: {} {} {} {} {}>".format(
         self.first_name, self.last_name, self.email, self.created_at.strftime("%m-%d-%Y %H:%M %p"), self.updated_at.strftime("%m-%d-%Y %H:%M %p")
      )
   # def __str__(self):


#    def getCreatedAt(self):     
#       created_at = {
#          "created_at": self.created_at.strftime("%m-%d-%Y %H:%M %p", gmtime())  
#       }
#       return created_at

#    def getUpdatedAt(self):     
#       updated_at = {
#          "updated_at": self.updated_at.strftime("%m-%d-%Y %H:%M %p", gmtime())
#       }
#       return updated_at