from flask import Flask 
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from conn import utilisateur,session, password, base_de_donne, port, Base
from Historique import HistoriqueCellule
from Experiences import Experience
from Cellules import Cellule
from read_db import get_cell_by_name,get_cellule_name_from_id,get_experience_by_id, get_historique_by_id , get_experience_of_cellule, get_all_experience , get_experience_avenir_encours, nouvelle_historique, nouvelle_experience_de_cellule, update_historique, verification_experience



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{utilisateur}:{password}@localhost:{port}/{base_de_donne}'


 #methods=['POST']
@app.route('/detail',methods=['POST'])
def detail():
    global session
    try:
        data = requests.get('http://10.119.20.100:8080/')
        #data = requests.get('http://127.0.0.1:9000/')
        info = data.json() 
        lieu =request.form.get('name')
        ecolab = lieu[1]
        cell =  lieu[3]
        jsonEcolab = f"ecolab_{ecolab}"
        jsonCellule = f"Cellule_{cell}"
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
    verification = verification_experience(experience_id)
    
    try: 
        cellule_id = int(request.form.get('cellule'))
        cellule_nom = get_cellule_name_from_id(cellule_id)
        experience_encours = int(request.form.get('experienceEnCours'))
        update_historiqu = update_historique(cellule_id)
        mise_a_jour_cellule = nouvelle_experience_de_cellule(cellule_id,experience_id)
        ajout_historique = nouvelle_historique(cellule_id,experience_id)

        session.commit()
        return render_template('success.html',cellule = cellule_nom)
    
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_message=str(e))

@app.route('/experiences')
def experiences():
    experiences = get_all_experience()
    return render_template('experiences.html',experiences=experiences)

@app.route('/add-experiences')
def addExperiences():
    return render_template('addExperience.html',experiences=experiences)

@app.route('/traitement-add-experiences',methods=['POST'])
def traitementAddExperiences():
    global session
    nom = request.form.get('nom')
    date_debut = request.form.get('date_debut')
    date_fin = request.form.get('date_fin')
    etat = request.form.get('etat_experience')
    newExperience = Experience(nom=nom,date_debut=date_debut,date_fin=date_fin,etat_experience=etat)
    session.add(newExperience)
    session.commit()
    return redirect(url_for('experiences'))

@app.route('/edit-experiences',methods=['POST'])
def editExperiences():
    id_experience = int(request.form.get('id_experience'))
    experience = get_experience_by_id(id_experience)
    #print(experience)
    return render_template('editExperience.html',experience=experience)

@app.route('/traitement-edit-experiences',methods=['POST'])
def traitementEditExperiences():
    global session
    id_experience = int(request.form.get('id_experience'))
    nom = request.form.get('nom')
    date_debut = request.form.get('date_debut')
    date_fin = request.form.get('date_fin')
    etat = request.form.get('etat_experience')

    experience = get_experience_by_id(id_experience)
    experience.nom=nom
    if date_debut:
        experience.date_debut = date_debut
    if date_fin:
        experience.date_fin = date_fin
    experience.etat_experience = etat   
    session.commit()
    return redirect(url_for('experiences'))

if __name__ == "__main__":
    app.run(host="10.118.10.109",port=5000, debug=True)