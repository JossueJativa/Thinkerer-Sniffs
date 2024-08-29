from data.controllerData import getDataFile

class Product:
    def __init__(self, id, name, stock, mensual_sales, installation, price):
        self.id = id
        self.name = name
        self.stock = stock
        self.mensual_sales = mensual_sales
        self.installation = installation
        self.price = price

    def getProduct(self):
        return self.id, self.name, self.stock, self.mensual_sales, self.installation, self.price
    
    @staticmethod
    def getAllProducts():
        try:
            products = getDataFile("Productos")
            product_data = []
            for index, product in products.iterrows():
                product_data.append({
                    'ID': product['ID'],
                    'Nombre': product['Nombre'],
                    'Stock': product['Stock'],
                    'Ventas Mensuales': product['Ventas Mensuales'],
                    'Instalación': product['Instalación'],
                    'Precio': product['Precio']
                })
            return product_data
        except Exception as e:
            print(f"Error: {e}")
            return []
        
    @staticmethod
    def getProductByID(id):
        products = Product.getAllProducts()
        product = next((p for p in products if p['ID'] == id), None)
        return product
