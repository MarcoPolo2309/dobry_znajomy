import datetime
import pickle

import tkinter as tk

from user import User
from emotion import Emotion
from listener import Listener
from asker import Asker
from user import *

users = Users()
users_list = users.get_users()

session = None


class LogIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#CDEFF9")
        self.controller = controller

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#CDEFF9"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        login_label = tk.Label(
            self, text="login", font=("Arial", 13), fg="#E258C0", bg="#CDEFF9"
        )
        login_label.place(relwidth=0.12, relheight=0.05, relx=0.28, rely=0.3)

        login_entry = tk.Entry(self, font=("Arial", 12), bg="#E7FDFF")
        login_entry.place(relwidth=0.25, relheight=0.05, relx=0.383, rely=0.3)

        password_label = tk.Label(
            self, text="password", font=("Arial", 13), fg="#E258C0", bg="#CDEFF9"
        )
        password_label.place(relwidth=0.15, relheight=0.05, relx=0.245, rely=0.4)

        password_entry = tk.Entry(self, font=("Arial", 12), bg="#E7FDFF")
        password_entry.place(relwidth=0.25, relheight=0.05, relx=0.383, rely=0.4)

        def log_in(controller, user_nick_name: str = None, user_password: str = None):
            user_nick_names_passwords = [
                (user.user_nick_name, user.user_password) for user in users_list
            ]
            if (user_nick_name, user_password) in user_nick_names_passwords:
                print("Access granted!")
                controller.show_frame(Options)
            else:
                print("Access denied")

        button1 = tk.Button(
            self,
            text="Log In",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#6EC0ED",
            command=lambda: log_in(controller, login_entry.get(), password_entry.get()),
        )
        button1.place(relwidth=0.25, relheight=0.055, relx=0.383, rely=0.5)

        account_label = tk.Label(
            self,
            text="Don't have account?",
            font=("Arial", 13),
            fg="#96B7C1",
            bg="#CDEFF9",
        )
        account_label.place(relwidth=0.3, relheight=0.055, relx=0.355, rely=0.63)

        button2 = tk.Button(
            self,
            text="Create an account",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#6EC0ED",
            command=lambda: controller.show_frame(CreateAccount),
        )
        button2.place(relwidth=0.25, relheight=0.055, relx=0.383, rely=0.72)


class CreateAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#CDEFF9")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#CDEFF9"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        name_label = tk.Label(
            self, text="Name", font=("Arial", 13), fg="#96B7C1", bg="#CDEFF9"
        )
        name_label.place(relwidth=0.12, relheight=0.05, relx=0.275, rely=0.3)

        name_entry = tk.Entry(self, font=("Arial", 12), bg="#E7FDFF")
        name_entry.place(relwidth=0.25, relheight=0.05, relx=0.383, rely=0.3)

        surname_label = tk.Label(
            self, text="Surname", font=("Arial", 13), fg="#96B7C1", bg="#CDEFF9"
        )
        surname_label.place(relwidth=0.15, relheight=0.05, relx=0.245, rely=0.4)

        surname_entry = tk.Entry(self, font=("Arial", 12), bg="#E7FDFF")
        surname_entry.place(relwidth=0.25, relheight=0.05, relx=0.383, rely=0.4)

        login2_label = tk.Label(
            self, text="Login", font=("Arial", 13), fg="#96B7C1", bg="#CDEFF9"
        )
        login2_label.place(relwidth=0.15, relheight=0.05, relx=0.26, rely=0.5)

        login2_entry = tk.Entry(self, font=("Arial", 12), bg="#E7FDFF")
        login2_entry.place(relwidth=0.25, relheight=0.05, relx=0.383, rely=0.5)

        password2_label = tk.Label(
            self, text="Password", font=("Arial", 13), fg="#96B7C1", bg="#CDEFF9"
        )
        password2_label.place(relwidth=0.15, relheight=0.05, relx=0.245, rely=0.6)

        password2_entry = tk.Entry(self, font=("Arial", 12), bg="#E7FDFF")
        password2_entry.place(relwidth=0.25, relheight=0.05, relx=0.383, rely=0.6)

        def create_account(
            controller,
            user_real_name: str = None,
            user_surname: str = None,
            user_nick_name: str = None,
            user_password: str = None,
        ):
            users.create_user(
                user_real_name, user_surname, user_nick_name, user_password
            )
            controller.show_frame(LogIn)
            print("Added new user")

        button3 = tk.Button(
            self,
            text="Create an account",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#6EC0ED",
            command=lambda: create_account(
                controller,
                name_entry.get(),
                surname_entry.get(),
                login2_entry.get(),
                password2_entry.get(),
            ),
        )
        button3.place(relwidth=0.25, relheight=0.055, relx=0.383, rely=0.7)


