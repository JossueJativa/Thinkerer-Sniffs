from data.controllerData import read_table, insert_user, read_table_by_condition, read_table_by_id, update_table, delete_table

class User:
    def __init__(self, id, name, email, phone, identity_card):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.identity_card = identity_card

    def getUser(self):
        user = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "identity_card": self.identity_card
        }
        return user

    @staticmethod
    def getUsers():
        try:
            users = read_table("users")
            return users
        except:
            return []
    
    @staticmethod
    def getUserById(id):
        user = read_table_by_id("users", id)
        return user
    
    @staticmethod
    def getUserByEmail(email):
        try:
            user = read_table_by_condition("users", "*", "email", email)
            if user:
                user_data = user[0]
                user_dict = {
                    "id": user_data[0],
                    "name": user_data[1],
                    "email": user_data[2],
                    "phone": user_data[3],
                    "identity_card": user_data[4]
                }
                return user_dict
            else:
                return None
        except:
            return None
    
    @staticmethod
    def getUserByName(name):
        try:
            user = read_table_by_condition("users", "*", "name", name)
            if user:
                user_data = user[0]
                user_dict = {
                    "id": user_data[0],
                    "Nombre": user_data[1],
                    "email": user_data[2],
                    "Celular": user_data[3],
                    "Cédula": user_data[4]
                }
                return user_dict
            else:
                return None
        except:
            return None
    
    @staticmethod
    def createUser(name, email, phone, identity_card):
        user = (name, email, phone, identity_card)
        user_id = insert_user(user)
        return user_id
    
    @staticmethod
    def updateUser(id, data):
        update_table("users", id, data)

    @staticmethod
    def deleteUser(id):
        delete_table("users", id)