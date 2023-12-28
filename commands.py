import requests
import customtkinter
from io import BytesIO
from PIL import Image

def get_pokemon():

    from gui import my_entry, my_label, my_textbox
    
    try:
        # Dictionary about the Pokemon requested
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{my_entry.get().lower()}')
        pokemon = r.json() 
    except:
        clear()
        my_textbox.insert("0.0", f"Ese Pokemon no existe.")
        return
        
    # Photo of that Pokemon
    img_url = pokemon['sprites']['front_default']
    r = requests.get(img_url)
    pokemon_img = r.content 

    # TextBox Widget Update
    name = pokemon['name'].capitalize()
    weight = pokemon['weight']
    height = pokemon['height']
    type = pokemon['types'][0]['type']['name'].capitalize()

    my_textbox.delete("0.0","end")
    my_textbox.insert("0.0", (f"Name: {name}\n"
                              f"Type: {type}\n"
                              f"Weight: {weight} lb\n"
                              f"Height: {height} in")
                              )

    # Image Widget Update 
    my_image = customtkinter.CTkImage(light_image=Image.open(BytesIO(pokemon_img)), size=(310, 310))
    my_label.configure(image=my_image)

    print(pokemon['name'])

def clear():
    from gui import my_label, my_textbox

    my_textbox.delete("0.0","end")
    my_label.configure(image=None)

def exit_app():
    exit()