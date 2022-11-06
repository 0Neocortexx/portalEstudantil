from config import *
from classes.Usuario import *

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'GET':
        return render_template('user.html')
