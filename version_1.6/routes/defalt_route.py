from config import *

@app.route("/")
def inicio():
    ip = request.host_url
    return f'<p>Projeto de apoio discente, comunicação e suporte em disciplinas do ensino médio. <br>Colaboradores:  <br> Aline Scholl Santos; <br> Jonathan Emmanuel De Oliveira</p> <br> <a href="{ip}main">Ir para o site!</a>'

@app.route('/main')
def main():
    return render_template('index.html')