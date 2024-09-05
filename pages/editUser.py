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
        self.configure(
            width=width,
            height=height,
        )

        self.var_name = ctk.StringVar()
        self.var_email = ctk.StringVar()
        self.var_phone = ctk.StringVar()
        self.var_password = ctk.StringVar()
        self.user_id = None

        self.users = [user[1] for user in get_users()]
        self.user_var = ctk.StringVar(value="Seleccione un usuario")
        self.user_dropdown = ctk.CTkOptionMenu(self, values=self.users, variable=self.user_var, command=self.select_user)
        self.user_dropdown.grid(row=1, column=0, padx=10, pady=10)

        labels = ["Nombre", "Email", "Teléfono", "Contraseña"]
        vars = [self.var_name, self.var_email, self.var_phone, self.var_password]

        for i, (label, var) in enumerate(zip(labels, vars)):
            Custom_Label(
                text_color=Colors.white,
                font=12
            ).create_label(self, text=label).grid(row=i+2, column=0, padx=10, pady=10)
            Custom_Input(
                bg_color=Colors.white,
                fg_color=Colors.black,
                text_color=Colors.black,
                width=300,
                height=30,
                border_radius=10
            ).create_input(self, textvariable=var).grid(row=i+2, column=1, padx=10, pady=10)

        self.custom_button_save = Custom_Button(
            text="Guardar Cambios",
            command=self.save_changes,
            fg_color=Colors.primary,
            hover_color=Colors.success
        )
        self.save_button = self.custom_button_save.create_button(self)
        self.save_button.grid(row=len(labels)+2, column=0, columnspan=2, pady=10)

        # Botón Volver a la página de usuarios
        self.custom_button_back = Custom_Button(
            text="Volver",
            command=lambda: self.show_frame("users"),
            fg_color=Colors.secondary,
            hover_color=Colors.danger
        )
        self.back_button = self.custom_button_back.create_button(self)
        self.back_button.grid(row=len(labels)+3, column=0, columnspan=2, pady=10)

    def select_user(self, selected_user_name):
        user = get_user_by_name(selected_user_name)
        if user:
            self.user_id = user['id']
            self.var_name.set(user['name'])
            self.var_email.set(user['email'])
            self.var_phone.set(user['phone'])
            self.var_password.set(user['password'])

    def save_changes(self):
        name = self.var_name.get()
        email = self.var_email.get()
        phone = self.var_phone.get()
        password = self.var_password.get()

        if not name or not email or not phone or not password:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return
        
        data = f"name = '{name}', email = '{email}', phone = '{phone}', password = '{password}'"

        try:
            update_user(self.user_id, data)
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except Exception as err:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el usuario: {err}")
