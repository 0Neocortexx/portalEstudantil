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
            email = dados["email"]
            email = email.lower()
            user = Usuario(email =  email,nome = dados['nome'],senha = dados['senha'], objetivo = dados['objetivo'])
            a = db.session.query(Usuario.email).filter_by(email = user.email).first()    

            if verificar_campo(dados["email"], filtro) or verificar_campo(dados["nome"], filtro)\
                or verificar_campo(dados["senha"], filtro) or verificar_campo(dados["objetivo"], filtro):
                resposta = jsonify({'resultado':'injecao', 'detalhes': 'Não insira nenhum tipo de Injeção de código! Temos proteção :D'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            elif "@" not in user.email: 
                resposta = jsonify({'resultado':'invalido', 'detalhes': 'Email inválido!'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta
                
            elif '' in user.email or '' in user.senha: 
                resposta = jsonify({'resultado':'invalido', 'detalhes': 'Não deixe campos vazios!'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            elif len(user.name) < 4 or len(user.objetivo) < 4:
                resposta = jsonify({'resultado':'pequeno', 'detalhes': 'É necessário nome ou objetivo maior que 4 caracteres!'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta
        
            elif a is not None:
                resposta = jsonify({'resultado':'usuario_ja_cadastrado', 'detalhes':'Email Já cadastrado!'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta
            
            else:
                user.senha = criptografar_sen(user.senha)
                print(user)
                db.session.add(user) # Adiciona a pessoa no banco
                db.session.commit() # Dá o commit no banco
                resposta = jsonify({'resultado': 'sucesso', 'detalhes': 'Usuário cadastrado!'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

        except Exception as e:
            resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})
            resposta.headers.add('Access-Control-Allow-Origin', '*')
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta


def verificar_campo(atributo: str, filtro: tuple) -> bool:
    for f in filtro:
        if  f in atributo:
            return True
    return False