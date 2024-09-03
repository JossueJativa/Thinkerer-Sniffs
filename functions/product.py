from classes import Product

def get_products():
    products = Product.getProducts()
    return products

def get_product_by_id(id):
    product = Product.getProductById(id)
    return product

def get_product_by_name(name):
    product = Product.getProductByName(name)
    return product

def create_product(name, stock, mensual_sales, installation, price):
    product_id = Product.createProduct(name, stock, mensual_sales, installation, price)
    return product_id

def update_product(id, data):
    Product.updateProduct(id, data)

def delete_product(id):
    Product.deleteProduct(id)