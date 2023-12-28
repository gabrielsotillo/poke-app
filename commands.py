def get_pokemon():

    import requests
    import customtkinter
    from io import BytesIO
    from PIL import Image
    from gui import my_entry, my_label

    # Dictionary about the Pokemon requested
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{my_entry.get().lower()}')
    pokemon = r.json() 

    # Photo of that Pokemon
    img_url = pokemon['sprites']['front_default']
    r = requests.get(img_url)
    pokemon_img = r.content 

    # Image Widget update 
    my_image = customtkinter.CTkImage(light_image=Image.open(BytesIO(pokemon_img)), size=(150, 150))
    my_label.configure(image=my_image)

    print(pokemon['name'])

def exit_app():
    exit()