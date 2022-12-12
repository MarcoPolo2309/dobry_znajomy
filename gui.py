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
