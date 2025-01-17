import json
import os
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Voter,Candidate
import hashlib
import requests


@login_required(login_url='accounts/login')
def verifyId(request):
    user = Voter.objects.filter(isverify=True)

    if user:
        context ={
            'isverify' : True
        }
    else:
        context ={
            'isverify' : False
        }

    return render(request,'voting/voterIdAuthentication.html',context)

def getHash(secret_msg, voter_id):
    hashString = secret_msg + str(voter_id)
    return hashlib.sha256(hashString.encode()).hexdigest()


@login_required(login_url='accounts/login')
def secret_msg(request):

    if request.method == 'POST':
        secret_msg = request.POST['secret_msg']
        reference_number = request.POST['reference_number']
        voter_id = request.POST['voter_id']

        hashKey = getHash(secret_msg, voter_id)
        
        obj = Voter(reference_no = reference_number,unique_hash=hashKey,voter_publickey=voter_id,isverify=True )
        obj.save()
        context = {
            'reference_number': reference_number
        }
        return render(request, 'voting/referenceNumber.html', context=context)

    return render(request, 'voting/voterSecretMessage.html')

@login_required(login_url='accounts/login')
def voting(request):
    if request.method == 'POST':
        secret_msg = request.POST['secret_msg']
        reference_number = request.POST['reference_number']
        voter_id = request.POST['voter_id']
        hashed = getHash(secret_msg, voter_id)
        queryset =Voter.objects.filter(reference_no= reference_number, unique_hash=hashed)

        if queryset:
            return redirect('voting_candidate')
        else:
            return redirect('voting')
    else:
        return render(request,'voting/voterVotingProcess.html')


@login_required(login_url='accounts/login')
def votingCandidate(request):
    queryset = Candidate.objects.all()


    context = {
        "candidates": queryset
    }

    return render(request,'voting/candidateslist.html', context=context)

def results(request):
    result= requests.get('http://localhost:3003/api/results')
    token_json_data = json.loads(result.text)
    print(token_json_data)
    results = token_json_data.get('results')
    querysets = Candidate.objects.all()
    winner= []
    winner_counts = []
    for key,value in results.items():
        for queryset in querysets:
            if key == queryset.candidate_publickey:
                winner.append({
                        'name': queryset.candidate_name,
                        'votes': value
                })
    # for el in winner:
    #    # print(el['name'] + " - " + el['votes'])
    context= {
        'winner' : winner,
        'winner_counts': winner_counts
    }
    return render(request,'voting/electionResults.html',context)

