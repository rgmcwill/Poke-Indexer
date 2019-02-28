from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from main.models import Game_Info,Team_RPI

# Create your views here.
# Ross made a really cool comment
def TeamStatistics(request):
    latest_team_list = Game_Info.objects.order_by('-pub_date')[:5]
    template = loader.get_template('TeamStatistics.html')
    context = {
        'latest_team_list': latest_team_list,
    }
    return HttpResponse(template.render(context, request))

def CurrentRanking(request):
    latest_team_list = Game_Info.objects.order_by('-pub_date')[:5]
    template = loader.get_template('CurrentRanking.html')
    context = {
        'latest_team_list': latest_team_list,
    }
    return HttpResponse(template.render(context, request))