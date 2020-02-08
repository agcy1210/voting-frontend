from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.verifyId,name='verifyId'),
    path('secret_msg/',views.secret_msg,name='secret_msg'),
    path('voting/',views.voting,name='voting'),
    path('voting/candidate', views.votingCandidate, name='voting_candidate')

]