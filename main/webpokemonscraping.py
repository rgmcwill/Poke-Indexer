import requests,datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from main.models import Pokemon,Type

class Web_Pokemon_Scraping:
    url = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)"

    def __init__(self):
        count = 0
        while(True):
            self.page = requests.get(self.url, headers=self.get_random_user_agent())
            print("got to url: "+self.page.url)
            print("got satus_code: "+ str(self.page.status_code))
            self.html = BeautifulSoup(self.page.text,'lxml')
            name = self.get_poke_name(self.html)
            numb = self.get_numb(self.html)
            types = self.get_types_name(self.html)
            self.url = self.get_next_url(self.html)

            for i in types:
                if not Type.objects.filter(name=i).exists():
                    Type(name=i).save()

            Pokemon(name=name,numb=numb).save()
            p = Pokemon.objects.filter(name=name,numb=numb)[0]
            for i in types:
                p.types.add(Type.objects.get(name=i))
            p.save()

            if count > 5:
                break
            count = count + 1


    def get_next_url(self,page):
        link_attrs = page.findAll(text="→")[0].parent.parent
        return "https://bulbapedia.bulbagarden.net" + str(link_attrs.attrs.get("href"))

    def get_poke_name(self,page):
            return page.find(id="firstHeading").text[:9]

    def get_types_name(self,page):
            type_link = page.find(href="/wiki/Type",title="Type")
            type_table = type_link.parent.parent
            return [type_table.findChildren()[11].text, type_table.findChildren()[15].text]

    def get_numb(self,page):
            numb_parent = page.findAll(title="List of Pokémon by National Pokédex number")
            numb_child = numb_parent[1].text
            return int(numb_child[1:])

    def get_all_poke(self):
        return Pokemon.objects.all()

    def get_random_user_agent(self):
        ua = UserAgent()
        return {'User-agent': ua.random}
