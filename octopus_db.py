from conn import session
from Experiences import Experience
from Cellules import Cellule
from Historique import HistoriqueCellule
from sqlalchemy.orm import joinedload
from pprint import pprint

# experiences = session.query(Experience).all()
# cellules = session.query(Cellule).all() 
# historiques = session.query(HistoriqueCellule).all()

class Octopus:
    def __init__(self):
        self.experiences = session.query(Experience).all()
        self.cellules = session.query(Cellule).all()
        self.historique = session.query(HistoriqueCellule).all()

    def update_database(self):
        global session
        session.commit()
        return "c'est bon"

    def get_all_experience(self):
        global session
        experiences = session.query(Experience).all()
        session.commit()
        return experiences
    
    def get_cellule_name_from_id(self, id_cellule):
        for cellule in self.cellules:
            if cellule.id == id_cellule:
                return cellule.nom
    
    def get_cellule_by_name(self,name):
        for cellule in self.cellules:
            if cellule.nom == name:
                return cellule
        return None
    def get_cellule_by_id(self,id_cellule):
        for cellule in self.cellules:
            if cellule.id == id_cellule:
                return cellule
    def get_futur_and_current_experience(self):
        result = []
        for experience in self.experiences:
            if experience.etat_experience == "à venir" or experience.etat_experience == "En cours":
                result.append(experience)
        return result

    def get_experience_by_id(self,id_experience):
        try :
            for experience in self.experiences:
                if experience.id == id_experience:
                    return experience
        except Exception as e:  
            print(f"Erreur lors de la récupération de l'expérience par ID : {str(e)}")
            return None
        
    def get_historique_by_id(self,cellule_id):
        global session
        historiques = session.query(HistoriqueCellule).all()
        result = []
        for historique in historiques:
            if historique.cellule_id == cellule_id:

                cellule = self.get_cellule_by_id(historique.cellule_id)
                experience = self.get_experience_by_id(historique.cellule_experience_id)
                result.append({"historique": historique, "cellule": cellule, "experience": experience})
        session.commit()
        return result

    def get_experience_of_cellule(self,cellule_id):
        for cellule in self.cellules:
            if cellule.id == cellule_id:
                return self.get_experience_by_id(cellule.experience_id)
        return None
    
    def get_experience_by_id(self,id):
        for experience in self.experiences:
            if experience.id == id :
                return experience
        return None

    def new_experience_of_cellule(self,id_cellule,id_experience):
        global session
        try :
            cellule = self.get_cellule_by_id(id_cellule)
            cellule.experience_id = id_experience
            session.commit()
            return "Mise à jour réussie"
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"
    
    def new_historique(self,id_cellule,id_experience):
        global session
        try:
            new_historique = HistoriqueCellule(cellule_id=id_cellule,cellule_experience_id=id_experience,status="En cours",action="Ajout d'une nouvelle expérience à la cellule")
            session.add(new_historique)
            session.commit()
            return "c'est bon"
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"
    
    def update_historique(self,cellule_id):
        global session
        historiques = session.query(HistoriqueCellule).all()
        try :
            for historique in historiques:
                if historique.cellule_id == cellule_id and historique.status == "En cours":
                    historique.status = "Terminés"
                    session.commit()
            return "mise a jour reussi !"
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"
    




# def get_all_experience():
#     return experiences

# def get_cellule_name_from_id(id_cellule):
#     for cellule in cellules:
#         if cellule.id == id_cellule:
#             return cellule.nom

# def get_cell_by_name(name):
#     for cellule in cellules:
#         if cellule.nom == name:
#             return cellule
#     return None #

# def get_cell_by_id(id_cellule):
#     for cellule in cellules:
#         if cellule.id == id_cellule:
#             return cellule#
        

# def get_experience_avenir_encours():
#     result = []
#     for experience in experiences:
#         if experience.etat_experience == "à venir" or experience.etat_experience == "En cours":
#             result.append(experience)
#     return result#

# def get_experience_by_id(id_experience):
#     try :
#         for experience in experiences:
#             if experience.id == id_experience:
#                 return experience
#     except Exception as e:  
#         print(f"Erreur lors de la récupération de l'expérience par ID : {str(e)}")
#         return None#
    

# def get_historique_by_id(cellule_id):
#     global session
#     historiques = session.query(HistoriqueCellule).all()
#     result = []
#     for historique in historiques:
#         if historique.cellule_id == cellule_id:

#             cellule = get_cell_by_id(historique.cellule_id)
#             experience = get_experience_by_id(historique.cellule_experience_id)
#             result.append({"historique": historique, "cellule": cellule, "experience": experience})
#     session.commit()
#     return result#

# def get_experience_of_cellule(cellule_id):
#     for cellule in cellules:
#         if cellule.id == cellule_id:
#             return get_experience_by_id(cellule.experience_id)
#     return None    #



# def get_experience_by_id(id):
#     for experience in experiences:
#         if experience.id == id :
#             return experience
#     return None #

# def nouvelle_experience_de_cellule(id_cellule,id_experience):
#     global session
#     try :
#         cellule = get_cell_by_id(id_cellule)
#         cellule.experience_id = id_experience
#         session.commit()
#         return "Mise à jour réussie"
#     except Exception as e:
#         return f"Une erreur s'est produite : {str(e)}" #
    
# def nouvelle_historique(id_cellule,id_experience):
    
#     global session
#     try:
#         new_historique = HistoriqueCellule(cellule_id=id_cellule,cellule_experience_id=id_experience,status="En cours",action="Ajout d'une nouvelle expérience à la cellule")
#         session.add(new_historique)
#         session.commit()
#         return "c'est bon"
#     except Exception as e:
#         return f"Une erreur s'est produite : {str(e)}" #
    
# def update_historique(cellule_id):
#     global session
#     historiques = session.query(HistoriqueCellule).all()
#     try :
#         for historique in historiques:
#             if historique.cellule_id == cellule_id and historique.status == "En cours":
#                 historique.status = "Terminés"
#                 session.commit()
#         return "mise a jour reussi !"
#     except Exception as e:
#         return f"Une erreur s'est produite : {str(e)}"
    

octopus = Octopus()


#for cell in experience1.cellules:
    #print(experience1.id,cell.id,cell.nom)