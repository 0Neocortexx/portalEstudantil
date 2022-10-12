from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import *
import os

# configurações
app = Flask(__name__)
# aplicar o cross domein
CORS(app)
# caminho do banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'portal_estudantil.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)
