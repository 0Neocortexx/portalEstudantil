# Flask imports
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from bcrypt import bcrypt

# configurações
app = Flask(__name__)
# caminho do banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'portalEstudantil.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Usuario(db.Model):
    email = db.Column(db.String(254), primary_key=True, nullable=False)
    nome = db.Column(db.String(254), nullable=False)
    senha = db.Column(db.String(254), nullable=False)
    objetivo = db.Column(db.String(254), nullable=False)

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}, Objetivo: {self.objetivo}'

    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "objetivo": self.objetivo
        }


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

            "usuario_email": self.usuario_email
        }