from django.db import models

# Create your models here.

class cakewale(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    skill=models.CharField(max_length=150)
    image=models.ImageField(upload_to='photo')


    
