from config import *
from classes.Usuario import *
from functions.verificar_senha import *
from functions.get_usuario import *

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
        usuario = get_usuario(email)
        nome = usuario.nome
        senha = senha.encode('utf-8') # Deixa a senha no padrão utf-8.
        login = verificar_senha(senha,email)  
        # Faz uma consulta no banco para saber se tem outro email igual
        usuario_encontrado = Usuario.query.filter_by(email=email).first()
        # Se não encontrar emails parecidos
        
        if usuario_encontrado is not None and login == True:
            # criar a json web token (JWT) usando o email 
            access_token = create_access_token(identity=email)
            # Retorna a (JWT) em json
            resposta =  jsonify({"resultado":"ok", "detalhes":access_token , 'nome': nome,'email':email})
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