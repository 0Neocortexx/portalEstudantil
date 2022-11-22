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


def criptografar_sen(senha: str):
        """Criptografa a senha usando o bcrypt."""
        senha = senha.encode('utf-8') # Deixa a senha no padrão utf-8.
        nova_senha = bcrypt.hashpw(senha,bcrypt.gensalt()) # Gera a senha criptografada
        senha = nova_senha
        return senha

filtro = ('alert.','<script>','<','>','javascript',';','--',",","=","+",'/',"'",'"',"src=","admin'--"
            ,"or 1=1", "delete from user", "document.write","sessionStorage.","Window.","document.",'href=',"]>")


def filtro(email: str):
    for f in filtro: # laço de repetição que verifica se não há um texto suspeito de possuir injeção XSS ou SQL.
        if f in email:
            resposta = email.replace(f,'')
    if resposta == '' and len(resposta)<=4 or '@' not in resposta:
        resposta = None
    return resposta

def get_usuario(email: str):
    return Usuario.query.get(email)

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

if __name__=="__main__":
    db.create.all()