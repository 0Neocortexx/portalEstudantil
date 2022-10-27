from crypt import methods
from config import *
from model import *

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

@app.route('/login', methods=['GET', 'POST'])
def login(): # Criar a função da rota
    # Se a requisição for GET 
    if request.method == 'GET':
        # Retorna o template do login
        return render_template('login.html')
    # Se não for GET 
    else:
        # Preparar uma resposta otimista
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        dados = request.get_json(force=True) # Pegar os dados do front e colocar na variavel dados
        email = dados['email'] # pega o email inserido no front em json
        senha = dados['senha'] # pega a senha inserida no front em json
        senha = senha.encode('utf-8') # Deixa a senha no padrão utf-8.
        login = verificar_senha(senha,email)  
        # Faz uma consulta no banco para saber se tem outro email igual
        usuario_encontrado = Usuario.query.filter_by(email=email).first()
        # Se não encontrar emails parecidos
        if usuario_encontrado is not None and login == True:
            # criar a json web token (JWT) usando o email 
            access_token = create_access_token(identity=email)
            # Retorna a (JWT) em json
            resposta =  jsonify({"resultado":"ok", "detalhes":access_token, 'email':email})
            # Adiciona o cabeçalho de liberação de origem
            resposta.headers.add('Access-Control-Allow-Origin', '*')
            print('Login Realizado!')
        else:
            # Vai responder erro
            resposta = jsonify({"resultado": "erro", "detalhes": "login e/ou senha inválido(s)"}) 

            # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        # Retorna resposta
        return resposta  # responder!


@app.route('/inserir_conteudo', methods = ['POST', 'GET'])
def inserir_conteudo():
    if request.method == 'GET':
        return render_template('inserir_conteudo.html')
    else:
        resposta = jsonify({"resultado":"ok", "detalhes": "ok"})

app.run(debug=True, host="0.0.0.0")