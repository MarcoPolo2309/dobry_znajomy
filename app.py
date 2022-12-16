from pathlib import Path
import pickle

import tkinter as tk

from gui import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.pages = []

        self.frames = {
            LogIn,
            Options,
            CreateAccount,
            CheckStatistics,
            EmotionRecognitionSession,
            EmotionRecognitionSessionForm,
            AppListening,
            AppAsking,
            SeeResolution,
            Resolution,
        }
        for F in (
            LogIn,
            Options,
            CreateAccount,
            CheckStatistics,
            EmotionRecognitionSession,
            EmotionRecognitionSessionForm,
            AppListening,
            AppAsking,
            SeeResolution,
            Resolution,
        ):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        session = self.frames[EmotionRecognitionSessionForm].get_session()
        frame = Wait(window, self, session)
        self.frames[Wait] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LogIn)

    def show_frame(self, page, **kwargs):
        frame = page(self, **kwargs)
        frame.tkraise()
        self.title("Application")


if __name__ == "__main__":
    app = App()
    app.maxsize(800, 500)
    app.mainloop()
