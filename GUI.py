import tkinter as tk
import customtkinter as ctk
import PIL as pil
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

'''class App(ctk.CTk):
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
            self.answer_entry.configure(state="disabled")
            print(self.answer_entry.get())           

        def copy():
            pass

        def clear():
            self.answer_entry.configure(state="normal")
            self.answer_entry.delete(0, tk.END)
        
        self.MainMenuFrame = ctk.CTkFrame(self, 
                                     fg_color="black",
                                     width=700,
                                     height=500)
        self.MainMenuFrame.pack(fill="both", expand=True)

        self.MainMenu_label = ctk.CTkLabel(self.MainMenuFrame,
                                    text="Password generator",
                                    text_color="white",
                                    fg_color="#01a6f8",
                                    width=200,
                                    height=25,
                                    font=("Bold", 20),
                                    corner_radius=5)
        self.MainMenu_label.pack(padx=10,
                                 pady=10)

        #Frames
        self.MainMenu_sideFrame1 = ctk.CTkFrame(self.MainMenuFrame, 
                                                fg_color="gray")
        self.MainMenu_sideFrame1.pack(side="right", 
                                padx=20, 
                                pady=20)

        self.MainMenu_sideFrame2 = ctk.CTkFrame(self.MainMenuFrame, 
                                                fg_color="gray")
        self.MainMenu_sideFrame2.pack(side="right", 
                                padx=10, 
                                pady=10)

        self.MainMenu_Mainframe = ctk.CTkFrame(self.MainMenuFrame,
                                               fg_color="gray",)
        self.MainMenu_Mainframe.pack(side="left",
                                padx=20,
                                pady=20)
        
        self.MainFrame_QuestionLable = ctk.CTkLabel(self.MainMenu_Mainframe,
                                                    text="questions",
                                                    text_color="black",
                                                    fg_color="white",
                                                    font=("Bold", 20),
                                                    width=500,
                                                    height=50,
                                                    corner_radius=5)
        self.MainFrame_QuestionLable.pack(padx=10,
                                          pady=10)
        
        #Entry
        self.answer_entry = ctk.CTkEntry(self.MainMenu_Mainframe,
                                         placeholder_text="enter your response",
                                         width= 500)
        self.answer_entry.pack(pady=5,
                               padx=5) 

        self.Mainframe_passwordlabel = ctk.CTkLabel(self.MainMenu_Mainframe,
                                                    text="password",
                                                    text_color="black",
                                                    fg_color="white",
                                                    width=500,
                                                    height=30,
                                                    corner_radius=5)
        self.Mainframe_passwordlabel.pack(pady=10,
                                          padx=10)
        
        self.Mainframe_passwordstrength = ctk.CTkProgressBar(
                                            self.MainMenu_Mainframe,)
        self.Mainframe_passwordstrength.pack(pady=10,
                                             padx=10)
                                            
        #buttons
        self.randompass_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                            text="random password", 
                                            command=randompass)
        self.randompass_btn.pack(pady=10, 
                                 padx=10)

        self.start_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                       text="start", 
                                       command=start)
        self.start_btn.pack(pady=10, 
                            padx=10)

        self.quit_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="quit", 
                                      command=quit)
        self.quit_btn.pack(pady=10, 
                           padx=10)

        self.tutorial_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                          text="tutorial", 
                                          command=tutorial)
        self.tutorial_btn.pack(pady=10, 
                               padx=10)

        self.copy_btn = ctk.CTkButton(self.MainMenu_sideFrame2, 
                                      text="Copy", 
                                      command=copy,
                                      width=10)
        self.copy_btn.pack(pady=5,
                           padx=5)

        self.enter_btn = ctk.CTkButton(self.MainMenu_sideFrame2, 
                                       text="Enter", 
                                       command=enter,
                                       width=10)
        self.enter_btn.pack(pady=5, 
                            padx=5)

        self.clear_btn = ctk.CTkButton(self.MainMenu_sideFrame2,
                                       text="Clear",
                                       command=clear,
                                       width=10)
        self.clear_btn.pack(pady=5, 
                            padx=5)
        
        self.randpasswordFrame = ctk.CTkFrame(self)

app = App() 
app.mainloop()
'''

class MainMenuWindow(ctk.CTk):
    def __init__(self, parent):
        super().__init__(parent)
        MainMenuMainFrame = ctk.CTkFrame(self, 
                                        fg_color="black",
                                        width=700,
                                        height=500)
        MainMenuMainFrame.pack(padx=10, pady=10)
        Label = ctk.CTkLabel(MainMenuMainFrame, text="password generator")
        Label.pack(padx=5, pady=5)

class randompassWindow(ctk.CTk):
    def __init__(self, parent):
        super().__init__(parent)
        randpasMainFrame = ctk.CTkFrame(self,
                                        fg_color="black",
                                        width=700,
                                        height=500)
        randpasMainFrame.pack(padx=10, pady=10)
        Label = ctk.CTkLabel(randpasMainFrame, text="Random Password")
        Label.pack(padx=5, pady=5)

class tutorWindow(ctk.CTk):
    def __init__(self, parent):
        super().__init__(parent)
        tutorMainFrame = ctk.CTkFrame(self,
                                      fg_color="black",
                                      width=700,
                                      height=500)
        tutorMainFrame.pack(padx=10, pady=10)
        Label = ctk.CTkLabel(tutorMainFrame, text="Tutorial")
        Label.pack(padx=5, pady=5)

class MainWindow():
    def __init__(self, master):
        MainFrame = ctk.CTkFrame(master)
        MainFrame.pack(padx=10, pady=10, fill="both", expand=True)
        self_index = 0

        self.framelist = [MainMenuWindow(MainFrame), 
                          randompassWindow(MainFrame),
                          tutorWindow(MainFrame)]
        
        MainWindowSideFrame = ctk.CTkFrame(master, 
                                           fg_color="gray")
        MainWindowSideFrame.pack(side="right", 
                                 fill="both",
                                 expand=True,
                                 padx=10,
                                 pady=10)
        
        randompass_btn = ctk.CTkButton(MainWindowSideFrame, 
                                       text="random password", 
                                       command=randompass)
        randompass_btn.pack(pady=10, padx=10)
        tutorial_btn = ctk.CTkButton(MainWindowSideFrame, 
                                     text="tutorial", 
                                     command=tutorial)
        tutorial_btn.pack(pady=10, padx=10)

        def randompass(self):
            self.framelist[self_index].forget()
            

app = ctk.CTk()
Mainwindow = MainWindow(app)
app.mainloop()