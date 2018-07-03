from django.conf.urls import url
from . import views           

urlpatterns = [
  # localhost:8000/ninja_gold - displays the four forms when the user goes to http://localhost 
  url(r'^$', views.index),  

  # localhost:8000/ninja_gold/process_money - determines how much gold to give/take away and redirects to '/ninja_gold/'
  url(r'^process_money$', views.process_money),

  # localhost:8000/ninja_gold/clear - clears session
  url(r'^clear$', views.clear),

]