import pip
# Caso falte algum pip, executar esse arquivo
pips = ['flask_sqlalchemy','flask_cors','flask','flask_session','flask_jwt_extended','bcrypt']
for i in pips:
    pip.main(['install',i]) 