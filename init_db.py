

###################################################################################################

from EcolabWeb import EcolabWeb
from Experiment import Experiment
from Cells import Cells
from History import Historiy_cells
from Connexion import utilisateur,session, password, base_de_donne, port, Base

###################################################################################################

'''Objets des Experiments'''
embl= Experiment(date_debut='2023/12/01' ,nom="EMBL-EXPOCER",status_experiment ="En cours")
gente= Experiment(date_debut='2023/08/01' ,nom="Gente-POP",status_experiment ="En cours")
mang= Experiment(date_debut='2023/09/01' ,nom="MangWarm",status_experiment ="En cours")
b2= Experiment(date_debut='2024/01/01' ,nom="B2",status_experiment ="En cours")
mines= Experiment(date_debut='2023/11/01' ,nom="Mines-Pluie",status_experiment ="En cours")


peace= Experiment(nom="Peace",status_experiment ="à venir")
lysimetre= Experiment(nom="Lysimètre",status_experiment ="à venir")
bacs= Experiment(nom="Bacs à évaporation",status_experiment ="à venir")

sybio= Experiment(nom="Sybio",status_experiment ="à venir")
optisol= Experiment(nom="Optisol",status_experiment ="à venir")
microbe= Experiment(nom="Microbe For",status_experiment ="à venir")
climate= Experiment(nom="Climate",status_experiment ="à venir")
agroserv= Experiment(nom="AgroServ",status_experiment ="à venir")

pasDExperiment = Experiment(nom="pas d'Experiment")

bioteca = Experiment(date_debut='2023/04/01', date_fin='2023/09/01', nom="BIOTECA",status_experiment ="Terminés")
oasis = Experiment(date_debut='2022/10/01', date_fin='2023/01/01', nom="Oasis",status_experiment ="Terminés")
riboStress = Experiment(date_debut='2019/01/01', date_fin='2023/08/01', nom="RiboStress",status_experiment ="Terminés")
aquaOXY = Experiment(date_debut='2023/01/01', date_fin='2023/03/01', nom="AquaOXY",status_experiment ="Terminés")
ehinzode = Experiment(date_debut='2023/02/01', date_fin='2023/09/01', nom="Rhizode",status_experiment ="Terminés")
syvie = Experiment(date_debut='2023/10/01', nom="Syvie",status_experiment ="Terminés")



''' Objetsde Cellss'''
E1C1 = Cells(nom="E1C1", ecolabWeb_id=1, Experiment_id=1)
E1C2 = Cells(nom="E1C2", ecolabWeb_id=1, Experiment_id=2)
E1C3 =Cells(nom="E1C3", ecolabWeb_id=1, Experiment_id=1)

E2C1 = Cells(nom="E2C1", ecolabWeb_id=2, Experiment_id=3)
E2C2 = Cells(nom="E2C2", ecolabWeb_id=2, Experiment_id=3)
E2C3 =Cells(nom="E2C3", ecolabWeb_id=2)

E3C1 = Cells(nom="E3C1", ecolabWeb_id=3, Experiment_id=2)
E3C2 = Cells(nom="E3C2", ecolabWeb_id=3, Experiment_id=2)
E3C3 =Cells(nom="E3C3", ecolabWeb_id=3, Experiment_id=2)

E4C1 = Cells(nom="E4C1",ecolabWeb_id=4)
E4C2 = Cells(nom="E4C2", ecolabWeb_id=4, Experiment_id=3)
E4C3 = Cells(nom="E4C3", ecolabWeb_id=4 ,Experiment_id=3)

E5C1 = Cells(nom="E5C1", ecolabWeb_id=5)
E5C2 = Cells(nom="E5C2", ecolabWeb_id=5)
E5C3 = Cells(nom="E5C3", ecolabWeb_id=5)

E6C1 = Cells(nom="E6C1",ecolabWeb_id=6, Experiment_id=4)
E6C2 = Cells(nom="E6C2", ecolabWeb_id=6,Experiment_id=5)
E6C3 = Cells(nom="E6C3",ecolabWeb_id=6)

