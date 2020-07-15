import requests,datetime,re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from main.models import Pokemon,Type,Game,Location

class Web_Pokemon_Scraping:
	url = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)"

	def __init__(self):
		count = 0
		while(True):
			name = self.get_poke_name(self.url)
			if not self.filled(name):
				self.page = requests.get(self.url, headers=self.get_random_user_agent())
				print("got to url: "+self.page.url)
				print("got satus_code: "+ str(self.page.status_code))
				self.html = BeautifulSoup(self.page.text,'lxml')

				self.url = self.get_next_url(self.html)
				numb = self.get_numb(self.html)
				types = self.get_types_name(self.html)
				locations = self.get_locations(self.html)

				for i in types:
					if not Type.objects.filter(name=i).exists():
						Type(name=i).save()

				for i in locations:
					if not Game.objects.filter(name=i).exists():
						#print("Did NOT exist")
						Game(name=i).save()
						g = Game.objects.get(name=i)
					else:
						#print("DID exist")
						g = Game.objects.get(name=i)
					#print("g , game object: ", g)
					#print("i , game name: ", i)
					for j in locations[i]:
						#print("j , location name: ", j)
						if not Location.objects.filter(name=j,game=g).exists():
							Location(name=j,game=g).save()

				if not Pokemon.objects.filter(name=name,numb=numb).exists():
					Pokemon(name=name,numb=numb).save()

				p = Pokemon.objects.filter(name=name)[0]
				p.numb = numb
				for i in types:
					p.types.add(Type.objects.get(name=i))
				for i in locations:
					for j in locations[i]:
						p.locations.add(Location.objects.get(name=j,game=Game.objects.get(name=i)))
				p.save()

			if count > 1:
				break
			count = count + 1

	def filled(self,name):
		filled = True
		q = Pokemon.objects.filter(name=name)
		if len(q) == 0:
			return False
		else:
			if q[0].numb == -1 or len(q[0].types.all()) == 0 or len(q[0].locations.all()) == 0:
				filled = False
		return filled

	def get_next_url(self,page):
		link_attrs = page.findAll(text="→")[0].parent.parent
		return "https://bulbapedia.bulbagarden.net" + str(link_attrs.attrs.get("href"))

	def get_poke_name(self,url):
		return re.search('wiki/(.*)_',url).group(1)
		#return (page.find(id="firstHeading").text).split(' ')[0]
	
	def get_poke_evolution(self,page):
		

	def get_types_name(self,page):
			type_link = page.find(href="/wiki/Type",title="Type")
			type_table = type_link.parent.parent
			return [type_table.findChildren()[11].text, type_table.findChildren()[15].text]

	def get_numb(self,page):
			numb_parent = page.findAll(title="List of Pokémon by National Pokédex number")
			numb_child = numb_parent[1].text
			return int(numb_child[1:])

	def get_locations(self,page):
		main_table = page.find(id="Game_locations").next.next.next
		all_sub_tables = main_table.findAll('table',width="100%")[1::2]
		exclude = ['Routes','Route','Bug-Catching Contest','Days of the week','Headbutt tree']
		a = {}
		for i in all_sub_tables:
			all_info = i.findAll('tr')
			titles = []
			locations = all_info[1::2]
			for j in all_info[::2]:
				temp = ''
				for k in j.findAll('th'):
					temp = temp + str(k.text.rstrip()[1:])+'|'
				temp = temp[:-1]
				titles.append(temp)
			for j in range(len(titles)):
				s = locations[j].findAll('a')
				t = []
				if s == []:
					t = [str(locations[j].text).replace('\n','')[1:]]
				else:
					for k in s:
						if not k.attrs['title'] in exclude:
							t.append(k.attrs['href'][6:].replace("_"," ").replace("%C3%A9","e").replace("%27","'").replace("List of Pokemon by Pal Park location#",""))
				s = t
				a.update({titles[j]:s})
		to_delete = []
		to_add = {}
		for i in a:
			t = i.split("|")
			if len(t) == 2:
				to_add.update({t[0]:a[i]})
				to_add.update({t[1]:a[i]})
				to_delete.append(i)
		a.update(to_add)
		for i in to_delete:
			del a[i]
		return a

	def get_all_poke(self):
		return Pokemon.objects.all()

	def get_random_user_agent(self):
		ua = UserAgent()
		return {'User-agent': ua.random}
