from conn import session
from Experiences import Experience
from Cellules import Cellule

experiences = session.query(Experience).all()
experience1 = experiences[5]

cellules = session.query(Cellule).all() 

def get_cell_by_name(name):
    for cellule in cellules:
        if cellule.nom == name:
            return cellule
    return None

cell = get_cell_by_name('E2C1')


print(cell.experience_id)

# def cel(idex):
#     cell = cellules['index']
#     return cell



#for cell in experience1.cellules:
    #print(experience1.id,cell.id,cell.nom)