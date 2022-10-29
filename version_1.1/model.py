from config import *

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

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataAcesso = db.Column(db.Date)

    usuario_id = db.Column(db.String(254), db.ForeignKey(Usuario.email))
    usuario = db.relationship("Usuario")


    def __str__(self):
        return f'ID do registro: {self.id}, Usuário: {self.usuario.email}, Data do ultimo acesso: {self.dataAcesso}'
    
    def json(self):
        return {
            "registro_id": self.id,
            "data_acesso": self.dataAcesso,
            "usuario_email": self.usuario.email
        }

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=False)

    conteudo = db.Column(db.Integer, db.ForeignKey(Conteudo.id))
    conteudo = db.relationship("Conteudo")

    usuario = db.Column(db.String(254), db.ForeignKey(Usuario.email))
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

# Funções 
# Função que recebe duas informações, 1- Senha digitada no front e 2- Email digitado no front
# Obs: Os dois dados em str
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

def get_usuario(email: str):
    return Usuario.query.get(email)
    
def criptografar_sen(senha: str):
        """Criptografa a senha usando o bcrypt."""
        senha = senha.encode('utf-8') # Deixa a senha no padrão utf-8.
        nova_senha = bcrypt.hashpw(senha,bcrypt.gensalt()) # Gera a senha criptografada
        senha = nova_senha
        return senha
        
if __name__=="__main__":
    db.create_all()