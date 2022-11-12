from config import *
from model.usuario import *
from model.conteudo import *
from model.comentarios import *
from model.avaliacao import *
from model.registro import *

if os.path.exists(arquivobd):
    os.remove(arquivobd)

db.create_all()
print('Tabelas criadas com sucesso!')