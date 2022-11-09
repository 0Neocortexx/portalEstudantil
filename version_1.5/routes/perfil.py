from config import *
from model.usuario import *

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'GET':
        return render_template('user.html')
