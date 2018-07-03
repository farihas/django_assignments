# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

import random
import datetime

def index(request):    
    # display the four forms when the user goes to http://localhost    
   if "gold" not in request.session:
      request.session["gold"] = 0     # When you start the game, your ninja should have 0 gold.    
   if "activity" not in request.session:
      request.session["activity"] = []

   return render(request, "ninja_gold/index.html")


def process_money(request):
   # determine how much gold to give/take away and redirect to '/ninja_gold/'
   gold = request.session["gold"]
   building = request.POST["building"]
   if building == "farm":
      x = random.randint(10, 20)
      gold += x
      message = "Earned {} golds from the farm! {}".format(gold, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
   elif building == "cave":
      x = random.randint(5, 10)
      gold += x
      message = "Earned {} golds from the cave! {}".format(gold, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
   elif building == "house":
      x = random.randint(2, 5)
      gold += x
      message = "Earned {} golds from the house! {}".format(gold, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
   elif building == "casino":
      luck = random.randint(0, 1)
      x = random.randint(0, 50)
      if luck == 0:
         gold -= x
         message = "<text id='red'>Entered a casino and lost {} golds... Ouch.. {}".format(gold, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
      else:
         gold += x    
         message = "Entered a casino and won {} golds! {}".format(gold, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  

   request.session["activity"].append(message)
   request.session["gold"] = gold      

   return redirect("/ninja_gold")


def clear(request):
   # clear session
   request.session.clear()
   # Redirect to index
   return redirect("/ninja_gold")


