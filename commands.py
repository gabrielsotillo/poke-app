import requests
import customtkinter
from io import BytesIO
from PIL import Image

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
        

def get_pokemon():

    from gui import my_entry, my_label, my_textbox
    
    try:
        # Dictionary about the Pokemon requested
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{my_entry.get().lower()}')
        pokemon_json = r.json() 
    except:
        clear()
        my_textbox.insert("0.0", f"Ese Pokemon no existe.")
        return
        
    pokemon = Pokemon(pokemon_json)

    my_textbox.delete("0.0","end")
    my_textbox.insert("0.0", pokemon.get_info())

    # Image Widget Update 
    my_image = customtkinter.CTkImage(light_image=Image.open(BytesIO(pokemon.image)), size=(310, 310))
    my_label.configure(image=my_image)

def clear():
    from gui import my_label, my_textbox

    my_textbox.delete("0.0","end")
    my_label.configure(image=None)

def exit_app():
    exit()