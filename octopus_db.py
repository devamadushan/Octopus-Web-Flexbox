from flask import Flask 
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from conn import utilisateur,session, password, base_de_donne, port, Base
from Historique import HistoriqueCellule
from Experiences import Experience
from Cellules import Cellule
from read_db import get_cell_by_name, get_historique_by_id , get_experience_of_cellule, get_all_experience , get_experience_avenir



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{utilisateur}:{password}@localhost:{port}/{base_de_donne}'


# @app.route('/toto', methods=['POST'])
# def traitementform():

#     nom = request.form['name']
#     date_debut = request.form['date_debut']
#     date_fin  = request.form['date_fin']
#     lieu = request.form['lieu']
#     print(nom)

#     return redirect('http://10.118.10.23:5000')

@app.route('/detail')
def detail():
    try:
        # data = requests.get('http://10.119.20.100:8080/')
        # info = data.json()
        # value = request.form.get('name')
        # exp = list(value)
        # ecolab = exp[0]
        # cell = exp[1]

        # lieu = "E"+ecolab+"C"+ cell
        lieu = "E6C3"
        cellule = get_cell_by_name(lieu)
        experienceEncours = get_experience_of_cellule(cellule.id)
        historique = get_historique_by_id(cellule.id)
        all_experience = get_all_experience()
        experience_avenir = get_experience_avenir()
        return render_template('detail.html',experience_avenir = experience_avenir , all_experience=all_experience,nom_cellule=lieu, 
                           cellule = cellule, experience=experienceEncours, historique= historique )
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_message=str(e))




    



if __name__ == "__main__":
    app.run(host="",port=5000, debug=True)