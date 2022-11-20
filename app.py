import tkinter as tk


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="blue")

        Button = tk.Button(
            self,
            text="Second",
            font=("Arial", 15),
            command=lambda: controller.show_frame(SecondPage),
        )
        Button.place(x=650, y=450)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="green")

        Button = tk.Button(
            self,
            text="Third",
            font=("Arial", 15),
            command=lambda: controller.show_frame(ThirdPage),
        )
        Button.place(x=650, y=450)

        Button = tk.Button(
            self,
            text="Home",
            font=("Arial", 15),
            command=lambda: controller.show_frame(FirstPage),
        )
        Button.place(x=100, y=450)


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="Tomato")

        Button = tk.Button(
            self,
            text="Home",
            font=("Arial", 15),
            command=lambda: controller.show_frame(FirstPage),
        )
        Button.place(x=650, y=450)

        Button = tk.Button(
            self,
            text="Back",
            font=("Arial", 15),
            command=lambda: controller.show_frame(SecondPage),
        )
        Button.place(x=100, y=450)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

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


app = Application()
app.maxsize(800, 500)
app.mainloop()
