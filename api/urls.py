from . import views
from django.urls import path
from django.urls import include



urlpatterns = [
    path('voter-publickey', views.VoterPublickeyApiView.as_view(), name='voter-publickey'),
    path('candidate-publickey', views.CandidatePublickeyApiView.as_view(), name='candidate-publickey'),
]