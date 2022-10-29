from config import *
from classes import *

@app.route('/inserir_conteudo', methods = ['POST', 'GET'])
def inserir_conteudo():
    if request.method == 'GET':
        return render_template('inserir_conteudo.html')
    else:
        resposta = jsonify({"resultado":"ok", "detalhes": "ok"})
        dados = request.get_json(Force = True)
        conteudo = Conteudo(titulo = dados["titulo"], materia = dados["materia"], usuario =dados["usuario"])