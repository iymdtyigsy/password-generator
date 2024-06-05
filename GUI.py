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
randompass_btn.pack(pady = 10)

start_btn = ctk.CTkButton(root, text="start", command=start)
start_btn.pack(pady = 10)

quit_btn = ctk.CTkButton(root, text="quit", command=quit)
quit_btn.pack(pady = 10)

tutorial_btn = ctk.CTkButton(root, text="tutorial", command=tutorial)
tutorial_btn.pack(pady = 10)

enter_btn = ctk.CTkButton(root, text="Enter", command=enter)
enter_btn.pack(pady = 10)

copy_btn = ctk.CTkButton(root, text="copy", command=copy)
copy_btn.pack(pady = 10)

MainMenu_Frame = ctk.CTkFrame(master= root, fg_color="light gray")
MainMenu_Frame.pack(side = "top", padx = 10, pady = 10)



root.mainloop()