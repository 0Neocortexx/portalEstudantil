from config import *
from classes.Usuario import *

class Conteudo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254), nullable=False)
    materia = db.Column(db.String(254), nullable=False)
    conteudo = db.Column(db.String(254), nullable=False)
    fontes = db.Column(db.String(254), nullable=False)

    usuario_email = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    usuario = db.relationship("Usuario")

    def __str__(self):
        return f'ID: {self.id},Titulo: {self.titulo}, Matéria: {self.materia}, \
            Conteudo: {self.conteudo}, Fontes: {self.fontes} \
            Email do usuário: {self.usuario_email}'

    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "materia": self.materia,
            "conteudo": self.conteudo,
            "fontes": self.fontes,

            "usuario_email": self.usuario_id
        }