from config import *
from classes.Conteudo import *

@app.route('/feed')
def listar():
    return render_template('feed.html')

@app.route('/feedlistar')
def listar_conteudos():
    conteudos = db.session.query(Conteudo).all()
    conteudo_json =  [ x.json() for x in conteudos]
    resposta = jsonify(conteudo_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...
