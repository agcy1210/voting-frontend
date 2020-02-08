from django.contrib import admin
from . import models

admin.site.register(models.Voter)
admin.site.register(models.Candidate)
