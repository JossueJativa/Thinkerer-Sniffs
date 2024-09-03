from data.controllerData import read_table, insert_user, read_table_by_id, update_table, delete_table

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
        user = read_table("users", email)
        return user
    
    @staticmethod
    def getUserByName(name):
        user = read_table("users", name)
        return user
    
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