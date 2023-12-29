import requests

class Pokemon:

    def __init__(self, pokemon):

        self.name = pokemon['name'].capitalize()
        self.weight = pokemon['weight']
        self.height = pokemon['height']
        self.type = pokemon['types'][0]['type']['name'].capitalize()
        self.image = self.get_img(pokemon) 

    def get_img(self, pokemon):
            
        url_img = pokemon['sprites']['front_default']
        r = requests.get(url_img)
        return r.content 
    
    def get_info(self):
         info = (f"Name: {self.name}\n"
                 f"Type: {self.type}\n"
                 f"Weight: {self.weight} lb\n"
                 f"Height: {self.height} in")

         return info
        

def get_pokemon(pokename):

    # Dictionary about the Pokemon requested
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokename}')
    pokemon_json = r.json() 
    pokemon = Pokemon(pokemon_json)
    return pokemon