from django.db import models

# Create your models here.
# Create your models here.
class Candidate(models.Model):
      username=models.CharField(max_length=100)
      email=models.EmailField(max_length=100)
      password=models.CharField(max_length=100)
