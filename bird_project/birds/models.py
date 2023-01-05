from django.db import models
from django.forms import ModelForm

class BirdSighting(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]
    AGE_CHOICES = [
        ('E', 'Egg'),
        ('H', 'Hatchling'),
        ('J', 'Juvenile'),
        ('A', 'Adult')
    ]
    
    species = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.CharField(max_length=1, choices=AGE_CHOICES)
    location = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    spotter = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

class SightingForm(ModelForm):        
    class Meta: 
        model = BirdSighting
        exclude = ['date']