import customtkinter as ctk
from tkinter import messagebox

from widgets import Custom_Input, Custom_Label, Custom_Button, Colors

class create_home_page(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback):
        super().__init__(parent)
        self.show_frame = show_frame_callback

        width = 1200
        height = 800
        self.configure(
            width=width,
            height=height,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a navbar frame
        self.navbar_frame = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.navbar_frame.grid(row=0, column=0, sticky="ew")

        # Navbar buttons
        self.button_billing = ctk.CTkButton(
            self.navbar_frame, text="Facturación", command=lambda: self.show_frame("home"))
        self.button_billing.grid(row=0, column=0, padx=10, pady=5)

        self.button_create_user = ctk.CTkButton(
            self.navbar_frame, text="Creación de usuarios", command=lambda: self.show_frame("users"))
        self.button_create_user.grid(row=0, column=1, padx=10, pady=5)

        self.button_product_list = ctk.CTkButton(
            self.navbar_frame, text="Lista de productos", command=lambda: self.show_frame("products"))
        self.button_product_list.grid(row=0, column=2, padx=10, pady=5)

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

        self.custom_button_logout = Custom_Button(
            text="Logout",
            command=self.logout,
            fg_color=Colors.secondary,
            hover_color=Colors.danger
        )

        # Page content
        self.welcome_label = self.custom_label.create_label(self, text="Welcome to the home page")
        self.welcome_label.grid(row=1, column=0, pady=5)

        self.logout_button = self.custom_button_logout.create_button(self)
        self.logout_button.grid(row=2, column=0, pady=5)

    def logout(self):
        self.show_frame("login")