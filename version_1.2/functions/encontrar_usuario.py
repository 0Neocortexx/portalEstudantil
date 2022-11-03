from config import *
from classes.Usuario import *

def get_senha(email: str):
    for q in db.session.query(Usuario.senha).filter(Usuario.email==email).all():
        return q
