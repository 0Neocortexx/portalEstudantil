from config import *

class Conteudo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254), nullable=False)
    materia = db.Column(db.String(254), nullable=False)

    usuario_id = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    usuario = db.relationship("Usuario")

    def __str__(self):
        return f'ID: {self.id},Titulo: {self.titulo}, Matéria: {self.materia}, \
            ID do usuário: {self.usuario_id}, Nome do usuario: {self.usuario.nome}, Email do usuário: {self.usuario.nome}'

    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "materia": self.materia,

            "usuario_id": self.usuario_id,
            "usuario_email": self.usuario.email,
            "usuario_nome" : self.usuario.nome
        }