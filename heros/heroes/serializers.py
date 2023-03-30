from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hero, Ability


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'name', 'about_me', 'biography', 'abilities',]
        depth = 1

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ['id','ability_name']