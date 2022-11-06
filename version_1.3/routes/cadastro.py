from config import *
from classes.Usuario import *
from functions.criptografar_senha import *

# Tentativa de um cadastro simples
# teste da rota cadastro: curl -d '{"email": "inseridoatravesdocurl", "nome": "test_user", "senha": "test_pass", "objetivo": "test_objective"}' -X POST -H "Content-Type:application/json" http://localhost:5000/cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET': # Se a requisição for GET
        return render_template('cadastro.html') # Retorna o Template do cadastro
    else:  # Se não, ele executa o procedimento do cadastro
        # Recebe os dados do front-end atraves do Json
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        dados = request.get_json() #o (force=True) dispensa o Content-Type na requisição no js
        user = Usuario(email =  dados['email'],nome = dados['nome'],senha = dados['senha'], objetivo = dados['objetivo'])
        user.senha = criptografar_sen(user.senha)
        try: # Tenta executar a operação de inserir o usuário no banco
             # Cria uma nova pessoa a partir dos dados
            db.session.add(user) # Adiciona a pessoa no banco
            db.session.commit() # Dá o commit no banco
            print(user)
            print('Usuário cadastrado!')
            resposta = jsonify({'Resultado': 'sucesso', 'Detalhes': 'ok'}) # Dá resposta caso o usuário for inserido
        # Caso a operação falhe
        except Exception as e:  # Transforma o erro na letra 'e'
            # introduz o erro em uma variável que poderá ser exibida no front-end
            resposta = jsonify({'resultado':'erro', 'detalhes':str(e)})
        # Fora do try
        resposta.headers.add("Access-Control-Allow-Origin","*")
        return resposta