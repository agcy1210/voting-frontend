from rest_framework import serializers
from voting import models

class VoterPublickeySerializer(serializers.Serializer):
    public_key = serializers.CharField(max_length=128)
    reference_no = serializers.CharField(max_length=64)

class CandidatePublickeySerializer(serializers.Serializer):
    candidate_id = serializers.IntegerField()
    candidate_name = serializers.CharField(max_length=50)
    party_name = serializers.CharField(max_length=128)
    candidate_publickey = serializers.CharField(max_length=128)
