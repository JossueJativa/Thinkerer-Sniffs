from data.controllerData import read_table, read_table_by_id, insert_employee, update_table, delete_table, read_table_by_condition

class Employee:
    def __init__(self, id, name, email, phone, password):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def getEmployee(self):
        employee = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password
        }
        return employee
    
    @staticmethod
    def getEmployees():
        employees = read_table("employees")
        return employees
    
    @staticmethod
    def getEmployeeById(id):
        try:
            employee = read_table_by_id("employees", id)
            return employee
        except:
            return None
    
    @staticmethod
    def getEmployeeByEmail(email):
        try:
            employee = read_table_by_condition("employees", "*", "email", email)
            if employee:
                employee_data = employee[0]
                employee_dict = {
                    "id": employee_data[0],
                    "name": employee_data[1],
                    "email": employee_data[2],
                    "phone": employee_data[3],
                    "password": employee_data[4]
                }
                return employee_dict
            else:
                return None
        except:
            return None
    
    @staticmethod
    def getEmployeeByName(name):
        try:
            employee = read_table_by_condition("employees", "*", "name", name)
            if employee:
                employee_data = employee[0]
                employee_dict = {
                    "id": employee_data[0],
                    "name": employee_data[1],
                    "email": employee_data[2],
                    "phone": employee_data[3],
                    "password": employee_data[4]
                }
                return employee_dict
            else:
                return None
        except:
            return None
    
    @staticmethod
    def getEmployeeByPhone(phone):
        try:
            employee = read_table_by_condition("employees", "*", "phone", phone)
            if employee:
                employee_data = employee[0]
                employee_dict = {
                    "id": employee_data[0],
                    "name": employee_data[1],
                    "email": employee_data[2],
                    "phone": employee_data[3],
                    "password": employee_data[4]
                }
                return employee_dict
            else:
                return None
        except:
            return None
    
    @staticmethod
    def createEmployee(name, email, phone, password):
        employee = (name, email, phone, password)
        employee_id = insert_employee(employee)
        return employee_id
    
    @staticmethod
    def updateEmployee(id, data):
        update_table("employees", id, data)

    @staticmethod
    def deleteEmployee(id):
        delete_table("employees", id)