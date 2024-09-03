import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from classes import Employee
from functions.authentication import create_employee
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors

class create_register_page(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback):
        super().__init__(parent)
        self.show_frame = show_frame_callback

        # Configure the size of the CTkFrame
        width = 1200
        height = 800
        self.configure(width=width, height=height)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
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

        # Create and place entries and labels
        self.create_and_place_entries()

        # Register and Login Buttons
        self.register_button = self.custom_button_register.create_button(self)
        self.register_button.grid(row=6, column=0, pady=10)

        self.login_button = self.custom_button_login.create_button(self)
        self.login_button.grid(row=6, column=1, pady=10)

    def create_and_place_entries(self):
        # Username Entry
        self.username_label = self.custom_label.create_label(self, text="Username:")
        self.username_label.grid(row=1, column=0, pady=5)
        self.username_entry = self.custom_input.create_input(self, textvariable=self.username)
        self.username_entry.grid(row=1, column=1, pady=5)

        # Email Entry
        self.email_label = self.custom_label.create_label(self, text="Email:")
        self.email_label.grid(row=2, column=0, pady=5)
        self.email_entry = self.custo
