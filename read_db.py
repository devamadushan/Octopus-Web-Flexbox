from conn import session
from Experiences import Experience
from Cellules import Cellule
from Historique import Historique
from sqlalchemy.orm import joinedload
from pprint import pprint

experiences = session.query(Experience).all()
experience1 = experiences[5]




cellules = session.query(Cellule).all() 
historiques = session.query(Historique).all()
def get_cell_by_name(name):
    for cellule in cellules:
        if cellule.nom == name:
            return cellule
    return None



def get_historique_by_id_name(object_id, object_name):
    result = []
    for historique in historiques:
        if historique.object_id == object_id and historique.object_name == object_name:
            result.append(historique)
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

caca = get_historique_by_id_name(1,'Experience')
cell = get_cell_by_name('E2C1')
experience = get_experience_of_cellule(4)

print(experience.nom)

# def cel(idex):
#     cell = cellules['index']
#     return cell



#for cell in experience1.cellules:
    #print(experience1.id,cell.id,cell.nom)