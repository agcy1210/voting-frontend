import json
import os
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Voter,Candidate

# Create your views here.

@login_required(login_url='accounts/login')
def authenticate(request):

    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    if request.method == 'POST':
        voterId = request.POST['voterId']
            
    return render(request,'voting/voterIdAuthentication.html')

@login_required(login_url='accounts/login')
def secretmessage(request):

    # # if request.user.is_authenticated:
    # #     return redirect('index')
    # # else:
    # if request.method == 'POST':
    #     voterId = request.POST['voterId']
            
    return render(request,'voting/voterSecretMessage.html')    





