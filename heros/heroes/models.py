from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=50)
    about_me = models.CharField(max_length=200)
    biography = models.CharField(max_length=400)

class Ability(models.Model):
    ability_name = models.CharField(max_length=100)
    abilities = models.ManyToManyField('Hero')
