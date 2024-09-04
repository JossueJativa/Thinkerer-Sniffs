import customtkinter as ctk
from tkinter import messagebox
from data.generatePDF import generate_pdf
from widgets import Custom_Input, Custom_Label, Custom_Button, Colors
from functions import get_users, get_products

class create_home_page(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback):
        super().__init__(parent)
        self.show_frame = show_frame_callback

        # Configuración de la página
        width = 1200
        height = 800
        self.configure(width=width, height=height)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.username = ""

        # Crear la barra de navegación
        self.navbar_frame = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.navbar_frame.grid(row=0, column=0, sticky="ew")
        self.create_navbar_buttons()

        # Custom Label for the welcome message
        self.custom_label = Custom_Label(text_color=Colors.white, font=14)
        self.welcome_label = self.custom_label.create_label(self, text="Seleccione un usuario")
        self.welcome_label.grid(row=1, column=0, pady=5)

        # Entry for searching users by name
        self.search_entry = Custom_Input(
            bg_color=Colors.white,
            fg_color=Colors.black,
            text_color=Colors.black,
            width=200,  # Adjust width as needed
            height=30,  # Adjust height as needed
            border_radius=5
        ).create_input(self)
        self.search_entry.grid(row=2, column=0, padx=10, pady=5)
        self.search_entry.bind("<KeyRelease>", self.update_user_dropdown)

        # Dropdown to select user
        self.users = [user[1] for user in get_users()]
        self.user_var = ctk.StringVar(value="Seleccione un usuario")
        self.user_dropdown = ctk.CTkOptionMenu(self, values=self.users, variable=self.user_var, command=self.select_user)
        self.user_dropdown.grid(row=3, column=0, padx=10, pady=5)

        # Frame to hold product table
        self.products_frame = ctk.CTkFrame(self)
        self.products_frame.grid(row=5, column=0, pady=10)

        # Buttons for calculating total and generating PDF
        self.calculate_button = ctk.CTkButton(self, text="Calcular Total", command=self.calculate_totals)
        self.calculate_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.generate_pdf_button = ctk.CTkButton(self, text="Generar PDF", command=self.generate_pdf)
        self.generate_pdf_button.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    def create_navbar_buttons(self):
        self.button_billing = ctk.CTkButton(self.navbar_frame, text="Facturación", command=lambda: self.show_frame("home"))
        self.button_billing.grid(row=0, column=0, padx=10, pady=5)
        self.button_create_user = ctk.CTkButton(self.navbar_frame, text="Creación de usuarios", command=lambda: self.show_frame("users"))
        self.button_create_user.grid(row=0, column=1, padx=10, pady=5)
        self.button_product_list = ctk.CTkButton(self.navbar_frame, text="Lista de productos", command=lambda: self.show_frame("products"))
        self.button_product_list.grid(row=0, column=2, padx=10, pady=5)

    def update_user_dropdown(self, event):
        search_term = self.search_entry.get().lower()
        filtered_users = [user for user in self.users if search_term in user.lower()]
        if filtered_users:
            self.user_dropdown.configure(values=filtered_users)
        else:
            self.user_dropdown.configure(values=["No se encontraron usuarios"])
            self.user_var.set("No se encontraron usuarios")

    def select_user(self, user):
        if user and user != "No se encontraron usuarios":
            self.username = user
            self.show_products()

    def show_products(self):
        # Clear previous product widgets
        for widget in self.products_frame.winfo_children():
            widget.destroy()

        # Fetch products
        products = get_products()

        # Create header row
        headers = ["Seleccionar", "Nombre", "Precio", "Instalación", "Precio Mensual", "Cantidad", "Meses/Años", "% Descuento"]
        for col, header in enumerate(headers):
            header_label = self.custom_label.create_label(self.products_frame, text=header)
            header_label.grid(row=0, column=col, padx=5, pady=5, sticky="w")

        # Create a row for each product
        self.check_vars = []
        self.quantity_entries = []
        self.duration_entries = []
        self.discount_entries = []

        for index, product in enumerate(products):
            product_name, price, mensual_sales, instal = product[1], product[5], product[3], product[4]

            check_var = ctk.IntVar()
            checkbox = ctk.CTkCheckBox(self.products_frame, variable=check_var, text=f"{index+1}")
            checkbox.grid(row=index+1, column=0, padx=5, pady=2, sticky="w")

            name_label = ctk.CTkLabel(self.products_frame, text=product_name)
            name_label.grid(row=index+1, column=1, padx=5, pady=2, sticky="w")

            price_label = ctk.CTkLabel(self.products_frame, text=f"${price}")
            price_label.grid(row=index+1, column=2, padx=5, pady=2, sticky="w")

            instal_label = ctk.CTkLabel(self.products_frame, text=f"${instal}")
            instal_label.grid(row=index+1, column=3, padx=5, pady=2, sticky="w")

            mensual_sales_label = ctk.CTkLabel(self.products_frame, text=f"${mensual_sales}")
            mensual_sales_label.grid(row=index+1, column=4, padx=5, pady=2, sticky="w")

            # Entry for specifying quantity
            quantity_entry = ctk.CTkEntry(self.products_frame, width=50)
            quantity_entry.grid(row=index+1, column=5, padx=5, pady=2, sticky="w")

            # Entry for specifying duration (months/years)
            duration_entry = ctk.CTkEntry(self.products_frame, width=50)
            duration_entry.grid(row=index+1, column=6, padx=5, pady=2, sticky="w")

            # Entry for specifying discount percentage with default value 0
            discount_entry = ctk.CTkEntry(self.products_frame, width=50)
            discount_entry.insert(0, "0")  # Set default discount value to 0
            discount_entry.grid(row=index+1, column=7, padx=5, pady=2, sticky="w")

            # Store references
            self.check_vars.append(check_var)
            self.quantity_entries.append(quantity_entry)
            self.duration_entries.append(duration_entry)
            self.discount_entries.append(discount_entry)

    def calculate_totals(self):
        subtotal = 0
        total_discount = 0

        for i, check_var in enumerate(self.check_vars):
            if check_var.get() == 1:  # Solo incluir productos seleccionados
                try:
                    # Obtener el precio y otras entradas
                    price = float(self.products_frame.grid_slaves(row=i+1, column=2)[0].cget("text").replace("$", ""))
                    installation = float(self.products_frame.grid_slaves(row=i+1, column=3)[0].cget("text").replace("$", ""))
                    quantity = int(self.quantity_entries[i].get())
                    discount_percent = float(self.discount_entries[i].get())
                    
                    # Calcular el total para el producto
                    total = (price * quantity) + (installation * quantity)
                    discount = total * (discount_percent / 100)
                    
                    # Acumulando descuento total y subtotal
                    total_discount += discount
                    subtotal += total - discount

                except ValueError:
                    messagebox.showerror("Error", "Ingrese valores válidos en las entradas.")
                    return

        # Calcular IVA (15%)
        iva = subtotal * 0.15
        total = subtotal + iva

        # Mostrar los resultados en un cuadro de mensaje
        messagebox.showinfo("Totales", f"Subtotal: ${subtotal:.2f}\nDescuento Total: ${total_discount:.2f}\nIVA (15%): ${iva:.2f}\nTotal: ${total:.2f}")

    def generate_pdf(self):
        subtotal = 0
        total_discount = 0

        selected_products_list = []
        for i, check_var in enumerate(self.check_vars):
            if check_var.get() == 1:  # Solo incluir productos seleccionados
                try:
                    # Obtener el precio y otras entradas
                    price = float(self.products_frame.grid_slaves(row=i+1, column=2)[0].cget("text").replace("$", ""))
                    installation = float(self.products_frame.grid_slaves(row=i+1, column=3)[0].cget("text").replace("$", ""))
                    quantity = int(self.quantity_entries[i].get())
                    discount_percent = float(self.discount_entries[i].get())
                    
                    # Calcular el total para el producto
                    total = (price * quantity) + (installation * quantity)
                    discount = total * (discount_percent / 100)
                    
                    # Acumulando subtotal y descuento total
                    total_discount += discount
                    subtotal += total - discount
                    
                    # Agregar producto a la lista de productos
                    product_name = self.products_frame.grid_slaves(row=i+1, column=1)[0].cget("text")
                    # Selected products list = Nombre, Precio, Cantidad, Meses, total
                    selected_products_list.append({
                        "Nombre": product_name,
                        "Precio": price,
                        "Cantidad": quantity,
                        "Meses": self.duration_entries[i].get(),
                        "Total": total - discount
                    })

                except ValueError:
                    messagebox.showerror("Error", "Ingrese valores válidos en las entradas.")
                    return

        # Calcular IVA (15%)
        iva = subtotal * 0.15
        total = subtotal + iva

        # Generar el PDF con la información de la factura
        try:
            generate_pdf(self.username, selected_products_list, subtotal, iva, total, total_discount)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el PDF. {e}")