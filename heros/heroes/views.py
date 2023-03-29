from django.shortcuts import render
import datetime
from django.http import HttpResponse
from heroes.models import Hero
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