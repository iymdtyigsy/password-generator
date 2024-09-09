"""This program is a password generator that has functions of
   random password generating, 
   password generating from the user answering 3 questions.
"""

import tkinter as tk
import random
import copy
import string
import re

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):
    """Window for the password generator program."""

    question_list = [
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
        "What is your favorite book?",
        "What type of music do you enjoy the most?",
        """If you could travel anywhere in the world, 
        where would you go?""",
        "What’s your favorite movie genre?",
        "What’s a hobby you’d like to pick up?",
        "If you could have any superpower, what would it be?",
        "What would you do if you won the lottery?",
        "If you could meet any historical figure, who would it be?",
        "What would you choose if you could live in any time period?",
        "If you could switch lives with someone for a day, who would it be?"
    ]

    answers = []
    number_of_question_asked = 0
    current_clone = None

    def get_start_questions(self):
        """Getting deepcopy of the questionlist,
           for the question to be chosen to ask.
        """
        self.current_clone = copy.deepcopy(self.question_list)
        return self.current_clone

    def reset_start_questions(self):
        """Reseting the question to ask."""
        self.current_clone = None

    def get_rand_quesiton(self):
        """Getting the random chosen question to ask."""
        questions_list = self.get_start_questions()
        index = random.randint(0, len(questions_list)-1)
        question = questions_list[index]
        self.current_clone.pop(index)
        return question

    def check_numbers_of_question_asked(self, check):
        """Checking the question is answered three times."""
        return check == 3

    def password_generate_by_answer(self, answer):
        """Generating the password from answers."""
        has_space = False
        has_empty = False
        answers_list = [str(items) for items in answer]
        random.shuffle(answers_list)
        between = ""
        self.answers.clear()
        if not answers_list:
            self.check_btn.configure(state="disabled")
            return None

        for answer in answers_list:
            if isinstance(answer, str):
                if " " in answer:
                    has_space = True
        if len(answers_list) < 3:
            has_empty = True

        if has_space:
            return "You answered space in your answer"
        elif has_empty:
            return "You didn't answer a question"
        else:
            password = (
                between.join(answers_list)+(str(random.randrange(0, 100)))
                )

            return password  # return password

    def split_string(self, string: str, max_characters: int):
        """Spliting the strings into lines so it fits in the label."""
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

    def password_strength_check(self, password):
        """checking the strength of the password."""
        length = len(password)

        with open("common.txt", "r") as f:
            common_password = f.read().splitlines()
        score = 0

        # Check if there is a unicode or non printable character in the password
        if any(ord(char) > 127 or not char.isprintable() for char in password):
            return 0, self.split_string(
                f"password contains unicode or"
                "non-printable characters. can't be checked"
                "(password length:{str(length)})", 25), 0

        # Check if the password is empty
        elif len(password) == 0:
            return 0, self.split_string(
                f"This is an empty password."
                "can't be checked (password length:{str(length)})",
                25), 0

        # Check if the password contains space or spaces
        elif ' ' in password:
            return 0, self.split_string(
                f"Password contains spaces. "
                "can't be checked (password length:{str(length)})",
                25), 0

        # Check if the password consist of the same characters repeated
        elif len(set(password)) == 1:
            return 1, self.split_string(
                f"Very Weak: "
                "Password consist of the same character repeated. "
                "(password length:{str(length)}) ",
                25), 0.2

        # Check if the password is less than 8 characters
        elif length < 8:
            return 1, self.split_string(
                f"Very Weak: Password needs to be at "
                "least 8 characters long. (password length:{str(length)})",
                25), 0.2

        elif length >= 8 and length < 15:
            score += 1

        elif length >= 15 and length < 25:
            score += 2

        # Separate checker to check for very long passwords
        elif length >= 25 and length <= 50:
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
                return 4, self.split_string(f"Good: this is a long password "
                                            "are you sure you can remember it ?"
                                            "(password length:{str(length)})",
                                            25), 0.8
            if score >= 4:
                return 5, self.split_string(f"Strong: this is a long password"
                                            "are you sure you can remember it?"
                                            "(password length:{str(length)})",
                                            25), 1.0

        # Check if the password is way too long
        elif length > 50:
            return 0, self.split_string(
                f"Password is too long for the"
                " program to check. (password length:{str(length)})",
                25), 0
        if password in common_password:
            return 1, self.split_string(
                f"Very Weak: This password is too common. "
                "Choose a more unique password. (password length:{str(length)})",
                25), 0.2
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

    def password_strength_display(self):
        """Displaying the strength in label and progess bar."""
        password = self.main_frame_password_label.cget("text")
        rank, message, progress = self.password_strength_check(password)
        self.strength_label.configure(text=f"""
        Password Strength: {message} (Rank: {rank}/5)
        """)
        self.main_frame_password_strength_bar.set(progress)
        if rank == 1:
            self.main_frame_password_strength_bar.configure(
                progress_color="red")
        elif rank == 2:
            self.main_frame_password_strength_bar.configure(
                progress_color="orange")
        elif rank == 3:
            self.main_frame_password_strength_bar.configure(
                progress_color="yellow")
        elif rank == 4:
            self.main_frame_password_strength_bar.configure(
                progress_color="lightgreen")
        elif rank == 5:
            self.main_frame_password_strength_bar.configure(
                progress_color="green")
        self.check_btn.configure(state="disabled")

    def random_password_strength_display(self):
        """Displaying the strength in label and progess bar,
          in random password menu.
          """
        password = self.main_frame_password_label_random.cget("text")
        rank, message, progress = self.password_strength_check(password)
        self.strength_label.configure(
            text=f"""
        Password Strength: {message} (Rank: {rank}/5)
        """)
        self.main_frame_password_strength_bar.set(progress)
        if rank == 1:
            self.main_frame_password_strength_bar.configure(
                progress_color="red")
        elif rank == 2:
            self.main_frame_password_strength_bar.configure(
                progress_color="orange")
        elif rank == 3:
            self.main_frame_password_strength_bar.configure(
                progress_color="yellow")
        elif rank == 4:
            self.main_frame_password_strength_bar.configure(
                progress_color="lightgreen")
        elif rank == 5:
            self.main_frame_password_strength_bar.configure(
                progress_color="green")
        self.check_btn.configure(state="disabled")

    def reset(self):
        """Reseting the random password menu."""
        self.main_frame_password_label_random.configure(text="")
        self.slider.set(8)
        self.lengthlabel.configure(text="8")
        self.checkboxnum.deselect()
        self.checkboxsmb.deselect()
        self.checkboxlow.deselect()
        self.checkboxup.deselect()
        self.copy_btn.configure(state="disabled")
        self.check_btn.configure(state="disabled")
        self.strength_label.configure(text="")
        self.main_frame_password_strength_bar.set(0)
        self.main_frame_password_strength_bar.configure(progress_color="")

    def sliding(self, value):
        """Getting the length of the slider."""
        self.lengthlabel.configure(text=int(value))

    def start(self):
        """Initiate asking questions."""
        self.main_frame_question_label.configure(
            text=self.split_string(self.get_rand_quesiton(), 20)
        )
        self.start_btn.configure(state="disabled")
        self.enter_btn.configure(state="normal")
        self.skip_btn.configure(state="normal")
        self.number_of_question_asked += 1

    def restart(self):
        """Reseting the main menu."""
        self.main_frame_question_label.configure(text="Click start to start.")
        self.start_btn.configure(state="normal")
        self.enter_btn.configure(state="disabled")
        self.skip_btn.configure(state="disabled")
        self.enter_btn.configure(state="disabled")
        self.check_btn.configure(state="disabled")
        self.restart_btn.configure(state="disabled")
        self.strength_label.configure(text="")
        self.main_frame_password_strength_bar.set(0)
        self.main_frame_password_strength_bar.configure(progress_color="")
        self.reset_start_questions()
        self.main_frame_password_label.configure(text="")
        self.number_of_question_asked = 0

    def return_to_main(self):
        """Returning to the main menu."""
        self.delete_current()
        self.load_main_menu()

    def quit(self):
        """Ending program."""
        self.destroy()

    def randompass(self):
        """Switch to random password menu."""
        self.delete_current()
        self.load_rand_password_menu()

    def tutorial(self):
        """Switch to tutorial menu"""
        self.delete_current()
        self.loadtutorial()

    def enter(self):
        """Entered button pressed, checks the answers entered,
           and generate the password.
           """
        check_number_of_question = (
            self.check_numbers_of_question_asked(self.number_of_question_asked))
        if len(self.answer_entry.get()) != 0:
            self.answers.append(self.answer_entry.get())
        self.answer_entry.delete(0, tk.END)
        self.main_frame_question_label.configure(text=self.get_rand_quesiton())
        self.number_of_question_asked += 1
        self.enter_btn.configure(
            state=check_number_of_question and "disabled" or "normal")
        self.skip_btn.configure(
            state=check_number_of_question and "disabled" or "normal")

        if check_number_of_question:
            result = self.password_generate_by_answer(self.answers)
            self.main_frame_question_label.configure(text=(
                result
                and "Here is your password"
                or "You have not entered any answers press restart to restart"))
            self.restart_btn.configure(state="normal")
            self.main_frame_password_label.configure(
                text=f"{result or 'You didn’t answer a question'}")
            self.check_btn.configure(state="normal")
            self.copy_btn.configure(state="normal")

            if not result:
                self.check_btn.configure(state="disabled")
                self.copy_btn.configure(state="disabled")

    def copy(self):
        """Copying the password."""
        password = self.main_frame_password_label.cget("text")
        self.clipboard_clear()
        self.clipboard_append(password)
        self.copy_btn.configure(state="disabled")

    def copy_rand(self):
        """Copying the password in random password menu."""
        password = self.main_frame_password_label_random.cget("text")
        self.clipboard_clear()
        self.clipboard_append(password)
        self.copy_btn.configure(state="disabled")

    def skip(self):
        """Skiping question."""
        self.main_frame_question_label.configure(text=self.get_rand_quesiton())
        if self.get_rand_quesiton() == None:
            self.reset_start_questions()
            self.main_frame_question_label.configure(
                text=self.get_rand_quesiton())

    def random_generate(self):
        """Generate password in random password menu."""
        character_list = []

        length = int(self.slider.get())

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
            self.main_frame_password_label_random.configure(
                text="Please select one option"
                " and at least a length of 4 characters")
            return ""
        if length < 4:
            self.main_frame_password_label_random.configure(
                text=self.split_string(
                    "Cannot generate a password "
                    "for a length of less than 4 characters!", 25))
            return ""
        if not character_list:
            self.main_frame_password_label_random.configure(
                text="Please select at"
                " least one character type!")
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

        self.main_frame_password_label_random.configure(text=password)
        self.copy_btn.configure(state="normal")
        self.check_btn.configure(state="normal")

    def delete_current(self):
        """Delete the current menu."""
        for widget in self.main_frame_holder.winfo_children():
            widget.forget()

    def __init__(self):
        """Initialize the Password Generator application window."""
        super().__init__()

        self.title("Password generator")
        self.geometry("700x500")
        self.minsize(700, 500)
        self.maxsize(700, 500)

        self.mainframe = ctk.CTkFrame(self, fg_color="black",
                                      width=700,
                                      height=500)
        self.mainframe.pack(fill="both",
                            expand=True)

        self.main_frame_label = (ctk.CTkLabel
                                 (self.mainframe,
                                  text="Password generator",
                                  text_color="white",
                                  fg_color="#01a6f8",
                                  width=200, height=25,
                                  font=("Bold", 20),
                                  corner_radius=5))
        self.main_frame_label.pack(padx=10,
                                   pady=10)

        self.main_frame_holder = ctk.CTkFrame(self.mainframe,
                                              width=600,
                                              height=400)
        self.main_frame_holder.pack(padx=10,
                                    pady=10,
                                    fill="both",
                                    expand=True)

        self.load_main_menu()

    def load_main_menu(self):
        """Load main menu."""

        self.main_menu_side_frame1 = ctk.CTkFrame(self.main_frame_holder,
                                                  fg_color="gray")
        self.main_menu_side_frame1.pack(side="right",
                                        padx=20,
                                        pady=20)

        self.main_menu_side_frame2 = ctk.CTkFrame(self.main_frame_holder,
                                                  fg_color="gray")
        self.main_menu_side_frame2.pack(side="right",
                                        padx=10,
                                        pady=10)

        self.main_menu_main_frame = ctk.CTkFrame(self.main_frame_holder,
                                                 fg_color="gray",)
        self.main_menu_main_frame.pack(side="left",
                                       padx=20,
                                       pady=20)

        self.main_frame_question_label = (
            ctk.CTkLabel(self.main_menu_main_frame,
                         text="Click start to start.",
                         text_color="black",
                         fg_color="white",
                         width=500,
                         height=50,
                         corner_radius=5))
        self.main_frame_question_label.pack(padx=10,
                                            pady=10)

        self.answer_entry = ctk.CTkEntry(self.main_menu_main_frame,
                                         placeholder_text="enter your response",
                                         width=500)
        self.answer_entry.pack(pady=5,
                               padx=5)

        self.main_frame_password_label = (
            ctk.CTkLabel(self.main_menu_main_frame,
                         text="",
                         text_color="black",
                         fg_color="white",
                         width=500,
                         height=30,
                         corner_radius=5))
        self.main_frame_password_label.pack(pady=10,
                                            padx=10)

        self.strength_label = ctk.CTkLabel(self.main_menu_main_frame,
                                           text="")
        self.strength_label.pack(pady=10)

        self.main_frame_password_strength_bar = (
            ctk.CTkProgressBar(self.main_menu_main_frame,
                               progress_color=""))
        self.main_frame_password_strength_bar.set(0)
        self.main_frame_password_strength_bar.pack(pady=10,
                                                   padx=10)

        self.random_password_btn = ctk.CTkButton(self.main_menu_side_frame1,
                                                 text="random password",
                                                 command=self.randompass)
        self.random_password_btn.pack(pady=10,
                                      padx=10)

        self.start_btn = ctk.CTkButton(self.main_menu_side_frame1,
                                       text="start",
                                       command=self.start)
        self.start_btn.pack(pady=10,
                            padx=10)

        self.restart_btn = ctk.CTkButton(self.main_menu_side_frame1,
                                         text="Restart",
                                         command=self.restart,
                                         state="disabled")
        self.restart_btn.pack(pady=10,
                              padx=10)

        self.quit_btn = ctk.CTkButton(self.main_menu_side_frame1,
                                      text="quit",
                                      hover_color="brown2",
                                      command=self.quit)
        self.quit_btn.pack(pady=10,
                           padx=10)

        self.tutorial_btn = ctk.CTkButton(self.main_menu_side_frame1,
                                          text="tutorial",
                                          command=self.tutorial)
        self.tutorial_btn.pack(pady=10,
                               padx=10)

        self.copy_btn = ctk.CTkButton(self.main_menu_side_frame2,
                                      text="Copy",
                                      state="disabled",
                                      command=self.copy,
                                      width=10)
        self.copy_btn.pack(pady=5,
                           padx=5)

        self.enter_btn = ctk.CTkButton(self.main_menu_side_frame2,
                                       text="Enter",
                                       command=self.enter,
                                       state="disabled",
                                       width=10)
        self.enter_btn.pack(pady=5,
                            padx=5)

        self.skip_btn = ctk.CTkButton(self.main_menu_side_frame2,
                                      text="Skip",
                                      command=self.skip,
                                      state="disabled",
                                      width=10)
        self.skip_btn.pack(pady=5,
                           padx=5)

        self.check_btn = ctk.CTkButton(self.main_menu_side_frame2,
                                       text="Check",
                                       command=self.password_strength_display,
                                       state="disabled",
                                       width=10)
        self.check_btn.pack(pady=5,
                            padx=5)

    def load_rand_password_menu(self):
        """Load random pass menu."""
        self.main_menu_side_frame1_randompassword = (
            ctk.CTkFrame(self.main_frame_holder,
                         fg_color="light gray"))
        self.main_menu_side_frame1_randompassword.pack(side="right",
                                                       padx=10,
                                                       pady=10)

        self.main_menu_main_frame_randompassword = (
            ctk.CTkFrame(self.main_frame_holder,
                         fg_color="light grey",))
        self.main_menu_main_frame_randompassword.pack(side="left",
                                                      padx=10,
                                                      pady=10)

        self.main_menu_main_frame_randompassword_1 = (
            ctk.CTkFrame(self.main_menu_main_frame_randompassword,
                         fg_color="gray",))
        self.main_menu_main_frame_randompassword_1.pack(padx=10,
                                                        pady=10)

        self.main_menu_main_frame_randompassword_2 = (
            ctk.CTkFrame(self.main_menu_main_frame_randompassword,
                         fg_color="gray"))
        self.main_menu_main_frame_randompassword_2.pack(padx=10,
                                                        pady=10)

        self.main_frame_randompassword_2_sector_1 = (
            ctk.CTkFrame(self.main_menu_main_frame_randompassword_2,
                         fg_color="gray"))
        self.main_frame_randompassword_2_sector_1.pack(padx=10,
                                                       pady=10)

        self.main_frame_randompassword_2_sector_2 = (
            ctk.CTkFrame(self.main_menu_main_frame_randompassword_2,
                         fg_color="gray"))
        self.main_frame_randompassword_2_sector_2.pack(padx=10,
                                                       pady=10)

        self.main_frame_password_label_random = (
            ctk.CTkLabel(self.main_menu_main_frame_randompassword_1,
                         text="password",
                         text_color="black",
                         fg_color="white",
                         width=500,
                         height=30,
                         corner_radius=5))
        self.main_frame_password_label_random.pack(pady=10,
                                                   padx=10)

        self.strength_label = ctk.CTkLabel(
            self.main_menu_main_frame_randompassword_1,
            text="")
        self.strength_label.pack(pady=10)

        self.main_frame_password_strength_bar = (
            ctk.CTkProgressBar(self.main_menu_main_frame_randompassword_1,
                               progress_color=""))
        self.main_frame_password_strength_bar.set(0)
        self.main_frame_password_strength_bar.pack(pady=10,
                                                   padx=10)

        self.passwordlength = ctk.CTkLabel(
            self.main_frame_randompassword_2_sector_1,
            text=("Password Length"))
        self.passwordlength.pack()

        self.slider = ctk.CTkSlider(self.main_frame_randompassword_2_sector_1,
                                    from_=0,
                                    to=50,
                                    command=self.sliding,
                                    height=20,)
        self.slider.pack(side="right")

        self.slider.set(8)

        self.generate_btn = (
            ctk.CTkButton(self.main_menu_side_frame1_randompassword,
                          text="Generate",
                          command=self.random_generate))
        self.generate_btn.pack(pady=10,
                               padx=10)

        self.copy_btn = ctk.CTkButton(self.main_menu_side_frame1_randompassword,
                                      text="Copy",
                                      command=self.copy_rand,
                                      state="disabled")
        self.copy_btn.pack(pady=10,
                           padx=10)

        self.check_btn = (
            ctk.CTkButton(self.main_menu_side_frame1_randompassword,
                          text="Check",
                          command=self.random_password_strength_display,
                          state="disabled"))
        self.check_btn.pack(pady=5,
                            padx=5)

        self.reset_btn = ctk.CTkButton(self.main_menu_side_frame1_randompassword,
                                       text="Reset",
                                       command=self.reset)
        self.reset_btn.pack(pady=10,
                            padx=10)

        self.tutorial_btn = (
            ctk.CTkButton(self.main_menu_side_frame1_randompassword,
                          text="tutorial",
                          command=self.tutorial))
        self.tutorial_btn.pack(pady=10,
                               padx=10)

        self.return_btn = (
            ctk.CTkButton(self.main_menu_side_frame1_randompassword,
                          text="return",
                          command=self.return_to_main))
        self.return_btn.pack(padx=10,
                             pady=10)

        self.quit_btn = (
            ctk.CTkButton(self.main_menu_side_frame1_randompassword,
                          text="quit",
                          hover_color="brown2",
                          command=self.quit))
        self.quit_btn.pack(pady=10,
                           padx=10)

        self.lengthlabel = (
            ctk.CTkLabel(self.main_frame_randompassword_2_sector_1,
                         text=self.slider.get(),
                         fg_color="light gray",
                         text_color="black",
                         corner_radius=5))
        self.lengthlabel.pack(side="right")

        check_symbol = ctk.StringVar(value="off")
        self.checkboxsmb = (
            ctk.CTkCheckBox(self.main_frame_randompassword_2_sector_2,
                            text="Symbols",
                            variable=check_symbol,
                            onvalue="on",
                            offvalue="off"))
        self.checkboxsmb.pack(pady=5,
                              padx=5)

        check_number = ctk.StringVar(value="off")
        self.checkboxnum = (
            ctk.CTkCheckBox(self.main_frame_randompassword_2_sector_2,
                            text="Numbers",
                            variable=check_number,
                            onvalue="on",
                            offvalue="off"))
        self.checkboxnum.pack(pady=5,
                              padx=5)

        check_up = ctk.StringVar(value="off")
        self.checkboxup = (
            ctk.CTkCheckBox(self.main_frame_randompassword_2_sector_2,
                            text="Uppercase",
                            variable=check_up,
                            onvalue="on",
                            offvalue="off"))
        self.checkboxup.pack(pady=5,
                             padx=5)

        check_low = ctk.StringVar(value="off")
        self.checkboxlow = (
            ctk.CTkCheckBox(self.main_frame_randompassword_2_sector_2,
                            text="Lowercase",
                            variable=check_low,
                            onvalue="on",
                            offvalue="off"))
        self.checkboxlow.pack(pady=5,
                              padx=5)

    def loadtutorial(self):
        """Load tutorial menu."""
        self.tutorial_frame = ctk.CTkFrame(self.main_frame_holder,
                                           fg_color="gray")
        self.tutorial_frame.pack(padx=10,
                                 pady=10,
                                 fill="both",
                                 expand=True)

        self.tutorial_frame_2 = ctk.CTkFrame(self.main_frame_holder,
                                             fg_color="transparent")
        self.tutorial_frame_2.pack(side="right",
                                   padx=10,
                                   pady=10)

        self.return_btn = (ctk.CTkButton
                           (self.tutorial_frame_2,
                            text="return",
                            command=self.return_to_main,
                            width=30,
                            height=30))
        self.return_btn.pack(side="right",
                             padx=10,
                             pady=10)

        self.textbox = ctk.CTkTextbox(self.tutorial_frame,
                                      fg_color="gray",
                                      font=("Helvetica", 14))
        self.textbox.pack(padx=10,
                          pady=10,
                          fill="both",
                          expand=True)

        self.textbox.insert("0.0", "Tutorial\n\n" +
                            """
        1. Main Menu 
        At Main Menu which is the password generator which 
        generates passwords 
        from the user answering 3 questions. 
        first, you press the Start button on the left-hand side which is 
        labelled Start, 
        and then the program displays the question on the big white label, 
        you enter your answer in the entry box which has "enter your response" 
        on it, 
        then you press the enter button on 
        your left-hand side which has the enter labelled on it 
        (answered 1st time), 
        a new question will appear on the white label and 
        you then enter your answers again (answered 2nd time) as the process 
        before, 
        for totally three times afterwards including the two times. 
        so the next time you answer the question will be the third time. 
        the program will then display the password in the white label below the 
        entry box.

        you can copy the password by pressing the copy button, 
        and check the password strength by pressing the check button. 
        when the check button is pressed a message describing the strength of 
        the password will display under the white label with the password in it. 
        the colour of the progress bar represents different strengths of the 
        password 
        (red = very weak, orange = weak, yellow = fair, lime green = strong, 
        green = very strong) 
        and the progress of the bar increases as the strength of the bar is 
        increased.
        you can also skip questions by pressing the skip button on your left 
        press restart to restart the process of answering questions to generate 
        a password. 
        tutorial buttons send you to the tutorial menu here. return button 
        returns to the main menu. 
        quit button ends the program. 

        2. random password 
        - press random password to go to the random password 
        menu 
        at random password you can generate a password by 
        selecting the types of characters you want in your password 
        by ticking the boxes and selecting the length by sliding the slider. 
        press generate after you have selected your options for the characters, 
        you want in the password and after you have selected your length from 
        the slider. 
        copy button copies the password generated. check button checks the 
        password strength. 
        reset button resets to the default setting for 
        the options of type character and the password length. 
        tutorial buttons send you to the tutorial menu here. 
        return button returns to the main menu. 
        quit button ends the program. 

        3. Issues
        Grey-out buttons are disabled 
        which means you can't press them 
        sometimes buttons are not disabled properly 
        so keep it in mind and 
        you can reset or restart to redo the password-generating process for 
        the best functionality. 
        Usually the copy and the check button that is not disabled properly

        When you skip the question sometimes the question you already entered 
        could appear again which is an error that will require fixing 
        but it doesn't affect the overall performance of the program 
        but to keep that in mind. 

        there is a error on if you generated the password in the main menu 
        and then you went straight to random password or tutorial menu
        and went back to the main menu you will keep on answering questions 
        with out stoping to generate the password
        have to press restart everytime you generate the password or reset
        on random password or just quit it.

        """)

        self.textbox.configure(state=ctk.DISABLED)


if __name__ == "__main__":
    MainWindow().mainloop()
