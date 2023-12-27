import requests
from gui import run_GUI

def run():

    pokemon = get_data('totodile')
    img_data = get_image(pokemon)

    print(pokemon['name'])
    run_GUI(img_data)

def get_data(name):

    url = f'https://pokeapi.co/api/v2/pokemon/{name}'

    r = requests.get(url)
    return r.json() # Retorna una lista de diccionarios

def get_image(pokemon):
    img_url = pokemon['sprites']['front_default']

    r = requests.get(img_url)
    return r.content

if __name__ == '__main__':
    run()