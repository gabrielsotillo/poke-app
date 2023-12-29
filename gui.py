import customtkinter
from io import BytesIO
from PIL import Image
from commands import get_pokemon


def run_GUI():

    # ------ Root creation and config ------
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('blue')
    root = customtkinter.CTk()
    root.geometry('800x600')
    root.title('PokeDex')

    # Frames
    left_frame = customtkinter.CTkFrame(master=root, width=400, fg_color="#dd2626")
    left_frame.pack(side='left', fill='both')

    right_frame = customtkinter.CTkFrame(master=root, width=400, height=600, fg_color='#d03939')
    right_frame.pack(fill='both', expand=True)
    
    top_frame = customtkinter.CTkFrame(master=right_frame, width=400, height=300, border_width=20, border_color='#d03939', fg_color="#ffffff")
    top_frame.pack(fill='both', expand=True)

    bottom_frame = customtkinter.CTkFrame(master=right_frame, width=400, height=300, fg_color=  '#d03939'  )
    bottom_frame.pack(fill='both', expand=True)

    # Label
    global my_label 
    my_label = customtkinter.CTkLabel(master=top_frame, text='')
    my_label.place(relx = 0.5, rely = 0.5, anchor = 'center')

    # Entry
    global my_entry 
    my_entry = customtkinter.CTkEntry(master=bottom_frame, placeholder_text='Pokemon')
    my_entry.pack(pady=20)

    # Buttons
    global search_button, clear_buttom, exit_button 
    search_button = customtkinter.CTkButton(master=bottom_frame, text='Search', command=search)
    search_button.pack(pady=6)
    clear_button = customtkinter.CTkButton(master=bottom_frame, text='Clear', command=clear)
    clear_button.pack(pady=6)
    exit_button = customtkinter.CTkButton(master=bottom_frame, text='Exit', command=exit_app)
    exit_button.pack(pady=6, side='bottom')

    # TextBox
    global my_textbox
    my_textbox = customtkinter.CTkTextbox(master=left_frame, width=350, height=550, font=('Helvetica', 25), text_color='black', fg_color='white')
    my_textbox.place(relx = 0.5, rely = 0.5, anchor = 'center')

    # ------------------------------------------------------

    root.mainloop()

def search():

    try:
        pokemon = get_pokemon(my_entry.get().lower())
    except:
        clear()
        my_textbox.insert("0.0", f"Ese Pokemon no existe.")
        return

    my_textbox.delete("0.0","end")
    my_textbox.insert("0.0", pokemon.get_info())

    # Image Widget Update 
    my_image = customtkinter.CTkImage(light_image=Image.open(BytesIO(pokemon.image)), size=(310, 310))
    my_label.configure(image=my_image)

def clear():

    my_textbox.delete("0.0","end")
    my_label.configure(image=None)

def exit_app():
    exit()