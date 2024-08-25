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
    
    def password_generate_by_answer(self, answer):
        has_space = False
        has_empty = False
        answerslist = [str(items) for items in answer]#.replace(' ',"")
        print(answerslist)
        random.shuffle(answerslist)
        print(answerslist)
        between = ''
        self.answers.clear()
        if not answerslist:
            self.check_btn.configure(state = "disabled")
            return None
        
        #return password
        for answer in answerslist:
            if isinstance(answer, str):
                if " " in answer:
                    has_space = True
        if len(answerslist) <3:
            has_empty = True
        
        if has_space:
            return "You answered space in your answer"
        elif has_empty:
            return "You didn't answer a question"
        else:
            # Generate a password based on the answers
            password = between.join(answerslist)+(str(random.randrange(0, 100)))
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
        if any(ord(char) > 127 or not char.isprintable() for char in password):
            return 0, self.split_string(f"password contains unicode or non-printable characters. can't be checked (password length:{str(length)})", 25), 0
        elif len(password) == 0:
            return 0, self.split_string(f"This is an empty password. can't be checked (password length:{str(length)})", 25), 0 
        elif ' ' in password:
            return 0, self.split_string(f"Password contains spaces. can't be checked (password length:{str(length)})", 25), 0
        elif len(set(password)) == 1:  
            return 1, self.split_string(f"Very Weak: Password consist of the same character repeated. (password length:{str(length)}) ", 25), 0.2
        elif length < 8:
            return 1, self.split_string(f"Very Weak: Password needs to be at least 8 characters long. (password length:{str(length)})", 25), 0.2
        elif length >= 8 and length < 15:
            score += 1
        elif length >= 15 and length <25:
            score += 2
        elif length >= 25 and length <=50:
            score += 2
            if re.search(r"[A-Z]", password):
                score += 1
            if re.search(r"[a-z]", password):
                score += 1
            if re.search(r"\d", password):
                score += 1
            if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                score += 1
            if score == 3:
                return 4, self.split_string(f"Good: this is a long password are you sure you can remember it ? (password length:{str(length)})", 25), 0.8
            if score >= 4:
                return 5, self.split_string(f"Strong: this is a long password are you sure you can remember it? (password length:{str(length)})", 25), 1.0
        elif length > 50:
            return 0, self.split_string(f"Password is too long for the program to check. (password length:{str(length)})", 25), 0
        if password in common_password:
            return 1, self.split_string(f"Very Weak: This password is too common. Choose a more unique password. (password length:{str(length)})", 25), 0.2
        if re.search(r"[A-Z]", password):
            score += 1
        if re.search(r"[a-z]", password):
            score += 1
        if re.search(r"\d", password):
            score += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        if score == 1:
            return 2, f"Weak (password length:{str(length)})", 0.4
        elif score == 2:
            return 3, f"Fair (password length:{str(length)})", 0.6
        elif score == 3:
            return 4, f"Good (password length:{str(length)})", 0.8
        elif score >= 4:
            return 5, f"Strong (password length:{str(length)})", 1.0
        
    def Pass_strengthdisplay(self):
        password = self.Mainframe_passwordlabel.cget("text")
        rank, message, progress = self.Pass_strengthcheck(password)
        self.Strength_label.configure(text=f"""
        Password Strength: {message} (Rank: {rank}/5)
        """)
        print(f"""
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
        self.copy_btn.configure(state = "disabled")
        self.check_btn.configure(state = "disabled")
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
            result = self.password_generate_by_answer(self.answers)
            self.MainFrame_QuestionLabel.configure(text = result and "Here is your password" or "You have not entered any answers press restart to restart")
            self.restart_btn.configure(state = "normal")
            self.Mainframe_passwordlabel.configure(text = f"{result or 'You didn’t answer a question'}")
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

    def random_generate(self):
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

        if not character_list and length < 4:
            self.Mainframe_passwordlabelRand.configure(text = "Please select one option and at least a length of 4 characters")
            return ""
        if length < 4:
            self.Mainframe_passwordlabelRand.configure(text=self.split_string("Cannot generate a password for a length of less than 4 characters!", 25))
            return ""
        if not character_list:
            self.Mainframe_passwordlabelRand.configure(text = "Please select at least one character type!")
            return ""
    
        password = []

        if include_numbers:
            password.append(random.choice(numbers))
        if include_symbols:
            password.append(random.choice(symbols))
        if include_lowercase:
           password.append(random.choice(lowercase))
        if include_uppercase:
           password.append(random.choice(uppercase))
        
        while len(password) < length:
           password.append(random.choice(character_list))

        random.shuffle(password)

        password = ''.join(password)

        self.Mainframe_passwordlabelRand.configure(text=password)
        self.copy_btn.configure(state = "normal")
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

        self.Mainframe_passwordstrength = ctk.CTkProgressBar(self.MainMenu_Mainframe, progress_color="")
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

        self.Mainframe_passwordstrength = ctk.CTkProgressBar(self.MainMenu_MainframeFir, progress_color="")
        self.Mainframe_passwordstrength.set(0)
        self.Mainframe_passwordstrength.pack(pady=10, padx=10)

        self.passwordlength = ctk.CTkLabel(self.SECframeSector1,text=("Password Length"))
        self.passwordlength.pack()

        self.Slider = ctk.CTkSlider(self.SECframeSector1, from_=0, to=50,command=self.sliding,height = 20,)
        self.Slider.pack(side = "right")

        self.Slider.set(8)
                                            
        #buttons

        self.generate_btn = ctk.CTkButton(self.MainMenu_sideFrame1RAND, text="Generate", command=self.random_generate)
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
        1. Main Menu At Main Menu which is the password generator which generates passwords 
        from the user answering 3 questions. 
        first, you press the Start button on the left-hand side which is labelled Start, 
        and then the program displays the question on the big white label, 
        you enter your answer in the entry box which has "enter your response" on it, 
        then you press the enter button on 
        your left-hand side which has the enter labelled on it (answered 1st time), 
        a new question will appear on the white label and 
        you then enter your answers again (answered 2nd time) as the process before, 
        for totally three times afterwards including the two times. 
        so the next time you answer the question will be the third time. 
        the program will then display the password in the white label below the entry box.

        you can copy the password by pressing the copy button, 
        and check the password strength by pressing the check button. 
        when the check button is pressed a message describing the strength of 
        the password will display under the white label with the password in it. 
        the colour of the progress bar represents different strengths of the password 
        (red = very weak, orange = weak, yellow = fair, lime green = strong, green = very strong) 
        and the progress of the bar increases as the strength of the bar is increased.
        you can also skip questions by pressing the skip button on your left 
        press restart to restart the process of answering questions to generate a password. 
        tutorial buttons send you to the tutorial menu here. return button returns to the main menu. 
        quit button ends the program. 

        2. random password - press random password to go to the random password menu 
        at random password you can generate a password by 
        selecting the types of characters you want in your password 
        by ticking the boxes and selecting the length by sliding the slider. 
        press generate after you have selected your options for the characters, 
        you want in the password and after you have selected your length from the slider. 
        copy button copies the password generated. check button checks the password strength. 
        reset button resets to the default setting for 
        the options of type character and the password length. 
        tutorial buttons send you to the tutorial menu here. 
        return button returns to the main menu. 
        quit button ends the program. 

        3. Grey-out buttons are disabled 
        which means you can't press them 
        sometimes buttons are not disabled properly 
        so keep it in mind and 
        you can reset or restart to redo the password-generating process for the best functionality. 
        Usually the copy and the check button that is not disabled properly
   
        """)
        self.textbox.configure(state = ctk.DISABLED)

if __name__ =="__main__":
    Mainwindow().mainloop()