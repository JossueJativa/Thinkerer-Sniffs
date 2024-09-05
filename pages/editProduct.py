import customtkinter as ctk
from tkinter import messagebox
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors
from functions import update_product, get_products, get_product_by_name

class edit_products_page(ctk.CTkFrame):
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
        self.var_stock = ctk.StringVar()
        self.var_mensual_sales = ctk.StringVar()
        self.var_installation = ctk.StringVar()
        self.var_price = ctk.StringVar()
        self.product_id = None

        self.products = [product[1] for product in get_products()]
        self.product_var = ctk.StringVar(value="Seleccione un producto")
        self.product_dropdown = ctk.CTkOptionMenu(self, values=self.products, variable=self.product_var, command=self.select_product)
        self.product_dropdown.grid(row=1, column=0, padx=10, pady=10)

        labels = ["Nombre", "Stock", "Ventas Mensuales", "Instalación", "Precio"]
        vars = [self.var_name, self.var_stock, self.var_mensual_sales, self.var_installation, self.var_price]

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

        # Botón Volver a la página de productos
        self.custom_button_back = Custom_Button(
            text="Volver",
            command=lambda: self.show_frame("products"),
            fg_color=Colors.secondary,
            hover_color=Colors.danger
        )
        self.back_button = self.custom_button_back.create_button(self)
        self.back_button.grid(row=len(labels)+3, column=0, columnspan=2, pady=10)

    def select_product(self, selected_product_name):
        product = get_product_by_name(selected_product_name)
        if product:
            self.product_id = product['id']
            self.var_name.set(product['name'])
            self.var_stock.set(product['stock'])
            self.var_mensual_sales.set(product['mensual_sales'])
            self.var_installation.set(product['installation'])
            self.var_price.set(product['price'])

    def save_changes(self):
        name = self.var_name.get()
        stock = self.var_stock.get()
        mensual_sales = self.var_mensual_sales.get()
        installation = self.var_installation.get()
        price = self.var_price.get()

        if not name or not stock or not mensual_sales or not installation or not price:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return
        
        data = f"name = '{name}', stock = {stock}, mensual_sales = {mensual_sales}, installation = {installation}, price = {price}"

        try:
            update_product(self.product_id, data)
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        except Exception as err:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el producto: {err}")