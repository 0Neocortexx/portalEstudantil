from config import *
from classes.Usuario import *

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataAcesso = db.Column(db.Date)

    usuario_email = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    usuario = db.relationship("Usuario")


    def __str__(self):
        return f'ID do registro: {self.id}, Usuário: {self.usuario.email}, Data do ultimo acesso: {self.dataAcesso}'
    
    def json(self):
        return {
            "registro_id": self.id,
            "data_acesso": self.dataAcesso,
            "usuario_email": self.usuario.email
        }