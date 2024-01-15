from conn import session
from Experiences import Experience
from Cellules import Cellule
from Historique import HistoriqueCellule
from sqlalchemy.orm import joinedload
from pprint import pprint

experiences = session.query(Experience).all()
experience1 = experiences[5]
cellules = session.query(Cellule).all() 
historiques = session.query(HistoriqueCellule).all()

def get_all_experience():
    return experiences

def get_cell_by_name(name):
    for cellule in cellules:
        if cellule.nom == name:
            return cellule
    return None

def get_cell_by_id(id_cellule):
    for cellule in cellules:
        if cellule.id == id_cellule:
            return cellule

def get_experience_avenir():
    result = []
    for experience in experiences:
        if experience.status == "à venir":
            result.append(experience)
    return result

def get_experience_by_id(id_experience):
    try :
        for experience in experiences:
            if experience.id == id_experience:
                return experience
    except Exception as e:  
        print(f"Erreur lors de la récupération de l'expérience par ID : {str(e)}")
        return None
    

def get_historique_by_id(cellule_id):
    result = []
    for historique in historiques:
        if historique.cellule_id == cellule_id:

            cellule = get_cell_by_id(historique.cellule_id)
            experience = get_experience_by_id(historique.cellule_experience_id)
            #print("jnioeff,klf,erl,kl,flnfjklrn",cellule)
            result.append({"historique": historique, "cellule": cellule, "experience": experience})
    return result

def get_experience_of_cellule(cellule_id):
    for cellule in cellules:
        if cellule.id == cellule_id:
            return get_experience_by_id(cellule.experience_id)
    return None    



def get_experience_by_id(id):
    for experience in experiences:
        if experience.id == id :
            return experience
    return None

def nouvelle_experience_de_cellule(id_cellule,id_experience):
    global session
    try :
        cellule = get_cell_by_id(id_cellule)
        cellule.experience_id = id_experience
        session.commit()
        return "Mise à jour réussie"
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"
    
def nouvelle_historique(id_cellule,id_experience):
    global session
    try:
        new_historique = HistoriqueCellule(cellule_id=id_cellule,cellule_experience_id=id_experience,action="Ajout d'une nouvelle Experience dans la cellule")
        session.add(new_historique)
        session.commit()
        return "c'est bon"
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"
    
#def update_experience():

    

#cell = nouvelle_historique(18,20)
#print(cell)
#print(blabla)
# def cel(idex):
#     cell = cellules['index']
#     return cell



#for cell in experience1.cellules:
    #print(experience1.id,cell.id,cell.nom)