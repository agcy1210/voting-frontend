from django.db import models

# Create your models here.
class Voter(models.Model):
    reference_no  = models.CharField(max_length=50)
    unique_hash = models.CharField(max_length=128)
    voter_publickey = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.voter_publickey


class Candidate(models.Model):
    candidate_name = models.CharField(max_length=50)
    party_name = models.CharField(max_length=128)
    candidate_publickey =  models.CharField(max_length=128)

    def __str__(self):
        return self.candidate_name


    

