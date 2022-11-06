from config import *
from classes.Conteudo import *

@app.route('/feed', method=['GET'])
def listar_conteudos():
    conteudos = db.session.query(Conteudo).all()
    conteudo_json =  [ x.json() for x in conteudos]
    for i in conteudo_json:
        print(i)
    resposta = jsonify(i)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
