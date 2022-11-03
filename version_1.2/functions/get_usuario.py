from config import *
from classes.Usuario import *

def get_usuario(email: str):
    return Usuario.query.get(email)
