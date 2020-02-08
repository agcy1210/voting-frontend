import json
import os
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Voter, Candidate
import hashlib

# Create your views here.


@login_required(login_url='accounts/login')
def verifyId(request):

    if request.method == 'POST':
        voterId = request.POST['voterId']

    return render(request, 'voting/voterIdAuthentication.html')


def getHash(secret_msg, voter_id):
    hashString = secret_msg + str(voter_id)
    return hashlib.sha256(hashString.encode()).hexdigest()


@login_required(login_url='accounts/login')
def secret_msg(request):

    if request.method == 'POST':
        secret_msg = request.POST['secret_msg']
        reference_number = request.POST['reference_number']

    hashString = secret_msg+reference_number
    hashKey = getHash(hashString)

    return render(request, 'voting/voterIdAuthentication.html')
