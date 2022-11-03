from config import *
from classes.Usuario import *

def get_nome(email:str):
    for q in db.session.query(Usuario.nome).filter(Usuario.email == email).all():
        return q 