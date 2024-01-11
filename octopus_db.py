from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from conn import utilisateur,session, password, base_de_donne, port, Base

from Experiences import Experience
from Cellules import Cellule



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{utilisateur}:{password}@localhost:{port}/{base_de_donne}'


@app.route('/toto', methods=['POST'])
def traitementform():

    nom = request.form['name']
    date_debut = request.form['date_debut']
    date_fin  = request.form['date_fin']
    lieu = request.form['lieu']
    print(nom)

    return "c'est bon"

if __name__ == "__main__":
    app.run(host="10.118.10.91",port=5000, debug=True)