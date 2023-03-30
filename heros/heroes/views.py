from django.shortcuts import render
import datetime
from django.http import HttpResponse, JsonResponse
import json
from heroes.models import Hero, Ability
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from heroes.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<h1>It is now %s.</h1>" % now
    return HttpResponse(html)

def all_heroes(request):
    a_hero = Hero.objects.values_list('name', 'about_me', 'biography', 'abilities')
    print(a_hero)
    html = ''
    for name in a_hero:
        html += '''<h1>Hero: %s 
                        <p>About: %s</p>
                            <p> Bio: %s</p>
                                <p> Abilities: %s</p>
                    </h1>''' % name
    return HttpResponse(html)

def json(request):
    data = list(Hero.objects.values())
    return JsonResponse(data, safe=False)

# def ability_json(request):
#     data = list(Ability.objects.value())
#     return JsonResponse(data, safe=False)