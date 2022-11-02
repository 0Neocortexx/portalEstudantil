from config import *

@app.route("/")
def inicio():
    return render_template('index.html')