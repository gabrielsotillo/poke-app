import customtkinter
from PIL import Image
from io import BytesIO

def run_GUI(img_data):

    # Root creation and config
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('blue')
    root = customtkinter.CTk()
    root.geometry('500x350')

    # Widgets
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    # Testing this codelines
    my_image = customtkinter.CTkImage(light_image=Image.open(BytesIO(img_data)), size=(300, 300))
    
    my_label = customtkinter.CTkLabel(master=frame, text='', image=my_image)
    my_label.pack(pady=10)


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

def login():
    print('Test')