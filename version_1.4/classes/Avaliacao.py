from config import *
from classes.Conteudo import *
from classes.Usuario import *

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=False)

    conteudo = db.Column(db.Integer, db.ForeignKey(Conteudo.id))
    conteudo = db.relationship("Conteudo")

    usuario_email = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    usuario = db.relationship("Usuario")

    def __str__(self):
        return f'ID da avaliação: {self.id}, nota: {self.nota}, Email do usuário: {self.usuario.email}, \
           Nome do usuário: {self.usuario.nome} ,Conteudo avaliado: {self.conteudo.titulo}'

    def json(self):
        return {
            "avaliacao_id": self.id,
            "nota": self.nota,

            "conteudo": self.conteudo.titulo,

            "usuario_email": self.usuario.email,
            "usuario_nome": self.usuario.nome
        }
