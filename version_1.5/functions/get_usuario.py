from config import *
from model.usuario import *

def get_usuario(email: str):
    return Usuario.query.get(email)
