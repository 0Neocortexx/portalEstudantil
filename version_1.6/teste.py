filtro = ('alert.','script','<','>','javascript',';','--',",","=","+",'/',"'",'"',"src=","admin'--"
            ,"or 1=1", "delete from usuario", "document.write","sessionStorage.","Window.","document.",'href=',"]>", "&#34","&#39")

emails = ['yahoo', 'gmail', 'outlook', 'hotmail']
email = dados['email']
nome = dados['nome']
senha = dados['senha']
objetivo = dados['objetivo']

a = ''


a = db.session.query(Usuario.email).filter_by(email = user.email).first()

for f in filtro:
    if f in email or f in nome or f in senha or f in objetivo:
        resposta = jsonify({'resultado':'injecao', 'detalhes': 'Não insira nenhum tipo de Injeção de código! Temos proteção :D'})
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta
    elif '' in email or '' in nome or '' in senha or None in objetivo:
        resposta = jsonify({'resultado':'vazio', 'detalhes': 'Não deixe campos vazios!'})
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta
    elif '@' not in email:
        resposta = jsonify({'resultado':'invalido', 'detalhes': 'Email inválido!'})
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta
    elif a is not None:
        resposta = jsonify({'resultado':'usuario_ja_cadastrado', 'detalhes':'Email Já cadastrado!'})
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta
    else:
        user.senha = criptografar_sen(user.senha)
        db.session.add(user) # Adiciona a pessoa no banco
        db.session.commit() # Dá o commit no banco
        print(user)
        print('Usuário cadastrado!')
        resposta = jsonify({'resultado': 'sucesso', 'detalhes': 'Usuário cadastrado!'})
