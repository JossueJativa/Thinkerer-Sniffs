import tkinter as tk
from PIL import Image, ImageTk
from classes import User, Product
from data.generatePDF import generate_pdf

def create_home_page(notebook):
    frame_home = tk.Frame(notebook)
    notebook.add(frame_home, text="Inicio")

    welcome_label = tk.Label(frame_home, text="Bienvenido al Sistema de Facturación", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    frame_buttons = tk.Frame(frame_home)
    frame_buttons.pack(pady=20)

    def show_invoice_selection():
        for widget in frame_invoice_selection.winfo_children():
            widget.destroy()

        tk.Label(frame_invoice_selection, text="Selecciona un Usuario:").pack(pady=5)

        users = User.getAllUsers()
        user_names = [user['Nombre'] for user in users]
        user_var = tk.StringVar(value=user_names[0] if user_names else "")

        for user in user_names:
            tk.Radiobutton(frame_invoice_selection, text=user, variable=user_var, value=user).pack(anchor='w')

        tk.Label(frame_invoice_selection, text="Selecciona Productos:").pack(pady=5)

        table_frame = tk.Frame(frame_invoice_selection)
        table_frame.pack(pady=10, fill='x')

        headers = ['Seleccionar', 'ID', 'Nombre', 'Precio', 'Instalaciones', 'Meses/Años', 'Descuento', 'Descuento %', 'Descuento Calculado']
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, borderwidth=1, relief='solid', padx=5, pady=5).grid(row=0, column=col, sticky='nsew')

        products = Product.getAllProducts()

        product_vars = {}

        for row_num, product in enumerate(products, start=1):
            product_id = product['ID']
            product_name = product['Nombre']
            product_price = product['Precio']
            product_installation = product['Instalación']

            selected_var = tk.BooleanVar()
            discount_var = tk.BooleanVar()
            discount_entry = tk.Entry(table_frame, width=10)
            discount_calculated_label = tk.Label(table_frame, text="$0.00", borderwidth=1, relief='solid', padx=5, pady=5)

            tk.Checkbutton(table_frame, variable=selected_var).grid(row=row_num, column=0, padx=5, pady=5)
            tk.Label(table_frame, text=product_id, borderwidth=1, relief='solid', padx=5, pady=5).grid(row=row_num, column=1)
            tk.Label(table_frame, text=product_name, borderwidth=1, relief='solid', padx=5, pady=5).grid(row=row_num, column=2)
            tk.Label(table_frame, text=f"${product_price:.2f}", borderwidth=1, relief='solid', padx=5, pady=5).grid(row=row_num, column=3)
            
            installations_entry = tk.Entry(table_frame, width=10)
            installations_entry.grid(row=row_num, column=4, padx=5, pady=5)

            if product_id % 2 == 0:
                months_entry = tk.Entry(table_frame, width=10)
                months_entry.grid(row=row_num, column=5, padx=5, pady=5)
            else:
                months_entry = tk.Label(table_frame, text="1", borderwidth=1, relief='solid', padx=5, pady=5)
                months_entry.grid(row=row_num, column=5, padx=5, pady=5)

            tk.Checkbutton(table_frame, variable=discount_var).grid(row=row_num, column=6, padx=5, pady=5)
            discount_entry.grid(row=row_num, column=7, padx=5, pady=5)
            discount_calculated_label.grid(row=row_num, column=8, padx=5, pady=5)

            product_vars[product_id] = (selected_var, installations_entry, months_entry, discount_var, discount_entry, discount_calculated_label)

        summary_frame = tk.Frame(frame_invoice_selection)
        summary_frame.pack(pady=10, fill='x')

        subtotal_label = tk.Label(summary_frame, text="Subtotal: $0.00")
        subtotal_label.pack(pady=5)
        iva_label = tk.Label(summary_frame, text="IVA (15%): $0.00")
        iva_label.pack(pady=5)
        total_label = tk.Label(summary_frame, text="Total: $0.00")
        total_label.pack(pady=5)

        def update_summary():
            subtotal = 0
            total_discount = 0
            selected_products_list = []

            for product_id, (selected_var, installations_entry, months_entry, discount_var, discount_entry, discount_calculated_label) in product_vars.items():
                if selected_var.get():
                    product = Product.getProductByID(product_id)
                    if product:
                        product_price = product['Precio']
                        product_installation = product['Instalación']
                        installations = int(installations_entry.get() or 0)
                        if isinstance(months_entry, tk.Entry):
                            months = int(months_entry.get() or 0)
                        else:
                            months = int(months_entry.cget("text") or 0)
                        discount = float(discount_entry.get() or 0) / 100 if discount_var.get() else 0
                        total_price = ((installations * (product_price * months)) + (product_installation * installations)) * (1 - discount)
                        subtotal += total_price
                        discount_amount = ((installations * (product_price * months)) + (product_installation * installations)) * discount
                        total_discount += discount_amount
                        discount_calculated_label.config(text=f"${discount_amount:.2f}")
                        selected_products_list.append({
                            'Nombre': product['Nombre'],
                            'Instalaciones': installations,
                            'Meses': months,
                            'Precio': product_price,
                            'DescuentoPorcentaje': discount * 100,
                            'DescuentoMonto': discount_amount,
                            'Total': total_price
                        })

            iva = subtotal * 0.15
            total = subtotal + iva

            subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")
            iva_label.config(text=f"IVA (15%): ${iva:.2f}")
            total_label.config(text=f"Total: ${total:.2f}")

            return selected_products_list, subtotal, iva, total, total_discount

        btn_confirm = tk.Button(frame_invoice_selection, text="Confirmar Selección", command=lambda: update_summary())
        btn_confirm.pack(pady=10)

        btn_generate_pdf = tk.Button(frame_invoice_selection, text="Generar PDF", command=lambda: generate_pdf(user_var.get(), *update_summary()))
        btn_generate_pdf.pack(pady=10)

    btn_invoice = tk.Button(frame_buttons, text="Generar Factura", command=show_invoice_selection)
    btn_invoice.grid(row=0, column=2, padx=10)

    frame_invoice_selection = tk.Frame(frame_home)
    frame_invoice_selection.pack(pady=20)