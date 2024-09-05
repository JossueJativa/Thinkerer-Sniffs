import customtkinter as ctk
from tkinter import ttk, messagebox
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors
from functions import create_user
from classes import User

class create_users_page(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback):
        super().__init__(parent)
        self.show_frame = show_frame_callback

        # Configure the size of the CTkFrame
        width = 1200
        height = 800
        self.configure(
            width=width,
            height=height,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Create a navbar frame
        self.navbar_frame = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.navbar_frame.grid(row=0, column=0, columnspan=4, sticky="ew")

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

        self.button_refresh = ctk.CTkButton(
            self.navbar_frame, text="Actualizar", command=self.refresh_page)
        self.button_refresh.grid(row=0, column=3, padx=10, pady=5)

        # Move "Actualizar" button below "Editar Usuario"
        self.custom_button_edit = Custom_Button(
            text="Editar Usuario",
            command=lambda: self.show_frame("editarUsuario"),
            fg_color=Colors.primary,
            hover_color=Colors.warning
        )
        self.edit_button = self.custom_button_edit.create_button(self)
        self.edit_button.grid(row=1, column=0, columnspan=4, pady=10)

        # Variables for entries
        self.var_nombre = ctk.StringVar()
        self.var_email = ctk.StringVar()
        self.var_celular = ctk.StringVar()
        self.var_cedula = ctk.StringVar()

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

        self.custom_button_add = Custom_Button(
            text="Agregar Usuario",
            command=self.add_user,
            fg_color=Colors.primary,
            hover_color=Colors.success
        )

        # Create and place labels and entries
        labels = ["Nombre", "Email", "Celular", "Cédula"]
        vars = [self.var_nombre, self.var_email, self.var_celular, self.var_cedula]

        for i, (label, var) in enumerate(zip(labels, vars)):
            self.custom_label.create_label(self, text=label).grid(row=i+2, column=0, padx=10, pady=10)
            self.custom_input.create_input(self, textvariable=var).grid(row=i+2, column=1, padx=10, pady=10)

        # Create and place the button to add the user
        self.add_button = self.custom_button_add.create_button(self)
        self.add_button.grid(row=len(labels)+2, column=0, columnspan=2, pady=10)

        # Create and place a table to display users using ttk.Treeview
        columns = ("id", "Nombre", "Email", "Celular", "Cédula")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        self.table.grid(row=len(labels)+3, column=0, columnspan=2, padx=10, pady=10)

        for col in columns:
            self.table.heading(col, text=col)

        self.update_user_table()

    def add_user(self):
        nombre = self.var_nombre.get()
        email = self.var_email.get()
        celular = self.var_celular.get()
        cedula = self.var_cedula.get()

        if not nombre or not email or not celular or not cedula:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return

        user_id = create_user(nombre, email, celular, cedula)
        if user_id:
            messagebox.showinfo("Información", "Usuario agregado correctamente.")
            self.update_user_table()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "No se pudo agregar el usuario.")

    def update_user_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        users = User.getUsers()
        for user in users:
            self.table.insert("", "end", values=user)

    def clear_entries(self):
        self.var_nombre.set("")
        self.var_email.set("")
        self.var_celular.set("")
        self.var_cedula.set("")

    def refresh_page(self):
        """Function to refresh or reload the page"""
        self.update_user_table()
        self.clear_entries()
        messagebox.showinfo("Información", "Página actualizada con éxito.")