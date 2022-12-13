from pathlib import Path
import pickle

import tkinter as tk

from user import User
from emotion import Emotion
from listener import Listener
from asker import Asker
from gui import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (
            LogIn,
            Options,
            CreateAccount,
            CheckStatistics,
            EmotionRecognitionSession,
            AppListening,
            AppAsking,
            SeeResolution,
            Resolution,
        ):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LogIn)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


if __name__ == "__main__":
    app = App()
    app.maxsize(800, 500)
    app.mainloop()
