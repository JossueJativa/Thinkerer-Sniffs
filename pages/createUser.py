import tkinter as tk
from tkinter import messagebox, ttk
from functions import createUser
from classes import User

def create_users_page(notebook):
    frame_users = tk.Frame(notebook)
    notebook.add(frame_users, text="Crear Usuarios")
    
    # Variables for entries
    var_nombre = tk.StringVar()
    var_email = tk.StringVar()
    var_celular = tk.StringVar()
    var_cedula = tk.StringVar()

    def add_user():
        nombre = var_nombre.get()
        email = var_email.get()
        celular = var_celular.get()
        cedula = var_cedula.get()
        
        if not nombre or not email or not celular or not cedula:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return
        
        success = createUser(nombre, email, celular, cedula)
        if success:
            update_user_table()
            clear_entries()
            messagebox.showinfo("Éxito", "Usuario agregado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo agregar el usuario.")
    
    def update_user_table():
        # Clear the existing table rows
        for row in table.get_children():
            table.delete(row)
        
        # Fetch users and update the table
        users = User.getAllUsers()
        for user in users:
            table.insert("", "end", values=(user['Nombre'], user['Email'], user['Celular'], user['Cédula']))
    
    def clear_entries():
        var_nombre.set("")
        var_email.set("")
        var_celular.set("")
        var_cedula.set("")
    
    tk.Label(frame_users, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(frame_users, textvariable=var_nombre).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame_users, text="Email:").grid(row=0, column=2, padx=10, pady=10)
    tk.Entry(frame_users, textvariable=var_email).grid(row=0, column=3, padx=10, pady=10)

    tk.Label(frame_users, text="Celular:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(frame_users, textvariable=var_celular).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(frame_users, text="Cédula:").grid(row=1, column=2, padx=10, pady=10)
    tk.Entry(frame_users, textvariable=var_cedula).grid(row=1, column=3, padx=10, pady=10)

    # Create and place the button to add a user
    btn_add_user = tk.Button(frame_users, text="Agregar Usuario", command=add_user)
    btn_add_user.grid(row=2, column=0, columnspan=4, pady=10)

    # Create and place the table to display users
    columns = ("Nombre", "Email", "Celular", "Cédula")
    table = ttk.Treeview(frame_users, columns=columns, show="headings")
    table.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
    
    for col in columns:
        table.heading(col, text=col)
    
    # Populate the table with existing users
    update_user_table()