

###################################################################################################


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Ecolab import Ecolab
from Experiences import Experience
from Cellules import Cellule
from Historique import HistoriqueCellule
from conn import utilisateur,session, password, base_de_donne, port, Base

###################################################################################################

'''Objets des experiences'''
embl= Experience(date_debut='2023/12/01' ,nom="EMBL-EXPOCER",status="En cours")
gente= Experience(date_debut='2023/08/01' ,nom="Gente-POP",status="En cours")
mang= Experience(date_debut='2023/09/01' ,nom="MangWarm",status="En cours")
b2= Experience(date_debut='2024/01/01' ,nom="B2",status="En cours")
mines= Experience(date_debut='2023/11/01' ,nom="Mines-Pluie",status="En cours")


peace= Experience(nom="Peace",status="à venir")
lysimetre= Experience(nom="Lysimètre",status="à venir")
bacs= Experience(nom="Bacs à évaporation",status="à venir")

sybio= Experience(nom="Sybio",status="à venir")
optisol= Experience(nom="Optisol",status="à venir")
microbe= Experience(nom="Microbe For",status="à venir")
climate= Experience(nom="Climate",status="à venir")
agroserv= Experience(nom="AgroServ",status="à venir")


bioteca = Experience(date_debut='2023/04/01', date_fin='2023/09/01', nom="BIOTECA",status="Terminés")
oasis = Experience(date_debut='2022/10/01', date_fin='2023/01/01', nom="Oasis",status="Terminés")
riboStress = Experience(date_debut='2019/01/01', date_fin='2023/08/01', nom="RiboStress",status="Terminés")
aquaOXY = Experience(date_debut='2023/01/01', date_fin='2023/03/01', nom="AquaOXY",status="Terminés")
ehinzode = Experience(date_debut='2023/02/01', date_fin='2023/09/01', nom="Rhizode",status="Terminés")
syvie = Experience(date_debut='2023/10/01', nom="Syvie",status="Terminés")



''' Objetsde Cellules'''
E1C1 = Cellule(nom="E1C1", ecolab_id=1, experience_id=1)
E1C2 = Cellule(nom="E1C2", ecolab_id=1, experience_id=2)
E1C3 =Cellule(nom="E1C3", ecolab_id=1, experience_id=1)

E2C1 = Cellule(nom="E2C1", ecolab_id=2, experience_id=3)
E2C2 = Cellule(nom="E2C2", ecolab_id=2, experience_id=3)
E2C3 =Cellule(nom="E2C3", ecolab_id=2)

E3C1 = Cellule(nom="E3C1", ecolab_id=3, experience_id=2)
E3C2 = Cellule(nom="E3C2", ecolab_id=3, experience_id=2)
E3C3 =Cellule(nom="E3C3", ecolab_id=3, experience_id=2)

E4C1 = Cellule(nom="E4C1",ecolab_id=4)
E4C2 = Cellule(nom="E4C2", ecolab_id=4, experience_id=3)
E4C3 = Cellule(nom="E4C3", ecolab_id=4 ,experience_id=3)

E5C1 = Cellule(nom="E5C1", ecolab_id=5)
E5C2 = Cellule(nom="E5C2", ecolab_id=5)
E5C3 = Cellule(nom="E5C3", ecolab_id=5)

E6C1 = Cellule(nom="E6C1",ecolab_id=6, experience_id=4)
E6C2 = Cellule(nom="E6C2", ecolab_id=6,experience_id=5)
E6C3 = Cellule(nom="E6C3",ecolab_id=6)

Ecolab_1 = Ecolab(nom ="Ecolab 1")
Ecolab_2 = Ecolab(nom ="Ecolab 2")
Ecolab_3 = Ecolab(nom ="Ecolab 3")
Ecolab_4 = Ecolab(nom ="Ecolab 4")
Ecolab_5 = Ecolab(nom ="Ecolab 5")
Ecolab_6 = Ecolab(nom ="Ecolab 6")

'''Objets des historiques des cellules'''
historique_1 = HistoriqueCellule(cellule_id=4,cellule_experience_id=14)
historique_2 = HistoriqueCellule(cellule_id=5,cellule_experience_id=14)

historique_3 = HistoriqueCellule(cellule_id=2,cellule_experience_id=15)

historique_4 = HistoriqueCellule(cellule_id=13,cellule_experience_id=16)
historique_5 = HistoriqueCellule(cellule_id=14,cellule_experience_id=16)
historique_6 = HistoriqueCellule(cellule_id=15,cellule_experience_id=16)

historique_7 = HistoriqueCellule(cellule_id=1,cellule_experience_id=17)

historique_8 = HistoriqueCellule(cellule_id=1,cellule_experience_id=18)
historique_9 = HistoriqueCellule(cellule_id=2,cellule_experience_id=18)
historique_10 = HistoriqueCellule(cellule_id=3,cellule_experience_id=18)

historique_11 = HistoriqueCellule(cellule_id=6,cellule_experience_id=19)

historique_12 = HistoriqueCellule(cellule_id=1,cellule_experience_id=1)
historique_13 = HistoriqueCellule(cellule_id=3,cellule_experience_id=1)

historique_14 = HistoriqueCellule(cellule_id=2,cellule_experience_id=2)
historique_15 = HistoriqueCellule(cellule_id=7,cellule_experience_id=2)
historique_16 = HistoriqueCellule(cellule_id=8,cellule_experience_id=2)
historique_17 = HistoriqueCellule(cellule_id=9,cellule_experience_id=2)

historique_18 = HistoriqueCellule(cellule_id=4,cellule_experience_id=3)
historique_19 = HistoriqueCellule(cellule_id=5,cellule_experience_id=3)
historique_20 = HistoriqueCellule(cellule_id=11,cellule_experience_id=3)
historique_21 = HistoriqueCellule(cellule_id=12,cellule_experience_id=3)

historique_22 = HistoriqueCellule(cellule_id=16,cellule_experience_id=4)

historique_23 = HistoriqueCellule(cellule_id=17,cellule_experience_id=5)


'''Historique'''
##session.add_all([historique_1,historique_2,historique_3,historique_4,historique_5,historique_6,historique_7,historique_8,historique_9,historique_10,historique_11,historique_12,historique_13,historique_14,historique_15,historique_16,historique_17,historique_18,historique_19,historique_20,historique_21,historique_22,historique_23])


'''Cellules'''
#session.add_all([E1C1,E1C2,E1C3,E2C1,E2C2,E2C3,E3C1,E3C2,E3C3,E4C1,E4C2,E4C3,E5C1,E5C2,E5C3,E6C1,E6C2,E6C3])

'''Experience'''
#session.add_all([embl, gente, mang, b2, mines, peace, lysimetre, bacs, sybio, optisol, microbe, climate, agroserv, bioteca, oasis, riboStress, aquaOXY, ehinzode, syvie])

'''Ecolab'''
#session.add_all([Ecolab_1,Ecolab_2,Ecolab_3,Ecolab_4,Ecolab_5,Ecolab_6])

session.commit()



    

