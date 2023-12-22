import requests
from gui import run_GUI

def run():

    pokemon = get_data('pikachu')
    img_url = pokemon['sprites']['front_default']
    print(pokemon['name'])
    run_GUI(img_url)

def get_data(pokemon):

    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

    r = requests.get(url)
    return r.json() # Retorna una lista de diccionarios

if __name__ == '__main__':
    run()