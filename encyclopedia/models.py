from django.db import models
from django.db.models.fields import CharField
from django.db.models.functions import Length

class Search(models.Model):
    text =  models.CharField(max_length = 3)
# Create your models here.
