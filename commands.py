import requests
#import inspect

class Pokemon:

    def __init__(self, pokemon):

        self.name = pokemon['name'].capitalize()
        self.weight = f"{pokemon['weight']} lb"
        self.height = f"{pokemon['height']} in"
        self.type = pokemon['types'][0]['type']['name'].capitalize()
        self.id = pokemon['id']
        self.image = self.get_img(pokemon) 

    def get_img(self, pokemon):
            
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

    # Dictionary about the Pokemon requested
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokename}')
    pokemon_json = r.json() 
    pokemon = Pokemon(pokemon_json)
    return pokemon