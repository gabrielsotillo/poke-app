import customtkinter
from commands import *


def run_GUI():

    # ------ Root creation and config ------
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('blue')
    root = customtkinter.CTk()
    root.geometry('500x400')
    root.title('PokeDex')

    # ---------------------- Widgets ----------------------
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    # Label
    global my_label 
    my_label = customtkinter.CTkLabel(master=frame, text='', height=150)
    my_label.pack(pady=10)

    # Entry
    global my_entry 
    my_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Pokemon')
    my_entry.pack(pady=12, padx=80)

    # Buttons
    global search_button, exit_button 
    search_button = customtkinter.CTkButton(master=frame, text='Search', command=get_pokemon)
    search_button.pack(pady=12, padx=10)
    exit_button = customtkinter.CTkButton(master=frame, text='Exit', command=exit_app)
    exit_button.pack(pady=12, padx=10)
    # ------------------------------------------------------

    root.mainloop()



'''
    label = customtkinter.CTkLabel(master=frame, text='Login System', font=('Roboto', 25))
    label.pack(pady=12, padx=18)

    entry_1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
    entry_1.pack(pady=12, padx=80)

    entry_2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
    entry_2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text='Login', command=login)
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text='Remember me')
    checkbox.pack(pady=12, padx=10)

'''

