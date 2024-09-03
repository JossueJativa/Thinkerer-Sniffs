import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from classes import Employee
from functions.authentication import create_employee
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors
import ctypes

class create_register_page(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback):
        super().__init__(parent)
        self.show_frame = show_frame_callback

        # Configurar el tamaño del CTkFrame
        width = 1200
        height = 800
        self.configure(
            width=width,
            height=height,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Load and display the logo image
        self.logo_image = Image.open("img/logo.png")
        self.logo_image = self.logo_image.resize((150, 150), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self, image=self.logo_photo)
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=20)

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
            command=lambda: self.show_frame("login"),
            fg_color=Colors.secondary,
            hover_color=Colors.success
        )

        self.custom_button_register = Custom_Button(
            text="Register",
            command=self.register_user,
            fg_color=Colors.primary,
            hover_color=Colors.success
        )

        self.username = ctk.StringVar()
        self.password = ctk.StringVar()
        self.email = ctk.StringVar()
        self.phone = ctk.StringVar()
        self.confirm_password = ctk.StringVar()

        # Username Entry
        self.username_label = self.custom_label.create_label(self, text="Username:")
        self.username_label.grid(row=1, column=0, pady=5)
        self.username_entry = self.custom_input.create_input(self, textvariable=self.username)
        self.username_entry.grid(row=1, column=1, pady=5)

        # Email Entry
        self.email_label = self.custom_label.create_label(self, text="Email:")
        self.email_label.grid(row=2, column=0, pady=5)
        self.email_entry = self.custom_input.create_input(self, textvariable=self.email)
        self.email_entry.grid(row=2, column=1, pady=5)

        # Phone Entry
        self.phone_label = self.custom_label.create_label(self, text="Phone:")
        self.phone_label.grid(row=3, column=0, pady=5)
        self.phone_entry = self.custom_input.create_input(self, textvariable=self.phone)
        self.phone_entry.grid(row=3, column=1, pady=5)

        # Password Entry
        self.password_label = self.custom_label.create_label(self, text="Password:")
        self.password_label.grid(row=4, column=0, pady=5)
        self.password_entry = self.custom_input.create_input(self, textvariable=self.password, show="*")
        self.password_entry.grid(row=4, column=1, pady=5)

        # Confirm Password Entry
        self.confirm_password_label = self.custom_label.create_label(self, text="Confirm Password:")
        self.confirm_password_label.grid(row=5, column=0, pady=5)
        self.confirm_password_entry = self.custom_input.create_input(self, textvariable=self.confirm_password, show="*")
        self.confirm_password_entry.grid(row=5, column=1, pady=5)

        # Register Button
        self.register_button = self.custom_button_register.create_button(self)
        self.register_button.grid(row=6, column=0, pady=10)

        # Login Button
        self.login_button = self.custom_button_login.create_button(self)
        self.login_button.grid(row=6, column=1, pady=10)

    def is_running_as_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except AttributeError:
            # If the function is not available, it means the operating system is not Windows
            return False

    def register_user(self):
        if not self.is_running_as_admin():
            messagebox.showwarning("Warning", "This operation requires administrator privileges.")
            return

        name = self.username.get()
        email = self.email.get()
        phone = self.phone.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()

        if password == confirm_password:
            if Employee.getEmployeeByEmail(email):
                messagebox.showwarning("Warning", "Email already exists.")
                return
            
            if Employee.getEmployeeByPhone(phone):
                messagebox.showwarning("Warning", "Phone already exists.")
                return
            
            if name and email and phone and password:
                create_employee(name, email, phone, password)
                messagebox.showinfo("Success", "User created successfully.")
                self.show_frame("login")
            else:
                messagebox.showwarning("Warning", "All fields must be completed.")
        else:
            messagebox.showwarning("Warning", "Passwords do not match.")
