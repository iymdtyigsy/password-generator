import tkinter as tk
import customtkinter as ctk
import random
import copy
import string
import re
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
    answers = []
    NumberOfQuestionAsked = 0

    CurrentClone = None
    def GetStartQuestions(self):
        self.CurrentClone = copy.deepcopy(self.questionlist)
        return self.CurrentClone

    def ResetStartQuestions(self):
        self.CurrentClone = None

    def GetRandQuesiton(self):
        questions_list = self.GetStartQuestions()

        if len(questions_list) > 1:
            index = random.randrange(1, len(questions_list))
        else:
            index = 0

        question = questions_list[index]
        self.CurrentClone.pop(index)
        return question

        #index = random.randint(0, len(questions_list)-1)
        #question = questions_list[index]
        #self.CurrentClone.pop(index)
        #return question

    def CheckNumQuestionAsked(self, check):
        return check == 3          
    
    def PassgenerateAlgo(self, answer):
        answerslist = [str(items).replace(' ',"") for items in answer]
        random.shuffle(answerslist)
        between = ''
        password = between.join(answerslist)+(str(random.randrange(1, 100)))
        self.answers.clear()
        if not answerslist:
            self.check_btn.configure(state = "disabled")
            return None
        return password
    
    def split_string(self, string: str, max_characters: int):
        lines = []
        current_line = ""

        for word in string.split():
            if len(current_line) + len(word) + 1 <= max_characters:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "
    
        if current_line:
            lines.append(current_line.strip())

        return '\n'.join(lines)
    
    def Pass_strengthcheck(self, password):

        length = len(password)
            
        with open("common.txt","r") as f:
            common_password = f.read().splitlines()

        score = 0

        if length < 8:
            return 1, self.split_string("Very Weak: Password must be at least 8 characters long.", 20), 0.2
        
        elif length >= 8 and length < 12:
            score += 1

        elif length >= 12:
            score += 2

        if password in common_password:
            return 1, self.split_string("Very Weak: This password is too common. Choose a more unique password.", 20), 0.2

        if re.search(r"[A-Z]", password):
            score += 1

        if re.search(r"[a-z]", password):
            score += 1

        if re.search(r"\d", password):
            score += 1

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1

        if score == 1:
            return 2, "Weak", 0.4
        elif score == 2:
            return 3, "Fair", 0.6
        elif score == 3:
            return 4, "Good", 0.8
        elif score >= 4:
            return 5, "Strong", 1.0
    
    def Pass_strengthdisplay(self):
        password = self.Mainframe_passwordlabel.cget("text")
        rank, message, progress = self.Pass_strengthcheck(password)
        self.Strength_label.configure(text=f"""
        Password Strength: {message} (Rank: {rank}/5)
        """)
        self.Mainframe_passwordstrength.set(progress)
        if rank == 1:
            self.Mainframe_passwordstrength.configure(progress_color="red")
        elif rank == 2:
            self.Mainframe_passwordstrength.configure(progress_color="orange")
        elif rank == 3:
            self.Mainframe_passwordstrength.configure(progress_color="yellow")
        elif rank == 4:
            self.Mainframe_passwordstrength.configure(progress_color="lightgreen")
        elif rank == 5:
            self.Mainframe_passwordstrength.configure(progress_color="green")
        self.check_btn.configure(state = "disabled")
    
    def RandPass_strengthdisplay(self):
        password = self.Mainframe_passwordlabelRand.cget("text")
        rank, message, progress = self.Pass_strengthcheck(password)
        self.Strength_label.configure(text=f"""
        Password Strength: {message} (Rank: {rank}/5)
        """)
        self.Mainframe_passwordstrength.set(progress)
        if rank == 1:
            self.Mainframe_passwordstrength.configure(progress_color="red")
        elif rank == 2:
            self.Mainframe_passwordstrength.configure(progress_color="orange")
        elif rank == 3:
            self.Mainframe_passwordstrength.configure(progress_color="yellow")
        elif rank == 4:
            self.Mainframe_passwordstrength.configure(progress_color="lightgreen")
        elif rank == 5:
            self.Mainframe_passwordstrength.configure(progress_color="green")
        self.check_btn.configure(state = "disabled")

    def reset(self):
        self.Mainframe_passwordlabelRand.configure(text="")
        self.Slider.set(8)
        self.lengthlabel.configure(text = "8")
        self.checkboxnum.deselect()
        self.checkboxsmb.deselect()
        self.checkboxlow.deselect()
        self.checkboxup.deselect()
        self.copy_btn
        self.Strength_label.configure(text = "")
        self.Mainframe_passwordstrength.set(0)
        self.Mainframe_passwordstrength.configure(progress_color="")

    def sliding(self, value):
        self.lengthlabel.configure(text=int(value))

    def randompass(self):
        self.delete_current()
        self.loadRandPass()
        
    def start(self):
        self.MainFrame_QuestionLabel.configure(text= self.split_string(self.GetRandQuesiton(), 20))
        self.start_btn.configure(state = "disabled")
        self.enter_btn.configure(state = "normal")
        self.skip_btn.configure(state = "normal")
        self.NumberOfQuestionAsked += 1

    def restart(self):
        self.MainFrame_QuestionLabel.configure(text= "Click start to start." )
        self.start_btn.configure(state = "normal")
        self.enter_btn.configure(state = "disabled")
        self.skip_btn.configure(state = "disabled")
        self.enter_btn.configure(state = "disabled")
        self.check_btn.configure(state = "disabled")
        self.restart_btn.configure(state = "disabled")
        self.Strength_label.configure(text = "")
        self.Mainframe_passwordstrength.set(0)
        self.Mainframe_passwordstrength.configure(progress_color="")
        self.ResetStartQuestions()
        self.Mainframe_passwordlabel.configure(text = "")
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
        if len(self.answer_entry.get()) != 0:
            self.answers.append(self.answer_entry.get())
        self.answer_entry.delete(0, tk.END)
        self.MainFrame_QuestionLabel.configure(text=self.GetRandQuesiton())
        self.NumberOfQuestionAsked += 1
        self.enter_btn.configure(state = CheckNumQuestion and "disabled" or "normal" )
        self.skip_btn.configure(state = CheckNumQuestion and "disabled" or "normal")
        if CheckNumQuestion:
            result = self.PassgenerateAlgo(self.answers)
            self.MainFrame_QuestionLabel.configure(text = result and "Here is your password" or "You have not entered any answers press restart to restart")
            self.restart_btn.configure(state = "normal")
            self.Mainframe_passwordlabel.configure(text = f"{result or ''}")
            self.check_btn.configure(state = "normal")
            self.copy_btn.configure(state = "normal")
            if not result:
                self.check_btn.configure(state = "disabled")
                self.copy_btn.configure(state = "disabled")
            
    def copy(self):
        password = self.Mainframe_passwordlabel.cget("text")
        self.clipboard_clear()
        self.clipboard_append(password)
        self.copy_btn.configure(state = "disabled")

    def copyRand(self):
        password = self.Mainframe_passwordlabelRand.cget("text")
        self.clipboard_clear()
        self.clipboard_append(password)
        self.copy_btn.configure(state = "disabled")

    def skip(self):
        self.MainFrame_QuestionLabel.configure(text= self.GetRandQuesiton())
        if self.GetRandQuesiton() == None:
            self.ResetStartQuestions()
            self.MainFrame_QuestionLabel.configure(text= self.GetRandQuesiton())

    def generate(self):
        character_list = []
        
        length = int(self.Slider.get())
        
        include_numbers = self.checkboxnum.get() == "on"
        include_symbols = self.checkboxsmb.get() == "on"
        include_lowercase = self.checkboxlow.get() == "on"
        include_uppercase = self.checkboxup.get() == "on"

        numbers = string.digits
        symbols = string.punctuation
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase

        if include_numbers:
            character_list.extend(numbers)
        if include_symbols:
            character_list.extend(symbols)
        if include_lowercase:
            character_list.extend(lowercase)
        if include_uppercase:
            character_list.extend(uppercase)

        if not character_list:
            self.Mainframe_passwordlabelRand.configure(text = "Please select at least one character type!")
            return ""

        password = ''.join(random.choice(character_list) for _ in range(length))

        self.copy_btn.configure(state = "normal")
        self.Mainframe_passwordlabelRand.configure(text=password)
        self.check_btn.configure(state = "normal")

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

        self.MainFrame = ctk.CTkFrame(self, fg_color="black",width=700,height=500)
        self.MainFrame.pack(fill="both", expand=True)

        self.MainFrame_label = ctk.CTkLabel(self.MainFrame,text="Password generator",text_color="white",fg_color="#01a6f8",width=200,height=25,font=("Bold", 20),corner_radius=5)
        self.MainFrame_label.pack(padx=10,pady=10)
        
        self.MainFrameHolder = ctk.CTkFrame(self.MainFrame,width=600,height=400)
        self.MainFrameHolder.pack(padx=10, pady=10, fill="both", expand=True)

        self.loadMainFrame()

    def loadMainFrame(self):
        #Frames
        self.MainMenu_sideFrame1 = ctk.CTkFrame(self.MainFrameHolder, fg_color="gray")
        self.MainMenu_sideFrame1.pack(side="right", padx=20, pady=20)

        self.MainMenu_sideFrame2 = ctk.CTkFrame(self.MainFrameHolder, fg_color="gray")
        self.MainMenu_sideFrame2.pack(side="right", padx=10, pady=10)

        self.MainMenu_Mainframe = ctk.CTkFrame(self.MainFrameHolder,fg_color="gray",)
        self.MainMenu_Mainframe.pack(side="left",padx=20,pady=20)
        
        self.MainFrame_QuestionLabel = ctk.CTkLabel(self.MainMenu_Mainframe,text="Click start to start.",text_color="black",fg_color="white",width=500,height=50,corner_radius=5)
        self.MainFrame_QuestionLabel.pack(padx=10,pady=10)
        
        #Entry
        self.answer_entry = ctk.CTkEntry(self.MainMenu_Mainframe,placeholder_text="enter your response",width= 500)
        self.answer_entry.pack(pady=5,padx=5) 

        self.Mainframe_passwordlabel = ctk.CTkLabel(self.MainMenu_Mainframe,text="",text_color="black",fg_color="white",width=500,height=30,corner_radius=5)
        self.Mainframe_passwordlabel.pack(pady=10,padx=10)
        

        self.Strength_label = ctk.CTkLabel(self.MainMenu_Mainframe, text="")
        self.Strength_label.pack(pady=10)

        self.Mainframe_passwordstrength = ctk.CTkProgressBar(self.MainMenu_Mainframe,)
        self.Mainframe_passwordstrength.set(0)
        self.Mainframe_passwordstrength.pack(pady=10,padx=10)
                                            
        #buttons
        self.randompass_btn = ctk.CTkButton(self.MainMenu_sideFrame1, text="random password", command=self.randompass)
        self.randompass_btn.pack(pady=10, padx=10)

        self.start_btn = ctk.CTkButton(self.MainMenu_sideFrame1, text="start", command=self.start)
        self.start_btn.pack(pady=10, padx=10)
        
        self.restart_btn = ctk.CTkButton(self.MainMenu_sideFrame1, text="Restart",command=self.restart, state= "disabled")
        self.restart_btn.pack(pady=10, padx=10)

        self.quit_btn = ctk.CTkButton(self.MainMenu_sideFrame1, text="quit",hover_color="brown2", command=self.quit)
        self.quit_btn.pack(pady=10, padx=10)

        self.tutorial_btn = ctk.CTkButton(self.MainMenu_sideFrame1, text="tutorial", command=self.tutorial)
        self.tutorial_btn.pack(pady=10, padx=10)

        self.copy_btn = ctk.CTkButton(self.MainMenu_sideFrame2, text="Copy",state="disabled", command=self.copy,width=10)
        self.copy_btn.pack(pady=5,padx=5)

        self.enter_btn = ctk.CTkButton(self.MainMenu_sideFrame2, text="Enter",command=self.enter,state= "disabled",width=10)
        self.enter_btn.pack(pady=5, padx=5)

        self.skip_btn = ctk.CTkButton(self.MainMenu_sideFrame2, text="Skip", command=self.skip, state= "disabled", width=10)
        self.skip_btn.pack(pady=5, padx=5)
        
        self.check_btn = ctk.CTkButton(self.MainMenu_sideFrame2, text="Check", command=self.Pass_strengthdisplay, state = "disabled", width=10)
        self.check_btn.pack(pady=5,padx=5)
        
        

    def loadRandPass(self):

        self.MainMenu_sideFrame1RAND = ctk.CTkFrame(self.MainFrameHolder, fg_color="light gray")
        self.MainMenu_sideFrame1RAND.pack(side="right", padx=10, pady=10)

        self.MainMenu_Mainframe = ctk.CTkFrame(self.MainFrameHolder,fg_color="light grey",)
        self.MainMenu_Mainframe.pack(side="left", padx=10, pady=10)

        self.MainMenu_MainframeFir = ctk.CTkFrame(self.MainMenu_Mainframe,fg_color="gray",)
        self.MainMenu_MainframeFir.pack(padx=10, pady=10)
        
        self.MainMenu_MainframeSEC = ctk.CTkFrame(self.MainMenu_Mainframe,fg_color="gray")
        self.MainMenu_MainframeSEC.pack(padx=10, pady=10)

        self.SECframeSector1 =ctk.CTkFrame(self.MainMenu_MainframeSEC,fg_color="gray")
        self.SECframeSector1.pack(padx=10, pady=10)

        self.SECframeSector2 =ctk.CTkFrame(self.MainMenu_MainframeSEC,fg_color="gray")
        self.SECframeSector2.pack(padx=10, pady=10)

        self.Mainframe_passwordlabelRand = ctk.CTkLabel(self.MainMenu_MainframeFir,text="password",text_color="black",fg_color="white",width=500,height=30,corner_radius=5)
        self.Mainframe_passwordlabelRand.pack(pady=10, padx=10)
        
        self.Strength_label = ctk.CTkLabel(self.MainMenu_MainframeFir, text="")
        self.Strength_label.pack(pady=10)

        self.Mainframe_passwordstrength = ctk.CTkProgressBar(self.MainMenu_MainframeFir)
        self.Mainframe_passwordstrength.set(0)
        self.Mainframe_passwordstrength.pack(pady=10, padx=10)

        self.passwordlength = ctk.CTkLabel(self.SECframeSector1,text=("Password Length"))
        self.passwordlength.pack()

        self.Slider = ctk.CTkSlider(self.SECframeSector1, from_=0, to=50,command=self.sliding,height = 20)
        self.Slider.pack(side = "right")

        self.Slider.set(8)
                                            
        #buttons

        self.generate_btn = ctk.CTkButton(self.MainMenu_sideFrame1RAND, text="Generate", command=self.generate)
        self.generate_btn.pack(pady=10,padx=10)

        self.copy_btn = ctk.CTkButton(self.MainMenu_sideFrame1RAND, text="Copy", command=self.copyRand, state = "disabled")
        self.copy_btn.pack(pady=10,padx=10)

        self.check_btn = ctk.CTkButton(self.MainMenu_sideFrame1RAND, text="Check", command=self.RandPass_strengthdisplay, state = "disabled")
        self.check_btn.pack(pady=5,padx=5)

        self.reset_btn = ctk.CTkButton(self.MainMenu_sideFrame1RAND, text="Reset", command=self.reset)
        self.reset_btn.pack(pady=10,padx=10)

        self.tutorial_btn = ctk.CTkButton(self.MainMenu_sideFrame1RAND, text="tutorial", command=self.tutorial)
        self.tutorial_btn.pack(pady=10,padx=10)

        self.returnbtn = ctk.CTkButton(self.MainMenu_sideFrame1RAND,text="return",command=self.Return)
        self.returnbtn.pack(padx=10, pady=10)

        self.quit_btn = ctk.CTkButton(self.MainMenu_sideFrame1RAND, text="quit", hover_color="brown2",command=self.quit)
        self.quit_btn.pack(pady=10,padx=10)

        self.lengthlabel = ctk.CTkLabel(self.SECframeSector1,text=self.Slider.get(),fg_color="light gray",text_color= "black",corner_radius= 5)
        self.lengthlabel.pack(side ="right")

        checkSymbol = ctk.StringVar(value="off")
        self.checkboxsmb = ctk.CTkCheckBox(self.SECframeSector2,text="Symbols",variable=checkSymbol,onvalue="on",offvalue="off")
        self.checkboxsmb.pack(pady=5,padx=5)

        checkNumber = ctk.StringVar(value="off")
        self.checkboxnum = ctk.CTkCheckBox(self.SECframeSector2,text="Numbers",variable=checkNumber,onvalue="on",offvalue="off")
        self.checkboxnum.pack(pady=5,padx=5)

        checkUp = ctk.StringVar(value="off")
        self.checkboxup = ctk.CTkCheckBox(self.SECframeSector2,text="Uppercase",variable=checkUp,onvalue="on",offvalue="off")
        self.checkboxup.pack(pady=5,padx=5)

        checkLow = ctk.StringVar(value="off")
        self.checkboxlow = ctk.CTkCheckBox(self.SECframeSector2,text="Lowercase",variable=checkLow,onvalue="on",offvalue="off")
        self.checkboxlow.pack(pady=5,padx=5)

    def loadtutorial(self):
        self.tutorialFrame = ctk.CTkFrame(self.MainFrameHolder,fg_color="gray")
        self.tutorialFrame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tutorialFrameSEC = ctk.CTkFrame(self.MainFrameHolder,fg_color="transparent")
        self.tutorialFrameSEC.pack(side="right",padx=10, pady=10)

        self.returnbtn = ctk.CTkButton(self.tutorialFrameSEC,text="return",command=self.Return,width=30,height=30)
        self.returnbtn.pack(side="right",padx=10, pady=10)
        
        self.textbox = ctk.CTkTextbox(self.tutorialFrame,fg_color="gray", font=("Helvetica", 14))
        self.textbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.textbox.insert("0.0", "Tutorial\n\n" + 
        """
        1.Main Menu 
          At Main Menu which is the password generator which generates password from the 
          user answering 3 questions. first you press the Start button on the left hand side 
          which is labeled Start, then the program would display question on the big white label, 
          you enter your answer in the entry box which has "enter your response" on it, 
          then you press the enter button on your left hand side which has the enter 
          labeled on it (answerd 1st time), a new question will appear on the white label and you 
          then enter your answers again (answerd 2nd time) as the process before, for totaly three 
          times afterwards including the two times before. 
          
          so the next time you answers the question will be the third time. 
          the program will then display the password in the white label below the entry box. 
          you can copy the password by pressing copy button, check the password strength 
          by pressing the check button. when the check button is pressed a message 
          describing the strength of the password will display under the white label 
          with the password in it. the colour of the progess bar repersents differnt
          strength of the password (red = very weak, orange = weak, yellow = fair, lime green 
          = strong, green = very strong) and the progess of the bar is increase as the strength 
          of the bar is increased.

        """)
        self.textbox.configure(state = ctk.DISABLED)

if __name__ =="__main__":
    Mainwindow().mainloop()
    