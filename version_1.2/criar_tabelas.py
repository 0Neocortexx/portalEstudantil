from config import *
from classes.Avaliacao import *
from classes.Comentarios import *
from classes.Conteudo import *
from classes.Registro import *
from classes.Usuario import *


if os.path.exists(arquivobd):
    os.remove(arquivobd)

# criar tabelas
db.create_all()
print("Tabelas Criadas com sucesso!")
