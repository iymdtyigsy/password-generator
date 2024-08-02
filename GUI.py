import tkinter as tk
import customtkinter as ctk
import random as rand
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class Mainwindow(ctk.CTk):

    questionlist = [
    "What's your favorite animal?",
    "Which celebrity would you choose for your best friend?",
    """If you could only wear one color for the rest of your life, 
    which one would you choose?""",
    "What’s your favorite place to visit?",
    "What is the worst food of all time?",
    "What is your favourite food of all time?",
    "What’s something you’re really good at?",
    "What’s your dream car?",
    "What's your favorite movie",
    "What was your favorite subject in school?",
    "What do you enjoy doing in your free time?",
    "What is your hobby or one of your hobbies?",
    ]

    CurrentClone = None
    def GetStartQuestions(self, clone):
        if clone == None:
            clone = self.questionlist.copy()
        return clone

    def ResetStartQuestions(self, clone):
        clone = None

    def GetRandQuesiton(self):
        questions_list = self.GetStartQuestions(self.CurrentClone)
        index = rand.randrange(1, len(questions_list))
        question = questions_list[index]
        self.questionlist.pop(index)
        return question
        
    NumberOfQuestionAsked = 0

    def CheckNumQuestionAsked(self, check):
        if check == 3:
            True
        else:
            False            

    def PassgenerateAlgo(self):
        pass 

    def reset(self):
        pass

    def sliding(self, value):
        self.lengthlabel.configure(text=int(value))

    def randompass(self):
        self.delete_current()
        self.loadRandPass()
        
    def start(self):
        self.MainFrame_QuestionLable.configure(text= self.GetRandQuesiton())
        self.start_btn.configure(state = "disabled")
        self.skip_btn.configure(state = "normal")
        self.enter_btn.configure(state = "normal")
        self.NumberOfQuestionAsked + 1

    def restart(self):
        self.MainFrame_QuestionLable.configure(text= "Click start to start." )
        self.start_btn.configure(state = "normal")
        self.skip_btn.configure(state = "disabled")
        self.enter_btn.configure(state = "disabled")
        self.ResetStartQuestions
        self.NumberOfQuestionAsked = 0

    def Return(self):
        self.delete_current()
        self.loadMainFrame()

    def quit(self):
        self.destroy()

    def tutorial(self):
        self.delete_current()
        self.loadtutorial()

    def enter(self):
        CheckNumQuestion = self.CheckNumQuestionAsked(self.NumberOfQuestionAsked)
        print(self.answer_entry.get())
        self.answer_entry.delete(0, tk.END)
        self.MainFrame_QuestionLable.configure(text=self.GetRandQuesiton())
        self.NumberOfQuestionAsked + 1
        if CheckNumQuestion:
            self.enter_btn.configure(state = "disabled")
        else:
            self.enter_btn.configure(state = "normal")
        

    def copy(self):
        pass

    def skip(self):
        self.MainFrame_QuestionLable.configure(text= self.GetRandQuesiton())

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
                                                    text="Click start to start.",
                                                    text_color="black",
                                                    fg_color="white",
                                                    font=("Bold",13),
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
        
        self.restart_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                       text="Restart", 
                                       command=self.restart)
        self.restart_btn.pack(pady=10, 
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
                                       state= "disabled",
                                       width=10)
        self.enter_btn.pack(pady=5, 
                            padx=5)

        self.skip_btn = ctk.CTkButton(self.MainMenu_sideFrame2,
                                       text="Skip",
                                       command=self.skip,
                                       state= "disabled",
                                       width=10)
        self.skip_btn.pack(pady=5, 
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
                                       command=self.generate())
        self.generate_btn.pack(pady=10,padx=10)

        self.copy_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="Copy", 
                                      command=self.copy())
        self.copy_btn.pack(pady=10,padx=10)

        self.reset_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="Reset", 
                                      command=self.reset())
        self.reset_btn.pack(pady=10,padx=10)

        self.tutorial_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                          text="tutorial", 
                                          command=self.tutorial())
        self.tutorial_btn.pack(pady=10,padx=10)

        self.returnbtn = ctk.CTkButton(self.MainMenu_sideFrame1,
                                       text="return",
                                       command=self.Return())
        self.returnbtn.pack(padx=10, pady=10)

        self.quit_btn = ctk.CTkButton(self.MainMenu_sideFrame1, 
                                      text="quit", 
                                      hover_color="brown2",
                                      command=self.quit())
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
    