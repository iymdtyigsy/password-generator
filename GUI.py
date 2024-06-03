import customtkinter as ctk
import PIL as pil
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 
root = ctk.CTk()
root.geometry("700x500")

def randompass():
    pass

def start():
    pass

def quit():
    pass

def tutorial():
    pass

def enter():
    pass

def copy():
    pass

randompass_btn = ctk.CTkButton(root, text="random password", command=randompass)
start_btn = ctk.CTkButton(root, text="start", command=start)
quit_btn = ctk.CTkButton(root, text="quit", command=quit)
tutorial_btn = ctk.CTkButton(root, text="tutorial", command=tutorial)
enter_btn = ctk.CTkButton(root, text="Enter", command=enter)
copy_btn = ctk.CTkButton(root, text="copy", command=copy)

copy_btn.pack(pady = 80)
enter_btn.pack(pady = 80)
tutorial_btn.pack(pady = 80)
quit_btn.pack(pady = 80)
randompass_btn.pack(pady = 80)
start_btn.pack(pady = 80)


root.mainloop()