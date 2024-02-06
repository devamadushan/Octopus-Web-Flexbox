'''
Flask : pip install SQLAlchemy

'''

############################################################################################################

# Importation des modules nécessaires
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from Connexion import utilisateur,session, password, base_de_donne, port, Base
from History import Historiy_cells
from Experiment import Experiment
from Cells import Cells
from User import User
from werkzeug.security import check_password_hash

############################################################################################################

# Auteur: Deva

class OctopusDB():
    def __init__(self):
        self.Experiments = session.query(Experiment).all()
        self.cellules = session.query(Cells).all()
        self.historique = session.query(Historiy_cells).all()
        self.users = session.query(User).all()


    # Method to retrieve all experiments from database
    def get_all_experience(self):
        global session
        Experiments = session.query(Experiment).all()
        session.commit()
        return Experiments


    # Method to retrieve the name of a cell from its ID
    def get_cellule_name_from_id(self, id_cellule):
        for cellule in self.cellules:
            if cellule.id == id_cellule:
                return cellule.nom

    # Method to retrieve a cell from its name
    def get_cellule_by_name(self,name):
        for cellule in self.cellules:
            if cellule.nom == name:
                return cellule
        return None

    # Method to retrieve a cell from its ID
    def get_cellule_by_id(self,id_cellule):
        for cellule in self.cellules:
            if cellule.id == id_cellule:
                return cellule

    # Method for retrieving current and future Experiments
    def get_futur_and_current_experience(self):
        result = []
        for Experiment in self.Experiments:
            if Experiment.status_experiment == "à venir" or Experiment.status_experiment == "En cours":
                result.append(Experiment)
        return result

    # Method to retrieve an Experiment from its ID
    def get_experience_by_id(self,id_Experiment):
        Experiments = session.query(Experiment).all()
        try :
            for experiment in Experiments:
                if experiment.id == id_Experiment:
                    return experiment
        except Exception as e:
            print(f"Erreur lors de la récupération de l'expérience par ID : {str(e)}")
            return None


       # Method to retrieve the history of a cell from its ID
    def get_historique_by_id(self,cellule_id):
        global session
        historiques = session.query(Historiy_cells).all()
        result = []
        for historique in historiques:
            if historique.cells_id == cellule_id:
                cellule = self.get_cellule_by_id(historique.cells_id)
                experience = self.get_experience_by_id(historique.cells_experiment_id)
                result.append({"historique": historique, "cellule": cellule, "experience": experience})
        session.commit()
        return result
        

    # Method to retrieve the Experiment of a cell from its ID
    def get_Experiment_of_cellule(self,cellule_id):
        for cellule in self.cellules:
            if cellule.id == cellule_id:
                return self.get_Experiment_by_id(cellule.Experiment_id)
        return None

 # Method to retrieve an Experiment from its ID
    def get_Experiment_by_id(self,id):
        for Experiment in self.Experiments:
            if Experiment.id == id :
                return Experiment
        return None

    # Method for updating a cell's Experiment
    def new_experience_of_cellule(self,id_cellule,id_Experiment):
        global session
        try :
            cellule = self.get_cellule_by_id(id_cellule)
            cellule.Experiment_id = id_Experiment
            session.commit()
            return "Mise à jour réussie"
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"

    # Method to update the history of a cell
    def new_historique(self,id_cellule,id_Experiment):
        global session
        try:
            new_historique = Historiy_cells(cells_id=id_cellule,cells_experiment_id=id_Experiment,status="En cours",action="Ajout d'une nouvelle expérience à la cellule")
            session.add(new_historique)
            session.commit()
            return "c'est bon"
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"

    # Method to update the history of a cell
    def update_historique(self,cellule_id):
        global session
        historiques = session.query(Historiy_cells).all()
        try :
            for historique in historiques:
                if historique.cells_id == cellule_id and historique.status == "En cours":
                    historique.status = "Terminé"
                    session.commit()
            return "mise a jour reussi !"
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"
        
        

   # Auteur Luca
    
    # Check if user exists
    def user_exists(cls,login,password):
        global session
        users = session.query(User).all()
        try:
            for user in users:
                if login == user.username:
                    if user.check_password(password):
                        return True
                    else:
                        return 'mot de passe incorrecte'
                    
            return 'Utilisateur inexistant'

        except Exception as e:
            return f"une erreur s'est produite : {str(e)}"
        

    # Method to find out if user exists and get their role
    def get_role_by_user(cls,username):
        global session
        users = session.query(User).all()
        try:
            for user in users:
                if username == user.username:
                        return user.role
            
            return 'utilisateur inexistant'
        except Exception as e:
            return f"une erreur s'est produite : {str(e)}"
        

    # Check if username exists
    def username_exist(cls,name):
        global session
        users = session.query(User).all()
        try :
            for user in users:
                if name == user.username:
                    return False
            return True
    
        except Exception as e:
            return f"une erreur s'est produite : {str(e)}"
        
    # Add user
    def add_user(cls,name,pwd):
        global session
        try :
            verification = octopus.username_exist(name)

            if verification == True:

                newUser = User(username = name)
                newUser.set_password(pwd)

                session.add(newUser)
                session.commit()

            else:
                return "Nom d'utilisateur indisponible" 
                

        except Exception as e:
            return f"une erreur s'est produite : {str(e)}"
        
     # Method to retrieve an experience from its ID
    def get_user_by_id(self,id):
        for user in self.users:
            if user.id == id:
                return user
        return None
        
    
    # Edit user role 
    def edit_role(cls,id,new_name, new_role):
        global session
        user = cls.get_user_by_id(id)
        if user:
            user.username = new_name
            user.role = new_role
            session.commit()
            return True
        return False
            


# name = 'admin'
# pwd = 'UtilisateurAdmin'



# Affichage du résultat

octopus = OctopusDB()




