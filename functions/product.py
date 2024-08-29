from classes import Product
from data.controllerData import writeFile, getDataFile

def createProduct(id, name, stock, mensual_sales, installation, price):
    # Crear una instancia del producto
    product = Product(
        id=id,
        name=name,
        stock=stock,
        mensual_sales=mensual_sales,
        installation=installation,
        price=price
    )
    product_info = product.getProduct()

    header = ['ID', 'Nombre', 'Stock', 'Ventas Mensuales', 'Instalación', 'Precio']
    sheetname = 'Productos'
    is_written = writeFile(sheetname, header, product_info)

    return is_written