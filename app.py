from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/mypage/<id>')
def mypage(id):
    if id == "me":
        return render_template("strona.html")
    elif id == "contact":
        return render_template("kontakt.html")