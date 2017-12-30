from models.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username, password):

    user = UserModel.find_by_username(username) # second param is for default value if not found
    if user and safe_str_cmp(user.password, password): # user.password == password
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)