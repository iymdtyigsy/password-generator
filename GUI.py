import tkinter
import customtkinter as ctk
import PIL as pil
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
    
        #root = ctk.CTk()
        self.title("Password generator")
        self.geometry("700x500")
        self.minsize(700, 500)
        self.maxsize(700, 500)    

        #functions
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

    #labels
        self.MainMenu_label = ctk.CTkLabel(self,
                                    text = "Password generator",
                                    text_color = "white",
                                    fg_color = "#01a6f8",
                                    width = 200,
                                    height = 25,
                                    font=("Bold", 20),
                                    corner_radius = 5)
        self.MainMenu_label.pack(padx = 10,
                            pady = 10)

        #Frames
        self.MainMenu_sideFrame1 = ctk.CTkFrame(self, 
                                        fg_color ="gray")
        self.MainMenu_sideFrame1.pack(side = "right", 
                                padx = 20, 
                                pady = 20)

        self.MainMenu_sideFrame2 = ctk.CTkFrame(self, 
                                        fg_color ="gray")
        self.MainMenu_sideFrame2.pack(side = "right", 
                                padx = 10, 
                                pady = 10)

        self.MainMenu_Mainframe = ctk.CTkFrame(self,
                                        fg_color ="gray",
                                        width = 500)
        self.MainMenu_Mainframe.pack(side = "left",
                                padx = 20,
                                pady = 20,
                                fill = "both")
                                            
        self.MainFrame_QuestionLable = ctk.CTkLabel(self.MainMenu_Mainframe,
                                            text = "questions",
                                            text_color = "black",
                                            fg_color = "white",
                                            font = ("Bold", 20),
                                            width = 500,
                                            height = 50,
                                            corner_radius= 5)
        self.MainFrame_QuestionLable.pack(side = "top",
                                    padx = 10,
                                    pady = 10)
                                            
        #buttons
        self.randompass_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                    text="random password", 
                                    command=randompass)
        self.randompass_btn.pack(pady = 10, 
                            padx = 10)

        self.start_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                text="start", 
                                command=start)
        self.start_btn.pack(pady = 10, 
                    padx = 10)

        self.quit_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                text="quit", 
                                command=quit)
        self.quit_btn.pack(pady = 10, 
                    padx = 10)

        self.tutorial_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                    text="tutorial", 
                                    command=tutorial)
        self.tutorial_btn.pack(pady = 10, 
                        padx = 10)

        self.copy_btn = ctk.CTkButton(self.MainMenu_sideFrame2, 
                                text="copy", 
                                command=copy,
                                width = 10)
        self.copy_btn.pack(pady = 5,
                    padx = 5)

        self.enter_btn = ctk.CTkButton(self.MainMenu_sideFrame2, 
                                text="Enter", 
                                command=enter,
                                width = 10)
        self.enter_btn.pack(pady = 5, 
                    padx = 5)



app = App()
app.mainloop()