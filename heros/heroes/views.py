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

# def all_heroes(request):
#     a_hero = Hero.objects.values_list('name')
#     a_about = Hero.objects.values_list('about_me')
#     print(a_hero)
#     html = ''
#     htmlTwo = ''
#     for name in a_hero:
#         html += '<h1>Hero: %s</h1>' % name
#     for about in a_about:
#         htmlTwo += '<h3>About: %s</h3>' % about
#     return HttpResponse(html + htmlTwo)
    
