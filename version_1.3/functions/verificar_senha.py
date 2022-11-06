from config import *
from classes.Usuario import *

def verificar_senha(senha_dig:str,email_dig:str): 
    # Percorre o banco para encontrar a senha correspondente ao email
    for q in db.session.query(Usuario.senha).filter(Usuario.email==email_dig).all():
        try:
            resultado = bcrypt.checkpw(senha_dig,q[0])
        except:
            return False
        if q == None:
            return False
        return resultado