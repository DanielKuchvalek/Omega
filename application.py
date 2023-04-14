from tkinter import Frame, Button, Toplevel, Label, Entry
import sys
from widgets import Widgets


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.role = None
        self.pack()
        self.login_window()

    def login_window(self):
        login_window = Frame(self.master, bg="gray10")
        login_window.pack(fill="both", expand=True)

        username_label = Label(login_window, text="Username:", fg="white", bg="gray10", font=("Arial", 12))
        username_label.pack(pady=5)
        username_entry = Entry(login_window, bg="gray25", fg="white", font=("Arial", 12))
        username_entry.pack()

        password_label = Label(login_window, text="Password:", fg="white", bg="gray10", font=("Arial", 12))
        password_label.pack(pady=5)
        password_entry = Entry(login_window, show="*", bg="gray25", fg="white", font=("Arial", 12))
        password_entry.pack()

        login_button = Button(login_window, text="Login", bg="gray40", fg="white", font=("Arial", 12),
                              activebackground="gray30", activeforeground="white", relief="flat", borderwidth=0,
                              highlightthickness=0,
                              command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.pack(pady=10, padx=60)

        self.master.bind("<Return>", lambda event: self.login(username_entry.get(), password_entry.get()))

        username_entry.focus_set()

    def login(self, username, password):
        if username == "admin" and password == "password" or username == "a" and password == "a":
            self.role = "admin"
        elif username == "user" and password == "password":
            self.role = "user"
        else:
            self.role = None

        if self.role:
            self.menu_widgets()
            self.master.withdraw()  # skryje okno s login formulářem

    def menu_widgets(self):
        self.widgets = Widgets(self.master, self.role)
        self.widgets.menu_widgets()

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell
