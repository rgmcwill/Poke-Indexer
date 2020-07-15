from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from main.models import Game_Info,Team_RPI,Team
from main.dbgame import DB_Game_Interface
from main.dbTeams import DB_Teams_Interface
from main.webscorescraping import Web_Scraping
from main.webteamscraping import Web_Team_Scraping
from main.webpokemonscraping import Web_Pokemon_Scraping
from.forms import PokemonSearch
from main.math import RPI_Calculation
from main.dbRating import DB_RPI_Interface
from main.webtargets import Past
from main.models import Pokemon

# Create your views here.
# Ross made a really cool comment
def DBLookup(request):
    if request.method == 'POST':
        #searched_team = request.POST['team']
        searched_pokemon = request.POST['pokemon']
        # print(searched_team)

        db = DB_Game_Interface()

        #latest_team_list = db.get_by_team(searched_team)
        pokemons = Pokemon.objects.filter(name=searched_pokemon)
        template = loader.get_template('DBLookup.html')
        context = {
            'poke_name' : searched_pokemon,
            'pokemons': pokemons,
            'form' : PokemonSearch()
        }
        return HttpResponse(template.render(context, request))
    else:
        '''db = DB_Teams_Interface()
        wts = Web_Team_Scraping()

        db.create_teams_from_dict(wts.get_team_info())
        '''
        db = DB_Game_Interface()
        Web_Pokemon_Scraping()
        '''
        #RPI_Calculation("Arkansas")
        ws = Web_Scraping(14,4,2019)
        #print(ws.get_pre_game_list())

        #ws = Past(1,2,2019,None,10,2,2019)'''
        '''
        for i in db.get_all_teams():
            RPI_Calculation(i)'''
        latest_team_list = db.get_by_team("Arkansas")
        pokemons = Pokemon.objects.all()
        template = loader.get_template('DBLookup.html')
        context = {
            'team_name' : "Arkansas",
            'poke_name' : "",
            'latest_team_list': latest_team_list,
            'pokemons': pokemons,
            'form' : PokemonSearch()
        }
        return HttpResponse(template.render(context, request))

def index(request):
    return redirect('/DBLookup')

def clear(request):
    for i in Pokemon.objects.all():
        i.delete()
    return redirect('/DBLookup')
