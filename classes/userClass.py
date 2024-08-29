from data.controllerData import getDataFile

class User:
    def __init__(self, name, email, phone, id):
        self.name = name
        self.email = email
        self.phone = phone
        self.id = id

    def getUser(self):
        return self.name, self.email, self.phone, self.id
    
    @staticmethod
    def getAllUsers():
        try:
            users = getDataFile("Usuarios")
            if users is None:
                raise ValueError("No data returned from getDataFile.")

            user_data = []
            for index, user in users.iterrows():
                user_data.append({
                    'Nombre': user['Nombre'],
                    'Email': user['Email'],
                    'Celular': user['Celular'],
                    'Cédula': user['Cédula']
                })
            return user_data
        except Exception as e:
            print(f"Error: {e}")
            return []
        
    @staticmethod
    def getUserByID(id):
        users = User.getAllUsers()
        user = next((u for u in users if u['Cédula'] == id), None)
        return user
    
    @staticmethod
    def getUserByName(name):
        users = User.getAllUsers()
        user = next((u for u in users if u['Nombre'] == name), None)
        return user
