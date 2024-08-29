import tkinter as tk
from tkinter import ttk
from pages import create_home_page, create_products_page, create_users_page

def minimize_window():
    root.iconify()

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)

def close_window():
    root.destroy()

# Configuración principal de la ventana
root = tk.Tk()
root.title("Facturador Sniffs")
root.geometry("1320x950")

logo_path = "img/icono-logo_1.png"
root.iconphoto(True, tk.PhotoImage(file=logo_path))

# Iniciar en pantalla completa
fullscreen = True
root.attributes('-fullscreen', fullscreen)

# Crear un Frame para los botones de control de ventana
title_bar = tk.Frame(root, bg="grey", relief="raised", bd=0)
title_bar.pack(fill=tk.X)

# Crear botón de cerrar
btn_close = tk.Button(title_bar, text="X", command=close_window, bg="grey", fg="white", bd=0, padx=10, pady=5)
btn_close.pack(side=tk.RIGHT)

# Crear botón de reducir pantalla (cambiar entre pantalla completa y ventana)
btn_toggle_fullscreen = tk.Button(title_bar, text="[]", command=toggle_fullscreen, bg="grey", fg="white", bd=0, padx=10, pady=5)
btn_toggle_fullscreen.pack(side=tk.RIGHT, padx=5)

# Crear botón de minimizar
btn_minimize = tk.Button(title_bar, text="_", command=minimize_window, bg="grey", fg="white", bd=0, padx=10, pady=5)
btn_minimize.pack(side=tk.RIGHT, padx=5)

# Crear el widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Agregar páginas al Notebook
create_home_page(notebook)
create_products_page(notebook)
create_users_page(notebook)

root.mainloop()
