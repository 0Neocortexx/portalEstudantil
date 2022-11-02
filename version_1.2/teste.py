"""from config import *
from classes.Usuario import *

def get_usuario(email: str):
    for q in db.session.query(Usuario.senha).filter(Usuario.email==email).all():
        return q

if __name__=="__main__":
    senha = get_usuario('inseridoatravesdocurl')
    print(senha)"""