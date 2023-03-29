from django.shortcuts import render
import datetime
from django.http import HttpResponse, JsonResponse
import json
from heroes.models import Hero, Ability
# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<h1>It is now %s.</h1>" % now
    return HttpResponse(html)

def all_heroes(request):
    a_hero = Hero.objects.values_list('name', 'about_me')
    print(a_hero)
    html = ''
    for name in a_hero:
        html += '<h1>Hero: %s <p>About: %s</p></h1>' % name
    return HttpResponse(html)

def json(request):
    data = list(Hero.objects.values())
    return JsonResponse(data, safe=False)

# def ability_json(request):
#     data = list(Ability.objects.value())
#     return JsonResponse(data, safe=False)