from config import *

class Usuario(db.Model):
    nome = db.Column(db.String(254), nullable=False)
    email = db.Column(db.String(254), primary_key=True, nullable=False)
    senha = db.Column(db.String(254), nullable=False)
    objetivo = db.Column(db.String(254), nullable=False)

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}, Objetivo: {self.objetivo}'

    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "objetivo": self.objetivo
        }

class Conteudo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254), nullable=False)
    materia = db.Column(db.String(254), nullable=False)
    usuario = db.Column(db.String(254), db.ForeignKey(Usuario.email))

    def __str__(self):
        return f'ID: {self.id},Titulo: {self.titulo}, Matéria: {self.materia}, Usuário: {self.usuario}'

    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "materia": self.materia,
            "usuario": self.usuario
        }

class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Integer, db.ForeignKey(Conteudo.id))
    usuario = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    comentario = db.Column(db.String, nullable=False)

    def __str__(self):
        return f'ID do comentário: {self.id}, ID do conteudo: {self.conteudo}, Email do usuário: {self.usuario}, comentário: {self.comentario}'

    def json(self):
        return {
            "idComentario": self.id,
            "idConteudo": self.conteudo,
            "emailUsuario": self.usuario,
            "comentario": self.comentario
        }

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataAcesso = db.Column(db.Date)
    usuario = db.Column(db.String(254), db.ForeignKey(Usuario.email))

    def __str__(self):
        return f'ID do registro: {self.id}, Usuário: {self.usuario}, data do ultimo acesso: {self.dataAcesso}'
    
    def json(self):
        return {
            "idRegistro": self.id,
            "dataAcesso": self.dataAcesso,
            "usuario": self.usuario
        }

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Integer, db.ForeignKey(Conteudo.id))
    usuario = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    nota = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f'ID da avaliação: {self.id}, Conteudo avaliado: {self.conteudo}, usuário: {self.usuario}, nota: {self.nota}'

    def json(self):
        return {
            "idAvaliacao": self.id,
            "conteudo": self.conteudo,
            "usuario": self.usuario,
            "nota": self.nota
        }

if __name__=="__main__":
    db.create_all()