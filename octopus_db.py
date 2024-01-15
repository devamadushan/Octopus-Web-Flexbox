from flask import Flask 
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from conn import utilisateur,session, password, base_de_donne, port, Base
from Historique import HistoriqueCellule
from Experiences import Experience
from Cellules import Cellule
from read_db import get_cell_by_name, get_historique_by_id , get_experience_of_cellule, get_all_experience , get_experience_avenir, nouvelle_historique, nouvelle_experience_de_cellule



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

#,methods=['POST']  
@app.route('/detail',methods=['POST'])
def detail():
    try:
        data = requests.get('http://10.119.20.100:8080/')
        info = data.json()
    
        value =request.form.get('name')
        
        exp = list(value)
        ecolab = exp[0]
        cell = exp[1]
       
        lieu = f"E{ecolab}C{cell}"
        #lieu = "E5C3"
        cellule = get_cell_by_name(lieu)
        experienceEncours = cellule.experience_id
        print(experienceEncours)
        historique = get_historique_by_id(cellule.id)
        experience_avenir = get_experience_avenir()
        return render_template('detail.html',experience_avenir = experience_avenir ,nom_cellule=lieu, 
                           cellule = cellule, experience=experienceEncours, historique= historique )
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_message=str(e))


@app.route('/nouvelle-experience-de-cellule', methods=['POST'])
def nouvelle_experience_dans_cellule():
    experience_id= request.form.get('experience')
    cellule_id = request.form.get('cellule')
    #mise_a_jour_cellule = nouvelle_experience_dans_cellule(cellule_id,experience_id)
    #ajout_historique = nouvelle_historique(cellule_id,experience_id)
    experience_encours = request.form.get('experienceEnCours')
    print(experience_encours)
    return "c'est bon"
    



if __name__ == "__main__":
    app.run(host="10.118.10.103",port=5000, debug=True)