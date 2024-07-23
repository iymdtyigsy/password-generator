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
"""
class MainMenuWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        MainMenuMainFrame = ctk.CTkFrame(self, 
                                        fg_color="black",
                                        width=700,
                                        height=500)
        MainMenuMainFrame.pack(padx=10, pady=10)
        Label = ctk.CTkLabel(MainMenuMainFrame, text="password generator")
        Label.pack(padx=5, pady=5)

class randompassWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        randpasMainFrame = ctk.CTkFrame(self,
                                        fg_color="black",
                                        width=700,
                                        height=500)
        randpasMainFrame.pack(padx=10, pady=10)
        Label = ctk.CTkLabel(randpasMainFrame, text="Random Password")
        Label.pack(padx=5, pady=5)

class tutorWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        tutorMainFrame = ctk.CTkFrame(self,
                                      fg_color="black",
                                      width=700,
                                      height=500)
        tutorMainFrame.pack(padx=10, pady=10)
        Label = ctk.CTkLabel(tutorMainFrame, text="Tutorial")
        Label.pack(padx=5, pady=5)

class MainWindow():
    def __init__(self):
        MainFrame = ctk.CTkFrame(self)
        MainFrame.pack(padx=10, pady=10, fill="both", expand=True)

        self.framelist = [MainMenuWindow(MainFrame), 
                          randompassWindow(MainFrame),
                          tutorWindow(MainFrame)]
        
        MainWindowSideFrame = ctk.CTkFrame(self, 
                                           fg_color="gray")
        MainWindowSideFrame.pack(side="right", 
                                 fill="both",
                                 expand=True,
                                 padx=10,
                                 pady=10)
        
        randompass_btn = ctk.CTkButton(MainWindowSideFrame, 
                                       text="random password", 
                                       command=self.randompass)
        randompass_btn.pack(pady=10, padx=10)
        tutorial_btn = ctk.CTkButton(MainWindowSideFrame, 
                                     text="tutorial", 
                                     command=self.tutorial)
        tutorial_btn.pack(pady=10, padx=10)

    def tutorial(self):
        pass

    def randompass(self):
        self_index = 0
        self.framelist[self_index].forget()
        self.index=(self.index+1)%len(self.framelist)
        self.framelist[self.index].tkraise()
        self.framelist[self.index].pack(padx=10, pady=10)
            

app = ctk.CTk()
Mainwindow = MainWindow(app)
app.mainloop()
"""
class Mainwindow(ctk.CTk):
    def reset(self):
        pass

    def sliding(self, value):
        self.lengthlabel.configure(text=int(value))

    def randompass(self):
        self.delete_current()
        self.loadRandPass()
        
    def start(self):
        pass
    
    def Return(self):
        self.delete_current()
        self.loadMainFrame()

    def quit(self):
        self.destroy()

    def tutorial(self):
        self.delete_current()
        self.loadtutorial()

    def enter(self):
        self.answer_entry.configure(state="disabled")
        print(self.answer_entry.get())           

    def copy(self):
        pass

    def clear(self):
        self.answer_entry.configure(state="normal")
        self.answer_entry.delete(0, tk.END)

    def generate(self):
        pass

    def delete_current(self):
        for widget in self.MainFrameHolder.winfo_children():
            widget.forget()

    def __init__(self):
        super().__init__()
    
        #root = ctk.CTk()
        self.title("Password generator")
        self.geometry("700x500")
        self.minsize(700, 500)
        self.maxsize(700, 500)

        self.MainFrame = ctk.CTkFrame(self, 
                                     fg_color="black",
                                     width=700,
                                     height=500)
        self.MainFrame.pack(fill="both", expand=True)

        self.MainFrame_label = ctk.CTkLabel(self.MainFrame,
                                    text="Password generator",
                                    text_color="white",
                                    fg_color="#01a6f8",
                                    width=200,
                                    height=25,
                                    font=("Bold", 20),
                                    corner_radius=5)
        self.MainFrame_label.pack(padx=10,
                                 pady=10)
        
        self.MainFrameHolder = ctk.CTkFrame(self.MainFrame,
                                            width=600,
                                            height=400)
        self.MainFrameHolder.pack(padx=10, pady=10, fill="both", expand=True)

        self.loadMainFrame()

        


    def loadMainFrame(self):
        #Frames
        self.MainMenu_sideFrame1 = ctk.CTkFrame(self.MainFrameHolder, 
                                                fg_color="gray")
        self.MainMenu_sideFrame1.pack(side="right", 
                                padx=20, 
                                pady=20)

        self.MainMenu_sideFrame2 = ctk.CTkFrame(self.MainFrameHolder, 
                                                fg_color="gray")
        self.MainMenu_sideFrame2.pack(side="right", 
                                padx=10, 
                                pady=10)

        self.MainMenu_Mainframe = ctk.CTkFrame(self.MainFrameHolder,
                                               fg_color="gray",)
        self.MainMenu_Mainframe.pack(side="left",
                                padx=20,
                                pady=20)
        
        self.MainFrame_QuestionLable = ctk.CTkLabel(self.MainMenu_Mainframe,
                                                    text="questions",
                                                    text_color="black",
                                                    fg_color="white",
                                                    font=("Bold",18),
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
                                            command=self.randompass)
        self.randompass_btn.pack(pady=10, 
                                 padx=10)

        self.start_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                       text="start", 
                                       command=self.start)
        self.start_btn.pack(pady=10, 
                            padx=10)

        self.quit_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="quit",
                                      hover_color="brown2", 
                                      command=self.quit)
        self.quit_btn.pack(pady=10, 
                           padx=10)

        self.tutorial_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                          text="tutorial", 
                                          command=self.tutorial)
        self.tutorial_btn.pack(pady=10, 
                               padx=10)

        self.copy_btn = ctk.CTkButton(self.MainMenu_sideFrame2, 
                                      text="Copy", 
                                      command=self.copy,
                                      width=10)
        self.copy_btn.pack(pady=5,
                           padx=5)

        self.enter_btn = ctk.CTkButton(self.MainMenu_sideFrame2, 
                                       text="Enter", 
                                       command=self.enter,
                                       width=10)
        self.enter_btn.pack(pady=5, 
                            padx=5)

        self.clear_btn = ctk.CTkButton(self.MainMenu_sideFrame2,
                                       text="Clear",
                                       command=self.clear,
                                       width=10)
        self.clear_btn.pack(pady=5, 
                            padx=5)
        
        

    def loadRandPass(self):
        self.MainMenu_sideFrame1 = ctk.CTkFrame(self.MainFrameHolder, 
                                                fg_color="light gray")
        self.MainMenu_sideFrame1.pack(side="right", padx=10, pady=10)

        self.MainMenu_Mainframe = ctk.CTkFrame(self.MainFrameHolder,
                                               fg_color="light grey",)
        self.MainMenu_Mainframe.pack(side="left", padx=10, pady=10)

        self.MainMenu_MainframeFir = ctk.CTkFrame(self.MainMenu_Mainframe,
                                               fg_color="gray",)
        self.MainMenu_MainframeFir.pack(padx=10, pady=10)
        
        self.MainMenu_MainframeSEC = ctk.CTkFrame(self.MainMenu_Mainframe,
                                                  fg_color="gray")
        self.MainMenu_MainframeSEC.pack(padx=10, pady=10)

        self.SECframeSector1 =ctk.CTkFrame(self.MainMenu_MainframeSEC,
                                           fg_color="gray")
        self.SECframeSector1.pack(padx=10, pady=10)

        self.SECframeSector2 =ctk.CTkFrame(self.MainMenu_MainframeSEC,
                                           fg_color="gray")
        self.SECframeSector2.pack(padx=10, pady=10)

        self.Mainframe_passwordlabel = ctk.CTkLabel(self.MainMenu_MainframeFir,
                                                    text="password",
                                                    text_color="black",
                                                    fg_color="white",
                                                    width=500,
                                                    height=30,
                                                    corner_radius=5)
        self.Mainframe_passwordlabel.pack(pady=10, padx=10)
        
        self.Mainframe_passwordstrength = ctk.CTkProgressBar(
                                            self.MainMenu_MainframeFir)
        self.Mainframe_passwordstrength.pack(pady=10, padx=10)

        self.passwordlength = ctk.CTkLabel(self.SECframeSector1,
                                           text=("Password Length"))
        self.passwordlength.pack()

        self.Slider = ctk.CTkSlider(self.SECframeSector1, 
                                    from_=0, 
                                    to=50,
                                    command=self.sliding,
                                    height = 20)
        self.Slider.pack(side = "right")

        self.Slider.set(8)
                                            
        #buttons
        self.generate_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                       text="Generate", 
                                       command=self.generate)
        self.generate_btn.pack(pady=10,padx=10)

        self.copy_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="Copy", 
                                      command=self.copy)
        self.copy_btn.pack(pady=10,padx=10)

        self.reset_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="Reset", 
                                      command=self.reset)
        self.reset_btn.pack(pady=10,padx=10)

        self.tutorial_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                          text="tutorial", 
                                          command=self.tutorial)
        self.tutorial_btn.pack(pady=10,padx=10)

        self.returnbtn = ctk.CTkButton(self.MainMenu_sideFrame1,
                                       text="return",
                                       command=self.Return,)
        self.returnbtn.pack(padx=10, pady=10)

        self.quit_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="quit", 
                                      hover_color="brown2",
                                      command=self.quit)
        self.quit_btn.pack(pady=10,padx=10)

        self.lengthlabel = ctk.CTkLabel(self.SECframeSector1,
                                        text=self.Slider.get(),
                                        font=("Helvetica", 15),
                                        fg_color="light gray",
                                        text_color= "black",
                                        corner_radius= 5)
        self.lengthlabel.pack(side ="right")

        checkSymbol = ctk.StringVar(value="off")
        self.checkboxsmb = ctk.CTkCheckBox(self.SECframeSector2,
                                        text="Symbols",
                                        variable=checkSymbol,
                                        onvalue="on",
                                        offvalue="off")
        self.checkboxsmb.pack(pady=5,padx=5)

        checkNumber = ctk.StringVar(value="off")
        self.checkboxnum = ctk.CTkCheckBox(self.SECframeSector2,
                                        text="Numbers",
                                        variable=checkNumber,
                                        onvalue="on",
                                        offvalue="off")
        self.checkboxnum.pack(pady=5,padx=5)

        checkLetters = ctk.StringVar(value="off")
        self.checkboxlet = ctk.CTkCheckBox(self.SECframeSector2,
                                        text="Letters",
                                        variable=checkLetters,
                                        onvalue="on",
                                        offvalue="off")
        self.checkboxlet.pack(pady=5,padx=5)

        checkUp = ctk.StringVar(value="off")
        self.checkboxup = ctk.CTkCheckBox(self.SECframeSector2,
                                        text="Uppercase",
                                        variable=checkUp,
                                        onvalue="on",
                                        offvalue="off")
        self.checkboxup.pack(pady=5,padx=5)

        checkLow = ctk.StringVar(value="off")
        self.checkboxlow = ctk.CTkCheckBox(self.SECframeSector2,
                                        text="Lowercase",
                                        variable=checkLow,
                                        onvalue="on",
                                        offvalue="off")
        self.checkboxlow.pack(pady=5,padx=5)



    def loadtutorial(self):
        self.tutorialFrame = ctk.CTkFrame(self.MainFrameHolder,
                                          fg_color="gray")
        self.tutorialFrame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tutorialFrameSEC = ctk.CTkFrame(self.MainFrameHolder,
                                             fg_color="transparent")
        self.tutorialFrameSEC.pack(side="right",padx=10, pady=10)

        self.returnbtn = ctk.CTkButton(self.tutorialFrameSEC,
                                       text="return",
                                       font=("bold",20),
                                       command=self.Return,
                                       width=30,
                                       height=30)
        self.returnbtn.pack(side="right",padx=10, pady=10)
        
        self.textbox = ctk.CTkTextbox(self.tutorialFrame,
                                      fg_color="gray",
                                      font=("bold", 20)
                                   )
        self.textbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.textbox.insert("0.0", "Tutorial\n\n" + 
        """
        This is tutorial
        """)
        self.textbox.configure(state = ctk.DISABLED)

if __name__ =="__main__":
    Mainwindow().mainloop()
    