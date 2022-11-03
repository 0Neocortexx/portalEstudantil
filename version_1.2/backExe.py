from config import *
from routes.cadastro import *
from routes.login import *
from routes.inserir_conteudo import *
from routes.defalt_route import *

app.run(debug=True, host='0.0.0.0')