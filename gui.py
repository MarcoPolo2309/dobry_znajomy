import pickle

import tkinter as tk

users = pickle.load(open("./data/users.pickle", "rb"))


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

        def log_in(user_name: str = None, user_password: str = None):
            user_names_passwords = [
                (user.user_name, user.user_password) for user in users
            ]
            if (user_name, user_password) in user_names_passwords:
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
            command=lambda: log_in(login_entry.get(), password_entry.get()),
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

        button3 = tk.Button(
            self,
            text="Create an account",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#6EC0ED",
            command=lambda: controller.show_frame(LogIn),
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
            command=lambda: controller.show_frame(EmotionRecognitionSession),
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
            command=lambda: controller.show_frame(AppListening),
        )
        button9.place(relwidth=0.4, relheight=0.5, relx=0.05, rely=0.25)

        button10 = tk.Button(
            self,
            text="App-asking",
            font=("Arial", 14),
            fg="#EAFDFF",
            bg="#00C5A4",
            command=lambda: controller.show_frame(AppAsking),
        )
        button10.place(relwidth=0.4, relheight=0.5, relx=0.55, rely=0.25)


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
            text="Answer the question:",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        answerthequestion_label.place(
            relwidth=0.25, relheight=0.05, relx=0.1765, rely=0.23
        )

        howareyou_label = tk.Label(
            self,
            text="How are you feeling today?",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        howareyou_label.place(relwidth=0.25, relheight=0.05, relx=0.2, rely=0.35)

        button14 = tk.Button(
            self,
            text="Very bad",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#03045e",
            command=lambda: controller.show_frame(Options),
        )
        button14.place(relwidth=0.1, relheight=0.055, relx=0.1, rely=0.44)

        button15 = tk.Button(
            self,
            text="Bad",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#023e8a",
            command=lambda: controller.show_frame(Options),
        )
        button15.place(relwidth=0.1, relheight=0.055, relx=0.25, rely=0.44)

        button16 = tk.Button(
            self,
            text="Not in the mood",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#0077b6",
            command=lambda: controller.show_frame(Options),
        )
        button16.place(relwidth=0.2, relheight=0.055, relx=0.4, rely=0.44)

        button17 = tk.Button(
            self,
            text="Good",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#00b4d8",
            command=lambda: controller.show_frame(Options),
        )
        button17.place(relwidth=0.1, relheight=0.055, relx=0.65, rely=0.44)

        button17 = tk.Button(
            self,
            text="Excellent",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#48cae4",
            command=lambda: controller.show_frame(Options),
        )
        button17.place(relwidth=0.12, relheight=0.055, relx=0.8, rely=0.44)

        whichemotion_label = tk.Label(
            self,
            text="Which emotion do you feel the most right now?",
            font=("Arial", 13),
            fg="#345B63",
            bg="#D9E9E4",
        )
        whichemotion_label.place(relwidth=0.45, relheight=0.05, relx=0.19, rely=0.58)

        button18 = tk.Button(
            self,
            text="Happiness",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#48cae4",
            command=lambda: controller.show_frame(Resolution),
        )
        button18.place(relwidth=0.12, relheight=0.055, relx=0.1, rely=0.67)

        button19 = tk.Button(
            self,
            text="Sadness",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#00b4d8",
            command=lambda: controller.show_frame(Resolution),
        )
        button19.place(relwidth=0.12, relheight=0.055, relx=0.275, rely=0.67)

        button20 = tk.Button(
            self,
            text="Neutral",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#0077b6",
            command=lambda: controller.show_frame(Resolution),
        )
        button20.place(relwidth=0.12, relheight=0.055, relx=0.45, rely=0.67)

        button21 = tk.Button(
            self,
            text="Fear",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#023e8a",
            command=lambda: controller.show_frame(Resolution),
        )
        button21.place(relwidth=0.12, relheight=0.055, relx=0.625, rely=0.67)

        button22 = tk.Button(
            self,
            text="Anger",
            font=("Arial", 13),
            fg="#EAFDFF",
            bg="#03045e",
            command=lambda: controller.show_frame(Resolution),
        )
        button22.place(relwidth=0.12, relheight=0.055, relx=0.805, rely=0.67)


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
