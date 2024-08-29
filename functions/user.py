from classes import User
from data.controllerData import writeFile, getDataFile

def createUser(nombre, email, celular, cedula):
    user = User(nombre, email, celular, cedula)
    user_info = user.getUser()

    header = ['Nombre', 'Email', 'Celular', 'Cédula']
    sheetname = 'Usuarios'
    is_written = writeFile(sheetname, header, user_info)

    return is_written