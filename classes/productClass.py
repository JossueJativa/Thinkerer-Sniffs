from data.controllerData import read_table, insert_product, read_table_by_id, update_table, delete_table, read_table_by_condition

class Product:
    def __init__(self, id, name, stock, mensual_sales, installation, price):
        self.id = id
        self.name = name
        self.stock = stock
        self.mensual_sales = mensual_sales
        self.installation = installation
        self.price = price

    def getProduct(self):
        product = {
            "id": self.id,
            "name": self.name,
            "stock": self.stock,
            "mensual_sales": self.mensual_sales,
            "installation": self.installation,
            "price": self.price
        }
        return product
    
    @staticmethod
    def getProducts():
        try:
            products = read_table("products")
            return products
        except:
            return []
    
    @staticmethod
    def getProductById(id):
        product = read_table_by_id("products", id)
        return product
    
    @staticmethod
    def getProductByName(name):
        try:
            product = read_table_by_condition("products", "*", "name", name)
            if product:
                product_data = product[0]
                product_dict = {
                    "id": product_data[0],
                    "name": product_data[1],
                    "stock": product_data[2],
                    "mensual_sales": product_data[3],
                    "installation": product_data[4],
                    "price": product_data[5]
                }
                return product_dict
            else:
                return None
        except:
            return None
    
    @staticmethod
    def createProduct(name, stock, mensual_sales, installation, price):
        product = (name, stock, mensual_sales, installation, price)
        product_id = insert_product(product)
        return product_id
    
    @staticmethod
    def updateProduct(id, data):
        update_table("products", id, data)

    @staticmethod
    def deleteProduct(id):
        delete_table("products", id)