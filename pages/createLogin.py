import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors
from classes import Employee

class create_login_page(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback):
        super().__init__(parent)
        self.show_frame = show_frame_callback

        # Configure the size of the CTkFrame
        width = 1200
        height = 800
        self.configure(width=width, height=height)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.email = tk.StringVar()
        self.password = tk.StringVar()

        # Load and display the logo image
        self.logo_image = Image.open("img/logo.png")
        self.logo_image = self.logo_image.resize((150, 150), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self, image=self.logo_photo)
        self.logo_label.grid(row=0, column=0, pady=20)

        # Custom input and label configurations
        self.custom_input = Custom_Input(
            bg_color=Colors.white,
            fg_color=Colors.black,
            text_color=Colors.black,
            width=300,
            height=30,
            border_radius=10
        )

        self.custom_label = Custom_Label(
            text_color=Colors.white,
            font=12
        )

        self.custom_button_login = Custom_Button(
            text="Login",
            command=self.login,
            fg_color=Colors.primary,
            hover_color=Colors.success
        )

        self.custom_button_register = Custom_Button(
            text="Register",
            command=lambda: self.show_frame("register"),
            fg_color=Colors.secondary,
            hover_color=Colors.success
        )

        # Create and place email label and entry
        self.email_label = self.custom_label.create_label(self, text="Email")
        self.email_label.grid(row=1, column=0, pady=10)
        self.email_entry = self.custom_input.create_input(self, textvariable=self.email)
        self.email_entry.grid(row=2, column=0, pady=10)

        # Create and place password label and entry
        self.password_label = self.custom_label.create_label(self, text="Password")
        self.password_label.grid(row=3, column=0, pady=10)
        self.password_entry = self.custom_input.create_input(self, textvariable=self.password, show="*")
        self.password_entry.grid(row=4, column=0, pady=10)

        # Create and place buttons
        self.login_button = self.custom_button_login.create_button(self)
        self.login_button.grid(row=5, column=0, pady=20)

        self.register_button = self.custom_button_register.create_button(self)
        self.register_button.grid(row=6, column=0, pady=10)

    def login(self):
        email = self.email.get()
        password = self.password.get()

        if email and password:
            employee = Employee.getEmployeeByEmail(email)
            if employee:
                if employee["password"] == password:
                    messagebox.showinfo("Success", "Login successful.")
                    self.show_frame("home")
                else:
                    messagebox.showwarning("Warning", "Incorrect password.")
            else:
                messagebox.showwarning("Warning", "Email not found.")
        else:
            messagebox.showwarning("Warning", "All fields must be completed.")
