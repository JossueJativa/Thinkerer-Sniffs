from classes import Employee

def get_employees():
    employees = Employee.getEmployees()
    return employees

def get_employee_by_id(id):
    employee = Employee.getEmployeeById(id)
    return employee

def get_employee_by_email(email):
    employee = Employee.getEmployeeByEmail(email)
    return employee

def get_employee_by_name(name):
    employee = Employee.getEmployeeByName(name)
    return employee

def get_employee_by_phone(phone):
    employee = Employee.getEmployeeByPhone(phone)
    return employee

def create_employee(name, email, phone, password):
    if not name or not email or not phone or not password:
        return "Missing data"
    
    if get_employee_by_email(email):
        return "Email already exists"
    
    if get_employee_by_phone(phone):
        return "Phone already exists"
    
    employee_id = Employee.createEmployee(name, email, phone, password)
    return employee_id

def update_employee(id, data):
    if not data:
        return "Missing data"
    
    if "email" in data:
        if get_employee_by_email(data["email"]):
            return "Email already exists"
        
    if "phone" in data:
        if get_employee_by_phone(data["phone"]):
            return "Phone already exists"
        
    Employee.updateEmployee(id, data)

def delete_employee(id):
    Employee.deleteEmployee(id)

def login_employee(email, password):
    employee = get_employee_by_email(email)
    if not employee:
        return "Email not found"
    
    if employee["password"] != password:
        return "Incorrect password"
    
    return employee["id"]