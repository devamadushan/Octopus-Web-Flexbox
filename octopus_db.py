from flask import Flask 
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from conn import utilisateur,session, password, base_de_donne, port, Base
from Historique import HistoriqueCellule
from Experiences import Experience
from Cellules import Cellule
from read_db import get_cell_by_name, get_historique_by_id , get_experience_of_cellule, get_all_experience , get_experience_avenir_encours, nouvelle_historique, nouvelle_experience_de_cellule, update_historique



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{utilisateur}:{password}@localhost:{port}/{base_de_donne}'

 #methods=['POST']
@app.route('/detail')
def detail():
    try:
        global session
        #data = requests.get('http://10.119.20.100:8080/')
        data = requests.get('http://127.0.0.1:9000/')
        info = data.json() 
        #value =request.form.get('name')
        
        #exp = list(value)
        ecolab = 2 #exp[0]
        cell =  1 #exp[1]
       
        lieu = f"E{ecolab}C{cell}"
        jsonEcolab = f"ecolab_{ecolab}"
        jsonCellule = f"Cellule_{cell}"
        lieu = "E5C3"
        cellule = get_cell_by_name(lieu)
        experienceEncours = cellule.experience_id
        
        historique = get_historique_by_id(cellule.id)
        experience_avenir_encours = get_experience_avenir_encours()
        session.commit()
        return render_template('detail.html',experience_avenir_encours = experience_avenir_encours ,nom_cellule=lieu, 
                           cellule = cellule, experience=experienceEncours,info = info, historique= historique, jsonEcolab = jsonEcolab, jsonCellule=jsonCellule )
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_message=str(e))


@app.route('/nouvelle-experience-de-cellule', methods=['POST'])
def nouvelle_experience_dans_cellule():
    global session
    experience_id= int(request.form.get('experience'))
    cellule_id = int(request.form.get('cellule'))
    experience_encours = request.form.get('experienceEnCours')
    update_historiqu = update_historique(cellule_id)
    mise_a_jour_cellule = nouvelle_experience_de_cellule(cellule_id,experience_id)
    ajout_historique = nouvelle_historique(cellule_id,experience_id)
   
    
    session.commit()
   
    return redirect(url_for('detail'))
    



if __name__ == "__main__":
    app.run(host="",port=5000, debug=True)