class Options(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#CDEFF9")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#CDEFF9"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        button4 = tk.Button(
            self,
            text="Start emotion recognition session",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#AED8A5",
            command=lambda: controller.show_frame(EmotionRecognitionSessionForm),
        )
        button4.place(relwidth=0.4, relheight=0.5, relx=0.05, rely=0.25)

        button5 = tk.Button(
            self,
            text="Check statistics",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#6EC0ED",
            command=lambda: controller.show_frame(CheckStatistics),
        )
        button5.place(relwidth=0.4, relheight=0.5, relx=0.55, rely=0.25)


# TUTAJ TRZEBA PODPIĄĆ DO TYCH PRZYCISKÓW BO JEST NA RAZIE ŻE PRZECHODZI ZNOWU NA LOGIN
class CheckStatistics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#CDEFF9")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#CDEFF9"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        button6 = tk.Button(
            self,
            text="See figures",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#6EC0ED",
            command=lambda: controller.show_frame(LogIn),
        )
        button6.place(relwidth=0.25, relheight=0.3, relx=0.05, rely=0.35)

        button7 = tk.Button(
            self,
            text="See 'my favourities'",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#00A7D8",
            command=lambda: controller.show_frame(LogIn),
        )
        button7.place(relwidth=0.25, relheight=0.3, relx=0.375, rely=0.35)

        button8 = tk.Button(
            self,
            text="Save on the device",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#002E94",
            command=lambda: controller.show_frame(LogIn),
        )
        button8.place(relwidth=0.25, relheight=0.3, relx=0.7, rely=0.35)


class EmotionRecognitionSession(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#D9E9E4")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#D9E9E4"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        button9 = tk.Button(
            self,
            text="App-listening",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#50BF84",
            command=lambda: controller.show_frame(EmotionRecognitionSessionForm),
        )
        button9.place(relwidth=0.4, relheight=0.5, relx=0.05, rely=0.25)

        button10 = tk.Button(
            self,
            text="App-asking",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#00C5A4",
            command=lambda: controller.show_frame(EmotionRecognitionSessionForm),
        )
        button10.place(relwidth=0.4, relheight=0.5, relx=0.55, rely=0.25)


class EmotionRecognitionSessionForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#D9E9E4")

        goodfriend_label = tk.Label(
            self,
            text="Set session parameters",
            font=("Arial", 15),
            fg="#E258C0",
            bg="#D9E9E4",
        )

        master = self

        hour_string = ""
        min_string = ""
        sec_string = ""
        last_value = ""
        f = ("Arial", 14)

        session_type_label = tk.Label(
            self,
            text="Type",
            font=f,
            fg="#E258C0",
            bg="#D9E9E4",
            justify=tk.LEFT,
        )

        session_duration_label = tk.Label(
            self,
            text="Duration (d,h,m,s)",
            font=f,
            fg="#E258C0",
            bg="#D9E9E4",
            justify=tk.LEFT,
        )

        session_feedback_timeout_label = tk.Label(
            self,
            text="Question every (h,m,s)",
            font=f,
            fg="#E258C0",
            bg="#D9E9E4",
            justify=tk.LEFT,
        )

        session_give_feedback_label = tk.Label(
            self,
            text="Give feedback",
            font=f,
            fg="#E258C0",
            bg="#D9E9E4",
            justify=tk.LEFT,
        )

        session_type_sb = tk.Spinbox(
            master,
            values=("Asking", "Listening"),
            wrap=True,
            textvariable=hour_string,
            width=10,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        day_sb1 = tk.Spinbox(
            master,
            from_=0,
            to=365,
            wrap=True,
            textvariable=hour_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        hour_sb1 = tk.Spinbox(
            master,
            from_=0,
            to=24,
            wrap=True,
            textvariable=hour_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        min_sb1 = tk.Spinbox(
            master,
            from_=0,
            to=59,
            wrap=True,
            textvariable=min_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        sec_sb1 = tk.Spinbox(
            master,
            from_=0,
            to=59,
            wrap=True,
            textvariable=sec_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        hour_sb = tk.Spinbox(
            master,
            from_=0,
            to=24,
            wrap=True,
            textvariable=hour_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        min_sb = tk.Spinbox(
            master,
            from_=0,
            to=59,
            wrap=True,
            textvariable=min_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        sec_sb = tk.Spinbox(
            master,
            from_=0,
            to=59,
            wrap=True,
            textvariable=sec_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )

        feedback_sb = tk.Spinbox(
            master,
            values=("Yes", "No"),
            wrap=True,
            textvariable=sec_string,
            width=2,
            state="readonly",
            font=f,
            justify=tk.CENTER,
        )
        goodfriend_label.place(relwidth=0.30, relheight=0.1, relx=0.35, rely=0.1)

        session_type_label.pack()
        session_type_label.place(relwidth=0.3, relheight=0.06, relx=0.1, rely=0.28)
        session_type_sb.place(relwidth=0.18, relheight=0.08, relx=0.41, rely=0.28)
        session_type = session_type_sb.get()

        session_duration_label.pack()
        session_duration_label.place(relwidth=0.3, relheight=0.06, relx=0.1, rely=0.4)
        day_sb1.place(relwidth=0.06, relheight=0.08, relx=0.38, rely=0.4)
        hour_sb1.place(relwidth=0.06, relheight=0.08, relx=0.44, rely=0.4)
        min_sb1.place(relwidth=0.06, relheight=0.08, relx=0.50, rely=0.4)
        sec_sb1.place(relwidth=0.06, relheight=0.08, relx=0.56, rely=0.4)
        hour = int(day_sb1.get()) * 24 + int(hour_sb1.get())
        minute = int(min_sb1.get())
        second = int(sec_sb1.get())
        session_duration = datetime.time(hour=hour, minute=minute, second=second)

        session_feedback_timeout_label.pack()
        session_feedback_timeout_label.place(
            relwidth=0.3, relheight=0.06, relx=0.1, rely=0.52
        )
        hour_sb.place(relwidth=0.06, relheight=0.08, relx=0.41, rely=0.52)
        min_sb.place(relwidth=0.06, relheight=0.08, relx=0.47, rely=0.52)
        sec_sb.place(relwidth=0.06, relheight=0.08, relx=0.53, rely=0.52)
        hour = int(hour_sb.get())
        minute = int(min_sb.get())
        second = int(sec_sb.get())
        session_feedback_timeout = datetime.time(
            hour=hour, minute=minute, second=second
        )

        session_give_feedback_label.pack()
        session_give_feedback_label.place(
            relwidth=0.3, relheight=0.06, relx=0.1, rely=0.64
        )
        feedback_sb.place(relwidth=0.06, relheight=0.08, relx=0.47, rely=0.64)
        session_give_feedback = True if feedback_sb.get() == "Yes" else False

        self.session = None

        def start_session(
            session_type: str,
            session_duration: datetime,
            session_feedback_timeout: datetime,
            session_give_feedback: bool,
        ):
            if session_type == "Asking":
                self.session = Asker(
                    session_start_date=datetime.datetime.now(),
                    session_duration=session_duration,
                    give_feedback=session_give_feedback,
                    feedback_timeout=session_feedback_timeout,
                )
                print("Created Asker session!")
            else:
                self.session = Listener()

            controller.show_frame(Wait)

        button1 = tk.Button(
            self,
            text="Start session",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#50BF84",
            command=lambda: start_session(
                session_type,
                session_duration,
                session_feedback_timeout,
                session_give_feedback,
            ),
        )
        button1.place(relwidth=0.30, relheight=0.15, relx=0.35, rely=0.8)

    def get_session(self):
        return self.session


class Wait(tk.Frame):
    def __init__(self, parent, controller, session):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#D9E9E4")

        self.session = session

        if session:
            print(session.feedback_timeout)


class AppListening(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#D9E9E4")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#D9E9E4"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        recognisedemotion_label = tk.Label(
            self,
            text="Recognised emotion:",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        recognisedemotion_label.place(
            relwidth=0.25, relheight=0.05, relx=0.15, rely=0.25
        )

        #        login_entry = tk.Entry(
        #            self,
        #            font=("Arial", 13),
        #            bg = "#E7FDFF"
        #        )
        #        login_entry.place(relwidth=0.25, relheight=0.05, relx=0.383, rely=0.3)

        maybeyouwantto_label = tk.Label(
            self,
            text="Maybe you want to ...",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        maybeyouwantto_label.place(relwidth=0.25, relheight=0.05, relx=0.15, rely=0.45)

        button11 = tk.Button(
            self,
            text="See a meme",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#50BF84",
            command=lambda: controller.show_frame(SeeResolution),
        )
        button11.place(relwidth=0.25, relheight=0.055, relx=0.383, rely=0.57)

        button12 = tk.Button(
            self,
            text="See a funny video",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#50BF84",
            command=lambda: controller.show_frame(SeeResolution),
        )
        button12.place(relwidth=0.25, relheight=0.055, relx=0.383, rely=0.67)

        button13 = tk.Button(
            self,
            text="Listen a song",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#50BF84",
            command=lambda: controller.show_frame(SeeResolution),
        )
        button13.place(relwidth=0.25, relheight=0.055, relx=0.383, rely=0.77)

        button26 = tk.Button(
            self,
            text="Skip",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#345B63",
            command=lambda: controller.show_frame(Resolution),
        )
        button26.place(relwidth=0.25, relheight=0.055, relx=0.383, rely=0.87)


class AppAsking(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#D9E9E4")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#D9E9E4"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        answerthequestion_label = tk.Label(
            self,
            text="Answer the questions below",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        answerthequestion_label.place(
            relwidth=0.25, relheight=0.05, relx=0.1765, rely=0.23
        )

        howareyou_label = tk.Label(
            self,
            text="How do you feel?",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        howareyou_label.place(relwidth=0.25, relheight=0.05, relx=0.2, rely=0.35)

        master = self
        text = ""

        mood = tk.Spinbox(
            master,
            values=("Very bad", "Bad", "Not in the mood", "Good", "Excellent"),
            wrap=True,
            textvariable=text,
            width=10,
            state="readonly",
            font=("Arial", 13),
            justify=tk.CENTER,
        )
        mood.place(relwidth=0.2, relheight=0.055, relx=0.4, rely=0.44)

        whichemotion_label = tk.Label(
            self,
            text="Which emotion do you feel the most right now?",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        whichemotion_label.place(relwidth=0.45, relheight=0.05, relx=0.19, rely=0.58)

        emotion = tk.Spinbox(
            master,
            values=("Happiness", "Sadness", "Neutral", "Fear", "Anger"),
            wrap=True,
            textvariable=text,
            width=10,
            state="readonly",
            font=("Arial", 13),
            justify=tk.CENTER,
        )
        emotion.place(relwidth=0.12, relheight=0.055, relx=0.45, rely=0.67)

        submit_button = tk.Button(
            self,
            text="Submit",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#03045e",
            command=lambda: controller.show_frame(Wait),
        )
        submit_button.place(relwidth=0.12, relheight=0.055, relx=0.44, rely=0.76)


class SeeResolution(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#D9E9E4")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#D9E9E4"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        button23 = tk.Button(
            self,
            text="See the resolution chosen by yourself",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#00C5A4",
            command=lambda: controller.show_frame(Resolution),
        )
        button23.place(relwidth=0.45, relheight=0.5, relx=0.03, rely=0.25)

        button24 = tk.Button(
            self,
            text="See the resolution chosen by the App",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#2E8473",
            command=lambda: controller.show_frame(Resolution),
        )
        button24.place(relwidth=0.45, relheight=0.5, relx=0.52, rely=0.25)


class Resolution(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#D9E9E4")

        goodfriend_label = tk.Label(
            self, text="Good Friend", font=("Arial", 15), fg="#E258C0", bg="#D9E9E4"
        )
        goodfriend_label.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.055)

        button25 = tk.Button(
            self,
            text="Save to 'my favourites'",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#00A7D8",
            command=lambda: controller.show_frame(Options),
        )
        button25.place(relwidth=0.25, relheight=0.055, relx=0.6, rely=0.8)
