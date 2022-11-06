"""from config import *
from classes.Usuario import *

def get_usuario(email: str):
    for q in db.session.query(Usuario.senha).filter(Usuario.email==email).all():
        return q

if __name__=="__main__":
    senha = get_usuario('inseridoatravesdocurl')
    print(senha)"""

"""from functions.get_username import *

nome = get_nome('jonas@g.c')
print(nome)"""

"""from config import *

filtro = ('alert.','<script>','<','>','javascript',';','--',",","=","+",'/',"'",'"',"src=","admin'--"
            ,"or 1=1", "delete from user", "document.write","sessionStorage.","Window.","document.",'href=',"]>")


def filtragem(email: str):
    for f in filtro: # laço de repetição que verifica se não há um texto suspeito de possuir injeção XSS ou SQL.
        if f in email:
            resposta = email.replace(f,'')
    if resposta == '' and len(resposta)<=4 or '@' not in resposta:
        resposta = None
    return resposta

a = ''

a = 'cacho rro'
b = a.replace(filtro,2 '')
print(b)"""

"""from classes.Conteudo import *

conteudos = db.session.query(Conteudo).all()
conteudo_json =  [ x.json() for x in conteudos]
for i in conteudo_json:
    print(i)
resposta = jsonify(i)
resposta.headers.add("Access-Control-Allow-Origin", "*")
return resposta"""