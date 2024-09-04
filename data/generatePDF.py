from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from datetime import datetime
import os
from functions import get_user_by_name
from tkinter import messagebox

def generate_pdf(userName, selected_products_list, subtotal, iva, total, total_discount=0):
    # Get current date and time for the unique code
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    code = f"INV_{current_time}"

    # Get the complete user data
    user = get_user_by_name(userName)
    if not user:
        messagebox.showerror("Error", "No se pudo encontrar la información del cliente")
        return
    
    client_name = user['Nombre']
    client_phone = user['Celular']
    client_id = user['Cédula']

    if not os.path.exists('facturas'):
        os.makedirs('facturas')

    pdf_path = f"facturas/cotizacion_{code}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Colors
    primary_color = HexColor("#131738")
    gray_color = colors.HexColor("#A9A9A9")

    # Header Section
    logo = "img/logo.png"
    c.drawImage(logo, 60, 720, width=60, height=60, mask='auto')  # 'mask="auto"' makes the background transparent

    # Company Information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(120, 760, "COTIZACION No.:")
    c.drawString(220, 760, code)
    c.drawString(120, 740, "Crystian Muñoz")
    
    c.setFont("Helvetica", 10)
    c.drawString(120, 720, "RUC: 1715838692001")
    c.drawString(220, 720, "Japón N37-214 y Pasaje Mónaco")
    c.drawString(120, 700, "Tel(f): (+593) 996761198")

    # Line Separator - Between Header and Client Information
    c.setStrokeColor(gray_color)
    c.line(40, 690, 550, 690)  # Line from x=40 to x=550 at y=690

    # Add additional space after line
    y_position = 670  # Start a bit lower after the line separator

    # Client details in a table format
    c.setFont("Helvetica-Bold", 10)
    client_details = [
        ["CLIENTE:", client_name, "TELÉFONO:", client_phone],
        ["RUC/CÉDULA:", client_id, "DIRECCIÓN:", "QUITO"],
        ["ATENCIÓN:", "", "VENDEDOR:", "VENDEDOR"],
        ["VÁLIDO POR:", "0 Días", "FECHA:", datetime.now().strftime("%d/%m/%Y")]
    ]

    for detail in client_details:
        c.drawString(60, y_position, detail[0])
        c.drawString(160, y_position, str(detail[1]))
        c.drawString(300, y_position, detail[2])
        c.drawString(400, y_position, str(detail[3]))
        y_position -= 20

    # Spacer after client details
    y_position -= 10

    # Product details
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(primary_color)
    c.drawString(60, y_position, "Producto")
    c.drawString(180, y_position, "Cantidad")
    c.drawString(300, y_position, "Meses")
    c.drawString(400, y_position, "Precio Unitario")
    c.drawString(500, y_position, "Total")

    y_position -= 20  # Move to the next line

    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    for product in selected_products_list:
        c.drawString(60, y_position, str(product['Nombre']))
        c.drawString(180, y_position, str(product['Cantidad']))
        c.drawString(300, y_position, str(product['Meses']))
        c.drawString(400, y_position, f"${product['Precio']:.2f}")
        c.drawString(500, y_position, f"${product['Total']:.2f}")
        y_position -= 20  # Adjust for next line

    # Spacer after product table
    y_position -= 10

    # Total amounts with discount
    c.drawString(60, y_position, f"Subtotal: ${subtotal:.2f}")
    y_position -= 15
    c.drawString(60, y_position, f"Descuento Total: ${total_discount:.2f}")
    y_position -= 15
    c.drawString(60, y_position, f"IVA (15%): ${iva:.2f}")
    y_position -= 15
    c.drawString(60, y_position, f"Total: ${total:.2f}")

    # Save PDF
    c.save()

    # Show success message
    messagebox.showinfo("Éxito", f"Factura generada con éxito. Código: {code}\nGuardado en: {pdf_path}")