# Flask imports
from flask_sqlalchemy import *
from flask_cors import *
from flask import *
from flask_session import *
from flask_jwt_extended import *

# System imports
from datetime import *
import os
import bcrypt

# configurações
app = Flask(__name__)
# aplicar o cross domein
CORS(app)
# caminho do banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'portalEstudantil.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

# segurança - JWT
app.config['JWT_SECRET_KEY'] = 'theAndrewislying'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes= 30)
jwt = JWTManager(app)