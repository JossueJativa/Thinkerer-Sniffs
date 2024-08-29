import tkinter as tk
from tkinter import messagebox, ttk
from functions import createProduct
from classes import Product

def create_products_page(notebook):
    frame_products = tk.Frame(notebook)
    notebook.add(frame_products, text="Crear Productos")
    
    # Variables for entries
    var_id = tk.StringVar()
    var_name = tk.StringVar()
    var_stock = tk.StringVar()
    var_mensual_sales = tk.StringVar()
    var_installation = tk.StringVar()
    var_price = tk.StringVar()

    def add_product():
        id = var_id.get()
        name = var_name.get()
        stock = var_stock.get()
        mensual_sales = var_mensual_sales.get()
        installation = var_installation.get()
        price = var_price.get()
        
        if not id or not name or not stock or not mensual_sales or not installation or not price:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return
        
        success = createProduct(id, name, stock, mensual_sales, installation, price)
        if success:
            update_product_table()
            clear_entries()
            messagebox.showinfo("Éxito", "Producto agregado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo agregar el producto.")
    
    def update_product_table():
        # Clear the existing table rows
        for row in table.get_children():
            table.delete(row)
        
        # Fetch products and update the table
        products = Product.getAllProducts()
        for product in products:
            table.insert("", "end", values=(
                product['ID'],
                product['Nombre'],
                product['Stock'],
                product['Ventas Mensuales'],
                product['Instalación'],
                product['Precio']
            ))
    
    def clear_entries():
        var_id.set("")
        var_name.set("")
        var_stock.set("")
        var_mensual_sales.set("")
        var_installation.set("")
        var_price.set("")
    
    # Layout for product entry fields
    tk.Label(frame_products, text="ID:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(frame_products, textvariable=var_id).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame_products, text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(frame_products, textvariable=var_name).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(frame_products, text="Stock:").grid(row=2, column=0, padx=10, pady=10)
    tk.Entry(frame_products, textvariable=var_stock).grid(row=2, column=1, padx=10, pady=10)

    tk.Label(frame_products, text="Ventas Mensuales:").grid(row=3, column=0, padx=10, pady=10)
    tk.Entry(frame_products, textvariable=var_mensual_sales).grid(row=3, column=1, padx=10, pady=10)

    tk.Label(frame_products, text="Instalación:").grid(row=4, column=0, padx=10, pady=10)
    tk.Entry(frame_products, textvariable=var_installation).grid(row=4, column=1, padx=10, pady=10)

    tk.Label(frame_products, text="Precio:").grid(row=5, column=0, padx=10, pady=10)
    tk.Entry(frame_products, textvariable=var_price).grid(row=5, column=1, padx=10, pady=10)

    # Create and place a button to add the product
    btn_add_product = tk.Button(frame_products, text="Agregar Producto", command=add_product)
    btn_add_product.grid(row=6, column=0, columnspan=2, pady=10)

    # Create and place a table to display products
    columns = ("ID", "Nombre", "Stock", "Ventas Mensuales", "Instalación", "Precio")
    table = ttk.Treeview(frame_products, columns=columns, show="headings")
    table.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    for col in columns:
        table.heading(col, text=col)

    # Populate the table with existing products
    update_product_table()