Ecolab_1 = EcolabWeb(nom ="Ecolab 1")
Ecolab_2 = EcolabWeb(nom ="Ecolab 2")
Ecolab_3 = EcolabWeb(nom ="Ecolab 3")
Ecolab_4 = EcolabWeb(nom ="Ecolab 4")
Ecolab_5 = EcolabWeb(nom ="Ecolab 5")
Ecolab_6 = EcolabWeb(nom ="Ecolab 6")

'''Objets des historiques des Cellss'''
historique_1 = Historiy_cells(cells_id=4,cells_experiment_id=14)
historique_2 = Historiy_cells(cells_id=5,cells_experiment_id=14, status="Terminér")

historique_3 = Historiy_cells(cells_id=2,cells_experiment_id=15, status="Terminér")

historique_4 = Historiy_cells(cells_id=13,cells_experiment_id=16, status="Terminér")
historique_5 = Historiy_cells(cells_id=14,cells_experiment_id=16, status="Terminér")
historique_6 = Historiy_cells(cells_id=15,cells_experiment_id=16, status="Terminér")

historique_7 = Historiy_cells(cells_id=1,cells_experiment_id=17, status="Terminér")

historique_8 = Historiy_cells(cells_id=1,cells_experiment_id=18, status="Terminér")
historique_9 = Historiy_cells(cells_id=2,cells_experiment_id=18, status="Terminér")
historique_10 = Historiy_cells(cells_id=3,cells_experiment_id=18, status="Terminér")

historique_11 = Historiy_cells(cells_id=6,cells_experiment_id=19, status="Terminér")

historique_12 = Historiy_cells(cells_id=1,cells_experiment_id=1, status="En cours")
historique_13 = Historiy_cells(cells_id=3,cells_experiment_id=1, status="En cours")

historique_14 = Historiy_cells(cells_id=2,cells_experiment_id=2, status="En cours")
historique_15 = Historiy_cells(cells_id=7,cells_experiment_id=2, status="En cours")
historique_16 = Historiy_cells(cells_id=8,cells_experiment_id=2, status="En cours")
historique_17 = Historiy_cells(cells_id=9,cells_experiment_id=2, status="En cours")

historique_18 = Historiy_cells(cells_id=4,cells_experiment_id=3, status="En cours")
historique_19 = Historiy_cells(cells_id=5,cells_experiment_id=3, status="En cours")
historique_20 = Historiy_cells(cells_id=11,cells_experiment_id=3, status="En cours")
historique_21 = Historiy_cells(cells_id=12,cells_experiment_id=3, status="En cours")

historique_22 = Historiy_cells(cells_id=16,cells_experiment_id=4, status="En cours")

historique_23 = Historiy_cells(cells_id=17,cells_experiment_id=5, status="En cours")


'''Historique'''
session.add_all([historique_1,historique_2,historique_3,historique_4,historique_5,historique_6,historique_7,historique_8,historique_9,historique_10,historique_11,historique_12,historique_13,historique_14,historique_15,historique_16,historique_17,historique_18,historique_19,historique_20,historique_21,historique_22,historique_23])

#session.add(historique_1)
'''Cellss'''
#session.add_all([E1C1,E1C2,E1C3,E2C1,E2C2,E2C3,E3C1,E3C2,E3C3,E4C1,E4C2,E4C3,E5C1,E5C2,E5C3,E6C1,E6C2,E6C3])

'''Experiment'''
#session.add_all([embl, gente, mang, b2, mines, peace, lysimetre, bacs, sybio, optisol, microbe, climate, agroserv, bioteca, oasis, riboStress, aquaOXY, ehinzode, syvie])

'''Ecolab'''
#session.add_all([Ecolab_1,Ecolab_2,Ecolab_3,Ecolab_4,Ecolab_5,Ecolab_6])

session.commit()



    

