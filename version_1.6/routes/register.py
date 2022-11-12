from config import *
from model.usuario import *
from functions.filtro import *
from functions.cripto_pass import *

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('cadastro.html')
    else:
        try:
            resposta = jsonify({'resultado':'ok', 'detalhes': 'ok'})
            dados = request.get_json(force=True)

            email = dados['email']
            nome = dados['nome']
            senha = dados['senha']
            objetivo = dados['objetivo']

            for f in filtro:
                if f in email or f in nome or f in senha or f in objetivo:
                    resposta = jsonify({'resultado':'injecao', 'detalhes': 'Não insira nenhum tipo de Injeção de código! Temos proteção :D'})
                    resposta.headers.add('Access-Control-Allow-Origin', '*')
                    return resposta
            
            if email == '' or nome == '' or senha == '' or objetivo == '':
                    resposta = jsonify({'resultado': 'email_vazio','detalhes': 'Não deixe campos vazios'})
                    resposta.headers.add('Access-Control-Allow-Origin', '*')
                    return resposta
                    
            if '@' not in email or len(email) <= 6:
                resposta = jsonify({'resultado':'email_invalido', 'detalhes':'Email Inválido!'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            if f in email or f in nome or f in senha or f in objetivo:
                resposta = jsonify({'resultado':'injecao', 'detalhes': 'Não insira nenhum tipo de Injeção de código! Temos proteção :D'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            user = Usuario(email = email, nome = nome, senha = senha, objetivo = objetivo)

            a = db.session.query(Usuario.email).filter_by(email = user.email).first()

            if a is not None:
                resposta = jsonify({'resultado':'usuario_ja_cadastrado', 'detalhes':'Email Já cadastrado!'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            user.senha = criptografar_sen(user.senha)

            db.session.add(user) # Adiciona a pessoa no banco
            db.session.commit() # Dá o commit no banco
            print(user)
            print('Usuário cadastrado!')
            resposta = jsonify({'resultado': 'sucesso', 'detalhes': 'Usuário cadastrado!'})

        except Exception as e:
            resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})
            resposta.headers.add('Access-Control-Allow-Origin', '*')

        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta
