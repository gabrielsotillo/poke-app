import requests
#import inspect
import json
json_gabo_file = open("data/gabo.json")
gabo_data = json.load(json_gabo_file)
gabo_img = open("data/gabo.jpg", "rb")

class Pokemon:

    def __init__(self, pokemon):

        self.name = pokemon['name'].capitalize()
        self.weight = f"{pokemon['weight']} lb"
        self.height = f"{pokemon['height']} in"
        self.type = pokemon['types'][0]['type']['name'].capitalize()
        self.id = pokemon['id']
        self.image = self.__get_img(pokemon) 

    def __get_img(self, pokemon): # The __ before implies this is a private function
        if pokemon["name"] == "Gabomon":
            f = gabo_img.read()
            b = bytearray(f)
            return  b
        else: 
            url_img = pokemon['sprites']['front_default']
            r = requests.get(url_img)
            return r.content 
    
    def get_info(self):

        info = ""
        for key in vars(self):
            if key == 'image':
                continue
            else:
                info = info + f"{key.capitalize()}: {vars(self)[key]}\n"
         
        return info
        

def get_pokemon(pokename):
    if ((pokename == "gabo") | (pokename == "gabrielon" )| (pokename ==  "gabriel" )|(pokename == "gabomon")):
        pokemon=Pokemon(gabo_data)
        return pokemon
    else: 
        # Dictionary about the Pokemon requested
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokename}')
        pokemon_json = r.json() 
        print(pokemon_json)
        pokemon = Pokemon(pokemon_json)
        return pokemon