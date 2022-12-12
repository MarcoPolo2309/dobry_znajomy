from pathlib import Path

import tkinter as tk

from user import User
from emotion import Emotion
from listener import Listener
from asker import Asker
from gui import FirstPage, SecondPage, ThirdPage


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


if __name__ == "__main__":
    app = App()
    app.maxsize(800, 500)
    app.mainloop()
