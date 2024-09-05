import customtkinter as ctk
from tkinter import messagebox
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors
from functions import update_user, get_users, get_user_by_name

class edit_users_page(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback):
        super().__init__(parent)
        self.show_frame = show_frame_callback

        width = 1200
        height = 800
        self.configure(width=width, height=height)

        self.var_name = ctk.StringVar()
        self.var_email = ctk.StringVar()
        self.var_phone = ctk.StringVar()
        self.var_identity = ctk.StringVar()
        self.user_id = None

        self.users = [user[1] for user in get_users()]
        self.filtered_users = self.users.copy()
        self.user_var = ctk.StringVar(value="Seleccione un usuario")

        # Entry for searching users by name
        self.search_entry = Custom_Input(
            bg_color=Colors.white,
            fg_color=Colors.black,
            text_color=Colors.black,
            width=200,
            height=30,
            border_radius=5
        ).create_input(self)
        self.search_entry.grid(row=1, column=0, padx=10, pady=10)
        self.search_entry.bind("<KeyRelease>", self.update_user_dropdown)

        # Dropdown to select user
        self.user_dropdown = ctk.CTkOptionMenu(self, values=self.filtered_users, variable=self.user_var, command=self.select_user)
        self.user_dropdown.grid(row=2, column=0, padx=10, pady=10)

        labels = ["Nombre", "Email", "Celular", "Cédula"]
        vars = [self.var_name, self.var_email, self.var_phone, self.var_identity]

        for i, (label, var) in enumerate(zip(labels, vars)):
            Custom_Label(
                text_color=Colors.white,
                font=12
            ).create_label(self, text=label).grid(row=i+3, column=0, padx=10, pady=10)
            Custom_Input(
                bg_color=Colors.white,
                fg_color=Colors.black,
                text_color=Colors.black,
                width=300,
                height=30,
                border_radius=10
            ).create_input(self, textvariable=var).grid(row=i+3, column=1, padx=10, pady=10)

        self.custom_button_save = Custom_Button(
            text="Guardar Cambios",
            command=self.save_changes,
            fg_color=Colors.primary,
            hover_color=Colors.success
        )
        self.save_button = self.custom_button_save.create_button(self)
        self.save_button.grid(row=len(labels)+3, column=0, columnspan=2, pady=10)

        # Botón Volver a la página de usuarios
        self.custom_button_back = Custom_Button(
            text="Volver",
            command=lambda: self.show_frame("users"),
            fg_color=Colors.secondary,
            hover_color=Colors.danger
        )
        self.back_button = self.custom_button_back.create_button(self)
        self.back_button.grid(row=len(labels)+4, column=0, columnspan=2, pady=10)

    def update_user_dropdown(self, event):
        search_term = self.search_entry.get().lower()
        self.filtered_users = [user for user in self.users if search_term in user.lower()]
        if not self.filtered_users:
            self.filtered_users = ["No se encontraron usuarios"]
        self.user_dropdown.configure(values=self.filtered_users)
        if self.filtered_users and self.filtered_users[0] != "No se encontraron usuarios":
            self.user_var.set(self.filtered_users[0])

    def select_user(self, selected_user_name):
        if selected_user_name and selected_user_name != "No se encontraron usuarios":
            user = get_user_by_name(selected_user_name)
            if user:
                self.user_id = user['id']
                self.var_name.set(user['Nombre'])
                self.var_email.set(user['email'])
                self.var_phone.set(user['Celular'])
                self.var_identity.set(user['Cédula'])

    def save_changes(self):
        name = self.var_name.get()
        email = self.var_email.get()
        phone = self.var_phone.get()
        identity_card = self.var_identity.get()

        if not name or not email or not phone or not identity_card:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return
        
        data = f"name = '{name}', email = '{email}', phone = '{phone}', identity_card = '{identity_card}'"

        try:
            update_user(self.user_id, data)
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except Exception as err:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el usuario: {err}")