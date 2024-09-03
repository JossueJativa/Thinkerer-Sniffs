from classes import User

def get_users():
    users = User.getUsers()
    return users

def get_user_by_id(id):
    user = User.getUserById(id)
    return user

def get_user_by_email(email):
    user = User.getUserByEmail(email)
    return user

def get_user_by_name(name):
    user = User.getUserByName(name)
    return user

def create_user(name, email, phone, identity_card):
    user_id = User.createUser(name, email, phone, identity_card)
    return user_id

def update_user(id, data):
    User.updateUser(id, data)

def delete_user(id):
    User.deleteUser(id)