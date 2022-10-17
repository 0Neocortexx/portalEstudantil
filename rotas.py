from crypt import methods
from config import *
from modelo import *

@app.route('/')
def home():
    return render_template('index.html')

    # Tentativa de um cadastro simples

# teste da rota cadastro: curl -d '{"email": "inseridoatravesdocurl", "nome": "test_user", "senha": "test_pass", "objetivo": "test_objective"}' -X POST -H "Content-Type:application/json" http://localhost:5000/cadastro


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET': # Se a requisição for GET
        return render_template('cadastro.html') # Retorna o Template do cadastro
    else:  # Se não, ele executa o procedimento do cadastro
        # Recebe os dados do front-end atraves do Json
        resposta = jsonify({"resultado": "ok", "detalhes": "ola"})
        dados = request.get_json() #o (force=True) dispensa o Content-Type na requisição no js
        print(dados)
        try: # Tenta executar a operação de inserir o usuário no banco
            new = Usuario(**dados) # Cria uma nova pessoa a partir dos dados
            db.session.add(new) # Adiciona a pessoa no banco
            db.session.commit() # Dá o commit no banco
        # Caso a operação falhe
        except Exception as e:  # Transforma o erro na letra 'e'
            # introduz o erro em uma variável que poderá ser exibida no front-end
            resposta = jsonify({'resultado':'erro', 'detalhes':str(e)})
        # Fora do try
        resposta.headers.add("Access-Control-Allow-Origin","*")
        return resposta

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        resposta = jsonify({"resultado": "ok", "detalhes": "ola"})
        dados = request.get_json(force=True)
        email = dados['email']
        senha = dados['senha']
        usuario_encontrado = Usuario.query.filter_by(email=email, senha=senha).first()
        if usuario_encontrado is not None:
            # criar a json web token (JWT)
            access_token = create_access_token(identity=login)

            # retornar
            resposta =  jsonify({"resultado":"ok", "detalhes":access_token}) 
        else:
            resposta = jsonify({"resultado": "erro", "detalhes": "login e/ou senha inválido(s)"})        
            # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta  # responder!


app.run(debug=True, host="0.0.0.0")