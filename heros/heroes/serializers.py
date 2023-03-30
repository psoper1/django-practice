from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hero


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['name', 'about_me', 'biography', 'abilities']
        depth = 1