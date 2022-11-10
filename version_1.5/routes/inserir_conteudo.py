from config import *
from model.conteudo import *

# Teste da rota curl -d '{"email": "inseridoatravesdocurl", "materia":"portugues", "titulo": "tartarugas matam", "conteudo": "tartarugas realmente matam? descubra no proximo bloco", "fontes": "biririnha"}' -X POST -H "Content-Type:application/json" http://localhost:5000/inserir_conteudo

@app.route('/inserir_conteudo', methods = ['POST', 'GET'])
def inserir_conteudo():
    if request.method == 'GET':
        return render_template('inserir_conteudo.html')
    else:
        resposta = jsonify({"resultado":"ok", "detalhes": "ok"})
        dados = request.get_json()
        conteudo = Conteudo(usuario_email = dados["usuario"],materia = dados["materia"] ,titulo = dados["titulo"], conteudo = dados["conteudo"], fontes = dados["fontes"])
        try: # Tenta executar a operação de inserir o usuário no banco
             # Cria uma nova pessoa a partir dos dados
            db.session.add(conteudo) # Adiciona a pessoa no banco
            db.session.commit() # Dá o commit no banco
            print('Conteudo cadastrado!')
            resposta = jsonify({'Resultado': 'sucesso', 'Detalhes': 'ok'}) # Dá resposta caso o usuário for inserido
        # Caso a operação falhe
        except Exception as e:  # Transforma o erro na letra 'e'
            # introduz o erro em uma variável que poderá ser exibida no front-end
            resposta = jsonify({'resultado':'erro', 'detalhes':str(e)})
        # Fora do try
        resposta.headers.add("Access-Control-Allow-Origin","*")
        return resposta