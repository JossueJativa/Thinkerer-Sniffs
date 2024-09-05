import customtkinter as ctk
from tkinter import ttk, messagebox
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors
from classes import Product
from functions import create_product
import ctypes

class create_products_page(ctk.CTkFrame):
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create a navbar frame
        self.navbar_frame = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.navbar_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

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

        # Add "Actualizar" button below "Editar Producto"
        self.button_refresh = ctk.CTkButton(
            self.navbar_frame, text="Actualizar", command=self.refresh_page)
        self.button_refresh.grid(row=0, column=3, padx=10, pady=5)

        # Move "Actualizar" button below "Editar Producto"
        self.custom_button_edit = Custom_Button(
            text="Editar Producto",
            command=lambda: self.show_frame("editarProducto"),
            fg_color=Colors.primary,
            hover_color=Colors.warning
        )
        self.edit_button = self.custom_button_edit.create_button(self)
        self.edit_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.var_name = ctk.StringVar()
        self.var_stock = ctk.StringVar()
        self.var_mensual_sales = ctk.StringVar()
        self.var_installation = ctk.StringVar()
        self.var_price = ctk.StringVar()

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
            text="Agregar Producto",
            command=self.add_product,
            fg_color=Colors.primary,
            hover_color=Colors.success
        )

        # Create and place labels and entries
        labels = ["Nombre", "Stock", "Ventas Mensuales", "Instalación", "Precio"]
        vars = [self.var_name, self.var_stock, self.var_mensual_sales, self.var_installation, self.var_price]

        for i, (label, var) in enumerate(zip(labels, vars)):
            self.custom_label.create_label(self, text=label).grid(row=i+3, column=0, padx=10, pady=10)
            self.custom_input.create_input(self, textvariable=var).grid(row=i+3, column=1, padx=10, pady=10)

        # Create and place the button to add the product
        self.add_button = self.custom_button_add.create_button(self)
        self.add_button.grid(row=len(labels)+3, column=0, columnspan=2, pady=10)

        # Create and place a table to display products using ttk.Treeview
        columns = ("ID", "Nombre", "Stock", "Ventas Mensuales", "Instalación", "Precio")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        self.table.grid(row=len(labels)+4, column=0, columnspan=2, padx=10, pady=10)

        for col in columns:
            self.table.heading(col, text=col)

        self.update_product_table()

    def is_running_as_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except AttributeError:
            # If the function is not available, it means the operating system is not Windows
            return False

    def add_product(self):
        if not self.is_running_as_admin():
            messagebox.showwarning("Advertencia", "Este proceso requiere privilegios de administrador.")
            return

        name = self.var_name.get()
        stock = self.var_stock.get()
        mensual_sales = self.var_mensual_sales.get()
        installation = self.var_installation.get()
        price = self.var_price.get()

        if not name or not stock or not mensual_sales or not installation or not price:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return

        success = create_product(name, stock, mensual_sales, installation, price)
        if success:
            self.update_product_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "Producto agregado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo agregar el producto.")

    def update_product_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        # Fetch products and update the table
        products = Product.getProducts()
        for product in products:
            self.table.insert("", "end", values=product)  # Directly use the tuple values

    def clear_entries(self):
        self.var_name.set("")
        self.var_stock.set("")
        self.var_mensual_sales.set("")
        self.var_installation.set("")
        self.var_price.set("")

    def refresh_page(self):
        self.update_product_table()
        self.clear_entries()
        messagebox.showinfo("Información", "Página actualizada con éxito.")
