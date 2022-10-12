from crypt import methods
from config import *
from modelo import *

@app.route('/')
def home():
    return render_template('index.html')

    # Tentativa de um cadastro simples

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
    return render_template('login.html')

app.run(debug=True, host="0.0.0.0")