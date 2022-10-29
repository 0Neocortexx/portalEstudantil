from config import *

class Comentarios(db.Model):
    conteudo_id = db.Column(db.Integer, db.ForeignKey(Conteudo.id))
    conteudo = db.relationship("Conteudo")

    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String, nullable=False)

    usuario_id = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    usuario = db.relationship("Usuario")
    
    def __str__(self):
        return f'ID do comentário: {self.id}, Comentário: {self.comentario}, ID do conteudo: {self.conteudo.id}, \
            Email do usuário: {self.usuario.email}, Nome do usuário: {self.usuario.nome}'

    def json(self):
        return {
            "conteudo_id": self.conteudo.id,

            "comentario_id": self.id,
            "comentario": self.comentario,

            "usuario_email": self.usuario.email,
            "usuario_nome": self.usuario.nome
        }